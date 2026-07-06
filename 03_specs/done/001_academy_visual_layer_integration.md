# 001_now — Academy Visual Layer Integration

## Closure Note — 2026-07-04
- Status: closed after material verification in HomeLab block/spec 007.
- Scope closed: visual layer integration only.
- This does **not** close the `academy` module; Academy remains live in `04_outputs/academy/STATE.md` and its continuity stays separate from this spec.
- `ia-mujeres-funnel` remains in handoff logic and is not reopened by this closure.

## Outcome
- The Academy module supports an on-demand visual layer after markdown distillation: state, UX, skills, agents, MCP config, and block-01 pilot canvas are all integrated.

## Scope
- In scope: `visualize-study-block` skill, `visual-editor` agent, `.mcp.json`, state tracking, workflow updates, fallback canvas generator, block-01 pilot canvas
- Out of scope: SaaS diagram providers, preview export assets, visualizing every historical block, cross-book canvas libraries

## Inputs
- Files: `04_outputs/academy/INTERACTION-DESIGN.md`, `04_outputs/academy/STATE.md`, `shared/skills/distill-study-block/SKILL.md`, block-01 markdown outputs
- Links: Anthropic Claude Code MCP docs, `yctimlin/mcp_excalidraw` docs
- Data: existing Academy agent and skill patterns

## Deliverable
- Path: multiple files across repo root, `shared/agents/`, `shared/skills/`, `04_outputs/academy/`, and block-01 output folder
- Format: AGENT.md and SKILL.md docs, project MCP config, lightweight scripts, markdown workflow updates, `.excalidraw` pilot canvas

## Acceptance Criteria
- [x] `.mcp.json` exists in project root with project-scoped Excalidraw MCP server config
- [x] `visualize-study-block` skill exists with create/review/apply guidance and fallback path
- [x] `visual-editor` agent exists with correct frontmatter and operating rules
- [x] Academy orchestration docs route visual requests and suggest visuals only on confirmation
- [x] `STATE.md` tracks per-block visual status and session continuity for visual actions
- [x] `INTERACTION-DESIGN.md` includes the optional post-distillation visual step
- [x] Block-01 markdown marks itself as a visual candidate
- [x] `block-01_canvas.excalidraw` exists as the first pilot canvas draft

## Risks and Edge Cases
- Risk: MCP server configured but canvas server not running — fallback file generation must keep the workflow unblocked
- Risk: future blocks may need more nuanced layouts than the deterministic fallback can provide
- Edge case: an existing canvas may drift from markdown — default repeated requests to review mode, not overwrite mode

## Open Questions
- Q1: none blocking for the v1 integration
