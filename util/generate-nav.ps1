#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Generates MkDocs navigation structure from docs directory

.DESCRIPTION
    Scans the docs directory structure and generates a YAML navigation tree 
    that can be inserted into mkdocs.yml. Uses frontmatter titles when available,
    otherwise derives titles from filenames and directory names.
.PARAMETER docsPath
    Path to the documentation directory to scan (default: "docs")

.PARAMETER outputFile
    Output file path for the generated navigation YAML (default: console output)

.PARAMETER updateMkdocs
    Update the mkdocs.yml file directly by replacing the nav section

.PARAMETER mkdocsPath
    Path to the mkdocs.yml file (default: "../mkdocs.yml")

.EXAMPLE
    .\generate-nav.ps1
    Generates navigation and outputs to console

.EXAMPLE
    .\generate-nav.ps1 -outputFile "nav.yml"
    Generates navigation and saves to nav.yml

.EXAMPLE
    .\generate-nav.ps1 -updateMkdocs
    Updates mkdocs.yml directly with generated navigation
#>

param(
    [Parameter(HelpMessage = "Path to the documentation directory")]
    [string]$docsPath = "",
    
    [Parameter(HelpMessage = "Output file path for generated navigation")]
    [string]$outputFile = "",
    
    [Parameter(HelpMessage = "Update mkdocs.yml directly")]
    [switch]$updateMkdocs,
    
    [Parameter(HelpMessage = "Path to mkdocs.yml file")]
    [string]$mkdocsPath = ""
)

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
    $indent = "  " * $indentLevel
    
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
        $subItems += "$indent  - $relativePath/index.md"
    }
    
    # Add other files in this directory
    foreach ($file in $mdFiles) {
        $fileRelativePath = $file.FullName.Substring((Resolve-Path $docsPath).Path.Length + 1) -replace '\\', '/'
        $fileTitle = Get-MarkdownTitle $file.FullName
        if (-not $fileTitle) {
            $fileTitle = ConvertTo-Title $file.BaseName
        }
        $subItems += "$indent  - $($fileTitle): $fileRelativePath"
    }
    
    # Add subdirectories
    foreach ($subDir in $subDirs) {
        $subDirItems = Build-DirectoryNav -dirPath $subDir.FullName -indentLevel ($indentLevel + 1)
        $subItems += $subDirItems
    }
    
    # Build final structure
    if ($subItems.Count -gt 0) {
        $items += "$indent- $dirTitle`:"
        $items += $subItems
    }
    elseif ($hasIndex) {
        # Directory with only index, no subitems
        $indexTitle = Get-MarkdownTitle $indexFile
        if (-not $indexTitle) { $indexTitle = $dirTitle }
        $items += "$indent- $($indexTitle): $relativePath/index.md"
    }
    
    return $items
}

# Auto-detect paths if not specified
if (-not $docsPath) {
    # Check if we're in the util directory
    if (Test-Path "..\docs") {
        $docsPath = "..\docs"
    }
    # Check if we're in the repository root
    elseif (Test-Path "docs") {
        $docsPath = "docs"
    }
    else {
        Write-Host "Error: Cannot auto-detect docs directory. Please specify -docsPath parameter." -ForegroundColor Red
        Write-Host "Searched for: ..\docs, docs" -ForegroundColor Yellow
        exit 1
    }
}

if (-not $mkdocsPath) {
    # Check if we're in the util directory
    if (Test-Path "..\mkdocs.yml") {
        $mkdocsPath = "..\mkdocs.yml"
    }
    # Check if we're in the repository root
    elseif (Test-Path "mkdocs.yml") {
        $mkdocsPath = "mkdocs.yml"
    }
    else {
        Write-Host "Error: Cannot auto-detect mkdocs.yml file. Please specify -mkdocsPath parameter." -ForegroundColor Red
        Write-Host "Searched for: ..\mkdocs.yml, mkdocs.yml" -ForegroundColor Yellow
        exit 1
    }
}

# Main execution
Write-Host "Generating MkDocs navigation from '$docsPath'..." -ForegroundColor Cyan

# Check if docs directory exists
if (-not (Test-Path $docsPath)) {
    Write-Host "Error: Docs directory '$docsPath' not found!" -ForegroundColor Red
    exit 1
}

# Build navigation tree
$navItems = @()

# Handle root index.md specially
$rootIndex = Join-Path $docsPath "index.md"
if (Test-Path $rootIndex) {
    $homeTitle = Get-MarkdownTitle $rootIndex
    if (-not $homeTitle) { $homeTitle = "Home" }
    $navItems += "- $($homeTitle): index.md"
}

# Process root level directories
$rootDirectories = Get-ChildItem -Path $docsPath -Directory | Sort-Object Name
foreach ($dir in $rootDirectories) {
    $subNav = Build-DirectoryNav -dirPath $dir.FullName -indentLevel 0
    $navItems += $subNav
}

# Process any root-level markdown files (excluding index.md which was handled above)
$rootFiles = Get-ChildItem -Path $docsPath -File -Filter "*.md" | Where-Object { $_.Name -ne 'index.md' } | Sort-Object Name
foreach ($file in $rootFiles) {
    $fileTitle = Get-MarkdownTitle $file.FullName
    if (-not $fileTitle) {
        $fileTitle = ConvertTo-Title $file.BaseName
    }
    $navItems += "- $($fileTitle): $($file.Name)"
}

# Generate final navigation YAML with proper indentation
$indentedNavItems = $navItems | ForEach-Object { "  $_" }
$navYaml = "nav:" + [Environment]::NewLine + ($indentedNavItems -join [Environment]::NewLine)

# Output results
if ($updateMkdocs) {
    # Update mkdocs.yml directly
    if (-not (Test-Path $mkdocsPath)) {
        Write-Host "Error: mkdocs.yml not found!" -ForegroundColor Red
        exit 1
    }
    
    # Read current mkdocs.yml
    $content = Get-Content $mkdocsPath -Raw -Encoding UTF8
    
    # Replace nav section
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
}
elseif ($outputFile) {
    # Save to output file
    Set-Content -Path $outputFile -Value $navYaml -Encoding UTF8
    Write-Host "Navigation saved to: $outputFile" -ForegroundColor Green
}
else {
    # Output to console
    Write-Host ""
    Write-Host $navYaml
}
