#!/usr/bin/env python3
"""Assemble the 50 lesson files into one styled HTML book for PDF conversion."""
import re, glob, os, html as ihtml
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, 'lessons')

md_block = markdown.Markdown(extensions=['tables', 'sane_lists'])
md_line  = markdown.Markdown(extensions=[])

def inline(s):
    """Render one line of markdown, stripping the wrapping <p>."""
    md_line.reset()
    out = md_line.convert(s.strip())
    return re.sub(r'^<p>|</p>$', '', out).strip()

def block(s):
    md_block.reset()
    out = md_block.convert(s.strip())
    # LibreOffice's HTML importer ignores CSS borders on cells; the legacy
    # attribute is the only reliable way to get ruled tables out of it.
    return out.replace('<table>', '<table border="1" cellspacing="0" cellpadding="4">')

def parse(path):
    raw = open(path, encoding='utf-8').read()
    title = re.search(r'^# (.+)$', raw, re.M).group(1)
    num, name = title.split(' · ', 1)
    meta = re.search(r'^# .+?\n\n(.*?)\n\n---', raw, re.S | re.M).group(1)
    metas = [inline(l.strip()) for l in meta.strip().split('\n') if l.strip()]
    passage = re.search(r'^## Reading Passage\n(.*?)\n## Key Vocabulary', raw, re.S | re.M).group(1)
    vocab   = re.search(r'^## Key Vocabulary\n(.*?)\n## Phrases & Collocations', raw, re.S | re.M).group(1)
    colloc  = re.search(r'^## Phrases & Collocations\n(.*)', raw, re.S | re.M).group(1)
    # strip the horizontal rules that separate sections in the source
    passage = re.sub(r'\n---\n\s*$', '\n', passage)
    entries = lambda t: [inline(l) for l in t.strip().split('\n') if l.strip().startswith('**')]
    topic = next((m for m in metas if m.startswith('<strong>Topic')), '')
    style = next((m for m in metas if m.startswith('<strong>Style')), '')
    clean = lambda s: re.sub(r'<[^>]+>', '', s).split(':', 1)[-1].strip()
    return dict(num=num, name=name, metas=metas, passage=passage,
                vocab=entries(vocab), colloc=entries(colloc),
                topic=clean(topic), style=clean(style))

files = sorted(glob.glob(os.path.join(LESSONS, 'lesson-*.md')))
data = [parse(f) for f in files]
assert len(data) == 50, len(data)

CSS = """
@page { size: 17cm 24cm; margin-top: 2.1cm; margin-bottom: 2.1cm; margin-left: 2.3cm; margin-right: 2.3cm; }
body { font-family: "Liberation Serif","Times New Roman",serif; font-size: 10.8pt;
       line-height: 1.45; text-align: justify; color: #16181c; }
p { margin-top: 0; margin-bottom: 0.46em; margin-left: 0; margin-right: 0; }

h1 { page-break-before: always; page-break-after: avoid;
     font-family: "Liberation Sans",Arial,sans-serif; font-size: 16.5pt; font-weight: bold;
     color: #14314f; text-align: left; line-height: 1.22;
     margin-top: 0; margin-bottom: 0.5em; margin-left: 0; margin-right: 0; }
h2 { page-break-after: avoid; font-family: "Liberation Sans",Arial,sans-serif;
     font-size: 10.5pt; font-weight: bold; color: #8a4212; letter-spacing: 0.05em;
     text-transform: uppercase; text-align: left;
     margin-top: 1.2em; margin-bottom: 0.5em; margin-left: 0; margin-right: 0; }
h3 { page-break-after: avoid; font-family: "Liberation Serif",serif; font-size: 11pt;
     font-weight: bold; color: #14314f; text-align: left;
     margin-top: 0.9em; margin-bottom: 0.3em; margin-left: 0; margin-right: 0; }

/* lesson header block: borders must sit on paragraphs, not on a div */
p.metatop { font-family: "Liberation Sans",Arial,sans-serif; font-size: 8.9pt; color: #3c4450;
            text-align: left; line-height: 1.4; border-top: 1.4pt solid #14314f;
            padding-top: 5pt; margin-top: 0; margin-bottom: 0; }
p.metamid { font-family: "Liberation Sans",Arial,sans-serif; font-size: 8.9pt; color: #3c4450;
            text-align: left; line-height: 1.4; margin-top: 0; margin-bottom: 0; }
p.metaend { font-family: "Liberation Sans",Arial,sans-serif; font-size: 8.9pt; color: #3c4450;
            text-align: left; line-height: 1.4; border-bottom: 1px solid #b9c2cc;
            padding-bottom: 6pt; margin-top: 0; margin-bottom: 1.25em; }

p.vocab { margin-top: 0; margin-bottom: 0.2em; margin-left: 0.55cm; margin-right: 0;
          font-size: 10.1pt; line-height: 1.35; text-align: left; }

table { border-collapse: collapse; width: 100%; font-size: 9.3pt;
        margin-top: 0.5em; margin-bottom: 0.8em; }
th { background-color: #e9edf2; border: 1px solid #8e99a4; padding-top: 3pt; padding-bottom: 3pt; padding-left: 5pt; padding-right: 5pt;
     font-family: "Liberation Sans",Arial,sans-serif; text-align: left; font-size: 9.3pt; }
td { border: 1px solid #8e99a4; padding-top: 3pt; padding-bottom: 3pt; padding-left: 5pt; padding-right: 5pt; text-align: left; font-size: 9.3pt; }
ul, ol { margin-top: 0.3em; margin-bottom: 0.6em; margin-left: 1.3em; }
li { margin-bottom: 0.22em; text-align: justify; }
hr { border: 0; border-top: 1px solid #c0c8d0; margin-top: 1em; margin-bottom: 1em; }

/* title page */
p.bigtitle { text-align: center; font-family: "Liberation Sans",Arial,sans-serif;
             font-size: 29pt; font-weight: bold; color: #14314f; line-height: 1.14;
             margin-top: 4.6cm; margin-bottom: 0; margin-left: 0; margin-right: 0; }
p.subtitle { text-align: center; font-size: 14pt; font-style: italic; color: #5a6472;
             margin-top: 0.55em; margin-bottom: 0; margin-left: 0; margin-right: 0; }
p.rule { text-align: center; color: #8a4212; font-size: 12pt; letter-spacing: 0.55em;
         margin-top: 1.5em; margin-bottom: 1.5em; margin-left: 0; margin-right: 0; }
p.tagline { text-align: center; font-family: "Liberation Sans",Arial,sans-serif;
            font-size: 9.6pt; color: #3c4450; line-height: 1.85;
            margin-top: 0; margin-bottom: 0; margin-left: 0; margin-right: 0; }

/* contents */
p.toch { text-align: left; font-family: "Liberation Sans",Arial,sans-serif; font-size: 9.2pt;
         font-weight: bold; letter-spacing: 0.13em; text-transform: uppercase; color: #8a4212;
         page-break-after: avoid;
         margin-top: 1.1em; margin-bottom: 0.45em; margin-left: 0; margin-right: 0; }
p.toc { text-align: left; font-size: 10.1pt; line-height: 1.33;
        margin-top: 0; margin-bottom: 0.3em; margin-left: 0.5cm; margin-right: 0; }
span.tocnum { font-family: "Liberation Sans",Arial,sans-serif; font-weight: bold; color: #14314f; }
span.tocstyle { color: #6b7481; font-size: 9.1pt; font-style: italic; }
p.lead { text-align: left; font-size: 10.6pt; color: #3c4450; font-style: italic;
         margin-top: 0; margin-bottom: 1em; margin-left: 0; margin-right: 0; }
"""

def esc(s):
    return s

out = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
       '<title>Advanced English: Reading &amp; Vocabulary</title>',
       '<style>', CSS, '</style></head><body>']

# ---------- title page ----------
out.append("""
<p class="bigtitle">Advanced English</p>
<p class="subtitle">Reading &amp; Vocabulary</p>
<p class="rule">&mdash;&mdash;&mdash;</p>
<p class="tagline">Fifty original passages in contemporary non-fiction prose<br>
Science &middot; Technology &middot; Finance &middot; Craft &middot; Society<br>
CEFR&nbsp;C1&ndash;C2</p>
""")

# ---------- how to use ----------
out.append("""
<h1 class="nobreak">How to Use This Course</h1>
<p class="metatop">&nbsp;</p>
<p class="metaend"><strong>Fifty lessons &middot; about 1,000 words of prose each &middot; 1,400 glossed items</strong></p>
<p>This is a reading course for people who can already read English comfortably and
now want to read it <em>well</em> &mdash; to handle the density, the irony, the hedging and the
register-shifting of real professional prose. Nothing here has been simplified. Every passage is
written the way a good journal, a good magazine or a good working memo is actually written.</p>
<p>Each lesson opens with a header naming its subject and its style, so that you know
what kind of English you are entering before you begin. The passage follows. After it come
twenty-two vocabulary items, defined in the sense the passage uses, and six multi-word phrases
&mdash; because fluency lives in collocation far more than in single words.</p>

<h2>Why the order looks random</h2>
<p>It is random &mdash; deliberately, and under two constraints. There are no units, no chapters
and no grouping by subject. A policy explainer on digital currency is followed by scene-driven
reportage about de-extinction, then a contrarian essay on why machines can play chess and cannot
fold laundry. No two consecutive lessons come from the same field, and no two open in the same
register.</p>
<p>This is the most important structural decision in the course. Material grouped by subject is
more comfortable to study and measurably worse to learn from: grouping lets you settle into one
vocabulary field and one register and coast. Mixing forces you to work out, every single time,
what kind of text you are in and what it is trying to do to you &mdash; which is the actual skill
that separates an advanced reader from an intermediate one. It will feel harder. That is the
mechanism, not a side effect.</p>

<h2>Six instructions worth following</h2>
<p class="noindent"><strong>1. Read once for the argument.</strong> Do not stop at unknown words.
Afterwards, ask yourself: what is this writer claiming, and what is the evidence?</p>
<p class="noindent"><strong>2. Read again with the glossary.</strong> Now go slowly. Find each
item back in the passage and notice the company it keeps.</p>
<p class="noindent"><strong>3. Name the register aloud.</strong> The header tells you the style.
Work out what produces the effect &mdash; sentence length? contractions? passive voice? hedging
verbs such as <em>appear</em>, <em>suggest</em>, <em>may</em>?</p>
<p class="noindent"><strong>4. Steal something.</strong> Copy three sentences by hand into a
notebook, then write your own versions on a different subject.</p>
<p class="noindent"><strong>5. Space it out.</strong> One lesson every two or three days beats
five in a weekend. Lesson 23 explains exactly why, and is worth reading early.</p>
<p class="noindent"><strong>6. Take them in order.</strong> The sequence is already mixed for
you. Re-sorting the lessons by subject would undo the one thing the design is doing.</p>

<h2>What this course deliberately excludes</h2>
<p>No entertainment or celebrity material. No party politics or politically inflamed
dispute. No adult content. No religion or the supernatural. No verse and no song lyrics. Everything
here is prose about the observable world &mdash; which turns out to leave a great deal of room.</p>
<p>The spine of the course is science and frontier technology: molecular biology, machine learning,
robotics, materials, energy, financial infrastructure, cryptocurrency. Around that spine sit lessons
on cities, language, archaeology, forensics, sport, food, conservation and typography &mdash;
scattered throughout rather than collected at the end, so that you finish with vocabulary for a
laboratory <em>and</em> for a conversation.</p>
""")

# ---------- contents ----------
out.append('<h1>Contents</h1>')
out.append('<p class="lead">Fifty lessons, in a deliberately irregular order. '
           'No units, no grouping by subject, and no two written in the same voice.</p>')
for d in data:
    n = d['num'].replace('Lesson ', '')
    out.append('<p class="toc"><b>%s</b>&nbsp;&nbsp;%s<br>'
               '<i><font size="2">%s &mdash; %s</font></i></p>'
               % (n, ihtml.escape(d['name']), d['topic'], d['style']))

# ---------- lessons ----------
for d in data:
    out.append('<h1>%s</h1>' % ihtml.escape(d['num'] + ' · ' + d['name']))
    n = len(d['metas'])
    for k, m in enumerate(d['metas']):
        cls = 'metatop' if k == 0 else ('metaend' if k == n - 1 else 'metamid')
        out.append('<p class="%s">%s</p>' % (cls, m))
    out.append(block(d['passage']))
    out.append('<h2>Key Vocabulary</h2>')
    for e in d['vocab']:
        out.append('<p class="vocab">%s</p>' % e)
    out.append('<h2>Phrases &amp; Collocations</h2>')
    for e in d['colloc']:
        out.append('<p class="vocab">%s</p>' % e)

out.append('<h1>End of Course</h1>')
out.append('<p>Fifty passages. Roughly fifty-four thousand words of continuous '
           'prose, one thousand one hundred glossed vocabulary items and three hundred '
           'collocations, across fifty subjects and fifty distinct registers.</p>'
           '<p>If you read them all, you did the thing the last lesson is about. '
           'Go back to the first lesson and read it again &mdash; it will be a different text now, '
           'and the difference is the measure of what you gained.</p>')
out.append('</body></html>')

dest = os.path.join(ROOT, 'build', 'book.html')
open(dest, 'w', encoding='utf-8').write('\n'.join(out))
print('wrote', dest, os.path.getsize(dest), 'bytes')
