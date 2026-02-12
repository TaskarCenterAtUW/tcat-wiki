#!/usr/bin/env pwsh
#Requires -Modules @{ ModuleName='Pester'; ModuleVersion='5.0.0' }

# Name: TCAT Wiki - Guides Lists Generator Tests
# Version: 3.0.0
# Date: 2026-02-05
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Pester tests for generate-guides-lists.ps1

.DESCRIPTION
    Comprehensive test suite for the Zensical guides lists generator script.
    Tests helper functions, guide detection, user manual handling, and output format.

.EXAMPLE
    Invoke-Pester .\generate-guides-lists.Tests.ps1
    Runs all tests in the test file

.EXAMPLE
    Invoke-Pester .\generate-guides-lists.Tests.ps1 -Output Detailed
    Runs all tests with detailed output

.NOTES
    Requires Pester v5+ to be installed: Install-Module -Name Pester -Force -SkipPublisherCheck
#>

BeforeAll {
    # Extract and load the helper functions from generate-guides-lists.ps1
    $scriptPath = Join-Path $PSScriptRoot "generate-guides-lists.ps1"
    $scriptContent = Get-Content $scriptPath -Raw

    # Set up required constants that the functions depend on
    $script:CRLF = "`r`n"
    $script:EXCLUDE_PARENT_FLAG = "exclude-from-parent-guides-list"
    $script:EXCLUDE_MAIN_FLAG = "exclude-from-main-guides-list"

    # Extract the helper functions region and execute it
    if ($scriptContent -match '(?s)#region Helper Functions(.+?)#endregion Helper Functions') {
        $functionBlock = $matches[1]
        # Create and invoke script block to define functions in current scope
        $sb = [ScriptBlock]::Create($functionBlock)
        . $sb
    } else {
        throw "Could not find Helper Functions region in generate-guides-lists.ps1"
    }
}

# ==============================================================================
# GET-GUIDEINFO TESTS
# ==============================================================================

Describe "Get-GuideInfo" {
    Context "When file has Guide tag in frontmatter" {
        It "Should detect file as a guide" {
            $testFile = Join-Path $TestDrive "guide-test.md"
            @"
---
title: Test Guide
tags:
    - Guide
---

# Test Guide

This is a test guide.
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            $result.IsUserManual | Should -Be $false
            $result.Title | Should -Be "Test Guide"
        }
    }

    Context "When file has User Manual tag in frontmatter" {
        It "Should detect file as both guide and user manual" {
            $testFile = Join-Path $TestDrive "user-manual-test.md"
            @"
---
title: Test User Manual
tags:
    - User Manual
    - External
---

# Test User Manual

This is a test user manual.
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            $result.IsUserManual | Should -Be $true
            $result.Title | Should -Be "Test User Manual"
        }
    }

    Context "When file has no Guide or User Manual tag" {
        It "Should not detect file as a guide" {
            $testFile = Join-Path $TestDrive "not-guide-test.md"
            @"
---
title: Regular Page
---

# Regular Page

This is not a guide.
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $false
            $result.IsUserManual | Should -Be $false
        }
    }

    Context "When file has exclude-from-parent-guides-list flag" {
        It "Should set ExcludeFromParent to true" {
            $testFile = Join-Path $TestDrive "exclude-parent-test.md"
            @"
---
title: Excluded Guide
tags:
    - Guide
# exclude-from-parent-guides-list
---

# Excluded Guide
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            $result.ExcludeFromParent | Should -Be $true
            $result.ExcludeFromMain | Should -Be $false
        }
    }

    Context "When file has exclude-from-main-guides-list flag" {
        It "Should set ExcludeFromMain to true" {
            $testFile = Join-Path $TestDrive "exclude-main-test.md"
            @"
---
title: Main Excluded Guide
tags:
    - Guide
# exclude-from-main-guides-list
---

# Main Excluded Guide
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            $result.ExcludeFromParent | Should -Be $false
            $result.ExcludeFromMain | Should -Be $true
        }
    }

    Context "When file has nav_order in frontmatter" {
        It "Should extract nav_order value" {
            $testFile = Join-Path $TestDrive "nav-order-test.md"
            @"
---
title: Ordered Guide
tags:
    - Guide
nav_order: 3
---

# Ordered Guide
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.NavOrder | Should -Be 3
        }
    }

    Context "When file has no nav_order" {
        It "Should return null for NavOrder" {
            $testFile = Join-Path $TestDrive "no-nav-order-test.md"
            @"
---
title: Unordered Guide
tags:
    - Guide
---

# Unordered Guide
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.NavOrder | Should -BeNullOrEmpty
        }
    }

    Context "When file has both exclude flags" {
        It "Should set both exclusion flags to true" {
            $testFile = Join-Path $TestDrive "exclude-both-test.md"
            @"
---
title: Fully Excluded Guide
tags:
    - Guide
# exclude-from-parent-guides-list
# exclude-from-main-guides-list
---

# Fully Excluded Guide
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.ExcludeFromParent | Should -Be $true
            $result.ExcludeFromMain | Should -Be $true
        }
    }

    Context "When exclude flags are incorrectly formatted as tags (array items)" {
        It "Should NOT detect exclusion when flags are array items instead of YAML comments" {
            $testFile = Join-Path $TestDrive "wrong-format-test.md"
            @"
---
title: Incorrectly Formatted Exclusions
tags:
    - Guide
    - exclude-from-parent-guides-list
    - exclude-from-main-guides-list
---

# Incorrectly Formatted Exclusions

This guide has exclusion flags as array items, which is incorrect.
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            # These should be FALSE because the format is wrong (array items instead of YAML comments)
            $result.ExcludeFromParent | Should -Be $false -Because "exclude flags must be YAML comments (# flag), not array items (- flag)"
            $result.ExcludeFromMain | Should -Be $false -Because "exclude flags must be YAML comments (# flag), not array items (- flag)"
        }
    }

    Context "When file does not exist" {
        It "Should return default values without throwing" {
            $result = Get-GuideInfo -FilePath "C:\nonexistent\file.md" -WarningAction SilentlyContinue
            $result.IsGuide | Should -Be $false
            $result.Title | Should -BeNullOrEmpty
        }
    }

    Context "When extracting description" {
        It "Should extract description between heading and Guides List reference" {
            $testFile = Join-Path $TestDrive "description-test.md"
            @"
---
title: Guide With Description
tags:
    - Guide
---

## Guide With Description

This is the description text that should be extracted.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../guides-list/index.md)._
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.Description | Should -Be "This is the description text that should be extracted."
        }
    }
}

# ==============================================================================
# GET-DIRECTORYTITLE TESTS
# ==============================================================================

Describe "Get-DirectoryTitle" {
    Context "When index.md has title in frontmatter" {
        It "Should extract the title" {
            $testDir = Join-Path $TestDrive "title-dir"
            New-Item -Path $testDir -ItemType Directory -Force | Out-Null
            $indexPath = Join-Path $testDir "index.md"
            @"
---
title: Directory Title
---

# Heading
"@ | Set-Content -Path $indexPath -Encoding UTF8

            $result = Get-DirectoryTitle -IndexPath $indexPath
            $result | Should -Be "Directory Title"
        }
    }

    Context "When index.md has no frontmatter" {
        It "Should return empty string" {
            $testDir = Join-Path $TestDrive "no-title-dir"
            New-Item -Path $testDir -ItemType Directory -Force | Out-Null
            $indexPath = Join-Path $testDir "index.md"
            @"
# Just a Heading

Content without frontmatter.
"@ | Set-Content -Path $indexPath -Encoding UTF8

            $result = Get-DirectoryTitle -IndexPath $indexPath
            $result | Should -BeNullOrEmpty
        }
    }

    Context "When file does not exist" {
        It "Should return empty string and not throw" {
            $result = Get-DirectoryTitle -IndexPath "C:\nonexistent\index.md" -WarningAction SilentlyContinue
            $result | Should -BeNullOrEmpty
        }
    }
}

# ==============================================================================
# TEST-ISUSERMANUALDIRECTORY TESTS
# ==============================================================================

Describe "Test-IsUserManualDirectory" {
    Context "When directory contains user manual index.md" {
        It "Should return true" {
            $testDir = Join-Path $TestDrive "user-manual-dir"
            New-Item -Path $testDir -ItemType Directory -Force | Out-Null
            $indexPath = Join-Path $testDir "index.md"
            @"
---
title: Test User Manual
tags:
    - User Manual
---
"@ | Set-Content -Path $indexPath -Encoding UTF8

            $result = Test-IsUserManualDirectory -Directory $testDir
            $result | Should -Be $true
        }
    }

    Context "When directory contains regular index.md" {
        It "Should return false" {
            $testDir = Join-Path $TestDrive "regular-dir"
            New-Item -Path $testDir -ItemType Directory -Force | Out-Null
            $indexPath = Join-Path $testDir "index.md"
            @"
---
title: Regular Section
---
"@ | Set-Content -Path $indexPath -Encoding UTF8

            $result = Test-IsUserManualDirectory -Directory $testDir
            $result | Should -Be $false
        }
    }

    Context "When directory has no index.md" {
        It "Should return false" {
            $testDir = Join-Path $TestDrive "no-index-dir"
            New-Item -Path $testDir -ItemType Directory -Force | Out-Null

            $result = Test-IsUserManualDirectory -Directory $testDir
            $result | Should -Be $false
        }
    }
}

# ==============================================================================
# GET-RELATIVEMARKDOWNPATH TESTS
# ==============================================================================

Describe "Get-RelativeMarkdownPath" {
    It "Should return relative path with forward slashes" {
        $fromPath = "C:\docs\section"
        $toPath = "C:\docs\section\page.md"

        $result = Get-RelativeMarkdownPath -FromPath $fromPath -ToPath $toPath
        $result | Should -Be "page.md"
    }

    It "Should handle parent directory navigation" {
        $fromPath = "C:\docs\section\subsection"
        $toPath = "C:\docs\other\page.md"

        $result = Get-RelativeMarkdownPath -FromPath $fromPath -ToPath $toPath
        $result | Should -Be "../../other/page.md"
    }

    It "Should convert backslashes to forward slashes" {
        $fromPath = "C:\docs"
        $toPath = "C:\docs\section\subsection\page.md"

        $result = Get-RelativeMarkdownPath -FromPath $fromPath -ToPath $toPath
        $result | Should -Not -Match '\\'
        $result | Should -Match '/'
    }
}

# ==============================================================================
# GET-GUIDESINDIRECTORY TESTS
# ==============================================================================

Describe "Get-GuidesInDirectory" {
    BeforeAll {
        $script:guidesTestDir = Join-Path $TestDrive "guides-test-dir"
        New-Item -Path $guidesTestDir -ItemType Directory -Force | Out-Null

        # Create index.md (not a guide)
        @"
---
title: Section Index
---
"@ | Set-Content -Path (Join-Path $guidesTestDir "index.md") -Encoding UTF8

        # Create a regular guide
        @"
---
title: Alpha Guide
tags:
    - Guide
---
"@ | Set-Content -Path (Join-Path $guidesTestDir "alpha-guide.md") -Encoding UTF8

        # Create another regular guide
        @"
---
title: Beta Guide
tags:
    - Guide
---
"@ | Set-Content -Path (Join-Path $guidesTestDir "beta-guide.md") -Encoding UTF8

        # Create a non-guide file
        @"
---
title: Regular Page
---
"@ | Set-Content -Path (Join-Path $guidesTestDir "not-a-guide.md") -Encoding UTF8
    }

    Context "When excluding own index" {
        It "Should not include index.md in results" {
            $result = Get-GuidesInDirectory -Directory $guidesTestDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            $result | Where-Object { $_.Name -eq "index.md" } | Should -BeNullOrEmpty
        }

        It "Should include guide files" {
            $result = Get-GuidesInDirectory -Directory $guidesTestDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            $result.Count | Should -Be 2
        }

        It "Should not include non-guide files" {
            $result = Get-GuidesInDirectory -Directory $guidesTestDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            $result | Where-Object { $_.Name -eq "not-a-guide.md" } | Should -BeNullOrEmpty
        }

        It "Should return guides sorted alphabetically" {
            $result = Get-GuidesInDirectory -Directory $guidesTestDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            $result[0].Name | Should -Be "alpha-guide.md"
            $result[1].Name | Should -Be "beta-guide.md"
        }
    }

    Context "When directory has user manual guides" {
        BeforeAll {
            $script:umGuidesDir = Join-Path $TestDrive "um-guides-dir"
            New-Item -Path $umGuidesDir -ItemType Directory -Force | Out-Null

            # Create index.md with User Manual tag
            @"
---
title: Test User Manual
tags:
    - User Manual
---
"@ | Set-Content -Path (Join-Path $umGuidesDir "index.md") -Encoding UTF8

            # Create a regular guide in the user manual directory
            @"
---
title: UM Sub Guide
tags:
    - Guide
---
"@ | Set-Content -Path (Join-Path $umGuidesDir "um-sub-guide.md") -Encoding UTF8
        }

        It "Should return user manuals before regular guides" {
            # This test verifies the sorting behavior with a user manual index
            $result = Get-GuidesInDirectory -Directory $umGuidesDir -ExcludeOwnIndex $false -ExcludeFlag $EXCLUDE_PARENT_FLAG
            # When not excluding own index, the User Manual index should come first
            $result[0].Name | Should -Be "index.md"
        }
    }

    Context "When guides have nav_order in frontmatter" {
        BeforeAll {
            $script:navOrderGuidesDir = Join-Path $TestDrive "nav-order-guides-dir"
            New-Item -Path $navOrderGuidesDir -ItemType Directory -Force | Out-Null

            # Create index.md (not a guide)
            @"
---
title: Section Index
---
"@ | Set-Content -Path (Join-Path $navOrderGuidesDir "index.md") -Encoding UTF8

            # Create guide without nav_order (should come last)
            @"
---
title: Zebra Guide
tags:
    - Guide
---
"@ | Set-Content -Path (Join-Path $navOrderGuidesDir "zebra-guide.md") -Encoding UTF8

            # Create guide with nav_order 2
            @"
---
title: Second Guide
tags:
    - Guide
nav_order: 2
---
"@ | Set-Content -Path (Join-Path $navOrderGuidesDir "beta-guide.md") -Encoding UTF8

            # Create guide with nav_order 1
            @"
---
title: First Guide
tags:
    - Guide
nav_order: 1
---
"@ | Set-Content -Path (Join-Path $navOrderGuidesDir "alpha-guide.md") -Encoding UTF8
        }

        It "Should sort guides by nav_order, with ordered guides before unordered" {
            $result = Get-GuidesInDirectory -Directory $navOrderGuidesDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            $result.Count | Should -Be 3
            $result[0].Name | Should -Be "alpha-guide.md" -Because "nav_order 1 should come first"
            $result[1].Name | Should -Be "beta-guide.md" -Because "nav_order 2 should come second"
            $result[2].Name | Should -Be "zebra-guide.md" -Because "guides without nav_order should come last"
        }
    }
}

# ==============================================================================
# GET-SUBDIRECTORIES TESTS
# ==============================================================================

Describe "Get-Subdirectories" {
    BeforeAll {
        $script:subdirTestRoot = Join-Path $TestDrive "subdir-test-root"
        New-Item -Path $subdirTestRoot -ItemType Directory -Force | Out-Null

        # Create regular subdirectory with index.md
        $regularDir = Join-Path $subdirTestRoot "regular-section"
        New-Item -Path $regularDir -ItemType Directory -Force | Out-Null
        @"
---
title: Regular Section
---
"@ | Set-Content -Path (Join-Path $regularDir "index.md") -Encoding UTF8

        # Create user manual subdirectory
        $umDir = Join-Path $subdirTestRoot "user-manual"
        New-Item -Path $umDir -ItemType Directory -Force | Out-Null
        @"
---
title: User Manual
tags:
    - User Manual
---
"@ | Set-Content -Path (Join-Path $umDir "index.md") -Encoding UTF8

        # Create resources directory (should be excluded)
        $resourcesDir = Join-Path $subdirTestRoot "resources"
        New-Item -Path $resourcesDir -ItemType Directory -Force | Out-Null
        @"
---
title: Resources
---
"@ | Set-Content -Path (Join-Path $resourcesDir "index.md") -Encoding UTF8

        # Create subdirectory without index.md (should be excluded)
        $noIndexDir = Join-Path $subdirTestRoot "no-index"
        New-Item -Path $noIndexDir -ItemType Directory -Force | Out-Null
    }

    It "Should exclude resources directory" {
        $result = Get-Subdirectories -Directory $subdirTestRoot
        $result | Where-Object { $_.Name -eq "resources" } | Should -BeNullOrEmpty
    }

    It "Should exclude directories without index.md" {
        $result = Get-Subdirectories -Directory $subdirTestRoot
        $result | Where-Object { $_.Name -eq "no-index" } | Should -BeNullOrEmpty
    }

    It "Should include directories with index.md" {
        $result = Get-Subdirectories -Directory $subdirTestRoot
        $result.Count | Should -Be 2
    }

    It "Should return user manual directories before regular directories" {
        $result = Get-Subdirectories -Directory $subdirTestRoot
        $result[0].Name | Should -Be "user-manual"
        $result[1].Name | Should -Be "regular-section"
    }
}

Describe "Get-Subdirectories nav_order sorting" {
    BeforeAll {
        $script:navOrderSubdirRoot = Join-Path $TestDrive "nav-order-subdir-root"
        New-Item -Path $navOrderSubdirRoot -ItemType Directory -Force | Out-Null

        # Create subdirectory without nav_order (should come last)
        $zdirPath = Join-Path $navOrderSubdirRoot "zdir"
        New-Item -Path $zdirPath -ItemType Directory -Force | Out-Null
        @"
---
title: Zdir Section
---
"@ | Set-Content -Path (Join-Path $zdirPath "index.md") -Encoding UTF8

        # Create subdirectory with nav_order 2
        $bdirPath = Join-Path $navOrderSubdirRoot "bdir"
        New-Item -Path $bdirPath -ItemType Directory -Force | Out-Null
        @"
---
title: Bdir Section
nav_order: 2
---
"@ | Set-Content -Path (Join-Path $bdirPath "index.md") -Encoding UTF8

        # Create subdirectory with nav_order 1
        $adirPath = Join-Path $navOrderSubdirRoot "adir"
        New-Item -Path $adirPath -ItemType Directory -Force | Out-Null
        @"
---
title: Adir Section
nav_order: 1
---
"@ | Set-Content -Path (Join-Path $adirPath "index.md") -Encoding UTF8
    }

    It "Should sort subdirectories by nav_order, with ordered directories before unordered" {
        $result = Get-Subdirectories -Directory $navOrderSubdirRoot
        $result.Count | Should -Be 3
        $result[0].Name | Should -Be "adir" -Because "nav_order 1 should come first"
        $result[1].Name | Should -Be "bdir" -Because "nav_order 2 should come second"
        $result[2].Name | Should -Be "zdir" -Because "directories without nav_order should come last"
    }
}

# ==============================================================================
# BUILD-GUIDEENTRY TESTS
# ==============================================================================

Describe "Build-GuideEntry" {
    BeforeAll {
        $script:entryTestDir = Join-Path $TestDrive "entry-test-dir"
        New-Item -Path $entryTestDir -ItemType Directory -Force | Out-Null

        @"
---
title: Test Entry Guide
tags:
    - Guide
---

## Test Entry Guide

This is the description.

_For a list of all guides
"@ | Set-Content -Path (Join-Path $entryTestDir "test-guide.md") -Encoding UTF8
    }

    It "Should generate header with link" {
        $guideFile = Get-Item (Join-Path $entryTestDir "test-guide.md")
        $result = Build-GuideEntry -GuideFile $guideFile -FromPath $entryTestDir -HeaderLevel "####"
        $result | Should -Match '#### \[Test Entry Guide\]\(test-guide\.md\)'
    }

    It "Should include description if available" {
        $guideFile = Get-Item (Join-Path $entryTestDir "test-guide.md")
        $result = Build-GuideEntry -GuideFile $guideFile -FromPath $entryTestDir -HeaderLevel "####"
        $result | Should -Match 'This is the description\.'
    }

    It "Should use the specified header level" {
        $guideFile = Get-Item (Join-Path $entryTestDir "test-guide.md")
        $resultH4 = Build-GuideEntry -GuideFile $guideFile -FromPath $entryTestDir -HeaderLevel "####"
        $resultH5 = Build-GuideEntry -GuideFile $guideFile -FromPath $entryTestDir -HeaderLevel "#####"

        $resultH4 | Should -Match '^#### '
        $resultH5 | Should -Match '^##### '
    }
}

# ==============================================================================
# BUILD-SECTIONHEADER TESTS
# ==============================================================================

Describe "Build-SectionHeader" {
    BeforeAll {
        $script:sectionTestDir = Join-Path $TestDrive "section-test-dir"
        New-Item -Path $sectionTestDir -ItemType Directory -Force | Out-Null

        @"
---
title: Test Section
---
"@ | Set-Content -Path (Join-Path $sectionTestDir "index.md") -Encoding UTF8
    }

    It "Should generate header with link and Guides suffix for non-user-manual" {
        $indexPath = Join-Path $sectionTestDir "index.md"
        $result = Build-SectionHeader -Title "Test Section" -IndexPath $indexPath -FromPath $TestDrive -HeaderLevel "####" -IsUserManual $false
        $result | Should -Match '#### \[Test Section\]\(.+\) Guides'
    }

    It "Should not include Guides suffix for user manual" {
        $indexPath = Join-Path $sectionTestDir "index.md"
        $result = Build-SectionHeader -Title "Test Section" -IndexPath $indexPath -FromPath $TestDrive -HeaderLevel "####" -IsUserManual $true
        $result | Should -Match '#### \[Test Section\]\(.+\)\s*$'
        $result | Should -Not -Match 'Guides'
    }

    It "Should use the specified header level" {
        $indexPath = Join-Path $sectionTestDir "index.md"
        $result = Build-SectionHeader -Title "Test Section" -IndexPath $indexPath -FromPath $TestDrive -HeaderLevel "###" -IsUserManual $false
        $result | Should -Match '^### '
    }
}

# ==============================================================================
# GET-TCATWIKISECTION TESTS
# ==============================================================================

Describe "Get-TcatWikiSection" {
    It "Should return TCAT Wiki section header" {
        $result = Get-TcatWikiSection
        $result | Should -Match '### TCAT Wiki Guides'
    }

    It "Should include Contributing link" {
        $result = Get-TcatWikiSection
        $result | Should -Match '\[Contributing\]\(https://github\.com/TaskarCenterAtUW/tcat-wiki/blob/main/CONTRIBUTING\.md\)'
    }

    It "Should include description for Contributing" {
        $result = Get-TcatWikiSection
        $result | Should -Match 'how to contribute to the TCAT Wiki'
    }
}

# ==============================================================================
# GET-ALLGUIDESATLEVEL TESTS
# ==============================================================================

Describe "Get-AllGuidesAtLevel" {
    BeforeAll {
        $script:allGuidesTestDir = Join-Path $TestDrive "all-guides-test"
        New-Item -Path $allGuidesTestDir -ItemType Directory -Force | Out-Null

        # Create index.md
        @"
---
title: All Guides Section
---
"@ | Set-Content -Path (Join-Path $allGuidesTestDir "index.md") -Encoding UTF8

        # Create regular guide
        @"
---
title: Regular Guide
tags:
    - Guide
---
"@ | Set-Content -Path (Join-Path $allGuidesTestDir "regular-guide.md") -Encoding UTF8

        # Create user manual subdirectory
        $umSubdir = Join-Path $allGuidesTestDir "user-manual"
        New-Item -Path $umSubdir -ItemType Directory -Force | Out-Null
        @"
---
title: Sub User Manual
tags:
    - User Manual
---
"@ | Set-Content -Path (Join-Path $umSubdir "index.md") -Encoding UTF8

        # Get subdirectories for testing
        $script:testSubdirs = @(Get-Item $umSubdir)
    }

    It "Should return user manuals before regular guides" {
        $result = Get-AllGuidesAtLevel -Directory $allGuidesTestDir -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $testSubdirs
        $result[0].Type | Should -Be 'UserManual'
        $result[1].Type | Should -Be 'Guide'
    }

    It "Should include Path property for all entries" {
        $result = Get-AllGuidesAtLevel -Directory $allGuidesTestDir -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $testSubdirs
        $result | ForEach-Object {
            $_.Path | Should -Not -BeNullOrEmpty
        }
    }

    It "Should include Info property for all entries" {
        $result = Get-AllGuidesAtLevel -Directory $allGuidesTestDir -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $testSubdirs
        $result | ForEach-Object {
            $_.Info | Should -Not -BeNullOrEmpty
        }
    }
}

# ==============================================================================
# INTEGRATION TESTS
# ==============================================================================

Describe "Integration Tests" -Tag "Integration" {
    BeforeAll {
        # Create a complete test documentation structure
        $script:integrationRoot = Join-Path $TestDrive "integration-docs"
        New-Item -Path $integrationRoot -ItemType Directory -Force | Out-Null

        # Create guides-list directory
        $guidesListDir = Join-Path $integrationRoot "guides-list"
        New-Item -Path $guidesListDir -ItemType Directory -Force | Out-Null
        @"
---
title: Guides List
---
"@ | Set-Content -Path (Join-Path $guidesListDir "index.md") -Encoding UTF8

        # Create a topic directory with user manual and guides
        $topicDir = Join-Path $integrationRoot "test-topic"
        New-Item -Path $topicDir -ItemType Directory -Force | Out-Null
        @"
---
title: Test Topic
---

# Test Topic

This is a test topic.
"@ | Set-Content -Path (Join-Path $topicDir "index.md") -Encoding UTF8

        # Create a guide in the topic
        @"
---
title: Topic Guide
tags:
    - Guide
---

# Topic Guide

This guide is about the topic.
"@ | Set-Content -Path (Join-Path $topicDir "topic-guide.md") -Encoding UTF8

        # Create user manual subdirectory
        $umDir = Join-Path $topicDir "user-manual"
        New-Item -Path $umDir -ItemType Directory -Force | Out-Null
        @"
---
title: Topic User Manual
tags:
    - User Manual
---

# Topic User Manual

This is the user manual.
"@ | Set-Content -Path (Join-Path $umDir "index.md") -Encoding UTF8

        # Create a guide in the user manual
        @"
---
title: Manual Chapter
tags:
    - Guide
---

# Manual Chapter

This is a chapter.
"@ | Set-Content -Path (Join-Path $umDir "chapter.md") -Encoding UTF8
    }

    Context "Directory structure parsing" {
        It "Should correctly identify all directories with index.md" {
            $allDirs = Get-ChildItem -Path $integrationRoot -Recurse -Directory |
                Where-Object { Test-Path (Join-Path $_.FullName "index.md") }
            $allDirs.Count | Should -Be 3  # guides-list, test-topic, user-manual
        }

        It "Should identify user manual directory correctly" {
            $topicDir = Join-Path $integrationRoot "test-topic"
            $umDir = Join-Path $topicDir "user-manual"
            Test-IsUserManualDirectory -Directory $umDir | Should -Be $true
            Test-IsUserManualDirectory -Directory $topicDir | Should -Be $false
        }
    }

    Context "Guides ordering" {
        It "Should place user manuals before regular guides in Get-AllGuidesAtLevel" {
            $topicDir = Join-Path $integrationRoot "test-topic"
            $subdirs = Get-Subdirectories -Directory $topicDir
            $entries = Get-AllGuidesAtLevel -Directory $topicDir -ExcludeFlag $EXCLUDE_PARENT_FLAG -Subdirectories $subdirs

            # First entry should be user manual (from subdirectory)
            $entries[0].Type | Should -Be 'UserManual'
            # Second entry should be regular guide
            $entries[1].Type | Should -Be 'Guide'
        }
    }
}

# ==============================================================================
# EDGE CASE TESTS
# ==============================================================================

Describe "Edge Cases" {
    Context "Empty directories" {
        It "Should handle directory with no guides gracefully" {
            $emptyDir = Join-Path $TestDrive "empty-dir"
            New-Item -Path $emptyDir -ItemType Directory -Force | Out-Null
            @"
---
title: Empty Section
---
"@ | Set-Content -Path (Join-Path $emptyDir "index.md") -Encoding UTF8

            $result = Get-GuidesInDirectory -Directory $emptyDir -ExcludeOwnIndex $true -ExcludeFlag $EXCLUDE_PARENT_FLAG
            $result | Should -BeNullOrEmpty
        }
    }

    Context "Special characters in titles" {
        It "Should handle titles with colons" {
            $testFile = Join-Path $TestDrive "colon-title.md"
            @"
---
title: "Guide: With Colon"
tags:
    - Guide
---
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.Title | Should -Be '"Guide: With Colon"'
        }

        It "Should handle titles with quotes" {
            $testFile = Join-Path $TestDrive "quote-title.md"
            @"
---
title: Guide "With" Quotes
tags:
    - Guide
---
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.Title | Should -Match 'Quotes'
        }
    }

    Context "Multiple tags" {
        It "Should handle files with multiple tags including Guide" {
            $testFile = Join-Path $TestDrive "multi-tag.md"
            @"
---
title: Multi Tag Guide
tags:
    - Guide
    - External
    - User
    - OSW 0.4
---
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
        }
    }

    Context "CRLF vs LF line endings" {
        It "Should handle LF line endings" {
            $testFile = Join-Path $TestDrive "lf-endings.md"
            "---`ntitle: LF Guide`ntags:`n    - Guide`n---`n`n# LF Guide" | Set-Content -Path $testFile -NoNewline -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            $result.Title | Should -Be "LF Guide"
        }

        It "Should handle CRLF line endings" {
            $testFile = Join-Path $TestDrive "crlf-endings.md"
            "---`r`ntitle: CRLF Guide`r`ntags:`r`n    - Guide`r`n---`r`n`r`n# CRLF Guide" | Set-Content -Path $testFile -NoNewline -Encoding UTF8

            $result = Get-GuideInfo -FilePath $testFile
            $result.IsGuide | Should -Be $true
            $result.Title | Should -Be "CRLF Guide"
        }
    }
}
