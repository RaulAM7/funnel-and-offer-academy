# Initial Context Report — 2026-03-21

## What was built
- BRIEF.md: Definido que es el repo (academia + laboratorio + cantera), para quien (usuario en ecosistema EduKami/Reboot/Skilland), outcome (metodologia propia + activos operativos), horizonte (largo plazo), criterios de exito (6 puntos concretos).
- FACTS.md: 27 hechos verificables extraidos de 10 ficheros fuente, organizados por dominio (Offer Design, Course Design, Funnel Design, Narrative, Validacion, Teoria Unificada, Contexto Repo). Cada hecho con source y confidence. Seccion de 6 unknowns/assumptions.
- CONSTRAINTS.md: 8 non-negotiables explicitos del repo. Budget y time marcados como Not stated. Tooling = docs-first.
- LINKS.md: 8 URLs encontradas en las fuentes con nota de relevancia.
- GLOSSARY.md: 23 terminos de dominio definidos, organizados por autor/sistema (Hormozi, Brunson, Valdo, Unificado).
- backlog.md: 10 items [inferred] anadidos, cubriendo destilacion por obra, sintesis transversal, itinerario y primer borrador de metodologia.
- decisions.md: 6 decisiones [inferred] registradas: prioridad funnels, scope dual, docs-first, boundary NotebookLM, metodologia propia, Funnel OS como referencia inicial.

## Gaps and unknowns
- No hay presupuesto ni restricciones temporales definidos — no bloquea el arranque pero impide planificacion de sprints.
- No hay baseline del estado actual de los sistemas downstream (Sales OS, Agentic Business OS) — bloqueara la fase de operacionalizacion cuando llegue.
- No se define el nivel de profundidad esperado en destilacion antes de pasar a operacionalizacion — necesita decision explicita cuando se escriba el primer spec.
- No hay ejemplos concretos de funnels u offers activos del usuario como referencia — limita la personalizacion de la metodologia.
- No queda claro si el corpus de 10 ficheros es todo el material inicial o si hay mas en NotebookLM u otros sitios.
- Falta definir quien mas (si alguien) consumira los outputs de este repo ademas del usuario.

## Conflicts found
- Hormozi y Brunson usan "Big Domino" con matices distintos. Hormozi lo aplica a cursos (el unico shift que desbloquea la transformacion). Brunson lo aplica a ventas (la creencia unica que tumba todas las objeciones). Resolucion: ambos usos documentados en GLOSSARY.md como entradas separadas. El Funnel OS unificado los trata como complementarios, no contradictorios.
- No se encontraron conflictos factuales entre fuentes. La teoria unificada (hormozi_and_russell_teoria_unificada.md) ya resuelve la integracion entre autores.

## Suggested next action
Resolver los 2-3 unknowns mas relevantes (nivel de profundidad de destilacion, completitud del corpus inicial) y luego ejecutar write-spec para la primera tarea del backlog: destilar Russell Brunson — DotCom Secrets.
