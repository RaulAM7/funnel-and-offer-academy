---
name: synthesize-book
description: Close and consolidate a book after its blocks have been studied. Read all extraction files, identify the book's core contributions, and produce a book synthesis document.
---

# Goal
Produce a single synthesis document that captures what the book truly contributes.

# Inputs
- All extraction files in `04_extraction/`
- All block summaries in `03_blocks/`
- The book map in `01_map/book-map.md`
- The itinerary in `02_itinerary/itinerary.md`

# Outputs
- `04_outputs/academy/[domain]/[author]/[book]/05_synthesis/book-synthesis.md`

# Procedure

1. Read all extraction files and block summaries.
2. Read the book map for the book's stated purpose and structure.
3. Identify:
   - The book's core thesis (1-3 sentences)
   - Its most valuable frameworks (max 5)
   - Its most actionable playbooks (max 5)
   - Recurring patterns across blocks
   - Its distinctive contribution vs common knowledge
   - Its limitations or blind spots
4. Consolidate elevation candidates from all extraction files.
5. Write the synthesis with this structure:

```
# Book Synthesis -- [Title]

> Author: [name]
> Domain: [domain]
> Blocks studied: N/N
> Synthesis date: YYYY-MM-DD

## Core Thesis

## Key Frameworks
| Framework | What it does | Source block |

## Key Playbooks
| Playbook | When to use | Source block |

## Patterns Detected

## Distinctive Contribution

## Limitations

## Elevation Recommendations

## Changelog
| Date | Action |
```

6. Maximum 300 lines.
7. Write all user-facing content in Spanish; keep framework names in original English.

# Anti-patterns
- Synthesizing before enough blocks are done. Require at least 80%.
- Producing a summary instead of a synthesis. Synthesis identifies patterns and contributions; summaries just compress.
- Exceeding 300 lines. This is a reference document, not a new book.
