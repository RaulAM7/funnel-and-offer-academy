# DECISIONS

Short decision log.

- 2026-03-01: Decision template initialized. Status: pending
- 2026-03-21: [inferred] Prioridad inicial practica: funnels primero, offers despues. Razon: el usuario percibe mas madurez previa en offer design y quiere profundizar en funnels. Source: what-is-this-repo-aboit.md
- 2026-03-21: [inferred] Scope dual desde el inicio: el repo cubre tanto offer design como funnel design, aunque se trabaje uno primero. Source: what-is-this-repo-aboit.md
- 2026-03-21: [inferred] Docs-first: no se introduce codigo ni implementacion tecnica hasta que haya claridad conceptual y metodologica. Source: what-is-this-repo-aboit.md, STACK.md
- 2026-03-21: [inferred] NotebookLM como herramienta complementaria, no sustitutiva. NotebookLM = exploracion live. Repo = consolidacion persistente. No todo lo de NLM entra al repo. Source: what-is-this-repo-aboit.md
- 2026-03-21: [inferred] Metodologia propia como objetivo final: los autores (Hormozi, Brunson, Valdo) son insumo, no destino. El repo debe construir un marco propio, mas compacto, accionable y alineado con el negocio del usuario. Source: what-is-this-repo-aboit.md
- 2026-03-21: [inferred] El Funnel OS 6.3 (teoria unificada) se adopta como modelo de referencia inicial para integrar las fuentes, sujeto a refinamiento conforme avance la destilacion. Source: hormozi_and_russell_teoria_unificada.md
- 2026-03-22: [decision] La capa visual de Academy se integra como paso opcional post-distilacion, sugerido pero nunca autoejecutado. Source: user direction + 04_outputs/academy/INTERACTION-DESIGN.md
- 2026-03-22: [decision] Excalidraw MCP se adopta como runtime primario de visualizacion a nivel proyecto mediante `.mcp.json`, con fallback local a `.excalidraw`. Source: user direction + Anthropic MCP docs + yctimlin/mcp_excalidraw docs
- 2026-03-22: [decision] Cada bloque visualizado tiene un canvas maestro persistente en `03_blocks/block-NN/block-NN_canvas.excalidraw`. Source: user direction
