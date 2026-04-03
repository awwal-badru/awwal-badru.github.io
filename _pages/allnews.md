---
title: "All News"
layout: gridlay
sitemap: false
permalink: /allnews.html
---

<div class="modern-sidebar-card">
  <h4 class="sidebar-heading"><i class="fa fa-newspaper-o mr-2"></i>News Archive</h4>

  <div class="news-list mt-4">
    {% for article in site.data.news %}
      <div class="news-item" style="cursor: default; background: rgba(158, 27, 50, 0.02)">
        <div class="news-date"><i class="fa fa-calendar mr-1"></i> {{ article.date }}</div>
        <div class="news-headline" style="font-size: 1rem; color: #333;">{{ article.headline }}</div>
      </div>
    {% endfor %}
  </div>
</div>
