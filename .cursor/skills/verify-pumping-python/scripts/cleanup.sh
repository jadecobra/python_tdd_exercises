#!/usr/bin/env bash
# Tear down only the instance this verification run started.
# Never kill by process name. Never delete artifacts.
set -euo pipefail

STATE="${VERIFY_STATE:-}"
if [[ -z "$STATE" && -f /tmp/pumping-python-verify-latest-path ]]; then
  STATE="$(cat /tmp/pumping-python-verify-latest-path)"
fi
if [[ -z "$STATE" && -L /tmp/pumping-python-verify-latest ]]; then
  STATE="$(readlink /tmp/pumping-python-verify-latest)"
fi
if [[ -z "$STATE" || ! -f "$STATE" ]]; then
  echo "CLEANUP: no state file; nothing to do."
  exit 0
fi

set -a
# shellcheck disable=SC1090
source "$STATE"
set +a

echo "CLEANUP starting"
echo "  STATE       $STATE"
echo "  LISTEN_PID  ${LISTEN_PID:-}"
echo "  LAUNCH_PID  ${LAUNCH_PID:-}"
echo "  BUILD_DIR   ${BUILD_DIR:-}"
echo "  PARENT      ${PARENT:-}"
echo "  ARTIFACTS   ${ARTIFACTS:-} (kept)"

stop_pid() {
  local pid="$1" label="$2"
  [[ -n "$pid" ]] || return 0
  if ! kill -0 "$pid" 2>/dev/null; then
    echo "  $label $pid already gone"
    return 0
  fi
  kill "$pid" 2>/dev/null || true
  local i=0
  while [[ $i -lt 20 ]]; do
    if ! kill -0 "$pid" 2>/dev/null; then
      echo "  $label $pid stopped"
      return 0
    fi
    i=$((i + 1))
    sleep 0.25
  done
  echo "  $label $pid still alive; sending KILL"
  kill -9 "$pid" 2>/dev/null || true
}

if [[ -n "${PORT:-}" && -n "${LISTEN_PID:-}" ]]; then
  NOW="$(lsof -nP -iTCP:"$PORT" -sTCP:LISTEN -t 2>/dev/null || true)"
  found=0
  for p in $NOW; do
    if [[ "$p" == "$LISTEN_PID" ]]; then
      stop_pid "$LISTEN_PID" "LISTEN_PID"
      found=1
    else
      echo "  WARNING: port $PORT now owned by $p (not our $LISTEN_PID); not killing it"
    fi
  done
  if [[ "$found" == "0" ]]; then
    stop_pid "$LISTEN_PID" "LISTEN_PID"
  fi
else
  stop_pid "${LISTEN_PID:-}" "LISTEN_PID"
fi

if [[ -n "${LAUNCH_PID:-}" && "${LAUNCH_PID:-}" != "${LISTEN_PID:-}" ]]; then
  stop_pid "$LAUNCH_PID" "LAUNCH_PID"
fi

if [[ -n "${PARENT:-}" ]]; then
  case "$PARENT" in
    /tmp/pumping-python-verify-*)
      rm -rf "$PARENT"
      echo "  removed $PARENT"
      ;;
    *)
      echo "  REFUSE to rm PARENT=$PARENT (not under /tmp/pumping-python-verify-)"
      ;;
  esac
fi

if [[ -n "${ARTIFACTS:-}" && -d "$ARTIFACTS" ]]; then
  echo "  artifacts remain at $ARTIFACTS"
fi

if [[ -f /tmp/pumping-python-verify-latest-path ]]; then
  CUR="$(cat /tmp/pumping-python-verify-latest-path 2>/dev/null || true)"
  if [[ "$CUR" == "$STATE" ]]; then
    rm -f /tmp/pumping-python-verify-latest-path /tmp/pumping-python-verify-latest
  fi
fi

echo "CLEANUP done"
