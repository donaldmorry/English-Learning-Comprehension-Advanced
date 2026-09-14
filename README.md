# Advanced English — Reading & Vocabulary

**A 50-lesson reading course in contemporary non-fiction prose, at CEFR C1–C2.**

### ▶ Read it online: **https://donaldmorry.github.io/English-Learning-Comprehension-Advanced/**

---

## What this is

Fifty original reading passages of about 1,000 words each, every one followed by a
glossary of the advanced vocabulary it contains — 1,100 defined words and 300
collocations in total.

It is for learners who can already read English comfortably and now want to read it
*well*: to handle the density, irony, hedging and register-shifting of real professional
prose. Nothing here has been simplified. The passages are written the way a good
magazine, a good journal or a good working memo is actually written.

## The order is deliberately scrambled

There are no units and no grouping by subject. Lesson 01 is a policy explainer on digital
currency; Lesson 02 is scene-driven reportage about de-extinction; Lesson 03 is a
contrarian essay on why machines can play chess and cannot fold laundry. Two constraints
were enforced on the shuffle:

- no two consecutive lessons come from the same field
- no two consecutive lessons open in the same register

Grouping material by subject is more comfortable to study and measurably worse to learn
from — it lets you settle into one vocabulary field and coast. Mixing forces you to work
out, every time, what kind of text you are in.
[Lesson 23](https://donaldmorry.github.io/English-Learning-Comprehension-Advanced/lessons/23.html)
explains the evidence, and is worth reading early.

## What's covered

Thirty-eight of the fifty lessons sit in science and frontier technology: molecular
biology, machine learning, robotics, materials, energy, financial infrastructure,
cryptocurrency. The rest cover cities, language, archaeology, forensics, sport, food,
conservation, typography and the craft of working well — scattered throughout rather than
collected at the end.

Fifty topics, fifty distinct registers. One lesson is a peer-reviewed literature review;
another a letter from an Antarctic research station; another a hard-nosed business case
study; another a friend talking to you across a kitchen table about sourdough.

**Deliberately excluded:** entertainment and celebrity, party politics and politically
inflamed disputes, adult content, and religion or the supernatural. No verse, no lyrics.

## How each lesson is built

| Section | What it does |
|---|---|
| Header | Names the topic, style and register before you read |
| Reading Passage | ~1,000 words of continuous prose |
| Key Vocabulary | 22 advanced words, defined in the sense used in the passage |
| Phrases & Collocations | 6 multi-word items — where fluency actually lives |

## Repository layout

```
lessons/          lesson-01.md … lesson-50.md   the source of truth
docs/             the published site (GitHub Pages serves from here)
  index.html        landing page, searchable list of all fifty
  about.html        how to use the course
  lessons/01.html … 50.html
  lessons.json      machine-readable index
  Advanced-English-Reading-and-Vocabulary.pdf   the whole course as one 263-page book
build/            site + PDF generators, and NOTES.md on how they work
SYLLABUS.md       every lesson's topic and style, in course order
```

## Building

The markdown in `lessons/` is the source. Everything else is generated:

```bash
python3 build/build_site.py   # regenerate docs/ (needs python3-markdown)
bash    build/make_pdf.sh     # regenerate the site and the PDF (needs libreoffice)
```

`build/NOTES.md` documents the PDF toolchain and the LibreOffice quirks it works around.

## Using it

1. **Read once for the argument.** Don't stop at unknown words.
2. **Read again with the glossary.** Find each item back in the passage.
3. **Name the register aloud.** Work out what produces the effect.
4. **Steal something.** Copy three sentences by hand; write your own versions.
5. **Space it out.** One lesson every two or three days beats five in a weekend.
6. **Take them in order.** The sequence is already mixed for you.
