---
title: "Talks"
layout: gridlay
sitemap: false
permalink: /talks/
---

<!-- Protected Candidate Presentations (Hidden by default; unlocked via passcode or secret access link) -->
<div id="private-talks-section" class="private-talks-container" style="display: none;" markdown="0">
  <div class="private-header">
    <div class="private-title-group">
      <span class="private-badge"><i class="fa fa-lock"></i> Protected</span>
      <h3 class="private-heading">Job Interview &amp; Teaching Demonstrations</h3>
    </div>
    <button class="lock-toggle-btn" onclick="lockPrivateSection()" title="Hide &amp; Lock Section">
      <i class="fa fa-lock"></i> Lock Section
    </button>
  </div>
  <p class="private-note">Confidential candidate presentations and teaching demonstrations.</p>

  <div class="interview-talk-card">
    <div class="talk-meta">
      <span class="talk-institution"><i class="fa fa-university mr-1"></i> Franklin College</span>
      <span class="talk-category">Teaching Demonstration</span>
    </div>
    <h4 class="talk-title">When Things Go Wrong: From Python If-Statements to Reliable Software Systems</h4>
    <p class="talk-desc">
      An interactive 23-slide pedagogical lecture designed for undergraduate computer science students. Bridges foundational conditional logic, structured exception handling (try-except blocks), and robust system reliability patterns.
    </p>
    <div class="talk-actions">
      <a href="{{ '/talks/franklin-teaching-demo/' | relative_url }}" target="_blank" class="talk-btn-primary">
        <i class="fa fa-play-circle mr-1"></i> Launch Interactive Presentation
      </a>
      <a href="{{ '/assets/files/Awwal_Badru_Teaching_Demo_FRA.pdf' | relative_url }}" target="_blank" class="talk-btn-secondary">
        <i class="fa fa-file-pdf-o mr-1"></i> Download PDF (23 Slides)
      </a>
    </div>
  </div>

  <!-- Drury University presentation will be added here upon slide upload -->
</div>

<!-- Public: Invited Talks -->
<div class="jumbotron" markdown="0">
  <h3><i class="fa fa-microphone mr-2"></i>Invited Talks</h3>
  
  <div style="background: rgba(158, 27, 50, 0.03); border: 1px solid rgba(158, 27, 50, 0.12); border-radius: 8px; padding: 1.25rem; margin-top: 1rem;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
      <div>
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.15rem; font-weight: 700;">Agentic Coding: LLM-Driven Software Engineering Workflows</h4>
        <div style="color: #666; font-size: 0.85rem; margin-bottom: 0.75rem;">Invited Guest Lecture / Technical Presentation</div>
      </div>
      <a href="{{ '/agentic-coding-talk/' | relative_url }}" target="_blank" class="btn btn-sm btn-crimson" style="background: var(--ua-crimson); color: #fff; border-radius: 20px; padding: 5px 14px; font-weight: 600; text-decoration: none;">
        <i class="fa fa-play-circle mr-1"></i> View Slides
      </a>
    </div>
    <p style="margin: 0; font-size: 0.9rem; color: #444; line-height: 1.5;">
      Exploration of agentic coding architectures, LLM-based autonomous software development workflows, interactive prompt loops, and modern toolchain orchestration.
    </p>
  </div>

  {% bibliography --query @incollection[keywords ^= invited] %}
</div>

<!-- Public: Regular Talks -->
<div class="jumbotron">
  <h3><i class="fa fa-bullhorn mr-2"></i>Regular &amp; Conference Talks</h3>
  {% bibliography --query @incollection[keywords != invited] %}
</div>

<!-- Discrete Unlock Trigger at Bottom of Page -->
<div class="discrete-lock-area" markdown="0">
  <button id="auth-toggle-icon" class="discrete-lock-btn" onclick="triggerPasscodeModal()" title="Private Access">
    <i class="fa fa-lock"></i>
  </button>
</div>

<!-- Passcode Modal -->
<div id="talks-passcode-modal" class="passcode-modal" style="display: none;" markdown="0">
  <div class="passcode-modal-content">
    <div class="modal-header-icon"><i class="fa fa-shield"></i></div>
    <h4>Private Presentations Access</h4>
    <p>Enter the passcode to view private candidate interview and teaching demo slides:</p>
    <div class="modal-input-row">
      <input type="password" id="modal-passcode-input" class="modal-input" placeholder="Passcode" maxlength="12" />
      <button class="modal-unlock-btn" onclick="submitModalPasscode()">Unlock</button>
    </div>
    <div id="modal-passcode-error" class="modal-error-msg" style="display: none;">
      <i class="fa fa-exclamation-circle"></i> Incorrect passcode. Try again.
    </div>
    <button class="modal-close-btn" onclick="closePasscodeModal()">Cancel</button>
  </div>
</div>

<script>
  const AUTH_HASH = "a325d2b1c02a0f957b78702a10d8cf29819c2bb6ed7202953015368b017c5f84";

  async function computeHash(str) {
    const buffer = new TextEncoder().encode(str);
    const digest = await crypto.subtle.digest('SHA-256', buffer);
    return Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
  }

  async function isUnlocked() {
    const params = new URLSearchParams(window.location.search);
    const key = params.get('auth') || params.get('key') || params.get('passcode');
    if (key) {
      const h = await computeHash(key);
      if (h === AUTH_HASH) {
        localStorage.setItem('talks_auth_hash', AUTH_HASH);
        return true;
      }
    }
    return localStorage.getItem('talks_auth_hash') === AUTH_HASH;
  }

  function showPrivateSection() {
    const section = document.getElementById('private-talks-section');
    if (section) {
      section.style.display = 'block';
      const icon = document.getElementById('auth-toggle-icon');
      if (icon) {
        icon.innerHTML = '<i class="fa fa-unlock-alt"></i>';
        icon.title = "Private presentations visible (Click to lock)";
        icon.style.opacity = '0.7';
        icon.style.color = 'var(--ua-crimson)';
      }
    }
  }

  function lockPrivateSection() {
    localStorage.removeItem('talks_auth_hash');
    localStorage.removeItem('talks_auth');
    const section = document.getElementById('private-talks-section');
    if (section) section.style.display = 'none';
    const icon = document.getElementById('auth-toggle-icon');
    if (icon) {
      icon.innerHTML = '<i class="fa fa-lock"></i>';
      icon.title = "Private Access";
      icon.style.opacity = '0.25';
      icon.style.color = '#888';
    }
  }

  async function triggerPasscodeModal() {
    if (await isUnlocked()) {
      lockPrivateSection();
    } else {
      const modal = document.getElementById('talks-passcode-modal');
      if (modal) {
        modal.style.display = 'flex';
        const input = document.getElementById('modal-passcode-input');
        if (input) {
          input.value = '';
          document.getElementById('modal-passcode-error').style.display = 'none';
          input.focus();
        }
      }
    }
  }

  async function submitModalPasscode() {
    const input = document.getElementById('modal-passcode-input');
    const val = input ? input.value.trim() : '';
    if (val) {
      const h = await computeHash(val);
      if (h === AUTH_HASH) {
        localStorage.setItem('talks_auth_hash', AUTH_HASH);
        closePasscodeModal();
        showPrivateSection();
        return;
      }
    }
    const err = document.getElementById('modal-passcode-error');
    if (err) err.style.display = 'block';
    if (input) {
      input.value = '';
      input.focus();
    }
  }

  function closePasscodeModal() {
    const modal = document.getElementById('talks-passcode-modal');
    if (modal) modal.style.display = 'none';
  }

  document.addEventListener('DOMContentLoaded', async function() {
    const input = document.getElementById('modal-passcode-input');
    if (input) {
      input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') submitModalPasscode();
      });
    }

    // Keyboard shortcut: Ctrl + Shift + U
    document.addEventListener('keydown', function(e) {
      if (e.ctrlKey && e.shiftKey && (e.key === 'U' || e.key === 'u')) {
        triggerPasscodeModal();
      }
    });

    if (await isUnlocked()) {
      showPrivateSection();
    }
  });
</script>
