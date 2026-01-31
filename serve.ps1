#!/usr/bin/env pwsh
# Helper PowerShell script to serve the Jekyll site on Windows.
$ErrorActionPreference = 'Stop'
if (Get-Command ruby -ErrorAction SilentlyContinue) {
  if (Test-Path Gemfile) {
    Write-Host "Installing gems (if needed)..."
    bundle install
  }
  Write-Host "Starting Jekyll (bundle exec jekyll serve --livereload)..."
  bundle exec jekyll serve --livereload
} elseif (Test-Path _site) {
  Write-Host "Ruby not found; serving existing _site with Python on port 4000"
  Push-Location _site
  python -m http.server 4000
  Pop-Location
} else {
  Write-Host "Ruby not found and _site missing. Install Ruby + Bundler, or build the site elsewhere."
  exit 1
}
