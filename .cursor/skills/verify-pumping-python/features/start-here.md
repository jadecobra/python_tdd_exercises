# Start here

Start here is the setup landing page that tells a reader how to prepare a computer before the TDD chapters, with OS-specific child pages and prev/next navigation.

## Sub-features

- `setup-identity` shows `<h1>start here`.
- `setup-children` lists the five OS/setup chapters in the local toctree.
- `setup-next` exposes Sphinx next as WSL install.
- `setup-mac` opens Mac OS requirements for a Mac reader.
- `setup-prev` returns to `join a HATCH`.

## How to get to it (user POV)

- Choose `start here` in the home toctree (`setup/index.html`).
- Follow `<link rel="next">` from `hatches/index.html` if present, or the toctree on any page.
- From this page, choose an OS child: `install WSL on Windows`, `linux/WSL requirements`, `Mac OS requirements`, `Windows without WSL requirements`, or `setup my computer`.

## Driving it with curl

Preconditions:

- Isolated autobuild is healthy at `http://127.0.0.1:$PORT/` (`scripts/doctor.sh` passes).
- Home toctree has been confirmed to contain `setup/index.html` (see `home-toc`) or this recipe opens that href directly.

- **Open start here.** Choose `start here`. Run `curl -sS -D artifacts/start-here/setup-index.headers -o artifacts/start-here/setup-index.html --max-time 15 "http://127.0.0.1:$PORT/setup/index.html"`. HTTP 200; `<title>` is `start here | pumping python: how I solve problems with Test Driven Development`; `<h1>` is `start here`.
- **See covered chapters.** In that HTML, assert these hrefs (page-relative): `install_wsl.html` (`install WSL on Windows`), `linux_requirements.html` (`linux/WSL requirements`), `mac_os_requirements.html` (`Mac OS requirements`), `windows_no_wsl_requirements.html` (`Windows without WSL requirements`), `setup_my_ide.html` (`setup my computer`).
- **Sphinx next.** Assert `<link rel="next" title="how to install Windows Subsystem for Linux on Windows" href="install_wsl.html">`. Run `curl -sS -D artifacts/start-here/install-wsl.headers -o artifacts/start-here/install-wsl.html --max-time 15 "http://127.0.0.1:$PORT/setup/install_wsl.html"`. HTTP 200; heading contains `Windows Subsystem for Linux` or `install WSL`.
- **Mac path.** Choose `Mac OS requirements`. Run `curl -sS -D artifacts/start-here/mac-os.headers -o artifacts/start-here/mac-os.html --max-time 15 "http://127.0.0.1:$PORT/setup/mac_os_requirements.html"`. HTTP 200; `<title>` / `<h1>` contain `Mac OS` or `MacOS`.
- **Prev.** Assert `<link rel="prev" title="join a HATCH" href="../hatches/index.html">` on the start-here page.
- **Proof.** Save headers + HTML for `setup/index.html` and one child. Confirm `$BUILD_DIR/setup/index.html` and the child file exist. Record that the user path was the live URL, not `source/setup/index.rst`.

## Gotchas

- From `/setup/index.html`, child hrefs are `install_wsl.html` not `setup/install_wsl.html`. Prefixing `setup/` twice 404s.
- Sphinx `rel=next` always goes to WSL install, even on a Mac. A Mac reader’s *content* next step is `mac_os_requirements.html` in the “what is next?” section — drive that href when proving the Mac path.
- After setup, the book tells readers to make a TDD environment manually (`make_tdd/make_tdd_manually.html`). That is a different feature file.
- `setup_my_ide.html` toctree label is `setup my computer`.
