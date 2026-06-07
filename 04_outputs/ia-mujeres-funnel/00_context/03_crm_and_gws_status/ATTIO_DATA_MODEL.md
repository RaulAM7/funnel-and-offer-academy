# ATTIO DATA MODEL

Modelo de datos deseado para el workspace de Skilland en Attio.

## Objects base (usar estándar Attio)

```
people      → Contactos / personas
companies   → Empresas, universidades, instituciones, administraciones
deals       → Oportunidades comerciales
```

No crear custom objects en sprint 1. Revisar si son necesarios después de inspeccionar el workspace.

---

## Object: companies

### Atributos estándar (ya existen en Attio)
- `name`
- `domains`

### Atributos custom a crear

| api_slug | Title | Type | Required |
|---|---|---|---|
| `company_type` | Company Type | select | No |
| `sector` | Sector | text | No |
| `subsector` | Subsector | text | No |
| `country` | Country | text | No |
| `region` | Region | text | No |
| `city` | City | text | No |
| `linkedin_url` | LinkedIn URL | text | No |
| `source` | Source | select | No |
| `strategic_priority` | Strategic Priority | select | No |
| `business_line_interest` | Business Line Interest | multiselect | No |
| `public_private_type` | Public/Private Type | select | No |
| `notes_summary` | Notes Summary | text | No |
| `old_crm_id` | Old CRM ID | text | No |
| `last_interaction_date` | Last Interaction Date | date | No |

### Options: company_type
```
University
University Foundation
Chamber of Commerce
Public Administration
Cluster / Association
Private Company
Training Provider
Technology Partner
Healthcare Company
Tourism Company
Consultancy
Other
```

### Options: public_private_type
```
Public
Private
Mixed
Third Sector
Unknown
```

### Options: strategic_priority (companies)
```
Low
Medium
High
Strategic
```

---

## Object: people

### Atributos estándar (ya existen en Attio)
- `name`
- `email_addresses`
- `phone_numbers`
- `company` (record reference)

### Atributos custom a crear

| api_slug | Title | Type | Required |
|---|---|---|---|
| `job_title` | Job Title | text | No |
| `linkedin_url` | LinkedIn URL | text | No |
| `source` | Source | select | No |
| `role_in_deal` | Role in Deal | select | No |
| `decision_maker_level` | Decision Maker Level | select | No |
| `preferred_language` | Preferred Language | select | No |
| `region` | Region | text | No |
| `country` | Country | text | No |
| `old_crm_id` | Old CRM ID | text | No |
| `last_interaction_date` | Last Interaction Date | date | No |
| `notes_summary` | Notes Summary | text | No |

### Options: role_in_deal
```
Decision Maker
Influencer
Technical Contact
Economic Buyer
Champion
Gatekeeper
Operational Contact
Unknown
```

### Options: decision_maker_level
```
Low
Medium
High
Final Decision Maker
Unknown
```

### Options: preferred_language
```
Spanish
English
French
Portuguese
Other
Unknown
```

---

## Object: deals

### Atributos estándar (ya existen en Attio)
- `name`
- `company` (record reference)

### Atributos custom a crear

| api_slug | Title | Type | Required |
|---|---|---|---|
| `main_contact` | Main Contact | record-reference (people) | No |
| `business_line` | Business Line | select | No |
| `deal_source` | Deal Source | select | No |
| `amount` | Amount | number | No |
| `currency` | Currency | text | No |
| `expected_close_date` | Expected Close Date | date | No |
| `strategic_priority` | Strategic Priority | select | No |
| `deal_type` | Deal Type | select | No |
| `proposal_url` | Proposal URL | text | No |
| `old_crm_id` | Old CRM ID | text | No |
| `summary` | Summary | text | No |

### Options: business_line
```
Skilland MicroCred
Skilland LMS / EduKami
Skilland Pro
AI Training / Workshops
European Projects
CRM / Automation
Custom AI Solution
Other
```

### Options: deal_source
```
Transfiere
Referral
Inbound
Outbound
Existing Network
Google Contacts
Email
Event
Public Tender
Partner
Old CRM
Manual
Other
```

### Options: deal_type
```
University Pilot
Microcredential Project
LMS Platform
Training Package
AI Workshop
Consulting
Custom Development
European Project
Public Sector Contract
Private Sector Contract
Other
```

---

## List: sales_pipeline

```
api_slug:      sales_pipeline
name:          Sales Pipeline
parent_object: deals
```

### Entry attributes

| api_slug | Title | Type | Required |
|---|---|---|---|
| `stage` | Stage | status | Yes |
| `owner` | Owner | user | No |
| `next_action` | Next Action | text | No |
| `next_action_date` | Next Action Date | date | No |
| `last_interaction_summary` | Last Interaction Summary | text | No |
| `last_interaction_date` | Last Interaction Date | date | No |
| `proposal_status` | Proposal Status | select | No |
| `probability` | Probability | number | No |
| `blocker` | Blocker | text | No |
| `priority` | Priority | select | No |
| `temperature` | Temperature | select | No |
| `forecast_category` | Forecast Category | select | No |
| `lost_reason` | Lost Reason | select | No |

### Options: stage (status)
```
No contactado
Contactado
En conversación
Reunión / diagnóstico
Propuesta en preparación
Propuesta enviada
Negociación
Por firmar
Ganado
Perdido
Dormido
```

### Options: proposal_status
```
No aplica
Pendiente de preparar
En preparación
En revisión interna
Enviada
Requiere cambios
Aceptada
Rechazada
```

### Options: priority
```
Low
Medium
High
Critical
```

### Options: temperature
```
Cold
Warm
Hot
Very Hot
Dormant
```

### Options: forecast_category
```
Pipeline
Best Case
Commit
Closed Won
Closed Lost
```

### Options: lost_reason
```
No budget
No timing
No decision
Competitor
Bad fit
Lost contact
Internal blocker
Price
Other
Unknown
```

---

## Other lists (backlog — do not create in sprint 1)

```
university_pipeline
public_sector_pipeline
africantech_pipeline
partners
lead_lists
event_leads
proposal_tracking
customer_success
```
