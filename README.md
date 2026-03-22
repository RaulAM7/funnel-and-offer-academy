# Funnel & Offer Academy

Repositorio `docs-first` para aprendizaje aplicado, destilacion metodologica y produccion de activos operativos sobre `offer design` y `funnel design`.

No es un proyecto de software tradicional. Es una combinacion de:
- academia interna
- laboratorio de I+D
- cantera de skills y agentes
- memoria persistente de trabajo

La idea central es simple: estudiar buenas fuentes, destilar valor real, convertirlo en metodologia propia y traducirlo a activos reutilizables.

## Que resuelve este repo

- Ordena estudio y destilacion de obras base de Alex Hormozi, Russell Brunson y otras referencias.
- Evita que el conocimiento se quede en resumentitis, notas sueltas o consumo pasivo.
- Convierte aprendizaje en outputs operativos: skills, agentes, playbooks, blueprints, workflows.
- Alimenta sistemas downstream del ecosistema EduKami / Reboot Academy / Skilland.

## Principios de trabajo

- `Distillation > accumulation`: no interesa guardar mucho; interesa guardar bien.
- `Assets > summaries`: la unidad de valor es el activo generado, no el libro leido.
- `Own method > author loyalty`: los autores son insumo, no destino.
- `NotebookLM = exploracion`, `repo = memoria persistente y produccion`.
- `Docs-first`: primero claridad conceptual, estructura y metodo; luego tooling o runtime si hace falta.

## Estado actual

- Modulo activo: `Academy`
- Dominio activo: `funnels`
- Autor activo: `Russell Brunson`
- Libro activo: `DotCom Secrets`
- Estado del libro: `1/5` bloques completados
- Siguiente paso sugerido: empezar `block-02 (Communication Funnel)`

Punto de control vivo:
- `04_outputs/academy/STATE.md`

## Como esta organizado

```text
00_inbox/       material crudo de entrada
01_harness/     reglas globales, stack y taskflow
02_context/     memoria destilada del proyecto
03_specs/       spec activa, backlog y decisiones
04_outputs/     entregables finales
05_scratch/     trabajo intermedio y descartes utiles
shared/         agentes y skills reutilizables
runners/        notas cortas para operar con agentes
```

## Flujo de trabajo del repo

El repo sigue una secuencia fija:

1. `Seed`
   Mete material crudo en `00_inbox/`.
2. `Distill`
   Convierte ese material en contexto estable dentro de `02_context/`.
3. `Spec`
   Trabaja desde una sola spec activa en `03_specs/now/`.
4. `Ship`
   Genera outputs finales en `04_outputs/`.
5. `QA`
   Verifica criterios de aceptacion, unknowns, riesgos y siguiente paso.

Documentos base que hay que leer antes de operar:
- `01_harness/RULES.md`
- `01_harness/STACK.md`
- `01_harness/TASKFLOW.md`

## Mapa operativo rapido

### 1. Si acabas de abrir el repo

Lee en este orden:

1. `01_harness/RULES.md`
2. `01_harness/STACK.md`
3. `01_harness/TASKFLOW.md`
4. `02_context/BRIEF.md`
5. `02_context/FACTS.md`
6. `02_context/CONSTRAINTS.md`
7. `03_specs/now/001_now.md`

### 2. Si vas a continuar trabajo del modulo Academy

Empieza aqui:

1. `04_outputs/academy/STATE.md`
2. `04_outputs/academy/INTERACTION-DESIGN.md`
3. `04_outputs/academy/funnels/russell-brunson/dotcom-secrets/02_itinerary/itinerary.md`
4. El source correspondiente en `00_inbox/`

### 3. Si vas a producir algo nuevo

- Usa una sola spec activa.
- Carga solo la skill necesaria desde `shared/skills/`.
- Escribe el entregable final en `04_outputs/`.
- Deja borradores o residuos de trabajo en `05_scratch/`.

## Contexto estable del proyecto

`02_context/` concentra la memoria util del sistema:

- `BRIEF.md`: que es este repo, para quien es y como se mide el exito
- `FACTS.md`: hechos verificados y nivel de confianza
- `CONSTRAINTS.md`: limites y no-negociables
- `GLOSSARY.md`: terminos del dominio
- `LINKS.md`: referencias externas

Esto debe seguir siendo legible en pocos minutos. No es un segundo inbox.

## Modulo Academy

El modulo Academy convierte una obra de referencia en conocimiento estructurado por bloques y luego lo eleva hacia metodologia propia.

Ahora mismo ya existen:

- Infraestructura base del modulo
- `STATE.md` para continuidad entre sesiones
- mapa e itinerario inicial de `DotCom Secrets`
- primer bloque destilado y su extraccion
- agentes y skills especificos para el ciclo de estudio

Ruta actual del trabajo activo:

```text
04_outputs/academy/funnels/russell-brunson/dotcom-secrets/
├── 01_map/
├── 02_itinerary/
├── 03_blocks/
├── 04_extraction/
└── 05_synthesis/
```

## Agentes y skills disponibles

Base del harness:
- Agentes: `distiller`, `planner`, `prospector`, `maker`, `reviewer`
- Skills: `initial-context-building`, `distill-context`, `write-spec`, `ship-output`, `qa-review`

Especificos de Academy:
- Agentes: `academy-orchestrator`, `study-distiller`, `method-synthesizer`
- Skills: `manage-academy-cycle`, `build-study-itinerary`, `distill-study-block`, `synthesize-book`, `synthesize-domain`

Indice rapido:
- `01_harness/SKILLS_INDEX.md`

## Que no debe pasar

- No usar `00_inbox/` como archivo permanente.
- No copiar material crudo a working files sin destilarlo.
- No trabajar varias specs activas a la vez.
- No convertir el repo en biblioteca muerta o coleccion de resumenes.
- No mezclar exploracion live con memoria persistente.

## Entradas utiles

- Instrucciones para agentes: `AGENTS.md`
- Runner Codex: `runners/codex.md`
- Runner Claude: `runners/claude.md`
- Diseno fundacional del modulo: `04_outputs/academy/academy-module-foundational-design.md`

## Resumen en una frase

Este repo existe para convertir estudio serio de offers y funnels en metodologia propia y activos operativos reutilizables, con un flujo disciplinado de `inbox -> context -> spec -> output -> QA`.
