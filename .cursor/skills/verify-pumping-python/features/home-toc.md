# Home and table of contents

The homepage identifies the book as Pumping Python and lists the reader table of contents so a user can open hatch signup, start-here setup, chapters, and search from one page.

## Sub-features

- `home-identity` shows the book title in `<title>` and the visible `<h1>`.
- `home-toctree` lists the primary reader links on the home page.
- `home-follow-hatch` opens `hatches/index.html` from the home toctree.
- `home-follow-setup` opens `setup/index.html` from the home toctree.
- `home-follow-chapter` opens `make_tdd/make_tdd_manually.html` from the home toctree.
- `home-search-link` exposes `search.html` via `rel=search` and the header form.

## How to get to it (user POV)

- Open `/` (or `/index.html`) on the isolated origin.
- Choose `join a HATCH` in the left toctree.
- Choose `start here` in the left toctree.
- Choose `make TDD manually` in the left toctree.
- Use the header search field or the `Search` link (`rel=search`).

## Driving it with curl

Preconditions:

- Isolated autobuild is healthy at `http://127.0.0.1:$PORT/` (`scripts/doctor.sh` passes).
- `$PORT` is not 8000 and `$BUILD_DIR` is under `/tmp/pumping-python-verify-`.
- Working directory for relative artifact paths is the skill directory, or use absolute paths.

- **Open home.** Request the homepage. Run `curl -sS -D artifacts/home-toc/homepage.headers -o artifacts/home-toc/homepage.html --max-time 15 "http://127.0.0.1:$PORT/"`. The status line is HTTP 200. `<title>` and `<h1>` both contain `pumping python: how I solve problems with test driven development`.
- **Checksum.** Hash the body. Run `shasum -a 256 artifacts/home-toc/homepage.html > artifacts/home-toc/homepage.sha256`. The file contains a 64-hex digest for `homepage.html`.
- **See toctree.** Read the homepage HTML. Assert it contains `href="hatches/index.html"` with text `join a HATCH`, `href="setup/index.html"` with text `start here`, `href="make_tdd/make_tdd_manually.html"` with text `make TDD manually`, and `href="search.html"`.
- **Follow hatch.** Choose `join a HATCH`. Run `curl -sS -D artifacts/home-toc/hatches-index.headers -o artifacts/home-toc/hatches-index.html --max-time 15 "http://127.0.0.1:$PORT/hatches/index.html"`. HTTP 200; `<title>` and `<h1>` contain `join a HATCH`.
- **Follow start here.** Choose `start here`. Run `curl -sS -D artifacts/home-toc/setup-index.headers -o artifacts/home-toc/setup-index.html --max-time 15 "http://127.0.0.1:$PORT/setup/index.html"`. HTTP 200; `<title>` and `<h1>` contain `start here`.
- **Follow chapter.** Choose `make TDD manually`. Run `curl -sS -D artifacts/home-toc/make-tdd-manually.headers -o artifacts/home-toc/make-tdd-manually.html --max-time 15 "http://127.0.0.1:$PORT/make_tdd/make_tdd_manually.html"`. HTTP 200; `<h1>` is `how to make a Python Test Driven Development environment manually`.
- **Header search form.** On the homepage HTML, assert `form id="searchbox"` with `action="search.html"` and `input id="search-input" name="q" aria-label="Search the docs"`.
- **Proof.** Write `artifacts/home-toc/PROOF.txt` with the feature id, origin, and the four GET paths. Confirm `$BUILD_DIR/index.html`, `$BUILD_DIR/hatches/index.html`, `$BUILD_DIR/setup/index.html`, and `$BUILD_DIR/make_tdd/make_tdd_manually.html` exist.

Or run the bundled helper:

```bash
scripts/drive-home-toc.sh
```

## Gotchas

- `GET /` and `GET /index.html` both work; doctor uses `/`.
- Logo `href` on home is `#` (current page), not `index.html`. Nested pages use `index.html` / `../index.html`.
- `rel=canonical` is `https://www.pumpingpython.com/index.html`. Proof the **local** origin, not the canonical host.
- `make TDD manually` appears more than once in the toctree (the RST lists it twice). Following either href is the same file.
- `make_tdd/index.html` is a different page (`how to make a Python Test Driven Development environment`). The home toctree chapter entry is `make_tdd/make_tdd_manually.html`.
- Cookiebot and gtag scripts are in the layout; their network load is not homepage proof.
