#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Navigation Section Generator
# Version: 3.0.1
# Date: 2025-12-31
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Generates and updates the Zensical nav structure in zensical.toml

.DESCRIPTION
    Scans the docs directory structure and updates the navigation section 
    in zensical.toml using proper TOML array-of-objects syntax. Uses frontmatter 
    titles when available, otherwise derives titles from filenames and directory names.

.EXAMPLE
    .\generate-nav.ps1
    Generates navigation section and updates zensical.toml

.NOTES
    Zensical navigation uses TOML format:
    nav = [
      {"Home" = "index.md"},
      {"Section" = [
         "section/index.md",
         {"Page" = "section/page.md"}
      ]}
    ]
#>

#region Helper Functions

<#
.SYNOPSIS
    Extracts the title from a markdown file's frontmatter or first heading.

.DESCRIPTION
    Reads a markdown file and attempts to extract the title from YAML frontmatter.
    Falls back to the first H1 heading if no frontmatter title exists.

.PARAMETER filePath
    The full path to the markdown file to read.

.OUTPUTS
    System.String. The extracted title, or $null if no title found.

.EXAMPLE
    Get-MarkdownTitle -filePath "C:\docs\index.md"
    Returns "Home" if the file has title: Home in frontmatter
#>
function Get-MarkdownTitle {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$filePath
    )
    
    try {
        $content = Get-Content $filePath -Raw -Encoding UTF8 -ErrorAction Stop
        
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
    } catch {
        # Silently return null for missing or unreadable files
    }
    
    return $null
}

<#
.SYNOPSIS
    Escapes a string for safe use in TOML output.

.DESCRIPTION
    Wraps strings in quotes and escapes internal quotes and backslashes as needed
    for valid TOML string output.

.PARAMETER text
    The string to escape for TOML.

.OUTPUTS
    System.String. The TOML-safe escaped string with surrounding quotes.

.EXAMPLE
    Protect-TomlString -text "Hello: World"
    Returns '"Hello: World"'
#>
function Protect-TomlString {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$text
    )
    
    # Escape backslashes first (\ -> \\), then quotes (" -> \")
    $escaped = $text -replace '\\', '\\'
    $escaped = $escaped -replace '"', '\"'
    return "`"$escaped`""
}

<#
.SYNOPSIS
    Converts a filename or directory name to a human-readable title.

.DESCRIPTION
    Transforms kebab-case and snake_case names to Title Case, with special
    handling for known acronyms and project names (OSW, TDEI, JOSM, etc.).

.PARAMETER name
    The filename or directory name to convert.

.OUTPUTS
    System.String. The converted title, or $null for index files.

.EXAMPLE
    ConvertTo-Title -name "opensidewalks"
    Returns "OpenSidewalks"

.EXAMPLE
    ConvertTo-Title -name "user-manual"
    Returns "User Manual"
#>
function ConvertTo-Title {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$name
    )
    
    # Remove file extension
    $name = [System.IO.Path]::GetFileNameWithoutExtension($name)
    
    # Handle special cases - known project names and acronyms
    $titleMap = @{
        'osw'             = 'OSW'
        'tdei'            = 'TDEI'
        'josm'            = 'JOSM'
        'aviv-scoutroute' = 'AVIV ScoutRoute'
        'accessmap'       = 'AccessMap'
        'walksheds'       = 'Walksheds'
        'tdei-walkshed'   = 'TDEI Walkshed'
        'tdei-workspaces' = 'TDEI Workspaces'
        'opensidewalks'   = 'OpenSidewalks'
        'tdei-core'       = 'TDEI Core'
        'index'           = ''
    }
    
    if ($titleMap.ContainsKey($name.ToLower())) {
        $result = $titleMap[$name.ToLower()]
        if ($result) { 
            return $result 
        } else { 
            return $null 
        }
    }
    
    # Convert kebab-case and snake_case to Title Case
    $result = $name -replace '[-_]', ' '
    $result = (Get-Culture).TextInfo.ToTitleCase($result.ToLower())
    
    return $result
}

<#
.SYNOPSIS
    Builds a TOML navigation array for a directory and its contents.

.DESCRIPTION
    Recursively scans a directory to build a Zensical-compatible TOML navigation
    structure. Handles index.md files, subdirectories, and regular markdown files.

.PARAMETER dirPath
    The full path to the directory to process.

.PARAMETER indentLevel
    The current indentation level for formatting (default: 1).

.PARAMETER docsBasePath
    The root docs directory path for calculating relative paths.

.OUTPUTS
    System.String[]. Array of TOML-formatted navigation lines.

.EXAMPLE
    Build-DirectoryNav -dirPath "C:\project\docs\opensidewalks" -indentLevel 1 -docsBasePath "C:\project\docs"
#>
function Build-DirectoryNav {
    [CmdletBinding()]
    [OutputType([string[]])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$dirPath,
        
        [Parameter(Mandatory = $false)]
        [int]$indentLevel = 1,
        
        [Parameter(Mandatory = $true)]
        [string]$docsBasePath
    )
    
    $items = @()
    $indent = "`t" * $indentLevel
    $childIndent = "`t" * ($indentLevel + 1)
    
    # Get directory name and relative path
    $dirInfo = Get-Item $dirPath
    $dirName = $dirInfo.Name
    $resolvedDocsPath = (Resolve-Path $docsBasePath).Path
    $relativePath = $dirPath.Substring($resolvedDocsPath.Length + 1) -replace '\\', '/'
    $dirTitle = ConvertTo-Title $dirName
    
    # Check for index.md
    $indexFile = Join-Path $dirPath "index.md"
    $hasIndex = Test-Path $indexFile
    
    # Get subdirectories and files (excluding resources directory)
    $subDirs = Get-ChildItem -Path $dirPath -Directory | 
        Where-Object { $_.Name -ne 'resources' } | 
        Sort-Object Name
    $mdFiles = Get-ChildItem -Path $dirPath -File -Filter "*.md" | 
        Where-Object { $_.Name -ne 'index.md' } | 
        Sort-Object Name
    
    # Build subitems - each item is a hashtable with Type and properties
    # Type: "simple" (single line item), "nested" (multiline subdirectory structure)
    $subItemsList = @()
    
    # Add index.md first if it exists (as a plain path for section index)
    if ($hasIndex) {
        $subItemsList += @{ Type = "simple"; Content = "`"$relativePath/index.md`""; Indent = $childIndent }
    }
    
    # Add other files in this directory
    foreach ($file in $mdFiles) {
        $fileRelativePath = $file.FullName.Substring($resolvedDocsPath.Length + 1) -replace '\\', '/'
        $fileTitle = Get-MarkdownTitle $file.FullName
        if (-not $fileTitle) {
            $fileTitle = ConvertTo-Title $file.BaseName
        }
        $escapedTitle = Protect-TomlString $fileTitle
        $subItemsList += @{ Type = "simple"; Content = "{$escapedTitle = `"$fileRelativePath`"}"; Indent = $childIndent }
    }
    
    # Add subdirectories recursively
    foreach ($subDir in $subDirs) {
        $subDirItems = @(Build-DirectoryNav -dirPath $subDir.FullName -indentLevel ($indentLevel + 1) -docsBasePath $docsBasePath)
        # Each subdirectory returns an array of lines - treat as a single nested item
        # Only strip trailing comma from the LAST line (the closing bracket line)
        $cleanedLines = @()
        for ($k = 0; $k -lt $subDirItems.Count; $k++) {
            if ($k -eq $subDirItems.Count - 1) {
                $cleanedLines += $subDirItems[$k].TrimEnd(',')
            } else {
                $cleanedLines += $subDirItems[$k]
            }
        }
        $subItemsList += @{ Type = "nested"; Lines = $cleanedLines }
    }
    
    # Build final structure with proper comma placement
    if ($subItemsList.Count -gt 0) {
        $escapedDirTitle = Protect-TomlString $dirTitle
        
        # Check if we can collapse to single line (only one simple item)
        if ($subItemsList.Count -eq 1 -and $subItemsList[0].Type -eq "simple") {
            $singleItem = $subItemsList[0]
            # Collapsed arrays have spaces inside brackets: [ "value" ]
            $items += "$indent{$escapedDirTitle = [ $($singleItem.Content) ]},"
        } else {
            # Multiple items or nested: multiline format
            $items += "$indent{$escapedDirTitle = ["
            
            for ($i = 0; $i -lt $subItemsList.Count; $i++) {
                $subItem = $subItemsList[$i]
                $isLast = ($i -eq $subItemsList.Count - 1)
                $comma = if ($isLast) { "" } else { "," }
                
                if ($subItem.Type -eq "simple") {
                    $items += "$($subItem.Indent)$($subItem.Content)$comma"
                } else {
                    # Nested item - multiple lines
                    $nestedLines = $subItem.Lines
                    for ($j = 0; $j -lt $nestedLines.Count; $j++) {
                        $line = $nestedLines[$j]
                        # Add comma only to the last line of this nested block if it's not the last item overall
                        if ($j -eq $nestedLines.Count - 1) {
                            $items += "$line$comma"
                        } else {
                            $items += $line
                        }
                    }
                }
            }
            
            $items += "$indent]},"
        }
    }
    
    return $items
}

<#
.SYNOPSIS
    Generates the complete TOML navigation section for zensical.toml.

.DESCRIPTION
    Scans the docs directory and generates a complete nav = [...] TOML section
    suitable for insertion into zensical.toml.

.PARAMETER docsBasePath
    The path to the docs directory.

.OUTPUTS
    System.String. The complete TOML navigation section.

.EXAMPLE
    $nav = Build-NavigationToml -docsBasePath "../docs"
#>
function Build-NavigationToml {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$docsBasePath
    )
    
    # Collect all nav items - each item is either a simple line or a multi-line block
    # Type: "simple" = single line, "block" = multi-line directory structure
    $navItemsList = @()
    
    # Handle root index.md specially
    $rootIndex = Join-Path $docsBasePath "index.md"
    if (Test-Path $rootIndex) {
        $homeTitle = Get-MarkdownTitle $rootIndex
        if (-not $homeTitle) { $homeTitle = "Home" }
        $escapedTitle = Protect-TomlString $homeTitle
        $navItemsList += @{ Type = "simple"; Content = "`t{$escapedTitle = `"index.md`"}" }
    }
    
    # Process root level directories (excluding resources and guides-list which is auto-generated)
    $excludedDirs = @('resources', 'guides-list', 'local-storage')
    $rootDirectories = Get-ChildItem -Path $docsBasePath -Directory | 
        Where-Object { $_.Name -notin $excludedDirs } |
        Sort-Object Name
    
    foreach ($dir in $rootDirectories) {
        $subNav = @(Build-DirectoryNav -dirPath $dir.FullName -indentLevel 1 -docsBasePath $docsBasePath)
        # Treat the entire directory output as a single block
        # Only strip trailing comma from the LAST line (the closing bracket line)
        $cleanedLines = @()
        for ($k = 0; $k -lt $subNav.Count; $k++) {
            if ($k -eq $subNav.Count - 1) {
                $cleanedLines += $subNav[$k].TrimEnd(',')
            } else {
                $cleanedLines += $subNav[$k]
            }
        }
        $navItemsList += @{ Type = "block"; Lines = $cleanedLines }
    }
    
    # Add guides-list section if it exists (always at the end before root files)
    $guidesListPath = Join-Path $docsBasePath "guides-list"
    if (Test-Path $guidesListPath) {
        $guidesIndex = Join-Path $guidesListPath "index.md"
        if (Test-Path $guidesIndex) {
            $guidesTitle = Get-MarkdownTitle $guidesIndex
            if (-not $guidesTitle) { $guidesTitle = "Guides List" }
            $escapedTitle = Protect-TomlString $guidesTitle
            $navItemsList += @{ Type = "simple"; Content = "`t{$escapedTitle = `"guides-list/index.md`"}" }
        }
    }
    
    # Process any root-level markdown files (excluding index.md)
    $rootFiles = Get-ChildItem -Path $docsBasePath -File -Filter "*.md" | 
        Where-Object { $_.Name -ne 'index.md' } | 
        Sort-Object Name
    
    foreach ($file in $rootFiles) {
        $fileTitle = Get-MarkdownTitle $file.FullName
        if (-not $fileTitle) {
            $fileTitle = ConvertTo-Title $file.BaseName
        }
        $escapedTitle = Protect-TomlString $fileTitle
        $navItemsList += @{ Type = "simple"; Content = "`t{$escapedTitle = `"$($file.Name)`"}" }
    }
    
    # Build final output with proper comma placement (no trailing comma on last item)
    $navItems = @()
    $navItems += "nav = ["
    
    for ($i = 0; $i -lt $navItemsList.Count; $i++) {
        $item = $navItemsList[$i]
        $isLast = ($i -eq $navItemsList.Count - 1)
        $comma = if ($isLast) { "" } else { "," }
        
        if ($item.Type -eq "simple") {
            $navItems += "$($item.Content)$comma"
        } else {
            # Block item - multiple lines, add comma only to last line
            $blockLines = $item.Lines
            for ($j = 0; $j -lt $blockLines.Count; $j++) {
                $line = $blockLines[$j]
                if ($j -eq $blockLines.Count - 1) {
                    $navItems += "$line$comma"
                } else {
                    $navItems += $line
                }
            }
        }
    }
    
    $navItems += "]"
    
    return ($navItems -join [Environment]::NewLine)
}

<#
.SYNOPSIS
    Updates the nav section in zensical.toml with new navigation content.

.DESCRIPTION
    Reads the existing zensical.toml, locates the nav = [...] section, and
    replaces it with the provided new navigation content. If no nav section
    exists, it will be added after the [project] section.

.PARAMETER zensicalFilePath
    The path to the zensical.toml file.

.PARAMETER newNavContent
    The new TOML navigation content to insert.

.OUTPUTS
    System.Boolean. $true if changes were made, $false if content was already up to date.

.EXAMPLE
    Update-ZensicalNav -zensicalFilePath "../zensical.toml" -newNavContent $navToml
#>
function Update-ZensicalNav {
    [CmdletBinding()]
    [OutputType([bool])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$zensicalFilePath,
        
        [Parameter(Mandatory = $true)]
        [string]$newNavContent
    )
    
    # Read current zensical.toml
    $content = Get-Content $zensicalFilePath -Raw -Encoding UTF8
    
    # Find and replace nav section using regex
    # Match nav = [ ... ] including nested brackets (multiline)
    $navPattern = '(?ms)^nav\s*=\s*\[.*?^\]'
    
    if ($content -match $navPattern) {
        $currentNav = $matches[0]
        
        # Normalize for comparison (remove trailing whitespace)
        $currentNavNormalized = $currentNav -replace '\s+$', ''
        $newNavNormalized = $newNavContent -replace '\s+$', ''
        
        if ($currentNavNormalized -eq $newNavNormalized) {
            return $false  # No changes needed
        }
        
        # Replace the nav section
        $newContent = $content -replace $navPattern, $newNavContent
        Set-Content -Path $zensicalFilePath -Value $newContent -Encoding UTF8 -NoNewline
        return $true
    } else {
        # Nav section doesn't exist - need to add it after [project] section comments
        # Find the end of the initial [project] comment block or after site_description
        
        # Look for a good insertion point - after the nav comment block if it exists
        $navCommentPattern = '(?ms)(#.*nav.*\r?\n(?:#.*\r?\n)*)'
        if ($content -match $navCommentPattern) {
            # Insert after the nav comment block
            $insertPoint = $content.IndexOf($matches[0]) + $matches[0].Length
            $newContent = $content.Insert($insertPoint, $newNavContent + [Environment]::NewLine + [Environment]::NewLine)
        } else {
            # Insert before [project.theme] if it exists
            $themePattern = '(?m)^\[project\.theme\]'
            if ($content -match $themePattern) {
                $insertPoint = $content.IndexOf($matches[0])
                $newContent = $content.Insert($insertPoint, $newNavContent + [Environment]::NewLine + [Environment]::NewLine)
            } else {
                # Append to end of file
                $newContent = $content.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $newNavContent + [Environment]::NewLine
            }
        }
        
        Set-Content -Path $zensicalFilePath -Value $newContent -Encoding UTF8 -NoNewline
        return $true
    }
}

#endregion Helper Functions

#region Main Execution

# Verify we're in the util directory
$currentDirName = Split-Path -Leaf (Get-Location)

if ($currentDirName -ne "util") {
    Write-Host "Error: This script must be run from the util/ directory" -ForegroundColor Red
    Write-Host "Current location: $(Get-Location)" -ForegroundColor Yellow
    exit 1
}

# Detect paths from current working directory
$docsPath = "..\docs"
$zensicalPath = "..\zensical.toml"

# Verify paths exist
if (-not (Test-Path $docsPath)) {
    Write-Host "Error: docs directory not found at $docsPath" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $zensicalPath)) {
    Write-Host "Error: zensical.toml not found at $zensicalPath" -ForegroundColor Red
    exit 1
}

# Main execution
Write-Host "Generating Zensical navigation from '$docsPath'..." -ForegroundColor Cyan

# Build navigation TOML
$navToml = Build-NavigationToml -docsBasePath $docsPath

# Update zensical.toml
Write-Host "Updating zensical.toml..." -ForegroundColor Cyan

try {
    $changed = Update-ZensicalNav -zensicalFilePath $zensicalPath -newNavContent $navToml
    
    if ($changed) {
        Write-Host "Successfully updated zensical.toml navigation section" -ForegroundColor Green
    } else {
        Write-Host "Navigation section is already up to date. No changes needed." -ForegroundColor Green
    }
} catch {
    Write-Host "Error updating zensical.toml: $_" -ForegroundColor Red
    exit 1
}

#endregion Main Execution
 