---
name: catalog-blueprints
description: Normalize funnel blueprints from extraction files into the author-level blueprint catalog. Use when blueprint candidates are flagged in extractions, when the user asks to catalog, or when validating existing entries against new sources. Funnels domain only for now.
---

# Goal
Transform blueprint candidates from extraction files into normalized, comparable catalog entries.

# Inputs
- Extraction files in `04_extraction/` (specifically `## Blueprint Candidates` and `## Patterns` sections)
- Existing catalog at `04_outputs/academy/[domain]/[author]/blueprint-catalog/`
- `04_outputs/academy/STATE.md`

# Outputs
- New or updated blueprint files at `04_outputs/academy/[domain]/[author]/blueprint-catalog/bp-NN_short-name.md`
- Updated `04_outputs/academy/[domain]/[author]/blueprint-catalog/catalog-index.md`

# Procedure

1. Read `STATE.md` to identify active domain, author, and book context.
2. Read `catalog-index.md` if it exists to know what is already cataloged.
3. Read the relevant extraction file(s) -- focus on `## Blueprint Candidates`, `## Patterns`, and `## Playbooks` sections for blueprint-worthy content.
4. For each candidate, determine if it qualifies as a blueprint:
   - YES if it describes a concrete funnel architecture, layout, sequence, or configuration with identifiable components and flow
   - NO if it is an abstract principle, general insight, or heuristic without structural specificity
5. For qualifying candidates, check the existing catalog for duplicates or matches:
   - If a matching entry exists and has the same source: skip
   - If a matching entry exists with a different source: update the existing entry -- add source, potentially upgrade from `draft` to `validated`
   - If no match: create a new entry
6. Write each new blueprint entry following the template in `blueprint-catalog/FICHA-TEMPLATE.md`. Key sections:

```markdown
# Blueprint: [Name]

> Type: [funnel-type | layout | sequence | configuration]
> Status: draft | validated
> Confidence: stated | inferred | hypothesis
> Created: YYYY-MM-DD
> Updated: YYYY-MM-DD

## Descripcion
[2-4 sentences: what this blueprint is and what it achieves]

## Cuando usar
[1-3 bullets: conditions or scenarios where this blueprint applies]

## Componentes / Etapas
[Numbered list: **Component name** — what it does in the funnel]

## Flujo visual
[Mermaid diagram (graph TD or graph LR) showing the user journey through the funnel.
Each node must correspond to a component listed above. Max 12 nodes.
This diagram is the structural source for later Excalidraw canvas generation.]

## Mecanica clave
[1-3 bullets: why this funnel works, the structural trick, the principle behind it]

## Variantes conocidas
[List variants or "Ninguna documentada aun."]

## Blueprints relacionados
[List related catalog entries or "Ninguno identificado aun."]

## Fuentes
| Libro | Bloque | Confianza | Notas |
|-------|--------|-----------|-------|
| [book] | [block] | [tag] | [brief note] |

## Visual status
> Canvas: pendiente | draft | reviewed
> Archivo: bp-NN_short-name_canvas.excalidraw
```

7. Update `catalog-index.md` after every action. The index uses this structure:

```markdown
# Catalogo de Blueprints -- [Author]

> Domain: [domain]
> Author: [author]
> Entries: [N]
> Last updated: YYYY-MM-DD

## Indice

| # | Blueprint | Tipo | Status | Fuente(s) | Fecha |
|---|-----------|------|--------|-----------|-------|
| 01 | [Name](bp-01_short-name.md) | funnel-type | draft | DotCom Secrets B04 | YYYY-MM-DD |

## Resumen
- Entries totales: N
- Draft: N
- Validated: N
```

8. Update the `## Catalogo de Blueprints` section in `STATE.md` with current counts.
9. Maximum 80 lines per blueprint entry (excluding the mermaid block).
10. The mermaid diagram must use `graph TD` for linear funnels or `graph LR` for branching flows. Max 12 nodes. Each node must map to a component in `## Componentes / Etapas`.
11. Always set `## Visual status` to `Canvas: pendiente` on new entries -- the visual-editor handles canvas creation later.
12. Write all user-facing content in Spanish; keep funnel type names and framework names in original English.

# Anti-patterns
- Cataloging abstract principles. This is for concrete funnel architectures only.
- Creating duplicate entries for the same funnel type from the same source.
- Marking entries as `validated` without multi-source confirmation.
- Exceeding 80 lines per entry (excluding mermaid). Blueprints should be scannable reference cards, not essays.
- Mermaid diagrams with more than 12 nodes. Split into sub-diagrams if needed.
- Mermaid nodes that don't match the components list. They must be 1:1.
- Cataloging before the extraction exists. Always work from completed extractions.
