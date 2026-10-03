# Join a HATCH

Join a HATCH is the signup landing page with five priced time-slot cards. Each card’s join control is a Cal.com embed trigger; verification observes the cards and links and does not complete a booking.

## Sub-features

- `hatch-identity` shows `<h1>join a HATCH`.
- `hatch-cards` renders five `div.price-card` slots with visible names.
- `hatch-join-links` exposes `a.enroll-btn` with `data-cal-link` for each slot.
- `hatch-from-home` is reachable from the home toctree and in-body “sign up” link.

## How to get to it (user POV)

- Choose `join a HATCH` in the left toctree (`hatches/index.html`).
- From the homepage body, follow `sign up for the 8-week course here` (`hatches/index.html#join-a-hatch`).
- Open `/hatches/index.html` directly.

## Driving it with curl

Preconditions:

- Isolated autobuild is healthy at `http://127.0.0.1:$PORT/` (`scripts/doctor.sh` passes).
- Do not click through to `app.cal.com` and do not submit a booking.

- **Open hatch page.** Choose `join a HATCH`. Run `curl -sS -D artifacts/join-hatch/hatches-index.headers -o artifacts/join-hatch/hatches-index.html --max-time 15 "http://127.0.0.1:$PORT/hatches/index.html"`. HTTP 200; `<title>` is `join a HATCH | pumping python: how I solve problems with Test Driven Development`; first `<h1>` is `join a HATCH`.
- **See cards.** In that HTML, assert five `class="price-card"` blocks and the visible names `morning marauders`, `sunlight soldiers`, `happy hour heroes`, `nighttime ninjas`, `weekend warriors`.
- **Map join controls (do not activate Cal.com).** Assert these `a.enroll-btn` attributes exist (href is a same-page fragment; booking is `data-cal-link`):

  - `join Morning Marauders` → `data-cal-link="jacobitegboje/pumping-python-morning-marauders"` `href="#morning-marauders-booking"`
  - `join sunlight soldiers` → `data-cal-link="jacobitegboje/pumping-python-sunlight-soldiers"`
  - `join happy hour heroes` → `data-cal-link="jacobitegboje/pumping-python-happy-hour-heroes"`
  - `join nighttime ninjas` → `data-cal-link="jacobitegboje/pumping-python-nighttime-ninjas"`
  - `join weekend warriors` → `data-cal-link="jacobitegboje/pumping-python-weekend-warriors"`

- **Map the embed boundary.** Assert the HTML contains `https://app.cal.com/embed/embed.js` and `Cal("init"`. That is the production booking boundary. Stop. Do not `curl` Cal.com to finish signup.
- **Home entry.** Run `curl -sS -o artifacts/join-hatch/from-home.html --max-time 15 "http://127.0.0.1:$PORT/"` and assert `hatches/index.html` and `sign up for the 8-week course here`.
- **Proof.** Save headers + HTML. Side effect: `$BUILD_DIR/hatches/index.html` exists. Record that Cal.com was mapped, not booked.

## Gotchas

- Join buttons look like ordinary links but `href` is a fragment (`#…-booking`). The real target is Cal.com via JS (`data-cal-link`). A 200 on the hatch page does not prove booking works — and this skill must not prove booking.
- `nighttime ninjas` uses `class="price-card highlight"`; still count it as a card.
- Card inner headings mix `<h1>` (most slots) and `<h3>` (`weekend warriors`). Assert the visible names, not a single heading level.
- `hatches/confirmation.html` exists as a post-signup page. Do not treat it as proof of a completed booking during verification.
- Cookiebot may inject a consent overlay in a real browser. curl sees the raw HTML including the Cookiebot script tag; ignore widget state.
