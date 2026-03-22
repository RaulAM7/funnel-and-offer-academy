# Funnel & Offer Design Academy

> Si estructuras bien ofertas, mensajes, funnels y conversion, dejas de tener una web que "existe" y pasas a tener un sistema comercial que escala.

---

## De que va esto

Este repo existe porque hay una diferencia enorme entre **consumir contenido** sobre funnels y offers y **convertir ese contenido en un sistema que funcione**.

La mayoria de gente lee a Brunson, a Hormozi, a los referentes del sector, y se queda en:
- resúmenes que no se usan
- notas que se pierden
- ideas sueltas que no conectan entre si

Este repo hace lo contrario. Es un **motor de transformacion de conocimiento**:
- estudia obras de referencia de forma sistematica
- extrae lo que realmente importa
- lo estructura en activos reutilizables
- y lo eleva progresivamente hacia una metodologia propia

No es una biblioteca. No es una coleccion de resumenes.
Es una academia interna donde Claude Code gestiona la complejidad y el usuario se centra en estudiar y pensar.

---

## La tesis de fondo

El punto de partida viene de DotCom Secrets, pero aplica a todo el repo:

**Mejor arquitectura comercial = mas ingresos, mas escalabilidad, mas capacidad de servir.**

Eso se consigue dominando cinco cosas:

```text
1. Estructurar productos y servicios       → ganar mas con el mismo trafico
2. Comunicar para que el cliente ascienda   → mas valor percibido, mas ventas
3. Disenar funnels por fases                → sistema, no paginas sueltas
4. Usar building blocks y funnels probados  → frameworks > improvisacion
5. Aplicar scripts de conversion            → vender en cada etapa del recorrido
```

El resultado final: **la empresa pasa de tener presencia online a tener una maquina de ventas y marketing escalable.**

---

## Que produce este repo

No outputs abstractos. Activos concretos:

- **Extracciones estructuradas** por bloque de estudio: insights, principios, playbooks, patrones, ejemplos
- **Sintesis de obra** que destilan lo esencial de cada libro
- **Sintesis de dominio** que cruzan varias obras y detectan convergencias
- **Catalogo de blueprints** con funnel types, layouts y configuraciones normalizadas
- **Metodo interno** que emerge del cruce de todo lo anterior

Cada pieza tiene trazabilidad: se sabe de donde viene, con que confianza y para que sirve.

---

## Principios de trabajo

- `Destilacion > acumulacion` — no interesa guardar mucho; interesa guardar bien
- `Activos > resumenes` — la unidad de valor es el activo generado, no el libro leido
- `Metodo propio > lealtad al autor` — los autores son insumo, no destino
- `El usuario estudia, Claude gestiona` — la complejidad estructural la absorbe el sistema
- `Docs-first` — primero claridad conceptual; tooling solo si hace falta

---

## Dominios

| Dominio | Foco | Corpus principal |
|---------|------|------------------|
| **Funnels** | arquitectura comercial, conversion, escalado | Russell Brunson (DotCom Secrets, Expert Secrets, Traffic Secrets) |
| **Offers** | diseno de oferta, pricing, packaging, valor | Alex Hormozi ($100M Offers, $100M Leads) |

---

## Estado actual

- **Modulo activo**: Academy
- **Dominio**: funnels
- **Libro**: DotCom Secrets (Russell Brunson)
- **Progreso**: 1/5 bloques completados
- **Blueprint catalog**: activado, vacio (los funnel types concretos llegan en bloques 03-05)
- **Punto de control vivo**: `04_outputs/academy/STATE.md`

---

## Estructura del repo

```text
00_inbox/        material crudo de entrada (libros, fuentes, PDFs convertidos)
01_harness/      reglas globales, stack, taskflow, indice de skills
02_context/      memoria destilada del proyecto (BRIEF, FACTS, CONSTRAINTS, GLOSSARY)
03_specs/        spec activa, backlog y decisiones
04_outputs/      entregables finales — aqui vive el modulo Academy
05_scratch/      trabajo intermedio y descartes utiles
shared/          agentes y skills reutilizables
runners/         notas para operar con agentes externos
```

### Arbol del modulo Academy

```text
04_outputs/academy/
├── STATE.md                          ← estado vivo del modulo
├── INTERACTION-DESIGN.md             ← como funciona la interaccion usuario-Claude
├── funnels/
│   └── russell-brunson/
│       ├── dotcom-secrets/
│       │   ├── 01_map/               ← que es el libro, estructura, posicion en el corpus
│       │   ├── 02_itinerary/         ← bloques de estudio, secuencia, densidad
│       │   ├── 03_blocks/            ← resumen + canvas por bloque
│       │   ├── 04_extraction/        ← extraccion estructurada por bloque
│       │   └── 05_synthesis/         ← sintesis de la obra completa
│       ├── blueprint-catalog/        ← catalogo normalizado de funnel types
│       ├── cross-work-synthesis/     ← cruce entre libros del mismo autor
│       └── internal-method/          ← metodo interno emergente
└── offers/
    └── alex-hormozi/
        ├── cross-work-synthesis/
        └── internal-method/
```

---

## Agentes y skills

### Sistema base del harness
- **Agentes**: `distiller`, `planner`, `prospector`, `maker`, `reviewer`
- **Skills**: `initial-context-building`, `distill-context`, `write-spec`, `ship-output`, `qa-review`

### Especificos de Academy
- **Agentes**: `academy-orchestrator`, `study-distiller`, `method-synthesizer`, `blueprint-cataloger`, `visual-editor`
- **Skills**: `manage-academy-cycle`, `build-study-itinerary`, `distill-study-block`, `visualize-study-block`, `synthesize-book`, `synthesize-domain`, `catalog-blueprints`

Indice completo: `01_harness/SKILLS_INDEX.md`

---

## Como se usa

### Si acabas de abrir el repo

Lee en este orden:
1. `01_harness/RULES.md`
2. `01_harness/STACK.md`
3. `01_harness/TASKFLOW.md`
4. `02_context/BRIEF.md`

### Si vas a continuar el modulo Academy

1. `04_outputs/academy/STATE.md` — donde estamos
2. `04_outputs/academy/INTERACTION-DESIGN.md` — como funciona
3. Di algo como "sigamos", "donde lo dejamos" o "vamos con el siguiente bloque"

### Frases que el sistema entiende

| Dices | Pasa |
|-------|------|
| "sigamos" / "donde lo dejamos" | Lee estado, reporta posicion, propone siguiente paso |
| "vamos con el siguiente bloque" | Procesa el bloque que toca |
| "como vamos" | Muestra progreso |
| "cataloga los blueprints" | Normaliza funnel types detectados en las extracciones |
| "sintetiza el libro" | Lanza sintesis de la obra |

---

## Flujo de trabajo general del repo

```text
1. Seed      → material crudo en 00_inbox/
2. Distill   → contexto estable en 02_context/
3. Spec      → una sola spec activa en 03_specs/now/
4. Ship      → outputs finales en 04_outputs/
5. QA        → verificacion contra criterios de aceptacion
```

---

## Que no debe pasar

- No usar `00_inbox/` como archivo permanente
- No trabajar varias specs activas a la vez
- No convertir el repo en biblioteca muerta o coleccion de resumenes
- No mezclar exploracion live con memoria persistente
- No auto-avanzar sin confirmacion del usuario

---

## En una frase

Este repo convierte estudio serio de funnels y offers en metodologia propia y activos operativos reutilizables, con un sistema donde **el usuario estudia y Claude gestiona**.
