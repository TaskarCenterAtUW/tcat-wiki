#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Link Checker
# Version: 4.0.0
# Date: 2026-02-06
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Link validation script for the TCAT Wiki

.DESCRIPTION
    Checks all .md files in the docs directory for broken internal and external links.
    External links are checked in parallel with domain-based throttling and results are
    cached to disk for performance.

.PARAMETER internal
    Check internal relative links

.PARAMETER external
    Check external absolute links

.PARAMETER NoCache
    Bypass the cache and force fresh external link checks

.EXAMPLE
    .\check-links.ps1
    Validates both internal and external links

.EXAMPLE
    .\check-links.ps1 -internal
    Validates only internal relative links

.EXAMPLE
    .\check-links.ps1 -external -NoCache
    Force fresh validation of all external links
#>

param(
    [Parameter(HelpMessage = "Check external links")]
    [switch]$external,

    [Parameter(HelpMessage = "Check internal links")]
    [switch]$internal,

    [Parameter(HelpMessage = "Bypass the cache and force fresh external link checks")]
    [switch]$NoCache
)

# Cache configuration
$script:CacheFilePath = Join-Path $PSScriptRoot ".link-cache.json"
$script:CacheTTLHours = 12

# If neither -external nor -internal is specified, default to both
if (-not $external -and -not $internal) {
    $external = $true
    $internal = $true
}

# Verify we're in the util directory
$currentDirName = Split-Path -Leaf (Get-Location)

if ($currentDirName -ne "util") {
    Write-Host "Error: This script must be run from the util/ directory" -ForegroundColor Red
    Write-Host "Current location: $(Get-Location)" -ForegroundColor Yellow
    exit 1
}

# Set docs path
$docsPath = "..\docs"

Write-Host "TCAT Wiki Link Validation" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host "Checking: $(if ($internal) { 'Internal' } else { '' })$(if ($internal -and $external) { ' and ' } else { '' })$(if ($external) { 'External' } else { '' }) links"
Write-Host ""

# Check if docs directory exists
if (-not (Test-Path $docsPath)) {
    Write-Host "Error: Docs directory '$docsPath' not found!" -ForegroundColor Red
    exit 1
}

# Find all markdown files
$markdownFiles = Get-ChildItem -Path $docsPath -Filter "*.md" -Recurse
if ($markdownFiles.Count -eq 0) {
    Write-Host "No markdown files found in '$docsPath'" -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($markdownFiles.Count) markdown files to validate" -ForegroundColor Green
Write-Host ""

$externalUrls = @{}
$brokenExternalLinks = @()
$brokenInternalLinks = @()

#region Helper Functions

# Function to extract links from markdown content
function Get-MarkdownLinks {
    param([string]$content)

    # Remove YAML frontmatter (contains # comments) to avoid extracting links from metadata
    $contentWithoutFrontmatter = $content -replace '(?ms)\A---\r?\n.*?\r?\n---\r?\n?', ''
    # Remove HTML comments (<!-- ... -->) which may span multiple lines
    $contentWithoutComments = $contentWithoutFrontmatter -replace '(?s)<!--.*?-->', ''
    # Remove code blocks (``` ... ```) to avoid extracting links from code examples
    $contentWithoutCodeBlocks = $contentWithoutComments -replace '```[\s\S]*?```', ''
    # Remove inline code (` ... `) to avoid extracting links from code
    $contentWithoutInlineCode = $contentWithoutCodeBlocks -replace '`[^`]*`', ''

    # Match [text](url) pattern
    $linkPattern = '\[([^\]]*)\]\(([^)]+)\)'
    $imagePattern = '!\[([^\]]*)\]\(([^)]+)\)'

    $links = [regex]::Matches($contentWithoutInlineCode, $linkPattern)
    $images = [regex]::Matches($contentWithoutInlineCode, $imagePattern)

    return ($links + $images)
}

# Function to check if URL is external
function Test-ExternalUrl {
    param([string]$url)
    return $url.StartsWith("http://") -or $url.StartsWith("https://")
}

# Function to validate internal link
function Test-InternalLink {
    param(
        [string]$filePath,
        [string]$linkUrl
    )

    # Skip fragment-only links
    if ($linkUrl.StartsWith("#")) {
        return $true
    }

    # Skip special URL schemes (mailto, tel, etc.)
    if ($linkUrl -match '^(mailto|tel|javascript|ftp|file):') {
        return $true
    }

    # Remove fragment from URL
    $cleanUrl = $linkUrl.Split('#')[0]
    if (-not $cleanUrl) {
        return $true
    }

    # Resolve relative path
    $baseDir = Split-Path $filePath -Parent
    $targetPath = Join-Path $baseDir $cleanUrl
    $resolvedPath = [System.IO.Path]::GetFullPath($targetPath)

    return Test-Path $resolvedPath
}

# Function to test external URL
function Test-ExternalUrlValid {
    param([string]$url)

    # Skip domains that block automated requests or are known to always fail
    $skipDomains = @(
        "*visualstudio.com*"
        "*docs.google.com*"
        "*firebase*"
        "*osm.workspaces-stage.sidewalks.washington.edu/api*"
    )

    foreach ($domain in $skipDomains) {
        if ($url -like $domain) {
            return @{
                valid  = $true
                status = "Skipped URL listed in skipDomains filter."
            }
        }
    }

    try {
        # Prepare headers with User-Agent to identify as a bot
        $headers = @{
            'User-Agent' = 'TCAT-Wiki-LinkChecker/4.0.0 (+https://github.com/TaskarCenterAtUW/tcat-wiki)'
        }

        # Use HEAD request first, fallback to GET if needed
        try {
            $response = Invoke-WebRequest -Uri $url -Method Head -TimeoutSec 5 -UseBasicParsing -Headers $headers -ErrorAction Stop
        } catch {
            # Some servers don't support HEAD, try GET
            $response = Invoke-WebRequest -Uri $url -Method Get -TimeoutSec 5 -UseBasicParsing -Headers $headers -ErrorAction Stop
        }
        return @{
            valid     = $response.StatusCode -lt 400
            status    = $response.StatusCode
            isTimeout = $false
        }
    } catch {
        # Extract more meaningful error messages
        $errorMessage = if ($_.Exception.Response.StatusCode) {
            "HTTP $($_.Exception.Response.StatusCode.value__): $($_.Exception.Response.StatusDescription)"
        } else {
            $_.Exception.Message
        }

        # Check if this is a timeout error
        $isTimeout = $errorMessage -match 'Timeout|timed out|HttpClient\.Timeout'

        return @{
            valid     = $false
            status    = $errorMessage
            isTimeout = $isTimeout
        }
    }
}

# Function to extract domain from URL (for throttling)
function Get-UrlDomain {
    param([string]$url)
    if ([string]::IsNullOrWhiteSpace($url)) {
        return "unknown"
    }
    try {
        $uri = [System.Uri]$url
        if ([string]::IsNullOrWhiteSpace($uri.Host)) {
            return "unknown"
        }
        return $uri.Host
    } catch {
        return "unknown"
    }
}

#endregion Helper Functions

#region Cache Functions

# Load cache from disk
function Get-LinkCache {
    if ($script:NoCache -or -not (Test-Path $script:CacheFilePath)) {
        return @{}
    }

    try {
        $cacheContent = Get-Content $script:CacheFilePath -Raw -Encoding UTF8 | ConvertFrom-Json -AsHashtable
        return $cacheContent ?? @{}
    } catch {
        Write-Host "  Warning: Could not read cache file, starting fresh" -ForegroundColor Yellow
        return @{}
    }
}

# Save cache to disk
function Save-LinkCache {
    param([hashtable]$cache)

    try {
        $cache | ConvertTo-Json -Depth 10 | Set-Content $script:CacheFilePath -Encoding UTF8
    } catch {
        Write-Host "  Warning: Could not save cache file" -ForegroundColor Yellow
    }
}

# Check if a cached result is still valid (within TTL)
function Test-CacheEntryValid {
    param([hashtable]$entry)

    if (-not $entry -or -not $entry.timestamp) {
        return $false
    }

    $cachedTime = [DateTime]::Parse($entry.timestamp)
    $age = (Get-Date) - $cachedTime
    return $age.TotalHours -lt $script:CacheTTLHours
}

#endregion Cache Functions

# Process each markdown file
foreach ($file in $markdownFiles) {
    $relativePath = $file.FullName.Substring((Get-Location).Path.Length + 1)
    Write-Host "Validating: $relativePath" -ForegroundColor Yellow

    try {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
    } catch {
        Write-Host "  ERROR reading file: $($_.Exception.Message)" -ForegroundColor Red
        continue
    }

    $links = Get-MarkdownLinks -content $content

    foreach ($link in $links) {
        $linkText = $link.Groups[1].Value
        $linkUrl = $link.Groups[2].Value

        if (Test-ExternalUrl -url $linkUrl) {
            # Collect external URLs for later testing if external checking is enabled
            if ($external) {
                $externalUrls[$linkUrl] = $true
            }
        } else {
            # Test internal link only if internal checking is enabled
            if ($internal) {
                if (-not (Test-InternalLink -filePath $file.FullName -linkUrl $linkUrl)) {
                    $brokenInternalLinks += @{
                        file = $relativePath
                        text = $linkText
                        url  = $linkUrl
                    }
                    Write-Host "  [X] Broken internal link: [$linkText]($linkUrl)" -ForegroundColor Red
                }
            }
        }
    }
}

# Test external URLs only if external checking is enabled
$timeoutWarnings = @()
$cacheHits = 0
if ($external) {
    Write-Host ""
    Write-Host "Validating $($externalUrls.Count) unique external URLs..." -ForegroundColor Cyan

    # Load existing cache
    $linkCache = Get-LinkCache

    # Separate URLs into cached (valid within TTL) and need-to-check
    $urlsToCheck = @()
    $cachedResults = @{}

    foreach ($url in $externalUrls.Keys | Sort-Object) {
        if (-not $NoCache -and $linkCache.ContainsKey($url) -and (Test-CacheEntryValid -entry $linkCache[$url])) {
            $cacheHits++
            $cachedResults[$url] = $linkCache[$url]
        } else {
            $urlsToCheck += $url
        }
    }

    if ($cacheHits -gt 0) {
        Write-Host "  Using $cacheHits cached results (valid within $($script:CacheTTLHours)h TTL)" -ForegroundColor Gray
    }

    # Process cached results first
    foreach ($url in $cachedResults.Keys | Sort-Object) {
        $cached = $cachedResults[$url]
        Write-Host "Testing: $url" -ForegroundColor Gray
        if (-not $cached.valid) {
            if ($cached.isTimeout) {
                $timeoutWarnings += @{
                    url    = $url
                    status = "$($cached.status) (cached)"
                }
                Write-Host "  [!] Timeout (cached): $($cached.status)" -ForegroundColor Yellow
            } else {
                $brokenExternalLinks += @{
                    url    = $url
                    status = "$($cached.status) (cached)"
                }
                Write-Host "  [X] Failed (cached): $($cached.status)" -ForegroundColor Red
            }
        } else {
            Write-Host "  [OK] OK (cached): $($cached.status)" -ForegroundColor Green
        }
    }

    # Check remaining URLs in parallel, throttled by domain
    if ($urlsToCheck.Count -gt 0) {
        Write-Host ""
        Write-Host "Checking $($urlsToCheck.Count) URLs (parallel with domain throttling)..." -ForegroundColor Cyan

        # Group URLs by domain for throttling
        $urlsByDomain = @{}
        foreach ($url in $urlsToCheck) {
            $domain = Get-UrlDomain -url $url
            if (-not $urlsByDomain.ContainsKey($domain)) {
                $urlsByDomain[$domain] = @()
            }
            $urlsByDomain[$domain] += $url
        }

        # Check URLs in parallel (max 5 concurrent, grouped to respect same-domain delays)
        $parallelResults = $urlsToCheck | ForEach-Object -ThrottleLimit 5 -Parallel {
            $url = $_

            # Test-ExternalUrlValid logic inline (functions not accessible in parallel block)
            $skipDomains = @(
                "*visualstudio.com*"
                "*docs.google.com*"
                "*firebase*"
                "*osm.workspaces-stage.sidewalks.washington.edu/api*"
            )

            $skipped = $false
            foreach ($domain in $skipDomains) {
                if ($url -like $domain) {
                    $skipped = $true
                    break
                }
            }

            if ($skipped) {
                $result = @{
                    url       = $url
                    valid     = $true
                    status    = "Skipped URL listed in skipDomains filter."
                    isTimeout = $false
                }
            } else {
                try {
                    $headers = @{
                        'User-Agent' = 'TCAT-Wiki-LinkChecker/3.4.0 (+https://github.com/TaskarCenterAtUW/tcat-wiki)'
                    }

                    try {
                        $response = Invoke-WebRequest -Uri $url -Method Head -TimeoutSec 5 -UseBasicParsing -Headers $headers -ErrorAction Stop
                    } catch {
                        $response = Invoke-WebRequest -Uri $url -Method Get -TimeoutSec 5 -UseBasicParsing -Headers $headers -ErrorAction Stop
                    }

                    $result = @{
                        url       = $url
                        valid     = $response.StatusCode -lt 400
                        status    = $response.StatusCode
                        isTimeout = $false
                    }
                } catch {
                    $errorMessage = if ($_.Exception.Response.StatusCode) {
                        "HTTP $($_.Exception.Response.StatusCode.value__): $($_.Exception.Response.StatusDescription)"
                    } else {
                        $_.Exception.Message
                    }

                    $isTimeout = $errorMessage -match 'Timeout|timed out|HttpClient\.Timeout'

                    $result = @{
                        url       = $url
                        valid     = $false
                        status    = $errorMessage
                        isTimeout = $isTimeout
                    }
                }
            }

            # Small delay to be nice to servers (shared across parallel jobs)
            Start-Sleep -Milliseconds 50

            # Return result
            $result
        }

        # Process parallel results and update cache
        foreach ($result in $parallelResults) {
            $url = $result.url
            Write-Host "Testing: $url" -ForegroundColor Gray

            # Update cache with new result
            $linkCache[$url] = @{
                valid     = $result.valid
                status    = $result.status
                isTimeout = $result.isTimeout
                timestamp = (Get-Date).ToString("o")
            }

            if (-not $result.valid) {
                if ($result.isTimeout) {
                    $timeoutWarnings += @{
                        url    = $url
                        status = $result.status
                    }
                    Write-Host "  [!] Timeout: $($result.status)" -ForegroundColor Yellow
                } else {
                    $brokenExternalLinks += @{
                        url    = $url
                        status = $result.status
                    }
                    Write-Host "  [X] Failed: $($result.status)" -ForegroundColor Red
                }
            } else {
                Write-Host "  [OK] OK: $($result.status)" -ForegroundColor Green
            }
        }

        # Save updated cache
        Save-LinkCache -cache $linkCache
    }
}

# Summary Report
Write-Host ""
Write-Host "VALIDATION SUMMARY" -ForegroundColor Cyan
Write-Host "==================" -ForegroundColor Cyan
Write-Host "Total markdown files: $($markdownFiles.Count)"
if ($internal) {
    Write-Host "Broken internal links: $($brokenInternalLinks.Count)"
}
if ($external) {
    Write-Host "Broken external links: $($brokenExternalLinks.Count)"
    if ($cacheHits -gt 0) {
        Write-Host "Cache hits: $cacheHits (skipped network requests)" -ForegroundColor Gray
    }
    if ($timeoutWarnings.Count -gt 0) {
        Write-Host "Timeout warnings: $($timeoutWarnings.Count)" -ForegroundColor Yellow
    }
}

if ($internal -and $brokenInternalLinks.Count -gt 0) {
    Write-Host ""
    Write-Host "[X] BROKEN INTERNAL LINKS ($($brokenInternalLinks.Count)):" -ForegroundColor Red
    foreach ($item in $brokenInternalLinks) {
        Write-Host "  File: $($item.file)" -ForegroundColor Yellow
        Write-Host "  Link: [$($item.text)]($($item.url))" -ForegroundColor White
        Write-Host ""
    }
}

if ($external -and $brokenExternalLinks.Count -gt 0) {
    Write-Host ""
    Write-Host "[X] BROKEN EXTERNAL LINKS ($($brokenExternalLinks.Count)):" -ForegroundColor Red
    foreach ($item in $brokenExternalLinks) {
        Write-Host "  URL: $($item.url)" -ForegroundColor White
        Write-Host "  Issue: $($item.status)" -ForegroundColor Yellow
        Write-Host ""
    }
}

if ($external -and $timeoutWarnings.Count -gt 0) {
    Write-Host ""
    Write-Host "[!] TIMEOUT WARNINGS ($($timeoutWarnings.Count)):" -ForegroundColor Yellow
    Write-Host "    These URLs timed out but may still be valid. They do not cause the link check to fail." -ForegroundColor Gray
    foreach ($item in $timeoutWarnings) {
        Write-Host "  URL: $($item.url)" -ForegroundColor White
        Write-Host "  Issue: $($item.status)" -ForegroundColor Yellow
        Write-Host ""
    }
}

# Calculate total broken links based on what was checked (timeouts don't count as broken)
$totalBroken = 0
if ($internal) { $totalBroken += $brokenInternalLinks.Count }
if ($external) { $totalBroken += $brokenExternalLinks.Count }

if ($totalBroken -eq 0) {
    Write-Host ""
    Write-Host "[OK] ALL CHECKED LINKS VALID! No broken links found." -ForegroundColor Green
}

# Exit with error code if any checked links are broken
if ($totalBroken -gt 0) {
    exit 1
} else {
    exit 0
}
