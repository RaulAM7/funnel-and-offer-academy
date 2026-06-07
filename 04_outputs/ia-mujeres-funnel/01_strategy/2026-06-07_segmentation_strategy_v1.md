# Segmentation Strategy v1 — SkilLand IA Mujeres

## Nota de Fase 6.1

La segmentacion sigue siendo necesaria para priorizar revision, personalizacion y seguimiento CRM, pero no se usaran variantes profundas de copy en esta primera tanda. El usuario ha decidido trabajar con una plantilla unificada y microvariaciones segun datos disponibles.

## Principio operativo

Segmentar no significa crear cuatro campanas separadas. En esta iteracion significa:

- decidir orden de revision;
- adaptar una linea de contexto;
- evitar errores de tono o area;
- asignar prioridad CRM;
- decidir si un registro entra en envio, requiere revision o queda fuera temporalmente.

## Segmentos accionables

| segmento | prioridad base | dolor probable | angulo de conversacion | CTA recomendado | riesgos | implicacion CRM |
|---|---:|---|---|---|---|---|
| Cabildos — Igualdad | P0 | Necesidad de politicas insulares medibles y legitimidad publica en igualdad digital. | IA como reto de igualdad y oportunidad territorial para mujeres de la isla. | Primera reunion institucional para valorar encaje. | Que suene a formacion blanda o accion simbolica. | `organization_type=cabildo`, `department_area=igualdad`, prioridad alta, revision humana. |
| Cabildos — Empleo | P0/P1 | Necesidad de activar empleabilidad cualificada y transicion laboral. | IA como palanca de empleo femenino, autonomia economica y nuevos roles. | Reunion para explorar encaje con empleo/desarrollo economico. | Que se perciba como discurso solo de igualdad y no de empleo. | `department_area=empleo`, prioridad segun calidad de contacto. |
| Cabildos — Politicas Sociales | P1 | Intervencion con colectivos vulnerables y necesidad de impacto justificable. | Inclusion, autonomia digital y acceso real a oportunidades tecnologicas. | Reunion para entender colectivos y objetivos. | Mayor sensibilidad sobre poblacion destinataria y presupuesto. | Requiere notas de contexto y seguimiento humano. |
| Ayuntamientos — Igualdad | P0/P1 | Necesidad de acciones locales visibles, utiles y justificables. | Igualdad digital local y futuro del trabajo para mujeres del municipio. | Reunion corta para valorar si tiene sentido para el municipio. | Buzon generico, poco tiempo del area, riesgo de parecer envio masivo. | Seguimiento por tandas, personalizacion con municipio/area. |
| Ayuntamientos — Empleo / Desarrollo Local | P1 | Necesidad de empleabilidad, productividad y oportunidades para mujeres del municipio. | IA como herramienta de desarrollo local y acceso a nuevos perfiles. | Reunion para valorar encaje con programas locales. | Si el framing es demasiado de igualdad, puede perder traccion. | Personalizacion por area, territorio y tipo de contacto. |
| Entidades publicas mixtas o ambiguas | P2 | Puede haber encaje, pero el area responsable no esta clara. | Derivacion a igualdad, empleo o desarrollo local. | Pedir derivacion o primera orientacion. | Baja precision, mayor riesgo de no respuesta. | Mantener en CRM con notas y `needs_manual_review` segun caso. |
| Registros en revision manual | Review | Datos incompletos, duplicados, ambiguos o contacto no usable. | No se recomienda envio hasta limpiar. | No aplica todavia. | Error reputacional, envio a persona/area incorrecta. | `needs_manual_review=true`, tarea de limpieza antes de draft. |

## Logica P0 / P1 / P2 / Review

### P0

Registros con alta confianza para primeras tandas:

- `high_confidence=true`;
- `needs_manual_review=false`;
- cabildo o ayuntamiento;
- area clara de Igualdad, Empleo, Mujer, Politicas Sociales o Desarrollo Local;
- email usable;
- sin duplicidad probable relevante;
- territorio y entidad claros.

### P1

Registros usables con alguna limitacion ligera:

- area clara, pero email generico de departamento;
- entidad y territorio claros, pero sin persona nominal;
- cabildo o ayuntamiento con buen encaje, aunque falte cargo exacto;
- posible revision ligera antes de draft.

### P2

Registros que pueden entrar despues de aprender de las primeras tandas:

- entidad publica mixta o ambigua;
- contacto institucional general;
- area no totalmente clara, pero con posible relacion con igualdad, empleo o desarrollo local;
- calidad suficiente para conservar, pero no para priorizar.

### Review

Registros que no deben enviarse sin limpieza:

- `needs_manual_review=true`;
- `duplicate_possible=true` sin resolver;
- email incompleto, dudoso o no usable;
- entidad o territorio ambiguos;
- area incompatible o desconocida;
- riesgo de tratar a una persona o institucion de forma incorrecta.

## Uso de segmentacion en el copy

Para esta primera tanda se mantiene un unico Email 1 base. La segmentacion solo modifica:

- saludo;
- linea de personalizacion;
- referencia a cabildo o ayuntamiento;
- referencia a Igualdad, Empleo, Desarrollo Local o Politicas Sociales;
- CTA secundario de derivacion cuando el buzon sea generico.

No se deben crear variantes profundas por segmento hasta validar respuesta humana y calidad real de datos.

## Ejemplos de angulo por segmento

### Cabildo — Igualdad

Enfoque: responsabilidad insular, igualdad digital, futuro del trabajo y posibilidad de accion territorial medible.

### Cabildo — Empleo

Enfoque: transicion laboral, acceso a nuevos roles, autonomia economica y desarrollo de talento femenino.

### Ayuntamiento — Igualdad

Enfoque: accion local, mujeres del municipio y conversacion institucional sobre brecha de IA.

### Ayuntamiento — Empleo / Desarrollo Local

Enfoque: oportunidades reales para mujeres del municipio, nuevos perfiles y conexion formacion-empleo.

### Buzon institucional general

Enfoque: derivacion respetuosa al area responsable, sin fingir cercania ni asumir interlocutor.

## Como deberia verse en CRM

Campos minimos para operar segmentacion y personalizacion:

- `business_line`: `SkilLand IA Mujeres`;
- `campaign`: `IA Mujeres 2026`;
- `organization_type`;
- `icp_segment`;
- `department_area`;
- `territory`;
- `priority`: P0, P1, P2, Review;
- `high_confidence`;
- `needs_manual_review`;
- `generic_email`;
- `duplicate_possible`;
- `personalization_line` si existe;
- `email_sender`: `gerencia@skilland.ai`;
- `email_attachment`: presentacion corta.

## Regla de entrada a tandas de envio

Entran primero:

- P0 revisados por humano;
- P1 con email usable y personalizacion segura;
- sin duplicidad probable sin resolver;
- sin datos inventados;
- con draft aprobado antes del envio.

Quedan fuera temporalmente:

- Review;
- duplicados no resueltos;
- emails no usables;
- registros sin entidad o territorio claro;
- registros que exijan copy especifico no validado.

## Ritmo recomendado

- Tandas pequenas de 5-10 contactos o ritmo similar.
- Revision humana previa de drafts.
- Aprendizaje entre tandas sobre respuestas, bounces y derivaciones.
- Escalado hacia el dataset completo si no aparecen problemas de calidad o tono.

## Ajuste validado Fase 6.1 — uso por carriles

La segmentacion no cambia la pelicula del funnel. Todos los segmentos aptos entran por Email 1 con objetivo de conversacion/reunion y luego se distribuyen por carriles segun eventos reales:

- Responde: pasa a conversacion humana, independientemente del segmento.
- No responde: pasa a seguimiento pendiente, follow-up y posible nurturing.
- Rebota o contacto incorrecto: pasa a revision manual.
- Dice no: se marca no interesado con motivo.

## Implicacion para retargeting

La prioridad P0/P1/P2 ayuda a decidir orden y nivel de revision, pero no debe cerrar contactos por silencio.

- P0/P1 sin respuesta: follow-up con especial cuidado institucional.
- P2 sin respuesta: puede pasar antes a nurturing si no hay senales fuertes.
- Review: no entra en retargeting hasta resolver datos.

`email_opened`, si existe, solo ajusta el tono del follow-up; no cambia el segmento ni convierte el contacto en interesado.
