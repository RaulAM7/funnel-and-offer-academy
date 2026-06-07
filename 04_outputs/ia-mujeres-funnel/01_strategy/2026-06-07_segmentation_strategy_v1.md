# Segmentation Strategy v1 — IA Mujeres

- Date: 2026-06-07
- Scope: cabildos y ayuntamientos canarios con areas afines a igualdad, empleo, politicas sociales y desarrollo local

## Logica de segmentacion

La segmentacion inicial debe seguir dos ejes:

1. tipo de entidad y responsabilidad institucional;
2. claridad del area y calidad operativa del contacto.

## Logica de priorizacion por registro

### P0

Registros con:

- `high_confidence = true`;
- `needs_manual_review = false`;
- `duplicate_possible = false` o riesgo bajo;
- `organization_type` cabildo o ayuntamiento;
- `icp_segment` claro;
- `department_area` claro;
- email usable, personal o de departamento.

### P1

Registros con buen encaje, pero con una friccion manejable:

- email generico de departamento;
- mezcla de areas compatible con el mensaje;
- posible revision ligera de tono o routing.

### P2

Registros usables, pero menos directos:

- email institucional general;
- area ambigua;
- encaje posible pero no prioritario para el primer piloto.

### Review

Registros que no deben entrar en piloto:

- `needs_manual_review = true`;
- falta de email usable;
- area poco clara;
- duplicado no resuelto;
- baja confianza o inconsistencias relevantes.

## Regla sobre `generic_email`

Un `generic_email` no es automaticamente malo. Un correo de departamento de Igualdad, Empleo o Servicios Sociales puede ser mas util que un correo personal si el mensaje esta pensado para ser derivado institucionalmente.

## Segmentos

| Segmento | Prioridad | Dolor probable | Angulo de conversacion | CTA recomendado | Riesgos | Implicacion CRM |
|---|---|---|---|---|---|---|
| Cabildos - Igualdad | P0 | Necesitan accion insular medible y con legitimidad publica. | Igualdad digital como politica publica insular con piloto escalable. | Diagnostico insular + piloto. | Que se perciba como formacion blanda. | Vista prioritaria, tareas rapidas, seguimiento cercano. |
| Cabildos - Empleo | P0/P1 | Necesitan empleabilidad y adaptacion a IA con impacto territorial. | IA Mujeres como palanca de empleabilidad y reconversion. | Reunion de diagnostico de empleabilidad. | Que el enfoque parezca demasiado social y poco laboral. | Etiqueta de segmento y prioridad alta en opportunity. |
| Cabildos - Politicas Sociales | P1 | Necesitan intervencion con colectivos vulnerables y justificacion de impacto. | Programa medible para inclusion y autonomia digital. | Conversacion sobre colectivo y piloto. | Mayor sensibilidad presupuestaria y de derivacion. | Requiere notas de contexto mas finas. |
| Ayuntamientos - Igualdad | P0 | Necesitan acciones locales visibles, aterrizadas y justificables. | Igualdad digital local con piloto municipal. | Diagnostico territorial local. | Buzon generico, poco tiempo del equipo. | Mayor volumen; seguimiento por lotes. |
| Ayuntamientos - Empleo / Desarrollo Local | P1 | Necesitan productividad, empleabilidad y apoyo a mujeres del municipio. | IA como herramienta de transicion laboral y desarrollo economico. | Reunion sobre piloto para empleo local. | Menor encaje si el framing suena solo a igualdad. | Separar bien copy por area en Fase 7. |
| Entidades publicas mixtas o ambiguas | P2 | Tienen competencias cruzadas, pero encaje incierto. | Conversacion exploratoria con foco en encaje institucional. | Validar area responsable. | Derivacion lenta, ownership difuso. | Mantener baja prioridad hasta aclarar. |
| Registros en revision manual | Review | Datos incompletos o ambiguos. | No salir a contacto hasta limpiar. | Ninguno. | Rebote, mal routing, mala primera impresion. | Cola de revision y tarea manual. |

## Prioridad por segmento

### Prioridad 1

- Cabildos - Igualdad
- Ayuntamientos - Igualdad

Son el mejor encaje entre tesis del producto, legitimidad institucional y coherencia del primer mensaje.

### Prioridad 2

- Cabildos - Empleo
- Cabildos - Politicas Sociales
- Ayuntamientos - Empleo / Desarrollo Local

Requieren modular el angulo hacia empleabilidad, productividad publica o inclusion con impacto.

### Prioridad 3

- Entidades publicas mixtas o ambiguas

No deben liderar el piloto. Sirven para ampliar casuisticas despues de validar mensaje.

## Implicacion CRM

La estrategia debe reflejarse en CRM con:

- `campaignName = IA Mujeres 2026`;
- `businessLineName = SkilLand IA Mujeres`;
- `icp_segment` como segmentador primario;
- `department_area` como modulador del angulo;
- `high_confidence`, `needs_manual_review`, `generic_email`, `duplicate_possible` como base operativa;
- una etiqueta o nota de prioridad comercial `P0`, `P1`, `P2`, `Review`.

## Regla de entrada a piloto

Solo entran en el piloto:

- registros P0;
- algunos P1 con area clara y routing plausible;
- ningun Review;
- ningun contacto sin email usable.
