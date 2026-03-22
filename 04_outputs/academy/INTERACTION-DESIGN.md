# Diseno de Interaccion Usuario - Modulo 1 Academy

## Como funciona una sesion de estudio

### Lo que hace el usuario
Abre una sesion nueva y dice algo como "vamos con el primer bloque", "sigamos", o "donde lo dejamos".

### Lo que pasa por debajo

1. Claude lee `STATE.md` → identifica bloque activo, progreso, siguiente paso
2. Lee el itinerario → localiza el bloque, sus capitulos y densidad
3. Lee el source file en `00_inbox/` — solo la parte correspondiente al bloque
4. Procesa el material y produce dos archivos:
   - `03_blocks/block-NN/block-NN_resumen.md` — resumen corto del bloque (30-50 lineas)
   - `04_extraction/extraction-block-NN.md` — extraccion estructurada: insights, principios, playbooks, ejemplos, patrones, dudas, candidatos a elevacion
5. Te presenta el bloque, lo ajusta contigo y lo cierra conversacionalmente
6. Si el bloque es denso o muy metodologico, puede sugerir una tercera accion opcional:
   - `03_blocks/block-NN/block-NN_canvas.excalidraw` — canvas de consumo visual / recall
7. Si confirmas la visualizacion, Claude enruta a `visual-editor`:
   - usa `Excalidraw MCP` si esta disponible
   - y si no, cae a un fallback local que genera el `.excalidraw`
8. Actualiza `STATE.md` — bloque marcado como completado, estado visual actualizado, log de sesion actualizado, siguiente paso propuesto

### El matiz clave: es conversacional, no automatico

El sistema esta pensado para que Claude trabaje **contigo**, no en silencio.

- Tu estas leyendo el libro en paralelo (NotebookLM, PDF, lo que sea)
- Claude trabaja el bloque contigo — puedes intervenir, comentar, decir "esto me parece clave", "no me convence esto", "profundiza en el Value Ladder"
- La extraccion se enriquece con tu input, no es solo un resumen automatico

### En la practica

La dinamica tipica sera: Claude procesa el bloque, te presenta lo que ha sacado, tu revisas y ajustas, y entre los dos se cierra el bloque. Segun como te sientas, puedes ir afinando el ritmo — mas conversacional o mas "procesa y ensename".

## Frases que el sistema entiende

| Dices | El sistema hace |
|-------|-----------------|
| "vamos con el siguiente bloque" | Lee STATE.md, identifica el bloque que toca, lo trabaja |
| "sigamos" / "donde lo dejamos" | Lee STATE.md, reporta posicion, propone siguiente paso |
| "como vamos" | Muestra progreso desde STATE.md |
| "esto me parece importante" | Lo incorpora a la extraccion o lo registra en hilos abiertos |
| "no me convence esa sintesis" | Ajusta el output segun tu feedback |
| "quiero centrarme en los blueprints" | Adapta el foco de la sesion |
| "visualiza este bloque" / "hazme el canvas" | Lanza la capa visual del bloque activo o del bloque que indiques |
| "revisa el canvas" | Compara el canvas actual contra el markdown y propone cambios sin sobreescribir por defecto |
| "aplica cambios al canvas" | Actualiza el `.excalidraw` existente |
| "sintetiza el libro" | Lanza sintesis de la obra (si hay suficientes bloques completados) |

## Principio central

> **El usuario estudia. Claude gestiona.**
>
> La complejidad estructural la absorbe Claude; la atencion del usuario se reserva para el aprendizaje de alto valor.

## Configuracion tipica

- Pantalla derecha: NotebookLM / PDF / libro / lectura
- Pantalla izquierda: Claude Code dentro del modulo Academy
- Superficie opcional cuando el bloque lo merece: canvas Excalidraw en navegador/editor
- El usuario: estudia, lee, reflexiona, toma notas, conversa
- Claude: organiza, enruta, registra, sintetiza, mantiene el modulo vivo
- Visual Editor: aparece solo bajo demanda para convertir frameworks densos en mapa visual consumible
