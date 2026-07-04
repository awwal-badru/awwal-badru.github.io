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
<a href="https://mtcfs.netlify.app/" target="_blank" rel="noopener">
  <button class="btn btn-warning btn-sm">Cooperative Financial System</button>
</a>
<a href="https://github.com/awwal-badru/geolocation-alert" target="_blank" rel="noopener">
  <button class="btn btn-primary btn-sm">Eagle Geolocation Alert</button>
</a>
<a href="https://github.com/awwal-badru" target="_blank"><button class="btn btn-info btn-sm">GitHub Repos</button></a>
<a href="https://adaptiveexperiments.github.io" target="_blank"><button class="btn btn-info btn-sm">EASI Project</button></a>
<!-- <a href="{{ site.url }}{{ site.baseurl }}/papers/example_proceeding.pdf" target="_blank"><button class="btn btn-danger btn-sm">PAPER</button></a> -->
</div>
</div>
</div>


### Adaptive Supplementary Materials — classroom platform (primary project)

A deployed system that uses contextual Thompson Sampling to deliver vetted, preference-aligned supplementary resources to students in real time. The system relies on live student ratings (no generative-AI content generation for core materials) and emphasizes transparency, instructor control, and lightweight, interpretable algorithms.

- Short summary: Real-time personalization of curated learning resources to improve engagement and perceived usefulness in software engineering courses.
- Role: Researcher, Developer, Maintainer, Instructor, and Learning Science Analyst.
- Website:
  <a href="https://myalp.cs.ua.edu" target="_blank" rel="noopener noreferrer" class="btn btn-outline-success btn-sm" style="margin-right:.5rem">Participate in my Adaptive Learning Platofrm experiment</a>
  <span style="font-family:monospace; color:#333">https://myalp.cs.ua.edu</span>

- Tech stack: JavaScript frontend (React.js), Node.js backend, PostgreSQL, small Python/JS bandit module for contextual Thompson Sampling, CSV/JSON export for mixed-methods analysis.
- Key features:
  - Contextual Thompson Sampling for per-topic personalization
  - Instructor dashboard for curation and monitoring
  - Live student rating collection and analytics
  - Exportable data for qualitative and quantitative research


### Financial System for Cooperative Society

A web-based financial management system for cooperative societies to manage member accounts, transactions, savings, and loans.

- Short summary: Lightweight cooperative finance management with member accounting and reporting.
- Role: Developer / Maintainer.
- Website:
  <a href="https://mtcfs.netlify.app/" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm" style="margin-right:.5rem">View Financial System</a>
  <span style="font-family:monospace; color:#333">https://mtcfs.netlify.app/</span>

- Tech stack: MERN — MongoDB, Express, React, Node.js; Netlify-hosted frontend (client) and Node/Express backend with MongoDB (Atlas).
- Key features:
  - Member account management
  - Transaction logging and summaries


### Eagle — Geolocation Alert & Emergency Response System

A cross-platform mobile and web application designed to connect citizens in distress with nearby emergency response units (Police, Medical, Fire/FRSC, Amotekun) in real time. The platform features an event-driven serverless architecture, live GPS navigation, and localized spatial querying to ensure fast, reliable emergency routing.

- Short summary: Geolocation-based emergency alert and tracking system enabling citizens to broadcast one-touch SOS signals and responders to navigate to incidents in real time.
- Role: Developer / Maintainer.
- Website:
  <a href="https://github.com/awwal-badru/geolocation-alert" target="_blank" rel="noopener noreferrer" class="btn btn-outline-dark btn-sm" style="margin-right:.5rem">View GitHub Repository</a>
  <span style="font-family:monospace; color:#333">https://github.com/awwal-badru/geolocation-alert</span>

- Tech stack: Flutter & Dart (iOS, Android, Web), Riverpod (state management), Firebase (Auth, Cloud Firestore, Cloud Storage, Node.js Cloud Functions), Google Maps Platform (Maps SDK, Geocoding, Places, Directions), `geoflutterfire_plus` (geohash indexing), and an offline mock engine for developer testing.
- Key features:
  - One-touch SOS alerting with agency categories (Police, Medical, Fire, Crime, Accident).
  - Real-time location streaming and routing navigation for citizens and active emergency units.
  - Interactive web-based dispatcher command center console with active ticket tracking and responder map.
  - Spatial responder querying (e.g. searching within 5km radius) using Firestore-compatible geohashing.
  - Clean serverless backend validation using Firestore Security Rules and Firebase App Check.
  - Fully simulated offline mock mode enabling end-to-end flow execution without active API tokens.

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 1.5rem; margin-bottom: 1.5rem;">
<div style="flex: 1 1 280px; text-align: center;">
<p style="margin-bottom: 5px; font-weight: bold; color: #555;">Citizen SOS (Mobile)</p>
<img src="{{ site.url }}{{ site.baseurl }}/images/eagle_citizen_sos_mobile.png" alt="Citizen SOS Mobile View" style="max-width: 100%; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
</div>
<div style="flex: 1 1 280px; text-align: center;">
<p style="margin-bottom: 5px; font-weight: bold; color: #555;">Responder Portal (Mobile)</p>
<img src="{{ site.url }}{{ site.baseurl }}/images/eagle_responder_portal_mobile.png" alt="Responder Portal Mobile View" style="max-width: 100%; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
</div>
<div style="flex: 2 1 450px; text-align: center;">
<p style="margin-bottom: 5px; font-weight: bold; color: #555;">Dispatcher Command Center (Desktop)</p>
<img src="{{ site.url }}{{ site.baseurl }}/images/eagle_command_center_desktop.png" alt="Command Center Desktop View" style="max-width: 100%; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
</div>
</div>

