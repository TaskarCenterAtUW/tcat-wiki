#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Guides Lists Generator
# Version: 4.0.0
# Date: 2025-12-08
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Generates guide sections in parent index.md files and maintains the main Guides List

.DESCRIPTION
    This script performs two phases:
    
    PHASE 1: For each directory with index.md, creates a "## Guides" section listing:
    - Direct guides in that directory
    - Subsections for subdirectories with their guides
    
    PHASE 2: Generates the main guides-list/index.md with hierarchical structure
    across all topics.
    
    Guide files must have "- Guide" tag in frontmatter.
    User manual index files should have "- User Manual" tag (implies Guide).
    
    Special frontmatter flags (YAML comments, invisible on built pages):
    - # exclude-from-parent-guides-list - Exclude from parent directory guides sections
    - # exclude-from-main-guides-list - Exclude from main guides list
    
    User Manual handling:
    - Detected by "- User Manual" tag on index.md
    - Don't get " Guides" suffix in section headers
    - In main guides list: only the user manual itself appears, not its subpages

.EXAMPLE
    .\generate-guides-lists.ps1
#>

# ==============================================================================
# CONSTANTS
# ==============================================================================

$CRLF = "`r`n"
$EXCLUDE_PARENT_FLAG = "exclude-from-parent-guides-list"
$EXCLUDE_MAIN_FLAG = "exclude-from-main-guides-list"

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

function Get-GuideInfo {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )
    
    $result = @{
        Title             = ""
        Description       = ""
        IsGuide           = $false
        IsUserManual      = $false
        ExcludeFromParent = $false
        ExcludeFromMain   = $false
    }
    
    try {
        $content = Get-Content $FilePath -Raw -ErrorAction Stop
        
        # Check for "- Guide" or "- User Manual" tag in frontmatter
        if ($content -match '(?s)^---\r?\n(.*?)\r?\n---') {
            $frontmatter = $matches[1]
            if ($frontmatter -match '- Guide') {
                $result.IsGuide = $true
            }
            if ($frontmatter -match '- User Manual') {
                $result.IsUserManual = $true
                $result.IsGuide = $true  # User manuals are also guides
            }
            if ($frontmatter -match "# $EXCLUDE_PARENT_FLAG") {
                $result.ExcludeFromParent = $true
            }
            if ($frontmatter -match "# $EXCLUDE_MAIN_FLAG") {
                $result.ExcludeFromMain = $true
            }
        }
        
        # Extract title from frontmatter
        if ($content -match 'title:\s*(.+?)(?:\r?\n|$)') {
            $result.Title = $matches[1].Trim()
        }
        
        # Extract description: everything between "# Title" and "_For a list of all guides"
        # Use lookahead to stop at first occurrence
        if ($content -match '(?s)(?:^|\r?\n)#\s+.+?(?:\r?\n)(.*?)(?=\r?\n_For a list of all guides)') {
            $descRaw = $matches[1].Trim()
            $descRaw = $descRaw -replace '^[\s\r\n]+|[\s\r\n]+$', ''
            $result.Description = $descRaw
        }
    }
    catch {
        Write-Warning "Could not read file: $FilePath - $_"
    }
    
    return $result
}

function Get-DirectoryTitle {
    param(
        [Parameter(Mandatory = $true)]
        [string]$IndexPath
    )
    
    try {
        $content = Get-Content $IndexPath -Raw -ErrorAction Stop
        
        if ($content -match 'title:\s*(.+?)(?:\r?\n|$)') {
            return $matches[1].Trim()
        }
    }
    catch {
        Write-Warning "Could not read title from: $IndexPath"
    }
    
    return ""
}

function Test-IsUserManualDirectory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory
    )
    
    $indexPath = Join-Path $Directory "index.md"
    if (Test-Path $indexPath -PathType Leaf) {
        $guideInfo = Get-GuideInfo -FilePath $indexPath
        return $guideInfo.IsUserManual
    }
    return $false
}

function Get-RelativeMarkdownPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FromPath,
        
        [Parameter(Mandatory = $true)]
        [string]$ToPath
    )
    
    $relativePath = [System.IO.Path]::GetRelativePath($FromPath, $ToPath)
    return $relativePath -replace '\\', '/'
}

function Get-GuidesInDirectory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory,
        
        [Parameter(Mandatory = $true)]
        [bool]$ExcludeOwnIndex,
        
        [Parameter(Mandatory = $true)]
        [string]$ExcludeFlag
    )
    
    $indexPath = Join-Path $Directory "index.md"
    $guides = @()
    
    Get-ChildItem -Path $Directory -Filter "*.md" -File | ForEach-Object {
        # Skip if it's the directory's own index.md and we're excluding it
        if ($ExcludeOwnIndex -and $_.FullName -eq $indexPath) {
            return
        }
        
        $guideInfo = Get-GuideInfo -FilePath $_.FullName
        
        # Include if it's a guide and not excluded by the flag
        $isExcluded = if ($ExcludeFlag -eq $EXCLUDE_PARENT_FLAG) { 
            $guideInfo.ExcludeFromParent 
        }
        else { 
            $guideInfo.ExcludeFromMain 
        }
        
        if ($guideInfo.IsGuide -and -not $isExcluded) {
            $guides += $_
        }
    }
    
    return $guides | Sort-Object FullName
}

function Get-Subdirectories {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory
    )
    
    $subdirs = @()
    
    Get-ChildItem -Path $Directory -Directory | ForEach-Object {
        if ($_.Name -eq "resources") {
            return
        }
        
        $indexPath = Join-Path $_.FullName "index.md"
        if (Test-Path $indexPath -PathType Leaf) {
            $subdirs += $_
        }
    }
    
    return $subdirs | Sort-Object FullName
}

function Build-GuideEntry {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo]$GuideFile,
        
        [Parameter(Mandatory = $true)]
        [string]$FromPath,
        
        [Parameter(Mandatory = $true)]
        [string]$HeaderLevel
    )
    
    $guideInfo = Get-GuideInfo -FilePath $GuideFile.FullName
    $relativePath = Get-RelativeMarkdownPath -FromPath $FromPath -ToPath $GuideFile.FullName
    
    $entry = "$HeaderLevel [$($guideInfo.Title)]($relativePath)$CRLF"
    
    if ($guideInfo.Description) {
        $entry += "$CRLF$($guideInfo.Description)$CRLF"
    }
    
    return $entry
}

function Build-SectionHeader {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Title,
        
        [Parameter(Mandatory = $true)]
        [string]$IndexPath,
        
        [Parameter(Mandatory = $true)]
        [string]$FromPath,
        
        [Parameter(Mandatory = $true)]
        [string]$HeaderLevel,
        
        [Parameter(Mandatory = $true)]
        [bool]$IsUserManual
    )
    
    $relativePath = Get-RelativeMarkdownPath -FromPath $FromPath -ToPath $IndexPath
    # User manuals don't get " Guides" suffix
    $displayTitle = if ($IsUserManual) { $Title } else { "$Title Guides" }
    
    return "$HeaderLevel [$displayTitle]($relativePath)$CRLF$CRLF"
}

function Get-TcatWikiSection {
    return "## TCAT Wiki Guides$CRLF$CRLF### [Contributing](../CONTRIBUTING.md)$CRLF$CRLF" +
    "This guide explains how to contribute to the TCAT Wiki.$CRLF"
}

# ==============================================================================
# MAIN FUNCTIONS
# ==============================================================================

function Update-ParentGuidesSection {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo]$Directory
    )
    
    $indexPath = Join-Path $Directory.FullName "index.md"
    $parentDir = $Directory.FullName
    
    # Get direct guides
    $directGuides = Get-GuidesInDirectory -Directory $parentDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
    
    # Get subdirectories
    $subdirs = Get-Subdirectories -Directory $parentDir
    
    # Check if there's anything to add
    $hasContent = $false
    if ($directGuides.Count -gt 0) {
        $hasContent = $true
    }
    else {
        # Check if any subdir has guides or is a user manual
        foreach ($subdir in $subdirs) {
            if (Test-IsUserManualDirectory -Directory $subdir.FullName) {
                $hasContent = $true
                break
            }
            $subdirGuides = Get-GuidesInDirectory -Directory $subdir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            if ($subdirGuides.Count -gt 0) {
                $hasContent = $true
                break
            }
        }
    }
    
    if (-not $hasContent) {
        return
    }
    
    # Build guides section
    $pageTitle = Get-DirectoryTitle -IndexPath $indexPath
    $dirDepth = ($indexPath -replace [regex]::Escape($script:docsPath), '' -split '\\' | Where-Object { $_ -ne '' }).Count - 1
    $relPathToGuidesList = ('../' * $dirDepth) + 'guides-list/index.md'
    
    $guidesSection = "$CRLF$CRLF## Guides$CRLF$CRLF"
    $guidesSection += "$pageTitle Guides$CRLF$CRLF"
    $guidesSection += "_For a list of all guides on the TCAT Wiki, refer to the [Guides List]($relPathToGuidesList)._$CRLF$CRLF"
    
    # Add direct guides
    foreach ($guide in $directGuides) {
        $guidesSection += Build-GuideEntry -GuideFile $guide -FromPath $parentDir -HeaderLevel "###"
        $guidesSection += $CRLF
    }
    
    # Add subdirectory subsections
    foreach ($subdir in $subdirs) {
        $subdirIndexPath = Join-Path $subdir.FullName "index.md"
        $subdirTitle = Get-DirectoryTitle -IndexPath $subdirIndexPath
        $isUserManual = Test-IsUserManualDirectory -Directory $subdir.FullName
        
        if ($isUserManual) {
            # User manual: show as a single guide entry (no child guides listed)
            $guidesSection += Build-GuideEntry -GuideFile (Get-Item $subdirIndexPath) -FromPath $parentDir -HeaderLevel "###"
            $guidesSection += $CRLF
        }
        else {
            # Regular directory: show section header with child guides
            $subdirGuides = Get-GuidesInDirectory -Directory $subdir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            
            if ($subdirGuides.Count -eq 0) {
                continue
            }
            
            $guidesSection += Build-SectionHeader -Title $subdirTitle -IndexPath $subdirIndexPath -FromPath $parentDir -HeaderLevel "###" -IsUserManual $false
            
            foreach ($guide in $subdirGuides) {
                $guidesSection += Build-GuideEntry -GuideFile $guide -FromPath $parentDir -HeaderLevel "####"
                $guidesSection += $CRLF
            }
        }
    }
    
    # Read existing content and replace ## Guides section
    $content = Get-Content $indexPath -Raw -ErrorAction Stop
    $content = $content -replace '(?s)\r?\n\r?\n## Guides\r?\n.*$', ''
    $content = $content.TrimEnd() + $guidesSection.TrimEnd()
    
    Set-Content -Path $indexPath -Value $content -Encoding UTF8
    
    $dirName = $Directory.Name
    Write-Host "  ✓ Updated: $dirName"
}

function Build-MainGuidesList {
    param(
        [Parameter(Mandatory = $true)]
        [array]$AllDirectories,
        
        [Parameter(Mandatory = $true)]
        [string]$DocsPath
    )
    
    # Start with header
    $content = "---${CRLF}title: Guides List${CRLF}---${CRLF}${CRLF}<!-- @format -->${CRLF}${CRLF}"
    $content += "# Guides List${CRLF}${CRLF}"
    $content += "Guides, tutorials, and user manuals produced by TCAT and/or its partners are listed below.${CRLF}${CRLF}"
    
    $guidesListPath = Join-Path $DocsPath "guides-list"
    
    # Process each directory
    foreach ($dir in $AllDirectories) {
        # Skip guides-list itself
        if ($dir.FullName -match 'guides-list$') {
            continue
        }
        
        # Check if this directory is a user manual
        $indexPath = Join-Path $dir.FullName "index.md"
        $isUserManual = Test-IsUserManualDirectory -Directory $dir.FullName
        
        # For user manuals: only show the index.md itself (not child pages)
        # For regular directories: show all guides except the index.md
        if ($isUserManual) {
            $indexInfo = Get-GuideInfo -FilePath $indexPath
            if (-not $indexInfo.IsGuide -or $indexInfo.ExcludeFromMain) {
                continue
            }
            
            $dirTitle = Get-DirectoryTitle -IndexPath $indexPath
            $depthFromDocs = ($dir.FullName -replace [regex]::Escape($DocsPath), '' -split '\\' | Where-Object { $_ -ne '' } | Measure-Object).Count
            $headerLevel = '#' * ($depthFromDocs + 1)
            
            # Add user manual as a single guide entry (no section header, just the guide)
            $content += Build-GuideEntry -GuideFile (Get-Item $indexPath) -FromPath $guidesListPath -HeaderLevel $headerLevel
            $content += $CRLF
        }
        else {
            # Regular directory: get guides excluding own index.md
            $guides = Get-GuidesInDirectory -Directory $dir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_MAIN_FLAG
            
            if ($guides.Count -eq 0) {
                continue
            }
            
            $dirTitle = Get-DirectoryTitle -IndexPath $indexPath
            $depthFromDocs = ($dir.FullName -replace [regex]::Escape($DocsPath), '' -split '\\' | Where-Object { $_ -ne '' } | Measure-Object).Count
            $headerLevel = '#' * ($depthFromDocs + 1)
            
            # Add section header
            $content += Build-SectionHeader -Title $dirTitle -IndexPath $indexPath -FromPath $guidesListPath -HeaderLevel $headerLevel -IsUserManual $false
            
            # Add guides
            foreach ($guide in $guides) {
                $guideHeaderLevel = '#' * ($depthFromDocs + 2)
                $content += Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
                $content += $CRLF
            }
        }
    }
    
    # Add TCAT Wiki section
    $content += Get-TcatWikiSection
    
    return $content
}

# ==============================================================================
# MAIN SCRIPT
# ==============================================================================

Write-Host ""
Write-Host "TCAT Wiki - Guides Lists Generator v4.0.0"
Write-Host "==========================================="
Write-Host ""

# Find docs path
$script:docsPath = ""
if (Test-Path "..\docs") {
    $script:docsPath = Resolve-Path "..\docs"
}
elseif (Test-Path "docs") {
    $script:docsPath = Resolve-Path "docs"
}
else {
    Write-Error "docs directory not found. Please run this script from the repository root or util directory."
    exit 1
}

Write-Host "Scanning: $script:docsPath"
Write-Host ""

# Get all directories with index.md
$allDirectories = Get-ChildItem -Path $script:docsPath -Recurse -Directory -ErrorAction Stop |
Where-Object { $_.Name -ne "resources" } |
ForEach-Object {
    $indexPath = Join-Path $_.FullName "index.md"
    if (Test-Path $indexPath -PathType Leaf) {
        $_
    }
} | Sort-Object FullName

Write-Host "Found $($allDirectories.Count) directories with index.md files"
Write-Host ""

# ==============================================================================
# PHASE 1: Update parent guides sections
# ==============================================================================

Write-Host "PHASE 1: Updating parent directory index.md files"
Write-Host "---------------------------------------------------"
Write-Host ""

foreach ($dir in $allDirectories) {
    try {
        Update-ParentGuidesSection -Directory $dir
    }
    catch {
        Write-Error "Failed processing $($dir.FullName): $_"
        exit 1
    }
}

Write-Host ""

# ==============================================================================
# PHASE 2: Generate main guides list
# ==============================================================================

Write-Host "PHASE 2: Generating main guides-list/index.md"
Write-Host "-----------------------------------------------"
Write-Host ""

try {
    $mainContent = Build-MainGuidesList -AllDirectories $allDirectories -DocsPath $script:docsPath
    $guidesListPath = Join-Path $script:docsPath "guides-list\index.md"
    Set-Content -Path $guidesListPath -Value $mainContent -Encoding UTF8
    Write-Host "✓ Generated main guides list"
}
catch {
    Write-Error "Failed generating main guides list: $_"
    exit 1
}

Write-Host ""
Write-Host "==========================================="
Write-Host "Guides list generation complete!"
Write-Host ""
