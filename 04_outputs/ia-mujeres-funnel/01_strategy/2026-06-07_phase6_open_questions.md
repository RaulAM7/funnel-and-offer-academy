# Phase 6.1 Open Questions — IA Mujeres Funnel

Este documento sustituye la lista inicial de `Unknowns` de Fase 6 tras feedback humano. La estrategia base existe, pero no se considera cerrada del todo hasta validar Email 1 v2, reglas de personalizacion y primera tanda operativa.

## Decisiones resueltas por feedback humano

- Voz del Email 1: Romina Ojeda Brito.
- Cuenta emisora definitiva: `gerencia@skilland.ai`.
- No usar `direccion@skilland.ai`, `sales@reboot.academy` ni varias cuentas para esta campana.
- Firma esperada en Gmail/GWS, no hardcodeada en el cuerpo del Email 1:

```text
Romina Ojeda Brito
Presidenta | WISE Canarias (Women In STEAM Empowerment Canarias)
Gerente | Instituto de Innovacion Tecnologica y Educativa para el Desarrollo
CEO | Reboot Academy
gerencia@skilland.ai | www.skilland.ai
+34 685 81 06 90
```

- En primer contacto se adjunta la presentacion corta: `Mujeres, IA y el futuro del Trabajo - Presentacion corta — SkilLand.pdf`.
- No se adjunta el dossier largo en Email 1; queda como activo posterior para seguimiento, retargeting o contactos que respondan.
- Para la primera tanda se usara una plantilla unificada para cabildos, ayuntamientos y registros actuales.
- La personalizacion sera ligera mediante campos CRM: nombre, entidad, territorio, area, tipo de organizacion y posible linea de contexto.
- No hay piloto estrategico restrictivo.
- La ejecucion sera progresiva por tandas pequenas, con revision humana de drafts antes de enviar.
- El objetivo operativo es cubrir el dataset actual de 100+ registros si la calidad lo permite.
- Funnel Academy no implementa workflows, no toca CRM y no toca GWS.
- Workflows, automatizaciones y validaciones tecnicas corresponden al repo/equipo CRM-GWS.
- Business Line y Campaign no se reabren en esta iteracion.
- Asociaciones quedan para segundo sprint; ahora se trabaja con cabildos, ayuntamientos y registros actuales del CRM.

## Pendientes reales antes de Fase 7

- `Resolved` — link de LinkedIn de Romina recuperado del PDF inicial.
- `Unknown` — bio oficial ampliada de Romina, solo si se quiere enriquecer la autoridad de la firma.
- `Pending human review` — validacion final de Email 1 v2.
- `Pending human review` — seleccion o revision de la primera tanda de envio.
- `Pending CRM validation` — confirmacion de que los campos disponibles permiten aplicar las reglas de personalizacion sin inventar datos.
- `Pending decision` — asunto final entre el recomendado y las alternativas propuestas.
- `Pending decision` — criterio exacto para pausar, ajustar o continuar entre tandas.

## Decisiones de copy para Email 1 v2

- Mantener tono institucional, cercano y no paternalista.
- No vender "curso de IA para mujeres".
- Presentar SkilLand IA Mujeres como conversacion estrategica sobre empoderamiento femenino en IA, futuro del trabajo e impacto territorial.
- Reforzar Reboot como proyecto nacido en Canarias para ayudar a personas y colectivos con barreras de acceso a oportunidades tecnologicas a reiniciar su trayectoria profesional.
- Usar la cifra de mas de 1.000 estudiantes como prueba de impacto, no como vanity metric aislada.
- Explicar la IA como riesgo de nueva exclusion laboral femenina o como oportunidad historica si se actua a tiempo.
- Quitar enlace frio de calendario.
- CTA recomendado: primera reunion adaptable a llamada, videollamada o encuentro presencial.

## No bloqueos actuales

- La falta de bio publica de Romina no bloquea Email 1 v2.
- La falta de dataset tabular de asociaciones no bloquea esta tanda.
- La no implementacion de workflows desde Funnel Academy no bloquea el diseno comercial ni el copy.
- El smoke test CRM/GWS puede seguir en paralelo; sus resultados se incorporaran cuando esten validados por el equipo tecnico.

## Actualizacion Fase 6.1 — enlaces y firma

### Decisiones integradas

- Los hipervinculos del PDF inicial se han recuperado e incorporado al Email 1 v2 donde encajan mejor.
- No se reincorpora el link frio de calendario; el PDF inicial no conserva ningun hipervinculo real en la frase "aqui link".
- No se hardcodea la firma en el cuerpo del email.

### Pendiente tecnico real

- `Unknown` — confirmar si GWS/Gmail anade automaticamente la firma de `gerencia@skilland.ai` al crear/enviar drafts reales.
- Si la firma no aparece, decidir si el equipo CRM-GWS inyecta una firma HTML controlada fuera del cuerpo de copy.

## Actualizacion Fase 6.1 — funnel validado

- El funnel queda organizado por tres carriles: respuesta/reunion, no respuesta/retargeting y cierre/bloqueo.
- `email_opened` queda como senal debil, no como stage.
- `reply_received` queda como evento fuerte.
- `meeting_booked` / reunion agendada queda como conversion primaria.
- `Sin respuesta` queda como estado temporal para follow-up o nurturing, no como cierre automatico.
