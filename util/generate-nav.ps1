#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Navigation Section Generator
# Version: 2.0.0
# Date: 2025-10-29
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Generates and updates the MkDocs nav structure in mkdocs.yml

.DESCRIPTION
    Scans the docs directory structure and updates the navigation section 
    in mkdocs.yml. Uses frontmatter titles when available, otherwise derives 
    titles from filenames and directory names.

.EXAMPLE
    .\generate-nav.ps1
    Generates navigation section and updates mkdocs.yml
#>

# Function to extract title from markdown frontmatter
function Get-MarkdownTitle {
    param([string]$filePath)
    
    try {
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        # Check for YAML frontmatter
        if ($content -match '(?s)^---\r?\n(.*?)\r?\n---') {
            $frontmatter = $matches[1]
            if ($frontmatter -match 'title:\s*(.+)') {
                return $matches[1].Trim().Trim('"').Trim("'")
            }
        }
        
        # Fallback to first heading
        if ($content -match '^#\s+(.+)') {
            return $matches[1].Trim()
        }
    }
    catch {
        Write-Warning "Could not read file: $filePath"
    }
    
    return $null
}

# Function to sanitize title for safe YAML output
function Protect-YamlTitle {
    param([string]$title)
    
    # If title contains special YAML characters, wrap in quotes and escape internal quotes
    if ($title -match '[:#\[\]&\*\?!|>''"-]|^\s|:\s') {
        # Escape any double quotes in the title
        $title = $title -replace '"', '\"'
        return "`"$title`""
    }
    
    return $title
}

# Function to convert filename/dirname to title
function ConvertTo-Title {
    param([string]$name)
    
    # Remove file extension
    $name = [System.IO.Path]::GetFileNameWithoutExtension($name)
    
    # Handle special cases
    $titleMap = @{
        'osw'             = 'OSW'
        'tdei'            = 'TDEI'
        'josm'            = 'JOSM'
        'aviv-scoutroute' = 'AVIV ScoutRoute'
        'accessmap'       = 'AccessMap'
        'walkshed'        = 'Walkshed'
        'opensidewalks'   = 'OpenSidewalks'
        'tdei-core'       = 'TDEI Core'
        'index'           = ''
    }
    
    if ($titleMap.ContainsKey($name.ToLower())) {
        $result = $titleMap[$name.ToLower()]
        if ($result) { 
            return $result 
        }
        else { 
            return $null 
        }
    }
    
    # Convert kebab-case and snake_case to Title Case
    $result = $name -replace '[-_]', ' '
    $result = (Get-Culture).TextInfo.ToTitleCase($result.ToLower())
    
    return $result
}

# Function to build navigation tree for a specific directory
function Build-DirectoryNav {
    param(
        [string]$dirPath,
        [int]$indentLevel = 0
    )
    
    $items = @()
    $indent = "    " * $indentLevel
    
    # Get directory name and relative path
    $dirInfo = Get-Item $dirPath
    $dirName = $dirInfo.Name
    $relativePath = $dirPath.Substring((Resolve-Path $docsPath).Path.Length + 1) -replace '\\', '/'
    $dirTitle = ConvertTo-Title $dirName
    
    # Check for index.md
    $indexFile = Join-Path $dirPath "index.md"
    $hasIndex = Test-Path $indexFile
    
    # Get subdirectories and files
    $subDirs = Get-ChildItem -Path $dirPath -Directory | Sort-Object Name
    $mdFiles = Get-ChildItem -Path $dirPath -File -Filter "*.md" | Where-Object { $_.Name -ne 'index.md' } | Sort-Object Name
    
    # Create subitems list
    $subItems = @()
    
    # Add index.md first if it exists
    if ($hasIndex) {
        $subItems += "$indent    - $relativePath/index.md"
    }
    
    # Add other files in this directory
    foreach ($file in $mdFiles) {
        $fileRelativePath = $file.FullName.Substring((Resolve-Path $docsPath).Path.Length + 1) -replace '\\', '/'
        $fileTitle = Get-MarkdownTitle $file.FullName
        if (-not $fileTitle) {
            $fileTitle = ConvertTo-Title $file.BaseName
        }
        $fileTitle = Protect-YamlTitle $fileTitle
        $subItems += "$indent    - $($fileTitle): $fileRelativePath"
    }
    
    # Add subdirectories
    foreach ($subDir in $subDirs) {
        $subDirItems = Build-DirectoryNav -dirPath $subDir.FullName -indentLevel ($indentLevel + 1)
        $subItems += $subDirItems
    }
    
    # Build final structure
    if ($subItems.Count -gt 0) {
        $dirTitle = Protect-YamlTitle $dirTitle
        $items += "$indent- $dirTitle`:"
        $items += $subItems
    }
    elseif ($hasIndex) {
        # Directory with only index, no subitems
        $indexTitle = Get-MarkdownTitle $indexFile
        if (-not $indexTitle) { $indexTitle = $dirTitle }
        $indexTitle = Protect-YamlTitle $indexTitle
        $items += "$indent- $($indexTitle): $relativePath/index.md"
    }
    
    return $items
}

# Verify we're in the util directory by checking the current working directory name
$currentDirName = Split-Path -Leaf (Get-Location)

if ($currentDirName -ne "util") {
    Write-Host "Error: This script must be run from the util/ directory" -ForegroundColor Red
    Write-Host "Current location: $(Get-Location)" -ForegroundColor Yellow
    exit 1
}

# Detect paths from current working directory
# (Script only runs from util/, so paths are always relative to parent)
$docsPath = "..\docs"
$mkdocsPath = "..\mkdocs.yml"

# Main execution
Write-Host "Generating MkDocs navigation from '$docsPath'..." -ForegroundColor Cyan

# Build navigation tree
$navItems = @()

# Handle root index.md specially
$rootIndex = Join-Path $docsPath "index.md"
if (Test-Path $rootIndex) {
    $homeTitle = Get-MarkdownTitle $rootIndex
    if (-not $homeTitle) { $homeTitle = "Home" }
    $homeTitle = Protect-YamlTitle $homeTitle
    $navItems += "- $($homeTitle): index.md"
}

# Process root level directories
$rootDirectories = Get-ChildItem -Path $docsPath -Directory | Sort-Object Name
foreach ($dir in $rootDirectories) {
    $subNav = Build-DirectoryNav -dirPath $dir.FullName -indentLevel 0
    $navItems += $subNav
}

# Process any root-level markdown files (excluding index.md)
$rootFiles = Get-ChildItem -Path $docsPath -File -Filter "*.md" | Where-Object { $_.Name -ne 'index.md' } | Sort-Object Name
foreach ($file in $rootFiles) {
    $fileTitle = Get-MarkdownTitle $file.FullName
    if (-not $fileTitle) {
        $fileTitle = ConvertTo-Title $file.BaseName
    }
    $fileTitle = Protect-YamlTitle $fileTitle
    $navItems += "- $($fileTitle): $($file.Name)"
}

# Generate final navigation YAML with proper indentation
$indentedNavItems = $navItems | ForEach-Object { "  $_" }
$navYaml = "nav:" + [Environment]::NewLine + ($indentedNavItems -join [Environment]::NewLine) + [Environment]::NewLine

# Update mkdocs.yml directly
Write-Host "Updating mkdocs.yml..." -ForegroundColor Cyan

# Read current mkdocs.yml
$content = Get-Content $mkdocsPath -Raw -Encoding UTF8

# Split content into lines for easier processing
$lines = $content -split "`r?`n"
$navStartIndex = -1
$navEndIndex = -1

# Find nav section
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^nav:') {
        $navStartIndex = $i
        break
    }
}

if ($navStartIndex -eq -1) {
    Write-Host "Error: Could not find nav section in mkdocs.yml" -ForegroundColor Red
    exit 1
}

# Find end of nav section (next top-level key or end of file)
for ($i = $navStartIndex + 1; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^[a-zA-Z]') {
        $navEndIndex = $i - 1
        break
    }
}

if ($navEndIndex -eq -1) {
    $navEndIndex = $lines.Count - 1
}

# Extract current nav section for comparison
$currentNavSection = ($lines[$navStartIndex..$navEndIndex] -join [Environment]::NewLine) + [Environment]::NewLine

# Normalize both strings for comparison (remove trailing whitespace variations)
$currentNavNormalized = $currentNavSection -replace '\s+$', ''
$navYamlNormalized = $navYaml -replace '\s+$', ''

# Compare with generated nav
if ($currentNavNormalized -eq $navYamlNormalized) {
    Write-Host "Navigation section is already up to date. No changes needed." -ForegroundColor Green
    exit 0
}

# Build new content
$beforeNav = $lines[0..($navStartIndex - 1)] -join [Environment]::NewLine
$afterNav = if ($navEndIndex + 1 -lt $lines.Count) { 
    [Environment]::NewLine + ($lines[($navEndIndex + 1)..($lines.Count - 1)] -join [Environment]::NewLine)
}
else { 
    "" 
}

$newContent = $beforeNav + [Environment]::NewLine + $navYaml + $afterNav

# Write updated content
Set-Content -Path $mkdocsPath -Value $newContent -Encoding UTF8 -NoNewline
Write-Host "Successfully updated mkdocs.yml navigation section" -ForegroundColor Green
