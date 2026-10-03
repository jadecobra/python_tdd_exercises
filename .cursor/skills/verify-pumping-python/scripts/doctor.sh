#!/usr/bin/env bash
# Read-only health check for the isolated Pumping Python verification instance.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO="$(cd "$SKILL_DIR/../../.." && pwd)"

STATE="${VERIFY_STATE:-}"
if [[ -z "$STATE" && -f /tmp/pumping-python-verify-latest-path ]]; then
  STATE="$(cat /tmp/pumping-python-verify-latest-path)"
fi
if [[ -z "$STATE" && -L /tmp/pumping-python-verify-latest ]]; then
  STATE="$(readlink /tmp/pumping-python-verify-latest)"
fi
if [[ -z "$STATE" || ! -f "$STATE" ]]; then
  echo "DOCTOR FAIL: no state file. Run scripts/launch.sh first." >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$STATE"
set +a

fail() { echo "DOCTOR FAIL: $*" >&2; exit 1; }

[[ "${VERIFY_APP:-}" == "pumping-python" ]] || fail "state is not a pumping-python verification run"
[[ -n "${PORT:-}" && -n "${LISTEN_PID:-}" && -n "${BUILD_DIR:-}" ]] || fail "state missing PORT/LISTEN_PID/BUILD_DIR"
[[ "$PORT" != "8000" ]] || fail "port is 8000 (user default); this skill must use an isolated high port"

case "$BUILD_DIR" in
  /tmp/pumping-python-verify-*/html) ;;
  *) fail "build dir is not disposable /tmp/pumping-python-verify-*/html (got $BUILD_DIR)" ;;
esac
[[ "$BUILD_DIR" != "$REPO/build/html" ]] || fail "build dir is the user's default $REPO/build/html"

if ! kill -0 "$LISTEN_PID" 2>/dev/null; then
  fail "LISTEN_PID $LISTEN_PID is not running"
fi

LSOF_PIDS="$(lsof -nP -iTCP:"$PORT" -sTCP:LISTEN -t 2>/dev/null || true)"
if [[ -z "$LSOF_PIDS" ]]; then
  fail "nothing is listening on TCP $PORT"
fi
for p in $LSOF_PIDS; do
  if [[ "$p" != "$LISTEN_PID" ]]; then
    fail "port $PORT is owned by PID $p, not our LISTEN_PID $LISTEN_PID. Refusing to drive a foreign instance."
  fi
done

if ! lsof -nP -iTCP:"$PORT" -sTCP:LISTEN | grep -q "127.0.0.1:$PORT"; then
  fail "listener on $PORT is not bound to 127.0.0.1 (our isolated host)"
fi

BODY="$(mktemp -t pp-doctor-body.XXXXXX)"
trap 'rm -f "$BODY"' EXIT
CODE="$(curl -sS -o "$BODY" -w '%{http_code}' --max-time 10 "http://127.0.0.1:$PORT/" || true)"
[[ "$CODE" == "200" ]] || fail "GET / returned HTTP $CODE, expected 200"

TITLE="$(python3 -c '
import re, sys
html = open(sys.argv[1], encoding="utf-8", errors="replace").read()
m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
print(" ".join(re.sub(r"<[^>]+>", "", m.group(1) if m else "").split()))
' "$BODY")"

echo "$TITLE" | grep -qi 'pumping python' || fail "page <title> does not contain 'pumping python' (got: $TITLE)"

if [[ ! -f "$BUILD_DIR/index.html" ]]; then
  fail "disposable build dir missing index.html: $BUILD_DIR"
fi
if ! grep -qi 'pumping python' "$BUILD_DIR/index.html"; then
  fail "disposable $BUILD_DIR/index.html does not contain pumping python"
fi

echo "DOCTOR PASS"
echo "  STATE       $STATE"
echo "  ORIGIN      http://127.0.0.1:$PORT"
echo "  PORT        $PORT"
echo "  LISTEN_PID  $LISTEN_PID"
echo "  LAUNCH_PID  ${LAUNCH_PID:-}"
echo "  BUILD_DIR   $BUILD_DIR"
echo "  HTTP        200"
echo "  TITLE       $TITLE"
echo "  TITLE_OK    contains 'pumping python'"
echo "  ISOLATED    port!=8000 and build dir under /tmp/pumping-python-verify-*"
