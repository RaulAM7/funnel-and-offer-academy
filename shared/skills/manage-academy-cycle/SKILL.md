---
name: manage-academy-cycle
description: Manage the Academy module lifecycle -- read state, decide next step, update progress, maintain session continuity, and route work. Use whenever entering the Academy module, checking progress, starting a session, or handling any "where are we" / "what's next" / "sigamos" interaction.
---

# Goal
Keep the Academy module self-managing so the user never carries management burden.

# Inputs
- `04_outputs/academy/STATE.md` (primary)
- `04_outputs/academy/` directory tree (to verify file existence matches state)

# Outputs
- Updated `04_outputs/academy/STATE.md` after every meaningful action

# Procedure

## On session entry
1. Read `04_outputs/academy/STATE.md`.
2. Verify state matches reality (files exist where state says they should).
3. Determine current position: domain, author, book, phase, block.
4. Compose a concise status report for the user: where we are, what was done last, what the recommended next step is.
5. Wait for user direction. Do not auto-advance without confirmation.

## On block completion
6. Update the block's row in the Progress table (status, date, notes).
7. Increment blocks_completed in YAML frontmatter.
8. Determine if this was the last block. If so, recommend book synthesis.
9. Log the session entry.
10. Report what was done and what comes next.

## On phase transition
11. Update active_phase in YAML frontmatter.
12. If transitioning to book-synthesis: verify sufficient blocks are complete.
13. If transitioning to domain-synthesis: verify at least 2 books synthesized.
14. Log the transition in Session Log.

## On new book entry
15. Create the book's folder structure (01_map through 05_synthesis).
16. Add the book to the Books Tracker table.
17. Set active_book, reset active_block and blocks_completed.
18. Route to build-study-itinerary to create the itinerary.

## Bootstrap (STATE.md does not exist)
19. Create STATE.md from template.
20. Scaffold the initial folder structure.
21. Route to the first book's map creation and itinerary building.

# Anti-patterns
- Asking the user "where were we?" -- always read STATE.md.
- Updating state without verifying that the referenced files actually exist.
- Auto-advancing through multiple blocks without user confirmation.
- Writing verbose session log entries. Keep them to one line each.
