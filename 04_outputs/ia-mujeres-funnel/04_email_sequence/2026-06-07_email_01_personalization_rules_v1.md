> Superseded: usar `2026-06-07_personalization_rules.md` como reglas finales para CRM/GWS.

# Email 01 Personalization Rules v1 — SkilLand IA Mujeres

## Objetivo

Definir microvariaciones seguras para Email 1 v2 sin crear campanas separadas por segmento. La personalizacion debe hacer que el mensaje parezca contextualizado, pero sin inventar datos ni fingir una relacion personal que no existe.

## Campos CRM necesarios

- `contact_name`
- `contact_role`
- `email`
- `email_type` o inferencia equivalente: personal, departamento, institucional general
- `organization_name`
- `organization_type`
- `territory`
- `department_area`
- `icp_segment`
- `generic_email`
- `high_confidence`
- `needs_manual_review`
- `duplicate_possible`
- `personalization_line`, si se valida manualmente

## Reglas de saludo

| condicion | saludo recomendado | nota |
|---|---|---|
| Persona nominal con tratamiento claro | `Estimada [nombre],` o `Estimado [nombre],` | Usar solo si el nombre es fiable. |
| Persona nominal sin genero/tratamiento claro | `Estimado/a [nombre],` | Evita asumir genero. |
| Email de departamento | `Estimado equipo de [area],` | Adecuado para igualdad, empleo, desarrollo local o politicas sociales. |
| Email institucional general | `A la atencion del area responsable de igualdad, empleo o desarrollo local,` | Busca derivacion sin fingir interlocutor. |
| Sin persona nominal pero area clara | `Estimado/a responsable de [area],` | Mantiene tono institucional. |
| Datos ambiguos | No enviar todavia | Pasar a Review. |

## Regla para persona nominal

Usar nombre solo si `contact_name` es fiable y no parece un alias de buzon.

Bloque recomendado:

```text
Le escribo porque creo que esta conversacion puede ser especialmente relevante para [entidad]/[territorio], por el papel de [area] en igualdad, empleo y acceso a oportunidades reales para las mujeres.
```

No usar formulas demasiado familiares. El email sigue siendo institucional.

## Regla para email generico de departamento

Si `generic_email=true` pero el area es clara, orientar el mensaje al equipo.

Bloque recomendado:

```text
Le escribo al equipo de [area] porque creo que esta conversacion puede ser especialmente relevante para [entidad], especialmente por su papel en [igualdad/empleo/desarrollo local] y en el acceso a oportunidades reales para las mujeres de [territorio].
```

## Regla para email institucional general

Si el email es institucional general y no hay area/persona clara, pedir derivacion.

Bloque recomendado:

```text
Me gustaria hacer llegar esta reflexion al area responsable de igualdad, empleo o desarrollo local de [entidad], porque creo que puede tener sentido abrir una primera conversacion sobre IA, mujeres y futuro del trabajo en [territorio].
```

CTA secundario opcional:

```text
Si no es la persona adecuada, agradeceria que pudiera derivarlo al area correspondiente.
```

## Bloques opcionales por tipo de organizacion

### Cabildo

```text
Le escribo porque los cabildos tienen un papel clave para activar conversaciones insulares sobre igualdad, empleo y futuro del trabajo, especialmente cuando la IA empieza a cambiar las competencias que necesitaran muchas mujeres del territorio.
```

### Ayuntamiento

```text
Le escribo porque los ayuntamientos tienen una posicion muy cercana a las mujeres del municipio y a las politicas locales de igualdad, empleo y desarrollo de oportunidades reales.
```

### Entidad publica mixta o ambigua

```text
Le escribo porque creo que esta reflexion podria ser relevante para el area de su entidad que trabaje igualdad, empleo, desarrollo local o politicas sociales.
```

## Bloques opcionales por area

### Igualdad

```text
Desde el area de igualdad, esta conversacion puede ayudar a anticipar como la IA afectara a la autonomia economica, el acceso a nuevos roles y la reduccion de brechas para mujeres del territorio.
```

### Empleo / Desarrollo Local

```text
Desde empleo y desarrollo local, el foco estaria en como la IA puede abrir nuevas oportunidades profesionales para mujeres y conectar formacion con necesidades reales del mercado.
```

### Politicas Sociales

```text
Desde politicas sociales, el enfoque puede centrarse en inclusion, autonomia digital y acceso a oportunidades tecnologicas para colectivos con mayores barreras de entrada.
```

### Area desconocida

No adaptar en exceso. Usar derivacion institucional y marcar revision si la entidad no encaja claramente.

## Ejemplos de personalizacion ligera

### 1. Cabildo con area de Igualdad

```text
Le escribo porque creo que esta conversacion puede ser especialmente relevante para el Cabildo de [isla], por el papel insular que tiene el area de Igualdad en anticipar nuevas brechas y abrir oportunidades reales para las mujeres del territorio.
```

### 2. Cabildo con area de Empleo

```text
Le escribo porque desde [entidad] trabajan en un punto clave de esta conversacion: empleo, transicion laboral y acceso de las mujeres a los nuevos roles que esta creando la tecnologia.
```

### 3. Ayuntamiento con area de Igualdad

```text
Le escribo porque creo que esta conversacion puede tener sentido para [municipio], especialmente por el papel de las politicas locales de igualdad en preparar a las mujeres del territorio ante los cambios que trae la IA.
```

### 4. Ayuntamiento con Desarrollo Local

```text
Le escribo porque desde desarrollo local se puede abrir una conversacion muy concreta sobre IA, nuevas oportunidades profesionales y autonomia economica para mujeres de [municipio].
```

### 5. Email institucional general sin persona nominal

```text
Me gustaria hacer llegar esta reflexion al area responsable de igualdad, empleo o desarrollo local de [entidad], porque creo que puede tener sentido abrir una primera conversacion sobre IA, mujeres y futuro del trabajo en [territorio].
```

## Reglas de seguridad de copy

- No inventar nombre, cargo, area ni territorio.
- No asumir que el destinatario conoce a Romina.
- No usar tono de venta ni urgencia artificial.
- No decir que existe un acuerdo, observatorio, partner o informe publico si no esta documentado.
- No adjuntar el dossier largo en primer contacto.
- No pedir compra, presupuesto ni contratacion en Email 1.
- No depender de tracking de apertura para avanzar estados.

## Criterio para pasar a Review

Enviar a revision manual si:

- falta entidad;
- falta territorio;
- el area no encaja con igualdad, empleo, politicas sociales o desarrollo local;
- el email parece duplicado;
- el email parece personal pero el nombre no es fiable;
- el buzon es demasiado generico y no se sabe a que area derivar;
- cualquier campo necesario exige inventar contexto.
