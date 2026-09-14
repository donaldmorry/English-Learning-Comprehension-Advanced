#!/usr/bin/env python3
"""Generate the static GitHub Pages site in docs/ from the lesson markdown."""
import re, os, glob, json, shutil, html as ihtml
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
    words = len(passage.split())
    return dict(n=n, title=title, topic=topic, style=style, level=level, words=words,
                passage=block(passage), vocab=parse_entries(vocab), colloc=parse_entries(colloc))

lessons = [parse(f) for f in sorted(glob.glob(os.path.join(ROOT, 'lessons', 'lesson-*.md')))]
assert len(lessons) == 50

# ---------------------------------------------------------------- templates
def page(title, body, cls='', desc='', depth=0):
    up = '../' * depth
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{up}assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#128218;</text></svg>">
<script>
(function(){{try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();
</script>
</head>
<body class="{cls}">
{body}
<script src="{up}assets/site.js" defer></script>
</body>
</html>
""".format(title=ihtml.escape(title), desc=ihtml.escape(desc), cls=cls, up=up, body=body)

def topbar(depth=0, extra=''):
    up = '../' * depth
    return """<header class="topbar">
  <a class="brand" href="{up}index.html"><span class="brand-mark">AE</span> Advanced English</a>
  <div class="topbar-right">{extra}
    <button id="theme-toggle" class="iconbtn" type="button" aria-label="Switch between light and dark">
      <span class="ico-sun" aria-hidden="true">&#9788;</span><span class="ico-moon" aria-hidden="true">&#9789;</span>
    </button>
  </div>
</header>""".format(up=up, extra=extra)

FOOT = """<footer class="foot">
  <p><strong>Advanced English &mdash; Reading &amp; Vocabulary.</strong>
     Fifty original passages at CEFR C1&ndash;C2.</p>
  <p class="muted">Source and PDF on <a href="https://github.com/{user}/{repo}">GitHub</a>.</p>
</footer>""".format(user=USER, repo=REPO)

# ---------------------------------------------------------------- index
rows = []
for L in lessons:
    rows.append(
      '<a class="row" href="lessons/{n:02d}.html" data-search="{s}">'
      '<span class="row-n">{n:02d}</span>'
      '<span class="row-main"><span class="row-title">{t}</span>'
      '<span class="row-topic">{tp}</span>'
      '<span class="row-style">{st}</span></span>'
      '<span class="row-go" aria-hidden="true">&rarr;</span></a>'.format(
        n=L['n'], t=ihtml.escape(L['title']),
        tp=ihtml.escape(L['topic']), st=ihtml.escape(L['style']),
        s=ihtml.escape((L['title'] + ' ' + L['topic'] + ' ' + L['style']).lower())))

index_body = topbar(0) + """
<main class="wrap">
  <section class="hero">
    <p class="eyebrow">CEFR C1&ndash;C2 &middot; Reading &amp; Vocabulary</p>
    <h1>Fifty passages that do not sound alike.</h1>
    <p class="lede">A reading course for people who already read English comfortably and now
    want to read it <em>well</em> &mdash; to handle the density, irony, hedging and
    register-shifting of real professional prose. Nothing here has been simplified.</p>
    <div class="cta">
      <a class="btn btn-primary" href="lessons/01.html">Start with Lesson 01</a>
      <a class="btn" href="about.html">How to use this course</a>
      <a class="btn" href="Advanced-English-Reading-and-Vocabulary.pdf">Download the PDF</a>
    </div>
    <ul class="stats">
      <li><b>50</b><span>lessons</span></li>
      <li><b>~1,000</b><span>words each</span></li>
      <li><b>1,400</b><span>glossed items</span></li>
      <li><b>50</b><span>distinct registers</span></li>
    </ul>
  </section>

  <section class="note">
    <h2>The order is deliberately scrambled</h2>
    <p>There are no units and no grouping by subject. Lesson 01 is a policy explainer on
    digital currency; Lesson 02 is scene-driven reportage about de-extinction; Lesson 03 is a
    contrarian essay on why machines can play chess and cannot fold laundry. No two
    consecutive lessons come from the same field, and no two open in the same register.</p>
    <p>Grouping material by subject is more comfortable to study and measurably worse to learn
    from &mdash; it lets you settle into one vocabulary field and coast. Mixing forces you to
    work out, every time, what kind of text you are in. <a href="lessons/23.html">Lesson 23</a>
    explains the evidence, and is worth reading early.</p>
  </section>

  <section class="listing">
    <div class="listing-head">
      <h2>All fifty lessons</h2>
      <input id="filter" type="search" placeholder="Filter by title, topic or style&hellip;"
             autocomplete="off" aria-label="Filter lessons">
    </div>
    <div id="rows" class="rows">
""" + '\n'.join(rows) + """
    </div>
    <p id="noresult" class="muted" hidden>No lesson matches that.</p>
  </section>
</main>
""" + FOOT

# ---------------------------------------------------------------- about
about_body = topbar(0) + """
<main class="wrap prose">
  <h1>How to use this course</h1>
  <p class="lede">Fifty lessons &middot; about 1,000 words of prose each &middot; 1,400 glossed
  items &middot; CEFR C1&ndash;C2.</p>

  <p>Each lesson opens with a header naming its subject and its style, so that you know what
  kind of English you are entering before you begin. The passage follows. After it come
  twenty-two vocabulary items, defined in the sense the passage uses, and six multi-word
  phrases &mdash; because fluency lives in collocation far more than in single words.</p>

  <h2>Six instructions worth following</h2>
  <ol class="steps">
    <li><b>Read once for the argument.</b> Do not stop at unknown words. Afterwards ask
        yourself: what is this writer claiming, and what is the evidence?</li>
    <li><b>Read again with the glossary.</b> Now go slowly. Find each item back in the passage
        and notice the company it keeps.</li>
    <li><b>Name the register aloud.</b> The header tells you the style. Work out what produces
        the effect &mdash; sentence length? contractions? passive voice? hedging verbs such as
        <em>appear</em>, <em>suggest</em>, <em>may</em>?</li>
    <li><b>Steal something.</b> Copy three sentences by hand into a notebook, then write your
        own versions on a different subject.</li>
    <li><b>Space it out.</b> One lesson every two or three days beats five in a weekend.
        <a href="lessons/23.html">Lesson 23</a> explains exactly why.</li>
    <li><b>Take them in order.</b> The sequence is already mixed for you. Re-sorting by subject
        would undo the one thing the design is doing.</li>
  </ol>

  <h2>What the course covers</h2>
  <p>Thirty-eight of the fifty lessons sit in science and frontier technology: molecular
  biology, machine learning, robotics, materials, energy, financial infrastructure,
  cryptocurrency. The rest cover cities, language, archaeology, forensics, sport, food,
  conservation, typography and the craft of working well &mdash; scattered throughout rather
  than collected at the end, so that you finish with vocabulary for a laboratory
  <em>and</em> for a conversation.</p>

  <h2>What it deliberately excludes</h2>
  <p>No entertainment or celebrity material. No party politics or politically inflamed
  disputes. No adult content. No religion or the supernatural. No verse and no song lyrics.
  Everything here is prose about the observable world &mdash; which turns out to leave a great
  deal of room.</p>

  <p class="backlink"><a href="index.html">&larr; All lessons</a></p>
</main>
""" + FOOT

# ---------------------------------------------------------------- lessons
def entry_html(items):
    out = ['<dl class="gloss">']
    for term, pos, definition in items:
        if definition:
            out.append('<dt>%s%s</dt><dd>%s</dd>' % (
                term, (' <span class="pos">%s</span>' % ihtml.escape(pos)) if pos else '', definition))
        else:
            out.append('<dt>%s</dt><dd></dd>' % term)
    out.append('</dl>')
    return '\n'.join(out)

os.makedirs(os.path.join(DOCS, 'lessons'), exist_ok=True)
os.makedirs(os.path.join(DOCS, 'assets'), exist_ok=True)

for i, L in enumerate(lessons):
    prev = lessons[i-1] if i > 0 else None
    nxt = lessons[i+1] if i < len(lessons)-1 else None
    nav = []
    nav.append('<a class="pn prev" href="%02d.html"><span>Previous</span><b>%s</b></a>' %
               (prev['n'], ihtml.escape(prev['title'])) if prev else '<span class="pn empty"></span>')
    nav.append('<a class="pn next" href="%02d.html"><span>Next</span><b>%s</b></a>' %
               (nxt['n'], ihtml.escape(nxt['title'])) if nxt else '<span class="pn empty"></span>')
    counter = '<span class="counter">%02d <i>/</i> 50</span>' % L['n']

    body = ('<div class="progress"><div id="bar"></div></div>' + topbar(1, counter) + """
<main class="wrap lesson">
  <article>
    <p class="eyebrow">Lesson {n:02d}</p>
    <h1>{title}</h1>
    <dl class="meta">
      <dt>Topic</dt><dd>{topic}</dd>
      <dt>Style &amp; Register</dt><dd>{style}</dd>
      <dt>Level</dt><dd>{level} &middot; {words} words</dd>
    </dl>
    <div class="passage">
{passage}
    </div>
    <h2 class="glosshead">Key Vocabulary</h2>
    {vocab}
    <h2 class="glosshead">Phrases &amp; Collocations</h2>
    {colloc}
  </article>
  <nav class="pagenav">{nav}</nav>
  <p class="backlink"><a href="../index.html">&larr; All fifty lessons</a></p>
</main>
""".format(n=L['n'], title=ihtml.escape(L['title']), topic=ihtml.escape(L['topic']),
           style=ihtml.escape(L['style']), level=ihtml.escape(L['level']), words=L['words'],
           passage=L['passage'], vocab=entry_html(L['vocab']),
           colloc=entry_html(L['colloc']), nav='\n'.join(nav)) + FOOT)

    html = page('Lesson %02d · %s — Advanced English' % (L['n'], L['title']), body,
                cls='lessonpage', desc='%s. %s' % (L['topic'], L['style']), depth=1)
    open(os.path.join(DOCS, 'lessons', '%02d.html' % L['n']), 'w', encoding='utf-8').write(html)

open(os.path.join(DOCS, 'index.html'), 'w', encoding='utf-8').write(
    page('Advanced English — Reading & Vocabulary', index_body, cls='home',
         desc='Fifty original C1-C2 reading passages with vocabulary glossaries, in fifty different registers.'))
open(os.path.join(DOCS, 'about.html'), 'w', encoding='utf-8').write(
    page('How to use this course — Advanced English', about_body,
         desc='How the course is built and how to work through it.'))
open(os.path.join(DOCS, '.nojekyll'), 'w').write('')

json.dump([{'n': L['n'], 'title': L['title'], 'topic': L['topic'], 'style': L['style'],
            'words': L['words']} for L in lessons],
          open(os.path.join(DOCS, 'lessons.json'), 'w'), indent=1)

print('generated %d lesson pages + index + about' % len(lessons))
