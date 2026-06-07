# PIPELINE DESIGN

Diseño del pipeline comercial principal de Skilland en Attio.

## Pipeline principal

```
List name:    Sales Pipeline
api_slug:     sales_pipeline
Parent object: deals
```

## Stages del pipeline (atributo `stage`, tipo `status`)

Los stages modelan el avance de cada oportunidad comercial.

```
No contactado          → Lead identificado pero sin contacto aún
Contactado             → Se ha hecho primer contacto (email, LinkedIn, etc.)
En conversación        → Hay diálogo activo con el contacto
Reunión / diagnóstico  → Se ha tenido o agendado una reunión
Propuesta en preparación → Estamos trabajando la propuesta
Propuesta enviada      → Propuesta enviada y esperando respuesta
Negociación            → Negociación activa de condiciones
Por firmar             → Acuerdo casi cerrado, pendiente de firma
Ganado                 → Deal cerrado y confirmado
Perdido                → Deal descartado
Dormido                → Deal en pausa sin fecha de reactivación
```

## Flujo típico de un deal

```
No contactado
    ↓
Contactado
    ↓
En conversación
    ↓
Reunión / diagnóstico
    ↓
Propuesta en preparación
    ↓
Propuesta enviada ←→ Negociación
    ↓
Por firmar
    ↓
Ganado

Salidas alternativas en cualquier punto:
    → Perdido
    → Dormido
```

## Atributos de entry en el pipeline

### Obligatorios de completar para operar el pipeline

- `stage`: dónde está el deal
- `owner`: quién lleva el deal (usuario de Attio)
- `next_action`: qué hay que hacer a continuación
- `next_action_date`: cuándo
- `priority`: Low / Medium / High / Critical

### Opcionales pero muy útiles

- `last_interaction_summary`: resumen de la última interacción
- `last_interaction_date`: cuándo fue
- `proposal_status`: estado de la propuesta
- `probability`: % estimado de cierre (0-100)
- `blocker`: qué está bloqueando el avance
- `temperature`: Cold / Warm / Hot / Very Hot / Dormant
- `forecast_category`: para forecasting
- `lost_reason`: por qué se perdió (solo si stage = Perdido)

## Relación con deal record

El deal record (en el object `deals`) tiene:
- `name`: nombre descriptivo del deal
- `company`: empresa relacionada
- `main_contact`: persona de contacto principal
- `business_line`: línea de negocio de Skilland
- `deal_source`: cómo llegó el lead
- `amount`: importe estimado
- `expected_close_date`: fecha esperada de cierre
- `deal_type`: tipo de deal
- `old_crm_id`: ID en el CRM anterior (para migración)

El entry en `sales_pipeline` añade los atributos del proceso encima del deal record.

## Pipelines adicionales (backlog)

No crear hasta que el pipeline principal esté operativo:

```
university_pipeline      → Pipeline específico para universidades
public_sector_pipeline   → Administraciones y sector público
africantech_pipeline     → Proyectos internacionales/AfricanTech
proposal_tracking        → Seguimiento de propuestas enviadas
lead_lists               → Listados de leads por segmento
```

## Reglas operativas del pipeline

- Un deal solo puede estar en `Perdido` si se indica `lost_reason`.
- Un deal en `Dormido` debe tener una nota explicando por qué.
- Los deals en `Propuesta enviada` o `Negociación` deben tener `next_action_date`.
- `forecast_category` se rellena a partir de `Por firmar` en adelante.
