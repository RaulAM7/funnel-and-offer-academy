# ICP2 Handoff to Scraping and CRM

- Fecha: 2026-06-12
- Modulo: SkilLand IA Mujeres
- Scope: handoff documental para otros repos
- No ejecutar desde Funnel Academy

## Estado

ICP2 `Asociaciones / ONG - Mujeres e Inclusion Tech` queda aprobado como ampliacion social/comunitaria del funnel IA Mujeres.

Este documento prepara el traspaso a scraping y CRM. Funnel Academy no scrapea, no crea CSVs reales, no toca CRM, no toca GWS, no envia emails y no modifica contactos reales.

## Para el repo de scraping

### Que buscar

Entidades canarias verificables que encajen con:

- asociaciones de mujeres;
- redes de mujeres STEAM;
- mujeres empresarias;
- igualdad, liderazgo femenino o talento femenino;
- ONG/fundaciones de inclusion social;
- inclusion tecnologica o digital;
- empleabilidad y formacion laboral;
- juventud, migracion, vulnerabilidad o desarrollo comunitario;
- emprendimiento y acceso a oportunidades;
- innovacion social con posible enfoque de genero.

### Que no buscar

- entidades sin actividad verificable en Canarias V1;
- empresas privadas puramente comerciales sin mision social clara;
- administraciones publicas ya cubiertas por el ICP institucional, salvo que aparezcan como fuente o financiador;
- asociaciones sin relacion con mujeres, inclusion, formacion, tecnologia, empleo, emprendimiento o acceso a oportunidades;
- emails inventados, deducidos por patron o no publicados;
- leads de Espana V2 mezclados con Canarias V1 sin presencia canaria verificable.

### Campos minimos

| Campo | Obligatorio | Nota |
|---|---|---|
| `organization_name` | Si | Nombre canonico. |
| `business_line` | Si | Siempre `SkilLand IA Mujeres`. |
| `campaign` | Si | Siempre `IA Mujeres 2026`. |
| `organization_type` | Si | asociacion, fundacion, ONG, red, federacion, colectivo, otro. |
| `territory` | Si | Canarias/isla/municipio si esta disponible. |
| `website` | Recomendado | Web oficial si existe. |
| `source_url` | Si | Fuente verificable. |
| `source_type` | Si | web_oficial, registro_publico, directorio, noticia_institucional, otra_fuente_verificable. |
| `source_confidence` | Si | high, medium, low. |
| `high_confidence` | Si | true solo si `source_confidence=high` y no hay flags graves. |
| `macro_icp` | Si | `asociaciones_ong_mujeres_inclusion_tech`. |
| `icp_segment` | Si | `ICP2 - Asociaciones/ONG - Mujeres e Inclusion Tech`. |
| `sub_icp` | Si | `mujeres_igualdad_steam` o `inclusion_tecnologica_impacto_social`. |
| `copy_variant` | Si | `mujeres_steam` o `inclusion_tech_genero`. |
| `priority` | Si | P0, P1, P2, Review. |
| `personalizacion_1` | Recomendado | Linea segura basada en fuente verificable; dejar vacio si obliga a inventar. |
| `contact_name` | Si existe | Solo si es publico y fiable. |
| `role_title` | Si existe | No inventar. |
| `email` | Si existe | No inventar ni deducir patrones. |
| `email_type` | Si | personal, area, generic, info, form, unknown. |
| `contact_url` | Si aplica | Formulario o pagina de contacto. |
| `needs_manual_review` | Si | true/false. |
| `duplicate_possible` | Si | true/false. |
| `quality_flags` | Recomendado | Flags breves separados por `;`. |

### Fuentes posibles

- webs oficiales de asociaciones, fundaciones y ONG;
- registros publicos de asociaciones/fundaciones;
- directorios institucionales verificables;
- federaciones o redes sectoriales;
- paginas de contacto oficiales;
- noticias institucionales o notas de prensa de la propia entidad;
- paginas de proyectos verificables.

Priorizar fuentes oficiales o trazables. Conservar siempre `source_url`.

### Criterios de calidad

- No inventar emails.
- No deducir emails por patron.
- No mezclar fuentes sin trazabilidad.
- No marcar P0 sin senal clara de mujeres, genero, STEAM, IA, empleabilidad femenina o formacion digital para mujeres.
- Marcar `needs_manual_review=true` ante fuente debil, contacto dudoso, duplicado o personalizacion insegura.
- Separar Canarias V1 de Espana V2.

## Para el repo CRM

### Mantener

| Campo | Valor |
|---|---|
| Business Line | `SkilLand IA Mujeres` |
| Campaign | `IA Mujeres 2026` |

No crear nueva Business Line, Campaign madre ni funnel separado.

### Crear o reutilizar campos

- `macro_icp`
- `sub_icp`
- `copy_variant`
- `priority`
- `source_confidence`
- `needs_manual_review`
- `duplicate_possible`

Tambien conservar campos ya usados cuando existan:

- `icp_segment`
- `department_area` si aplica;
- `source_type`
- `source_url`
- `generic_email`
- `high_confidence`
- `quality_flags`

### Operacion CRM

- Crear vistas separadas para ICP2, no workflows duplicados.
- Filtrar por `macro_icp`, `sub_icp`, `copy_variant`, `priority` y `needs_manual_review`.
- Asegurar que los drafts usan el `copy_variant` correcto.
- Ejecutar por tandas pequenas.
- Revisar drafts manualmente antes de envio.
- No mezclar metricas sin segmentacion: reportar total IA Mujeres y desglose ICP institucional vs ICP2.
- Mantener la misma secuencia y estados del funnel.

## No hacer

- No crear Business Line nueva.
- No crear Campaign nueva.
- No crear funnel nuevo.
- No duplicar workflows.
- No mezclar metricas sin segmentacion.
- No enviar sin revision humana.
- No tocar CRM desde Funnel Academy.
- No tocar GWS desde Funnel Academy.
- No crear CSVs falsos.
- No inventar contactos.

## Criterios de listo para scraping

ICP2 esta listo para scraping cuando existen:

- definicion clara de ICP2;
- subtipos `sub_icp`;
- criterios de inclusion y exclusion;
- campos requeridos;
- reglas de prioridad;
- `copy_variant` definidos;
- alcance Canarias V1;
- prohibicion explicita de inventar emails o datos.

Con este handoff, el siguiente repo puede crear su spec activa y producir el dataset limpio.

## Criterios de listo para CRM

El dataset ICP2 estara listo para CRM cuando:

- `organizations_clean.csv` y `contacts_clean.csv` existan en el repo de scraping;
- `sub_icp` y `copy_variant` esten presentes;
- `priority` sea filtrable;
- `needs_manual_review` este identificado;
- `source_url` exista;
- haya informe de calidad de datos;
- los posibles duplicados esten marcados;
- los registros Review no entren en envio;
- se pueda separar ICP institucional de ICP2 sin crear una campana nueva.
