(() => {
  const root = document.documentElement;
  const saved = localStorage.getItem('coral-theme');
  if (saved === 'dark' || saved === 'light') root.dataset.theme = saved;
  else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) root.dataset.theme = 'dark';

  function updateThemeLabel() {
    const btn = document.querySelector('[data-theme-toggle]');
    if (!btn) return;
    const dark = root.dataset.theme === 'dark';
    btn.textContent = dark ? 'Tema claro' : 'Tema escuro';
    btn.setAttribute('aria-label', dark ? 'Usar tema claro' : 'Usar tema escuro');
  }
  updateThemeLabel();

  document.addEventListener('click', (event) => {
    const themeBtn = event.target.closest('[data-theme-toggle]');
    if (themeBtn) {
      const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      localStorage.setItem('coral-theme', next);
      updateThemeLabel();
    }

    const menuBtn = event.target.closest('[data-menu-toggle]');
    if (menuBtn) {
      const targetId = menuBtn.getAttribute('aria-controls');
      const target = document.getElementById(targetId);
      if (target) {
        const open = target.classList.toggle('open');
        menuBtn.setAttribute('aria-expanded', String(open));
      }
    }

    const docsBtn = event.target.closest('[data-docs-menu-toggle]');
    if (docsBtn) toggleDocsMenu();

    if (event.target.matches('.docs-backdrop')) toggleDocsMenu(false);
  });

  function toggleDocsMenu(force) {
    const sidebar = document.querySelector('.docs-sidebar');
    const backdrop = document.querySelector('.docs-backdrop');
    const btn = document.querySelector('[data-docs-menu-toggle]');
    if (!sidebar || !backdrop) return;
    const shouldOpen = typeof force === 'boolean' ? force : !sidebar.classList.contains('open');
    sidebar.classList.toggle('open', shouldOpen);
    backdrop.classList.toggle('open', shouldOpen);
    document.body.classList.toggle('menu-open', shouldOpen);
    if (btn) btn.setAttribute('aria-expanded', String(shouldOpen));
  }

  document.querySelectorAll('.docs-sidebar a').forEach(a => a.addEventListener('click', () => toggleDocsMenu(false)));

  const tocLinks = [...document.querySelectorAll('[data-toc-link]')];
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const sections = tocLinks.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(e => e.isIntersecting).sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      tocLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === '#' + visible.target.id));
    }, { rootMargin: '-18% 0px -70% 0px' });
    sections.forEach(section => observer.observe(section));
  }

  const search = document.querySelector('[data-doc-search]');
  const status = document.querySelector('[data-search-status]');
  if (search) {
    const searchable = [...document.querySelectorAll('[data-searchable]')];
    const originals = new Map(searchable.map(el => [el, el.innerHTML]));
    const escapeRegExp = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const reset = () => searchable.forEach(el => { el.innerHTML = originals.get(el); el.closest('.docs-section')?.removeAttribute('data-search-match'); });

    search.addEventListener('input', () => {
      reset();
      const q = search.value.trim();
      if (!q) {
        if (status) status.textContent = '';
        return;
      }
      let count = 0;
      const re = new RegExp(escapeRegExp(q), 'gi');
      searchable.forEach(el => {
        const text = el.textContent || '';
        if (!re.test(text)) return;
        re.lastIndex = 0;
        const section = el.closest('.docs-section');
        if (section) section.dataset.searchMatch = 'true';
        const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach(node => {
          if (!node.nodeValue || !re.test(node.nodeValue)) { re.lastIndex = 0; return; }
          re.lastIndex = 0;
          const frag = document.createDocumentFragment();
          let last = 0;
          node.nodeValue.replace(re, (match, offset) => {
            frag.append(node.nodeValue.slice(last, offset));
            const mark = document.createElement('mark');
            mark.className = 'search-hit';
            mark.textContent = match;
            frag.append(mark);
            last = offset + match.length;
            count++;
            return match;
          });
          frag.append(node.nodeValue.slice(last));
          node.parentNode.replaceChild(frag, node);
        });
      });
      if (status) status.textContent = count ? `${count} ocorrência${count === 1 ? '' : 's'} encontrada${count === 1 ? '' : 's'}.` : 'Nenhuma ocorrência encontrada.';
    });
  }
})();
