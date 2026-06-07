# Context Setup Report — IA Mujeres Funnel

- Date: 2026-06-07
- Scope: setup administrativo de contexto para `04_outputs/ia-mujeres-funnel/`
- Status: completed

## 1. Carpetas creadas

```text
04_outputs/ia-mujeres-funnel/
├── STATE.md
├── 00_context/
│   ├── 2026-06-07_context_setup_report.md
│   ├── 00_context_index.md
│   ├── 01_product_strategy/
│   ├── 02_icp_and_data/
│   ├── 03_crm_and_gws_status/
│   ├── 04_existing_assets/
│   └── 05_constraints/
├── 01_strategy/
├── 02_funnel_map/
├── 03_offer_positioning/
├── 04_email_sequence/
├── 05_crm_implementation_notes/
└── 06_outputs_ready_for_execution/
```

## 2. Documentos encontrados y copiados

| source_repo | source_path | destination_path | category | notes |
|---|---|---|---|---|
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/skilland_ia_mujeres_documento_estrategico.md` | `00_context/01_product_strategy/skilland_ia_mujeres_documento_estrategico.md` | product_strategy | Documento estratégico operativo principal. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/Mujeres, IA y el Futuro del Trabajo — SkilLand.md` | `00_context/01_product_strategy/Mujeres, IA y el Futuro del Trabajo — SkilLand.md` | product_strategy | Dossier largo en markdown. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/Mujeres, IA y el futuro del Trabajo - Presentación — SkilLand (1).pdf` | `00_context/01_product_strategy/Mujeres, IA y el futuro del Trabajo - Presentación — SkilLand (1).pdf` | product_strategy | Presentación/deck en PDF. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland_ia_mujeres/data_prep/2026-06-04_data_quality_report.md` | `00_context/02_icp_and_data/2026-06-04_data_quality_report.md` | icp_and_data | Reporte de calidad del dataset. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland_ia_mujeres/data_prep/2026-06-04_dataset_inventory.md` | `00_context/02_icp_and_data/2026-06-04_dataset_inventory.md` | icp_and_data | Inventario de datasets y trazabilidad. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland_ia_mujeres/data_prep/2026-06-04_twenty_import_mapping.md` | `00_context/02_icp_and_data/2026-06-04_twenty_import_mapping.md` | icp_and_data | Mapping CRM Twenty. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/cabildos_contactos_igualdad_social/directorio_cabildos_igualdad_social.md` | `00_context/02_icp_and_data/directorio_cabildos_igualdad_social.md` | icp_and_data | Directorio narrativo/tabular de cabildos. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/cabildos_contactos_igualdad_social/scraping_notes.md` | `00_context/02_icp_and_data/scraping_notes.md` | icp_and_data | Notas de fuentes y metodología. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/ayuntamientos_contactos_igualdad_social/directorio_ayuntamientos_igualdad_social.md` | `00_context/02_icp_and_data/directorio_ayuntamientos_igualdad_social.md` | icp_and_data | Directorio narrativo/tabular de ayuntamientos. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/ayuntamientos_contactos_igualdad_social/coverage_report.md` | `00_context/02_icp_and_data/coverage_report.md` | icp_and_data | Cobertura del directorio municipal. |
| `agentic-scrapping-Experiment-scrappling` | `04_outputs/skilland-ia-mujeres/ayuntamientos_contactos_igualdad_social/scraping_notes_ayuntamientos.md` | `00_context/02_icp_and_data/scraping_notes_ayuntamientos.md` | icp_and_data | Metodología y notas de scraping municipal. |
| `skilland-crm` | `03_specs/now/002_ia_mujeres_crm_import.md` | `00_context/03_crm_and_gws_status/002_ia_mujeres_crm_import.md` | crm_status | Spec activa de importación IA Mujeres. |
| `skilland-crm` | `03_specs/now/003_ia_mujeres_crm_workflows.md` | `00_context/03_crm_and_gws_status/003_ia_mujeres_crm_workflows.md` | crm_status | Spec de workflows IA Mujeres. |
| `skilland-crm` | `03_specs/now/004_ia_mujeres_crm_smoke_test.md` | `00_context/03_crm_and_gws_status/004_ia_mujeres_crm_smoke_test.md` | crm_status | Spec de smoke test IA Mujeres. |
| `skilland-crm` | `04_outputs/ia_mujeres_crm_import/2026-06-04_ia_mujeres_crm_import_dry_run.md` | `00_context/03_crm_and_gws_status/2026-06-04_ia_mujeres_crm_import_dry_run.md` | crm_status | Dry run de importación. |
| `skilland-crm` | `04_outputs/ia_mujeres_crm_import/2026-06-04_ia_mujeres_crm_import_report.md` | `00_context/03_crm_and_gws_status/2026-06-04_ia_mujeres_crm_import_report.md` | crm_status | Resultado de importación. |
| `skilland-crm` | `04_outputs/ia_mujeres_workflows/2026-06-04_ia_mujeres_workflow_design.md` | `00_context/03_crm_and_gws_status/2026-06-04_ia_mujeres_workflow_design.md` | crm_status | Diseño de workflows. |
| `skilland-crm` | `04_outputs/ia_mujeres_workflows/2026-06-04_workflow_capabilities_audit.md` | `00_context/03_crm_and_gws_status/2026-06-04_workflow_capabilities_audit.md` | crm_status | Auditoría de capacidades workflow. |
| `skilland-crm` | `04_outputs/ia_mujeres_workflows/2026-06-04_workflow_implementation_result.md` | `00_context/03_crm_and_gws_status/2026-06-04_workflow_implementation_result.md` | crm_status | Resultado de implementación de workflows. |
| `skilland-crm` | `04_outputs/ia_mujeres_smoke_test/2026-06-04_smoke_test_report.md` | `00_context/03_crm_and_gws_status/2026-06-04_smoke_test_report.md` | crm_status | Reporte de smoke test CRM. |
| `SkilLand-Attio-CRM-Operations` | `02_context/ATTIO_DATA_MODEL.md` | `00_context/03_crm_and_gws_status/ATTIO_DATA_MODEL.md` | crm_status | Contexto adicional de modelado CRM. |
| `SkilLand-Attio-CRM-Operations` | `02_context/CRM_MIGRATION_MAP.md` | `00_context/03_crm_and_gws_status/CRM_MIGRATION_MAP.md` | crm_status | Contexto adicional de migración CRM. |
| `SkilLand-Attio-CRM-Operations` | `02_context/PIPELINE_DESIGN.md` | `00_context/03_crm_and_gws_status/PIPELINE_DESIGN.md` | crm_status | Contexto adicional de pipeline CRM. |
| `google-workspace-CLI-Experiment` | `04_outputs/ia_mujeres_gws_cli/2026-06-04_crm_email_event_contract.md` | `00_context/03_crm_and_gws_status/2026-06-04_crm_email_event_contract.md` | gws_status | Contrato de eventos CRM/email. |
| `google-workspace-CLI-Experiment` | `04_outputs/ia_mujeres_gws_cli/2026-06-04_gws_cli_audit.md` | `00_context/03_crm_and_gws_status/2026-06-04_gws_cli_audit.md` | gws_status | Auditoría del CLI. |
| `google-workspace-CLI-Experiment` | `04_outputs/ia_mujeres_gws_cli/2026-06-04_gws_smoke_test_report.md` | `00_context/03_crm_and_gws_status/2026-06-04_gws_smoke_test_report.md` | gws_status | Reporte smoke test GWS. |
| `google-workspace-CLI-Experiment` | `04_outputs/ia_mujeres_gws_cli/2026-06-04_multi_account_setup_plan.md` | `00_context/03_crm_and_gws_status/2026-06-04_multi_account_setup_plan.md` | gws_status | Setup multi-account. |
| `google-workspace-CLI-Experiment` | `04_outputs/ia_mujeres_gws_cli/2026-06-04_operator_guide.md` | `00_context/03_crm_and_gws_status/2026-06-04_operator_guide.md` | gws_status | Guía operativa. |

## 3. Documentos no encontrados

| expected_document | searched_locations | impact |
|---|---|---|
| Repo exacto `../skilland-crm` en raíz de workspace | `../skilland-crm` | Sin bloqueo. Se encontró equivalente útil en `../Skilland.ai/Skilland.ai-CRM/skilland-crm`. |
| Repo exacto `../gws-cli` | `../gws-cli` | Sin bloqueo. No existe con ese nombre. |
| Repo exacto `../cli-gws` | `../cli-gws` | Sin bloqueo. No existe con ese nombre. |
| Repo exacto `../google-workspace-cli` | `../google-workspace-cli` | Sin bloqueo. No existe con ese nombre. |
| Repo exacto `../Google-Workspace-CLI` | `../Google-Workspace-CLI` | Sin bloqueo. Se usó `../google-workspace-CLI-Experiment` como equivalente localizado. |
| Borrador real de `Current Email 01` | `funnel-and-offer-academy`, `agentic-scrapping-Experiment-scrappling`, `Skilland.ai/Skilland.ai-CRM`, `google-workspace-CLI-Experiment` | Impacto bajo para Fase 6; impacto alto para Fase 7. Se dejó placeholder. |
| Notas reales de Romina Ojeda | `funnel-and-offer-academy`, `agentic-scrapping-Experiment-scrappling`, `Skilland.ai/Skilland.ai-CRM`, `google-workspace-CLI-Experiment` | Impacto bajo para Fase 6; impacto medio para posicionamiento fino y copy. Se dejó placeholder. |
| Dataset tabular suficiente de asociaciones | Reportes e inventario de `agentic-scrapping-Experiment-scrappling` | Sin bloqueo para el arranque actual. Limita la expansión futura del ICP fuera de cabildos y ayuntamientos. |

## 4. Archivos omitidos por seguridad o tamaño

| source_path | reason_omitted | notes |
|---|---|---|
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/organizations_clean.csv` | tamaño/scope | Dataset tabular no copiado; documentado en `dataset_file_locations.md`. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/contacts_clean.csv` | tamaño/scope | Dataset tabular no copiado; documentado en `dataset_file_locations.md`. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/import_ready_combined.csv` | tamaño/scope | Dataset combinado no copiado; documentado en `dataset_file_locations.md`. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/organizations_clean.json` | tamaño/scope | JSON de apoyo para tooling; innecesario en este setup. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/contacts_clean.json` | tamaño/scope | JSON de apoyo para tooling; innecesario en este setup. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland-ia-mujeres/ayuntamientos_contactos_igualdad_social/fuentes_ayuntamientos.json` | scope | Útil para auditoría de trazabilidad, pero no necesario para el snapshot inicial. |
| `/home/reboot/Escritorio/Skilland.ai/Skilland.ai-CRM/skilland-crm/04_outputs/ia_mujeres_crm_import/2026-06-04_ia_mujeres_crm_import_dry_run.json` | scope | JSON técnico redundante respecto al `.md`. |
| `/home/reboot/Escritorio/Skilland.ai/Skilland.ai-CRM/skilland-crm/04_outputs/ia_mujeres_crm_import/2026-06-04_ia_mujeres_crm_import_report.json` | scope | JSON técnico redundante respecto al `.md`. |
| `/home/reboot/Escritorio/Skilland.ai/Skilland.ai-CRM/skilland-crm/scripts/.env` | seguridad | No copiar secretos ni credenciales. |
| `/home/reboot/Escritorio/Skilland.ai/Skilland.ai-CRM/skilland-crm/.env` | seguridad | No copiar secretos ni credenciales. |

## 5. Recomendación para Fase 6

- Contexto listo para Fase 6: `Sí`, con grounding suficiente para empezar diseño de funnel sin tocar todavía copy final.
- Lectura prioritaria para Claude/Codex:
  1. `05_constraints/known_constraints_and_decisions.md`
  2. `01_product_strategy/skilland_ia_mujeres_documento_estrategico.md`
  3. `01_product_strategy/Mujeres, IA y el Futuro del Trabajo — SkilLand.md`
  4. `02_icp_and_data/2026-06-04_data_quality_report.md`
  5. `02_icp_and_data/2026-06-04_dataset_inventory.md`
  6. `03_crm_and_gws_status/2026-06-04_ia_mujeres_crm_import_report.md`
  7. `03_crm_and_gws_status/2026-06-04_gws_cli_audit.md`
  8. `03_crm_and_gws_status/2026-06-04_operator_guide.md`
- Pendiente de pegado manual por el usuario:
  - borrador real del primer email;
  - notas reales, bio o positioning concreto de Romina Ojeda;
  - cualquier deck/propuesta adicional no versionada en los repos locales localizados.
- Bloqueos:
  - `Ninguno` para iniciar Fase 6.
  - `Sí` para Fase 7 si se quiere trabajar sobre el borrador real del primer email y no sobre placeholders.

