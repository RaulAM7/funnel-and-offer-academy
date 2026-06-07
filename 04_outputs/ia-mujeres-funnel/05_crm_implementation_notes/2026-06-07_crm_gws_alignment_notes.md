# CRM GWS Alignment Notes — IA Mujeres

- Date: 2026-06-07
- Scope: alineacion entre estrategia de Fase 6 y operativa actual CRM + GWS

## CRM / Twenty como fuente de verdad

CRM debe conservar:

- deal / opportunity;
- `campaignName = IA Mujeres 2026`;
- `businessLineName = SkilLand IA Mujeres`;
- relacion nativa de Business Line;
- prioridad comercial `P0`, `P1`, `P2`, `Review` en nota o campo operativo;
- `icp_segment`;
- `department_area`;
- `high_confidence`;
- `needs_manual_review`;
- `generic_email`;
- `duplicate_possible`;
- tareas;
- reuniones;
- notas de decision y contexto.

## Campos CRM necesarios para operar esta fase

### Ya disponibles o documentados

- `campaignName`
- `businessLineName`
- `icp_segment`
- `department_area`
- `high_confidence`
- `needs_manual_review`
- `generic_email`
- `duplicate_possible`
- `outreachStatus`
- `firstEmailSentAt`
- `lastEmailSentAt`
- `lastReplyAt`
- `followUpDueAt`
- `meetingStatus`
- `meetingDate`

### Necesarios a nivel operativo, aunque puedan vivir como notas o convencion

- prioridad comercial `P0/P1/P2/Review`
- motivo de cierre `No interesado` o `Nurturing`
- criterio de lote piloto
- resumen de reunion realizada

## Eventos GWS necesarios

Los eventos minimos utiles para esta campana son:

- `draft_created`
- `email_sent`
- `reply_received`
- `send_failed`
- `bounce_detected`
- `manual_review_required`

## Que puede medir de forma fiable el sistema

- draft creado;
- email enviado;
- reply recibido;
- bounce si Gmail lo expone o se detecta;
- reunion propuesta;
- reunion agendada;
- estado comercial actualizado.

## Que NO puede medir de forma fiable

- apertura de email;
- lectura real;
- clics si no existe infraestructura externa;
- interes cualificado sin intervencion humana.

## Rol humano obligatorio

El humano debe intervenir en:

- validacion final de lotes P0 y P1;
- aprobacion de drafts;
- interpretacion del contexto politico o institucional;
- lectura de replies;
- paso de `Respuesta recibida` a `Conversacion iniciada`;
- propuesta y cierre de agenda;
- decision de nurturing o cierre.

## Dependencias del smoke test 4.1

Esta fase no queda bloqueada por el smoke test, pero hay piezas que dependen de su validacion:

- validacion de que el cambio de `outreachStatus` activa tareas coherentes;
- validacion de que la deteccion de reply puede registrarse sin tocar datos reales;
- validacion de que el flujo draft > send > thread > reply no rompe aislamiento por campaign;
- validacion de que las cuentas emisoras finales son correctas.

## Pendientes para workflows reales

- Los workflows deben completarse y activarse manualmente en UI.
- `Sin respuesta` no tiene automatizacion nativa cerrada en esta fase.
- `Propuesta solicitada` y `Reunion realizada` hoy dependen de tarea y nota humana.
- La asociacion `thread_id -> crm_deal_id` sigue pendiente de integracion real.
- Falta confirmar el estado real de las cuentas `gerencia@skilland.ai` y `direccion@skilland.ai` porque la documentacion mezcla "pendiente" y "operativas".

## Regla de traduccion estrategia -> operativa

La documentacion de Fase 6 usa el lenguaje comercial en espanol, pero la operativa real sigue este mapeo:

- `Pendiente primer email` -> `pending_first_email`
- `Primer email enviado` -> `first_email_sent`
- `Seguimiento pendiente` -> `follow_up_pending`
- `Respuesta recibida` -> `replied`
- `Reunion propuesta` -> `meeting_to_schedule`
- `Reunion agendada` -> `meeting_scheduled`
- `No interesado` -> `lost`
- `Nurturing / a futuro` -> `nurturing`

## Nota sobre el piloto

El piloto debe operar con:

- 12 oportunidades maximo;
- 8 P0 minimo;
- hasta 4 P1;
- 0 Review;
- revision humana previa obligatoria;
- medida por envio, reply, bounce, reunion propuesta y reunion agendada.
