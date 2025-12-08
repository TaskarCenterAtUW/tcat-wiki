#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Guides Lists Generator
# Version: 3.0.0
# Date: 2025-12-08
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Generates guide sections in parent index.md files and maintains the main Guides List

.DESCRIPTION
    This script performs two phases:
    
    PHASE 1: Recursively scans docs/ (except resources/) for .md files with "- Guide" in frontmatter.
    For each guide file found, it injects a "## Guides" section into the parent directory's index.md
    with the guide title, filename link, and full description.
    
    PHASE 2: Generates the main guides-list/index.md by collecting all guides from directories
    and organizing them with the correct hierarchy. Directories with no guides receive an 
    "_Coming soon!_" placeholder (unless they have child directories).
    
    Guide files must:
    - Have "- Guide" tag in the frontmatter
    - Include a description between the "# Title" line and "_For a list of all guides..._" line
    
    Special frontmatter flags (YAML comments, invisible on built pages):
    - # skip-in-guides-lists: true - Exclude a guide from guides lists
    - # include-in-guides-lists: true - Force include a topic index in guides lists

.EXAMPLE
    .\generate-guides-lists.ps1
#>

function Get-GuideInfo {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )
    
    $result = @{
        Title          = ""
        Description    = ""
        IsGuide        = $false
        SkipGuidesList = $false
    }
    
    try {
        $content = Get-Content $FilePath -Raw -ErrorAction Stop
        
        # Check for "- Guide" tag in frontmatter
        if ($content -match '(?s)^---\r?\n(.*?)\r?\n---' -and $matches[1] -match '- Guide') {
            $result.IsGuide = $true
        }
        
        # Check for skip-in-guides-lists flag in frontmatter
        if ($content -match '(?s)^---\r?\n(.*?)\r?\n---' -and $matches[1] -match '# skip-in-guides-lists:\s*true') {
            $result.SkipGuidesList = $true
        }
        
        # Extract title from frontmatter
        if ($content -match 'title:\s*(.+?)(?:\r?\n|$)') {
            $result.Title = $matches[1].Trim()
        }
        
        # Extract description: everything between "# Title" and "_For a list of all guides..._"
        # Use multiline mode to find the H1 header anywhere in the document
        if ($content -match '(?s)(?:^|\r?\n)#\s+.+?(?:\r?\n)(.*?)(?:\r?\n_For a list of all guides)') {
            $descRaw = $matches[1].Trim()
            # Clean up: remove leading/trailing whitespace but preserve internal structure
            $descRaw = $descRaw -replace '^[\s\r\n]+|[\s\r\n]+$', ''
            $result.Description = $descRaw
        }
    }
    catch {
        Write-Warning "Could not read file: $FilePath - $_"
    }
    
    return $result
}

function Get-IndexTitleFromFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$IndexPath
    )
    
    try {
        $content = Get-Content $IndexPath -Raw -ErrorAction Stop
        
        # Extract title from frontmatter
        if ($content -match 'title:\s*(.+?)(?:\r?\n|$)') {
            return $matches[1].Trim()
        }
    }
    catch {
        Write-Warning "Could not read title from: $IndexPath"
    }
    
    return ""
}

function Get-IncludeInGuidesList {
    param(
        [Parameter(Mandatory = $true)]
        [string]$IndexPath
    )
    
    try {
        $content = Get-Content $IndexPath -Raw -ErrorAction Stop
        
        # Check for include-in-guides-lists flag in frontmatter (YAML comment, invisible on page)
        if ($content -match '(?s)^---\r?\n(.*?)\r?\n---' -and $matches[1] -match '# include-in-guides-lists:\s*true') {
            return $true
        }
    }
    catch {
        Write-Warning "Could not read include flag from: $IndexPath"
    }
    
    return $false
}

function Get-RelativePathFromGuidesList {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetIndexPath,
        
        [Parameter(Mandatory = $true)]
        [string]$DocsPath
    )
    
    # Calculate relative path from docs/guides-list/ to target index.md
    $guidesListPath = Join-Path $DocsPath "guides-list"
    $targetPath = $TargetIndexPath
    
    $relative = [System.IO.Path]::GetRelativePath($guidesListPath, $targetPath) -replace '\\', '/'
    return $relative
}

function Update-ParentGuidesSection {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ParentIndexPath,
        
        [Parameter(Mandatory = $true)]
        [object[]]$GuideFiles,
        
        [Parameter(Mandatory = $true)]
        [string]$DocsPath
    )
    
    if ($GuideFiles.Count -eq 0) {
        return $false
    }
    
    $dirName = Split-Path $ParentIndexPath -Parent | Split-Path -Leaf
    Write-Host "  Updating: $dirName"
    
    try {
        $content = Get-Content $ParentIndexPath -Raw -ErrorAction Stop
        
        # Use Windows-style line endings (CRLF)
        $lineEnding = "`r`n"
        
        # Get the title from this file's frontmatter
        $pageTitle = Get-IndexTitleFromFile -IndexPath $ParentIndexPath
        
        # Calculate how many directory levels up from this file to the docs root
        # Then add the path to guides-list
        $dirDepth = ($ParentIndexPath -replace [regex]::Escape($docsPath), '' -split '\\' | Where-Object { $_ -ne '' }).Count - 1
        $relPathToGuidesList = ('../' * $dirDepth) + 'guides-list/index.md'
        
        # Remove existing "## Guides" section if it exists (everything from "## Guides" to end)
        $content = $content -replace '(?s)\r?\n\r?\n## Guides\r?\n.*$', ''
        
        # Build new Guides section at the end (with blank lines before and after header)
        $guidesSection = "$lineEnding$lineEnding## Guides$lineEnding$lineEnding"
        $guidesSection += "$pageTitle Guides$lineEnding$lineEnding"
        $guidesSection += "_For a list of all guides on the TCAT Wiki, refer to the [Guides List]($relPathToGuidesList)._$lineEnding$lineEnding"
        
        for ($i = 0; $i -lt $GuideFiles.Count; $i++) {
            $file = $GuideFiles[$i]
            $guideInfo = Get-GuideInfo -FilePath $file.FullName
            
            # Calculate relative path from parent index.md to this guide file
            $parentDir = Split-Path $ParentIndexPath -Parent
            $relPathToGuide = [System.IO.Path]::GetRelativePath($parentDir, $file.FullName) -replace '\\', '/'
            
            $guidesSection += "### [$($guideInfo.Title)]($relPathToGuide)$lineEnding"
            if ($guideInfo.Description) {
                $guidesSection += "$lineEnding$($guideInfo.Description)$lineEnding"
            }
            
            if ($i -lt ($GuideFiles.Count - 1)) {
                $guidesSection += "$lineEnding"
            }
        }
        
        # Append Guides section to end of file (trim trailing newlines then add single newline)
        $content = $content.TrimEnd() + $guidesSection.TrimEnd()
        
        Set-Content -Path $ParentIndexPath -Value $content -Encoding UTF8
        Write-Host "    ✓ Updated with $($GuideFiles.Count) guide(s)"
        return $true
    }
    catch {
        Write-Warning "  Could not update $ParentIndexPath - $_"
        return $false
    }
}


# ==============================================================================
# MAIN SCRIPT
# ==============================================================================

Write-Host ""
Write-Host "TCAT Wiki - Guides Lists Generator v3.0.0"
Write-Host "==========================================="
Write-Host ""

# Auto-detect docs path
$docsPath = ""
if (Test-Path "..\docs") {
    $docsPath = Resolve-Path "..\docs"
}
elseif (Test-Path "docs") {
    $docsPath = Resolve-Path "docs"
}
else {
    Write-Error "docs directory not found. Please run this script from the repository root or util directory."
    exit 1
}

Write-Host "Scanning: $docsPath"
Write-Host ""

# ==============================================================================
# PHASE 1: Update parent index.md files with Guides sections
# ==============================================================================

Write-Host "PHASE 1: Updating parent directory index.md files"
Write-Host "---------------------------------------------------"
Write-Host ""

# Find all directories with index.md (recursively, excluding resources)
$directoriesToProcess = Get-ChildItem -Path $docsPath -Recurse -Directory -ErrorAction Stop |
Where-Object { $_.Name -ne "resources" -and $_.Name -ne ".git" } |
ForEach-Object {
    $indexPath = Join-Path $_.FullName "index.md"
    if (Test-Path $indexPath -PathType Leaf) {
        $_ | Add-Member -NotePropertyName "IndexPath" -NotePropertyValue $indexPath -PassThru
    }
} | Sort-Object FullName

Write-Host "Found $($directoriesToProcess.Count) directories with index.md files"
Write-Host ""

$updatedCount = 0

foreach ($dir in $directoriesToProcess) {
    # Find all .md files in this directory and its subdirectories that have "- Guide" tag
    # Exclude only the parent directory's own index.md, but include nested index.md files
    $guideFiles = @(Get-ChildItem -Path $dir.FullName -Filter "*.md" -File -Recurse |
        Where-Object { $_.FullName -ne $dir.IndexPath } |
        ForEach-Object {
            $guideInfo = Get-GuideInfo -FilePath $_.FullName
            if ($guideInfo.IsGuide -and -not $guideInfo.SkipGuidesList) { $_ }
        } | Sort-Object FullName)
    
    if ($guideFiles.Count -gt 0) {
        if (Update-ParentGuidesSection -ParentIndexPath $dir.IndexPath -GuideFiles $guideFiles -DocsPath $docsPath) {
            $updatedCount++
        }
    }
}

Write-Host ""
Write-Host "Updated $updatedCount directories with guide sections"
Write-Host ""

# ==============================================================================
# PHASE 2: Generate main guides-list/index.md
# ==============================================================================

Write-Host "PHASE 2: Generating main guides-list/index.md"
Write-Host "-----------------------------------------------"
Write-Host ""

# Build the main guides list by processing all directories
$mainContent = "---`r`ntitle: Guides List`r`n---`r`n`r`n<!-- @format -->`r`n`r`n# Guides List`r`n`r`nGuides, tutorials, and user manuals produced by TCAT and/or its partners are listed below.`r`n`r`n"

# Process each directory and add its guides or "Coming soon!"
$processedCount = 0
foreach ($dir in $directoriesToProcess) {
    # Skip guides-list itself
    if ($dir.FullName -match 'guides-list$') {
        continue
    }
    
    # Get the title from this directory's index.md
    $indexTitle = Get-IndexTitleFromFile -IndexPath $dir.IndexPath
    if (-not $indexTitle) {
        continue
    }
    
    # Calculate relative path from guides-list to this index.md
    $relPath = Get-RelativePathFromGuidesList -TargetIndexPath $dir.IndexPath -DocsPath $docsPath
    
    # Calculate depth for header level (## for root, ### for 1 level deep, etc.)
    $depthFromDocs = ($dir.FullName -replace [regex]::Escape($docsPath), '' -split '\\' | Where-Object { $_ -ne '' } | Measure-Object).Count
    $headerLevel = '#' * ($depthFromDocs + 1)  # +1 because we want ## minimum
    
    # Find all guides in this directory and its subdirectories, excluding any with skip-in-guides-lists flag
    # Exclude only this directory's own index.md, but include nested index.md files
    $guideFiles = @(Get-ChildItem -Path $dir.FullName -Filter "*.md" -File -Recurse |
        Where-Object { $_.FullName -ne $dir.IndexPath } |
        ForEach-Object {
            $guideInfo = Get-GuideInfo -FilePath $_.FullName
            if ($guideInfo.IsGuide -and -not $guideInfo.SkipGuidesList) { $_ }
        } | Sort-Object FullName)
    
    # Determine if this directory should be included in the guides list
    $includeInList = Get-IncludeInGuidesList -IndexPath $dir.IndexPath
    $hasGuides = $guideFiles.Count -gt 0
    $hasChildDirs = @(Get-ChildItem -Path $dir.FullName -Directory -ErrorAction SilentlyContinue | 
        Where-Object { $_.Name -ne "resources" -and $_.Name -ne ".git" }).Count -gt 0
    
    # Include in guides list if:
    # 1. It has guides, OR
    # 2. It's explicitly marked with include-in-guides-lists: true, OR
    # 3. It has child directories (infer from structure)
    if (-not $hasGuides -and -not $includeInList -and -not $hasChildDirs) {
        continue
    }
    
    # Add section header
    $mainContent += "$headerLevel [$indexTitle]($relPath) Guides`r`n`r`n"
    
    if ($guideFiles.Count -eq 0) {
        # No guides in this directory - show "Coming soon!" only for leaf directories
        if (-not $hasChildDirs) {
            $mainContent += "_Coming soon!_`r`n`r`n"
        }
    }
    else {
        # Add all guides with descriptions
        foreach ($guide in $guideFiles) {
            $guideInfo = Get-GuideInfo -FilePath $guide.FullName
            # Calculate relative path from guides-list to this guide file
            $guideFullPath = $guide.FullName
            $guideRelPath = [System.IO.Path]::GetRelativePath((Join-Path $docsPath "guides-list"), $guideFullPath) -replace '\\', '/'
            
            # Determine header level for guide (one level deeper than section)
            $guideHeaderLevel = '#' * ($depthFromDocs + 2)
            
            $mainContent += "$guideHeaderLevel [$($guideInfo.Title)]($guideRelPath)`r`n"
            if ($guideInfo.Description) {
                $mainContent += "`r`n$($guideInfo.Description)`r`n"
            }
            $mainContent += "`r`n"
        }
    }
    
    $processedCount++
}

# Add TCAT Wiki Guides section
$mainContent += "## TCAT Wiki Guides`r`n`r`n"
$mainContent += "### [Contributing](../CONTRIBUTING.md)`r`n`r`n"
$mainContent += "This guide explains how to contribute to the TCAT Wiki."

# Write main guides list
$mainIndexPath = Join-Path $docsPath "guides-list" "index.md"
Set-Content -Path $mainIndexPath -Value $mainContent -Encoding UTF8

Write-Host "✓ Generated main guides list from $processedCount directories"
Write-Host ""

Write-Host "==========================================="
Write-Host "Guides list generation complete!"
Write-Host ""
