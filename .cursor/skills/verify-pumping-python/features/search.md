# Search

Search lets a reader open the Sphinx search page and the header search field. Result lists are filled by JavaScript (`searchtools.js` + `searchindex.js`); curl can prove the form and index exist, not the rendered hit list.

## Sub-features

- `search-header-form` is the header `form#searchbox` on every page.
- `search-page` is `/search.html` with `#search-results` and a JS fallback message.
- `search-index` serves `/searchindex.js` for client-side lookup.
- `search-query-url` accepts `?q=` but does not render hits without JS.

## How to get to it (user POV)

- Use the header field `Search the docs` (`input#search-input`, placeholder `Search ...`) on any page. On inner pages the form `action` is `search.html`.
- Follow `<link rel="search" title="Search" href="search.html">`.
- Open `/search.html` directly.
- Press the theme shortcut advertised by the `⌘K` kbd hint (browser only; not curl).

## Driving it with curl

Preconditions:

- Isolated autobuild is healthy at `http://127.0.0.1:$PORT/` (`scripts/doctor.sh` passes).
- Do not treat Cookiebot, Google CSE (`searchbox.html.bak` is not in the build), or gtag as search.

- **Open search page.** Choose Search. Run `curl -sS -D artifacts/search/search.headers -o artifacts/search/search.html --max-time 15 "http://127.0.0.1:$PORT/search.html"`. HTTP 200; `<title>` starts with `Search | pumping python`.
- **See form.** Assert `form id="searchbox"` with `input id="search-input" name="q" type="search" aria-label="Search the docs"`. On this page `action` is `#`.
- **See JS search surface.** Assert `div id="search-results"` and the fallback text `Please activate Javascript to enable searching the documentation.` Assert scripts `src="_static/searchtools.js"` and `src="searchindex.js"`.
- **Fetch index.** Run `curl -sS -D artifacts/search/searchindex.headers -o artifacts/search/searchindex.js --max-time 15 "http://127.0.0.1:$PORT/searchindex.js"`. HTTP 200; body is non-empty JavaScript (tens of KB). A grep for a known term such as `unittest` or `HATCH` should match.
- **Query URL without JS.** Run `curl -sS -D artifacts/search/query.headers -o artifacts/search/query.html --max-time 15 "http://127.0.0.1:$PORT/search.html?q=unittest"`. HTTP 200; the HTML still has `#search-results` empty of hits. Do **not** claim a result list from this response.
- **Header form on home.** Run `curl -sS -o artifacts/search/home-form.html --max-time 15 "http://127.0.0.1:$PORT/"` and assert `form id="searchbox" action="search.html"` and `aria-label="Search the docs"`.
- **Proof.** Save headers + HTML + `searchindex.js`. Side effects: `$BUILD_DIR/search.html` and `$BUILD_DIR/searchindex.js` exist.

## Gotchas

- Search results are JS-only. curl of `search.html?q=…` will not contain hit markup. The fallback node `#fallback` is hidden by an inline script in a browser; curl still sees `Please activate Javascript to enable searching the documentation.`
- `source/_templates/searchbox.html.bak` is a Google CSE snippet and is **not** applied (`.bak`, not a live template). Do not look for `gcse:search` in the build.
- Header form `action` is `search.html` on content pages and `#` on `/search.html` itself.
- `rel=search` href is `#` on the search page and `search.html` (or `../search.html`) elsewhere.
- A 200 on `searchindex.js` plus the form is the honest curl proof. Filling the field and reading `#search-results` requires a browser runtime this repo does not ship.
