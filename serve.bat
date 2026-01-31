@echo off
REM Helper batch script to serve the Jekyll site on Windows ( CMD )
ruby -v >nul 2>&1
if %errorlevel%==0 (
  if exist Gemfile (
    echo Installing gems (if needed)...
    bundle install
  )
  echo Starting Jekyll (bundle exec jekyll serve --livereload)...
  bundle exec jekyll serve --livereload
) else (
  if exist _site (
    echo Ruby not found; serving existing _site with Python on port 4000
    pushd _site
    python -m http.server 4000
    popd
  ) else (
    echo Ruby not found and _site missing. Install Ruby + Bundler or build the site elsewhere.
    exit /b 1
  )
)
