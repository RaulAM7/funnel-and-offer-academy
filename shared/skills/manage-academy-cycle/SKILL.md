---
name: manage-academy-cycle
description: Manage the Academy module lifecycle -- read state, decide next step, update progress, maintain session continuity, and route work. Use whenever entering the Academy module, checking progress, starting a session, or handling any "where are we" / "what's next" / "sigamos" interaction.
---

# Goal
Keep the Academy module self-managing so the user never carries management burden.

# Inputs
- `04_outputs/academy/STATE.md` (primary)
- `04_outputs/academy/` directory tree (to verify file existence matches state)
- Block summary files in `03_blocks/` when visual status or candidacy needs verification
- Blueprint catalog index at `04_outputs/academy/[domain]/[author]/blueprint-catalog/catalog-index.md` (when checking catalog state)

# Outputs
- Updated `04_outputs/academy/STATE.md` after every meaningful action

# Procedure

## On session entry
1. Read `04_outputs/academy/STATE.md`.
2. Verify state matches reality (files exist where state says they should).
3. Determine current position: domain, author, book, phase, block.
4. Compose a concise status report for the user: where we are, what was done last, what the recommended next step is.
5. If the most recent completed block is a visual candidate and has no canvas yet, you may suggest the visual step once.
6. Wait for user direction. Do not auto-advance without confirmation.

## On block completion
7. Update the block's row in the Progress table (status, date, notes).
8. Set the block visual status to `no` unless a canvas already exists.
9. Increment blocks_completed in YAML frontmatter.
10. Check if the completed block's extraction file contains a `## Blueprint Candidates` section. If so, note it in the status report and include "blueprint cataloging available" in the recommended next steps (after visual, before next block).
11. Determine if this was the last block. If so, recommend book synthesis.
12. Log the session entry.
13. Report what was done and what comes next.

## On visual action
14. Verify the target block files exist.
15. If a canvas was created, set visual status to `draft`.
16. If a canvas was revised and accepted, set visual status to `reviewed`.
17. Add a concise session log entry.
18. Keep the recommended next step aligned with the user flow: review canvas if draft, otherwise continue the book.

## On phase transition
19. Update active_phase in YAML frontmatter.
20. If transitioning to book-synthesis: verify sufficient blocks are complete. Include a note about how many blueprint catalog entries exist and whether any are still draft.
21. If transitioning to domain-synthesis: verify at least 2 books synthesized.
22. Log the transition in Session Log.

## On new book entry
23. Create the book's folder structure (01_map through 05_synthesis).
24. Add the book to the Books Tracker table.
25. Set active_book, reset active_block and blocks_completed.
26. Route to build-study-itinerary to create the itinerary.

## Bootstrap (STATE.md does not exist)
27. Create STATE.md from template.
28. Scaffold the initial folder structure.
29. Route to the first book's map creation and itinerary building.

# Anti-patterns
- Asking the user "where were we?" -- always read STATE.md.
- Updating state without verifying that the referenced files actually exist.
- Auto-advancing through multiple blocks without user confirmation.
- Auto-running visualization because the block looks dense. Suggest it, do not assume it.
- Writing verbose session log entries. Keep them to one line each.
