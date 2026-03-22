# Academy Modular Foundation Learning

- Fecha: 2026-03-21
- Estado: diseño abstracto profundo del Módulo 1
- Naturaleza: documento fundacional para diseñar e implementar el módulo Academy dentro del repo
- Ámbito: arquitectura conceptual, lógica operativa, sistema de orquestación, agentes, skills, outputs y criterios de evolución
- Relación con el sistema: este documento desarrolla en profundidad el **Módulo 1** del repo general Funnel & Offer Design Academy
- Propósito inmediato: servir como contexto de alto valor para abrir una nueva conversación con Claude Code y planear la implementación concreta del módulo antes de empezar a estudiar el primer libro de Russell Brunson

---

# Qué es este documento

Este documento no es una spec técnica cerrada ni una implementación final.

Es un **documento fundacional de diseño abstracto** para el módulo Academy.  
Su función es darle a Claude Code una comprensión profunda de:

- qué debe ser este módulo,
- para qué existe,
- cómo debe funcionar,
- qué tipo de outputs debe producir,
- cómo debe autogestionarse,
- qué piezas conviene crear,
- y qué principios deben gobernar su implementación.

Este documento se sitúa un nivel por encima de la implementación.  
No busca todavía definir todos los nombres finales, todos los archivos exactos ni cada detalle operacional.  
Busca fijar correctamente el **modelo mental**, la **arquitectura conceptual** y la **lógica de funcionamiento**.

---

# Posición del módulo dentro del repo general

El repo completo Funnel & Offer Design Academy tiene tres grandes bloques lógicos:

1. **Academia / consumo de teoría / destilación de conocimiento**
2. **Cantera / traducción a assets operativos**
3. **Análisis de competencia / benchmark vivo / retroalimentación del sistema**

Este documento desarrolla el primero.

---

# Qué es exactamente el módulo Academy

El módulo Academy es el sistema del repo encargado de:

- estudiar sistemáticamente obras de referencia,
- convertirlas en conocimiento útil,
- procesarlas por bloques,
- extraer valor real,
- sintetizarlo,
- y elevarlo progresivamente hacia una metodología interna más compacta y accionable.

No es un repositorio de libros.  
No es una biblioteca de PDFs.  
No es un sistema de resúmenes superficiales.  
No es una carpeta con notas sueltas.

Es un **motor de transformación de fuentes en conocimiento estructurado**.

En una sola frase:

> El módulo Academy existe para transformar obras fuente de offer design y funnel design en conocimiento destilado, síntesis doctrinal y bases para una metodología interna futura.

---

# Qué problema resuelve el módulo Academy

Este módulo busca resolver varios problemas que el usuario tiene muy claros.

## 1. Evitar aprendizaje caótico

El usuario consume o quiere consumir material muy valioso, pero sin sistema ese aprendizaje se dispersa.

El módulo Academy debe convertir ese consumo en un recorrido ordenado y acumulativo.

## 2. Evitar evaporación del aprendizaje

Entender algo no basta.  
Hace falta que el sistema capture lo importante y lo convierta en artefactos reutilizables.

## 3. Evitar que todo quede pegado al autor original

El usuario quiere aprender de los mejores, pero no quiere quedar preso del framing de cada autor.  
Quiere poder destilar, comparar, sintetizar y construir un marco propio.

## 4. Evitar que el usuario cargue con la complejidad del sistema

El usuario no quiere ser el project manager del módulo.  
Quiere estudiar, pensar, reflexionar y conversar con el contenido.  
La gestión del módulo debe recaer en Claude Code.

## 5. Crear una base sólida para el resto del repo

Lo que nazca aquí alimentará más adelante:

- metodología interna,
- blueprints,
- catálogos,
- playbooks,
- y, en el futuro, skills, subagentes y workflows del módulo 2.

---

# Qué no debe ser el módulo Academy

Es importante dejar muy claro qué no debe pasar.

## No debe ser una biblioteca muerta

Los libros no son el output.  
Son el input.

## No debe ser un cementerio de resúmenes

Los resúmenes pueden existir como paso intermedio, pero la finalidad es destilar utilidad.

## No debe ser un sistema dependiente de gestión manual del usuario

Si el usuario tiene que recordar qué toca, dónde va cada cosa y qué subagente usar, el diseño ha fallado.

## No debe mezclar niveles de conocimiento sin orden

Hay que separar:

- trabajo pegado a la fuente,
- síntesis transversal,
- metodología interna.

## No debe construir demasiada maquinaria demasiado pronto

La arquitectura debe ser potente, pero sobria.  
Mejor pocas piezas con responsabilidades bien agrupadas que una inflación de skills y subagentes.

---

# Misión operativa del módulo

La misión operativa del módulo Academy puede resumirse así:

> Ingerir fuentes de referencia, organizarlas por dominio, autor y obra, diseñar itinerarios de estudio, trabajar las obras por bloques, extraer insights y activos cognitivos útiles, sintetizar las obras y elevar progresivamente lo valioso hacia capas transversales y hacia un método interno.

---

# Dominios del módulo

El módulo nace preparado para dos dominios:

## Funnels
Principalmente asociado al corpus de Russell Brunson en la fase inicial.

## Offers
Principalmente asociado al corpus de Alex Hormozi.

Aunque ambos dominios existen desde el principio, la prioridad práctica inicial probablemente será:

1. Funnels
2. Offers

Esto no cambia la arquitectura general.  
Solo cambia el orden operativo de trabajo.

---

# Relación entre Academy y las fuentes

Las fuentes base del módulo son libros y materiales de referencia.

Estas fuentes viven como materia prima.  
No deben confundirse con outputs.

Principio importante:

> El módulo Academy no guarda valor por almacenar libros, sino por el conocimiento que fabrica a partir de ellos.

Por tanto, conviene pensar el módulo como un sistema con dos planos distintos:

## Plano fuente
Donde están los materiales brutos.

## Plano output
Donde están los artefactos generados por el procesamiento de esas fuentes.

Este documento se centra sobre todo en el **plano output**, aunque presupone un plano fuente bien abastecido.

---

# Relación entre Academy y NotebookLM

NotebookLM y el módulo Academy no compiten; cumplen funciones distintas.

## NotebookLM
Sirve para:
- explorar rápido,
- estudiar de forma viva,
- consultar material,
- probar preguntas,
- moverse cómodamente por el contenido.

## Academy
Sirve para:
- consolidar lo importante,
- registrar conocimiento que merece persistir,
- ordenar el progreso,
- destilar outputs reutilizables,
- sostener continuidad entre sesiones,
- y construir el sistema vivo de aprendizaje acumulativo.

Principio clave:

> NotebookLM = exploración y consumo.  
> Academy = consolidación, estructura, destilación y memoria operativa.

---

# Modelo de experiencia deseado

La experiencia ideal del usuario es extremadamente importante y debe guiar la implementación.

## Escena ideal de uso

- En una pantalla: NotebookLM, PDF, fuente, libro, lectura.
- En otra pantalla: Claude Code trabajando dentro del módulo Academy.
- El usuario: estudia, lee, reflexiona, toma notas y conversa.
- Claude Code: organiza, enruta, propone siguiente paso, mantiene continuidad, actualiza outputs y absorbe la carga estructural.

La frase más importante de UX del módulo es esta:

> **El usuario estudia. Claude Code gestiona.**

O todavía más precisa:

> **La complejidad estructural la absorbe Claude Code; la atención del usuario se reserva para el aprendizaje de alto valor.**

---

# Principio de autosuficiencia del módulo

Este es uno de los principios centrales del diseño.

## Principio

> El módulo Academy debe ser estructuralmente complejo, pero experiencialmente ligero.

Eso implica que la complejidad interna del sistema no puede traducirse en fricción constante para el usuario.

El usuario no debe tener que:

- recordar el estado interno del módulo,
- decidir manualmente qué fase toca,
- saber a qué carpeta exacta debe ir cada output,
- seleccionar a mano qué agente o skill usar cada vez,
- o gestionar la continuidad entre sesiones.

Todo eso debe recaer primariamente sobre Claude Code mediante una capa explícita de orquestación.

---

# Arquitectura conceptual del módulo

El módulo Academy no debe entenderse solo como un árbol de carpetas.  
Debe entenderse como un sistema con capas.

## Capas conceptuales

### 1. Orchestration / Management
Gobierna el módulo, decide estado, siguiente paso, routing y continuidad.

### 2. Sources
El material de referencia disponible.

### 3. Itinerary
La secuencia de estudio propuesta a nivel de dominio, autor, obra y bloque.

### 4. Block Work
La unidad operativa real del estudio: bloques de una obra.

### 5. Extraction
El procesamiento útil de cada bloque.

### 6. Book Synthesis
La síntesis de una obra ya recorrida o parcialmente trabajada.

### 7. Domain Synthesis
La síntesis transversal de varias obras dentro de funnels u offers.

### 8. Internal Method
La capa donde empieza a emerger un método propio del sistema.

---

# El flujo canónico del módulo

El módulo Academy debe moverse siempre sobre un flujo relativamente estable.

## Flujo maestro

1. **Mapear corpus**
2. **Diseñar itinerario**
3. **Trabajar bloque**
4. **Sintetizar obra**
5. **Sintetizar dominio**
6. **Actualizar método interno**

Este flujo no implica que cada sesión recorra todas las fases.  
Implica que el sistema siempre sabe en qué punto del flujo está cada objeto de trabajo.

---

# Organización lógica de outputs

El módulo Academy vive en `04_outputs` porque produce outputs, no fuentes.

La lógica base recomendada es:

- un gran contenedor del módulo Academy,
- subdividido por dominio,
- luego por autor,
- luego por obra,
- y dentro de cada obra, por fases de procesamiento.

La lógica profunda es más importante que el naming final.  
La estructura debe reflejar **cómo se trabaja una obra**, no solo cómo se guarda.

## Cada obra debe poder expresar, como mínimo, estas fases

### A. Map
Qué es la obra, cómo está estructurada, qué promete, cuál es su posición dentro del corpus.

### B. Itinerary
Cómo se consumirá: bloques, secuencia, dependencias, prioridades.

### C. Blocks
Las unidades de estudio reales.

### D. Extraction
Lo útil destilado de los bloques.

### E. Synthesis
Lo que queda de la obra una vez recorrida o suficientemente trabajada.

---

# Las tres alturas del conocimiento dentro del módulo

Es fundamental distinguir tres alturas o niveles del conocimiento.

## Nivel 1 — Source-bound knowledge
Conocimiento muy pegado a una obra o a un bloque concreto.

Ejemplos:
- síntesis de bloque,
- insights del capítulo 2,
- playbooks detectados en una obra concreta.

## Nivel 2 — Domain synthesis
Conocimiento que cruza varias obras dentro de un dominio.

Ejemplos:
- patrones comunes entre varios libros,
- taxonomía de funnel types,
- principios recurrentes de diseño de offers.

## Nivel 3 — Internal doctrine
Conocimiento ya reformulado como marco interno del sistema.

Ejemplos:
- método interno de funnel design,
- criterio interno de evaluación de offers,
- catálogo normalizado del sistema.

Si esta distinción no se mantiene, el módulo se vuelve confuso.  
Si se mantiene, el crecimiento es mucho más limpio.

---

# Qué debe producir cada obra

Toda obra trabajada por el módulo debería terminar generando, como mínimo, este paquete de outputs conceptuales.

## 1. Mapa de la obra
Qué es, qué busca, cómo está compuesta, qué papel tiene en el corpus.

## 2. Itinerario de la obra
Cómo se trabajará: bloques, secuencia, hitos, prioridades.

## 3. Trabajo por bloques
El recorrido operativo real.

## 4. Extracciones útiles
Insights, principios, playbooks, ejemplos, heurísticas, patrones, elementos reutilizables.

## 5. Síntesis de la obra
Qué aporta realmente la obra al sistema.

## 6. Assets detectados
Qué partes de esa obra parecen transferibles o catalogables.

## 7. Contribución al método interno
Qué merece ser elevado a capas más generales del módulo.

---

# Capa transversal por dominio

Además del trabajo por obra, cada dominio necesita capas transversales.

## Funnels
Debería tender a tener, además de las carpetas por libro:

- síntesis transversal de obras,
- catálogo de blueprints o tipologías,
- método interno del dominio funnels.

## Offers
Debería tender a tener:

- síntesis transversal de obras,
- posible catálogo de componentes de offer,
- método interno del dominio offers.

---

# Por qué funnels merece probablemente una capa de catálogo más fuerte

El dominio funnels tiene un rasgo muy particular: las obras de referencia suelen contener no solo teoría o principios, sino también muchos:

- layouts,
- tipos de funnel,
- secuencias,
- configuraciones,
- estructuras típicas,
- variantes,
- escenarios de uso.

Por eso, en funnels tiene mucho sentido prever una capa específica donde vayan emergiendo estos activos de forma normalizada.

No deben quedar enterrados solo dentro de cada libro.

Más adelante, esto podrá tomar forma como un **blueprint catalog**.  
Pero en esta fase, basta con que la arquitectura lo permita.

---

# Sobriedad estructural: decisión de V2

En versiones anteriores del diseño aparecieron bastantes subagentes y skills.  
Esa expansión era útil como mapa de posibilidades, pero para una primera versión abstracta operativa conviene simplificar.

## Regla de V2

> Menos piezas explícitas, más responsabilidades bien agrupadas.

La pregunta correcta no es “qué microfunción existe”.  
La pregunta correcta es:

> “Qué pocas piezas necesitamos para que el módulo funcione bien, se autogestione y pueda escalar sin caos.”

---

# Arquitectura de subagentes — V2

La V2 reduce el sistema a un núcleo muy pequeño.

## 1. Academy Orchestrator

### Rol
Cerebro operativo del módulo.

### Responsabilidades
- mantener el estado del módulo,
- saber qué dominio, obra y bloque están activos,
- decidir el siguiente mejor paso,
- enrutar outputs,
- mantener continuidad entre sesiones,
- coordinar el flujo general,
- minimizar la carga de gestión del usuario.

### Filosofía
No estudia por el usuario.  
No reemplaza la reflexión.  
Orquesta el sistema para que el usuario pueda estudiar sin fricción.

---

## 2. Study Distiller

### Rol
Trabajador principal del día a día.

### Responsabilidades
- trabajar bloques concretos,
- procesar el contenido relevante,
- extraer insights,
- detectar playbooks, principios, ejemplos y patrones,
- separar señal de paja,
- generar outputs por bloque o por porción de obra.

### Filosofía
Es la pieza que convierte estudio en conocimiento procesado.

---

## 3. Method Synthesizer

### Rol
Motor de síntesis y compactación doctrinal.

### Responsabilidades
- sintetizar una obra completa o suficientemente recorrida,
- cruzar varias obras,
- detectar principios comunes y redundancias,
- proponer capas de síntesis de dominio,
- contribuir al método interno.

### Filosofía
Sube el conocimiento de nivel: de la obra al sistema.

---

## 4. Blueprint Cataloger — opcional

### Rol
Especialista en catalogación de funnels o estructuras.

### Cuándo tendría sentido
Solo si desde muy pronto aparece mucho volumen real de blueprints, tipologías o layouts que merezca un tratamiento propio.

### Decisión V2
No es núcleo obligatorio de arranque.  
Es una pieza opcional que puede emerger pronto, especialmente en funnels, pero no es necesario convertirla en actor principal antes de comprobar el volumen real.

---

# Arquitectura de skills — V2

También se reduce a un set pequeño y fuerte.

## 1. manage-academy-cycle

### Función
Skill grande de gestión del ciclo del módulo.

### Agrupa
- gestión del estado,
- decisión del siguiente paso,
- routing de outputs,
- continuidad,
- cierre de fase o de bloque.

### Por qué existe
Porque estas responsabilidades no necesitan cinco skills distintas; necesitan una sola skill de orquestación coherente.

---

## 2. build-study-itinerary

### Función
Diseñar el itinerario general o por obra.

### Output esperado
Secuencia de trabajo razonable:
- por dominio,
- por autor,
- por obra,
- por bloque.

### Por qué existe
Porque diseñar itinerario sí es una tarea con entidad propia.

---

## 3. distill-study-block

### Función
Procesar la unidad recurrente real de trabajo: un bloque.

### Output esperado
- insights,
- principios,
- playbooks,
- ejemplos,
- patrones,
- elementos reutilizables,
- límites o dudas relevantes.

### Por qué existe
Porque esta será probablemente la skill más usada del módulo.

---

## 4. synthesize-book

### Función
Cerrar o consolidar una obra.

### Output esperado
- síntesis de la obra,
- aportes diferenciales,
- contribución al sistema,
- qué se eleva y qué no.

### Por qué existe
Porque una obra necesita una fase clara de consolidación.

---

## 5. synthesize-domain

### Función
Cruzar varias obras de un mismo dominio y construir una capa más general.

### Output esperado
- síntesis transversal,
- patrones recurrentes,
- doctrina emergente,
- bases del método interno.

### Por qué existe
Porque sin esta skill el sistema se queda a ras de libro y nunca sube de nivel.

---

## 6. catalog-blueprints — opcional

### Función
Normalizar y acumular tipologías, layouts y configuraciones.

### Decisión V2
Existe como posibilidad razonable, sobre todo en funnels, pero no es imprescindible al minuto cero.

---

# Resumen del núcleo V2

## Subagentes núcleo
- Academy Orchestrator
- Study Distiller
- Method Synthesizer

## Skill núcleo
- manage-academy-cycle
- build-study-itinerary
- distill-study-block
- synthesize-book
- synthesize-domain

## Piezas opcionales
- Blueprint Cataloger
- catalog-blueprints

---

# Cómo debe repartirse el trabajo

## Academy Orchestrator
Gestiona el sistema.

## Study Distiller
Trabaja la unidad de estudio.

## Method Synthesizer
Sube el conocimiento de nivel.

Ese reparto es suficientemente simple para implementarse bien y suficientemente potente para escalar.

---

# El módulo no debe depender de control manual sesión a sesión

Esto debe quedar clarísimo para Claude Code.

Cada vez que el usuario abra el módulo Academy, Claude debería poder reconstruir o mantener fácilmente:

- estado actual,
- obra activa,
- fase activa,
- outputs existentes,
- outputs pendientes,
- siguiente paso recomendado,
- continuidad entre lo último hecho y lo siguiente.

El sistema no puede depender de memoria informal del usuario.

---

# El módulo debe estar preparado para ser conversacional

El modo real de uso no será que el usuario “lance procesos” de forma fría.  
Será más parecido a esto:

- “vamos con el siguiente bloque”
- “¿qué has sacado de esto?”
- “esto me parece importante”
- “no me convence esa síntesis”
- “quiero centrarme hoy en los blueprints”
- “sigamos por donde lo dejamos”

Por tanto, la implementación del módulo debe ser robusta no solo estructuralmente, sino también conversacionalmente.

Debe tolerar:

- interrupciones,
- sesiones parciales,
- cambios de ritmo,
- reformulaciones del usuario,
- y trabajo no lineal, sin perder coherencia.

---

# Qué debe hacer Claude Code al implementar este módulo

Cuando Claude Code reciba este contexto, no debería limitarse a crear carpetas bonitas.  
Debería interpretar que la implementación tiene varias responsabilidades.

## 1. Diseñar una estructura concreta del módulo
Traducción del diseño abstracto a una doc tree usable.

## 2. Diseñar la capa de estado
Cómo se representa el progreso y la continuidad del módulo.

## 3. Diseñar la capa de workflow
Cómo se mueve el sistema entre:
- obra,
- bloque,
- síntesis,
- dominio,
- método.

## 4. Diseñar o proponer los subagentes
Con nombre, rol, instrucciones y límites.

## 5. Diseñar o proponer las skills
Con alcance claro, trigger razonable y outputs esperados.

## 6. Diseñar la relación entre outputs por obra y outputs transversales
Cómo se promueve conocimiento desde una obra hacia una capa de dominio o método.

## 7. Mantener sobriedad
Evitar sobrediseñar el módulo con veinte piezas innecesarias.

---

# Criterios de éxito del módulo Academy

Este módulo será exitoso si logra que el usuario pueda:

## 1. Estudiar sin cargar con la gestión
Ese es el criterio principal.

## 2. Trabajar una obra de forma ordenada
Sin perder contexto ni outputs.

## 3. Reanudar fácilmente el trabajo
Sin fricción entre sesiones.

## 4. Acumular valor real
No solo notas, sino síntesis, patrones y estructura.

## 5. Subir progresivamente de nivel
De bloque → obra → dominio → método interno.

## 6. Preparar el terreno para el resto del sistema
Especialmente para el módulo 2 más adelante.

---

# Riesgos principales que hay que vigilar

## Riesgo 1 — Biblioteca disfrazada
Tener muchas carpetas y muchos libros, pero poco conocimiento destilado.

## Riesgo 2 — Overengineering
Crear demasiados agentes o skills antes de validar el flujo real de uso.

## Riesgo 3 — Gestión manual encubierta
Que el sistema parezca automático pero en realidad dependa de que el usuario lo sostenga.

## Riesgo 4 — Mezcla de niveles
Confundir outputs pegados a un libro con síntesis doctrinal o método interno.

## Riesgo 5 — Rígidez excesiva
Un sistema demasiado ceremonial puede volverse más pesado que útil.

---

# Recomendación estratégica para la implementación

La implementación del módulo debería seguir esta secuencia mental:

## Paso 1
Aterrizar la estructura del módulo Academy dentro de `04_outputs`.

## Paso 2
Definir cómo se representará el estado vivo del módulo.

## Paso 3
Diseñar el flujo base:
- itinerario,
- bloque,
- síntesis de obra,
- síntesis de dominio.

## Paso 4
Diseñar el núcleo mínimo de subagentes y skills.

## Paso 5
Validar que el usuario puede usarlo con fricción mínima.

## Paso 6
Solo después, abrir espacio para piezas opcionales como catalogación especializada.

---

# Posición de este documento dentro del trabajo inmediato

Este documento debe servir como base para una nueva conversación con Claude Code del tipo:

- entrar en la carpeta Academy,
- leer este documento como contexto fundacional,
- y proponer una implementación concreta del módulo.

No debería verse como documento final de ejecución, sino como:

> la base doctrinal y arquitectónica a partir de la cual Claude Code debe pensar una implementación concreta, usable y sobria.

---

# Definición final del módulo Academy

> El módulo Academy es el sistema autosuficiente del repo encargado de convertir obras fuente de funnels y offers en conocimiento procesado, síntesis estructurada y bases para una metodología interna, absorbiendo la complejidad organizativa para que el usuario pueda centrarse en estudiar y extraer valor.

---

# Principio final de diseño

> **Academy debe comportarse como una academia viva y auto-orquestada: el usuario aporta atención, criterio y reflexión; Claude Code aporta estructura, continuidad, orden y memoria operativa.**

---

# Cierre

Este documento no cierra todavía la implementación concreta.  
Pero sí fija los elementos que no deberían perderse en esa implementación:

- el módulo existe para transformar fuentes en conocimiento útil,
- debe organizarse por dominio, autor, obra y fases de procesamiento,
- debe distinguir entre conocimiento pegado a la fuente, síntesis transversal y método interno,
- debe tener una capa explícita de orquestación,
- debe usar un núcleo pequeño de subagentes y skills,
- y debe minimizar al máximo la carga administrativa sobre el usuario.

La siguiente conversación con Claude Code debería tomar este documento como punto de partida para proponer:

- doc tree concreta,
- representación de estado,
- flujo de trabajo del módulo,
- definición de subagentes,
- definición de skills,
- y plan de implementación del módulo Academy antes de comenzar con el primer libro de Russell Brunson.

---

# Apéndice visual — Diseño abstracto del Módulo 1 (V2)


MÓDULO 1 = ACADEMY

Objetivo:
fuentes → estudio guiado → extracción → síntesis → método interno


## 1) Doc tree lógico


04_outputs/
└── academy/
    ├── funnels/
    │   └── russell-brunson/
    │       ├── [book-01]/
    │       │   ├── 01_map/
    │       │   ├── 02_itinerary/
    │       │   ├── 03_blocks/
    │       │   ├── 04_extraction/
    │       │   └── 05_synthesis/
    │       ├── [book-02]/
    │       ├── [book-03]/
    │       ├── cross-work-synthesis/
    │       ├── blueprint-catalog/        ← opcional
    │       └── internal-method/
    │
    └── offers/
        └── alex-hormozi/
            ├── [book-01]/
            │   ├── 01_map/
            │   ├── 02_itinerary/
            │   ├── 03_blocks/
            │   ├── 04_extraction/
            │   └── 05_synthesis/
            ├── [book-02]/
            ├── [book-03]/
            ├── cross-work-synthesis/
            ├── component-catalog/        ← opcional
            └── internal-method/


## 2) Capas del módulo


[ORCHESTRATION]
      ↓
[SOURCES] → [ITINERARY] → [BLOCK WORK] → [BOOK SYNTHESIS] → [DOMAIN SYNTHESIS] → [INTERNAL METHOD]


## 3) Flujo canónico


1. mapear corpus
2. construir itinerario
3. trabajar bloque
4. sintetizar obra
5. sintetizar dominio
6. actualizar método interno


## 4) Subagentes V2


┌───────────────────────┐
│ Academy Orchestrator  │
├───────────────────────┤
│ - gestiona estado     │
│ - decide siguiente    │
│ - enruta outputs      │
│ - mantiene continuidad│
│ - auto-gestiona módulo│
└───────────┬───────────┘
            │ delega
            ▼
┌───────────────────────┐
│ Study Distiller       │
├───────────────────────┤
│ - trabaja bloques     │
│ - extrae insights     │
│ - detecta playbooks   │
│ - separa señal/paja   │
│ - produce outputs     │
└───────────┬───────────┘
            │ eleva
            ▼
┌───────────────────────┐
│ Method Synthesizer    │
├───────────────────────┤
│ - sintetiza libros    │
│ - cruza varias obras  │
│ - sintetiza dominio   │
│ - propone método      │
└───────────────────────┘


### Opcional

┌───────────────────────┐
│ Blueprint Cataloger   │
├───────────────────────┤
│ - normaliza funnels   │
│ - clasifica layouts   │
│ - construye catálogo  │
└───────────────────────┘


## 5) Skills V2

┌──────────────────────────────┐
│ manage-academy-cycle         │
├──────────────────────────────┤
│ estado + siguiente paso +    │
│ routing + continuidad        │
└──────────────────────────────┘

┌──────────────────────────────┐
│ build-study-itinerary        │
├──────────────────────────────┤
│ itinerario general + por obra│
└──────────────────────────────┘

┌──────────────────────────────┐
│ distill-study-block          │
├──────────────────────────────┤
│ bloque → insights/playbooks/ │
│ principios/ejemplos          │
└──────────────────────────────┘

┌──────────────────────────────┐
│ synthesize-book              │
├──────────────────────────────┤
│ cierre y destilación de obra │
└──────────────────────────────┘

┌──────────────────────────────┐
│ synthesize-domain            │
├──────────────────────────────┤
│ cruce de obras + método      │
└──────────────────────────────┘

### Opcional

┌──────────────────────────────┐
│ catalog-blueprints           │
├──────────────────────────────┤
│ catálogo transversal funnel  │
└──────────────────────────────┘


## 6) Reparto funcional


Academy Orchestrator
    ↓
gestiona el sistema

Study Distiller
    ↓
trabaja la unidad de estudio

Method Synthesizer
    ↓
sube de nivel y compacta doctrina


## 7) UX ideal del usuario


PANTALLA DERECHA
- NotebookLM
- PDF / libro
- consumo / estudio

PANTALLA IZQUIERDA
- ClaudeCode
- orquestación automática
- outputs / continuidad

USUARIO
- estudia
- reflexiona
- toma notas
- conversa

CLAUDE
- organiza
- decide
- registra
- sintetiza
- mantiene el módulo vivo


## 8) Principio operativo central


El módulo 1 debe ser:

estructuralmente complejo
pero
experiencialmente ligero

La complejidad la absorbe ClaudeCode.
El usuario solo estudia.


## 9) Versión ultra resumida


ACADEMY/
  dominio/
    autor/
      obra/
        map
        itinerary
        blocks
        extraction
        synthesis
    cross-work-synthesis
    catalog (opcional)
    internal-method

SUBAGENTES:
  1. Academy Orchestrator
  2. Study Distiller
  3. Method Synthesizer
  4. Blueprint Cataloger (opcional)

SKILLS:
  1. manage-academy-cycle
  2. build-study-itinerary
  3. distill-study-block
  4. synthesize-book
  5. synthesize-domain
  6. catalog-blueprints (opcional)
