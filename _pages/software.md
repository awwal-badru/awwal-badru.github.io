---
title: "Software"
layout: gridlay
sitemap: false
permalink: /software/
---

<style>
img{
  border-radius: 10px;
}
iframe {
  width: 175px;
  display: inline;
  vertical-align:middle;
  <!-- margin-bottom:5px; -->
  <!-- margin-left:5px; -->
  <!-- border: 1px solid red; -->
}
.col-md-3 {
  margin:0;
  padding:0;
  margin-top:10px;
  margin-bottom:10px;
  display:block;
  overflow:hidden;
  text-align:center;
  display: table-cell;
  height: auto;
  float: none;
  background:white;
  border-radius:20px;
  <!-- border: 1px solid black; -->
}
</style>

<div class="jumbotron">
<div class="row align-items-end">
<div class="col-md-12 col-sm-12">
<h4><b>Sample Software Projects</b></h4>
<a href="https://adaptiveexperiments.github.io/" target="_blank"><button class="btn btn-success btn-sm">WEBSITE</button></a>
<a href="https://github.com" target="_blank"><button class="btn btn-info btn-sm">EMIS GIT</button></a>
<a href="https://github.com" target="_blank"><button class="btn btn-info btn-sm">ALP GIT</button></a>
<a href="{{ site.url }}{{ site.baseurl }}/papers/example_proceeding.pdf" target="_blank"><button class="btn btn-danger btn-sm">PAPER</button></a> 
</div>
</div>
</div>


### Adaptive Supplementary Materials — classroom platform (primary project)

A deployed system that uses contextual Thompson Sampling to deliver vetted, preference-aligned supplementary resources to students in real time. The system relies on live student ratings (no generative-AI content generation for core materials) and emphasizes transparency, instructor control, and lightweight, interpretable algorithms.

- Short summary: Real-time personalization of curated learning resources to improve engagement and perceived usefulness in software engineering courses.
- Role: Architect, implementer, classroom deployer, and data analyst.
- Tech stack: JavaScript frontend (React.js), Node.js backend, PostgreSQL, small Python/JS bandit module for contextual Thompson Sampling, CSV/JSON export for mixed-methods analysis.
- Key features:
  - Contextual Thompson Sampling for per-topic personalization
  - Instructor dashboard for curation and monitoring
  - Live student rating collection and analytics
  - Exportable data for qualitative and quantitative research
