#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Utility Runner
# Version: 3.0.0
# Date: 2026-02-06
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Runs all TCAT Wiki utility scripts with validation

.DESCRIPTION
    This script performs two phases:

    PHASE 1: Runs Pester tests for all utility scripts to ensure they are working correctly.
    The tests are run in this order:
    1. run-utils.Tests.ps1 (self-check)
    2. generate-guides-lists.Tests.ps1
    3. generate-nav.Tests.ps1
    4. check-links.Tests.ps1

    If any test fails, the script exits with an error code.

    PHASE 2: Runs the utility scripts in sequence:
    1. generate-guides-lists.ps1 - Generates guide sections in index.md files
    2. generate-nav.ps1 - Updates navigation in zensical.toml
    3. check-links.ps1 - Validates all links in documentation

.PARAMETER SkipTests
    Skip Phase 1 (Pester tests) and run utilities directly.
    Use with caution - only recommended when you've already run tests.

.PARAMETER TestsOnly
    Run only Phase 1 (Pester tests) without running the utilities.

.PARAMETER SkipLinkCheck
    Skip external link checking in Phase 2 (internal links are still checked). Useful for quick iterations.
    Mutually exclusive with -NoCache.

.PARAMETER NoCache
    Force fresh external link checks by bypassing the cache. Passes -NoCache to check-links.ps1.
    Mutually exclusive with -SkipLinkCheck.

.EXAMPLE
    .\run-utils.ps1
    Runs all tests, then all utilities if tests pass.

.EXAMPLE
    .\run-utils.ps1 -TestsOnly
    Runs only the Pester tests.

.EXAMPLE
    .\run-utils.ps1 -SkipTests
    Skips tests and runs utilities directly.

.EXAMPLE
    .\run-utils.ps1 -SkipLinkCheck
    Runs tests and utilities, but skips external link checking (internal links still checked).

.EXAMPLE
    .\run-utils.ps1 -NoCache
    Runs tests and utilities, forcing fresh external link checks (bypasses cache).
#>

param(
    [switch]$SkipTests,
    [switch]$TestsOnly,
    [switch]$SkipLinkCheck,
    [switch]$NoCache
)

# Validate mutually exclusive parameters
if ($SkipLinkCheck -and $NoCache) {
    Write-Host "ERROR: -SkipLinkCheck and -NoCache cannot be used together." -ForegroundColor Red
    Write-Host "  -SkipLinkCheck: Skips external link checking entirely (only internal links checked)" -ForegroundColor Yellow
    Write-Host "  -NoCache: Forces fresh external link checks (bypasses cache)" -ForegroundColor Yellow
    exit 1
}

#region Helper Functions
# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

function Test-PesterVersion {
    <#
    .SYNOPSIS
        Checks if Pester v5+ is installed
    .DESCRIPTION
        Verifies that Pester module version 5.0.0 or higher is available.
        Returns $true if valid, $false otherwise.
    .OUTPUTS
        Boolean indicating whether Pester v5+ is available
    #>
    $requiredVersion = [Version]"5.0.0"

    $pesterModule = Get-Module -Name Pester -ListAvailable |
        Sort-Object Version -Descending |
        Select-Object -First 1

    if (-not $pesterModule) {
        Write-Host "  ✗ ERROR: Pester module is not installed." -ForegroundColor Red
        Write-Host "    Install with: Install-Module -Name Pester -Force -SkipPublisherCheck" -ForegroundColor Yellow
        return $false
    }

    if ($pesterModule.Version -lt $requiredVersion) {
        Write-Host "  ✗ ERROR: Pester v5+ is required. Found v$($pesterModule.Version)" -ForegroundColor Red
        Write-Host "    Update with: Install-Module -Name Pester -Force -SkipPublisherCheck" -ForegroundColor Yellow
        return $false
    }

    # Import the correct version
    Import-Module Pester -MinimumVersion $requiredVersion -Force
    return $true
}

function Get-TestFiles {
    <#
    .SYNOPSIS
        Gets all Pester test files in the util directory in the correct order
    .DESCRIPTION
        Returns test files with run-utils.Tests.ps1 first (self-check),
        followed by other test files in alphabetical order.
    .OUTPUTS
        Array of FileInfo objects for test files
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UtilPath
    )

    $allTests = Get-ChildItem -Path $UtilPath -Filter "*.Tests.ps1" -File | Sort-Object Name

    # Separate self-test from others
    $selfTest = $allTests | Where-Object { $_.Name -eq "run-utils.Tests.ps1" }
    $otherTests = $allTests | Where-Object { $_.Name -ne "run-utils.Tests.ps1" }

    # Return self-test first, then others
    $result = @()
    if ($selfTest) {
        $result += $selfTest
    }
    $result += $otherTests

    return $result
}

function Invoke-PesterTests {
    <#
    .SYNOPSIS
        Runs Pester tests for all test files
    .DESCRIPTION
        Executes each test file and tracks results. Returns $true if all pass.
    .OUTPUTS
        Boolean indicating whether all tests passed
    #>
    param(
        [Parameter(Mandatory = $true)]
        [array]$TestFiles
    )

    $allPassed = $true
    $totalTests = 0
    $totalPassed = 0
    $totalFailed = 0

    foreach ($testFile in $TestFiles) {
        Write-Host "  Running: $($testFile.Name)" -ForegroundColor Cyan

        try {
            $config = New-PesterConfiguration
            $config.Run.Path = $testFile.FullName
            $config.Run.PassThru = $true
            $config.Output.Verbosity = 'Minimal'
            $result = Invoke-Pester -Configuration $config -ErrorAction Stop
        } catch {
            Write-Host "    ✗ ERROR: Failed to run Pester - $_" -ForegroundColor Red
            $allPassed = $false
            continue
        }

        if ($null -eq $result) {
            Write-Host "    ✗ ERROR: Pester returned no result" -ForegroundColor Red
            $allPassed = $false
            continue
        }

        $totalTests += $result.TotalCount
        $totalPassed += $result.PassedCount
        $totalFailed += $result.FailedCount

        if ($result.FailedCount -gt 0) {
            Write-Host "    ✗ FAILED: $($result.FailedCount) test(s) failed" -ForegroundColor Red
            $allPassed = $false
        } else {
            Write-Host "    ✓ PASSED: $($result.PassedCount) test(s)" -ForegroundColor Green
        }
    }

    Write-Host ""
    Write-Host "  Summary: $totalPassed/$totalTests tests passed" -ForegroundColor $(if ($allPassed) { "Green" } else { "Red" })

    return $allPassed
}

function Invoke-UtilityScript {
    <#
    .SYNOPSIS
        Runs a utility script and checks for errors
    .DESCRIPTION
        Executes a PowerShell script and returns $true if it succeeds.
    .OUTPUTS
        Boolean indicating whether the script succeeded
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$ScriptPath,

        [Parameter(Mandatory = $false)]
        [string]$Description = "",

        [Parameter(Mandatory = $false)]
        [switch]$Silent
    )

    $scriptName = Split-Path -Leaf $ScriptPath

    if (-not $Silent) {
        if ($Description) {
            Write-Host "  $Description" -ForegroundColor Cyan
        }
        Write-Host "  Running: $scriptName" -ForegroundColor Cyan
        Write-Host ""
    }

    # Reset LASTEXITCODE before running
    $global:LASTEXITCODE = 0

    try {
        if ($Silent) {
            & $ScriptPath *> $null
        } else {
            & $ScriptPath
        }

        if ($LASTEXITCODE -ne 0) {
            if (-not $Silent) {
                Write-Host ""
                Write-Host "  ✗ FAILED: $scriptName exited with code $LASTEXITCODE" -ForegroundColor Red
            }
            return $false
        }

        if (-not $Silent) {
            Write-Host ""
            Write-Host "  ✓ COMPLETED: $scriptName" -ForegroundColor Green
        }
        return $true
    } catch {
        if (-not $Silent) {
            Write-Host ""
            Write-Host "  ✗ ERROR: $scriptName - $_" -ForegroundColor Red
        }
        return $false
    }
}

#endregion Helper Functions

# ==============================================================================
# MAIN SCRIPT
# ==============================================================================

Write-Host ""
Write-Host "TCAT Wiki - Utility Runner v1.0.0"
Write-Host "==================================="
Write-Host ""

# Determine script location
$utilPath = $PSScriptRoot
if (-not $utilPath) {
    $utilPath = Split-Path -Parent $MyInvocation.MyCommand.Path
}

# Verify we're in the right place
if (-not (Test-Path (Join-Path $utilPath "generate-nav.ps1"))) {
    Write-Error "Could not find utility scripts. Please run from the util directory."
    exit 1
}

# ==============================================================================
# PHASE 1: Run Pester Tests
# ==============================================================================

if (-not $SkipTests) {
    Write-Host "PHASE 1: Running Pester Tests"
    Write-Host "------------------------------"
    Write-Host ""

    # Check Pester version first
    if (-not (Test-PesterVersion)) {
        Write-Host ""
        Write-Host "==========================================="
        Write-Host "PHASE 1 FAILED: Pester v5+ is required" -ForegroundColor Red
        Write-Host ""
        exit 1
    }

    $testFiles = Get-TestFiles -UtilPath $utilPath

    if ($testFiles.Count -eq 0) {
        Write-Host "  No test files found!" -ForegroundColor Yellow
    } else {
        Write-Host "  Found $($testFiles.Count) test file(s)"
        Write-Host ""

        $allTestsPassed = Invoke-PesterTests -TestFiles $testFiles

        if (-not $allTestsPassed) {
            Write-Host ""
            Write-Host "==========================================="
            Write-Host "PHASE 1 FAILED: Some tests did not pass" -ForegroundColor Red
            Write-Host "Fix the failing tests before running utilities."
            Write-Host ""
            exit 1
        }

        Write-Host ""
        Write-Host "PHASE 1 COMPLETE: All tests passed" -ForegroundColor Green
    }

    Write-Host ""
}

# ==============================================================================
# PHASE 2: Run Utility Scripts
# ==============================================================================

if (-not $TestsOnly) {
    Write-Host "PHASE 2: Running Utility Scripts"
    Write-Host "---------------------------------"
    Write-Host ""

    # 1. Generate guides lists
    $guidesListScript = Join-Path $utilPath "generate-guides-lists.ps1"
    if (-not (Invoke-UtilityScript -ScriptPath $guidesListScript -Description "Step 1/3: Generating guides lists")) {
        Write-Host ""
        Write-Host "==========================================="
        Write-Host "PHASE 2 FAILED at Step 1" -ForegroundColor Red
        exit 1
    }

    Write-Host ""

    # 2. Generate navigation
    $navScript = Join-Path $utilPath "generate-nav.ps1"
    if (-not (Invoke-UtilityScript -ScriptPath $navScript -Description "Step 2/3: Generating navigation")) {
        Write-Host ""
        Write-Host "==========================================="
        Write-Host "PHASE 2 FAILED at Step 2" -ForegroundColor Red
        exit 1
    }

    Write-Host ""

    # 3. Check links
    $linkCheckScript = Join-Path $utilPath "check-links.ps1"
    if ($SkipLinkCheck) {
        # Only check internal links when -SkipLinkCheck is used
        Write-Host "  Step 3/3: Checking internal links only (-SkipLinkCheck)" -ForegroundColor Cyan
        Write-Host ""
        & $linkCheckScript -internal
        if ($LASTEXITCODE -ne 0) {
            Write-Host ""
            Write-Host "==========================================="
            Write-Host "PHASE 2 FAILED at Step 3" -ForegroundColor Red
            exit 1
        }
    } elseif ($NoCache) {
        # Check all links with fresh cache
        Write-Host "  Step 3/3: Checking all links (-NoCache)" -ForegroundColor Cyan
        Write-Host ""
        & $linkCheckScript -NoCache
        if ($LASTEXITCODE -ne 0) {
            Write-Host ""
            Write-Host "==========================================="
            Write-Host "PHASE 2 FAILED at Step 3" -ForegroundColor Red
            exit 1
        }
    } else {
        # Check both internal and external links (with cache)
        if (-not (Invoke-UtilityScript -ScriptPath $linkCheckScript -Description "Step 3/3: Checking all links")) {
            Write-Host ""
            Write-Host "==========================================="
            Write-Host "PHASE 2 FAILED at Step 3" -ForegroundColor Red
            exit 1
        }
    }

    Write-Host ""
    Write-Host "PHASE 2 COMPLETE: All utilities ran successfully" -ForegroundColor Green
}

Write-Host ""
Write-Host "==========================================="
Write-Host "Utility runner complete!"
Write-Host ""
