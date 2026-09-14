# Build notes

`make_pdf.sh` turns the 50 lesson files into the course PDF:

```
lessons/*.md  --build_book.py-->  build/book.html
build/book.html  --soffice (HTML StarWriter filter)-->  book.odt
book.odt  --patch_odt.py-->  book-final.odt      (adds the page-number footer)
book-final.odt  --soffice-->  Advanced-English-Reading-and-Vocabulary.pdf
```

Run it with `bash build/make_pdf.sh`.

## Why it is built this way

No `pandoc`, no LaTeX, no headless Chrome is installed on this machine. LibreOffice is
the only converter available, and its HTML importer has several quirks that cost real
time to find. They are recorded here so nobody rediscovers them:

1. **Multi-value `margin` shorthands are mis-parsed.** `margin: 4.4cm 0 0 0` was applied
   to the left and right edges as well, squeezing a 30pt title into a 3.6cm column and
   wrapping it mid-word. **Always use `margin-top` / `margin-bottom` / `margin-left` /
   `margin-right` longhand.** The same applies to `padding`.
2. **`div` styling and descendant selectors are ignored.** `div.meta { border-top: ... }`
   and `div.meta p { font-size: ... }` both do nothing. Only simple class or element
   selectors applied directly to the styled element survive — hence `p.metatop`,
   `p.metamid`, `p.metaend` rather than a wrapper div.
3. **CSS borders on `th`/`td` are dropped**, and hairlines below ~1px are floored to
   nothing. Tables need the legacy `border="1" cellspacing="0" cellpadding="4"`
   attributes, which `build_book.py` injects after the Markdown conversion.
4. **Page breaks must sit on the element itself.** `page-break-before` on a wrapper div
   is ignored; it is set on `h1` and on `p.unitno` instead.
5. **`text-indent` is ignored**, so the book uses block paragraphs with spacing rather
   than first-line indents.
6. **Page furniture cannot come from CSS.** The page-number footer is added by editing
   the ODF `styles.xml` between the two conversions (`patch_odt.py`): it fills in the
   empty `<style:footer-style/>` on page layout `Mpm2`, attaches a `<style:footer>` to
   the `HTML` master page, and adds a `FirstPage` master page with no footer so that the
   title page is clean.
7. `@page { size: ... }` **is** honoured — the book is 17 × 24 cm — and `<text:h>`
   outline levels survive, so the PDF gets a navigable bookmark tree for free.

## Checks worth re-running after editing lessons

```bash
# passage length, glossary counts, header fields, duplicate terms
python3 - <<'PY'
import re,glob
for f in sorted(glob.glob('lessons/lesson-*.md')):
    s=open(f).read()
    w=len(re.search(r'## Reading Passage\n(.*?)\n## Key Vocabulary',s,re.S).group(1).split())
    print(f, w)
PY
```

`SYLLABUS.md`'s table is generated from the lesson headers — if you change a lesson's
**Topic** or **Style & Register** line, regenerate the matching row rather than editing
the table by hand.
