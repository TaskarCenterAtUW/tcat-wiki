#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Link Checker
# Version: 3.3.0
# Date: 2026-01-02
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Link validation script for the TCAT Wiki

.DESCRIPTION
    Checks all .md files in the docs directory for broken internal and external links.

.PARAMETER internal
    Check internal relative links

.PARAMETER external
    Check external absolute links

.EXAMPLE
    .\check-links.ps1
    Validates both internal and external links

.EXAMPLE
    .\check-links.ps1 -internal
    Validates only internal relative links
#>

param(
    [Parameter(HelpMessage = "Check external links")]
    [switch]$external,
    
    [Parameter(HelpMessage = "Check internal links")]
    [switch]$internal
)

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
$externalUrlCache = @{}
$brokenExternalLinks = @()
$brokenInternalLinks = @()

#region Helper Functions

# Function to extract links from markdown content
function Get-MarkdownLinks {
    param([string]$content)
    
    # Remove code blocks (``` ... ```) to avoid extracting links from code examples
    $contentWithoutCodeBlocks = $content -replace '```[\s\S]*?```', ''
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
            'User-Agent' = 'TCAT-Wiki-LinkChecker/3.3.0 (+https://github.com/TaskarCenterAtUW/tcat-wiki)'
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

#endregion Helper Functions

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
if ($external) {
    Write-Host ""
    Write-Host "Validating $($externalUrls.Count) unique external URLs..." -ForegroundColor Cyan

    foreach ($url in $externalUrls.Keys | Sort-Object) {
        Write-Host "Testing: $url" -ForegroundColor Gray
        
        # Check cache first
        if ($externalUrlCache.ContainsKey($url)) {
            $result = $externalUrlCache[$url]
        } else {
            $result = Test-ExternalUrlValid -url $url
            $externalUrlCache[$url] = $result
        }
        
        if (-not $result.valid) {
            if ($result.isTimeout) {
                # Timeout - track as warning, not failure
                $timeoutWarnings += @{
                    url    = $url
                    status = $result.status
                }
                Write-Host "  [!] Timeout: $($result.status)" -ForegroundColor Yellow
            } else {
                # Actual broken link
                $brokenExternalLinks += @{
                    url    = $url
                    status = $result.status
                }
                Write-Host "  [X] Failed: $($result.status)" -ForegroundColor Red
            }
        } else {
            Write-Host "  [OK] OK: $($result.status)" -ForegroundColor Green
        }
        
        Start-Sleep -Milliseconds 100  # Be nice to servers
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
