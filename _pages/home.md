---
title: "Home"
layout: homelay
sitemap: false
permalink: /
---

### Welcome

My research focuses on developing and evaluating personalized, adaptive delivery systems for supplementary learning materials to support diverse student knowledge levels and preferences in Software Engineering Education, a method termed the real time data-driven Adaptive Learning Platform.

#### Research focus
- Continuously assess student knowledge states and learning preferences.
- Select and adapt content (readings, videos, exercises) to maximize engagement and mastery.
- Provide timely feedback and scaffolding for underrepresented and novice learners.
- Integrate with software engineering curricula and tooling to measure real learning outcomes.

This work brings together machine learning, human–computer interaction, and education research to create equitable, data‑driven learning experiences that improve retention, confidence, and performance in software engineering courses.

<div class="container mt-4 mb-5" markdown="0">
  <div class="row justify-content-center">
    <div class="col-md-10">
      
      <div id="platformCarousel" class="carousel slide modern-carousel" data-bs-ride="carousel" data-bs-interval="15000">
        
        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li data-bs-target="#platformCarousel" data-bs-slide-to="0" class="active"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="1"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="2"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="3"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="4"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="5"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="6"></li>
          <li data-bs-target="#platformCarousel" data-bs-slide-to="7"></li>
        </ol>

        <!-- Wrapper for slides -->
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="slide-text-top">
              <h5>Step 1: Navigate to Registration & Consent</h5>
              <p>Navigate to the registration page and review the consent form details.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_0.png?v={{ site.time | date: '%s' }}" alt="Step 1: Registration & Consent">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Step 2: Accept Consent & Register</h5>
              <p>Click the "I Agree" button to navigate to the sign-up form and register your account.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_1.png?v={{ site.time | date: '%s' }}" alt="Step 2: Sign Up & Register">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Step 3: Secure Login</h5>
              <p>Log in using your credentials to securely access your learning workspace.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_2.png?v={{ site.time | date: '%s' }}" alt="Step 3: Secure Login">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Steps 4-5: Select Topics & Take Pre-Test</h5>
              <p>Select available course topics for your institution and take a Pre-Test to evaluate your initial understanding.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_3.png?v={{ site.time | date: '%s' }}" alt="Steps 4-5: Select Topics & Pre-Test">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Steps 6-7: Access Material & Learn</h5>
              <p>Access learning materials for the chosen topic. View supplementary material adaptively rendered based on prior data.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_4.png?v={{ site.time | date: '%s' }}" alt="Steps 6-7: Access Material & Learn">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Step 8: Complete Requirements</h5>
              <p>Read or watch the material to the end, rate its usefulness, take the post-test quiz, and review AI generated concepts.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_5.png?v={{ site.time | date: '%s' }}" alt="Step 8: Complete Requirements">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Concept Mapping & Review</h5>
              <p>Review the conceptual layout and map of your learning progress to reinforce core concepts.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_6.png?v={{ site.time | date: '%s' }}" alt="Concept Mapping & Review">
          </div>
          
          <div class="carousel-item">
            <div class="slide-text-top">
              <h5>Step 9: Monitor Performance</h5>
              <p>Use the personalized student dashboard to track your overall learning progress and scores.</p>
            </div>
            <img class="d-block placeholder-bg" src="{{ site.url }}{{ site.baseurl }}/images/extracted_main/page_7.png?v={{ site.time | date: '%s' }}" alt="Step 9: Monitor Performance">
          </div>
        </div>

        <!-- Controls -->
        <a class="carousel-control-prev custom-carousel-arrow" href="#platformCarousel" role="button" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next custom-carousel-arrow" href="#platformCarousel" role="button" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
      
      <div class="text-center mt-3 mb-5" style="color: #666; font-size: 0.95rem;">
        <em>Learning Platform Walkthrough</em><br/>
      </div>

      <div class="modern-sidebar-card mt-4" markdown="0">
        <h4 class="sidebar-heading"><i class="fa fa-newspaper-o mr-2"></i>Latest News</h4>
        {% include news-alert.html %}

        <div class="news-list mt-3">
          {% for article in site.data.news limit:3 %}
            <a href="{{ site.url }}{{ site.baseurl }}/allnews.html" class="news-item">
              <div class="news-date"><i class="fa fa-calendar mr-1"></i> {{ article.date }}</div>
              <div class="news-headline" title="{{ article.headline | escape }}">{{ article.headline }}</div>
            </a>
          {% endfor %}
        </div>

        <div class="text-center mt-4">
          <a href="{{ site.url }}{{ site.baseurl }}/allnews.html" class="news-see-all">View All News &rarr;</a>
        </div>
      </div>

    </div>
  </div>
</div>

