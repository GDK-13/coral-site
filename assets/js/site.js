(() => {
  const root = document.documentElement;
  const siteRoot = root.dataset.siteRoot || '';
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

  // ---------- Helpers compartilhados ----------
  const ESCAPE_MAP = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
  const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (c) => ESCAPE_MAP[c]);
  const normalizeText = (value) => String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const escapeRegExp = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const isWordChar = (c) => /[a-z0-9_]/.test(c);

  async function loadJson(path) {
    // Em file:// o fetch não é suportado (e poluiria o console com erros);
    // os valores embutidos no HTML cobrem esse contexto.
    if (location.protocol === 'file:') throw new Error('fetch indisponível em file://');
    const response = await fetch(path, { cache: 'no-store' });
    if (!response.ok) throw new Error(`${response.status} ${path}`);
    return response.json();
  }

  // Copiar com fallback para contextos sem navigator.clipboard (ex.: file://).
  async function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      try {
        await navigator.clipboard.writeText(text);
        return true;
      } catch (_) { /* segue para o fallback */ }
    }
    try {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:-1000px;opacity:0';
      document.body.append(ta);
      ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      return ok;
    } catch (_) {
      return false;
    }
  }

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

  function toggleTocPanel(force) {
    const toc = document.querySelector('.toc');
    const fab = document.querySelector('[data-toc-toggle]');
    if (!toc || !fab) return;
    const shouldOpen = typeof force === 'boolean' ? force : !toc.classList.contains('open');
    toc.classList.toggle('open', shouldOpen);
    fab.setAttribute('aria-expanded', String(shouldOpen));
    if (shouldOpen) toc.querySelector('a')?.focus({ preventScroll: true });
  }

  // Botão copiar em blocos de código (melhoria progressiva).
  function setupCopyButtons() {
    document.querySelectorAll('.code-card').forEach((card) => {
      if (card.querySelector('.code-copy-btn')) return;
      const code = card.querySelector('code');
      if (!code) return;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'code-copy-btn';
      btn.textContent = 'Copiar';
      btn.setAttribute('aria-label', 'Copiar código do bloco');
      btn.addEventListener('click', async () => {
        const ok = await copyText(code.innerText);
        btn.textContent = ok ? 'Copiado' : 'Não foi possível copiar';
        btn.classList.toggle('copied', ok);
        setTimeout(() => {
          btn.textContent = 'Copiar';
          btn.classList.remove('copied');
        }, 2000);
      });
      card.append(btn);
    });
  }
  setupCopyButtons();

  // ---------- Âncoras copiáveis nos títulos de seção ----------
  // Adicionadas antes do snapshot da busca local para que o reset de destaques
  // não as remova; o clique é tratado por delegação por causa do reset de innerHTML.
  function setupHeadingAnchors() {
    document.querySelectorAll('.docs-main h2[id], .docs-main h3[id]').forEach((h) => {
      const label = h.textContent.trim();
      const anchor = document.createElement('a');
      anchor.className = 'heading-anchor';
      anchor.href = '#' + h.id;
      anchor.setAttribute('aria-label', 'Copiar link para a seção ' + label);
      anchor.append(document.createTextNode('#'));
      const tip = document.createElement('span');
      tip.className = 'heading-anchor-tip';
      tip.textContent = 'Link copiado';
      anchor.append(tip);
      h.append(anchor);
    });
  }
  setupHeadingAnchors();

  // Oculta o botão de TOC quando a página não tem subseções.
  const tocFab = document.querySelector('[data-toc-toggle]');
  if (tocFab && document.querySelector('.toc .toc-empty')) {
    tocFab.setAttribute('aria-hidden', 'true');
  }

  // ---------- Cards da Referência da API ----------
  // Cada função/ classe na seção "Referência da API" começa com um
  // <h4> contendo apenas um <code> (nome da função) e termina no
  // <details class="api-tech-details"> seguinte. Embrulhamos esse
  // intervalo em <section class="api-fn-card"> para que o CSS possa
  // aplicar borda, padding e o rodapé "Detalhes técnicos" colado.
  // Melhoria progressiva: se o JS não rodar, o conteúdo permanece
  // legível como texto corrido.
  (function wrapApiFunctionCards() {
    const article = document.querySelector('.docs-main .docs-section');
    if (!article) return;
    // Só atua em <h4> cujo único conteúdo é um <code> — evita capturar
    // h4s da sidebar/TOC (que não estão em .docs-main).
    const fnHeaders = Array.from(article.querySelectorAll('h4')).filter((h) => {
      // Critério: tem exatamente um filho <code> e nenhum texto direto relevante.
      const code = h4OnlyCode(h);
      return Boolean(code);
    });
    if (!fnHeaders.length) return;

    fnHeaders.forEach((h4) => {
      // Coleta todos os irmãos seguintes até o próximo h4 (ou h1/h2/h3, ou fim).
      const siblings = [];
      let node = h4.nextElementSibling;
      while (node && !/^(H1|H2|H3|H4)$/.test(node.tagName)) {
        siblings.push(node);
        node = node.nextElementSibling;
      }
      const card = document.createElement('section');
      card.className = 'api-fn-card';
      // Preserva âncora: move o id do h4 para o card para que #hash continue funcionando.
      if (h4.id) {
        card.id = h4.id;
        h4.removeAttribute('id');
        card.setAttribute('data-api-anchor', '');
      }
      h4.parentNode.insertBefore(card, h4);
      card.appendChild(h4);
      siblings.forEach((s) => card.appendChild(s));
    });
  })();

  function h4OnlyCode(h4) {
    // Retorna o <code> se for o único conteúdo do h4; caso contrário, null.
    const children = Array.from(h4.childNodes).filter((n) => {
      if (n.nodeType === Node.TEXT_NODE) return n.nodeValue.trim().length > 0;
      return true;
    });
    if (children.length !== 1) return null;
    const only = children[0];
    return only.tagName === 'CODE' ? only : null;
  }

  document.addEventListener('click', async (event) => {
    const headingAnchor = event.target.closest('.heading-anchor');
    if (headingAnchor) {
      event.preventDefault();
      const id = headingAnchor.getAttribute('href').slice(1);
      const ok = await copyText(location.href.split('#')[0] + '#' + id);
      headingAnchor.classList.toggle('copied', ok);
      const tip = headingAnchor.querySelector('.heading-anchor-tip');
      if (tip) tip.textContent = ok ? 'Link copiado' : 'Falha ao copiar';
      setTimeout(() => headingAnchor.classList.remove('copied'), 1800);
      return;
    }

    const themeBtn = event.target.closest('[data-theme-toggle]');
    if (themeBtn) {
      const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      localStorage.setItem('coral-theme', next);
      updateThemeLabel();
    }

    const menuBtn = event.target.closest('[data-menu-toggle]');
    if (menuBtn) {
      const target = document.getElementById(menuBtn.getAttribute('aria-controls'));
      if (target) {
        const open = target.classList.toggle('open');
        menuBtn.setAttribute('aria-expanded', String(open));
      }
    }

    if (event.target.closest('[data-docs-menu-toggle]')) toggleDocsMenu();
    if (event.target.closest('[data-toc-toggle]')) toggleTocPanel();
    if (event.target.matches('.docs-backdrop')) toggleDocsMenu(false);
  });

  document.querySelectorAll('.docs-sidebar a').forEach((a) => a.addEventListener('click', () => toggleDocsMenu(false)));
  document.querySelectorAll('.toc a[data-toc-link]').forEach((a) => a.addEventListener('click', () => toggleTocPanel(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      toggleTocPanel(false);
      toggleDocsMenu(false);
    }
  });

  const tocLinks = [...document.querySelectorAll('[data-toc-link]')];
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const sections = tocLinks.map((link) => document.querySelector(link.getAttribute('href'))).filter(Boolean);
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      tocLinks.forEach((link) => link.classList.toggle('active', link.getAttribute('href') === '#' + visible.target.id));
    }, { rootMargin: '-18% 0px -70% 0px' });
    sections.forEach((section) => observer.observe(section));
  }

  // ============================================================
  // BUSCA CORAL — paleta global com motor de pontuação próprio.
  //
  // Índice estático gerado pelo renderizador e carregado via
  // <script defer> (docs/dados/indice_busca.js): funciona em http(s)
  // e também em file://, onde fetch() falharia por política CORS.
  //
  // Recursos: multi-termo (AND com fallback OR), tolerância a erros
  // de digitação (subsequência com janela limitada), variantes leves
  // de plural pt-BR, ranking por campo (título > seção > texto),
  // "você quis dizer", recentes, destaques locais sem acentos.
  // ============================================================
  const INDICE = (window.CORAL_INDICE_BUSCA && Array.isArray(window.CORAL_INDICE_BUSCA.paginas))
    ? window.CORAL_INDICE_BUSCA.paginas : [];
  const searchStatusEl = document.querySelector('[data-search-status]');
  const RECENTES_KEY = 'coral-recentes';
  const MAX_RESULTS = 24;
  const MAX_PER_PAGE = 3;

  // Normaliza removendo acentos mantendo um mapa de índices normalizados -> originais.
  function normWithMap(text) {
    let norm = '';
    const map = [];
    for (let i = 0; i < text.length; i += 1) {
      const decomposed = text[i].normalize('NFD');
      for (let j = 0; j < decomposed.length; j += 1) {
        const part = decomposed[j];
        if (part >= '\u0300' && part <= '\u036f') continue;
        norm += part;
        map.push(i);
      }
    }
    return { norm: norm.toLowerCase(), map };
  }

  const pageNormCache = new WeakMap();
  const sectionNormCache = new WeakMap();

  function pageNorms(page) {
    let cached = pageNormCache.get(page);
    if (!cached) {
      cached = {
        titulo: normWithMap(page.titulo || ''),
        apelido: normWithMap(page.apelido || ''),
        descricao: normWithMap(page.descricao || ''),
      };
      pageNormCache.set(page, cached);
    }
    return cached;
  }

  function sectionNorms(sec) {
    let cached = sectionNormCache.get(sec);
    if (!cached) {
      cached = { titulo: normWithMap(sec.titulo || ''), texto: normWithMap(sec.texto || '') };
      sectionNormCache.set(sec, cached);
    }
    return cached;
  }

  function isCurrentPage(page) {
    return location.pathname.endsWith('/docs/' + page.url);
  }

  function splitTerms(raw) {
    const parts = normalizeText(String(raw || '')).split(/[^a-z0-9_]+/).filter(Boolean);
    const terms = parts.filter((p) => p.length >= 2);
    return [...new Set(terms)];
  }

  // Variantes leves de plural pt-BR: ampliam o recall ("listas" <-> "lista",
  // "funcoes" <-> "funcao", "itens" <-> "item") com penalidade pequena.
  function termVariants(term) {
    const out = [term];
    if (term.length >= 5) {
      if (term.endsWith('s')) out.push(term.slice(0, -1));
      if (term.endsWith('es')) out.push(term.slice(0, -2));
      if (term.endsWith('ns')) out.push(term.slice(0, -2) + 'm');
      if (term.endsWith('oes')) out.push(term.slice(0, -3) + 'ao');
    }
    return [...new Set(out)];
  }

  function findVariant(norm, variant) {
    const pos = norm.indexOf(variant);
    if (pos < 0) return null;
    const before = pos > 0 ? norm[pos - 1] : '';
    const after = pos + variant.length < norm.length ? norm[pos + variant.length] : '';
    return { pos, wordStart: !isWordChar(before), wordEnd: !isWordChar(after) };
  }

  // Subsequência com janela limitada: tolera erros de digitação
  // ("matrz" encontra "matriz", "funca" encontra "funcao").
  function fuzzyFind(norm, term) {
    if (term.length < 3 || norm.length < term.length) return null;
    const win = term.length + 2 + Math.floor(term.length / 3);
    let best = null;
    for (let start = 0; start + term.length <= norm.length; start += 1) {
      if (norm[start] !== term[0]) continue;
      let ti = 1;
      let run = 1;
      let last = start;
      const limit = Math.min(norm.length, start + win);
      for (let j = start + 1; j < limit && ti < term.length; j += 1) {
        if (norm[j] !== term[ti]) continue;
        run = (j === last + 1) ? run + 1 : 1;
        last = j;
        ti += 1;
      }
      if (ti < term.length) continue;
      const span = last - start + 1;
      if (!best || span < best.span) best = { pos: start, span };
      if (best.span === term.length) break;
    }
    return best;
  }

  // Pesos por campo: título da página > apelido (coral.x) > título da seção > descrição > texto.
  const FIELD_WEIGHTS = {
    pageTitle: { exact: 70, word: 52, substr: 34, fuzzy: 16 },
    apelido: { exact: 64, word: 47, substr: 30, fuzzy: 14 },
    secTitle: { exact: 56, word: 42, substr: 25, fuzzy: 12 },
    descricao: { exact: 34, word: 24, substr: 12, fuzzy: 0 },
  };

  function scoreField(normStr, variants, weights) {
    if (!normStr) return { score: 0, wordHit: false };
    let best = 0;
    let wordHit = false;
    for (let vi = 0; vi < variants.length; vi += 1) {
      const f = findVariant(normStr, variants[vi]);
      if (!f) continue;
      const base = (f.wordStart && f.wordEnd) ? weights.exact : (f.wordStart ? weights.word : weights.substr);
      const s = base * (vi ? 0.88 : 1);
      if (s > best) best = s;
      if (f.wordStart) wordHit = true;
    }
    if (!best && weights.fuzzy) {
      const fz = fuzzyFind(normStr, variants[0]);
      if (fz) best = weights.fuzzy;
    }
    return { score: best, wordHit };
  }

  // Pontua um termo contra todos os campos de uma (página, seção).
  function scoreTerm(term, page, sec) {
    const variants = termVariants(term);
    const pn = pageNorms(page);
    const sn = sec ? sectionNorms(sec) : null;
    const titleFields = [
      scoreField(pn.titulo.norm, variants, FIELD_WEIGHTS.pageTitle),
      scoreField(pn.apelido.norm, variants, FIELD_WEIGHTS.apelido),
      sn ? scoreField(sn.titulo.norm, variants, FIELD_WEIGHTS.secTitle) : null,
      scoreField(pn.descricao.norm, variants, FIELD_WEIGHTS.descricao),
    ].filter(Boolean);
    let titleScore = 0;
    let titleHit = false;
    titleFields.forEach((f) => {
      if (f.score > titleScore) titleScore = f.score;
      if (f.wordHit) titleHit = true;
    });

    let textScore = 0;
    let textPos = -1;
    if (sn && sn.texto.norm) {
      for (let vi = 0; vi < variants.length; vi += 1) {
        const v = variants[vi];
        const first = sn.texto.norm.indexOf(v);
        if (first < 0) continue;
        let c = 0;
        let idx = first;
        while (idx >= 0 && c < 6) {
          c += 1;
          idx = sn.texto.norm.indexOf(v, idx + v.length);
        }
        const wordStart = first === 0 || !isWordChar(sn.texto.norm[first - 1]);
        const s = ((wordStart ? 12 : 7) + Math.min(c - 1, 4) * 1.5) * (vi ? 0.88 : 1);
        if (s > textScore) { textScore = s; textPos = first; }
      }
      if (!textScore) {
        const fz = fuzzyFind(sn.texto.norm, term);
        if (fz) { textScore = 3; textPos = fz.pos; }
      }
    }
    return { score: Math.max(titleScore, textScore), titleHit, textPos };
  }

  // Executa a busca completa. Multi-termo com semântica AND; se nada casar,
  // cai para OR (resultados parciais) em vez de deixar o usuário sem nada.
  function findGlobalResults(rawQuery) {
    const terms = splitTerms(rawQuery);
    if (!terms.length) return null;
    const andResults = [];
    const orResults = [];

    INDICE.forEach((page) => {
      const sections = page.secoes || [];
      let pageHasAnd = false;

      sections.forEach((sec, si) => {
        let total = 0;
        let matched = 0;
        let bestPos = -1;
        terms.forEach((t) => {
          const r = scoreTerm(t, page, sec);
          if (r.score <= 0) return;
          total += r.score;
          matched += 1;
          if (r.textPos >= 0 && (bestPos < 0 || r.textPos < bestPos)) bestPos = r.textPos;
        });
        if (!matched) return;
        const entry = { page, sec, si, score: total, pos: bestPos, matched };
        if (matched === terms.length) { andResults.push(entry); pageHasAnd = true; }
        else orResults.push(entry);
      });

      // Resultado em nível de página (sem âncora de seção).
      if (!pageHasAnd) {
        let total = 0;
        let matched = 0;
        terms.forEach((t) => {
          const r = scoreTerm(t, page, null);
          if (r.score <= 0) return;
          total += r.score;
          matched += 1;
        });
        if (matched === terms.length) andResults.push({ page, sec: null, si: -1, score: total + 6, pos: -1, matched });
        else if (matched) orResults.push({ page, sec: null, si: -1, score: total + 4, pos: -1, matched });
      }
    });

    const partial = andResults.length === 0 && orResults.length > 0;
    const pool = partial ? orResults : andResults;
    pool.forEach((r) => { if (isCurrentPage(r.page)) r.score += 8; });

    // Máximo de seções por página evita que um módulo sozinho inunde os resultados.
    const byPage = new Map();
    pool.forEach((r) => {
      if (!byPage.has(r.page)) byPage.set(r.page, []);
      byPage.get(r.page).push(r);
    });
    let flat = [];
    byPage.forEach((arr) => {
      arr.sort((a, b) => b.score - a.score || a.si - b.si);
      flat = flat.concat(arr.slice(0, MAX_PER_PAGE));
    });
    flat.sort((a, b) => b.score - a.score || a.page.ordem - b.page.ordem || a.si - b.si);
    return { terms, results: flat.slice(0, MAX_RESULTS), total: pool.length, pages: byPage.size, partial };
  }

  // ---------- "Você quis dizer" ----------
  let vocabCache = null;
  function getVocab() {
    if (vocabCache) return vocabCache;
    const vocab = new Set();
    const addWords = (s) => {
      normalizeText(String(s || '')).split(/[^a-z0-9_]+/).forEach((w) => {
        if (w.length >= 4 && w.length <= 18) vocab.add(w);
      });
    };
    INDICE.forEach((p) => {
      addWords(p.titulo);
      addWords(p.apelido);
      addWords(p.descricao);
      (p.secoes || []).forEach((s) => addWords(s.titulo));
    });
    vocabCache = vocab;
    return vocab;
  }

  function levenshtein(a, b, max) {
    if (Math.abs(a.length - b.length) > max) return max + 1;
    let prev = new Array(b.length + 1);
    let cur = new Array(b.length + 1);
    for (let j = 0; j <= b.length; j += 1) prev[j] = j;
    for (let i = 1; i <= a.length; i += 1) {
      cur[0] = i;
      let rowMin = cur[0];
      for (let j = 1; j <= b.length; j += 1) {
        const cost = a[i - 1] === b[j - 1] ? 0 : 1;
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
        rowMin = Math.min(rowMin, cur[j]);
      }
      if (rowMin > max) return max + 1;
      const tmp = prev; prev = cur; cur = tmp;
    }
    return prev[b.length];
  }

  function didYouMean(term) {
    const vocab = getVocab();
    if (!vocab.size || vocab.has(term)) return null;
    let best = null;
    let bestD = 3;
    vocab.forEach((w) => {
      if (Math.abs(w.length - term.length) > 2) return;
      const d = levenshtein(term, w, 2);
      if (d < bestD) { bestD = d; best = w; }
    });
    return best;
  }

  // ---------- Destaque de ocorrências (títulos e snippets) ----------
  function markString(str, terms) {
    if (!str) return '';
    const { norm, map } = normWithMap(str);
    const variants = terms.flatMap(termVariants);
    const ranges = [];
    variants.forEach((v) => {
      let idx = norm.indexOf(v);
      while (idx >= 0) {
        if (idx === 0 || !isWordChar(norm[idx - 1])) ranges.push([idx, idx + v.length]);
        idx = norm.indexOf(v, idx + 1);
      }
    });
    if (!ranges.length) return escapeHtml(str);
    ranges.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
    const merged = [];
    ranges.forEach((r) => {
      const last = merged[merged.length - 1];
      if (last && r[0] < last[1]) last[1] = Math.max(last[1], r[1]);
      else merged.push([r[0], r[1]]);
    });
    let html = '';
    let prev = 0;
    merged.forEach((r) => {
      const s = map[r[0]] ?? 0;
      const e = (map[r[1] - 1] ?? s) + 1;
      html += escapeHtml(str.slice(prev, s)) + '<mark class="search-match">' + escapeHtml(str.slice(s, e)) + '</mark>';
      prev = e;
    });
    return html + escapeHtml(str.slice(prev));
  }

  function buildSnippet(sec, pos, terms) {
    const text = sec.texto || '';
    if (!text) return null;
    const { norm, map } = sectionNorms(sec).texto;
    if (!norm) return null;
    const W = 96;
    const anchor = pos >= 0 ? pos : 0;
    let s = Math.max(0, anchor - W);
    while (s > 0 && isWordChar(norm[s])) s -= 1;
    if (s > 0) s += 1;
    let e = Math.min(norm.length, anchor + W);
    while (e < norm.length && isWordChar(norm[e])) e += 1;

    const ranges = [];
    terms.flatMap(termVariants).forEach((v) => {
      let idx = norm.indexOf(v, s);
      while (idx >= 0 && idx + v.length <= e) {
        if (idx === 0 || !isWordChar(norm[idx - 1])) ranges.push([idx, idx + v.length]);
        idx = norm.indexOf(v, idx + 1);
      }
    });
    if (!ranges.length && pos >= 0) {
      const len = Math.min(terms[0] ? terms[0].length : 1, norm.length - pos);
      if (len > 0) ranges.push([pos, pos + len]);
    }
    if (!ranges.length) return null;

    ranges.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
    const merged = [];
    ranges.forEach((r) => {
      const last = merged[merged.length - 1];
      if (last && r[0] < last[1]) last[1] = Math.max(last[1], r[1]);
      else merged.push([r[0], r[1]]);
    });

    const oS = map[s] ?? 0;
    const oE = (map[Math.min(e, norm.length) - 1] ?? text.length - 1) + 1;
    let html = s > 0 ? '… ' : '';
    let prev = oS;
    merged.forEach((r) => {
      const ms = map[r[0]] ?? 0;
      const me = (map[r[1] - 1] ?? ms) + 1;
      if (ms < prev) return;
      html += escapeHtml(text.slice(prev, ms)) + '<mark class="search-match">' + escapeHtml(text.slice(ms, me)) + '</mark>';
      prev = me;
    });
    html += escapeHtml(text.slice(prev, oE));
    if (e < norm.length) html += ' …';
    return html;
  }

  // ---------- Visitados recentemente ----------
  function loadRecentes() {
    try {
      const raw = localStorage.getItem(RECENTES_KEY);
      const arr = raw ? JSON.parse(raw) : [];
      return Array.isArray(arr) ? arr.filter((x) => x && x.url && x.titulo).slice(0, 6) : [];
    } catch (_) {
      return [];
    }
  }

  function pushRecente(entry) {
    try {
      const arr = loadRecentes().filter((x) => x.url !== entry.url);
      arr.unshift({ url: entry.url, titulo: entry.titulo, grupo: entry.grupo || '' });
      localStorage.setItem(RECENTES_KEY, JSON.stringify(arr.slice(0, 6)));
    } catch (_) { /* armazenamento indisponível */ }
  }

  function recordCurrentPage() {
    if (!INDICE.length) return;
    const page = INDICE.find((p) => location.pathname.endsWith('/docs/' + p.url));
    if (page) pushRecente({ url: page.url, titulo: page.titulo, grupo: page.grupo });
  }

  // ---------- Busca local: destaques na própria página ----------
  // Acento-insensível: casa sobre o texto normalizado e devolve o texto
  // original dentro de <mark>. As âncoras dos títulos são ignoradas.
  const searchableEls = [...document.querySelectorAll('.docs-main [data-searchable]')];
  const searchableOriginals = new Map(searchableEls.map((el) => [el, el.innerHTML]));

  function resetHighlights() {
    searchableEls.forEach((el) => { el.innerHTML = searchableOriginals.get(el); });
  }

  function runLocalHighlight(rawQuery) {
    resetHighlights();
    const terms = splitTerms(rawQuery);
    if (!terms.length) {
      if (searchStatusEl) searchStatusEl.textContent = '';
      return 0;
    }
    const pattern = terms.flatMap(termVariants).map(escapeRegExp).join('|');
    const re = new RegExp(pattern, 'g');
    let count = 0;
    searchableEls.forEach((el) => {
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const nodes = [];
      while (walker.nextNode()) {
        const node = walker.currentNode;
        if (node.parentElement && node.parentElement.closest('.heading-anchor')) continue;
        if ((node.nodeValue || '').trim()) nodes.push(node);
      }
      nodes.forEach((node) => {
        const value = node.nodeValue || '';
        const { norm, map } = normWithMap(value);
        re.lastIndex = 0;
        const ranges = [];
        let m = re.exec(norm);
        while (m) {
          const os = map[m.index] ?? 0;
          const oe = (map[m.index + m[0].length - 1] ?? os) + 1;
          ranges.push([os, oe]);
          count += 1;
          if (ranges.length >= 400) break;
          m = re.exec(norm);
        }
        if (!ranges.length) return;
        ranges.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
        const frag = document.createDocumentFragment();
        let prev = 0;
        ranges.forEach((r) => {
          if (r[0] < prev) return;
          frag.append(value.slice(prev, r[0]));
          const mark = document.createElement('mark');
          mark.className = 'search-hit';
          mark.textContent = value.slice(r[0], r[1]);
          frag.append(mark);
          prev = r[1];
        });
        frag.append(value.slice(prev));
        node.parentNode.replaceChild(frag, node);
      });
    });
    if (searchStatusEl) {
      searchStatusEl.textContent = count
        ? count + ' ocorrência' + (count === 1 ? '' : 's') + ' nesta página.'
        : 'Nenhuma ocorrência nesta página.';
    }
    return count;
  }

  // ---------- Paleta de busca (modal) ----------
  const MAGNIFIER_SVG = '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="7" cy="7" r="5" stroke="currentColor" stroke-width="1.7"/><path d="M11 11l3.4 3.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>';
  const SUGESTOES_URLS = ['instalacao.html', 'primeiro_programa.html', 'modulos/jogos.html', 'modulos/json.html', 'modulos/matematica.html', 'testes.html', 'repl_cli.html'];

  let modal = null;
  let input = null;
  let listEl = null;
  let countEl = null;
  let localCountEl = null;
  let clearBtn = null;
  let closeBtn = null;
  let optionEls = [];
  let activeOption = -1;
  let lastQuery = '';
  let lastTrigger = null;

  function resultHref(page, sec) {
    if (isCurrentPage(page)) return sec && sec.id ? '#' + sec.id : '#conteudo-docs';
    return siteRoot + 'docs/' + page.url + (sec && sec.id ? '#' + sec.id : '');
  }

  function groupLabel(text) {
    return '<div class="search-group-label" aria-hidden="true">' + escapeHtml(text) + '</div>';
  }

  function simpleOption(entry) {
    return '<a class="search-result" role="option" href="' + escapeHtml(siteRoot + 'docs/' + entry.url) + '"'
      + ' data-url="' + escapeHtml(entry.url) + '" data-titulo="' + escapeHtml(entry.titulo) + '"'
      + ' data-grupo="' + escapeHtml(entry.grupo || '') + '">'
      + '<span class="search-result-eyebrow">' + escapeHtml(entry.grupo || 'Documentação') + '</span>'
      + '<span class="search-result-title">' + escapeHtml(entry.titulo) + '</span>'
      + '</a>';
  }

  function trimSnippetText(text, max) {
    if (text.length <= max) return text;
    const cut = text.slice(0, max);
    const sp = cut.lastIndexOf(' ');
    return (sp > 40 ? cut.slice(0, sp) : cut) + '…';
  }

  function resultOptionHtml(r, idx, terms) {
    const { page, sec } = r;
    const eyebrow = page.titulo + (page.apelido ? ' · ' + page.apelido : '');
    const title = sec && sec.titulo ? sec.titulo : page.titulo;
    const snippet = sec ? buildSnippet(sec, r.pos, terms) : null;
    const fallbackSnippet = page.descricao ? markString(trimSnippetText(page.descricao, 150), terms) : null;
    return '<a class="search-result" role="option" id="coral-opt-' + idx + '" href="' + escapeHtml(resultHref(page, sec)) + '"'
      + ' data-url="' + escapeHtml(page.url) + '" data-titulo="' + escapeHtml(page.titulo) + '"'
      + ' data-grupo="' + escapeHtml(page.grupo || '') + '">'
      + '<span class="search-result-eyebrow">' + escapeHtml(eyebrow) + '</span>'
      + '<span class="search-result-title">' + markString(title, terms) + '</span>'
      + (snippet || fallbackSnippet ? '<span class="search-result-snippet">' + (snippet || fallbackSnippet) + '</span>' : '')
      + '</a>';
  }

  function collectOptions() {
    optionEls = [...listEl.querySelectorAll('[role="option"]')];
    activeOption = -1;
    input.setAttribute('aria-expanded', String(optionEls.length > 0));
    input.removeAttribute('aria-activedescendant');
  }

  function getSugestoes() {
    const out = [];
    SUGESTOES_URLS.forEach((url) => {
      const p = INDICE.find((x) => x.url === url);
      if (p) out.push({ url: p.url, titulo: p.titulo, grupo: p.grupo });
    });
    if (!out.length) INDICE.slice(0, 6).forEach((p) => out.push({ url: p.url, titulo: p.titulo, grupo: p.grupo }));
    return out.slice(0, 6);
  }

  function renderIdleState() {
    const recentes = loadRecentes();
    let html = '';
    if (recentes.length) {
      html += groupLabel('Visitados recentemente')
        + '<ul class="search-results-list">' + recentes.map(simpleOption).join('') + '</ul>';
    }
    if (INDICE.length) {
      html += groupLabel('Sugestões')
        + '<ul class="search-results-list">' + getSugestoes().map(simpleOption).join('') + '</ul>';
    }
    if (!INDICE.length) {
      html += '<div class="search-empty">Índice de busca indisponível nesta instalação. Use a navegação lateral ou o menu.</div>';
    }
    html += '<div class="search-tip">A busca casa <strong>todos</strong> os termos (ex.: <code>lista matriz</code>), ignora acentos, tolera erros de digitação e cobre títulos, texto e código das páginas.</div>';
    listEl.innerHTML = html;
    collectOptions();
  }

  function renderSearch() {
    const q = String(input.value || '').trim();
    clearBtn.hidden = !q;
    if (!q) {
      renderIdleState();
      countEl.textContent = INDICE.length ? INDICE.length + ' páginas indexadas' : '';
      return;
    }
    if (!INDICE.length) {
      listEl.innerHTML = '<div class="search-empty">Índice de busca indisponível nesta instalação.</div>';
      countEl.textContent = 'Índice indisponível';
      return;
    }
    const res = findGlobalResults(q);
    if (!res.total) {
      const sug = res.terms.map(didYouMean).find(Boolean);
      listEl.innerHTML = '<div class="search-empty"><strong>Nenhum resultado</strong> para «' + escapeHtml(q) + '».'
        + (sug ? ' Você quis dizer <button type="button" class="search-suggest" data-search-suggest="' + escapeHtml(sug) + '">' + escapeHtml(sug) + '</button>?' : '')
        + '<br><span class="search-tip-inline">Tente termos mais curtos ou remova uma palavra: a busca exige todos os termos, e sem eles exibe correspondências parciais.</span></div>';
      countEl.textContent = 'Nenhum resultado';
      collectOptions();
      return;
    }
    const here = res.results.filter((r) => isCurrentPage(r.page));
    const elsewhere = res.results.filter((r) => !isCurrentPage(r.page));
    let html = '';
    if (res.partial) html += '<div class="search-partial">Nem todos os termos apareceram juntos; exibindo páginas com pelo menos um deles.</div>';
    let idx = 0;
    if (here.length) {
      html += groupLabel('Nesta página') + '<ul class="search-results-list">'
        + here.map((r) => resultOptionHtml(r, idx++, res.terms)).join('') + '</ul>';
    }
    if (elsewhere.length) {
      html += groupLabel(here.length ? 'Outras páginas' : 'Documentação') + '<ul class="search-results-list">'
        + elsewhere.map((r) => resultOptionHtml(r, idx++, res.terms)).join('') + '</ul>';
    }
    listEl.innerHTML = html;
    collectOptions();
    countEl.textContent = res.total + ' resultado' + (res.total === 1 ? '' : 's') + ' · ' + res.pages + ' página' + (res.pages === 1 ? '' : 's')
      + (res.results.length < res.total ? ' · exibindo ' + res.results.length : '');
  }

  function updateLocalCount() {
    if (!localCountEl) return;
    if (!searchableEls.length || !String(input.value || '').trim()) { localCountEl.textContent = ''; return; }
    const n = document.querySelectorAll('.docs-main mark.search-hit').length;
    localCountEl.textContent = n ? n + ' nesta página' : '';
  }

  function moveActive(delta) {
    if (!optionEls.length) return;
    activeOption = (activeOption + delta + optionEls.length) % optionEls.length;
    optionEls.forEach((el, i) => el.classList.toggle('active', i === activeOption));
    const el = optionEls[activeOption];
    input.setAttribute('aria-activedescendant', el.id);
    el.scrollIntoView({ block: 'nearest' });
  }

  function applyQuery(value) {
    input.value = value;
    lastQuery = value;
    runLocalHighlight(value);
    renderSearch();
    updateLocalCount();
  }

  function buildModal() {
    if (modal) return;
    modal = document.createElement('div');
    modal.className = 'search-modal';
    modal.innerHTML = (
      '<div class="search-backdrop" data-search-close></div>'
      + '<div class="search-panel" role="dialog" aria-modal="true" aria-labelledby="coral-search-heading">'
      + '<h2 class="visually-hidden" id="coral-search-heading">Buscar na documentação</h2>'
      + '<div class="search-input-row">'
      + '<span class="search-icon" aria-hidden="true">' + MAGNIFIER_SVG + '</span>'
      + '<input id="coral-search-input" type="text" placeholder="Buscar páginas, seções, funções…" autocomplete="off" autocapitalize="off" spellcheck="false" role="combobox" aria-expanded="false" aria-controls="coral-search-list" aria-autocomplete="list" aria-label="Termo de busca">'
      + '<button class="search-clear" type="button" data-search-clear aria-label="Limpar busca" hidden>Limpar</button>'
      + '<button class="search-close" type="button" data-search-close>Fechar</button>'
      + '</div>'
      + '<div class="search-list" id="coral-search-list" role="listbox" aria-label="Resultados da busca"></div>'
      + '<div class="search-footer">'
      + '<span class="search-count" data-search-count aria-live="polite"></span>'
      + '<span class="search-local" data-search-local></span>'
      + '<span class="search-hints" aria-hidden="true"><kbd>↑↓</kbd> navegar · <kbd>Enter</kbd> abrir · <kbd>Esc</kbd> fechar</span>'
      + '</div>'
      + '</div>'
    );
    document.body.append(modal);
    input = modal.querySelector('#coral-search-input');
    listEl = modal.querySelector('#coral-search-list');
    countEl = modal.querySelector('[data-search-count]');
    localCountEl = modal.querySelector('[data-search-local]');
    clearBtn = modal.querySelector('[data-search-clear]');
    closeBtn = modal.querySelector('[data-search-close]');

    input.addEventListener('input', () => {
      lastQuery = input.value;
      runLocalHighlight(lastQuery);
      renderSearch();
      updateLocalCount();
    });

    modal.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        event.preventDefault();
        event.stopPropagation();
        closeModal();
        return;
      }
      if (event.key === 'Tab') {
        // Mantém o foco circulando dentro da paleta.
        const focusables = [input, clearBtn, closeBtn, ...optionEls].filter((el) => el && !el.hidden);
        if (focusables.length) {
          const i = focusables.indexOf(document.activeElement);
          const next = event.shiftKey ? (i <= 0 ? focusables.length - 1 : i - 1) : (i === focusables.length - 1 ? 0 : i + 1);
          event.preventDefault();
          focusables[next].focus();
        }
        return;
      }
      if (event.target !== input) return;
      if (event.key === 'ArrowDown' && optionEls.length) { event.preventDefault(); moveActive(1); }
      else if (event.key === 'ArrowUp' && optionEls.length) { event.preventDefault(); moveActive(-1); }
      else if (event.key === 'Enter' && optionEls.length) {
        event.preventDefault();
        (optionEls[activeOption >= 0 ? activeOption : 0]).click();
      }
    });

    modal.addEventListener('click', (event) => {
      if (event.target.closest('[data-search-close]')) {
        closeModal();
        return;
      }
      if (event.target.closest('[data-search-clear]')) {
        applyQuery('');
        input.focus();
        return;
      }
      if (event.target.closest('[data-search-suggest]')) {
        applyQuery(event.target.closest('[data-search-suggest]').getAttribute('data-search-suggest') || '');
        input.focus();
        input.select();
      }
    });

    // Clique em resultado: registra nos recentes antes de navegar.
    listEl.addEventListener('click', (event) => {
      const opt = event.target.closest('[role="option"]');
      if (!opt) return;
      if (opt.dataset.url) pushRecente({ url: opt.dataset.url, titulo: opt.dataset.titulo, grupo: opt.dataset.grupo });
      closeModal();
    });
  }

  function openModal() {
    buildModal();
    if (closeTimer) { clearTimeout(closeTimer); closeTimer = null; }
    lastTrigger = document.activeElement;
    modal.classList.remove('closing');
    modal.classList.add('open');
    document.body.classList.add('search-open');
    input.value = lastQuery;
    renderSearch();
    updateLocalCount();
    input.focus();
    input.select();
  }

  let closeTimer = null;

  function closeModal() {
    if (!modal || !modal.classList.contains('open')) return;
    modal.classList.remove('open');
    modal.classList.add('closing');
    document.body.classList.remove('search-open');
    if (closeTimer) clearTimeout(closeTimer);
    closeTimer = setTimeout(() => {
      modal.classList.remove('closing');
      closeTimer = null;
    }, 160);
    if (lastTrigger && typeof lastTrigger.focus === 'function' && document.contains(lastTrigger)) lastTrigger.focus();
    else input.blur();
  }

  // Botões de abertura (topbar da docs, landing e 404).
  document.querySelectorAll('[data-search-open]').forEach((btn) => {
    btn.addEventListener('click', () => openModal());
  });

  function isTypingTarget(target) {
    if (!target) return false;
    const tag = target.tagName;
    return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || target.isContentEditable;
  }

  // Atalhos: "/" e Ctrl/Cmd+K abrem a paleta de qualquer página.
  document.addEventListener('keydown', (event) => {
    if ((event.key === 'k' || event.key === 'K') && (event.ctrlKey || event.metaKey) && !event.altKey) {
      event.preventDefault();
      openModal();
      return;
    }
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !isTypingTarget(event.target)) {
      event.preventDefault();
      openModal();
    }
  });

  recordCurrentPage();

  (async () => {
    try {
      const version = await loadJson(`${siteRoot}docs/dados/versao.json`);
      document.querySelectorAll('[data-version-key]').forEach((el) => {
        const key = el.getAttribute('data-version-key');
        if (version[key] !== undefined) el.textContent = version[key];
      });
    } catch (_) {
      // Valores já estão embutidos no HTML para abrir sem servidor local.
    }

    const grid = document.querySelector('[data-module-grid]');
    if (!grid) return;
    try {
      const modules = await loadJson(`${siteRoot}docs/dados/modulos.json`);
      const highlighted = modules.filter((item) => item.destaque).slice(0, 8);
      if (!highlighted.length) return;
      grid.innerHTML = '';
      highlighted.forEach((item) => {
        const article = document.createElement('a');
        article.className = 'card module-card module-card-link';
        article.href = `${siteRoot}docs/modulos/${item.nome}.html`;
        const code = document.createElement('code');
        code.textContent = item.importacao;
        const title = document.createElement('h3');
        title.textContent = item.nome.charAt(0).toUpperCase() + item.nome.slice(1).replaceAll('_', ' ');
        const p = document.createElement('p');
        p.textContent = item.finalidade || 'Módulo público da Coral.';
        article.append(code, title, p);
        grid.append(article);
      });
    } catch (_) {
      // Cards estáticos permanecem como fallback.
    }
  })();
})();
