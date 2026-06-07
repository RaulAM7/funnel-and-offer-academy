# Dataset File Locations — IA Mujeres

## Datasets localizados pero no copiados completos

| original_path | size_bytes | approx_rows | description | recommendation_phase_6 |
|---|---:|---:|---|---|
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/organizations_clean.csv` | 54084 | 95 organizations + header | Dataset normalizado de organizaciones para importación CRM. | No copiar en Fase 4. Usar como referencia remota y valorar snapshot en Fase 6 solo si hace falta revisión operativa fina. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/contacts_clean.csv` | 157803 | 166 contacts + header | Dataset normalizado de contactos institucionales y personales. | No copiar por defecto en Fase 4. Consultar en origen; snapshot solo si la Fase 6 necesita segmentación detallada fuera del repo fuente. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/import_ready_combined.csv` | 224672 | ~261 records + header | Vista combinada organization/contact para revisión e importación. | No copiar por defecto. Es útil para QA y mapping, pero añade peso y duplica datasets ya descritos en los reportes. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/organizations_clean.json` | 89501 | ~95 objects | Export JSON de organizaciones limpias. | No copiar en Fase 4. Mantener solo ubicación y usar si una fase posterior necesita consumo programático. |
| `/home/reboot/Escritorio/agentic-scrapping-Experiment-scrappling/04_outputs/skilland_ia_mujeres/data_prep/contacts_clean.json` | 229230 | ~166 objects | Export JSON de contactos limpios. | No copiar en Fase 4. Consultar en origen; snapshot solo si se justifica para tooling posterior. |

## Nota

Las cifras de filas son aproximadas y se apoyan en los reportes `2026-06-04_data_quality_report.md` y `2026-06-04_dataset_inventory.md` del repo de scraping.
