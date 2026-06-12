# Prompt for Scraping Repo - ICP2 Asociaciones / ONG

- Fecha: 2026-06-12
- Repo destino: `RaulAM7/agentic-scrapping-Experiment-scrappling`
- Uso: prompt operativo para ejecutar despues en el repo de scraping
- No ejecutar scraping desde Funnel Academy

## Prompt

```text
Estamos trabajando sobre la linea SkilLand IA Mujeres.

Objetivo:
Crear el dataset Canarias V1 para el nuevo ICP2 aprobado estrategicamente:

ICP2: Asociaciones / ONG - Mujeres e Inclusion Tech

Definicion:
Entidades sociales, asociaciones, fundaciones y ONG en Canarias que trabajan con mujeres, igualdad, talento femenino, STEAM, inclusion digital, empleabilidad, emprendimiento, vulnerabilidad, juventud, migracion, formacion tecnologica, desarrollo comunitario o acceso a oportunidades, y que pueden actuar como compradoras, prescriptoras, partners comunitarias, canales de captacion o co-disenadoras de programas de empoderamiento femenino en IA.

Regla estrategica:
ICP2 NO es un funnel separado. Es una ampliacion social/comunitaria del mismo funnel IA Mujeres.

Mantener:
- business_line = SkilLand IA Mujeres
- campaign = IA Mujeres 2026
- mismo buyer journey
- mismos estados del funnel
- misma secuencia
- misma logica de seguimiento
- mismas metricas principales
- mismo handoff CRM/GWS
- revision humana obligatoria
- cadencia prudente por tandas

Diferenciar solo:
- macro_icp
- sub_icp
- copy_variant
- priority/scoring
- source_confidence
- personalizacion segura

Alcance:
- Trabajar solo Canarias V1.
- No mezclar Espana V2 salvo que una entidad nacional tenga sede, delegacion o actividad canaria verificable.
- Espana V2 queda como escalado futuro.

Antes de producir datos:
1. Crear una spec activa en el repo de scraping.
2. Crear contexto operativo del ICP2.
3. Registrar criterios de inclusion/exclusion.
4. Definir fuentes permitidas y criterios de calidad.

Subtipos:
1. sub_icp = mujeres_igualdad_steam
   Para asociaciones de mujeres, mujeres STEAM, mujeres empresarias, redes de liderazgo femenino, asociaciones de igualdad, asociaciones feministas con linea de empleo/emprendimiento/formacion, entidades de mujeres profesionales o comunidades de talento femenino.
   copy_variant = mujeres_steam
   Prioridad: P0 o P1 segun calidad de contacto.

2. sub_icp = inclusion_tecnologica_impacto_social
   Para ONG, fundaciones y asociaciones que no son exclusivamente de mujeres, pero trabajan inclusion tecnologica, impacto social, empleabilidad, formacion laboral, juventud, vulnerabilidad, migracion, emprendimiento, desarrollo comunitario, innovacion social, equidad de genero o acceso a oportunidades.
   copy_variant = inclusion_tech_genero
   Prioridad: P1 alto. P0 solo si se verifica programa concreto con mujeres, genero, empleabilidad femenina, formacion digital para mujeres, emprendimiento femenino o brecha digital de genero.

Que buscar:
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

Que no buscar:
- administraciones publicas ya cubiertas por el ICP institucional, salvo que sean fuente o financiador;
- entidades fuera de Canarias V1;
- empresas puramente comerciales sin mision social clara;
- asociaciones sin relacion verificable con mujeres, inclusion, formacion, tecnologia, empleo, emprendimiento o acceso a oportunidades;
- emails inventados o deducidos por patron;
- leads sin source_url.

Fuentes:
- priorizar fuentes oficiales o verificables;
- webs oficiales;
- registros publicos;
- directorios institucionales;
- federaciones o redes sectoriales;
- paginas de contacto oficiales;
- noticias institucionales o de la propia entidad;
- paginas de proyectos verificables.

Conservar siempre source_url.

Campos requeridos en organizations_clean.csv:
- organization_name
- business_line
- campaign
- organization_type
- territory
- island
- municipality
- website
- email_main
- phone_main
- source_url
- source_type
- source_confidence
- high_confidence
- macro_icp
- icp_segment
- sub_icp
- copy_variant
- priority
- personalizacion_1
- needs_manual_review
- duplicate_possible
- quality_flags
- notes

Campos requeridos en contacts_clean.csv:
- organization_name
- business_line
- campaign
- contact_name
- role_title
- department_area
- email
- email_type
- phone
- territory
- island
- municipality
- contact_url
- source_url
- source_type
- source_confidence
- high_confidence
- macro_icp
- icp_segment
- sub_icp
- copy_variant
- priority
- personalizacion_1
- generic_email
- needs_manual_review
- duplicate_possible
- quality_flags
- notes

Valores fijos:
- business_line = SkilLand IA Mujeres
- campaign = IA Mujeres 2026
- macro_icp = asociaciones_ong_mujeres_inclusion_tech
- icp_segment = ICP2 - Asociaciones/ONG - Mujeres e Inclusion Tech

Valores permitidos:
- sub_icp: mujeres_igualdad_steam, inclusion_tecnologica_impacto_social
- copy_variant: mujeres_steam, inclusion_tech_genero
- priority: P0, P1, P2, Review
- source_confidence: high, medium, low
- email_type: personal, area, generic, info, form, unknown

Reglas de prioridad:
- P0: encaje claro, fuente verificable, contacto usable y senal explicita de mujeres/igualdad/STEAM/IA/empleabilidad femenina/formacion digital para mujeres.
- P1: buen encaje con inclusion, tecnologia, empleabilidad, formacion o impacto social; contacto usable; personalizacion segura.
- P2: encaje posible pero amplio, indirecto o con baja senal de genero/IA; conservar para revision posterior.
- Review: datos ambiguos, fuente debil, contacto dudoso, duplicado probable, territorio no claro o personalizacion insegura.

Reglas de calidad:
- No inventar emails.
- No deducir emails por patron.
- No inventar nombres, cargos, programas, resultados, alianzas ni claims.
- No afirmar foco de mujeres si la fuente solo demuestra inclusion general.
- high_confidence = true solo cuando source_confidence = high y no existan flags graves.
- personalizacion_1 debe ser una linea segura basada en fuente verificable; si no se puede generar sin inventar, dejar vacio y registrar la nota correspondiente.
- Marcar needs_manual_review=true cuando haya duda de fuente, contacto, duplicado, territorio, sub_icp o copy_variant.
- Marcar duplicate_possible=true cuando haya coincidencias relevantes por nombre, web, email o telefono.
- Conservar source_url por cada registro.

Entregables esperados:
1. Directorio documental del trabajo realizado.
2. Data quality report.
3. organizations_clean.csv.
4. contacts_clean.csv.
5. Notas de fuentes y gaps.
6. Resumen listo para handoff CRM.

No enviar emails.
No tocar CRM.
No tocar GWS.
No crear workflows.
No crear contactos reales fuera de los CSVs del repo de scraping.
No ejecutar nada desde Funnel Academy.
```

## Nota de uso

Este prompt debe ejecutarse en el repo de scraping. Funnel Academy solo deja preparado el handoff estrategico y operativo.
