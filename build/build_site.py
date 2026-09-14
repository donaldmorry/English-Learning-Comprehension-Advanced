#!/usr/bin/env python3
"""Generate the static GitHub Pages site in docs/ from the lesson markdown.

Setting is academic: unified serif, dense vertical rhythm, rules rather than
boxes, and no pictographic characters anywhere in the output.
"""
import re, os, glob, json, html as ihtml
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
REPO = 'English-Learning-Comprehension-Advanced'
USER = 'donaldmorry'

md_block = markdown.Markdown(extensions=['tables', 'sane_lists'])
md_line = markdown.Markdown(extensions=[])

def inline(s):
    md_line.reset()
    return re.sub(r'^<p>|</p>$', '', md_line.convert(s.strip())).strip()

def block(s):
    md_block.reset()
    return md_block.convert(s.strip())

ENTRY = re.compile(r'^\*\*(.+?)\*\*(?:\s*\*\((.+?)\)\*)?\s*—\s*(.+)$')

def parse_entries(text):
    out = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line.startswith('**'):
            continue
        m = ENTRY.match(line)
        if m:
            out.append((inline(m.group(1)), m.group(2) or '', inline(m.group(3))))
        else:
            out.append((inline(line), '', ''))
    return out

def parse(path):
    raw = open(path, encoding='utf-8').read()
    n = int(re.search(r'lesson-(\d+)', path).group(1))
    title = re.search(r'^# Lesson \d+ · (.+)$', raw, re.M).group(1)
    topic = re.search(r'^\*\*Topic:\*\* (.+?)\s*$', raw, re.M).group(1)
    style = re.search(r'^\*\*Style & Register:\*\* (.+?)\s*$', raw, re.M).group(1)
    level = re.search(r'^\*\*Level:\*\* (.+?)\s*$', raw, re.M).group(1)
    passage = re.search(r'^## Reading Passage\n(.*?)\n## Key Vocabulary', raw, re.S | re.M).group(1)
    vocab = re.search(r'^## Key Vocabulary\n(.*?)\n## Phrases & Collocations', raw, re.S | re.M).group(1)
    colloc = re.search(r'^## Phrases & Collocations\n(.*)', raw, re.S | re.M).group(1)
    passage = re.sub(r'\n---\s*$', '\n', passage)
    return dict(n=n, title=title, topic=topic, style=style, level=level,
                words=len(passage.split()), passage=block(passage),
                vocab=parse_entries(vocab), colloc=parse_entries(colloc))

lessons = [parse(f) for f in sorted(glob.glob(os.path.join(ROOT, 'lessons', 'lesson-*.md')))]
assert len(lessons) == 50, len(lessons)

# A plain lettered favicon — no pictographic characters.
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' fill='%2315151a'/%3E"
           "%3Ctext x='16' y='23' font-family='Georgia,serif' font-size='19' fill='%23fffffd'"
           " text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E")

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="__FAVICON__">
<link rel="stylesheet" href="__UP__assets/style.css">
<script>(function(){try{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>
</head>
<body>
<div class="sheet">
__BODY__
</div>
<script src="__UP__assets/site.js" defer></script>
</body>
</html>
"""

def page(title, body, desc='', depth=0):
    return (SHELL.replace('__TITLE__', ihtml.escape(title))
                 .replace('__DESC__', ihtml.escape(desc))
                 .replace('__FAVICON__', FAVICON)
                 .replace('__UP__', '../' * depth)
                 .replace('__BODY__', body))

def masthead(depth=0, folio=''):
    up = '../' * depth
    f = '<span>%s</span>' % folio if folio else ''
    return ('<header class="runhead">'
            '<a class="title-link" href="%sindex.html">Advanced English</a>'
            '<span class="runhead-right">%s'
            '<button id="theme-toggle" class="togglebtn" type="button" '
            'aria-label="Switch colour scheme">'
            '<span class="lbl-dark">Dark</span><span class="lbl-light">Light</span>'
            '</button></span></header>' % (up, f))

FOOT = ('<footer class="foot">'
        '<p>Advanced English &mdash; Reading and Vocabulary. '
        'Fifty original passages at CEFR C1&ndash;C2.</p>'
        '<p>Source, lesson files and the complete PDF: '
        '<a href="https://github.com/{u}/{r}">github.com/{u}/{r}</a></p>'
        '</footer>').format(u=USER, r=REPO)

# ------------------------------------------------------------------ contents
rows = []
for L in lessons:
    rows.append(
      '<li data-search="{s}">'
      '<span class="n">{n:02d}</span>'
      '<a class="t" href="lessons/{n:02d}.html">{t}</a>'
      '<span class="sub">{tp}</span>'
      '<span class="reg">{st}</span></li>'.format(
        n=L['n'], t=ihtml.escape(L['title']), tp=ihtml.escape(L['topic']),
        st=ihtml.escape(L['style']),
        s=ihtml.escape((L['title'] + ' ' + L['topic'] + ' ' + L['style']).lower())))

index_body = masthead(0) + """
<main>
  <section class="frontmatter">
    <p class="label">A reading course in contemporary non-fiction prose</p>
    <h1>Advanced English: Reading and Vocabulary</h1>
    <p class="abstract">Fifty original passages of approximately one thousand words,
    each followed by a glossary of the advanced vocabulary it contains. Written for
    readers at CEFR C1&ndash;C2 who are already comfortable in English and now want to
    read it well: to handle the density, irony, hedging and register-shifting of real
    professional prose. Nothing here has been simplified.</p>

    <div class="colophon">
      <div><span class="k">Lessons</span><span class="v">50</span></div>
      <div><span class="k">Words per passage</span><span class="v">c. 1,000</span></div>
      <div><span class="k">Glossed items</span><span class="v">1,400</span></div>
      <div><span class="k">Distinct registers</span><span class="v">50</span></div>
    </div>

    <p class="actions">
      <a href="lessons/01.html">Begin at Lesson 01</a>
      <a href="about.html">Method and use</a>
      <a href="Advanced-English-Reading-and-Vocabulary.pdf">Complete text (PDF, 263 pp.)</a>
    </p>
  </section>

  <hr class="rule-thin">

  <section>
    <h2>On the order of the lessons</h2>
    <div class="standfirst">
      <p>There are no units and no grouping by subject. Lesson 01 is a policy explainer
      on digital currency; Lesson 02 is scene-driven reportage on de-extinction; Lesson 03
      is a contrarian essay on why machines play chess well and fold laundry badly. Two
      constraints were imposed on the sequence: no two consecutive lessons are drawn from
      the same field, and no two open in the same register.</p>
      <p>Material grouped by subject is more comfortable to study and measurably worse to
      learn from, since grouping permits the reader to settle into one vocabulary field and
      one register and coast. Interleaving obliges the reader to determine, on each
      occasion, what kind of text is at hand. <a href="lessons/23.html">Lesson 23</a> sets
      out the evidence, and is worth reading early.</p>
    </div>
  </section>

  <section>
    <div class="contents-head">
      <h2>Contents</h2>
      <input id="filter" type="search" placeholder="Filter by title, subject or register"
             autocomplete="off" aria-label="Filter the table of contents">
    </div>
    <ol class="toc" id="rows">
""" + '\n'.join(rows) + """
    </ol>
    <p id="noresult" class="muted" hidden>No lesson matches that term.</p>
  </section>
</main>
""" + FOOT

# ------------------------------------------------------------------ method
about_body = masthead(0) + """
<main class="prose">
  <p class="label">Editorial note</p>
  <h1>Method and use</h1>
  <p class="abstract">Fifty lessons; approximately one thousand words of prose in each;
  1,400 glossed items; CEFR C1&ndash;C2 throughout.</p>
  <hr class="rule-firm">

  <p>Each lesson opens with a header naming its subject and its style, so that the reader
  knows what kind of English is about to be entered. The passage follows. After it come
  twenty-two vocabulary items, defined in the sense the passage uses, and six multi-word
  phrases, since fluency resides in collocation far more than in single words.</p>

  <h2>1. Procedure</h2>
  <ol>
    <li><b>Read once for the argument.</b> Do not stop at unknown words. Afterwards ask
      what the writer is claiming, and on what evidence.</li>
    <li><b>Read again with the glossary.</b> Now proceed slowly. Locate each item in the
      passage and observe the company it keeps.</li>
    <li><b>Identify the register aloud.</b> The header names the style; determine what
      produces the effect. Sentence length? Contractions? Passive constructions? Hedging
      verbs such as <em>appear</em>, <em>suggest</em>, <em>may</em>?</li>
    <li><b>Imitate.</b> Copy three sentences by hand, then compose your own on an
      unrelated subject.</li>
    <li><b>Distribute the practice.</b> One lesson every two or three days is worth more
      than five in a weekend. <a href="lessons/23.html">Lesson 23</a> gives the evidence.</li>
    <li><b>Preserve the order.</b> The sequence is already interleaved. Re-sorting the
      lessons by subject would defeat the one thing the arrangement is doing.</li>
  </ol>

  <h2>2. Scope</h2>
  <p>Thirty-eight of the fifty lessons are drawn from science and frontier technology:
  molecular biology, machine learning, robotics, materials science, energy, financial
  infrastructure and cryptocurrency. The remainder treat cities, language, archaeology,
  forensic evidence, sport, food chemistry, conservation, typography and the conduct of
  skilled work. These are distributed throughout rather than collected at the end, so that
  the reader finishes with vocabulary suited to a laboratory and to a conversation alike.</p>

  <h2>3. Exclusions</h2>
  <p>The course contains no entertainment or celebrity material, no partisan or
  politically inflamed argument, no adult content, and no treatment of religion or the
  supernatural. There is no verse and there are no song lyrics. Every passage is prose
  concerning the observable world, which proves to leave a great deal of room.</p>

  <p class="backlink"><a href="index.html">Return to the contents</a></p>
</main>
""" + FOOT

# ------------------------------------------------------------------ lessons
def gloss_html(items):
    out = ['<dl class="gloss">']
    for term, pos, definition in items:
        p = ' <span class="pos">%s</span>' % ihtml.escape(pos) if pos else ''
        out.append('<div class="g"><dt>%s%s</dt><dd>%s</dd></div>' % (term, p, definition))
    out.append('</dl>')
    return '\n'.join(out)

os.makedirs(os.path.join(DOCS, 'lessons'), exist_ok=True)
os.makedirs(os.path.join(DOCS, 'assets'), exist_ok=True)

for i, L in enumerate(lessons):
    prev = lessons[i-1] if i > 0 else None
    nxt = lessons[i+1] if i < len(lessons)-1 else None
    nav = []
    nav.append('<div class="pn prev"><span class="k">Preceding</span>'
               '<a href="%02d.html">%02d. %s</a></div>' % (prev['n'], prev['n'], ihtml.escape(prev['title']))
               if prev else '<div class="pn prev"></div>')
    nav.append('<div class="pn next"><span class="k">Following</span>'
               '<a href="%02d.html">%02d. %s</a></div>' % (nxt['n'], nxt['n'], ihtml.escape(nxt['title']))
               if nxt else '<div class="pn next"></div>')

    body = masthead(1, 'Lesson %02d / 50' % L['n']) + """
<main>
  <article>
    <header class="lesson-head">
      <p class="label">Lesson %(n)02d</p>
      <h1>%(title)s</h1>
    </header>
    <dl class="meta">
      <div><dt>Subject</dt><dd>%(topic)s</dd></div>
      <div><dt>Register</dt><dd>%(style)s</dd></div>
      <div><dt>Level</dt><dd>%(level)s</dd></div>
      <div><dt>Extent</dt><dd>%(words)s words</dd></div>
    </dl>
    <div class="passage">
%(passage)s
    </div>
    <h2 class="glosshead">Key vocabulary</h2>
    %(vocab)s
    <h2 class="glosshead">Phrases and collocations</h2>
    %(colloc)s
  </article>
  <nav class="pagenav">%(nav)s</nav>
  <p class="backlink"><a href="../index.html">Return to the contents</a></p>
</main>
""" % dict(n=L['n'], title=ihtml.escape(L['title']), topic=ihtml.escape(L['topic']),
           style=ihtml.escape(L['style']), level=ihtml.escape(L['level']),
           words='{:,}'.format(L['words']), passage=L['passage'],
           vocab=gloss_html(L['vocab']), colloc=gloss_html(L['colloc']),
           nav='\n'.join(nav)) + FOOT

    html = page('Lesson %02d. %s — Advanced English' % (L['n'], L['title']), body,
                desc='%s. %s' % (L['topic'], L['style']), depth=1)
    open(os.path.join(DOCS, 'lessons', '%02d.html' % L['n']), 'w', encoding='utf-8').write(html)

open(os.path.join(DOCS, 'index.html'), 'w', encoding='utf-8').write(
    page('Advanced English: Reading and Vocabulary', index_body,
         desc='Fifty original C1-C2 reading passages with vocabulary glossaries, '
              'in fifty distinct registers.'))
open(os.path.join(DOCS, 'about.html'), 'w', encoding='utf-8').write(
    page('Method and use — Advanced English', about_body,
         desc='How the course is constructed and how to work through it.'))
open(os.path.join(DOCS, '.nojekyll'), 'w').write('')

json.dump([{'n': L['n'], 'title': L['title'], 'topic': L['topic'], 'style': L['style'],
            'words': L['words']} for L in lessons],
          open(os.path.join(DOCS, 'lessons.json'), 'w'), indent=1)

print('generated %d lesson pages, contents and editorial note' % len(lessons))
