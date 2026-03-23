#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Guides Lists Generator
# Version: 10.0.0
# Date: 2026-03-23
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Generates guide sections in parent index.md files and maintains the main Guides List

.DESCRIPTION
    This script performs two phases for the Zensical-based TCAT Wiki documentation site:

    PHASE 1: For each directory with index.md, creates a "### Guides" section
    (or "### Table of Contents" for user manual pages) listing:
    - Tutorials first (in a "Tutorials" subsection)
    - User manual subdirectories next (sorted alphabetically)
    - Direct guides in that directory (sorted alphabetically)
    - Subsections for non-user-manual subdirectories with their guides

    PHASE 2: Generates the main guides-list/index.md with hierarchical structure
    across all topics, maintaining consistent ordering with tutorials first,
    then user manuals, then regular guides at each hierarchy level.

    Guide files must have "- Guide" tag in frontmatter.
    User manual index files should have "- User Manual" tag (implies Guide).
    Tutorial files should have "- Tutorial" tag (implies Guide).

    Special frontmatter flags (YAML comments, invisible on built pages):
    - # exclude-from-parent-guides-list - Exclude from parent directory guides sections
    - # exclude-from-main-guides-list - Exclude from main guides list

    Tutorial handling:
    - Detected by "- Tutorial" tag in frontmatter (implies Guide)
    - May be single files or multi-page directories (with index.md tagged "- Tutorial")
    - Single-file tutorials may live in a tutorial/ subdirectory or directly in a topic directory
    - Multi-page tutorials may live in a tutorial/ subdirectory or as direct children of any directory
    - Multi-page tutorials are treated like user manuals: only the index appears in parent/main listings
    - Multi-page tutorial pages get "### Table of Contents" instead of "### Guides"
    - Always appear first at their heading level (before user manuals and regular guides)
    - Listed under a "Tutorials" subsection header at each level

    User Manual handling:
    - Detected by "- User Manual" tag on index.md
    - Always appear after tutorials but before regular guides at their heading level
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
        nav_order, and exclusion flags. Returns a hashtable with the extracted information.
    .OUTPUTS
        Hashtable with keys: Title, Description, IsGuide, IsUserManual, IsTutorial, ExcludeFromParent, ExcludeFromMain, NavOrder
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
        IsTutorial        = $false
        ExcludeFromParent = $false
        ExcludeFromMain   = $false
        NavOrder          = $null
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
            if ($frontmatter -match '- Tutorial') {
                $result.IsTutorial = $true
                $result.IsGuide = $true  # Tutorials are also guides
            }
            if ($frontmatter -match "# $EXCLUDE_PARENT_FLAG") {
                $result.ExcludeFromParent = $true
            }
            if ($frontmatter -match "# $EXCLUDE_MAIN_FLAG") {
                $result.ExcludeFromMain = $true
            }
            # Extract nav_order if present
            if ($frontmatter -match 'nav_order:\s*(\d+)') {
                $result.NavOrder = [int]$matches[1]
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

function Test-IsTutorialDirectory {
    <#
    .SYNOPSIS
        Checks if a directory contains a tutorial (index.md with "- Tutorial" tag)
    .OUTPUTS
        Boolean indicating whether the directory is a tutorial
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory
    )

    $indexPath = Join-Path $Directory "index.md"
    if (Test-Path $indexPath -PathType Leaf) {
        $guideInfo = Get-GuideInfo -FilePath $indexPath
        return $guideInfo.IsTutorial
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
        Gets all guide files in a directory, sorted with tutorials first, then user manuals
    .DESCRIPTION
        Scans a directory for .md files with guide tags, separating tutorials and
        user manuals from regular guides and returning them sorted with tutorials
        first, then user manuals, then regular guides. Also scans any tutorial/
        subdirectory for additional guide files.
    .OUTPUTS
        Array of FileInfo objects for guide files, tutorials first, then user manuals
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
    $tutorials = [System.Collections.ArrayList]@()
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
            $entry = @{
                File     = $_
                NavOrder = $guideInfo.NavOrder
            }
            if ($guideInfo.IsTutorial) {
                [void]$tutorials.Add($entry)
            } elseif ($guideInfo.IsUserManual) {
                [void]$userManuals.Add($entry)
            } else {
                [void]$regularGuides.Add($entry)
            }
        }
    }

    # Also scan tutorial/ subdirectory for additional guide files and multi-page tutorials
    $tutorialSubdir = Join-Path $Directory "tutorial"
    if (Test-Path $tutorialSubdir -PathType Container) {
        # Scan single-file guides directly in tutorial/
        Get-ChildItem -Path $tutorialSubdir -Filter "*.md" -File | ForEach-Object {
            $guideInfo = Get-GuideInfo -FilePath $_.FullName

            $isExcluded = if ($ExcludeFlag -eq $EXCLUDE_PARENT_FLAG) {
                $guideInfo.ExcludeFromParent
            } else {
                $guideInfo.ExcludeFromMain
            }

            if ($guideInfo.IsGuide -and -not $isExcluded) {
                $entry = @{
                    File     = $_
                    NavOrder = $guideInfo.NavOrder
                }
                if ($guideInfo.IsTutorial) {
                    [void]$tutorials.Add($entry)
                } elseif ($guideInfo.IsUserManual) {
                    [void]$userManuals.Add($entry)
                } else {
                    [void]$regularGuides.Add($entry)
                }
            }
        }

        # Scan multi-page tutorial/user-manual directories within tutorial/
        Get-ChildItem -Path $tutorialSubdir -Directory | ForEach-Object {
            $subIndexPath = Join-Path $_.FullName "index.md"
            if (Test-Path $subIndexPath -PathType Leaf) {
                $guideInfo = Get-GuideInfo -FilePath $subIndexPath

                $isExcluded = if ($ExcludeFlag -eq $EXCLUDE_PARENT_FLAG) {
                    $guideInfo.ExcludeFromParent
                } else {
                    $guideInfo.ExcludeFromMain
                }

                if ($guideInfo.IsGuide -and -not $isExcluded) {
                    $indexFile = Get-Item $subIndexPath
                    $entry = @{
                        File     = $indexFile
                        NavOrder = $guideInfo.NavOrder
                    }
                    if ($guideInfo.IsTutorial) {
                        [void]$tutorials.Add($entry)
                    } elseif ($guideInfo.IsUserManual) {
                        [void]$userManuals.Add($entry)
                    } else {
                        [void]$regularGuides.Add($entry)
                    }
                }
            }
        }
    }

    # Sort by nav_order first (items with nav_order come before those without), then alphabetically
    $sortedTutorials = @($tutorials | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.File.FullName } } | ForEach-Object { $_.File })
    $sortedUserManuals = @($userManuals | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.File.FullName } } | ForEach-Object { $_.File })
    $sortedRegularGuides = @($regularGuides | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.File.FullName } } | ForEach-Object { $_.File })
    return $sortedTutorials + $sortedUserManuals + $sortedRegularGuides
}

function Get-Subdirectories {
    <#
    .SYNOPSIS
        Gets subdirectories that have index.md files, sorted with tutorials first, then user manuals
    .DESCRIPTION
        Scans a directory for subdirectories containing index.md files,
        excluding the 'resources' and 'tutorial' directories. Returns them sorted with
        tutorial directories first, then user manual directories, then regular directories,
        each group sorted by nav_order then alphabetically.
    .OUTPUTS
        Array of DirectoryInfo objects, tutorial directories first, then user manuals
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$Directory
    )

    $tutorialDirs = [System.Collections.ArrayList]@()
    $userManualDirs = [System.Collections.ArrayList]@()
    $regularDirs = [System.Collections.ArrayList]@()

    Get-ChildItem -Path $Directory -Directory | ForEach-Object {
        if ($_.Name -eq "resources" -or $_.Name -eq "tutorial") {
            return
        }

        $indexPath = Join-Path $_.FullName "index.md"
        if (Test-Path $indexPath -PathType Leaf) {
            $guideInfo = Get-GuideInfo -FilePath $indexPath
            $entry = @{
                Directory = $_
                NavOrder  = $guideInfo.NavOrder
            }
            if (Test-IsTutorialDirectory -Directory $_.FullName) {
                [void]$tutorialDirs.Add($entry)
            } elseif (Test-IsUserManualDirectory -Directory $_.FullName) {
                [void]$userManualDirs.Add($entry)
            } else {
                [void]$regularDirs.Add($entry)
            }
        }
    }

    # Sort by nav_order first (items with nav_order come before those without), then alphabetically
    $sortedTutorialDirs = @($tutorialDirs | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } } | ForEach-Object { $_.Directory })
    $sortedUserManualDirs = @($userManualDirs | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } } | ForEach-Object { $_.Directory })
    $sortedRegularDirs = @($regularDirs | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } } | ForEach-Object { $_.Directory })
    return $sortedTutorialDirs + $sortedUserManualDirs + $sortedRegularDirs
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

    $header = "$HeaderLevel [$Title]($relativePath)$suffix$CRLF"

    # Extract and include the description from the index page
    $guideInfo = Get-GuideInfo -FilePath $IndexPath
    if ($guideInfo.Description) {
        $header += "$CRLF$($guideInfo.Description)$CRLF"
    }

    $header += $CRLF
    return $header
}

function Get-AllGuidesAtLevel {
    <#
    .SYNOPSIS
        Gets all guide entries (tutorials, user manuals, and regular guides) at a directory level
    .DESCRIPTION
        Collects tutorial files, user manual subdirectories, and regular guide files from a
        directory, returning them sorted with tutorials first, then user manuals, then regular
        guides. Within each category, items are sorted by nav_order first, then alphabetically.
    .OUTPUTS
        Array of hashtables with Type ('Tutorial', 'UserManual', or 'Guide'), Path, Info, and NavOrder properties
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

    $tutorialEntries = [System.Collections.ArrayList]@()
    $userManualEntries = [System.Collections.ArrayList]@()
    $regularGuideEntries = [System.Collections.ArrayList]@()

    # Check subdirectories for tutorial directories and user manuals (if any exist)
    if ($Subdirectories) {
        foreach ($subdir in $Subdirectories) {
            if (Test-IsTutorialDirectory -Directory $subdir.FullName) {
                $indexPath = Join-Path $subdir.FullName "index.md"
                $guideInfo = Get-GuideInfo -FilePath $indexPath

                $isExcluded = if ($ExcludeFlag -eq $EXCLUDE_PARENT_FLAG) {
                    $guideInfo.ExcludeFromParent
                } else {
                    $guideInfo.ExcludeFromMain
                }

                if ($guideInfo.IsGuide -and -not $isExcluded) {
                    [void]$tutorialEntries.Add(@{
                            Type      = 'Tutorial'
                            Path      = $indexPath
                            Info      = $guideInfo
                            File      = (Get-Item $indexPath)
                            Directory = $subdir
                            NavOrder  = $guideInfo.NavOrder
                        })
                }
            } elseif (Test-IsUserManualDirectory -Directory $subdir.FullName) {
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
                            NavOrder  = $guideInfo.NavOrder
                        })
                }
            }
        }
    }

    # Get guide files from the directory (already sorted by Get-GuidesInDirectory)
    $guides = Get-GuidesInDirectory -Directory $Directory -ExcludeOwnIndex $true -ExcludeFlag $ExcludeFlag
    foreach ($guide in $guides) {
        $guideInfo = Get-GuideInfo -FilePath $guide.FullName
        if ($guideInfo.IsTutorial) {
            [void]$tutorialEntries.Add(@{
                    Type     = 'Tutorial'
                    Path     = $guide.FullName
                    Info     = $guideInfo
                    File     = $guide
                    NavOrder = $guideInfo.NavOrder
                })
        } else {
            [void]$regularGuideEntries.Add(@{
                    Type     = 'Guide'
                    Path     = $guide.FullName
                    Info     = $guideInfo
                    File     = $guide
                    NavOrder = $guideInfo.NavOrder
                })
        }
    }

    # Sort by nav_order first (items with nav_order come before those without), then alphabetically
    # Tutorials first, then user manuals, then regular guides
    $sortedTutorials = @($tutorialEntries | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Path } })
    $sortedUserManuals = @($userManualEntries | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Path } })
    $sortedRegularGuides = @($regularGuideEntries | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Path } })
    return $sortedTutorials + $sortedUserManuals + $sortedRegularGuides
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
        if (Test-IsTutorialDirectory -Directory $subdir.FullName) {
            continue  # Tutorial directories are already in allEntries
        }
        $subdirSubdirs = Get-Subdirectories -Directory $subdir.FullName
        $subdirEntries = Get-AllGuidesAtLevel -Directory $subdir.FullName -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $subdirSubdirs
        if ($subdirEntries.Count -gt 0) {
            $hasSubdirContent = $true
            break
        }
        # A subdirectory with no visible children still counts as content
        # if its own index.md is a guide (e.g. all children excluded from parent)
        $subdirIndexPath = Join-Path $subdir.FullName "index.md"
        if (Test-Path $subdirIndexPath -PathType Leaf) {
            $subdirGuideInfo = Get-GuideInfo -FilePath $subdirIndexPath
            if ($subdirGuideInfo.IsGuide -and -not $subdirGuideInfo.ExcludeFromParent) {
                $hasSubdirContent = $true
                break
            }
        }
    }

    if ($allEntries.Count -eq 0 -and -not $hasSubdirContent) {
        return
    }

    # Check if this directory is a user manual or tutorial - use "Table of Contents" instead of "Guides"
    $isUserManual = Test-IsUserManualDirectory -Directory $parentDir
    $isTutorial = Test-IsTutorialDirectory -Directory $parentDir
    $sectionTitle = if ($isUserManual -or $isTutorial) { "Table of Contents" } else { "Guides" }

    # Build guides section header
    $pageTitle = Get-DirectoryTitle -IndexPath $indexPath
    $dirDepth = ($indexPath -replace [regex]::Escape($script:docsPath), '' -split '\\' | Where-Object { $_ -ne '' }).Count - 1
    $relPathToGuidesList = ('../' * $dirDepth) + 'guides-list/index.md'

    $guidesSection = "$CRLF$CRLF### $sectionTitle$CRLF$CRLF"
    $guidesSection += "$pageTitle $sectionTitle$CRLF$CRLF"

    # Only include the Guides List reference for non-user-manual/non-tutorial pages
    if (-not $isUserManual -and -not $isTutorial) {
        $guidesSection += "_For a list of all guides on the TCAT Wiki, refer to the [Guides List]($relPathToGuidesList)._{ .guides-list-ref }$CRLF$CRLF"
    }

    # Separate entries by type for proper ordering
    $tutorialEntries = @($allEntries | Where-Object { $_.Type -eq 'Tutorial' })
    $userManualEntries = @($allEntries | Where-Object { $_.Type -eq 'UserManual' })
    $regularGuideEntries = @($allEntries | Where-Object { $_.Type -eq 'Guide' })

    # Add Tutorials section if any exist (listed first)
    if ($tutorialEntries.Count -gt 0) {
        $guidesSection += "#### Tutorials$CRLF$CRLF"
        foreach ($entry in $tutorialEntries) {
            $guidesSection += Build-GuideEntry -GuideFile $entry.File -FromPath $parentDir -HeaderLevel "#####"
            $guidesSection += $CRLF
        }
    }

    # Add User Manual entries
    foreach ($entry in $userManualEntries) {
        $guidesSection += Build-GuideEntry -GuideFile (Get-Item $entry.Path) -FromPath $parentDir -HeaderLevel "####"
        $guidesSection += $CRLF
    }

    # Add Regular Guide entries
    foreach ($entry in $regularGuideEntries) {
        $guidesSection += Build-GuideEntry -GuideFile $entry.File -FromPath $parentDir -HeaderLevel "####"
        $guidesSection += $CRLF
    }

    # Add subdirectory subsections (non-user-manual/non-tutorial directories only)
    foreach ($subdir in $subdirs) {
        # Skip user manual and tutorial directories - they were already added above
        if (Test-IsUserManualDirectory -Directory $subdir.FullName) {
            continue
        }
        if (Test-IsTutorialDirectory -Directory $subdir.FullName) {
            continue
        }

        $subdirIndexPath = Join-Path $subdir.FullName "index.md"
        $subdirTitle = Get-DirectoryTitle -IndexPath $subdirIndexPath

        # Get all entries for this subdirectory (user manuals + guides)
        $subdirSubdirs = Get-Subdirectories -Directory $subdir.FullName
        $subdirEntries = Get-AllGuidesAtLevel -Directory $subdir.FullName -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $subdirSubdirs

        if ($subdirEntries.Count -eq 0) {
            # No visible child entries - but if the subdirectory's index.md is
            # itself a guide, show it as a standalone entry (e.g. jobs/index.md
            # inside a user manual where all child pages are excluded from parent)
            $subdirGuideInfo = Get-GuideInfo -FilePath $subdirIndexPath
            if ($subdirGuideInfo.IsGuide -and -not $subdirGuideInfo.ExcludeFromParent) {
                $guidesSection += Build-GuideEntry -GuideFile (Get-Item $subdirIndexPath) -FromPath $parentDir -HeaderLevel "####"
                $guidesSection += $CRLF
            }
            continue
        }

        $guidesSection += Build-SectionHeader -Title $subdirTitle -IndexPath $subdirIndexPath -FromPath $parentDir -HeaderLevel "####" -IsUserManual $false

        # Separate subdirectory entries by type
        $subdirTutorials = @($subdirEntries | Where-Object { $_.Type -eq 'Tutorial' })
        $subdirUserManuals = @($subdirEntries | Where-Object { $_.Type -eq 'UserManual' })
        $subdirRegularGuides = @($subdirEntries | Where-Object { $_.Type -eq 'Guide' })

        # Add Tutorials subsection if any exist
        if ($subdirTutorials.Count -gt 0) {
            $guidesSection += "##### Tutorials$CRLF$CRLF"
            foreach ($subdirEntry in $subdirTutorials) {
                $guidesSection += Build-GuideEntry -GuideFile $subdirEntry.File -FromPath $parentDir -HeaderLevel "######"
                $guidesSection += $CRLF
            }
        }

        # Add User Manual entries
        foreach ($subdirEntry in $subdirUserManuals) {
            $guidesSection += Build-GuideEntry -GuideFile (Get-Item $subdirEntry.Path) -FromPath $parentDir -HeaderLevel "#####"
            $guidesSection += $CRLF
        }

        # Add Regular Guide entries
        foreach ($subdirEntry in $subdirRegularGuides) {
            $guidesSection += Build-GuideEntry -GuideFile $subdirEntry.File -FromPath $parentDir -HeaderLevel "#####"
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
            $isTutorial = Test-IsTutorialDirectory -Directory $dir.FullName

            if ($isUserManual -or $isTutorial) {
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
        # Uses Get-AllGuidesAtLevel to ensure tutorials/user manuals appear before regular guides at each level
        # Note: Tutorials and user manuals directly under the topic directory are handled separately before this is called
        function Invoke-DirectoryHierarchyProcessing {
            param([string]$ParentPath, [int]$Depth)

            if (-not $dirsByParent.ContainsKey($ParentPath)) {
                return
            }

            # Get children at this level, separate tutorials and user manuals from regular dirs
            $children = $dirsByParent[$ParentPath]
            $tutorialDirs = [System.Collections.ArrayList]@()
            $userManualDirs = [System.Collections.ArrayList]@()
            $regularDirs = [System.Collections.ArrayList]@()

            foreach ($child in $children) {
                $indexPath = Join-Path $child.FullName "index.md"
                $navOrder = $null
                if (Test-Path $indexPath -PathType Leaf) {
                    $guideInfo = Get-GuideInfo -FilePath $indexPath
                    $navOrder = $guideInfo.NavOrder
                }
                $entry = @{
                    Directory = $child
                    NavOrder  = $navOrder
                }
                if (Test-IsTutorialDirectory -Directory $child.FullName) {
                    # Skip tutorial dirs at Depth 1 - they were already processed at the topic level
                    if ($Depth -gt 1) {
                        [void]$tutorialDirs.Add($entry)
                    }
                } elseif (Test-IsUserManualDirectory -Directory $child.FullName) {
                    # Skip user manuals at Depth 1 - they were already processed at the topic level
                    if ($Depth -gt 1) {
                        [void]$userManualDirs.Add($entry)
                    }
                } else {
                    [void]$regularDirs.Add($entry)
                }
            }

            # Process tutorial directories first (they appear as guide entries, not sections)
            # Sort by nav_order first, then alphabetically
            foreach ($entry in ($tutorialDirs | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } })) {
                $dir = $entry.Directory
                $indexPath = Join-Path $dir.FullName "index.md"
                $indexInfo = Get-GuideInfo -FilePath $indexPath

                if (-not $indexInfo.IsGuide -or $indexInfo.ExcludeFromMain) {
                    continue
                }

                $relativePath = $dir.FullName -replace [regex]::Escape($DocsPath), ''
                $pathParts = @($relativePath -split '\\' | Where-Object { $_ -ne '' })
                $depthInTopic = $pathParts.Count - 1

                # Tutorial directories appear at guide level (one deeper than section header would be)
                $headerLevel = '#' * ($depthInTopic + 3)
                $guideEntry = Build-GuideEntry -GuideFile (Get-Item $indexPath) -FromPath $guidesListPath -HeaderLevel $headerLevel
                $script:content += $guideEntry + $CRLF
            }

            # Process user manual directories (they appear as guide entries, not sections)
            # Sort by nav_order first, then alphabetically
            foreach ($entry in ($userManualDirs | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } })) {
                $dir = $entry.Directory
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
                $guideEntry = Build-GuideEntry -GuideFile (Get-Item $indexPath) -FromPath $guidesListPath -HeaderLevel $headerLevel
                $script:content += $guideEntry + $CRLF
            }

            # Process regular directories (they become section headers with their own content)
            # Sort by nav_order first, then alphabetically
            foreach ($entry in ($regularDirs | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } })) {
                $dir = $entry.Directory
                $indexPath = Join-Path $dir.FullName "index.md"
                $relativePath = $dir.FullName -replace [regex]::Escape($DocsPath), ''
                $pathParts = @($relativePath -split '\\' | Where-Object { $_ -ne '' })
                $depthInTopic = $pathParts.Count - 1

                # Check if this directory has any content (guides or children with content)
                $guides = Get-GuidesInDirectory -Directory $dir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_MAIN_FLAG
                $hasChildren = $dirsByParent.ContainsKey($dir.FullName)

                # Also check for tutorial and user manual children
                $childTutorials = @()
                $childUserManuals = @()
                if ($hasChildren -and $dirsByParent[$dir.FullName]) {
                    $childTutorials = @($dirsByParent[$dir.FullName] | Where-Object {
                            $_ -and $_.FullName -and (Test-IsTutorialDirectory -Directory $_.FullName)
                        })
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

                # First, separate tutorials from other guides
                $tutorialGuides = @()
                $nonTutorialGuides = @()
                foreach ($guide in $guides) {
                    $gi = Get-GuideInfo -FilePath $guide.FullName
                    if ($gi.IsTutorial) {
                        $tutorialGuides += $guide
                    } else {
                        $nonTutorialGuides += $guide
                    }
                }

                # Collect child tutorial directory entries
                $childTutEntries = @($childTutorials | ForEach-Object {
                        $tutIndexPath = Join-Path $_.FullName "index.md"
                        $tutInfo = Get-GuideInfo -FilePath $tutIndexPath
                        @{
                            Directory = $_
                            NavOrder  = $tutInfo.NavOrder
                            Info      = $tutInfo
                        }
                    })

                # Add Tutorials section if any exist (listed first)
                if ($tutorialGuides.Count -gt 0 -or $childTutEntries.Count -gt 0) {
                    $tutorialHeaderLevel = '#' * ($depthInTopic + 4)
                    $script:content += "${tutorialHeaderLevel} Tutorials${CRLF}${CRLF}"
                    $tutorialGuideLevel = '#' * ($depthInTopic + 5)
                    foreach ($guide in $tutorialGuides) {
                        $guideEntry = Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel $tutorialGuideLevel
                        $script:content += $guideEntry + $CRLF
                    }
                    # Add multi-page tutorial directory entries
                    foreach ($tutEntry in ($childTutEntries | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } })) {
                        $tutDir = $tutEntry.Directory
                        $tutInfo = $tutEntry.Info

                        if (-not $tutInfo.IsGuide -or $tutInfo.ExcludeFromMain) {
                            continue
                        }

                        $tutIndexPath = Join-Path $tutDir.FullName "index.md"
                        $guideEntry = Build-GuideEntry -GuideFile (Get-Item $tutIndexPath) -FromPath $guidesListPath -HeaderLevel $tutorialGuideLevel
                        $script:content += $guideEntry + $CRLF
                    }
                }

                # Then add user manual children
                # Get nav_order for child user manuals and sort
                $childUmEntries = @($childUserManuals | ForEach-Object {
                        $umIndexPath = Join-Path $_.FullName "index.md"
                        $umInfo = Get-GuideInfo -FilePath $umIndexPath
                        @{
                            Directory = $_
                            NavOrder  = $umInfo.NavOrder
                            Info      = $umInfo
                        }
                    })
                foreach ($umEntry in ($childUmEntries | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } })) {
                    $umDir = $umEntry.Directory
                    $umInfo = $umEntry.Info

                    if (-not $umInfo.IsGuide -or $umInfo.ExcludeFromMain) {
                        continue
                    }

                    $umIndexPath = Join-Path $umDir.FullName "index.md"
                    $guideHeaderLevel = '#' * ($depthInTopic + 4)
                    $guideEntry = Build-GuideEntry -GuideFile (Get-Item $umIndexPath) -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
                    $script:content += $guideEntry + $CRLF
                }

                # Then add remaining direct guides (non-tutorial, already sorted by Get-GuidesInDirectory)
                foreach ($guide in $nonTutorialGuides) {
                    $guideHeaderLevel = '#' * ($depthInTopic + 4)
                    $guideEntry = Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
                    $script:content += $guideEntry + $CRLF
                }

                # Recursively process non-user-manual/non-tutorial children
                if ($hasChildren -and $dirsByParent[$dir.FullName]) {
                    $nonSpecialChildren = @($dirsByParent[$dir.FullName] | Where-Object {
                            $_ -and $_.FullName -and
                            -not (Test-IsUserManualDirectory -Directory $_.FullName) -and
                            -not (Test-IsTutorialDirectory -Directory $_.FullName)
                        })
                    if ($nonSpecialChildren.Count -gt 0) {
                        Invoke-DirectoryHierarchyProcessing -ParentPath $dir.FullName -Depth ($Depth + 1)
                    }
                }
            }
        }

        # Get all guides directly in the topic directory (includes tutorial/ subdir scan)
        $topicGuides = Get-GuidesInDirectory -Directory $topicDir.FullName -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_MAIN_FLAG

        # Separate tutorials from other guides
        $topicTutorials = @()
        $topicRegularGuides = @()
        foreach ($guide in $topicGuides) {
            $gi = Get-GuideInfo -FilePath $guide.FullName
            if ($gi.IsTutorial) {
                $topicTutorials += $guide
            } else {
                $topicRegularGuides += $guide
            }
        }

        # Also check for tutorial directories directly under the topic
        $topicTutorialDirs = @()
        if ($dirsByParent.ContainsKey($topicDir.FullName)) {
            foreach ($child in $dirsByParent[$topicDir.FullName]) {
                if (Test-IsTutorialDirectory -Directory $child.FullName) {
                    $tutIndexPath = Join-Path $child.FullName "index.md"
                    $tutInfo = Get-GuideInfo -FilePath $tutIndexPath
                    if ($tutInfo.IsGuide -and -not $tutInfo.ExcludeFromMain) {
                        $topicTutorialDirs += Get-Item $tutIndexPath
                    }
                }
            }
        }

        # First, add tutorials section if any exist (single-file + multi-page directories)
        if ($topicTutorials.Count -gt 0 -or $topicTutorialDirs.Count -gt 0) {
            $script:content += "#### Tutorials${CRLF}${CRLF}"
            foreach ($guide in $topicTutorials) {
                $script:content += Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel '#####'
                $script:content += $CRLF
            }
            foreach ($tutDirIndex in $topicTutorialDirs) {
                $script:content += Build-GuideEntry -GuideFile $tutDirIndex -FromPath $guidesListPath -HeaderLevel '#####'
                $script:content += $CRLF
            }
        }

        # Then, check for user manual directories directly under the topic (skip tutorials)
        # Sort by nav_order, then alphabetically
        if ($dirsByParent.ContainsKey($topicDir.FullName)) {
            $topicChildren = $dirsByParent[$topicDir.FullName]
            # Get nav_order for each child and sort
            $childEntries = @($topicChildren | ForEach-Object {
                    $indexPath = Join-Path $_.FullName "index.md"
                    $navOrder = $null
                    if (Test-Path $indexPath -PathType Leaf) {
                        $guideInfo = Get-GuideInfo -FilePath $indexPath
                        $navOrder = $guideInfo.NavOrder
                    }
                    @{
                        Directory = $_
                        NavOrder  = $navOrder
                    }
                })
            foreach ($childEntry in ($childEntries | Sort-Object @{Expression = { if ($null -eq $_.NavOrder) { [int]::MaxValue } else { $_.NavOrder } } }, @{Expression = { $_.Directory.FullName } })) {
                $child = $childEntry.Directory
                if (Test-IsTutorialDirectory -Directory $child.FullName) {
                    continue  # Already handled in tutorials section above
                }
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

        # Then add remaining regular guides directly in the topic directory
        foreach ($guide in $topicRegularGuides) {
            $guideHeaderLevel = '####'  # H4 for top-level guides under the topic
            $script:content += Build-GuideEntry -GuideFile $guide -FromPath $guidesListPath -HeaderLevel $guideHeaderLevel
            $script:content += $CRLF
        }

        # Finally process non-user-manual subdirectories and their children recursively
        Invoke-DirectoryHierarchyProcessing -ParentPath $topicDir.FullName -Depth 1
    }

    return $script:content.TrimEnd()
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
    Write-Error "docs directory not found. Please run this script from the repository root or utilities directory."
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
