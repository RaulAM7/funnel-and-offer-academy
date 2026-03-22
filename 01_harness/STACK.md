# STACK

Default: docs-first workspace with light utility tooling.

If code is introduced later, track here:
- Runtime/framework: Python 3 utility scripts for local Excalidraw fallback generation; Docker-hosted Excalidraw MCP + canvas for live visual editing.
- Project layout conventions: visual tooling lives under `shared/skills/visualize-study-block/`; master canvases live beside each studied block in `03_blocks/block-NN/`.
- Build/test/dev commands:
  - `bash shared/skills/visualize-study-block/scripts/start_canvas.sh`
  - `python3 shared/skills/visualize-study-block/scripts/build_canvas.py --summary <summary.md> --extraction <extraction.md> --output <canvas.excalidraw>`
  - `python3 -m json.tool .mcp.json`
