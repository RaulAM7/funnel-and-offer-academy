---
name: visualize-study-block
description: Create, review, and refine Excalidraw canvases for Academy study blocks after markdown distillation is done. Use when the user asks to visualize a block, make a canvas, review a canvas, or apply revisions to an existing canvas.
---

# Goal
Turn a distilled study block into a recall-oriented visual canvas that is easier to consume than raw markdown.

# Inputs
- `04_outputs/academy/STATE.md`
- `04_outputs/academy/[domain]/[author]/[book]/03_blocks/block-NN/*.md`
- `04_outputs/academy/[domain]/[author]/[book]/04_extraction/extraction-block-NN.md`
- Existing `block-NN_canvas.excalidraw` if present

# Outputs
- `04_outputs/academy/[domain]/[author]/[book]/03_blocks/block-NN/block-NN_canvas.excalidraw`

# Procedure

1. Read `STATE.md` first and confirm the active book/block matches the user request.
2. Read the block summary and extraction before touching any canvas. The markdown remains the semantic source.
3. Decide the mode:
   - `create`: no canvas exists yet
   - `review`: canvas exists and the user asked to inspect or improve it
   - `apply-revision`: canvas exists and the user explicitly asked to change it
4. Prefer the project MCP setup in `.mcp.json` for live Excalidraw work. Read `references/mcp-setup.md` only if setup details are needed.
5. If the MCP canvas is unavailable, use `scripts/build_canvas.py` as the file-based fallback to generate or refresh a draft canvas.
6. Optimize the visual for recall, not decoration:
   - one frame or cluster per major framework
   - short labels, clear hierarchy, obvious relationships
   - include principles, playbooks, risks, and tensions only when they help orientation
7. Save a single master artifact: `block-NN_canvas.excalidraw`.
8. If you are in `review` mode, do not overwrite the canvas by default. Return a concise review and wait for an explicit request to apply changes.
9. After any create or apply action, update `STATE.md` visual status for that block and add a one-line session log entry.

# Anti-patterns
- Treating the canvas as a prettier summary. The canvas should reorganize the block spatially.
- Auto-overwriting an existing canvas on a generic "visualiza" request.
- Mixing multiple blocks into the same visual artifact.
- Adding decorative clutter that does not improve recall.
- Letting the canvas drift from the markdown without calling out the mismatch.
