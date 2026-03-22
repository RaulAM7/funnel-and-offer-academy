# Excalidraw MCP Setup

- Project MCP config lives in `.mcp.json`.
- The MCP server is Docker-based and expects the live canvas at `http://localhost:3000`.
- To start the canvas server, run:
  - `bash shared/skills/visualize-study-block/scripts/start_canvas.sh`
- If the MCP server or live canvas is unavailable, use the fallback generator:
  - `python3 shared/skills/visualize-study-block/scripts/build_canvas.py --summary <summary.md> --extraction <extraction.md> --output <block_canvas.excalidraw>`
- The fallback is for draft creation and deterministic refreshes. Prefer MCP for iterative editing when it is available.
