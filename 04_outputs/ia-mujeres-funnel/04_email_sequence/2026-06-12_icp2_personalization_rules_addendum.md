# ICP2 Personalization Rules Addendum

- Fecha: 2026-06-12
- Base: `2026-06-07_personalization_rules.md`
- Estado: addendum para nuevo sprint aprobado

## Principio

Las reglas anteriores excluian asociaciones en el sprint previo porque no habia dataset tabular suficiente y la tanda estaba centrada en cabildos, ayuntamientos y registros publicos.

Este addendum no borra ni contradice ese historico. Habilita ICP2 como nuevo sprint aprobado: `Asociaciones / ONG - Mujeres e Inclusion Tech`.

La personalizacion debe ser media por defecto, segura y verificable. No inventar datos, cargos, programas, resultados, alianzas ni foco de genero.

## Reglas de saludo

| Caso | Saludo recomendado | Revision |
|---|---|---|
| Contacto nominal fiable, nombre femenino reconocido | `Estimada {nombre},` | Apto si fuente y email son fiables. |
| Contacto nominal fiable, nombre masculino reconocido | `Estimado {nombre},` | Apto si fuente y email son fiables. |
| Contacto nominal fiable, genero no reconocido | `Estimado {nombre},` | Revisar si el nombre parece dudoso. |
| Equipo de asociacion o fundacion sin persona nominal | `Estimado equipo,` | Apto si entidad y email son claros. |
| Email generico de asociacion | `Estimado equipo,` | Incluir derivacion si procede. |
| Email `info@` | `Estimado equipo,` | Usar copy de derivacion y marcar posible baja precision. |
| Formulario/contacto general | No crear email directo. | Pasar a proceso que corresponda al repo de scraping/CRM. |
| Fundacion/ONG con area concreta | `Estimado equipo de [area],` solo si el area es literal y fiable. | Si el area no es clara, usar `Estimado equipo,`. |
| Entidad sin persona nominal | `Estimado equipo,` | Apto solo con entidad, territorio y canal fiables. |

No usar `Estimado/a`. No usar nombre completo en el saludo salvo que el sistema CRM no pueda separar nombre de pila y se revise manualmente.

## Reglas de `personalizacion_1`

`personalizacion_1` debe cumplir:

- estar basada en fuente verificable;
- no afirmar mas de lo que la fuente dice;
- conectar entidad + mision + posible linea IA Mujeres;
- evitar halagos exagerados;
- evitar lenguaje paternalista;
- diferenciar si la entidad es de mujeres o es una ONG generalista.

Plantilla segura para `mujeres_igualdad_steam`:

```text
Le escribo porque el trabajo de [entidad] con mujeres, igualdad, talento femenino o STEAM puede ser un punto de partida valioso para acercar la IA de forma practica, util y medible a mujeres de [territorio].
```

Plantilla segura para `inclusion_tecnologica_impacto_social`:

```text
Le escribo porque el trabajo de [entidad] en inclusion, formacion, empleabilidad o acceso a oportunidades puede conectar bien con una posible linea sobre mujeres, IA y futuro del trabajo en [territorio].
```

Plantilla generica cuando hay encaje pero poca precision:

```text
Le escribo porque creemos que algunas entidades sociales canarias pueden tener un papel importante para acercar la IA de forma util, comprensible y medible a mujeres que hoy pueden estar mas lejos de esas oportunidades.
```

## Reglas por `sub_icp`

| `sub_icp` | Usar cuando | Evitar |
|---|---|---|
| `mujeres_igualdad_steam` | La fuente muestra mujeres, igualdad, STEAM, liderazgo femenino, empresarias, profesionales, emprendimiento femenino o formacion para mujeres. | No usar si la entidad solo trabaja inclusion general sin foco verificable en mujeres. |
| `inclusion_tecnologica_impacto_social` | La fuente muestra inclusion, tecnologia, empleabilidad, juventud, migracion, vulnerabilidad, formacion, emprendimiento o acceso a oportunidades. | No afirmar foco de mujeres si no esta verificado; plantearlo como linea a explorar. |

## Reglas por `copy_variant`

| `copy_variant` | Enfoque |
|---|---|
| `mujeres_steam` | Comunidad, confianza, legitimidad, talento femenino, igualdad, STEAM, tecnologia como oportunidad real. |
| `inclusion_tech_genero` | Barreras de acceso, formacion, tecnologia, empleabilidad, inclusion, posible linea especifica de mujeres e IA. |

El draft debe usar el `copy_variant` asociado al `sub_icp`. Si hay conflicto entre ambos campos, marcar `needs_manual_review=true`.

## Reglas por prioridad

| Prioridad | Personalizacion permitida |
|---|---|
| P0 | Puede usar personalizacion media-alta si hay fuente clara. Revisar humano antes de enviar. |
| P1 | Usar personalizacion media con datos seguros. Evitar afirmaciones especificas no necesarias. |
| P2 | Usar personalizacion generica y valorar si conviene esperar a una tanda posterior. |
| Review | No enviar. Limpiar datos, fuente, duplicado, contacto o encaje. |

## Ejemplos seguros

```text
Le escribo porque [entidad] trabaja en torno a mujeres, igualdad o talento femenino, y creemos que puede tener sentido explorar como acercar la IA de forma practica y medible a esa comunidad.
```

```text
Dentro de la labor de [entidad] en inclusion y acceso a oportunidades, creemos que podria tener sentido valorar una linea especifica sobre mujeres, IA y futuro del trabajo.
```

```text
Si esta conversacion corresponde a otra persona del equipo, le agradeceria que pudiera reenviarselo o indicarme con quien hablar.
```

## Ejemplos prohibidos

- `Sabemos que teneis un programa de IA para mujeres` si no esta verificado.
- `Vuestra asociacion lidera la inclusion digital en Canarias` si no hay fuente validada.
- `Podemos garantizar empleabilidad` o cualquier promesa de resultado.
- `Os traemos mujeres para formar` o formulaciones que traten a la comunidad como canal pasivo.
- `Como administracion publica...` dirigido a una asociacion u ONG.
- `Como asociacion de mujeres...` dirigido a una ONG generalista sin foco verificado.

## Cuando pasar a `needs_manual_review=true`

Marcar revision manual si:

- `sub_icp` no esta claro;
- `copy_variant` no coincide con el `sub_icp`;
- la fuente no confirma actividad en Canarias;
- solo hay un agregador sin fuente primaria;
- el email parece deducido, incompleto o no verificable;
- hay formulario pero no email;
- hay posible duplicado;
- el contacto nominal no es fiable;
- la entidad tiene encaje amplio pero no hay senal de genero/inclusion/tecnologia/formacion suficiente;
- la personalizacion exigiria inventar datos.

## Cuando no enviar

No enviar si:

- `needs_manual_review=true`;
- no existe canal usable;
- no hay `source_url`;
- el territorio Canarias V1 no esta verificado;
- el encaje tematico es demasiado debil;
- la entidad o contacto son ambiguos;
- hay riesgo de tratar como asociacion de mujeres a una ONG generalista;
- hay riesgo de tratar como administracion publica a una entidad social.
