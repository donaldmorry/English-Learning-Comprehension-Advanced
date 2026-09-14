#!/bin/bash
# Build the course PDF: markdown -> HTML -> ODT -> (patch page footer) -> PDF
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="${TMPDIR:-/tmp}/eng-course-build"
rm -rf "$WORK"; mkdir -p "$WORK"

python3 "$ROOT/build/build_book.py"
python3 "$ROOT/build/build_site.py"
cp "$ROOT/build/book.html" "$WORK/"
soffice --headless --norestore -env:UserInstallation=file://$WORK/loprofile \
        --infilter="HTML (StarWriter)" --convert-to odt --outdir "$WORK" "$WORK/book.html" >/dev/null 2>&1
python3 "$ROOT/build/patch_odt.py" "$WORK/book.odt" "$WORK/book-final.odt"
soffice --headless --norestore -env:UserInstallation=file://$WORK/loprofile \
        --convert-to pdf --outdir "$WORK" "$WORK/book-final.odt" >/dev/null 2>&1
cp "$WORK/book-final.pdf" "$ROOT/docs/Advanced-English-Reading-and-Vocabulary.pdf"
echo "PDF: $ROOT/docs/Advanced-English-Reading-and-Vocabulary.pdf"
pdfinfo "$ROOT/docs/Advanced-English-Reading-and-Vocabulary.pdf" 2>/dev/null | grep -E 'Pages|Page size|File size' || true
