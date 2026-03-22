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
10. Determine if this was the last block. If so, recommend book synthesis.
11. Log the session entry.
12. Report what was done and what comes next.

## On visual action
13. Verify the target block files exist.
14. If a canvas was created, set visual status to `draft`.
15. If a canvas was revised and accepted, set visual status to `reviewed`.
16. Add a concise session log entry.
17. Keep the recommended next step aligned with the user flow: review canvas if draft, otherwise continue the book.

## On phase transition
18. Update active_phase in YAML frontmatter.
19. If transitioning to book-synthesis: verify sufficient blocks are complete.
20. If transitioning to domain-synthesis: verify at least 2 books synthesized.
21. Log the transition in Session Log.

## On new book entry
22. Create the book's folder structure (01_map through 05_synthesis).
23. Add the book to the Books Tracker table.
24. Set active_book, reset active_block and blocks_completed.
25. Route to build-study-itinerary to create the itinerary.

## Bootstrap (STATE.md does not exist)
26. Create STATE.md from template.
27. Scaffold the initial folder structure.
28. Route to the first book's map creation and itinerary building.

# Anti-patterns
- Asking the user "where were we?" -- always read STATE.md.
- Updating state without verifying that the referenced files actually exist.
- Auto-advancing through multiple blocks without user confirmation.
- Auto-running visualization because the block looks dense. Suggest it, do not assume it.
- Writing verbose session log entries. Keep them to one line each.
