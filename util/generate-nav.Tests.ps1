#!/usr/bin/env pwsh
#Requires -Modules @{ ModuleName='Pester'; ModuleVersion='5.0.0' }

# Name: TCAT Wiki - Navigation Generator Tests
# Version: 2.0.0
# Date: 2026-02-05
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Pester tests for generate-nav.ps1

.DESCRIPTION
    Comprehensive test suite for the Zensical navigation generator script.
    Tests helper functions, TOML output format, and edge cases.

.EXAMPLE
    Invoke-Pester .\generate-nav.Tests.ps1
    Runs all tests in the test file

.EXAMPLE
    Invoke-Pester .\generate-nav.Tests.ps1 -Output Detailed
    Runs all tests with detailed output

.NOTES
    Requires Pester v5+ to be installed: Install-Module -Name Pester -Force -SkipPublisherCheck
#>

BeforeAll {
    # Extract and load the helper functions from generate-nav.ps1
    $scriptPath = Join-Path $PSScriptRoot "generate-nav.ps1"
    $scriptContent = Get-Content $scriptPath -Raw

    # Extract just the helper functions region and execute it
    if ($scriptContent -match '(?s)#region Helper Functions(.+?)#endregion Helper Functions') {
        $functionBlock = $matches[1]
        # Create and invoke script block to define functions in current scope
        $sb = [ScriptBlock]::Create($functionBlock)
        . $sb
    } else {
        throw "Could not find Helper Functions region in generate-nav.ps1"
    }
}

Describe "Get-MarkdownTitle" {
    Context "When file has YAML frontmatter with title" {
        It "Should extract title from frontmatter" {
            $testFile = Join-Path $TestDrive "test-frontmatter.md"
            @"
---
title: My Custom Title
tags:
    - Guide
---

# Heading Title
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-MarkdownTitle -filePath $testFile
            $result | Should -Be "My Custom Title"
        }
    }

    Context "When file has quoted title in frontmatter" {
        It "Should extract and unquote the title" {
            $testFile = Join-Path $TestDrive "test-quoted.md"
            @"
---
title: "Quoted: Title"
---

# Heading
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-MarkdownTitle -filePath $testFile
            $result | Should -Be "Quoted: Title"
        }
    }

    Context "When file has no frontmatter but has heading" {
        It "Should fall back to first H1 heading" {
            $testFile = Join-Path $TestDrive "test-heading.md"
            @"
# Heading Only Title

Content here.
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-MarkdownTitle -filePath $testFile
            $result | Should -Be "Heading Only Title"
        }
    }

    Context "When file has neither frontmatter nor heading" {
        It "Should return null" {
            $testFile = Join-Path $TestDrive "test-empty.md"
            "Just some content without any title." | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-MarkdownTitle -filePath $testFile
            $result | Should -BeNullOrEmpty
        }
    }

    Context "When file does not exist" {
        It "Should return null and not throw" {
            $result = Get-MarkdownTitle -filePath "C:\nonexistent\file.md"
            $result | Should -BeNullOrEmpty
        }
    }
}

Describe "Get-NavOrder" {
    Context "When file has nav_order in frontmatter" {
        It "Should extract nav_order value" {
            $testFile = Join-Path $TestDrive "test-nav-order.md"
            @"
---
title: Ordered Page
nav_order: 5
---

# Content
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-NavOrder -filePath $testFile
            $result | Should -Be 5
        }
    }

    Context "When file has no nav_order" {
        It "Should return null" {
            $testFile = Join-Path $TestDrive "test-no-nav-order.md"
            @"
---
title: Unordered Page
---

# Content
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-NavOrder -filePath $testFile
            $result | Should -BeNullOrEmpty
        }
    }

    Context "When file has nav_order as first item" {
        It "Should extract nav_order value" {
            $testFile = Join-Path $TestDrive "test-nav-first.md"
            @"
---
nav_order: 1
title: First Page
---
"@ | Set-Content -Path $testFile -Encoding UTF8

            $result = Get-NavOrder -filePath $testFile
            $result | Should -Be 1
        }
    }

    Context "When file does not exist" {
        It "Should return null and not throw" {
            $result = Get-NavOrder -filePath "C:\nonexistent\file.md"
            $result | Should -BeNullOrEmpty
        }
    }
}

Describe "Protect-TomlString" {
    It "Should wrap string in quotes" {
        $result = Protect-TomlString -text "Hello World"
        $result | Should -Be '"Hello World"'
    }

    It "Should escape internal quotes" {
        $result = Protect-TomlString -text 'Say "Hello"'
        $result | Should -Be '"Say \"Hello\""'
    }

    It "Should escape backslashes" {
        $result = Protect-TomlString -text 'Path\To\File'
        # In TOML, backslashes are escaped as \\ (one backslash becomes two)
        $result | Should -Be '"Path\\To\\File"'
    }

    It "Should escape both quotes and backslashes correctly" {
        $result = Protect-TomlString -text 'C:\Path "quoted"'
        $result | Should -Be '"C:\\Path \"quoted\""'
    }
}

Describe "ConvertTo-Title" {
    Context "Known acronyms and project names" {
        It "Should return 'OSW' for 'osw'" {
            ConvertTo-Title -Name "osw" | Should -Be "OSW"
        }

        It "Should return 'TDEI' for 'tdei'" {
            ConvertTo-Title -Name "tdei" | Should -Be "TDEI"
        }

        It "Should return 'JOSM' for 'josm'" {
            ConvertTo-Title -Name "josm" | Should -Be "JOSM"
        }

        It "Should return 'OpenSidewalks' for 'opensidewalks'" {
            ConvertTo-Title -Name "opensidewalks" | Should -Be "OpenSidewalks"
        }

        It "Should return 'AccessMap' for 'accessmap'" {
            ConvertTo-Title -Name "accessmap" | Should -Be "AccessMap"
        }

        It "Should return 'AVIV ScoutRoute' for 'aviv-scoutroute'" {
            ConvertTo-Title -Name "aviv-scoutroute" | Should -Be "AVIV ScoutRoute"
        }
    }

    Context "Index files" {
        It "Should return null for 'index'" {
            ConvertTo-Title -Name "index" | Should -BeNullOrEmpty
        }

        It "Should return null for 'index.md'" {
            ConvertTo-Title -Name "index.md" | Should -BeNullOrEmpty
        }
    }

    Context "Kebab-case and snake_case names" {
        It "Should convert 'user-manual' to 'User Manual'" {
            ConvertTo-Title -Name "user-manual" | Should -Be "User Manual"
        }

        It "Should convert 'my-great-guide' to 'My Great Guide'" {
            ConvertTo-Title -Name "my-great-guide" | Should -Be "My Great Guide"
        }

        It "Should convert 'user_guide' to 'User Guide'" {
            ConvertTo-Title -Name "user_guide" | Should -Be "User Guide"
        }

        It "Should strip .md extension before converting" {
            ConvertTo-Title -Name "my-guide.md" | Should -Be "My Guide"
        }
    }
}

Describe "Build-NavigationToml" {
    BeforeAll {
        # Create test directory structure
        $script:TestDocsPath = Join-Path $TestDrive "nav-test-docs"
        New-Item -Path $TestDocsPath -ItemType Directory -Force | Out-Null

        # Create root index.md
        @"
---
title: Home
---

# Welcome
"@ | Set-Content -Path (Join-Path $TestDocsPath "index.md") -Encoding UTF8

        # Create a section with index and pages
        $sectionPath = Join-Path $TestDocsPath "my-section"
        New-Item -Path $sectionPath -ItemType Directory -Force | Out-Null

        @"
---
title: My Section
---
"@ | Set-Content -Path (Join-Path $sectionPath "index.md") -Encoding UTF8

        @"
---
title: First Page
---
"@ | Set-Content -Path (Join-Path $sectionPath "first-page.md") -Encoding UTF8

        # Create a root-level markdown file
        @"
---
title: Contributing
---
"@ | Set-Content -Path (Join-Path $TestDocsPath "CONTRIBUTING.md") -Encoding UTF8

        $script:NavResult = Build-NavigationToml -docsBasePath $TestDocsPath
    }

    It "Should start with 'nav = ['" {
        $NavResult | Should -Match '^nav = \['
    }

    It "Should end with ']'" {
        $NavResult | Should -Match '\]$'
    }

    It "Should include Home entry" {
        $NavResult | Should -Match '\{"Home" = "index\.md"\}'
    }

    It "Should include section with nested structure" {
        $NavResult | Should -Match '\{"My Section" = \['
    }

    It "Should include section index.md" {
        $NavResult | Should -Match '"my-section/index\.md"'
    }

    It "Should include section pages" {
        $NavResult | Should -Match '\{"First Page" = "my-section/first-page\.md"\}'
    }

    It "Should include root-level markdown files" {
        $NavResult | Should -Match '\{"Contributing" = "CONTRIBUTING\.md"\}'
    }
}

Describe "Update-ZensicalNav" {
    Context "When updating existing nav section" {
        BeforeAll {
            $script:TestTomlPath = Join-Path $TestDrive "test-update.toml"
            @"
[project]
site_name = "Test Site"

nav = [
  {"Old" = "old.md"},
]

[project.theme]
language = "en"
"@ | Set-Content -Path $TestTomlPath -Encoding UTF8

            $script:NewNav = @"
nav = [
  {"New" = "new.md"},
]
"@
        }

        It "Should return true when changes are made" {
            $result = Update-ZensicalNav -zensicalFilePath $TestTomlPath -newNavContent $NewNav
            $result | Should -Be $true
        }

        It "Should update the nav section content" {
            $content = Get-Content $TestTomlPath -Raw
            $content | Should -Match '\{"New" = "new\.md"\}'
            $content | Should -Not -Match '\{"Old" = "old\.md"\}'
        }

        It "Should preserve content before nav section" {
            $content = Get-Content $TestTomlPath -Raw
            $content | Should -Match 'site_name = "Test Site"'
        }

        It "Should preserve content after nav section" {
            $content = Get-Content $TestTomlPath -Raw
            $content | Should -Match '\[project\.theme\]'
        }
    }

    Context "When nav content is already up to date" {
        It "Should return false when no changes needed" {
            $testPath = Join-Path $TestDrive "test-no-change.toml"
            @"
[project]
nav = [
  {"Same" = "same.md"},
]
"@ | Set-Content -Path $testPath -Encoding UTF8

            $sameNav = @"
nav = [
  {"Same" = "same.md"},
]
"@
            $result = Update-ZensicalNav -zensicalFilePath $testPath -newNavContent $sameNav
            $result | Should -Be $false
        }
    }
}

Describe "TOML Output Format Validation" {
    BeforeAll {
        $script:FormatTestDocs = Join-Path $TestDrive "format-test-docs"
        New-Item -Path $FormatTestDocs -ItemType Directory -Force | Out-Null

        @"
---
title: Test Home
---
"@ | Set-Content -Path (Join-Path $FormatTestDocs "index.md") -Encoding UTF8

        $script:GeneratedNav = Build-NavigationToml -docsBasePath $FormatTestDocs
    }

    It "Should use proper TOML inline table syntax with curly braces" {
        $GeneratedNav | Should -Match '\{".+" = ".+"\}'
    }

    It "Should use double quotes for all strings" {
        $GeneratedNav | Should -Not -Match "= '[^']+'"
    }

    It "Should have proper array structure with brackets" {
        $GeneratedNav | Should -Match '^\s*nav = \['
        $GeneratedNav | Should -Match '\]$'
    }
}

Describe "Edge Cases" {
    Context "When directory contains special characters in titles" {
        It "Should handle titles with colons" {
            $specialDocs = Join-Path $TestDrive "special-docs"
            New-Item -Path $specialDocs -ItemType Directory -Force | Out-Null

            @"
---
title: Home
---
"@ | Set-Content -Path (Join-Path $specialDocs "index.md") -Encoding UTF8

            @"
---
title: "Guide: Special Characters"
---
"@ | Set-Content -Path (Join-Path $specialDocs "special-guide.md") -Encoding UTF8

            $nav = Build-NavigationToml -docsBasePath $specialDocs
            $nav | Should -Match '"Guide: Special Characters"'
        }
    }

    Context "When directory is empty except for index" {
        It "Should create a section structure when section has only index.md" {
            $emptySection = Join-Path $TestDrive "empty-section-docs"
            New-Item -Path $emptySection -ItemType Directory -Force | Out-Null

            @"
---
title: Home
---
"@ | Set-Content -Path (Join-Path $emptySection "index.md") -Encoding UTF8

            $emptyDir = Join-Path $emptySection "empty-dir"
            New-Item -Path $emptyDir -ItemType Directory -Force | Out-Null

            @"
---
title: Empty Section
---
"@ | Set-Content -Path (Join-Path $emptyDir "index.md") -Encoding UTF8

            $nav = Build-NavigationToml -docsBasePath $emptySection
            # Sections with only index.md still get wrapped in a section with title from ConvertTo-Title
            $nav | Should -Match '"empty-dir/index\.md"'
        }
    }

    Context "When resources directory exists" {
        It "Should exclude resources directory from navigation" {
            $resourcesDocs = Join-Path $TestDrive "resources-docs"
            New-Item -Path $resourcesDocs -ItemType Directory -Force | Out-Null

            @"
---
title: Home
---
"@ | Set-Content -Path (Join-Path $resourcesDocs "index.md") -Encoding UTF8

            $resourcesDir = Join-Path $resourcesDocs "resources"
            New-Item -Path $resourcesDir -ItemType Directory -Force | Out-Null
            New-Item -Path (Join-Path $resourcesDir "images") -ItemType Directory -Force | Out-Null

            $nav = Build-NavigationToml -docsBasePath $resourcesDocs
            $nav | Should -Not -Match 'resources'
        }
    }

    Context "When files have nav_order in frontmatter" {
        It "Should sort files by nav_order, with ordered files before unordered" {
            $navOrderDocs = Join-Path $TestDrive "nav-order-docs"
            New-Item -Path $navOrderDocs -ItemType Directory -Force | Out-Null

            @"
---
title: Home
---
"@ | Set-Content -Path (Join-Path $navOrderDocs "index.md") -Encoding UTF8

            # Create a section with files that have nav_order
            $sectionPath = Join-Path $navOrderDocs "manual"
            New-Item -Path $sectionPath -ItemType Directory -Force | Out-Null

            @"
---
title: Manual
---
"@ | Set-Content -Path (Join-Path $sectionPath "index.md") -Encoding UTF8

            # File without nav_order (should come last)
            @"
---
title: Zebra Page
---
"@ | Set-Content -Path (Join-Path $sectionPath "zebra.md") -Encoding UTF8

            # File with nav_order 2
            @"
---
title: Second Page
nav_order: 2
---
"@ | Set-Content -Path (Join-Path $sectionPath "beta.md") -Encoding UTF8

            # File with nav_order 1
            @"
---
title: First Page
nav_order: 1
---
"@ | Set-Content -Path (Join-Path $sectionPath "alpha.md") -Encoding UTF8

            $nav = Build-NavigationToml -docsBasePath $navOrderDocs

            # Extract the order of items in the manual section
            # The pattern should show alpha (nav_order 1) before beta (nav_order 2) before zebra (no nav_order)
            $alphaPos = $nav.IndexOf('"First Page"')
            $betaPos = $nav.IndexOf('"Second Page"')
            $zebraPos = $nav.IndexOf('"Zebra Page"')

            $alphaPos | Should -BeLessThan $betaPos -Because "nav_order 1 should come before nav_order 2"
            $betaPos | Should -BeLessThan $zebraPos -Because "files with nav_order should come before files without"
        }

        It "Should sort subdirectories by nav_order from their index.md" {
            $subDirOrderDocs = Join-Path $TestDrive "subdir-order-docs"
            New-Item -Path $subDirOrderDocs -ItemType Directory -Force | Out-Null

            @"
---
title: Home
---
"@ | Set-Content -Path (Join-Path $subDirOrderDocs "index.md") -Encoding UTF8

            # Create topic with subdirectories having nav_order
            $topicPath = Join-Path $subDirOrderDocs "topic"
            New-Item -Path $topicPath -ItemType Directory -Force | Out-Null

            @"
---
title: Topic
---
"@ | Set-Content -Path (Join-Path $topicPath "index.md") -Encoding UTF8

            # Subdir without nav_order
            $zdirPath = Join-Path $topicPath "zdir"
            New-Item -Path $zdirPath -ItemType Directory -Force | Out-Null
            @"
---
title: Zdir Section
---
"@ | Set-Content -Path (Join-Path $zdirPath "index.md") -Encoding UTF8

            # Subdir with nav_order 2
            $bdirPath = Join-Path $topicPath "bdir"
            New-Item -Path $bdirPath -ItemType Directory -Force | Out-Null
            @"
---
title: Bdir Section
nav_order: 2
---
"@ | Set-Content -Path (Join-Path $bdirPath "index.md") -Encoding UTF8

            # Subdir with nav_order 1
            $adirPath = Join-Path $topicPath "adir"
            New-Item -Path $adirPath -ItemType Directory -Force | Out-Null
            @"
---
title: Adir Section
nav_order: 1
---
"@ | Set-Content -Path (Join-Path $adirPath "index.md") -Encoding UTF8

            $nav = Build-NavigationToml -docsBasePath $subDirOrderDocs

            # The order should be adir (nav_order 1), bdir (nav_order 2), zdir (no nav_order)
            # Note: ConvertTo-Title converts directory names, so we look for "Adir", "Bdir", "Zdir"
            $adirPos = $nav.IndexOf('"Adir"')
            $bdirPos = $nav.IndexOf('"Bdir"')
            $zdirPos = $nav.IndexOf('"Zdir"')

            $adirPos | Should -BeLessThan $bdirPos -Because "nav_order 1 should come before nav_order 2"
            $bdirPos | Should -BeLessThan $zdirPos -Because "directories with nav_order should come before directories without"
        }
    }
}

Describe "Integration Test" {
    BeforeAll {
        # Create a complete test wiki structure
        $script:IntegrationDocs = Join-Path $TestDrive "integration-docs"
        New-Item -Path $IntegrationDocs -ItemType Directory -Force | Out-Null

        # Root index
        @"
---
title: TCAT Wiki
---
"@ | Set-Content -Path (Join-Path $IntegrationDocs "index.md") -Encoding UTF8

        # OpenSidewalks section
        $oswPath = Join-Path $IntegrationDocs "opensidewalks"
        New-Item -Path $oswPath -ItemType Directory -Force | Out-Null

        @"
---
title: OpenSidewalks
---
"@ | Set-Content -Path (Join-Path $oswPath "index.md") -Encoding UTF8

        # Schema subsection
        $schemaPath = Join-Path $oswPath "schema"
        New-Item -Path $schemaPath -ItemType Directory -Force | Out-Null

        @"
---
title: Schema
---
"@ | Set-Content -Path (Join-Path $schemaPath "index.md") -Encoding UTF8

        @"
---
title: Core Edges in OSW
---
"@ | Set-Content -Path (Join-Path $schemaPath "core-edges-in-osw.md") -Encoding UTF8

        # TDEI section
        $tdeiPath = Join-Path $IntegrationDocs "tdei"
        New-Item -Path $tdeiPath -ItemType Directory -Force | Out-Null

        @"
---
title: TDEI
---
"@ | Set-Content -Path (Join-Path $tdeiPath "index.md") -Encoding UTF8

        # Root contributing file
        @"
---
title: Contributing
---
"@ | Set-Content -Path (Join-Path $IntegrationDocs "CONTRIBUTING.md") -Encoding UTF8

        $script:IntegrationNav = Build-NavigationToml -docsBasePath $IntegrationDocs
    }

    It "Should generate valid TOML structure" {
        $IntegrationNav | Should -Match '^nav = \['
        $IntegrationNav | Should -Match '\]$'
    }

    It "Should include root home page first" {
        $lines = $IntegrationNav -split "`n"
        $firstEntry = $lines | Where-Object { $_ -match '\{' } | Select-Object -First 1
        $firstEntry | Should -Match '"TCAT Wiki"'
    }

    It "Should correctly nest OpenSidewalks section" {
        $IntegrationNav | Should -Match '\{"OpenSidewalks" = \['
    }

    It "Should correctly nest Schema subsection under OpenSidewalks" {
        $IntegrationNav | Should -Match '\{"Schema" = \['
    }

    It "Should use correct acronym casing for TDEI" {
        $IntegrationNav | Should -Match '\{"TDEI" = \['
    }

    It "Should include Contributing at root level" {
        $IntegrationNav | Should -Match '\{"Contributing" = "CONTRIBUTING\.md"\}'
    }
}
