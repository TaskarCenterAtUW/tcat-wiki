#!/usr/bin/env pwsh

<#
.SYNOPSIS
    Generates index.md files for all guides directories in the docs folder.

.DESCRIPTION
    This script recursively searches through the docs directory for any subdirectory 
    named "guides" and generates an index.md file containing a list of all .md files
    in that directory (excluding index.md itself).

.EXAMPLE
    .\generate-guides-lists.ps1
#>

function Get-RelativePathToGuidesIndex {
    param(
        [Parameter(Mandatory = $true)]
        [string]$CurrentPath
    )
    
    # Normalize path separators  
    $normalizedPath = $CurrentPath -replace '[/\\]', '/'
    
    # Remove any leading path components before 'docs'
    if ($normalizedPath -match 'docs/(.*)') {
        $relativePath = $matches[1]  # Everything after docs/
    }
    else {
        Write-Warning "Could not find 'docs' directory in path: $CurrentPath"
        return '../../guides/index.md'  # Fallback
    }
    
    # Split the path after docs/
    $pathParts = $relativePath -split '/' | Where-Object { $_ -ne '' }
    
    # Special case: if we're in docs/guides, link to self
    if ($pathParts.Count -eq 1 -and $pathParts[0] -eq 'guides') {
        return 'index.md'
    }
    
    # Calculate how many levels to go back from current guides directory to docs
    # We need to go back pathParts.Count levels to get to docs root
    $levelsToGoBack = $pathParts.Count
    
    if ($levelsToGoBack -eq 1) {
        # We're in docs/guides
        return 'index.md'
    }
    else {
        $backPath = ('../' * $levelsToGoBack) + 'guides/index.md'
        return $backPath
    }
}

function Get-GuideInfo {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateScript({ Test-Path $_ -PathType Leaf })]
        [string]$FilePath
    )
    
    $result = @{
        Title       = ""
        Description = ""
    }
    
    try {
        $content = Get-Content $FilePath -ErrorAction Stop
        
        # Look for YAML front matter title first
        $inFrontMatter = $false
        foreach ($line in $content) {
            if ($line -eq '---') {
                $inFrontMatter = -not $inFrontMatter
                continue
            }
            if ($inFrontMatter -and $line -match '^title:\s*(.+)$') {
                $result.Title = $matches[1].Trim()
                break
            }
        }
        
        # If no title found in front matter, look for H1
        if (-not $result.Title) {
            foreach ($line in $content) {
                if ($line -match '^#\s+(.+)$') {
                    $result.Title = $matches[1].Trim()
                    break
                }
            }
        }
        
        # Extract description (first paragraph after H1)
        $foundH1 = $false
        $foundEmptyAfterH1 = $false
        $inFrontMatterDesc = $false
        foreach ($line in $content) {
            # Skip front matter
            if ($line -eq '---') {
                $inFrontMatterDesc = -not $inFrontMatterDesc
                continue
            }
            if ($inFrontMatterDesc) { continue }
            
            # Find H1 header
            if (-not $foundH1 -and $line -match '^#\s+') {
                $foundH1 = $true
                continue
            }
            
            # After H1, look for first non-empty line
            if ($foundH1) {
                if ($line.Trim() -eq "") {
                    $foundEmptyAfterH1 = $true
                    continue
                }
                # Skip any additional headers or special formatting
                if ($foundEmptyAfterH1 -and $line -notmatch '^#' -and $line -notmatch '^_.*_$' -and $line -notmatch '^---$') {
                    $result.Description = $line.Trim()
                    break
                }
            }
        }
    }
    catch {
        Write-Warning "Could not read file: $FilePath - $_"
        return $result
    }
    
    # Fallback to filename without extension if no title found
    if (-not $result.Title) {
        $result.Title = [System.IO.Path]::GetFileNameWithoutExtension($FilePath)
    }
    
    return $result
}

function New-GuidesList {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateScript({ Test-Path $_ -PathType Container })]
        [string]$GuidesPath
    )
    
    Write-Host "Processing guides directory: $GuidesPath"
    
    # Get all .md files except index.md
    $mdFiles = Get-ChildItem -Path $GuidesPath -Filter "*.md" | 
    Where-Object { $_.Name -ne "index.md" } |
    Sort-Object Name
    
    if ($mdFiles.Count -eq 0) {
        Write-Host "  No guides found (excluding index.md)"
        return
    }
    
    # Determine the directory name for the title
    $dirName = Split-Path $GuidesPath -Leaf
    $parentPath = Split-Path $GuidesPath -Parent
    
    # Create appropriate title based on directory structure
    $sectionTitle = switch -Regex ($GuidesPath) {
        'docs[/\\]guides$' { "Guides List" }
        'opensidewalks[/\\]guides$' { "OpenSidewalks Guides" }
        'workspaces[/\\]guides$' { "Workspaces Guides" }
        'aviv-scoutroute[/\\]guides$' { "AVIV ScoutRoute Guides" }
        'aviv-scoutroute[/\\]long-form[/\\]guides$' { "Long Form Quest Definition Guides" }
        'josm[/\\]guides$' { "JOSM Guides" }
        default { "$($dirName.Substring(0,1).ToUpper())$($dirName.Substring(1)) Guides" }
    }
    
    # Build content
    $content = @()
    $content += "---"
    $content += "title: $sectionTitle"
    $content += "---"
    $content += ""
    $content += "# $sectionTitle"
    $content += ""
    
    # Add description based on the guides directory
    switch -Regex ($GuidesPath) {
        'docs[/\\]guides$' { 
            $content += "Guides, tutorials, and user manuals produced by TCAT and/or its partners are listed below."
        }
        'opensidewalks[/\\]guides$' { 
            $content += "Guides, tutorials, and user manuals related to OpenSidewalks and produced by TCAT and/or its partners are listed below."
        }
        default {
            # For other guides directories, add a more specific description
            $parentIndexPath = Join-Path $parentPath "index.md"
            if (Test-Path $parentIndexPath) {
                $parentInfo = Get-GuideInfo -FilePath $parentIndexPath
                if ($parentInfo.Title) {
                    $content += "Guides for [$($parentInfo.Title)](../index.md)."
                }
                else {
                    $parentName = Split-Path $parentPath -Leaf
                    $content += "Guides for [$parentName](../index.md)."
                }
            }
        }
    }
    
    # Add back-reference to main guides list (except for main guides index)
    if ($GuidesPath -notmatch 'docs[/\\]guides$') {
        $content += ""
        $guidesIndexPath = Get-RelativePathToGuidesIndex -CurrentPath $GuidesPath
        $content += "_For a list of all guides on the TCAT Wiki, refer to the [Guides List]($guidesIndexPath)._"
    }
    
    $content += ""
    $content += "---"
    $content += ""
    
    # Add each guide
    for ($i = 0; $i -lt $mdFiles.Count; $i++) {
        $file = $mdFiles[$i]
        $guideInfo = Get-GuideInfo -FilePath $file.FullName
        $fileName = $file.Name
        
        $content += "### [$($guideInfo.Title)]($fileName)"
        $content += ""
        
        if ($guideInfo.Description) {
            $content += $guideInfo.Description
        }
        
        # Only add empty line if not the last item
        if ($i -lt ($mdFiles.Count - 1)) {
            $content += ""
        }
    }
    
    # Write the index.md file
    $indexPath = Join-Path $GuidesPath "index.md"
    $content | Set-Content -Path $indexPath -Encoding UTF8
    
    Write-Host "  Generated index.md with $($mdFiles.Count) guides"
}

# Main script execution
Write-Host "Searching for guides directories in docs..."

# Verify docs directory exists
if (-not (Test-Path "docs" -PathType Container)) {
    Write-Error "docs directory not found. Please run this script from the repository root."
    exit 1
}

# Find all directories named "guides" under docs
$guidesDirectories = Get-ChildItem -Path "docs" -Recurse -Directory -ErrorAction Stop | 
Where-Object { $_.Name -eq "guides" }

if ($guidesDirectories.Count -eq 0) {
    Write-Host "No guides directories found."
    exit 0
}

Write-Host "Found $($guidesDirectories.Count) guides directories:"
foreach ($dir in $guidesDirectories) {
    Write-Host "  $($dir.FullName)"
}

Write-Host ""

# Process each guides directory
foreach ($guidesDir in $guidesDirectories) {
    New-GuidesList -GuidesPath $guidesDir.FullName
    Write-Host ""
}

Write-Host "Guide list generation complete!"