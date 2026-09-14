#!/usr/bin/env bash
# Create the GitHub repo, push this course to it, and turn on GitHub Pages.
#
#   GH_TOKEN=<your token> bash build/publish.sh
#
# or just run it and paste the token when prompted (it is not echoed, never
# written to disk, and is stripped from the git remote after the push).
#
# Token needs the "repo" scope. A fine-grained token needs Contents: write,
# Administration: write and Pages: write on the account.

set -euo pipefail

USER="donaldmorry"
REPO="English-Learning-Comprehension-Advanced"
SITE="https://${USER}.github.io/${REPO}/"

cd "$(dirname "$0")/.."

TOKEN="${GH_TOKEN:-}"
if [ -z "$TOKEN" ]; then
  read -rsp "GitHub token for ${USER}: " TOKEN
  echo
fi
if [ -z "$TOKEN" ]; then
  echo "No token given."
  exit 1
fi

AUTH="Authorization: Bearer ${TOKEN}"
ACC="Accept: application/vnd.github+json"
VER="X-GitHub-Api-Version: 2022-11-28"

field() { python3 -c "import sys,json
try: d=json.load(sys.stdin)
except Exception: print(''); raise SystemExit
print(d.get('$1') or d.get('message') or '')"; }

echo "==> checking the token"
LOGIN=$(curl -sS -H "$AUTH" -H "$ACC" -H "$VER" https://api.github.com/user | field login)
if [ "$LOGIN" != "$USER" ]; then
  if [ -z "$LOGIN" ] || [ "$LOGIN" = "Bad credentials" ]; then
    echo "    token rejected: ${LOGIN:-no response}"
    echo "    make a new one at https://github.com/settings/tokens (scope: repo)"
    exit 1
  fi
  echo "    note: token belongs to '$LOGIN', not '$USER' — continuing"
else
  echo "    authenticated as $LOGIN"
fi

echo "==> creating ${USER}/${REPO}"
read -r -d '' PAYLOAD <<'JSON' || true
{"name":"English-Learning-Comprehension-Advanced",
 "description":"A 50-lesson advanced English reading and vocabulary course (CEFR C1-C2).",
 "homepage":"https://donaldmorry.github.io/English-Learning-Comprehension-Advanced/",
 "private":false,"has_issues":true,"has_wiki":false,"has_projects":false}
JSON
RESULT=$(curl -sS -X POST -H "$AUTH" -H "$ACC" -H "$VER" \
         https://api.github.com/user/repos -d "$PAYLOAD" | field full_name)
if [ "$RESULT" = "${USER}/${REPO}" ]; then
  echo "    created"
elif printf '%s' "$RESULT" | grep -qi "already exists"; then
  echo "    already exists - pushing into it"
else
  echo "    could not create: $RESULT"
  exit 1
fi

echo "==> pushing"
git remote remove origin 2>/dev/null || true
git remote add origin "https://${TOKEN}@github.com/${USER}/${REPO}.git"
git push -u origin main --quiet
git remote set-url origin "https://github.com/${USER}/${REPO}.git"
echo "    pushed; token removed from .git/config"

echo "==> enabling GitHub Pages (branch main, folder /docs)"
PAGES=$(curl -sS -X POST -H "$AUTH" -H "$ACC" -H "$VER" \
        "https://api.github.com/repos/${USER}/${REPO}/pages" \
        -d '{"source":{"branch":"main","path":"/docs"}}' | field html_url)
if printf '%s' "$PAGES" | grep -q '^http'; then
  echo "    enabled: $PAGES"
elif printf '%s' "$PAGES" | grep -qi "already exists"; then
  echo "    already enabled"
else
  echo "    could not enable automatically: ${PAGES:-unknown error}"
  echo "    do it by hand: repo Settings > Pages > Source: main, folder /docs"
fi

echo
echo "Repository : https://github.com/${USER}/${REPO}"
echo "Live site  : ${SITE}"
echo "The first Pages build takes a minute or two."
echo
echo "Now revoke the token you just used: https://github.com/settings/tokens"
