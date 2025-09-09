#!/usr/bin/env powershell
<#
.SYNOPSIS
    Link validation script for TCAT Wiki documentation

.DESCRIPTION
    Checks all .md files in the specified directory for broken internal and external links.
    Returns exit code 0 if all links are valid, 1 if any links are broken.

.PARAMETER docsPath
    Path to the documentation directory to scan (default: "docs")

.PARAMETER verboseOutput
    Show verbose output during validation

.EXAMPLE
    .\check-links.ps1
    Validates links in the default "docs" directory

.EXAMPLE
    .\check-links.ps1 -docsPath "documentation" -verboseOutput
    Validates links in "documentation" directory with verbose output
#>

param(
    [Parameter(HelpMessage = "Path to the documentation directory")]
    [string]$docsPath = "..\docs",
    
    [Parameter(HelpMessage = "Show verbose output")]
    [switch]$verboseOutput
)

Write-Host "TCAT Wiki Link Validation" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
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

$brokenInternalLinks = @()
$brokenExternalLinks = @()
$externalUrls = @{}

# Function to extract links from markdown content
function Get-MarkdownLinks {
    param([string]$content)
    
    # Match [text](url) pattern
    $linkPattern = '\[([^\]]*)\]\(([^)]+)\)'
    $imagePattern = '!\[([^\]]*)\]\(([^)]+)\)'
    
    $links = [regex]::Matches($content, $linkPattern)
    $images = [regex]::Matches($content, $imagePattern)
    
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
    
    # Skip known problematic domains that block automated requests
    $skipDomains = @(
        "*visualstudio.com*"
    )
    
    foreach ($domain in $skipDomains) {
        if ($url -like $domain) {
            return @{
                valid  = $true
                status = "Skipped (known to block automated requests)"
            }
        }
    }
    
    try {
        # Use HEAD request first, fallback to GET if needed
        try {
            $response = Invoke-WebRequest -Uri $url -Method Head -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
        }
        catch {
            # Some servers don't support HEAD, try GET
            $response = Invoke-WebRequest -Uri $url -Method Get -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
        }
        return @{
            valid  = $response.StatusCode -lt 400
            status = $response.StatusCode
        }
    }
    catch {
        # Extract more meaningful error messages
        $errorMessage = if ($_.Exception.Response.StatusCode) {
            "HTTP $($_.Exception.Response.StatusCode.value__): $($_.Exception.Response.StatusDescription)"
        }
        else {
            $_.Exception.Message
        }
        
        return @{
            valid  = $false
            status = $errorMessage
        }
    }
}

# Process each markdown file
foreach ($file in $markdownFiles) {
    $relativePath = $file.FullName.Substring((Get-Location).Path.Length + 1)
    if ($verboseOutput) {
        Write-Host "Validating: $relativePath" -ForegroundColor Yellow
    }
    
    try {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
    }
    catch {
        Write-Host "  ERROR reading file: $($_.Exception.Message)" -ForegroundColor Red
        continue
    }
    
    $links = Get-MarkdownLinks -content $content
    
    foreach ($link in $links) {
        $linkText = $link.Groups[1].Value
        $linkUrl = $link.Groups[2].Value
        
        if (Test-ExternalUrl -url $linkUrl) {
            # Collect external URLs for later testing
            $externalUrls[$linkUrl] = $true
        }
        else {
            # Test internal link
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

# Test external URLs
Write-Host ""
Write-Host "Validating $($externalUrls.Count) unique external URLs..." -ForegroundColor Cyan

foreach ($url in $externalUrls.Keys | Sort-Object) {
    if ($verboseOutput) {
        Write-Host "Testing: $url" -ForegroundColor Gray
    }
    
    $result = Test-ExternalUrlValid -url $url
    
    if (-not $result.valid) {
        $brokenExternalLinks += @{
            url    = $url
            status = $result.status
        }
        Write-Host "  [X] Failed: $($result.status)" -ForegroundColor Red
    }
    else {
        if ($verboseOutput) {
            Write-Host "  [OK] OK: $($result.status)" -ForegroundColor Green
        }
    }
    
    Start-Sleep -Milliseconds 500  # Be nice to servers
}

# Summary Report
Write-Host ""
Write-Host "VALIDATION SUMMARY" -ForegroundColor Cyan
Write-Host "==================" -ForegroundColor Cyan
Write-Host "Total markdown files: $($markdownFiles.Count)"
Write-Host "Broken internal links: $($brokenInternalLinks.Count)"
Write-Host "Broken external links: $($brokenExternalLinks.Count)"

if ($brokenInternalLinks.Count -gt 0) {
    Write-Host ""
    Write-Host "[X] BROKEN INTERNAL LINKS ($($brokenInternalLinks.Count)):" -ForegroundColor Red
    foreach ($item in $brokenInternalLinks) {
        Write-Host "  File: $($item.file)" -ForegroundColor Yellow
        Write-Host "  Link: [$($item.text)]($($item.url))" -ForegroundColor White
        Write-Host ""
    }
}

if ($brokenExternalLinks.Count -gt 0) {
    Write-Host ""
    Write-Host "[X] BROKEN EXTERNAL LINKS ($($brokenExternalLinks.Count)):" -ForegroundColor Red
    foreach ($item in $brokenExternalLinks) {
        Write-Host "  URL: $($item.url)" -ForegroundColor White
        Write-Host "  Issue: $($item.status)" -ForegroundColor Yellow
        Write-Host ""
    }
}

if ($brokenInternalLinks.Count -eq 0 -and $brokenExternalLinks.Count -eq 0) {
    Write-Host ""
    Write-Host "[OK] ALL LINKS VALID! No broken links found." -ForegroundColor Green
}

# Exit with error code if any links are broken
if ($brokenInternalLinks.Count -gt 0 -or $brokenExternalLinks.Count -gt 0) {
    exit 1
}
else {
    exit 0
}
