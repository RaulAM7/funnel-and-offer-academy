# CRM / GWS Alignment Notes — IA Mujeres Funnel

## Nota de alcance Fase 6.1

Funnel Academy disena el funnel comercial, el copy, las reglas de personalizacion y la logica de estados. No implementa workflows, no toca contactos reales, no envia emails y no modifica GWS.

La implementacion tecnica de workflows, automatizaciones, smoke tests y validacion CRM-GWS queda fuera de este repo y corresponde al equipo/repositorio CRM-GWS.

## Decisiones operativas integradas

- Business Line CRM: `SkilLand IA Mujeres`.
- Campaign/Funnel CRM: `IA Mujeres 2026`.
- Cuenta emisora definitiva para esta campana: `gerencia@skilland.ai`.
- No usar `direccion@skilland.ai` ni `sales@reboot.academy`.
- Email 1 se envia con presentacion corta adjunta.
- No adjuntar dossier largo en primer contacto.
- Primera tanda con plantilla unificada y personalizacion ligera.
- Envio progresivo por tandas pequenas con revision humana de drafts.
- No hay restriccion estrategica por tamano fijo.
- Objetivo operativo: cubrir el dataset actual de 100+ registros si la calidad lo permite.

## CRM / Twenty como fuente de verdad

Twenty debe conservar la verdad comercial y operativa sobre:

- deals u oportunidades;
- estado comercial del contacto;
- Business Line;
- Campaign;
- prioridad P0/P1/P2/Review;
- segmento ICP;
- tipo de organizacion;
- area/departamento;
- territorio;
- flags de calidad de datos;
- revision manual;
- tareas;
- reuniones;
- notas comerciales;
- resultado de respuesta o no respuesta.

## Campos CRM necesarios

Campos ya asumidos o necesarios para operar esta campana:

- `business_line`;
- `campaign`;
- `organization_type`;
- `icp_segment`;
- `department_area`;
- `territory`;
- `priority`;
- `high_confidence`;
- `needs_manual_review`;
- `generic_email`;
- `duplicate_possible`;
- `contact_name`;
- `contact_role`;
- `email`;
- `email_type` si existe o se puede derivar;
- `personalization_line` si se aprueba;
- `email_sender`;
- `email_attachment`;
- `last_email_sent_at`;
- `last_message_id`;
- `last_thread_id`;
- `reply_received_at`;
- `bounce_status` si esta disponible;
- `meeting_status`;
- `next_task`.

## GWS CLI como fuente operativa

GWS CLI debe registrar o devolver, cuando la implementacion tecnica lo permita:

- draft creado;
- draft aprobado;
- email enviado;
- cuenta emisora usada;
- destinatario;
- asunto;
- attachment usado;
- `message_id`;
- `thread_id`;
- respuesta detectada;
- bounce si esta disponible;
- timestamps relevantes.

## Que se puede medir de forma fiable

- Email preparado como draft.
- Draft revisado por humano.
- Email enviado.
- Cuenta emisora usada.
- Message ID y thread ID si GWS los expone.
- Respuesta recibida.
- Bounce si GWS o el workflow lo detecta.
- Reunion propuesta.
- Reunion agendada.
- Reunion realizada.
- Propuesta solicitada.
- No interesado.
- Sin respuesta tras ventana definida.

## Que no se debe usar como KPI principal

- Aperturas de email.
- Clicks no instrumentados.
- Inferencias de interes sin respuesta.
- Metricas no disponibles en CRM/GWS.
- Resultados de impacto antes de ejecutar un proyecto real.

## Ownership operativo

| elemento | fuente principal | responsable operativo | nota |
|---|---|---|---|
| Estado comercial | CRM | Humano / CRM | No depende de aperturas. |
| Segmento y prioridad | CRM | Humano | Debe revisarse en P0/P1. |
| Draft | GWS | Humano / GWS | Debe aprobarse antes de enviar. |
| Envio | GWS | Operador autorizado | No desde Funnel Academy. |
| Message ID / Thread ID | GWS | GWS / integracion | Debe sincronizarse si el workflow lo permite. |
| Respuesta | GWS + CRM | Humano | La interpretacion comercial es humana. |
| Bounce | GWS + CRM | GWS / humano | Si esta disponible. |
| Reunion | CRM | Humano | Fuente comercial de verdad. |
| Workflow real | Repo CRM-GWS | Equipo tecnico | Fuera de scope de Funnel Academy. |

## Estados comerciales recomendados

- Pendiente revision.
- Pendiente primer email.
- Primer email draft creado.
- Primer email aprobado.
- Primer email enviado.
- Respuesta recibida.
- Conversacion iniciada.
- Reunion propuesta.
- Reunion agendada.
- Reunion realizada.
- Propuesta solicitada.
- No interesado.
- Sin respuesta.
- Revisión manual.

## Dependencias del smoke test 4.1

El smoke test 4.1 puede aportar confirmacion tecnica sobre:

- capacidad real de crear drafts;
- capacidad real de enviar desde `gerencia@skilland.ai`;
- captura de `message_id` y `thread_id`;
- deteccion de respuestas;
- deteccion de bounces;
- sincronizacion con CRM;
- limites operativos por cuenta o lote.

Fase 6.1 no debe bloquearse por el smoke test. Sus resultados deben incorporarse cuando esten validados por el equipo CRM-GWS.

## Pendientes para workflows reales

Pendiente fuera de este repo:

- confirmar eventos GWS disponibles;
- definir sincronizacion exacta CRM-GWS;
- decidir si los drafts se crean desde CRM, GWS CLI o proceso intermedio;
- implementar tareas automaticas, si aplica;
- implementar deteccion de respuestas y bounces, si aplica;
- validar permisos y seguridad;
- activar workflows reales en el entorno tecnico correspondiente.

## Regla de prudencia operativa

La campana debe ejecutarse por tandas pequenas:

- 5-10 contactos o ritmo similar;
- revision humana de cada draft;
- pausa si aparecen errores de personalizacion, tono, adjunto o calidad de datos;
- continuidad hacia el dataset completo si las senales son aceptables.

Esta regla es prudencia operativa, no un piloto estrategico restrictivo.

## Ajuste validado Fase 6.1 — funnel por carriles

La logica operativa queda organizada en tres carriles:

- Carril principal: respuesta recibida, conversacion iniciada, reunion propuesta, reunion agendada, reunion realizada, propuesta solicitada.
- Carril de retargeting: seguimiento pendiente, sin respuesta, follow-up 1, follow-up 2, nurturing a futuro.
- Carril de cierre/bloqueo: no interesado, bounce/contacto invalido, no procede, revision manual.

## Stages, statuses, eventos y tareas

No todos los conceptos deben ser stages de CRM.

- Stages comerciales: conversacion iniciada, reunion propuesta, reunion agendada, reunion realizada, propuesta solicitada, no interesado.
- Outreach status: pendiente primer email, primer email enviado, seguimiento pendiente, sin respuesta, nurturing.
- Eventos GWS: `draft_created`, `email_sent`, `email_opened`, `reply_received`, `bounce_detected`.
- Tareas humanas: aprobar draft, responder interesado, proponer reunion, hacer follow-up, revisar contacto.

## Aperturas

`email_opened` solo debe guardarse como senal auxiliar si existe tracking fiable.

No debe:

- ser stage principal;
- activar cierre;
- contarse como conversion;
- mencionarse en el copy de follow-up.

## Firma Gmail/GWS

No hardcodear firma en el cuerpo del Email 1 desde Funnel Academy.

Pendiente tecnico externo: validar si el metodo real de GWS inserta la firma de Gmail al crear/enviar el draft desde `gerencia@skilland.ai`. Si no la inserta, el repo/equipo CRM-GWS debera decidir si inyecta una firma HTML controlada.
