# Make TDD manually

Make TDD manually is the first real TDD chapter linked from the home table of contents. It teaches how to make a Python Test Driven Development environment by hand (uv, folders, first unittest).

## Sub-features

- `chapter-identity` shows the long `<h1>` for the manual TDD environment chapter.
- `chapter-from-toc` is linked as `make TDD manually` → `make_tdd/make_tdd_manually.html`.
- `chapter-requirements` points back at start here.
- `chapter-nav` exposes prev `conventions` and next `what is a module?`.
- `chapter-next-section` includes a visible “what is next?” heading.

## How to get to it (user POV)

- Choose `make TDD manually` in the home toctree.
- Open `/make_tdd/make_tdd_manually.html` directly.
- After finishing start-here setup, follow the book’s recommendation to make a TDD environment manually (same href).

## Driving it with curl

Preconditions:

- Isolated autobuild is healthy at `http://127.0.0.1:$PORT/` (`scripts/doctor.sh` passes).
- Home toctree contains `make_tdd/make_tdd_manually.html` (see `home-toc`) or this recipe opens that href directly.

- **Open chapter from toctree href.** Choose `make TDD manually`. Run `curl -sS -D artifacts/make-tdd-manually/chapter.headers -o artifacts/make-tdd-manually/chapter.html --max-time 15 "http://127.0.0.1:$PORT/make_tdd/make_tdd_manually.html"`. HTTP 200.
- **Identity.** Assert `<title>` starts with `how to make a Python Test Driven Development environment manually` and contains `pumping python`. Assert `<h1>` is `how to make a Python Test Driven Development environment manually`.
- **Requirements point at setup.** In the chapter HTML, assert a link to start here (`../setup/index.html` or visible text `start here`).
- **Prev/next.** Assert `<link rel="prev" title="conventions" href="../conventions.html">` and `<link rel="next" title="what is a module?" href="../exceptions/ModuleNotFoundError/index.html">`.
- **Optional follow next.** Run `curl -sS -D artifacts/make-tdd-manually/next.headers -o artifacts/make-tdd-manually/next.html --max-time 15 "http://127.0.0.1:$PORT/exceptions/ModuleNotFoundError/index.html"`. HTTP 200; heading/title contain `module`.
- **Proof.** Save headers + HTML. Side effect: `$BUILD_DIR/make_tdd/make_tdd_manually.html` exists. Quote the observed `<h1>` in `PROOF.txt`.

## Gotchas

- Toctree **label** is `make TDD manually`. Page **title/h1** is the long “how to make a Python Test Driven Development environment manually”. Assert both; do not expect the h1 to equal the toctree label.
- `make_tdd/index.html` is a different document (`how to make a Python Test Driven Development environment`). Do not treat it as this chapter.
- Nested hrefs are `../setup/index.html`, not `setup/index.html`.
- The chapter is long (tabs for WSL/Linux/Mac vs no-WSL). curl proof is the served HTML containing those tab labels, not executing the terminal commands in the chapter.
