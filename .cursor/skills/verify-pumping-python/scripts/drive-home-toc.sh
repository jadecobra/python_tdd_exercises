#!/usr/bin/env bash
# Drive the home-toc feature against the isolated live autobuild server.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

STATE="${VERIFY_STATE:-}"
if [[ -z "$STATE" && -f /tmp/pumping-python-verify-latest-path ]]; then
  STATE="$(cat /tmp/pumping-python-verify-latest-path)"
fi
if [[ -z "$STATE" || ! -f "$STATE" ]]; then
  echo "DRIVE FAIL: no state file. Run scripts/launch.sh then scripts/doctor.sh." >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$STATE"
set +a

"$SCRIPT_DIR/doctor.sh"
echo "doctor passed"

OUT="$ARTIFACTS/home-toc"
mkdir -p "$OUT"
PARSE="$SCRIPT_DIR/parse_page.py"

fetch() {
  local rel="$1" stem="$2"
  local url="http://127.0.0.1:${PORT}${rel}"
  echo "GET $url"
  curl -sS -D "$OUT/${stem}.headers" -o "$OUT/${stem}.html" --max-time 15 "$url"
  local status
  status="$(head -n 1 "$OUT/${stem}.headers")"
  echo "  $status"
  if ! grep -E 'HTTP/[0-9.]+ 200' "$OUT/${stem}.headers" >/dev/null; then
    echo "DRIVE FAIL: $url not HTTP 200 ($status)" >&2
    exit 1
  fi
}

echo "DRIVE home-toc"
fetch "/" "homepage"
python3 "$PARSE" "$OUT/homepage.html" --url "http://127.0.0.1:${PORT}/" \
  --meta "$OUT/homepage.meta.txt" \
  --expect-title-substr "pumping python" \
  --expect-h1-substr "pumping python" \
  --expect-href "hatches/index.html" \
  --expect-href "setup/index.html" \
  --expect-href "make_tdd/make_tdd_manually.html" \
  --expect-href "search.html" \
  --expect-text "join a HATCH" \
  --expect-text "start here" \
  --expect-text "make TDD manually"

fetch "/hatches/index.html" "hatches-index"
python3 "$PARSE" "$OUT/hatches-index.html" --url "http://127.0.0.1:${PORT}/hatches/index.html" \
  --meta "$OUT/hatches-index.meta.txt" \
  --expect-title-substr "join a HATCH" \
  --expect-h1-substr "join a HATCH"

fetch "/setup/index.html" "setup-index"
python3 "$PARSE" "$OUT/setup-index.html" --url "http://127.0.0.1:${PORT}/setup/index.html" \
  --meta "$OUT/setup-index.meta.txt" \
  --expect-title-substr "start here" \
  --expect-h1-substr "start here"

fetch "/make_tdd/make_tdd_manually.html" "make-tdd-manually"
python3 "$PARSE" "$OUT/make-tdd-manually.html" --url "http://127.0.0.1:${PORT}/make_tdd/make_tdd_manually.html" \
  --meta "$OUT/make-tdd-manually.meta.txt" \
  --expect-title-substr "how to make a Python Test Driven Development environment manually" \
  --expect-h1-substr "how to make a Python Test Driven Development environment manually"

fetch "/search.html" "search"
python3 "$PARSE" "$OUT/search.html" --url "http://127.0.0.1:${PORT}/search.html" \
  --meta "$OUT/search.meta.txt" \
  --expect-title-substr "Search" \
  --expect-text 'id="searchbox"' \
  --expect-text 'aria-label="Search the docs"' \
  --expect-text 'id="search-results"'

fetch "/robots.txt" "robots"
fetch "/llms.txt" "llms"

python3 -c '
import hashlib, pathlib, sys
raw = pathlib.Path(sys.argv[1]).read_bytes()
pathlib.Path(sys.argv[2]).write_text(hashlib.sha256(raw).hexdigest() + "  homepage.html\n")
' "$OUT/homepage.html" "$OUT/homepage.sha256"

for rel in index.html hatches/index.html setup/index.html make_tdd/make_tdd_manually.html search.html; do
  if [[ ! -f "$BUILD_DIR/$rel" ]]; then
    echo "DRIVE FAIL: disposable build missing $BUILD_DIR/$rel" >&2
    exit 1
  fi
done

{
  echo "feature: home-toc"
  echo "origin: http://127.0.0.1:$PORT"
  echo "listen_pid: $LISTEN_PID"
  echo "build_dir: $BUILD_DIR"
  echo "action: GET / then follow toctree hrefs hatches/index.html, setup/index.html, make_tdd/make_tdd_manually.html, search.html"
  echo "result: each route HTTP 200 with expected title/h1 from live autobuild HTML (not conf.py)"
  echo "side_effects: $BUILD_DIR/{index.html,hatches/index.html,setup/index.html,make_tdd/make_tdd_manually.html,search.html} exist"
} > "$OUT/PROOF.txt"

echo "DRIVE PASS home-toc"
echo "  evidence in $OUT"
echo "EVIDENCE_DIR=$OUT"
