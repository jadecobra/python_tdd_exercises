# Pumping Python verification map

This directory is the maintained source for verifying the reader-facing behavior of the Pumping Python local Sphinx docs site. Read the index before driving the app, then use the matching feature file as the recipe.

## Baseline preconditions

- Launch an isolated sphinx-autobuild with `scripts/launch.sh` (loopback, high port, `/tmp/pumping-python-verify-$RUN_ID/html`).
- Never drive the user's `bin/run.sh` instance on port 8000 or files under `$REPO/build/html`.
- Run `scripts/doctor.sh` and require HTTP 200, title containing `pumping python`, `LISTEN_PID` owning the port, and the disposable build dir.
- Origin is `http://127.0.0.1:$PORT/`. Canonical tags pointing at `https://www.pumpingpython.com/` are production URLs, not the instance under test.
- No auth. Do not click Cal.com booking buttons or treat Cookiebot/gtag/Trustpilot as proof.

## Driving conventions

- Start every recipe from the baseline state unless its preconditions say otherwise.
- Prefer `<title>`, visible `<h1>`, toctree `a.reference.internal` hrefs, and `form#searchbox` / `input#search-input[aria-label="Search the docs"]`.
- Treat every command as literal. Keep quoted names and flags unchanged.
- Drive with `curl` against the live autobuild origin. Follow hrefs as they appear on the current page (home-relative vs `../` from nested pages).
- Restore nothing: these pages are read-only. Do not remove proof artifacts during cleanup.

## Proof and skip reporting

- Capture the user action (HTTP request) and the resulting page (status + title/h1 + relevant hrefs), not only that the server is up.
- HTTP proof includes `curl -D` headers, the HTML body, and a checksum of the homepage when home is in play.
- Side-effect proof is that `$BUILD_DIR/<route>` exists for the driven path.
- Record the feature ID and entry point with every artifact.
- Report an unreachable path with the attempted command and the unmet precondition.
- Do not report a skipped entry point as verified through a different path.

## Feature entry contract

Each feature file starts with an H1 title and one paragraph describing the user-visible behavior. It then uses exactly four H2 sections in this order.

1. `Sub-features` lists short IDs with one line for each behavior.
2. `How to get to it (user POV)` lists every user entry point.
3. `Driving it with curl` starts with `Preconditions:` and uses labeled bullets that pair each user action with an exact command and observable result.
4. `Gotchas` lists traps that can waste or invalidate a verification run.

Keep implementation details out of the map. Name only user paths, stable handles, required state, commands, and observable proof.

## Features

- [Home and table of contents](./home-toc.md) covers the homepage identity, toctree links, and following those hrefs.
- [Start here](./start-here.md) covers `/setup/index.html` and its OS-setup children.
- [Join a HATCH](./join-hatch.md) covers hatch cards and Cal.com join links without completing a booking.
- [Make TDD manually](./make-tdd-manually.md) covers the first real chapter linked from the home toctree.
- [Search](./search.md) covers the header search form and `/search.html` (results are JavaScript-only).
