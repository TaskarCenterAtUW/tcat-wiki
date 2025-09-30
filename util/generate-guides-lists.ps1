#!/usr/bin/env pwsh
# This script is designed to be run in a PowerShell environment.

# Name: TCAT Wiki - Guides Lists Generator
# Version: 1.0.2
# Date: 2025-09-30
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

<#
.SYNOPSIS
	Generates index.md files for all guides directories

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
	
	# Special case: if we're in docs/guides-list, link to self
	if ($pathParts.Count -eq 1 -and $pathParts[0] -eq 'guides-list') {
		return 'index.md'
	}
	
	# Calculate how many levels to go back from current guides directory to docs
	# We need to go back pathParts.Count levels to get to docs root
	$levelsToGoBack = $pathParts.Count
	
	if ($levelsToGoBack -eq 1) {
		# We're in docs/guides-list
		return 'index.md'
	}
	else {
		$backPath = ('../' * $levelsToGoBack) + 'guides-list/index.md'
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
	
	# Get all .md files except main index.md
	$mdFiles = Get-ChildItem -Path $GuidesPath -Filter "*.md" | 
	Where-Object { $_.Name -ne "index.md" } |
	Sort-Object Name
	
	if ($mdFiles.Count -eq 0) {
		Write-Host "  No guides found (excluding index.md)"
		return
	}
	
	# Get the parent path for building descriptions
	$parentPath = Split-Path $GuidesPath -Parent
	
	# Create appropriate title based on directory structure
	$sectionTitle = switch -Regex ($GuidesPath) {
		'docs[/\\]guides-list$' { "Guides List" }
		'aviv-scoutroute[/\\]long-form[/\\]guides$' { "Long Form Quest Definition Guides" }
		default { 
			# Get parent directory name and convert to title case
			$parentDirName = Split-Path (Split-Path $GuidesPath -Parent) -Leaf
			
			# Handle special cases for better formatting
			$titleName = switch ($parentDirName) {
				'opensidewalks' { 'OpenSidewalks' }
				'aviv-scoutroute' { 'AVIV ScoutRoute' }
				'josm' { 'JOSM' }
				'accessmap' { 'AccessMap' }
				'tdei-core' { 'TDEI Core' }
				default { 
					# Convert kebab-case to Title Case
					($parentDirName -split '-' | ForEach-Object { 
						$_.Substring(0, 1).ToUpper() + $_.Substring(1).ToLower() 
					}) -join ' '
				}
			}
			"$titleName Guides"
		}
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
		'docs[/\\]guides-list$' { 
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
	if ($GuidesPath -notmatch 'docs[/\\]guides-list$') {
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

# Auto-detect docs path
$docsPath = ""
# Check if we're in the util directory
if (Test-Path "..\docs") {
	$docsPath = "..\docs"
}
# Check if we're in the repository root
elseif (Test-Path "docs") {
	$docsPath = "docs"
}
else {
	Write-Error "docs directory not found. Please run this script from the repository root or util directory."
	exit 1
}

# Find all directories named "guides" under docs
$guidesDirectories = Get-ChildItem -Path $docsPath -Recurse -Directory -ErrorAction Stop | 
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

# Generate master guides index by aggregating all other guides directories
Write-Host "Generating master guides index..."

$masterContent = @()
$masterContent += "---"
$masterContent += "title: Guides List"
$masterContent += "---"
$masterContent += ""
$masterContent += "# Guides List"
$masterContent += ""
$masterContent += "Guides, tutorials, and user manuals produced by TCAT and/or its partners are listed below."
$masterContent += ""

# Process each guides directory (excluding the main docs/guides-list)
foreach ($guidesDir in $guidesDirectories | Where-Object { $_.FullName -notmatch 'docs[/\\]guides-list$' }) {
	$indexPath = Join-Path $guidesDir.FullName "index.md"
	
	if (Test-Path $indexPath) {
		Write-Host "  Aggregating: $($guidesDir.FullName)"
		
		try {
			$content = Get-Content $indexPath -ErrorAction Stop
			$inFrontMatter = $false
			$foundTitle = $false
			$sectionTitle = ""
			$relativePath = ""
			
			# Extract section title and calculate relative path
			foreach ($line in $content) {
				if ($line -eq '---') {
					$inFrontMatter = -not $inFrontMatter
					continue
				}
				if ($inFrontMatter -and $line -match '^title:\s*(.+)$') {
					$sectionTitle = $matches[1].Trim()
					continue
				}
				if (-not $inFrontMatter -and -not $foundTitle -and $line -match '^#\s+(.+)$') {
					if (-not $sectionTitle) {
						$sectionTitle = $matches[1].Trim()
					}
					$foundTitle = $true
					break
				}
			}
			
			# Calculate relative path from docs/guides-list to this guides directory
			$guidesPath = $guidesDir.FullName -replace '[/\\]', '/'
			if ($guidesPath -match 'docs/(.*)') {
				$relativePath = "../$($matches[1])/index.md"
			}
			
			# Add section header
			if ($sectionTitle -and $relativePath) {
				$masterContent += "## [$sectionTitle]($relativePath)"
				$masterContent += ""
				
				# Extract and add individual guide entries  
				$guidesBasePath = ($guidesPath -replace '.*docs/', '') -replace '/guides$', ''
				$frontMatterCount = 0
				$afterContentSeparator = $false
				
				foreach ($line in $content) {
					# Count front matter separators (first two ---)
					if ($line -eq '---') {
						$frontMatterCount++
						if ($frontMatterCount -eq 3) {
							# This is the content separator, start capturing after this
							$afterContentSeparator = $true
							continue
						}
						if ($frontMatterCount -le 2) {
							continue  # Skip front matter
						}
					}
					
					# Skip content until we reach the separator
					if ($frontMatterCount -lt 3) {
						continue
					}
					
					# Process guide entries after the separator
					if ($afterContentSeparator) {
						if ($line.Trim() -ne '') {
							# Adjust relative paths for guide links
							if ($line -match '^###\s+\[([^\]]+)\]\(([^)]+)\)') {
								$guideTitle = $matches[1]
								$guideFile = $matches[2]
								# Convert relative path to be relative from docs/guides-list
								$adjustedPath = "../$guidesBasePath/guides/$guideFile"
								$masterContent += "### [$guideTitle]($adjustedPath)"
							}
							else {
								$masterContent += $line
							}
						}
						else {
							# Preserve empty lines
							$masterContent += $line
						}
					}
				}
				
				$masterContent += ""
			}
		}
		catch {
			Write-Warning "Could not process: $indexPath - $_"
		}
	}
}

# Write the master guides index
$masterIndexPath = Join-Path $docsPath "guides-list" "index.md"
$masterContent | Set-Content -Path $masterIndexPath -Encoding UTF8

Write-Host "  Generated master guides index with content from $($guidesDirectories.Count - 1) sub-directories"
Write-Host ""

Write-Host "Guide list generation complete!"
