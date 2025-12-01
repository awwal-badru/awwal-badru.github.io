---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About

{% for member in site.data.pi %}

<div class="jumbotron">
<div class="row">
<div class="col-sm-4">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-8 col-xs-12">
  <h3>{{ member.name }}</h3>
  <h4><i>{{ member.info }}</i></h4>
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-3x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-3x"></i></a> {% endif %}

  <ul style="overflow: hidden">
    {% for education in member.education %}
      <li>{{ education | replace: "-","&#8211;" }}</li>
    {% endfor %}
  </ul>

</div>
</div>
</div>
{% endfor %}

{% if site.data.experience %}
<div class="about-section employment jumbotron">
  <h3>Employment History</h3>
  <ul class="employment-list">
    {% for e in site.data.experience %}
      <li class="employment-entry">
        <div class="entry-period">{{ e.period }}</div>
        <div class="entry-content">
          <div class="entry-title">{% if e.title %}{{ e.title }}{% endif %}{% if e.organization %}, <span class="entry-org">{{ e.organization }}</span>{% endif %}</div>
          {% if e.details and e.details.size > 0 %}
            <ul class="entry-details">
              {% for d in e.details %}
                <li>{{ d }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </div>
      </li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% comment %}
Teaching experience placed directly below Employment History
{% endcomment %}

{% if site.data.teaching_exp %}
<div class="about-section teaching jumbotron">
  <h3>Teaching Experience</h3>
  <ul class="teaching-list">
    {% for t in site.data.teaching_exp %}
      <li class="teaching-entry">
        <div class="teaching-period">{{ t.period }}</div>

        <div class="teaching-content">
          <div class="teaching-title">{{ t.title }}</div>
          {% if t.organization %}
            <div class="teaching-org">{{ t.organization }}</div>
          {% endif %}

          {% if t.courses and t.courses.size > 0 %}
            <ul class="teaching-courses" aria-label="Courses taught">
              {% for c in t.courses %}
                <li class="course">{{ c }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </div>
      </li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% if site.data.grants %}

<div class="jumbotron">
  <h3>Grants</h3>
  <ul>
    {% for grant in site.data.grants %}
      <li>{{ grant.name }}</li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% if site.data.awards %}
<div class="about-section awards jumbotron">
  <h3>Awards & Scholarships</h3>
  <ul class="awards-list">
    {% for item in site.data.awards %}
      <li class="award-entry">
        <div class="award-year">{{ item.year }}</div>
        <div class="award-body"><strong>{{ item.title }}</strong>{% if item.institution %}, {{ item.institution }}{% endif %}{% if item.value %} — {{ item.value }}{% endif %}</div>
      </li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% if site.data.people %}

<div class="jumbotron">
  <h3>Students and Mentoring</h3>
  <ul>
    {% for student in site.data.people %}
      <li>{{ student.name }}, {{ student.location }} ({{ student.degree }}, {{ student.year }})</li>
    {% endfor %}
  </ul>
</div>
{% endif %}

<div class="jumbotron">
  <h4>Sponsors</h4>
  <div style='display:block; text-align:center; margin-left:auto; margin-right:auto;'>
  {% for funder in site.data.funders %}<a href="{{ funder.url }}" target="_blank"><img src='{{ site.url }}{{ site.baseurl }}/images/{{ funder.image }}' style='max-height: 80px; max-width: 200px; margin: 1%'/></a>{% endfor %}
  </div>
</div>


