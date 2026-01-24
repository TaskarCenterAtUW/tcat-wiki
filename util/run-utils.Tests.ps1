#!/usr/bin/env pwsh
#Requires -Modules @{ ModuleName='Pester'; ModuleVersion='5.0.0' }

# Name: TCAT Wiki - Utility Runner Tests
# Version: 1.0.0
# Date: 2026-01-02
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Pester tests for run-utils.ps1

.DESCRIPTION
    Test suite for the TCAT Wiki utility runner script.
    Tests helper functions and validates script behavior.

.EXAMPLE
    Invoke-Pester .\run-utils.Tests.ps1
    Runs all tests in the test file

.EXAMPLE
    Invoke-Pester .\run-utils.Tests.ps1 -Output Detailed
    Runs all tests with detailed output

.NOTES
    Requires Pester v5+ to be installed: Install-Module -Name Pester -Force -SkipPublisherCheck
#>

BeforeAll {
    # Extract and load the helper functions from run-utils.ps1
    $scriptPath = Join-Path $PSScriptRoot "run-utils.ps1"
    $scriptContent = Get-Content $scriptPath -Raw

    # Extract the helper functions region and execute it
    if ($scriptContent -match '(?s)#region Helper Functions(.+?)#endregion Helper Functions') {
        $functionBlock = $matches[1]
        # Create and invoke script block to define functions in current scope
        $sb = [ScriptBlock]::Create($functionBlock)
        . $sb
    } else {
        throw "Could not find Helper Functions region in run-utils.ps1"
    }
}

# ==============================================================================
# GET-TESTFILES TESTS
# ==============================================================================

Describe "Get-TestFiles" {
    BeforeAll {
        # Create test directory with mock test files
        $script:testUtilDir = Join-Path $TestDrive "test-util"
        New-Item -Path $testUtilDir -ItemType Directory -Force | Out-Null

        # Create mock test files
        "# mock test" | Set-Content -Path (Join-Path $testUtilDir "alpha.Tests.ps1") -Encoding UTF8
        "# mock test" | Set-Content -Path (Join-Path $testUtilDir "beta.Tests.ps1") -Encoding UTF8
        "# mock test" | Set-Content -Path (Join-Path $testUtilDir "run-utils.Tests.ps1") -Encoding UTF8
        "# mock test" | Set-Content -Path (Join-Path $testUtilDir "zeta.Tests.ps1") -Encoding UTF8

        # Create non-test files (should be ignored)
        "# script" | Set-Content -Path (Join-Path $testUtilDir "some-script.ps1") -Encoding UTF8
    }

    It "Should return only .Tests.ps1 files" {
        $result = Get-TestFiles -UtilPath $testUtilDir
        $result | ForEach-Object { $_.Name | Should -Match '\.Tests\.ps1$' }
    }

    It "Should return run-utils.Tests.ps1 first" {
        $result = Get-TestFiles -UtilPath $testUtilDir
        $result[0].Name | Should -Be "run-utils.Tests.ps1"
    }

    It "Should return other test files in alphabetical order after run-utils" {
        $result = Get-TestFiles -UtilPath $testUtilDir
        $result[1].Name | Should -Be "alpha.Tests.ps1"
        $result[2].Name | Should -Be "beta.Tests.ps1"
        $result[3].Name | Should -Be "zeta.Tests.ps1"
    }

    It "Should return correct count of test files" {
        $result = Get-TestFiles -UtilPath $testUtilDir
        $result.Count | Should -Be 4
    }

    Context "When run-utils.Tests.ps1 does not exist" {
        BeforeAll {
            $script:noSelfTestDir = Join-Path $TestDrive "no-self-test"
            New-Item -Path $noSelfTestDir -ItemType Directory -Force | Out-Null
            "# mock test" | Set-Content -Path (Join-Path $noSelfTestDir "other.Tests.ps1") -Encoding UTF8
        }

        It "Should return other tests without error" {
            $result = Get-TestFiles -UtilPath $noSelfTestDir
            $result.Count | Should -Be 1
            $result[0].Name | Should -Be "other.Tests.ps1"
        }
    }

    Context "When no test files exist" {
        BeforeAll {
            $script:emptyDir = Join-Path $TestDrive "empty-util"
            New-Item -Path $emptyDir -ItemType Directory -Force | Out-Null
            "# script" | Set-Content -Path (Join-Path $emptyDir "script.ps1") -Encoding UTF8
        }

        It "Should return empty array" {
            $result = Get-TestFiles -UtilPath $emptyDir
            $result.Count | Should -Be 0
        }
    }
}

# ==============================================================================
# INVOKE-UTILITYSCRIPT TESTS
# ==============================================================================

Describe "Invoke-UtilityScript" {
    Context "When script succeeds" {
        BeforeAll {
            $script:successScript = Join-Path $TestDrive "success-script.ps1"
            @'
Write-Host "Success!"
exit 0
'@ | Set-Content -Path $successScript -Encoding UTF8
        }

        It "Should return true" {
            $result = Invoke-UtilityScript -ScriptPath $successScript -Silent
            $result | Should -Be $true
        }
    }

    Context "When script fails with exit code" {
        BeforeAll {
            $script:failScript = Join-Path $TestDrive "fail-script.ps1"
            @'
Write-Host "Failing!"
exit 1
'@ | Set-Content -Path $failScript -Encoding UTF8
        }

        It "Should return false" {
            $result = Invoke-UtilityScript -ScriptPath $failScript -Silent
            $result | Should -Be $false
        }
    }

    Context "When script does not exist" {
        It "Should return false and not throw" {
            $result = Invoke-UtilityScript -ScriptPath "C:\nonexistent\script.ps1" -ErrorAction SilentlyContinue -Silent
            $result | Should -Be $false
        }
    }

    Context "With description parameter" {
        BeforeAll {
            $script:descScript = Join-Path $TestDrive "desc-script.ps1"
            "Write-Host 'Done'" | Set-Content -Path $descScript -Encoding UTF8
        }

        It "Should accept description parameter" {
            { Invoke-UtilityScript -ScriptPath $descScript -Description "Test description" -Silent } | Should -Not -Throw
        }
    }
}

# ==============================================================================
# SCRIPT STRUCTURE TESTS
# ==============================================================================

Describe "Script Structure" {
    BeforeAll {
        $script:scriptPath = Join-Path $PSScriptRoot "run-utils.ps1"
        $script:scriptContent = Get-Content $scriptPath -Raw
    }

    It "Should have Helper Functions region" {
        $scriptContent | Should -Match '#region Helper Functions'
        $scriptContent | Should -Match '#endregion Helper Functions'
    }

    It "Should define Get-TestFiles function" {
        $scriptContent | Should -Match 'function Get-TestFiles'
    }

    It "Should define Invoke-PesterTests function" {
        $scriptContent | Should -Match 'function Invoke-PesterTests'
    }

    It "Should define Invoke-UtilityScript function" {
        $scriptContent | Should -Match 'function Invoke-UtilityScript'
    }

    It "Should have SkipTests parameter" {
        $scriptContent | Should -Match '\[switch\]\$SkipTests'
    }

    It "Should have TestsOnly parameter" {
        $scriptContent | Should -Match '\[switch\]\$TestsOnly'
    }

    It "Should have SkipLinkCheck parameter" {
        $scriptContent | Should -Match '\[switch\]\$SkipLinkCheck'
    }

    It "Should reference generate-guides-lists.ps1" {
        $scriptContent | Should -Match 'generate-guides-lists\.ps1'
    }

    It "Should reference generate-nav.ps1" {
        $scriptContent | Should -Match 'generate-nav\.ps1'
    }

    It "Should reference check-links.ps1" {
        $scriptContent | Should -Match 'check-links\.ps1'
    }
}

# ==============================================================================
# INTEGRATION TESTS
# ==============================================================================

Describe "Integration Tests" -Tag "Integration" {
    Context "Actual util directory" {
        It "Should find test files in real util directory" {
            $result = Get-TestFiles -UtilPath $PSScriptRoot
            $result.Count | Should -BeGreaterThan 0
        }

        It "Should find run-utils.Tests.ps1 first in real util directory" {
            $result = Get-TestFiles -UtilPath $PSScriptRoot
            $result[0].Name | Should -Be "run-utils.Tests.ps1"
        }

        It "Should find at least 4 test files (run-utils, generate-guides-lists, generate-nav, check-links)" {
            $result = Get-TestFiles -UtilPath $PSScriptRoot
            $result.Count | Should -BeGreaterOrEqual 4
        }
    }
}

# ==============================================================================
# EDGE CASE TESTS
# ==============================================================================

Describe "Edge Cases" {
    Context "Script with no exit code" {
        BeforeAll {
            $script:noExitScript = Join-Path $TestDrive "no-exit-script.ps1"
            "Write-Host 'No explicit exit'" | Set-Content -Path $noExitScript -Encoding UTF8
        }

        It "Should return true when script completes without explicit exit" {
            $result = Invoke-UtilityScript -ScriptPath $noExitScript -Silent
            $result | Should -Be $true
        }
    }

    Context "Script with Write-Error but no exit" {
        BeforeAll {
            $script:errorScript = Join-Path $TestDrive "error-script.ps1"
            @'
Write-Error "Something went wrong" -ErrorAction SilentlyContinue
Write-Host "But continuing..."
'@ | Set-Content -Path $errorScript -Encoding UTF8
        }

        It "Should return true if script completes despite Write-Error" {
            $result = Invoke-UtilityScript -ScriptPath $errorScript -ErrorAction SilentlyContinue -Silent
            $result | Should -Be $true
        }
    }
}
