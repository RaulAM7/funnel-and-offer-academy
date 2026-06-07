# CRM MIGRATION MAP

Mapping del CRM antiguo (Twenty) al nuevo modelo de Attio.

## Fuentes de datos

| Source | Type | Status |
|---|---|---|
| Twenty CRM | REST API / DB export | Unknown — verificar acceso |
| Google Contacts | Google API / export CSV | Unknown — verificar permisos |
| Gmail | Google API | Unknown — solo para contexto |
| Google Drive | Google API | Unknown — solo para propuestas |
| Raw CSVs | Files en `00_inbox/raw_contact_lists/` | Pendiente de recibir |

## Stage mapping: Twenty → Attio

| Twenty stage | Attio stage |
|---|---|
| Posible oportunidad | No contactado |
| Contactado / en conversación | En conversación |
| En reuniones / diagnóstico | Reunión / diagnóstico |
| Propuesta / negociación | Negociación |
| Propuesta enviada | Propuesta enviada |
| Ganado | Ganado |
| Perdido | Perdido |
| Dormido | Dormido |

Default para stages desconocidos: `No contactado`

Ver también: `config/pipeline_stages.yaml`

## Object mapping

| Twenty entity | Attio object |
|---|---|
| Contact / Person | people |
| Company / Organization | companies |
| Opportunity / Deal | deals |
| Activity / Note | note (on record) |
| Task | task (on record) |

## Field mapping: companies (Twenty → Attio)

| Twenty field | Attio attribute | Notes |
|---|---|---|
| `id` | `old_crm_id` | Guardar para trazabilidad |
| `name` | `name` | Estándar |
| `domain_name` | `domains` | Estándar Attio |
| `address.city` | `city` | Custom |
| `address.country` | `country` | Custom |
| `industry` | `sector` | Custom |
| `linked_in_url` | `linkedin_url` | Custom |
| (no equivalent) | `company_type` | Mapear manualmente o deducir |
| (no equivalent) | `strategic_priority` | Deducir o pedir al equipo |

## Field mapping: people (Twenty → Attio)

| Twenty field | Attio attribute | Notes |
|---|---|---|
| `id` | `old_crm_id` | Guardar para trazabilidad |
| `name.first + name.last` | `name` | Concatenar |
| `emails[0].email` | `email_addresses` | Primary email |
| `phones[0].number` | `phone_numbers` | |
| `job_title` | `job_title` | Custom |
| `linked_in_url` | `linkedin_url` | Custom |
| `company.id` | `company` | Record reference — resolver por nombre/dominio |

## Field mapping: deals (Twenty → Attio)

| Twenty field | Attio attribute | Notes |
|---|---|---|
| `id` | `old_crm_id` | Guardar para trazabilidad |
| `name` | `name` | |
| `company.id` | `company` | Resolver por nombre/old_crm_id |
| `point_of_contact.id` | `main_contact` | Resolver por email |
| `amount.amount` | `amount` | |
| `amount.currency_code` | `currency` | |
| `close_date` | `expected_close_date` | |
| `stage` | `stage` (entry) | Ver stage mapping arriba |
| (no equivalent) | `business_line` | Mapear manualmente |
| (no equivalent) | `deal_source` | Poner `Old CRM` por defecto |

## Migration rules

1. **Migrar solo deals activos o con valor histórico** (no todos los dormidos o perdidos viejos).
2. **Preservar relaciones**: company → people → deals deben estar vinculados.
3. **Guardar `old_crm_id`** en todos los records migrados para trazabilidad y dedup.
4. **No migrar duplicados**: si ya existe en Attio (por email/dominio), hacer update, no create.
5. **Crear nota de migración** en cada deal migrado con: `Migrado desde Twenty CRM. Old ID: <id>. Fecha migración: <date>`.
6. **No migrar notas y tareas antiguas** de forma masiva — migrar solo lo que tenga valor.

## Unknown / to verify

- Acceso al API de Twenty o export de DB
- Total de records en Twenty: people, companies, deals
- Calidad de datos en Twenty (emails válidos, empresas duplicadas, etc.)
- Deals activos vs inactivos en Twenty
