---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

### Overview & Research Vision

My research explores how undergraduate software engineering (SE) students learn and how adaptive, evidence-based tools can support their learning across diverse classroom and project contexts. Modern software engineering curricula move rapidly, and static lectures or generic resources frequently leave students underserved when navigating complex technical concepts. I investigate how students interact with supplementary instructional materials, interpret conceptual explanations, and make decisions about self-directed study.

My overarching goal is to design, deploy, and evaluate human-centered learning systems that provide clearer guidance, accessible explanations, and personalized support—fostering deeper comprehension, student confidence, and self-efficacy in computing.

### Interdisciplinary Methodology

My work bridges **empirical software engineering**, **applied artificial intelligence**, and **human-centered computing**. Grounded in computing education research (CER), I employ rigorous mixed methods:

- **Controlled Classroom Experiments:** Measuring comprehension, engagement, and retention across alternative instructional interventions.
- **Behavioral & Interaction Analytics:** Analyzing how students navigate digital materials, where misconceptions arise, and how pacing affects outcomes.
- **Surveys & Qualitative Inquiries:** Capturing student perceptions, self-reported learning preferences, cognitive load, and preference dynamics.

### Core Systems & Pedagogical Platforms

A central component of my research is translating empirical insights into practical, instructor-friendly software tools:

- **ALP (Adaptive Learning Platform):** A lightweight adaptive platform that uses **contextual Thompson sampling** to personalize explanation selection in real time. Rather than relying on black-box generative models that risk hallucinations and algorithmic bias, ALP curates from vetted, high-quality material pools using live student feedback to match individual preferences, prior knowledge, and topic difficulty.
- **GenAI Pedagogical Analyzer:** An automated evaluation tool that evaluates learning materials across essential educational dimensions, including clarity, cognitive load, prerequisite alignment, and conceptual coherence. This system provides actionable diagnostics to help instructors refine materials and guide students more effectively.

### Empirical Validation & Key Findings

My research is validated through multi-institution classroom studies:

- **Adaptive Selection vs. Randomization:** Demonstrated that contextual multi-armed bandit algorithms significantly outperform static and randomized material delivery in student satisfaction and usefulness ratings.
- **Personalization Factors & Learning Dimensions:** Investigated how individual learner preferences, visual/verbal tendencies, and gender influence perceived material usefulness. Learner preferences emerged as the dominant predictor of usefulness (mediated by relevance, clarity, and worked examples), while strict visual/verbal mode-matching showed minimal effect, providing empirical nuance to contemporary learning-style debates.
- **Systematic Analysis of Material Design:** Surveyed and analyzed student navigation behaviors to establish concrete guidelines for authoring effective technical explanations and project scaffolds.

### Undergraduate Research Integration & Mentorship

I view research as a natural extension of undergraduate education. My projects provide accessible entry points for students at all levels to engage in meaningful, publishable research:

- **User Interface & Interaction Design:** Designing accessible, intuitive web interfaces and dashboards for educational platforms.
- **Algorithmic Evaluation:** Benchmarking recommendation and bandit algorithms with simulated and real classroom telemetry.
- **User Studies & Empirical Evaluation:** Involving students in protocol design, IRB preparation, data collection, usability testing, and qualitative analysis.
- **Applied System Development:** Mentoring undergraduates in full-stack engineering, cloud architecture, software engineering best practices, and open-source software development.

### 10-Year Strategic Research & Undergraduate Mentorship Roadmap

My long-term research vision follows a structured 10-year trajectory designed to scale from platform deployment to nationwide dissemination, with **undergraduate researchers actively involved at every stage**:

- **Years 1–2: Cloud-Based ALP Deployment & Dynamic Arms Expansion**
  - *Research Focus:* Architect and deploy a robust, cloud-hosted web version of the Adaptive Learning Platform (ALP). Deploy across multiple core computing courses and implement dynamic arms expansion to scale candidate supplementary materials beyond small subsets (accommodating more than 3 candidate resources per topic).
  - *Undergraduate Role:* Students contribute directly to full-stack web engineering, cloud infrastructure setup, API development, and candidate resource curation and benchmarking.

- **Years 2–3: Federated Learning Integration for Privacy-Preserving Personalization**
  - *Research Focus:* Integrate federated learning into the contextual Thompson sampling architecture. This enables multi-course and cross-departmental models to collaboratively learn student preference patterns without centralizing or exposing sensitive learner data.
  - *Undergraduate Role:* Students participate in distributed algorithm prototyping, local client simulation, data privacy evaluations, and benchmarking model convergence rates.

- **Years 4–5: Cross-Institutional Scaling & Multi-Campus Evaluation**
  - *Research Focus:* Scale ALP deployments to partner colleges and universities across diverse institutional contexts to test the generalizability of adaptive material recommendations across varied student cohorts.
  - *Undergraduate Role:* Students co-lead cross-institutional user studies, survey administration, usability testing, and multi-site telemetry data analysis.

- **Years 5–6: Longitudinal Learning & Trajectory Tracking**
  - *Research Focus:* Conduct multi-semester longitudinal tracking to investigate how adaptive supplementary support impacts long-term concept retention, project execution in upper-division courses, and career readiness.
  - *Undergraduate Role:* Students assist with cohort tracking, qualitative interview analysis, statistical modeling of long-term learning gains, and co-authoring conference manuscripts.

- **Years 7–10: Explainable AI (XAI) Integration & National Dissemination**
  - *Research Focus:* Once rich, multi-institutional datasets have accumulated sufficient data points at scale, integrate **Explainable AI (XAI)** models into ALP. XAI provides transparent, human-centered rationales for adaptive recommendations, helping students reflect metacognitively on their learning gaps and empowering instructors with clear diagnostic reasoning. Release a mature, modular open-source toolkit for nationwide adoption.
  - *Undergraduate Role:* Students lead algorithmic transparency evaluations, co-author peer-reviewed publications, present findings at premier venues (e.g., SIGCSE, ICSE/SEET, Learning@Scale), and build developer documentation for national distribution.

### Funding Strategy: External, Internal, and Undergraduate Support

To sustain this 10-year research agenda and support continuous undergraduate research involvement, I have established a multifaceted funding roadmap targeting federal agencies, professional computing societies, industry initiatives, and institutional programs:

#### 1. External Federal Grants (National Science Foundation — NSF)
- **NSF CRII (Computer and Information Science and Engineering Research Initiation Initiative):** Targeted in Years 1–3 to fund preliminary platform infrastructure, algorithmic validation of contextual bandits in computing education, and summer undergraduate research stipends.
- **NSF IUSE: Computing (Improving Undergraduate STEM Education):** Primary vehicle for Years 3–6 to fund cross-institutional scaling, pedagogical telemetry analysis, and rigorous curriculum integration of adaptive supplementary platforms.
- **NSF CAREER (Faculty Early Career Development Program):** A core long-term priority combining adaptive systems research (federated contextual bandits, explainable AI) with comprehensive undergraduate education and broadening participation in software engineering.
- **NSF REU (Research Experiences for Undergraduates) Supplements:** Integrated into all federal grant proposals to fund dedicated semester and summer stipends, housing, and conference travel for undergraduate student researchers.
- **NSF SaTC-EDU (Secure and Trustworthy Cyberspace Education):** Supporting the development of adaptive learning modules for software security, vulnerability auditing, and defensive coding in the AI era.

#### 2. Professional Societies & Industry Foundations
- **ACM SIGCSE Special Projects Grants:** Seed grants to pilot innovative instructional interventions and create open-access course materials for computing educators.
- **ACM & IEEE Student Travel Grants:** Enabling undergraduate student authors to travel, network, and present their peer-reviewed papers at premier venues (ACM SIGCSE, IEEE/ACM ICSE-SEET, Learning@Scale).
- **Industry Academic Research Awards (Google, Microsoft, Amazon AWS Educate):** Seeking cloud computing credits, digital education awards, and applied AI research grants to power large-scale ALP cloud infrastructure and hosting.

#### 3. Internal Institutional & Campus Funding
- **Faculty Startup & Seed Grants:** Leveraging initial departmental startup funds for server hosting, software licensing, lab workstations, and initial pilot data collection.
- **Campus Undergraduate Research & Creative Activity (URCA / UGR) Fellowships:** Tapping campus-wide competitive programs to provide competitive student research fellowships, summer research stipends, and academic-year credit.
- **Curricular Innovation & Teaching Improvement Grants:** Internal instructional grants to support redesigning foundational and upper-division software engineering courses to integrate adaptive learning technology.
- **Departmental Student Travel & Research Funds:** University matching funds to support undergraduate travel and registration for academic conference presentations.
