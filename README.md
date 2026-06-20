# Awwal Badru — Personal Academic Website

Welcome to the repository for my personal academic portfolio and CV website. I am a Ph.D. Candidate in Computer Science at the University of Alabama.

🔗 **Live Website:** [awwal-badru.github.io](https://awwal-badru.github.io)

---

## 🚀 About the Site

This website is statically generated using **Jekyll**, **Liquid**, and **Sass** (Bootstrap), featuring modern styling, robust accessibility, unified typography, and clean layouts.

### Key Features
- **Responsive Layout**: Designed to work seamlessly across mobile, tablet, and desktop screens.
- **Dynamic Dark/Light Themes**: Supports a global system-matched or user-toggled dark/light mode with high-contrast readable color schemes.
- **Secure Online CV Viewer**: Implements a canvas-based dynamic PDF viewer under a masked route `/cv/` utilizing **PDF.js**, which blocks right-clicks, print/save shortcuts, and browser PDF download bars.
- **Jekyll Scholar Bibliography**: Publication listings, citations, and talks are dynamically generated from a BibTeX repository (`assets/ref.bib`).

---

## 🛠️ Local Development

For quick local setup and running on Windows, follow these commands. For more detailed instructions on toolchain dependencies, see [RUN_LOCALLY.md](RUN_LOCALLY.md).

1. Install dependencies:
   ```powershell
   gem install bundler
   bundle install
   ```

2. Spin up the local development server:
   ```powershell
   bundle exec jekyll serve --livereload
   ```

3. Open your browser and navigate to:
   [http://127.0.0.1:4000](http://127.0.0.1:4000)

---

## 📂 Project Structure

- `_data/`: Contains YAML database entries for website content (experiences, teaching, awards, etc.).
  - `pi.yml`: Personal info, social links, and target CV file location.
- `_pages/`: Markdown and HTML pages representing site navigation.
  - `cv.html`: Custom secure PDF viewer.
  - `about.md`, `publications.md`, `talks.md`, `research.md`, `software.md`, `teaching.md`, `blogs.md`: Core website pages.
- `assets/`: Contains assets such as custom stylesheets (`main.scss`), reference BibTeX records (`ref.bib`), and source files (PDFs, images).
- `_layouts/` & `_includes/`: HTML templates and modular components (header, head, sidebar, footer) reused across pages.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
