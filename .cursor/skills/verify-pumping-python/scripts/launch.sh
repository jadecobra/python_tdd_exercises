#!/usr/bin/env bash
# Start an isolated Pumping Python sphinx-autobuild instance.
# Never attaches to an already-running server. Never uses repo build/html or port 8000.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO="$(cd "$SKILL_DIR/../../.." && pwd)"
ARTIFACTS="$SKILL_DIR/artifacts"

if [[ ! -f "$REPO/source/conf.py" ]]; then
  echo "REFUSE: expected Sphinx conf at $REPO/source/conf.py" >&2
  exit 1
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "REFUSE: uv is not on PATH" >&2
  exit 1
fi

mkdir -p "$ARTIFACTS"

pick_port() {
  local p
  for p in 8765 8766 8767 8768 8769 8770 8771 8772; do
    if ! lsof -nP -iTCP:"$p" -sTCP:LISTEN >/dev/null 2>&1; then
      echo "$p"
      return 0
    fi
  done
  return 1
}

PORT="${VERIFY_PORT:-}"
if [[ -z "$PORT" ]]; then
  PORT="$(pick_port)" || {
    echo "REFUSE: no free high port in 8765-8772" >&2
    exit 1
  }
else
  if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
    echo "REFUSE: port $PORT is already in use; will not attach" >&2
    lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >&2 || true
    exit 1
  fi
fi

if [[ "$PORT" == "8000" ]]; then
  echo "REFUSE: port 8000 is the default sphinx-autobuild port; pick an unused high port" >&2
  exit 1
fi

RUN_ID="${VERIFY_RUN_ID:-$(date +%Y%m%d%H%M%S)-$$}"
PARENT="/tmp/pumping-python-verify-$RUN_ID"
BUILD_DIR="$PARENT/html"
STATE="${VERIFY_STATE:-$PARENT/state.env}"
LOG="$PARENT/autobuild.log"

if [[ "$BUILD_DIR" == "$REPO/build/html" ]]; then
  echo "REFUSE: build dir must be disposable under /tmp, not $BUILD_DIR" >&2
  exit 1
fi

mkdir -p "$BUILD_DIR" "$(dirname "$STATE")"

cd "$REPO"

# Double-fork so the autobuild survives the launching shell/job group.
# Do not pass --open-browser. Bind loopback only.
PIDFILE="$PARENT/uv.pid"
: >"$LOG"
python3 "$SCRIPT_DIR/daemonize_autobuild.py" "$PIDFILE" "$LOG" "$REPO" "$PORT" "$BUILD_DIR"
# Give the grandchild a moment to write the pidfile.
i=0
LAUNCH_PID=""
while [[ $i -lt 50 ]]; do
  if [[ -s "$PIDFILE" ]]; then
    LAUNCH_PID="$(cat "$PIDFILE")"
    break
  fi
  i=$((i + 1))
  sleep 0.1
done
if [[ -z "$LAUNCH_PID" ]]; then
  echo "REFUSE: daemonize did not write pidfile $PIDFILE" >&2
  tail -n 40 "$LOG" >&2 || true
  exit 1
fi

LISTEN_PID=""
READY=0
i=0
while [[ $i -lt 180 ]]; do
  if ! kill -0 "$LAUNCH_PID" 2>/dev/null; then
    echo "REFUSE: sphinx-autobuild exited before becoming ready. Last log lines:" >&2
    tail -n 80 "$LOG" >&2 || true
    exit 1
  fi
  LISTEN_PID="$(lsof -nP -iTCP:"$PORT" -sTCP:LISTEN -t 2>/dev/null | head -n 1 || true)"
  if [[ -n "$LISTEN_PID" ]]; then
    CODE="$(curl -sS -o /tmp/pp-verify-ready-body.html -w '%{http_code}' --max-time 5 "http://127.0.0.1:$PORT/" || true)"
    if [[ "$CODE" == "200" ]] && grep -qi 'pumping python' /tmp/pp-verify-ready-body.html; then
      READY=1
      break
    fi
  fi
  i=$((i + 1))
  sleep 2
done

if [[ "$READY" != "1" ]]; then
  echo "REFUSE: instance did not become ready on 127.0.0.1:$PORT within timeout" >&2
  echo "--- autobuild.log ---" >&2
  tail -n 80 "$LOG" >&2 || true
  if [[ -n "${LISTEN_PID:-}" ]]; then kill "$LISTEN_PID" 2>/dev/null || true; fi
  kill "$LAUNCH_PID" 2>/dev/null || true
  exit 1
fi

umask 077
{
  echo "VERIFY_APP=pumping-python"
  echo "REPO=$REPO"
  echo "SKILL_DIR=$SKILL_DIR"
  echo "ARTIFACTS=$ARTIFACTS"
  echo "RUN_ID=$RUN_ID"
  echo "PARENT=$PARENT"
  echo "BUILD_DIR=$BUILD_DIR"
  echo "PORT=$PORT"
  echo "ORIGIN=http://127.0.0.1:$PORT"
  echo "LAUNCH_PID=$LAUNCH_PID"
  echo "LISTEN_PID=$LISTEN_PID"
  echo "LOG=$LOG"
  echo "PIDFILE=$PIDFILE"
  echo "STARTED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
} >"$STATE"

ln -sfn "$STATE" /tmp/pumping-python-verify-latest
echo "$STATE" > /tmp/pumping-python-verify-latest-path

echo "LAUNCHED"
echo "  ORIGIN      http://127.0.0.1:$PORT"
echo "  PORT        $PORT"
echo "  LAUNCH_PID  $LAUNCH_PID"
echo "  LISTEN_PID  $LISTEN_PID"
echo "  BUILD_DIR   $BUILD_DIR"
echo "  STATE       $STATE"
echo "  LOG         $LOG"
echo "  ARTIFACTS   $ARTIFACTS"
echo "STATE=$STATE"
