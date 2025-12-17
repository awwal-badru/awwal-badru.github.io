---
title: "Software"
layout: gridlay
sitemap: false
permalink: /software/
---

<style>
img{ border-radius: 10px; }

/* keep iframe and column rules */
iframe { width: 175px; display: inline; vertical-align: middle; }
.col-md-3 { margin:0; padding:0; margin-top:10px; margin-bottom:10px; display:block; overflow:hidden; text-align:center; display: table-cell; height: auto; float: none; background:white; border-radius:20px; }

/* UA crimson before hover, keep green on hover */
.btn-success.custom-crimson {
  background-color: #9E1B32; /* UA crimson */
  border-color: #9E1B32;
  color: #fff;
}
.btn-success.custom-crimson:hover,
.btn-success.custom-crimson:focus,
.btn-success.custom-crimson:active {
  background-color: #198754 !important; /* retain Bootstrap success green on hover */
  border-color: #198754 !important;
  color: #fff !important;
}
</style>

<div class="jumbotron">
<div class="row align-items-end">
<div class="col-md-12 col-sm-12">
<h4><b>Software Projects</b></h4>
<a href="https://myalp.cs.ua.edu" target="_blank" rel="noopener">
  <button class="btn btn-success btn-sm custom-crimson">Learning Hub</button>
</a>
<a href="https://github.com/awwal-badru" target="_blank"><button class="btn btn-info btn-sm">GitHub Repos</button></a>
<a href="https://adaptiveexperiments.github.io" target="_blank"><button class="btn btn-info btn-sm">EASI Project</button></a>
<a href="{{ site.url }}{{ site.baseurl }}/papers/example_proceeding.pdf" target="_blank"><button class="btn btn-danger btn-sm">PAPER</button></a> 
</div>
</div>
</div>


### Adaptive Supplementary Materials — classroom platform (primary project)

A deployed system that uses contextual Thompson Sampling to deliver vetted, preference-aligned supplementary resources to students in real time. The system relies on live student ratings (no generative-AI content generation for core materials) and emphasizes transparency, instructor control, and lightweight, interpretable algorithms.

- Short summary: Real-time personalization of curated learning resources to improve engagement and perceived usefulness in software engineering courses.
- Role: Students, Researcher, Instructor, and Learning Science Analyst.
- Website:
  <a href="https://myalp.cs.ua.edu" target="_blank" rel="noopener noreferrer" class="btn btn-outline-success btn-sm" style="margin-right:.5rem">Participate in my Adaptive Learning Platofrm experiment</a>
  <span style="font-family:monospace; color:#333">https://myalp.cs.ua.edu</span>

- Tech stack: JavaScript frontend (React.js), Node.js backend, PostgreSQL, small Python/JS bandit module for contextual Thompson Sampling, CSV/JSON export for mixed-methods analysis.
- Key features:
  - Contextual Thompson Sampling for per-topic personalization
  - Instructor dashboard for curation and monitoring
  - Live student rating collection and analytics
  - Exportable data for qualitative and quantitative research
