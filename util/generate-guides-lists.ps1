#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Guides Lists Generator
# Version: 6.0.0
# Date: 2026-01-24
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Generates guide sections in parent index.md files and maintains the main Guides List

.DESCRIPTION
    This script performs two phases for the Zensical-based TCAT Wiki documentation site:

    PHASE 1: For each directory with index.md, creates a "### Guides" section
    (or "### Table of Contents" for user manual pages) listing:
    - User manual subdirectories first (sorted alphabetically)
    - Direct guides in that directory (sorted alphabetically)
    - Subsections for non-user-manual subdirectories with their guides

    PHASE 2: Generates the main guides-list/index.md with hierarchical structure
    across all topics, maintaining consistent ordering with user manuals first
    at each hierarchy level.

    Guide files must have "- Guide" tag in frontmatter.
    User manual index files should have "- User Manual" tag (implies Guide).

    Special frontmatter flags (YAML comments, invisible on built pages):
    - # exclude-from-parent-guides-list - Exclude from parent directory guides sections
    - # exclude-from-main-guides-list - Exclude from main guides list

    User Manual handling:
    - Detected by "- User Manual" tag on index.md
    - Always appear first at their heading level (before regular guides)
    - Use "### Table of Contents" instead of "### Guides" on their own pages
    - Don't get " Guides" suffix in section headers
    - In main guides list: only the user manual itself appears, not its subpages
    - Section headers format: "[Title](link) Guides" (not "[Title Guides](link)")

.EXAMPLE
    .\generate-guides-lists.ps1
#>

# ==============================================================================
# CONSTANTS
# ==============================================================================

$CRLF = "`r`n"
$EXCLUDE_PARENT_FLAG = "exclude-from-parent-guides-list"
$EXCLUDE_MAIN_FLAG = "exclude-from-main-guides-list"

#region Helper Functions
# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

function Get-GuideInfo {
    <#
    .SYNOPSIS
        Extracts guide metadata from a markdown file's frontmatter
    .DESCRIPTION
        Parses YAML frontmatter to extract title, description, guide tags,
        and exclusion flags. Returns a hashtable with the extracted information.
    .OUTPUTS
        Hashtable with keys: Title, Description, IsGuide, IsUserManual, ExcludeFromParent, ExcludeFromMain
    #>
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

        # Extract description: everything between "## Title" heading and one of these markers:
        # - "_For a list of all guides" (regular pages)
        # - "---" horizontal rule (user manual pages)
        # - "### Guides" or "### Table of Contents" section headers
        if ($content -match '(?s)(?:^|\r?\n)##\s+.+?(?:\r?\n)(.*?)(?=\r?\n(?:_For a list of all guides|---|#{2,3} (?:Guides|Table of Contents)))') {
            $descRaw = $matches[1].Trim()
            $descRaw = $descRaw -replace '^[\s\r\n]+|[\s\r\n]+$', ''
            $result.Description = $descRaw
        }
    } catch {
        Write-Warning "Could not read file: $FilePath - $_"
    }

    return $result
}

function Get-DirectoryTitle {
    <#
    .SYNOPSIS
        Extracts the title from an index.md file's frontmatter
    .OUTPUTS
        String containing the title, or empty string if not found
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$IndexPath
    )

    try {
        $content = Get-Content $IndexPath -Raw -ErrorAction Stop

        if ($content -match 'title:\s*(.+?)(?:\r?\n|$)') {
            return $matches[1].Trim()
        }
    } catch {
        Write-Warning "Could not read title from: $IndexPath"
    }

    return ""
}

function Test-IsUserManualDirectory {
    <#
    .SYNOPSIS
        Checks if a directory contains a user manual (index.md with "- User Manual" tag)
    .OUTPUTS
        Boolean indicating whether the directory is a user manual
    #>
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
    <#
    .SYNOPSIS
        Calculates the relative path between two locations, formatted for markdown links
    .DESCRIPTION
        Returns a relative path with forward slashes suitable for use in markdown links
    .OUTPUTS
        String containing the relative path with forward slashes
    #>
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
    <#
    .SYNOPSIS
        Gets all guide files in a directory, sorted with user manuals first
    .DESCRIPTION
        Scans a directory for .md files with guide tags, separating user manuals
        from regular guides and returning them sorted with user manuals first.
    .OUTPUTS
        Array of FileInfo objects for guide files, user manuals first
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory,

        [Parameter(Mandatory = $true)]
        [bool]$ExcludeOwnIndex,

        [Parameter(Mandatory = $true)]
        [string]$ExcludeFlag
    )

    $indexPath = Join-Path $Directory "index.md"
    $userManuals = [System.Collections.ArrayList]@()
    $regularGuides = [System.Collections.ArrayList]@()

    Get-ChildItem -Path $Directory -Filter "*.md" -File | ForEach-Object {
        # Skip if it's the directory's own index.md and we're excluding it
        if ($ExcludeOwnIndex -and $_.FullName -eq $indexPath) {
            return
        }

        $guideInfo = Get-GuideInfo -FilePath $_.FullName

        # Include if it's a guide and not excluded by the flag
        $isExcluded = if ($ExcludeFlag -eq $EXCLUDE_PARENT_FLAG) {
            $guideInfo.ExcludeFromParent
        } else {
            $guideInfo.ExcludeFromMain
        }

        if ($guideInfo.IsGuide -and -not $isExcluded) {
            if ($guideInfo.IsUserManual) {
                [void]$userManuals.Add($_)
            } else {
                [void]$regularGuides.Add($_)
            }
        }
    }

    # Return user manuals first, then regular guides, each sorted by FullName
    $sortedUserManuals = @($userManuals | Sort-Object FullName)
    $sortedRegularGuides = @($regularGuides | Sort-Object FullName)
    return $sortedUserManuals + $sortedRegularGuides
}

function Get-Subdirectories {
    <#
    .SYNOPSIS
        Gets subdirectories that have index.md files, sorted with user manual directories first
    .DESCRIPTION
        Scans a directory for subdirectories containing index.md files,
        excluding the 'resources' directory. Returns them sorted with
        user manual directories appearing before regular directories.
    .OUTPUTS
        Array of DirectoryInfo objects, user manual directories first
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory
    )

    $userManualDirs = [System.Collections.ArrayList]@()
    $regularDirs = [System.Collections.ArrayList]@()

    Get-ChildItem -Path $Directory -Directory | ForEach-Object {
        if ($_.Name -eq "resources") {
            return
        }

        $indexPath = Join-Path $_.FullName "index.md"
        if (Test-Path $indexPath -PathType Leaf) {
            if (Test-IsUserManualDirectory -Directory $_.FullName) {
                [void]$userManualDirs.Add($_)
            } else {
                [void]$regularDirs.Add($_)
            }
        }
    }

    # Return user manual directories first, then regular directories, each sorted by FullName
    $sortedUserManualDirs = @($userManualDirs | Sort-Object FullName)
    $sortedRegularDirs = @($regularDirs | Sort-Object FullName)
    return $sortedUserManualDirs + $sortedRegularDirs
}

function Build-GuideEntry {
    <#
    .SYNOPSIS
        Builds a markdown entry for a guide file
    .DESCRIPTION
        Creates a header line with link to the guide, followed by the
        guide's description if available.
    .OUTPUTS
        String containing the formatted markdown entry
    #>
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
    <#
    .SYNOPSIS
        Builds a markdown section header with link to index page
    .DESCRIPTION
        Creates a header like: ### [Title](path) Guides
        User manuals don't get the " Guides" suffix after the link
    #>
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
    # Format: "### [Title](link) Guides" - User manuals don't get " Guides" suffix
    $suffix = if ($IsUserManual) { "" } else { " Guides" }

    return "$HeaderLevel [$Title]($relativePath)$suffix$CRLF$CRLF"
}

function Get-TcatWikiSection {
    <#
    .SYNOPSIS
        Returns the static TCAT Wiki section content for the main guides list
    .DESCRIPTION
        Generates the TCAT Wiki section that appears at the end of the main guides list,
        containing links to wiki-level documentation like CONTRIBUTING.md.
    .OUTPUTS
        String containing the markdown content for the TCAT Wiki section
    #>
    return "### TCAT Wiki Guides$CRLF$CRLF#### [Contributing](../CONTRIBUTING.md)$CRLF$CRLF" +
    "This guide explains how to contribute to the TCAT Wiki.$CRLF"
}

function Get-AllGuidesAtLevel {
    <#
    .SYNOPSIS
        Gets all guide entries (user manuals and regular guides) at a directory level
    .DESCRIPTION
        Collects user manual subdirectories and regular guide files from a directory,
        returning them sorted with user manuals first. This ensures proper ordering
        where user manuals always appear before regular guides at the same heading level.
    .OUTPUTS
        Array of hashtables with Type ('UserManual' or 'Guide'), Path, and Info properties
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory,

        [Parameter(Mandatory = $true)]
        [string]$ExcludeFlag,

        [Parameter(Mandatory = $false)]
        [AllowNull()]
        [array]$Subdirectories = @()
    )

    $userManualEntries = [System.Collections.ArrayList]@()
    $regularGuideEntries = [System.Collections.ArrayList]@()

    # Check subdirectories for user manuals (if any exist)
    if ($Subdirectories) {
        foreach ($subdir in $Subdirectories) {
            if (Test-IsUserManualDirectory -Directory $subdir.FullName) {
                $indexPath = Join-Path $subdir.FullName "index.md"
                $guideInfo = Get-GuideInfo -FilePath $indexPath

                $isExcluded = if ($ExcludeFlag -eq $EXCLUDE_PARENT_FLAG) {
                    $guideInfo.ExcludeFromParent
                } else {
                    $guideInfo.ExcludeFromMain
                }

                if ($guideInfo.IsGuide -and -not $isExcluded) {
                    [void]$userManualEntries.Add(@{
                            Type      = 'UserManual'
                            Path      = $indexPath
                            Info      = $guideInfo
                            Directory = $subdir
                        })
                }
            }
        }
    }

    # Get regular guide files from the directory
    $guides = Get-GuidesInDirectory -Directory $Directory -ExcludeOwnIndex $true -ExcludeFlag $ExcludeFlag
    foreach ($guide in $guides) {
        $guideInfo = Get-GuideInfo -FilePath $guide.FullName
        [void]$regularGuideEntries.Add(@{
                Type = 'Guide'
                Path = $guide.FullName
                Info = $guideInfo
                File = $guide
            })
    }

    # Return user manuals first (sorted), then regular guides (sorted)
    $sorted = @($userManualEntries | Sort-Object { $_.Path }) + @($regularGuideEntries | Sort-Object { $_.Path })
    return $sorted
}

#endregion Helper Functions

#region Main Functions
# ==============================================================================
# MAIN FUNCTIONS
# ==============================================================================

function Update-ParentGuidesSection {
    <#
    .SYNOPSIS
        Updates the ### Guides (or ### Table of Contents) section in a directory's index.md file
    .DESCRIPTION
        Generates and inserts the Guides section content, listing user manuals first,
        then direct guides, then subsections for non-user-manual subdirectories.
        User manual pages get "### Table of Contents" instead of "### Guides".
        Replaces any existing ### Guides or ### Table of Contents section (or legacy ## versions).
    #>
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo]$Directory
    )

    $indexPath = Join-Path $Directory.FullName "index.md"
    $parentDir = $Directory.FullName

    # Get subdirectories (sorted with user manual directories first)
    $subdirs = Get-Subdirectories -Directory $parentDir

    # Check if there's anything to add using Get-AllGuidesAtLevel
    $allEntries = Get-AllGuidesAtLevel -Directory $parentDir -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $subdirs

    # Also check subdirectories for nested content
    $hasSubdirContent = $false
    foreach ($subdir in $subdirs) {
        if (Test-IsUserManualDirectory -Directory $subdir.FullName) {
            continue  # User manuals are already in allEntries
        }
        $subdirSubdirs = Get-Subdirectories -Directory $subdir.FullName
        $subdirEntries = Get-AllGuidesAtLevel -Directory $subdir.FullName -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $subdirSubdirs
        if ($subdirEntries.Count -gt 0) {
            $hasSubdirContent = $true
            break
        }
    }

    if ($allEntries.Count -eq 0 -and -not $hasSubdirContent) {
        return
    }

    # Check if this directory is a user manual - use "Table of Contents" instead of "Guides"
    $isUserManual = Test-IsUserManualDirectory -Directory $parentDir
    $sectionTitle = if ($isUserManual) { "Table of Contents" } else { "Guides" }

    # Build guides section header
    $pageTitle = Get-DirectoryTitle -IndexPath $indexPath
    $dirDepth = ($indexPath -replace [regex]::Escape($script:docsPath), '' -split '\\' | Where-Object { $_ -ne '' }).Count - 1
    $relPathToGuidesList = ('../' * $dirDepth) + 'guides-list/index.md'

    $guidesSection = "$CRLF$CRLF### $sectionTitle$CRLF$CRLF"
    $guidesSection += "$pageTitle $sectionTitle$CRLF$CRLF"

    # Only include the Guides List reference for non-user-manual pages
    if (-not $isUserManual) {
        $guidesSection += "_For a list of all guides on the TCAT Wiki, refer to the [Guides List]($relPathToGuidesList)._$CRLF$CRLF"
    }

    # Add all top-level entries (user manuals and direct guides, sorted with user manuals first)
    foreach ($entry in $allEntries) {
        if ($entry.Type -eq 'UserManual') {
            # User manual: show as a single guide entry (no child guides listed)
            $guidesSection += Build-GuideEntry -GuideFile (Get-Item $entry.Path) -FromPath $parentDir -HeaderLevel "####"
            $guidesSection += $CRLF
        } else {
            # Regular guide file
            $guidesSection += Build-GuideEntry -GuideFile $entry.File -FromPath $parentDir -HeaderLevel "####"
            $guidesSection += $CRLF
        }
    }

    # Add subdirectory subsections (non-user-manual directories only)
    foreach ($subdir in $subdirs) {
        # Skip user manual directories - they were already added above
        if (Test-IsUserManualDirectory -Directory $subdir.FullName) {
            continue
        }

        $subdirIndexPath = Join-Path $subdir.FullName "index.md"
        $subdirTitle = Get-DirectoryTitle -IndexPath $subdirIndexPath

        # Get all entries for this subdirectory (user manuals + guides)
        $subdirSubdirs = Get-Subdirectories -Directory $subdir.FullName
        $subdirEntries = Get-AllGuidesAtLevel -Directory $subdir.FullName -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $subdirSubdirs

        if ($subdirEntries.Count -eq 0) {
            continue
        }

        $guidesSection += Build-SectionHeader -Title $subdirTitle -IndexPath $subdirIndexPath -FromPath $parentDir -HeaderLevel "####" -IsUserManual $false

        foreach ($subdirEntry in $subdirEntries) {
            if ($subdirEntry.Type -eq 'UserManual') {
                $guidesSection += Build-GuideEntry -GuideFile (Get-Item $subdirEntry.Path) -FromPath $parentDir -HeaderLevel "#####"
            } else {
                $guidesSection += Build-GuideEntry -GuideFile $subdirEntry.File -FromPath $parentDir -HeaderLevel "#####"
            }
            $guidesSection += $CRLF
        }
    }

    # Read existing content and replace ### Guides or ### Table of Contents section (or legacy ## versions)
    $content = Get-Content $indexPath -Raw -ErrorAction Stop
    $content = $content -replace '(?s)\r?\n\r?\n#{2,3} (Guides|Table of Contents)\r?\n.*$', ''

    $content = $content.TrimEnd() + $guidesSection.TrimEnd()

    Set-Content -Path $indexPath -Value $content -Encoding UTF8

    $dirName = $Directory.Name
    Write-Host "  ✓ Updated: $dirName"
}

function Build-MainGuidesList {
    <#
    .SYNOPSIS
        Builds the main guides-list/index.md content
    .DESCRIPTION
        Generates a hierarchical guides list organized by topic, with H3 headers
        for each top-level topic. User manuals always appear first at each level.
        Uses script-scoped $content variable for nested function access.
    .OUTPUTS
        String containing the complete markdown content for guides-list/index.md
    #>
    param(
        [Parameter(Mandatory = $true)]
        [array]$AllDirectories,

        [Parameter(Mandatory = $true)]
        [string]$DocsPath
    )

    # Start with header - use script scope so nested function can modify it
    $script:content = "---${CRLF}title: Guides List${CRLF}---${CRLF}${CRLF}<!-- @format -->${CRLF}${CRLF}"
    $script:content += "## Guides List${CRLF}${CRLF}"
    $script:content += "Guides, tutorials, and user manuals produced by TCAT and/or its partners are listed below.${CRLF}${CRLF}"

    $guidesListPath = Join-Path $DocsPath "guides-list"

    # Group directories by top-level topic
    $topicGroups = @{}

    foreach ($dir in $AllDirectories) {
        # Skip guides-list itself
        if ($dir.FullName -match 'guides-list$') {
            continue
        }

        # Get the top-level topic directory (e.g., "accessmap", "opensidewalks", "tdei")
        $relativePath = $dir.FullName -replace [regex]::Escape($DocsPath), ''
        $pathParts = @($relativePath -split '\\' | Where-Object { $_ -ne '' })

        if ($pathParts.Count -eq 0) {
            continue
        }

        $topLevelTopic = $pathParts[0]

        if (-not $topicGroups.ContainsKey($topLevelTopic)) {
            $topicGroups[$topLevelTopic] = [System.Collections.ArrayList]@()
        }

        [void]$topicGroups[$topLevelTopic].Add($dir)
    }

    # Process each top-level topic
    foreach ($topic in ($topicGroups.Keys | Sort-Object)) {
        $directories = $topicGroups[$topic]

        # Get the top-level directory for this topic
        $topicDir = $directories | Where-Object {
            $relativePath = $_.FullName -replace [regex]::Escape($DocsPath), ''
            $pathParts = @($relativePath -split '\\' | Where-Object { $_ -ne '' })
            $pathParts.Count -eq 1
        } | Select-Object -First 1

        if (-not $topicDir) {
            continue
        }

        $topicIndexPath = Join-Path $topicDir.FullName "index.md"
        $topicTitle = Get-DirectoryTitle -IndexPath $topicIndexPath

        # Check if there are any guides in this topic
        $hasGuides = $false
        foreach ($dir in $directories) {
            $indexPath = Join-Path $dir.FullName "index.md"
            $isUserManual = Test-IsUserManualDirectory -Directory $dir.FullName

            if ($isUserManual) {
                $indexInfo = Get-GuideInfo -FilePath $indexPath
                if ($indexInfo.IsGuide -and -not $indexInfo.ExcludeFromMain) {
                    $hasGuides = $true
                    break
                }
            } else {
                $guides = Get-GuidesInDirectory -Directory $dir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_MAIN_FLAG
                if ($guides.Count -gt 0) {
                    $hasGuides = $true
                    break
                }
            }
        }

        if (-not $hasGuides) {
            continue
        }

        # Add H3 header for the topic
        $topicRelativePath = Get-RelativeMarkdownPath -FromPath $guidesListPath -ToPath $topicIndexPath
        $script:content += "### [$topicTitle]($topicRelativePath)${CRLF}${CRLF}"

        # Group directories by parent path for hierarchical processing
        $dirsByParent = @{}
        foreach ($dir in $directories) {
            $parentPath = Split-Path -Parent $dir.FullName
            if (-not $dirsByParent.ContainsKey($parentPath)) {
                $dirsByParent[$parentPath] = [System.Collections.ArrayList]@()
            }
            [void]$dirsByParent[$parentPath].Add($dir)
        }

        # Recursive function to process a directory and its children
        # Uses Get-AllGuidesAtLevel to ensure user manuals appear before regular guides at each level
        # Note: User manuals directly under the topic directory are handled separately before this is called
        function Invoke-DirectoryHierarchyProcessing {
            param([string]$ParentPath, [int]$Depth)

            if (-not $dirsByParent.ContainsKey($ParentPath)) {
                return
            }

            # Get children at this level, separate user manuals from regular dirs
            $children = $dirsByParent[$ParentPath]
            $userManualDirs = [System.Collections.ArrayList]@()
            $regularDirs = [System.Collections.ArrayList]@()

            foreach ($child in $children) {
                if (Test-IsUserManualDirectory -Directory $child.FullName) {
                    # Skip user manuals at Depth 1 - they were already processed at the topic level
                    if ($Depth -gt 1) {
                        [void]$userManualDirs.Add($child)
                    }
                } else {
                    [void]$regularDirs.Add($child)
                }
            }

            # Process user manual directories first (they appear as guide entries, not sections)
            foreach ($dir in ($userManualDirs | Sort-Object FullName)) {
                $indexPath = Join-Path $dir.FullName "index.md"
                $indexInfo = Get-GuideInfo -FilePath $indexPath

                if (-not $indexInfo.IsGuide -or $indexInfo.ExcludeFromMain) {
                    continue
                }

                $relativePath = $dir.FullName -replace [regex]::Escape($DocsPath), ''
                $pathParts = @($relativePath -split '\\' | Where-Object { $_ -ne '' })
                $depthInTopic = $pathParts.Count - 1

                # User manuals appear at guide level (one deeper than section header would be)
                $headerLevel = '#' * ($depthInTopic + 3)
                $entry = Build-GuideEntry -GuideFile (Get-Item $indexPath) -FromPath $guidesListPath -HeaderLevel $headerLevel
                $script:content += $entry + $CRLF
            }

            # Process regular directories (they become section headers with their own content)
            foreach ($dir in ($regularDirs | Sort-Object FullName)) {
                $indexPath = Join-Path $dir.FullName "index.md"
                $relativePath = $dir.FullName -replace [regex]::Escape($DocsPath), ''
                $pathParts = @($relativePath -split '\\' | Where-Object { $_ -ne '' })
                $depthInTopic = $pathParts.Count - 1

                # Check if this directory has any content (guides or children with content)
                $guides = Get-GuidesInDirectory -Directory $dir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_MAIN_FLAG
                $hasChildren = $dirsByParent.ContainsKey($dir.FullName)

                # Also check for user manual children
                $childUserManuals = @()
                if ($hasChildren -and $dirsByParent[$dir.FullName]) {
                    $childUserManuals = @($dirsByParent[$dir.FullName] | Where-Object {
                            $_ -and $_.FullName -and (Test-IsUserManualDirectory -Directory $_.FullName)
                        })
                }

                if ($guides.Count -eq 0 -and -not $hasChildren) {
                    continue
                }

                $dirTitle = Get-DirectoryTitle -IndexPath $indexPath

                # Add section header if not top-level
                if ($depthInTopic -gt 0) {
                    $headerLevel = '#' * ($depthInTopic + 3)
                    $sectionHeader = Build-SectionHeader -Title $dirTitle -IndexPath $indexPath -FromPath $guidesListPath -HeaderLevel $headerLevel -IsUserManual $false
                    $script:content += $sectionHeader
                }

                # First, add user manual children (they should appear first under this section)
                foreach ($umDir in ($childUserManuals | Sort-Object FullName)) {
                    $umIndexPath = Join-Path $umDir.FullName "index.md"
                    $umInfo = Get-GuideInfo -FilePath $umIndexPath

                    if (-not $umInfo.IsGuide -or $umInfo.ExcludeFromMain) {
                        continue
                    }

                    $guideHeaderLevel = '#' * ($depthInTopic + 4)
                    $entry = Build-GuideEntry -GuideFile (Get-Item $umIndexPath) -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
                    $script:content += $entry + $CRLF
                }

                # Then add direct guides
                foreach ($guide in $guides) {
                    $guideHeaderLevel = '#' * ($depthInTopic + 4)
                    $guideEntry = Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
                    $script:content += $guideEntry + $CRLF
                }

                # Recursively process non-user-manual children
                if ($hasChildren -and $dirsByParent[$dir.FullName]) {
                    $nonUmChildren = @($dirsByParent[$dir.FullName] | Where-Object {
                            $_ -and $_.FullName -and -not (Test-IsUserManualDirectory -Directory $_.FullName)
                        })
                    if ($nonUmChildren.Count -gt 0) {
                        Invoke-DirectoryHierarchyProcessing -ParentPath $dir.FullName -Depth ($Depth + 1)
                    }
                }
            }
        }

        # First, check for user manual directories directly under the topic and add them first
        if ($dirsByParent.ContainsKey($topicDir.FullName)) {
            $topicChildren = $dirsByParent[$topicDir.FullName]
            foreach ($child in ($topicChildren | Sort-Object FullName)) {
                if (Test-IsUserManualDirectory -Directory $child.FullName) {
                    $umIndexPath = Join-Path $child.FullName "index.md"
                    $umInfo = Get-GuideInfo -FilePath $umIndexPath

                    if ($umInfo.IsGuide -and -not $umInfo.ExcludeFromMain) {
                        $entry = Build-GuideEntry -GuideFile (Get-Item $umIndexPath) -FromPath $guidesListPath -HeaderLevel '####'
                        $script:content += $entry + $CRLF
                    }
                }
            }
        }

        # Then add any regular guides directly in the topic directory
        $topicGuides = Get-GuidesInDirectory -Directory $topicDir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_MAIN_FLAG
        foreach ($guide in $topicGuides) {
            $guideHeaderLevel = '####'  # H4 for top-level guides under the topic
            $script:content += Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
            $script:content += $CRLF
        }

        # Finally process non-user-manual subdirectories and their children recursively
        Invoke-DirectoryHierarchyProcessing -ParentPath $topicDir.FullName -Depth 1
    }

    # Add TCAT Wiki section
    $script:content += Get-TcatWikiSection

    return $script:content
}

#endregion Main Functions

# ==============================================================================
# MAIN SCRIPT
# ==============================================================================

Write-Host ""
Write-Host "TCAT Wiki - Guides Lists Generator v5.1.0"
Write-Host "==========================================="
Write-Host ""

# Find docs path
$script:docsPath = ""
if (Test-Path "..\docs") {
    $script:docsPath = Resolve-Path "..\docs"
} elseif (Test-Path "docs") {
    $script:docsPath = Resolve-Path "docs"
} else {
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
    } catch {
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
} catch {
    Write-Error "Failed generating main guides list: $_"
    exit 1
}

Write-Host ""
Write-Host "==========================================="
Write-Host "Guides list generation complete!"
Write-Host ""
