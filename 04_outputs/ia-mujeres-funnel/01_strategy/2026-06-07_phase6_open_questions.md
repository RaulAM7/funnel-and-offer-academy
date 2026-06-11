# Phase 6.1 Open Questions — IA Mujeres Funnel

Este documento sustituye la lista inicial de `Unknowns` de Fase 6 tras feedback humano. La estrategia base existe, pero no se considera cerrada del todo hasta validar Email 1 v4.1, reglas de personalizacion y primera tanda operativa.

## Decisiones resueltas por feedback humano

- Voz del Email 1: Romina Ojeda Brito.
- Cuenta emisora definitiva: `gerencia@skilland.ai`.
- No usar `direccion@skilland.ai`, `sales@reboot.academy` ni varias cuentas para esta campana.
- Firma minima incluida en el cuerpo de Email 1:

```text
Romina Ojeda Brito
Presidenta | WISE Canarias (Women In STEAM Empowerment Canarias)
Gerente | Instituto de Innovacion Tecnologica y Educativa para el Desarrollo
CEO | Reboot Academy
gerencia@skilland.ai | www.skilland.ai
+34 685 81 06 90
```

- En primer contacto se adjunta el dosier breve azul v2: `Mujeres, IA y el Futuro del Trabajo · Dossier — SkilLand v2.pdf`.
- No se adjunta el dossier largo en Email 1; queda como activo posterior para seguimiento, retargeting o contactos que respondan.
- Para la primera tanda se usara una plantilla unificada para cabildos, ayuntamientos y registros actuales.
- Email 1 v4.1 funciona con personalizacion ligera y variables minimas: saludo calculado, territorio naturalizado y derivacion si corresponde.
- No hay piloto estrategico restrictivo.
- La ejecucion sera progresiva por tandas pequenas, con revision humana de drafts antes de enviar.
- El objetivo operativo es cubrir el dataset actual de 100+ registros si la calidad lo permite.
- Funnel Academy no implementa workflows, no toca CRM y no toca GWS.
- Workflows, automatizaciones y validaciones tecnicas corresponden al repo/equipo CRM-GWS.
- Business Line y Campaign no se reabren en esta iteracion.
- Asociaciones quedan para segundo sprint; ahora se trabaja con cabildos, ayuntamientos y registros actuales del CRM.

## Pendientes reales antes de Fase 7

- `Resolved` — link de LinkedIn de Romina recuperado del PDF inicial, pero eliminado del Email 1 v4.1.
- `Unknown` — bio oficial ampliada de Romina, solo si se quiere enriquecer la autoridad de la firma.
- `Resolved` — validacion final del draft real de Email 1 v4.1 realizada en CRM/GWS con prueba interna.
- `Pending human review` — seleccion o revision de la primera tanda de envio.
- `Pending CRM validation` — confirmacion de que los campos disponibles permiten aplicar las reglas de personalizacion sin inventar datos.
- `Pending decision` — asunto final entre el recomendado y las alternativas propuestas.
- `Pending decision` — criterio exacto para pausar, ajustar o continuar entre tandas.

## Decisiones de copy para Email 1 v4.1

- Mantener tono institucional, cercano y no paternalista.
- No vender "curso de IA para mujeres".
- Presentar SkilLand IA Mujeres como conversacion estrategica sobre empoderamiento femenino en IA, futuro del trabajo e impacto territorial.
- Reforzar Reboot como proyecto nacido en Canarias para ayudar a personas y colectivos con barreras de acceso a oportunidades tecnologicas a reiniciar su trayectoria profesional.
- Usar la cifra de mas de 1.000 estudiantes como prueba de impacto, no como vanity metric aislada.
- Explicar la IA como riesgo de nueva exclusion laboral femenina o como oportunidad historica si se actua a tiempo.
- Quitar enlace frio de calendario.
- CTA recomendado: llamada breve la proxima semana.

## No bloqueos actuales

- La falta de bio publica de Romina no bloquea Email 1 v4.1.
- La falta de dataset tabular de asociaciones no bloquea esta tanda.
- La no implementacion de workflows desde Funnel Academy no bloquea el diseno comercial ni el copy.
- El smoke test CRM/GWS puede seguir en paralelo; sus resultados se incorporaran cuando esten validados por el equipo tecnico.

## Actualizacion Fase 6.1 — enlaces y firma

### Decisiones integradas

- Los hipervinculos del PDF inicial se recuperaron en fase previa, pero Email 1 v4.1 no incluye LinkedIn de Romina ni hipervinculos en su nombre.
- No se reincorpora el link frio de calendario; el PDF inicial no conserva ningun hipervinculo real en la frase "aqui link".
- La firma minima `Romina Ojeda Brito` se incluye en el cuerpo del email.

### Pendiente tecnico real

- `Resolved` — no depender de firma automatica GWS/Gmail; Email 1 v4.1 incluye firma minima en cuerpo.

## Actualizacion Fase 6.1 — funnel validado

- El funnel queda organizado por tres carriles: respuesta/reunion, no respuesta/retargeting y cierre/bloqueo.
- `email_opened` queda como senal debil, no como stage.
- `reply_received` queda como evento fuerte.
- `meeting_booked` / reunion agendada queda como conversion primaria.
- `Sin respuesta` queda como estado temporal para follow-up o nurturing, no como cierre automatico.
