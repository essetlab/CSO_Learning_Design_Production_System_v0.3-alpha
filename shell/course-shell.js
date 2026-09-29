(() => {
  const host = document.querySelector('[data-cso-shell]');
  if (!host) return;

  const variant = host.dataset.variant || 'standard';
  const courseTitle = host.dataset.courseTitle || '';
  const courseContext = host.dataset.courseContext || '';
  const progressLabel = host.dataset.progressLabel || '';
  const progressPercent = Math.max(0, Math.min(100, Number(host.dataset.progressPercent || 0)));
  const drawerEyebrow = host.dataset.drawerEyebrow || '';
  const menuTemplate = document.querySelector('template[data-shell-menu]');
  const menuHTML = menuTemplate ? menuTemplate.innerHTML : '<a href="#main">Current learning</a>';

  const skip = document.createElement('a');
  skip.className = 'skip-link';
  skip.href = '#main';
  skip.textContent = host.dataset.skipLabel || 'Skip to learning content';

  host.innerHTML = `
    <header class="appbar ${variant === 'immersive' ? 'appbar--immersive' : ''}" aria-label="Course header">
      <div class="appbar__inner">
        <button class="icon-button" data-shell-menu-button type="button" aria-label="Menu" aria-expanded="false" aria-controls="courseMenu">
          <span aria-hidden="true" class="menu-icon">☰</span><span class="menu-label">Menu</span>
        </button>
        <div class="brand" aria-label="DEC CSO Learning Hub">
          <span class="brand__mark" aria-hidden="true">DEC</span><span class="brand__name">CSO Learning Hub</span>
        </div>
        <div class="course-context">
          <span class="course-context__title"></span><span class="course-context__module"></span>
        </div>
        <div class="course-progress" aria-label="${escapeHTML(progressLabel)}">
          <span class="course-progress__label"></span>
          <span class="course-progress__track" aria-hidden="true"><span></span></span>
        </div>
      </div>
    </header>
    <aside class="drawer" id="courseMenu" aria-hidden="true" aria-label="Course menu" inert>
      <div class="drawer__header">
        <div>${drawerEyebrow ? `<span class="drawer__eyebrow">${escapeHTML(drawerEyebrow)}</span>` : ''}<strong>Course tools</strong></div>
        <button class="icon-button icon-button--light" data-shell-close-button type="button">Close</button>
      </div>
      <nav aria-label="Course tools">${menuHTML}</nav>
    </aside>
    <div class="drawer-backdrop" data-shell-backdrop hidden></div>`;

  document.body.insertBefore(skip, document.body.firstChild);
  host.querySelector('.course-context__title').textContent = courseTitle;
  host.querySelector('.course-context__module').textContent = courseContext;
  host.querySelector('.course-progress__label').textContent = progressLabel;
  host.querySelector('.course-progress__track span').style.width = `${progressPercent}%`;

  const button = host.querySelector('[data-shell-menu-button]');
  const close = host.querySelector('[data-shell-close-button]');
  const drawer = host.querySelector('.drawer');
  const backdrop = host.querySelector('[data-shell-backdrop]');

  function setDrawer(open) {
    drawer.dataset.open = open ? 'true' : 'false';
    drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
    drawer.inert = !open;
    button.setAttribute('aria-expanded', open ? 'true' : 'false');
    backdrop.hidden = !open;
    if (open) close.focus(); else button.focus();
  }

  button.addEventListener('click', () => setDrawer(true));
  close.addEventListener('click', () => setDrawer(false));
  backdrop.addEventListener('click', () => setDrawer(false));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && drawer.dataset.open === 'true') setDrawer(false); });
  drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setDrawer(false)));

  const actionsHost = document.querySelector('[data-cso-learning-actions]');
  if (actionsHost) {
    document.body.dataset.shellActions = 'true';
    const previousLabel = actionsHost.dataset.previousLabel || 'Previous';
    const continueLabel = actionsHost.dataset.continueLabel || 'Continue';
    const statusText = actionsHost.dataset.status || '';
    actionsHost.innerHTML = `
      <footer class="learning-actions" aria-label="Learning navigation">
        <div class="learning-actions__inner">
          <button class="button button--secondary" type="button" data-action="previous">${escapeHTML(previousLabel)}</button>
          <span class="learning-actions__status" id="completionStatus">${escapeHTML(statusText)}</span>
          <button class="button button--primary" id="continueButton" data-action="continue" type="button" disabled>${escapeHTML(continueLabel)}</button>
        </div>
      </footer>`;
  }

  function escapeHTML(value) {
    return String(value).replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#039;','"':'&quot;'}[c]));
  }
})();
