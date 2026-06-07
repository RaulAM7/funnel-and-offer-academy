# CRM/GWS Execution Handoff — IA Mujeres

## Estado del handoff

Funnel Academy deja cerrado el sprint estrategico/copy minimo de IA Mujeres.

El siguiente paso vive en CRM/GWS, previsiblemente en el repo `skilland-crm`.

No implementar desde este repo.

## Alcance entregado por Funnel Academy

- Funnel validado: conversacion institucional first.
- Email 1 final aprobado como base.
- Follow-up 1.
- Follow-up 2 con white paper.
- Nota de retargeting de contenido.
- Reglas finales de personalizacion.
- Handoff operativo para CRM/GWS.

## Cuenta emisora

```text
gerencia@skilland.ai
```

## Voz y firma

Voz: Romina Ojeda Brito.

Firma esperada: firma Gmail/GWS de `gerencia@skilland.ai`.

No hardcodear firma en el cuerpo salvo que CRM/GWS confirme que Gmail no la inserta automaticamente.

## Asunto final Email 1

```text
Una preocupación que quería compartir con usted
```

## Adjuntos por etapa

| Etapa | Adjunto |
|---|---|
| Email 1 | `Mujeres, IA y el futuro del Trabajo - Presentacion corta — SkilLand.pdf` |
| Follow-up 1 | Sin dossier largo. |
| Follow-up 2 | Dossier largo / white paper. |
| Retargeting futuro | Dossier largo / white paper u otro contenido validado. |

Archivo de white paper sugerido:

```text
Mujeres, IA y el Futuro del Trabajo - Informe largo white paper para impactos posteriores o retargeting a quien no responda — SkilLand.pdf
```

CRM/GWS debe validar nombres exactos de archivo antes de crear drafts.

## Secuencia

| Paso | Timing | Accion |
|---|---|---|
| Email 1 | Inicio | Enviar presentacion corta y abrir conversacion. |
| Follow-up 1 | 10 dias despues de Email 1 | Retomar sin presion y facilitar derivacion. |
| Follow-up 2 | 10 dias despues de Follow-up 1 | Compartir white paper como ultimo intento suave. |
| Nurturing | Posterior | Mantener contacto para retargeting futuro. |

## Tandas de envio

Recomendacion operativa:

- tandas de 5 en 5;
- revision humana previa de cada draft;
- una tanda puede ejecutarse minutos despues de otra si todo esta correcto;
- no convertir esto todavia en dashboard ni centro de mando.

## Criterios para pausar o revisar

Pausar antes de la siguiente tanda si aparece:

- rebotes relevantes;
- errores de personalizacion;
- respuestas negativas que indiquen problema de enfoque;
- problema con adjunto;
- problema con firma;
- tono incorrecto;
- senales de mala entregabilidad;
- confusion por destinatario, area o entidad.

## Campos necesarios

- `[nombre]`
- `[entidad]`
- `[territorio]`
- `[area]`
- `[tipo_organizacion]`
- `[personalizacion_1]`

`[personalizacion_1]` es recomendable guardarlo en CRM/deal si el equipo lo ve facil, pero no debe bloquear la ejecucion. Si falta, usar linea institucional generica.

## Eventos conceptuales a registrar

- `draft_created`
- `email_sent`
- `reply_received`
- `bounce_detected`
- `meeting_proposed`
- `meeting_booked`
- `nurturing`

`email_opened`, si existe, es senal debil. No es KPI principal ni stage comercial.

## Metricas conceptuales

- Metrica principal: reunion agendada.
- Metrica secundaria: respuesta positiva, conversacion iniciada o derivacion correcta.
- Sin respuesta no es cierre; pasa a follow-up o nurturing.
- Aperturas no son KPI principal.

Dashboard y centro de mando quedan para CRM/GWS, no para Funnel Academy.

## Proceso comercial a comunicar

- Reunion inicial.
- Posible jornada divulgativa y de escucha en territorio.
- Entregable asociado especializado en el contexto y con informacion recogida en terreno.
- Diseno de proyecto a medida.
- Objetivos, financiacion y KPIs de impacto.

No sonar a "charla gratis" ni a venta agresiva. Posicionar como colaboracion institucional y proceso de co-diseno.

## Cosas que NO debe hacer Funnel Academy

- No enviar emails.
- No crear workflows.
- No tocar CRM.
- No tocar GWS.
- No implementar dashboard.
- No seleccionar ni modificar contactos reales.

## Cosas que debe hacer CRM/GWS despues

- Seleccionar tanda.
- Crear drafts.
- Validar firma.
- Validar adjuntos.
- Revisar personalizacion.
- Enviar.
- Registrar eventos.
- Controlar respuestas.
- Pasar interesados a gestion humana.
- Pasar sin respuesta a follow-up o nurturing.

## Respuestas manuales

Respuestas positivas, derivaciones y peticiones de informacion se gestionan manualmente por Romina/Raul/equipo. No se entrega playbook extenso en este sprint.

## Validaciones externas pendientes

- Firma automatica Gmail/GWS.
- Adjuntos reales y nombre exacto de archivo.
- Seleccion de tanda inicial.
- Revision humana de drafts.
