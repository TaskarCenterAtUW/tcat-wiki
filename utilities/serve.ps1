#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Local Serve Wrapper
# Version: 1.0.0
# Date: 2026-07-06
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
    Serves a local preview of the site that matches the deployed build exactly.

.DESCRIPTION
    Wraps utilities/build_site.py: runs the two-layer build prep (copy, filter,
    dispatch generation, agent-doc stripping, and zensical.build.toml generation),
    then runs `zensical serve -f zensical.build.toml`.

    Unlike running `zensical serve` directly against the committed zensical.toml
    (which reads docs_dir = docs and therefore shows every assistant stub/draft
    page), this wrapper serves the same human-docs/ layer that gets deployed.

    Source edits are NOT live-reloaded across the human/agent split: editing a
    file under docs/ will not update the running preview. Stop the server
    (Ctrl+C) and re-run this script to refresh after making source edits.

.EXAMPLE
    .\utilities\serve.ps1
    Prepares the two-layer build, then serves it at http://localhost:8000

.NOTES
    Requires the Python virtual environment to be activated first:
        .\.venv\Scripts\Activate.ps1
#>

$repoRoot = Split-Path -Parent $PSScriptRoot
Push-Location $repoRoot
try {
    python utilities/build_site.py --serve
} finally {
    Pop-Location
}
