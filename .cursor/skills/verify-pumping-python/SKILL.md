---
name: verify-pumping-python
description: "Drive the Pumping Python local Sphinx docs site the way a reader does — homepage, toctree, start-here, hatch signup cards, chapter pages, and search — and capture HTTP evidence. Use when proving reader-facing pages, nav, search, or hatch/setup entry points on a live sphinx-autobuild instance."
---

# Verify Pumping Python (local Sphinx docs)

Pumping Python is a Sphinx HTML book (`html_theme = sphinxawesome_theme`), not a CLI product. The surface under test is a local `sphinx-autobuild` site. Static extras `robots.txt` and `llms.txt` are also served. There is no auth. Hatch "join" cards are HTML on `/hatches/index.html` with Cal.com `data-cal-link` attributes — map them, do not complete a booking.

Drive with **curl** against the isolated live server. There is no Playwright/Cypress in this repo. Prefer stable handles: page `<title>`, visible `<h1>`, toctree `a.reference.internal` hrefs, and `form#searchbox` / `input#search-input[aria-label="Search the docs"]`.

Repo root: the directory that contains `source/conf.py` and `bin/run.sh`. The repo's own command is `bin/run.sh` → `uv run sphinx-autobuild --host 0.0.0.0 source build/html -j auto` (default port **8000**). **Verification must not reuse that command, that bind, that port, or `build/html`.**

Helpers live in this skill directory (`scripts/`). Run them from anywhere; they locate the repo relative to the skill.

## Launch

Isolated instance: loopback only, unused high port (8765, then 8766…), disposable build dir under `/tmp/pumping-python-verify-$RUN_ID/html`. Never attach to an already-running autobuild. Never pass `--open-browser`.

Exact helper:

```bash
/Users/johnnyblase/gym/python_tdd_exercises/.cursor/skills/verify-pumping-python/scripts/launch.sh
```

What it runs (equivalent if you start by hand):

```bash
REPO=/Users/johnnyblase/gym/python_tdd_exercises
RUN_ID="$(date +%Y%m%d%H%M%S)-$$"
PARENT="/tmp/pumping-python-verify-$RUN_ID"
BUILD_DIR="$PARENT/html"
PORT=8765   # or next free in 8765-8772; refuse 8000
cd "$REPO"
uv run sphinx-autobuild --host 127.0.0.1 --port "$PORT" source "$BUILD_DIR" -j auto
```

Confirmed flags from `uv run sphinx-autobuild --help` on this Mac: `--host HOST`, `--port PORT`, `--open-browser` (do **not** use), `-j auto`, positional `SOURCE_DIR OUTPUT_DIR`. Default listen port when `--port` is omitted is 8000 — verification always sets `--port`.

**Ready signal:** `GET http://127.0.0.1:$PORT/` returns HTTP 200 and the HTML contains `pumping python` (`html_title` / `html_short_title`). First Sphinx build can take a couple of minutes.

Launch double-forks via `scripts/daemonize_autobuild.py` so the server is not a child of the agent shell (otherwise the job group dies when `launch.sh` returns).

Launch writes `$PARENT/state.env` and points `/tmp/pumping-python-verify-latest-path` at it. Subsequent helpers read `VERIFY_STATE` or that pointer.

**Teardown:** `scripts/cleanup.sh` (see Cleanup). Always run generated cleanup after a failed iteration so ports are not stranded.

Two instances are OK if ports and build dirs differ. A process already bound to 8000 (`bin/run.sh` / user default) is **not** this instance — leave it alone.

## Doctor

Read-only. Answers "is this instance worth driving?" Refuse if the answering process is not the PID we started.

```bash
/Users/johnnyblase/gym/python_tdd_exercises/.cursor/skills/verify-pumping-python/scripts/doctor.sh
```

Checks:

1. `state.env` exists and `VERIFY_APP=pumping-python`.
2. `LISTEN_PID` is alive (`kill -0`).
3. `lsof -nP -iTCP:$PORT -sTCP:LISTEN` lists **only** that PID (foreign PID → refuse, do not attach).
4. Listener is `127.0.0.1:$PORT`, not `*:8000` / `0.0.0.0`.
5. `GET /` is HTTP 200.
6. `<title>` contains `pumping python`.
7. `BUILD_DIR` is `/tmp/pumping-python-verify-*/html` and is **not** `$REPO/build/html`. `$BUILD_DIR/index.html` exists and also contains `pumping python`.

Run doctor first whenever anything looks off, and before every drive.

## Drive

Harness: HTTP on the Mac (`curl -sS -D headers -o body`) against `http://127.0.0.1:$PORT`, following real routes from the **built HTML**, not `conf.py`.

Local origin is `http://127.0.0.1:$PORT/`. `html_baseurl` / `rel=canonical` still say `https://www.pumpingpython.com/` — that is production, not the instance under test. Cookiebot (`consent.cookiebot.com`) and gtag (`G-0VPJ6HXTE8`) load from the network; they are not proof. Trustpilot widget JS in `conf.py` `html_js_files` is also third-party.

### Stable handles (from the built theme)

| Handle | Where | Value |
| --- | --- | --- |
| `<title>` | every page | page heading ` \| pumping python: how I solve problems with Test Driven Development` |
| `<h1>` | `#content` | visible chapter/page title |
| toctree | `nav a.reference.internal` | see routes below |
| search form | header | `form#searchbox method="get"`; on inner pages `action="search.html"`; on `/search.html` `action="#"` |
| search field | header | `input#search-input[name=q][type=search][aria-label="Search the docs"]` |
| search link | `<head>` | `<link rel="search" title="Search" href="search.html">` (relative to the page) |
| skip link | top of body | `a[href="#content"]` "Skip to content" |
| next/prev | `<head>` + footer | `link[rel=next]`, `link[rel=prev]` (`html_theme_options.show_prev_next` is true) |
| hatch cards | `/hatches/index.html` | `div.price-card` + `a.enroll-btn[data-cal-link]` |

### Key routes (built hrefs)

From `/` toctree (`source/index.rst` → built `index.html`):

- `/` — home. `<title>` and `<h1>`: `pumping python: how I solve problems with test driven development`. `<link rel="next" href="hatches/index.html" title="join a HATCH">`.
- `/hatches/index.html` — `join a HATCH`.
- `/setup/index.html` — `start here`. Rel next: `setup/install_wsl.html` (`how to install Windows Subsystem for Linux on Windows`).
- `/make_tdd/make_tdd_manually.html` — toctree label `make TDD manually`; `<h1>` `how to make a Python Test Driven Development environment manually`.
- `/search.html` — Sphinx search page (generated). Title starts with `Search | pumping python`.
- `/robots.txt`, `/llms.txt` — `html_extra_path` static files.

Also present, not required for the first five features: `/conventions.html`, `/genindex.html`, `/hatches/confirmation.html`.

Follow hrefs **as they appear on the current page**. From `/setup/index.html` they are relative (`install_wsl.html`, `../hatches/index.html`). From `/` they are `setup/index.html`, `hatches/index.html`.

### One-feature helper

```bash
/Users/johnnyblase/gym/python_tdd_exercises/.cursor/skills/verify-pumping-python/scripts/drive-home-toc.sh
```

Feature recipes: [`features/README.md`](features/README.md). Drive the map; one convenient entry point is not a substitute for listed entry points.

## Evidence

Directory (must survive cleanup):

`/Users/johnnyblase/gym/python_tdd_exercises/.cursor/skills/verify-pumping-python/artifacts/`

Per drive, write a subdirectory named after the feature id (`artifacts/home-toc/`, …):

- `*.headers` — `curl -D` response headers (status line is the proof of HTTP 200).
- `*.html` — response body snapshot of the resulting page.
- `*.meta.txt` — extracted `<title>`, `<h1>`, sha256, URL.
- `homepage.sha256` — checksum of the homepage body when driving home.
- `PROOF.txt` — feature id, entry point, action taken, resulting state, side effects.

Proof standards:

1. **Real user path.** Fetch the live autobuild URL a reader would open. Do not treat `source/conf.py` values, `source/*.rst`, or `$REPO/build/html` as the proof. The disposable `$BUILD_DIR` file for that route is the side-effect check, not the user-visible action.
2. **Action and resulting state.** Record the request (method + path) and the resulting status + title/h1 (and toctree hrefs when that is the claim). A final screenshot of an unrelated page is not enough.
3. **Side effects.** For these docs, the side effect of a successful serve is that `$BUILD_DIR/<route>` exists as HTML (or `robots.txt` / `llms.txt`). Search JS results are **not** a file-system side effect; see search gotchas.
4. **Mocks only at production boundaries.** Cookiebot, gtag, Trustpilot, and Cal.com embeds are production third parties. Do not load or complete them to prove the book. Observing `data-cal-link` / script `src` in the HTML is enough to map the boundary.

Bonus screenshot of the homepage is optional. This Mac has `screencapture` (desktop only) and does **not** have `wkhtmltoimage` or Playwright — skip screenshots unless a real page renderer is already installed.

## Cleanup

```bash
/Users/johnnyblase/gym/python_tdd_exercises/.cursor/skills/verify-pumping-python/scripts/cleanup.sh
```

- Kill **only** `LISTEN_PID` (and `LAUNCH_PID` if different) recorded in `state.env`. Never `pkill sphinx-autobuild` / never kill by process name. If `lsof` shows a different PID on the port, do not kill it.
- Remove only `/tmp/pumping-python-verify-$RUN_ID/` (the disposable parent that contains `html/` and `state.env`).
- **Never delete `artifacts/`.** Proof that cleanup kept evidence: `ls` the feature subdirectory after cleanup.

Do not stop the user's default instance on port 8000.

## Helpers

All executable. Invocation is the path below (or `VERIFY_STATE=/path/to/state.env` prefixed).

| Script | What |
| --- | --- |
| `scripts/launch.sh` | Isolated autobuild; prints PORT, LISTEN_PID, BUILD_DIR, STATE |
| `scripts/doctor.sh` | Read-only readiness / isolation check |
| `scripts/drive-home-toc.sh` | Runs doctor, drives `home-toc`, writes `artifacts/home-toc/` |
| `scripts/cleanup.sh` | Kill our PIDs, rm disposable parent, keep artifacts |
| `scripts/parse_page.py` | Title/h1/href assertions used by the drive helper |

```bash
SKILL=/Users/johnnyblase/gym/python_tdd_exercises/.cursor/skills/verify-pumping-python
"$SKILL/scripts/launch.sh"
"$SKILL/scripts/doctor.sh"
"$SKILL/scripts/drive-home-toc.sh"
"$SKILL/scripts/cleanup.sh"
ls -la "$SKILL/artifacts/home-toc"
```

Optional: `VERIFY_PORT=8766 VERIFY_RUN_ID=manual1 "$SKILL/scripts/launch.sh"` when 8765 is taken.

## Feature map

Start at [`features/README.md`](features/README.md). Keep it honest with `/maintain-verification-skill` as the book changes.
