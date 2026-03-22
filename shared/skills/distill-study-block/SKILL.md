---
name: distill-study-block
description: Process one study block from a source book -- extract insights, principles, playbooks, patterns, and examples into structured output files. Use when studying a block or when the user says "vamos con el siguiente bloque" or similar.
---

# Goal
Transform one block of source material into structured, reusable knowledge.

# Inputs
- The source file in `00_inbox/` (read only the sections for the active block)
- The book's itinerary at `02_itinerary/itinerary.md` (to know block boundaries)
- Previous block extractions in `04_extraction/` (for continuity and cross-reference)

# Outputs
- `04_outputs/academy/[domain]/[author]/[book]/03_blocks/block-NN/block-NN_resumen.md`
- `04_outputs/academy/[domain]/[author]/[book]/04_extraction/extraction-block-NN.md`

# Procedure

1. Read the itinerary to identify which chapters/sections belong to this block.
2. Read the relevant section of the source file.
3. If prior extraction files exist, scan them briefly for continuity (avoid repeating already-extracted material).
4. Process the block material and extract into these categories:

## Extraction Categories

### Insights
Key ideas or concepts that carry genuine informational value.
Format: one bullet per insight, with brief explanation.

### Principles
Generalizable rules or heuristics the author states or implies.
Format: principle statement + context where it applies.

### Playbooks
Actionable sequences or recipes described in the text.
Format: name + steps + when to use.

### Examples
Concrete cases, stories, or scenarios the author uses to illustrate points.
Format: brief summary + what it demonstrates.

### Patterns
Recurring structures, templates, or blueprints that appear in the material.
Format: pattern name + components + use case.

### Limits and Doubts
Anything that seems questionable, contradictory, or context-dependent.
Format: what + why it is flagged.

### Elevation Candidates
Items that seem valuable enough to potentially warrant cross-work synthesis or method-level inclusion.
Format: what + why it might be elevated.

5. Write the block summary file (`03_blocks/block-NN/block-NN_resumen.md`):
   - 30-50 lines maximum
   - What the block covered, key takeaways, connection to prior blocks
   - End with `## Visual candidate`
   - Format: `Yes|No` + one-line reason about whether the block deserves a visual canvas
   - If a canvas already exists, mention it by file name in this section

6. Write the extraction file (`04_extraction/extraction-block-NN.md`):
   - Use the categories above as H2 sections
   - Omit empty categories rather than including empty sections
   - Maximum 200 lines per extraction
   - Each item tagged with confidence: stated | inferred | hypothesis
   - Write all user-facing content in Spanish; keep framework names in original English (e.g. Value Ladder, Attractive Character)

# Anti-patterns
- Summarizing instead of extracting. The goal is structured extraction, not paraphrase.
- Extracting everything. Only signal, not noise.
- Extraction files that exceed 200 lines. Compress or split.
- Ignoring prior blocks. Continuity matters.
- Inventing content not present in the source material.
- Forgetting to flag whether the block is worth visualizing.
