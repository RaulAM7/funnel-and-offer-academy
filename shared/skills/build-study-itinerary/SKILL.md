---
name: build-study-itinerary
description: Design a study itinerary for a book -- divide it into logical blocks, define sequence, estimate scope. Use when starting a new book in the Academy or when the user asks to plan how a book will be studied.
---

# Goal
Produce a clear, reasonable study itinerary that breaks a book into workable blocks.

# Inputs
- The source file in `00_inbox/` for the book
- `04_outputs/academy/[domain]/[author]/[book]/01_map/book-map.md` (if it exists)

# Outputs
- `04_outputs/academy/[domain]/[author]/[book]/02_itinerary/itinerary.md`
- Update to STATE.md (blocks_total set, block rows added to Progress table)

# Procedure

1. Read the book's table of contents and overall structure from the source file.
2. If a book-map exists, read it for additional context.
3. Group chapters/sections into 4-7 blocks. Grouping criteria:
   - Thematic coherence (chapters that cover one conceptual area)
   - Manageable scope (each block workable in one study session)
   - Dependency awareness (do not split tightly coupled chapters)
4. For each block, define:
   - Block number and short descriptor
   - Which chapters/sections it includes
   - What the block covers (1-2 sentences)
   - Estimated density: light | medium | heavy
   - Dependencies on prior blocks (if any)
5. Write the itinerary file with this structure:

```
# Study Itinerary -- [Book Title]

> Author: [name]
> Domain: [funnels/offers]
> Source: 00_inbox/[filename]
> Blocks: [N]
> Created: YYYY-MM-DD

## Block Sequence

### Block 01 -- [Descriptor]
- Chapters: [list]
- Covers: [1-2 sentences]
- Density: light | medium | heavy
- Depends on: none | block-NN

### Block 02 -- [Descriptor]
...

## Study Notes
- [Any notes about recommended order, optional sections, etc.]
```

6. Update STATE.md: set blocks_total, add block rows to the Progress table.

# Anti-patterns
- Making too many small blocks (more than 7). Consolidate.
- Making blocks so large they cannot be worked in one session.
- Splitting a single cohesive concept across two blocks.
