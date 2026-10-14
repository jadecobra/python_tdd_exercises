# Project Agent Guidelines

## Stated goals

### Any technical work
- Evidence over narrative. Primary sources are the truth.
- Shortest path to a correct, maintainable, fast outcome.
- Verify before conclusions. Confidence follows only what was checked.

### Book chapters
Two audiences, one honesty bar:

1. **Technical fidelity.** Steps, snippets, `literalinclude`s, line numbers, emphasizes, catalogs, terminal quotes, and review or meta claims match the real files and real Python, unittest, and pytest behavior.
2. **Beginner experience.** Read as a motivated beginner. A sentence, code block, danger box, "shows …", or "by the end" claim that does not deliver is a lie. Flag it. Fix it. A softer sentence is not a fix.

Fat-tailed `.. meta::` text is for beginners and LLMs. Check it against the opening, the review, and the final code.

## Evidence

- Read the file and reproduce the behavior before changing it. Comments, docs, and a summary of the problem are claims to check.
- Confidence under 80, stop before any edit to chapter text, code windows, quotes, danger boxes, or published meta. Ask. An assumption may appear in the report. It must not be written into the chapter.
- An author instruction about taste or intentional pedagogy stands. A checked runtime fact still wins. Flag a quote that does not match Python before rewriting it.

## Routing

- Any edit under `source/` loads `notes/proofread-chapter-prompt.md` before the file is written. That prompt owns the chapter checklist, review voice, and mechanical checks. Do not copy them here.
- Before saving a chapter `.rst`, run `python3 tools/check_chapter_rst.py` on that file. It must exit 0.
- Load `notes/general-critique-protocol.md` only when the user asked for a critique. Chapter prose follows the proofread prompt, not the harsh-critique stance.
- One-off content bug: fix the content. Add a checklist bullet only when the same miss recurs or the payoff is obvious. Append `notes/chapter-review-log.md` after a completed chapter review. Do not load the ledger on startup.
- Data-structure chapters live under `source/basic_objects/`.
