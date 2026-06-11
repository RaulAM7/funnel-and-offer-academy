# CRM/GWS Execution Handoff — IA Mujeres

## Estado del handoff

Funnel Academy deja cerrado el sprint estrategico/copy minimo de IA Mujeres con Email 1 v4.1 como version vigente.

El siguiente paso vive en CRM/GWS, previsiblemente en el repo `skilland-crm`. La version v4.1 ya fue sincronizada alli para las siguientes tandas.

No implementar desde este repo.

## Alcance entregado por Funnel Academy

- Funnel validado: conversacion institucional first.
- Email 1 v4.1 final aprobado como base.
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

Firma minima incluida en el cuerpo: `Romina Ojeda Brito`.

No depender de firma automatica Gmail/GWS para que el email quede firmado.

## Asunto final Email 1

```text
Una preocupación que quería compartir con usted
```

Template vigente:

```text
04_email_sequence/2026-06-11_email_01_v4_1.md
```

## Adjuntos por etapa

| Etapa | Adjunto |
|---|---|
| Email 1 | `Mujeres, IA y el Futuro del Trabajo · Dossier — SkilLand v2.pdf` |
| Follow-up 1 | Sin dossier largo. |
| Follow-up 2 | Dossier largo / white paper. |
| Retargeting futuro | Dossier largo / white paper u otro contenido validado. |

Archivo de white paper sugerido:

```text
Mujeres, IA y el Futuro del Trabajo - Informe largo white paper para impactos posteriores o retargeting a quien no responda — SkilLand.pdf
```

El dosier breve azul v2 figura en el workspace de Funnel Academy, pero CRM/GWS debe validar disponibilidad operativa y nombres exactos de archivo antes de crear drafts.

## Secuencia

| Paso | Timing | Accion |
|---|---|---|
| Email 1 | Inicio | Enviar dosier breve azul v2 y abrir conversacion. |
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

## Variables minimas Email 1 v4.1

- `{{saludo_nombre}}`
- `{{territorio}}`
- `{{derivacion_si_corresponde}}`

`{{saludo_nombre}}` se calcula desde nombre de pila:

- femenino reconocido: `Estimada {nombre}`;
- masculino reconocido: `Estimado {nombre}`;
- nombre no reconocido: `Estimado {nombre}`;
- sin nombre usable: `Estimado equipo`.

No usar `Estimado/a` ni nombre completo en el saludo.

`{{territorio}}` debe ser municipio para ayuntamientos e isla para cabildos.

`{{derivacion_si_corresponde}}` solo se usa cuando el buzon sea generico o exista duda de interlocutor. Si no aplica, queda vacio.

Texto recomendado:

```text
Si cree que esta conversación corresponde a otra persona del equipo, le agradecería mucho que pudiera reenviárselo o indicarme con quién hablar.
```

CRM puede conservar reglas amplias de segmentacion y personalizacion para revision, priorizacion y follow-ups, pero Email 1 v4.1 no depende de `[area]`, `[tipo_organizacion]` ni `[personalizacion_1]` en el cuerpo base.

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
- Objetivos concretos y KPIs de impacto.

No sonar a "charla gratis" ni a venta agresiva. Posicionar como colaboracion institucional y proceso de co-diseno.

## Sincronizacion CRM

El repo `Skilland-ai/skilland-crm` queda sincronizado con:

- template vigente de Email 1 v4.1;
- asunto;
- variables mínimas;
- adjunto Email 1: dosier breve azul v2;
- reglas de derivación para buzones genéricos;
- eliminación del LinkedIn de Romina;
- eliminación de referencias económicas o presupuestarias en Email 1;
- validación de firma explicita en cuerpo.

No implementar nada de CRM desde este repo.

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
- Validar firma explicita en cuerpo.
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

- Firma explicita en cuerpo.
- Adjuntos reales, disponibilidad operativa y nombre exacto de archivo.
- Seleccion de tanda inicial.
- Revision humana de drafts.
