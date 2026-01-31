# Run site locally (Windows)

Quick steps to run this Jekyll site locally on Windows.

1) Install Ruby (recommended)

- Download and install Ruby from RubyInstaller: https://rubyinstaller.org/
- During install, enable the MSYS2 option and follow prompts to install the toolchain.

2) Open a command prompt (PowerShell or CMD) in the repository folder and run:

```powershell
gem install bundler
bundle install
bundle exec jekyll serve --livereload
```

3) Open your browser to http://127.0.0.1:4000

Alternative: if you don't want to install Ruby but have an existing static build
(the `_site` folder), you can serve `_site` with Python:

```powershell
cd _site
python -m http.server 4000
# then open http://127.0.0.1:4000
```

Helper scripts were added:

- `serve.ps1` — PowerShell helper that runs `bundle install` + `bundle exec jekyll serve`, or falls back to serving `_site` with Python.
- `serve.bat` — CMD helper with the same behavior.

If you prefer WSL, install Ruby/Jekyll there and run the same `bundle exec jekyll serve` command.
