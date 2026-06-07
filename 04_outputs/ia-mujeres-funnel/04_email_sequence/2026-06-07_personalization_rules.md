# Personalization Rules Final — IA Mujeres

## Principio

Usar personalizacion media por defecto. Usar personalizacion alta solo cuando haya buena informacion verificada.

No inventar datos. Si falta informacion, usar linea institucional generica de derivacion.

## Campos necesarios

- `[nombre]`
- `[entidad]`
- `[territorio]`
- `[area]`
- `[tipo_organizacion]`
- `[personalizacion_1]`

## Campo opcional recomendado en CRM

Si el equipo CRM lo ve facil, guardar una `personalizacion_1` en el deal/contacto antes de crear el draft.

No bloquear ejecucion por no tener este campo. Si no existe, generar una linea institucional segura desde los campos basicos disponibles.

## Nivel de personalizacion

| Nivel | Cuando usar | Ejemplo |
|---|---|---|
| Media | Default para casi todos los registros aptos. | Entidad + territorio + area/tipo de organizacion. |
| Alta | Solo si hay informacion fiable y relevante. | Mencion de contexto territorial o area concreta con alta confianza. |
| Baja / generica | Cuando falta persona o area clara. | Derivacion institucional sin asumir interlocutor. |

## Reglas de saludo

| Caso | Saludo recomendado |
|---|---|
| Contacto con nombre nominal fiable | `Estimado/a [nombre],` |
| Email generico de area | `Estimado equipo de [area],` |
| Email institucional general | `A la atencion del area responsable de igualdad, empleo o desarrollo local,` |
| Sin nombre pero area clara | `Estimado/a responsable de [area],` |
| Datos ambiguos | No enviar; pasar a revision manual. |

## Reglas por tipo de contacto

### Contacto con nombre nominal

Usar nombre si es fiable. No asumir cercania personal.

```text
Le escribo porque creo que esta conversacion puede ser especialmente relevante para [entidad]/[territorio], por el papel de [area] en igualdad, empleo y acceso a oportunidades reales para las mujeres.
```

### Email generico de area

Orientar el mensaje al equipo, no a una persona ficticia.

```text
Le escribo al equipo de [area] porque creo que esta conversacion puede ser especialmente relevante para [entidad], especialmente por su papel en igualdad, empleo, desarrollo local o politicas sociales en [territorio].
```

### Email institucional general

Pedir derivacion de forma respetuosa.

```text
Me gustaria hacer llegar esta reflexion al area responsable de igualdad, empleo o desarrollo local de [entidad], porque creo que puede tener sentido abrir una primera conversacion sobre IA, mujeres y futuro del trabajo en [territorio].
```

## Reglas por tipo de organizacion

### Cabildo

```text
Le escribo porque los cabildos tienen un papel clave para activar conversaciones insulares sobre igualdad, empleo y futuro del trabajo, especialmente cuando la IA empieza a cambiar las competencias y oportunidades del territorio.
```

### Ayuntamiento

```text
Le escribo porque los ayuntamientos tienen una posicion muy cercana a las mujeres del municipio y a las politicas locales de igualdad, empleo y desarrollo de oportunidades reales.
```

### Caso generico institucional

```text
Le escribo porque creo que esta reflexion podria ser relevante para el area de su entidad que trabaje igualdad, empleo, desarrollo local o politicas sociales.
```

## Reglas por area

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

### Generico institucional

```text
Creo que esta conversacion puede tener sentido para el area responsable de igualdad, empleo, desarrollo local o politicas sociales de [entidad].
```

## Plantilla de `[personalizacion_1]` por defecto

```text
Le escribo porque creo que esta conversacion puede ser especialmente relevante para [entidad]/[territorio], por el papel que tienen las administraciones locales e insulares en igualdad, empleo, desarrollo local y acceso a oportunidades reales para las mujeres.
```

## Prohibiciones

- No inventar nombre, cargo, area, territorio ni contexto.
- No fingir cercania.
- No mencionar datos que no esten en CRM o contexto validado.
- No usar aperturas como argumento de follow-up.
- No generar variantes profundas por segmento en este sprint.
- No crear campanas separadas para cabildos, ayuntamientos y registros actuales.
- No incluir asociaciones en este sprint.

## Segmentacion operativa

Mantener una plantilla unificada para:

- cabildos;
- ayuntamientos;
- registros institucionales actuales.

Aplicar solo lineas adaptativas por:

- Igualdad;
- Empleo / Desarrollo Local;
- Politicas Sociales;
- caso generico institucional.

Asociaciones quedan fuera de este sprint y pasan a segundo sprint.

## Revision manual

Pasar a revision si:

- falta entidad;
- falta territorio;
- el area es incompatible o desconocida;
- hay posible duplicado;
- el email no parece usable;
- la personalizacion exigiria inventar datos;
- el contacto nominal no es fiable.
