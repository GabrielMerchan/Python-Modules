# The Codex: el sistema de imports de Python, explicado con alquimia

Proyecto del **Python Module 06** del Common Core de [42 Madrid](https://www.42madrid.com/). Es un pequeño "laboratorio de alquimia" que sirve de excusa para entender a fondo cómo funcionan los imports en Python.

Todas las funciones son deliberadamente triviales: solo devuelven strings como `"Fire element created"`. La lógica no importa. Lo interesante es **cómo llega cada función a cada script** y por qué a veces no llega.

Si alguna vez te has preguntado para qué sirve el `__init__.py`, qué significa el punto en `from .elements import ...` o por qué Python te dice `partially initialized module (most likely due to a circular import)`, este repositorio intenta responderlo con ejemplos que puedes ejecutar.

---

## Qué vas a encontrar

| Parte | Tema | Scripts |
|---|---|---|
| I. The Alembic | Las distintas sintaxis de import y cómo un paquete decide qué expone | `ft_alembic_[0-5].py` |
| II. Distillation | Un módulo que usa código de otros módulos, dentro y fuera del paquete; alias | `ft_distillation_[0-1].py` |
| III. The Great Transmutation | Imports absolutos vs relativos | `ft_transmutation_[0-2].py` |
| IV. Avoid the Explosion | Dependencias circulares: por qué explotan y cómo evitarlo | `ft_kaboom_[0-1].py` |

---

## Índice

1. [Reglas del ejercicio](#reglas-del-ejercicio)
2. [Estructura del proyecto](#estructura-del-proyecto)
3. [Cómo ejecutarlo](#cómo-ejecutarlo)
4. [Antes de empezar: qué hace Python al importar](#antes-de-empezar-qué-hace-python-al-importar)
5. [Parte I: The Alembic](#parte-i-the-alembic)
6. [Parte II: Distillation](#parte-ii-distillation)
7. [Parte III: The Great Transmutation](#parte-iii-the-great-transmutation)
8. [Parte IV: Avoid the Explosion](#parte-iv-avoid-the-explosion)
9. [Calidad de código](#calidad-de-código)
10. [Resumen de conceptos](#resumen-de-conceptos)

---

## Reglas del ejercicio

El enunciado impone restricciones que condicionan cómo está escrito el código:

- Python 3.10 o superior.
- Solo se pueden importar módulos creados en el propio proyecto: nada de la librería estándar ni paquetes externos.
- **Prohibido modificar `sys.path`.** Todo tiene que funcionar con la resolución de imports por defecto.
- El código debe pasar `flake8` sin errores y `mypy` con anotaciones de tipo completas.
- La estructura de archivos está fijada por el enunciado.

---

## Estructura del proyecto

```
.
|-- alchemy/                      # Paquete principal
|   |-- __init__.py               # Interfaz pública del paquete
|   |-- elements.py               # create_earth(), create_air()
|   |-- potions.py                # healing_potion(), strength_potion()
|   |-- grimoire/                 # Subpaquete: dependencias circulares
|   |   |-- __init__.py           # Vacío a propósito
|   |   |-- light_spellbook.py    # Circularidad resuelta
|   |   |-- light_validator.py
|   |   |-- dark_spellbook.py     # Circularidad sin resolver (explota)
|   |   `-- dark_validator.py
|   `-- transmutation/            # Subpaquete: absolutos vs relativos
|       |-- __init__.py
|       `-- recipes.py            # lead_to_gold()
|-- elements.py                   # create_fire(), create_water()
|-- ft_alembic_[0-5].py
|-- ft_distillation_[0-1].py
|-- ft_transmutation_[0-2].py
`-- ft_kaboom_[0-1].py
```

Fíjate en que hay **dos archivos llamados `elements.py`**: uno en la raíz y otro dentro de `alchemy/`. No es un descuido. Obliga a pensar a cuál de los dos apunta cada import.

---

## Cómo ejecutarlo

```bash
git clone <url-de-este-repositorio>
cd <carpeta-del-repositorio>

python3 ft_alembic_0.py      # cada script se ejecuta por separado
```

No hay dependencias que instalar. Si quieres comprobar la calidad del código:

```bash
pip install flake8 mypy
flake8 .
mypy .
```

Dos scripts terminan con una excepción **a propósito**, porque su objetivo es demostrar un fallo:

| Script | Excepción | Qué demuestra |
|---|---|---|
| `ft_alembic_4.py` | `AttributeError` | Una función que existe, pero que el paquete no expone |
| `ft_kaboom_1.py` | `ImportError` | Una dependencia circular sin resolver |

---

## Antes de empezar: qué hace Python al importar

Casi todo lo que pasa en este proyecto se explica con estos tres pasos. Cuando Python encuentra `import algo`:

**1. Mira en `sys.modules`.** Es una caché, un diccionario `nombre -> módulo`. Si el módulo ya se importó antes, lo devuelve tal cual y **no vuelve a ejecutar su código**. Un módulo se ejecuta una sola vez, aunque lo importen diez archivos distintos.

**2. Si no está, lo busca en las carpetas de `sys.path`.** La primera de esas carpetas es **la carpeta del script que estás ejecutando**. Como todos los `ft_*.py` están en la raíz del proyecto, la raíz entra en `sys.path`, y por eso `import elements` e `import alchemy` funcionan sin configurar nada. Da igual desde qué directorio lances el script: lo que cuenta es dónde está el archivo.

**3. Crea el módulo, lo registra en `sys.modules` y ejecuta su código de arriba abajo.** El detalle importante es el orden: el módulo queda registrado **antes** de terminar de ejecutarse. Mientras se ejecuta está "parcialmente inicializado". Esto es lo que explica la Parte IV.

Dos conceptos más:

- Un **módulo** es un archivo `.py`. Un **paquete** es una carpeta con un archivo `__init__.py`. Al importar un paquete, o cualquier cosa que haya dentro, Python ejecuta primero su `__init__.py`.
- En los imports las rutas se escriben con puntos y sin extensión: `alchemy/transmutation/recipes.py` se importa como `alchemy.transmutation.recipes`.

---

## Parte I: The Alembic

> **Pregunta:** ¿qué formas hay de importar algo, y quién decide qué se puede importar de un paquete?

### Seis formas de llegar a una función

| Script | Import | Nombre que queda disponible | Llamada |
|---|---|---|---|
| `ft_alembic_0` | `import elements` | el módulo `elements` | `elements.create_fire()` |
| `ft_alembic_1` | `from elements import create_water` | solo la función | `create_water()` |
| `ft_alembic_2` | `import alchemy.elements` | el paquete `alchemy` | `alchemy.elements.create_earth()` |
| `ft_alembic_3` | `from alchemy.elements import create_air` | solo la función | `create_air()` |
| `ft_alembic_4` | `import alchemy` | el paquete `alchemy` | `alchemy.create_air()` |
| `ft_alembic_5` | `from alchemy import create_air` | solo la función | `create_air()` |

**`import X` frente a `from X import Y`:**

- `import X` te da el **módulo**, y accedes a su contenido con `X.algo`. Es más largo, pero siempre se ve de dónde viene cada cosa.
- `from X import Y` te da directamente el **objeto `Y`**. Es más cómodo, pero pierdes la referencia al origen y puedes chocar con nombres que ya tengas.

**Un detalle de `ft_alembic_2`:** `import alchemy.elements` no solo carga `elements.py`. Antes ejecuta `alchemy/__init__.py`, y el nombre que queda disponible en el script es `alchemy`. Por eso la llamada es `alchemy.elements.create_earth()` y no `elements.create_earth()`.

**`from alchemy import elements` no es lo mismo que `from alchemy.elements import create_air`.** El primero trae el *submódulo* entero; el segundo va al archivo y trae una *función* concreta.

### El `__init__.py` como interfaz pública

```python
# alchemy/__init__.py
from .elements import create_air
from .potions import strength_potion
from .potions import healing_potion as heal
from .transmutation.recipes import lead_to_gold

__all__ = ["create_air", "strength_potion", "heal", "lead_to_gold"]
```

Lo que se importa en el `__init__.py` es lo que ve quien escribe `import alchemy`. Aquí se expone `create_air`, pero **no** `create_earth`. Por eso `ft_alembic_4.py` termina así:

```
=== Alembic 4 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: Air element created
Now show that not all functions can be reached
This will raise an exception!
Testing the hidden create_earth: Traceback (most recent call last):
  ...
AttributeError: module 'alchemy' has no attribute 'create_earth'. Did you mean: 'create_air'?
```

`create_earth` existe en `alchemy/elements.py`, pero el paquete no la ofrece en su nivel superior. Sigue siendo accesible por la ruta completa, `alchemy.elements.create_earth()`, como hace `ft_alembic_2`. Así es como un paquete separa su **API pública** de sus **detalles internos**.

### Para qué sirve `__all__`

`__all__` es una lista con los nombres que el paquete declara como públicos. Tiene dos efectos:

1. **Define qué entra con `from alchemy import *`.** Solo los nombres de la lista.
2. **Deja claro que esos imports son intencionados.** Sin `__all__`, un linter como flake8 ve imports en el `__init__.py` que no se usan dentro del propio archivo y avisa con `F401 imported but unused`. `__all__` indica que están ahí para re-exportarse. mypy también lo tiene en cuenta.

### Un detalle de salida: `flush=True`

```python
print("Testing the hidden create_earth: ", end="", flush=True)
print(f"{alchemy.create_earth()}")
```

`print` escribe en `stdout`, que usa un buffer: un texto sin salto de línea puede quedarse retenido. El traceback de un error va por `stderr`, que no tiene buffer. Sin `flush=True`, el traceback podría aparecer en pantalla **antes** que el texto que se imprimió primero.

---

## Parte II: Distillation

> **Pregunta:** ¿cómo usa un módulo del paquete código que está en otros sitios?

### Dos `elements` en el mismo archivo

```python
# alchemy/potions.py
from .elements import create_air, create_earth    # alchemy/elements.py
from elements import create_fire, create_water    # elements.py de la raíz
```

Las dos líneas importan algo llamado `elements`, pero apuntan a archivos distintos:

- **`from .elements`** es un import **relativo**. El punto significa "el paquete en el que está este archivo", así que resuelve a `alchemy/elements.py`.
- **`from elements`** es un import **absoluto**. Python lo busca en `sys.path`, encuentra la raíz del proyecto y resuelve al `elements.py` de la raíz.

En Python 3, un `import elements` escrito dentro de `alchemy/` **no** mira primero en la carpeta de al lado. Si quieres el archivo vecino, tienes que pedirlo explícitamente con el punto.

### Alias a nivel de paquete

```python
# alchemy/__init__.py
from .potions import healing_potion as heal
```

`heal` no es una función nueva: es otro nombre para la misma función, creado en el `__init__.py`. Desde fuera se puede llamar `alchemy.heal()`, pero `potions.py` no sabe que ese alias existe. Sirve para ofrecer una API más cómoda sin tocar el módulo original.

| Script | Acceso |
|---|---|
| `ft_distillation_0` | Directo al archivo: `from alchemy.potions import strength_potion, healing_potion` |
| `ft_distillation_1` | A través del paquete: `import alchemy`, luego `alchemy.strength_potion()` y `alchemy.heal()` |

### Strings largos en varias líneas

```python
result = (f"Strength potion brewed with '{create_fire()}' "
          f"and '{create_water()}'")
```

Dos literales de string seguidos **dentro de la misma expresión** se concatenan solos. Los paréntesis son imprescindibles, porque mantienen la expresión abierta al saltar de línea. Hay dos errores habituales:

- **Sin paréntesis:** la primera línea ya es una sentencia completa. La segunda se evalúa por separado y su resultado se pierde, así que el string sale cortado sin ningún error.
- **Con `+` al inicio de la segunda línea y sin paréntesis:** Python lo interpreta como un "más unario" (como el `-` de `-5`) aplicado a un string, y lanza `TypeError: bad operand type for unary +: 'str'`.

---

## Parte III: The Great Transmutation

> **Pregunta:** ¿absolutos o relativos? ¿Y cómo se hace accesible una función desde distintos niveles?

### Los dos tipos de import en un mismo archivo

```python
# alchemy/transmutation/recipes.py
from ..potions import strength_potion      # relativo: alchemy/potions.py
from ..elements import create_air          # relativo: alchemy/elements.py
import elements                            # absoluto: elements.py de la raíz
```

- `.` es el paquete actual (`alchemy.transmutation`).
- `..` es el paquete padre (`alchemy`).

### Tres caminos a la misma función

| Script | Import | Quién hace visible `lead_to_gold` |
|---|---|---|
| `ft_transmutation_0` | `import alchemy.transmutation.recipes` | Nadie: se usa la ruta completa hasta el archivo |
| `ft_transmutation_1` | `import alchemy.transmutation` | `alchemy/transmutation/__init__.py` |
| `ft_transmutation_2` | `import alchemy` | `alchemy/__init__.py` |

Cada `__init__.py` "sube" la función un nivel. Es el mismo mecanismo de la Parte I aplicado a un subpaquete.

### ¿Cuándo usar cada uno?

| | Absolutos | Relativos |
|---|---|---|
| Ejemplo | `from alchemy.potions import ...` | `from ..potions import ...` |
| Legibilidad | Ruta completa, sin ambigüedad | Hay que saber dónde está el archivo |
| Si renombras el paquete | Hay que cambiar todos los imports | Siguen funcionando |
| Si mueves el paquete | Pueden romperse | Siguen funcionando si la estructura interna no cambia |
| Dónde funcionan | En cualquier sitio | Solo dentro de un paquete |
| PEP 8 | Opción recomendada por defecto | Aceptables para referencias internas en paquetes complejos |

Una regla práctica razonable: **absolutos para lo que viene de fuera del paquete, relativos para moverse dentro de él.** Es lo que hace `recipes.py`.

### Por qué un script no puede usar imports relativos

Cuando ejecutas `python3 ft_transmutation_0.py`, ese archivo no pertenece a ningún paquete: Python lo carga como `__main__`, sin paquete padre. Un import relativo necesita saber "relativo a qué paquete", así que falla:

```
ImportError: attempted relative import with no known parent package
```

---

## Parte IV: Avoid the Explosion

> **Pregunta:** ¿qué pasa cuando dos módulos se necesitan mutuamente?

### El diseño

Cada grimorio (light y dark) tiene dos archivos que dependen el uno del otro:

- El **spellbook** define los ingredientes permitidos y registra hechizos. Para decidir si un hechizo se acepta, necesita al validator.
- El **validator** comprueba los ingredientes. Para saber cuáles son válidos, necesita la lista del spellbook.

```
spellbook  ──(validate_ingredients)──▶  validator
    ▲                                       │
    └──────(allowed_ingredients)────────────┘
```

Los dos grimorios son idénticos salvo en los nombres y los ingredientes. La diferencia está en **cómo** se importan el uno al otro.

### Por qué explota el grimorio dark

```python
# dark_spellbook.py, línea 1
from .dark_validator import validate_ingredients

# dark_validator.py, línea 1
from .dark_spellbook import dark_spell_allowed_ingredients
```

Esto es lo que pasa paso a paso al ejecutar `ft_kaboom_1.py`:

1. Se importa `dark_spellbook`. Python lo registra en `sys.modules` y empieza a ejecutarlo.
2. Su línea 1 importa `dark_validator`. Python deja `dark_spellbook` a medias y empieza a ejecutar `dark_validator`.
3. La línea 1 de `dark_validator` pide `dark_spell_allowed_ingredients` a `dark_spellbook`.
4. `dark_spellbook` ya está en `sys.modules`, así que Python no lo carga otra vez. Pero solo se ha ejecutado su línea 1, y **esa función todavía no está definida**.
5. Resultado:

```
ImportError: cannot import name 'dark_spell_allowed_ingredients' from partially
initialized module 'alchemy.grimoire.dark_spellbook' (most likely due to a circular import)
```

El problema no es que dos módulos se importen mutuamente, sino que uno **pide un nombre concreto** (`from ... import nombre`) a otro que aún no ha llegado a definirlo.

### Cómo lo evita el grimorio light: import diferido

```python
# light_spellbook.py
def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients   # import dentro de la función
    ...
```

`light_spellbook.py` no importa nada al cargarse, así que se ejecuta de principio a fin y define todas sus funciones. El validator solo se importa **cuando alguien llama** a `light_spell_record`. Para entonces `light_spellbook` ya está completo en `sys.modules`, y cuando `light_validator` pide `light_spell_allowed_ingredients`, la función ya existe.

La dependencia mutua sigue ahí. Lo único que cambia es **el momento** en que se resuelve: de "al cargar el módulo" a "al llamar a la función".

Resultado:

```
=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell: Spell recorded: Fantasy (Earth, wind and fire - VALID)
```

### Otras formas de resolverlo

El import diferido no es la única opción:

| Técnica | En qué consiste | Pros y contras |
|---|---|---|
| **Import diferido** (la usada aquí) | Importar dentro de la función que lo necesita | Cambio pequeño y localizado. La dependencia queda escondida dentro de una función. |
| **Importar el módulo en vez del nombre** | `from . import light_spellbook` y usar `light_spellbook.light_spell_allowed_ingredients()` al llamar | Obtener un módulo parcialmente cargado sí está permitido; el nombre se busca más tarde. Es frágil si alguien lo cambia a `from ... import nombre`. |
| **Mover el import al final del archivo** | Definir primero las funciones e importar después | Funciona, pero va contra PEP 8 y flake8 lo marca (`E402`). |
| **Inyección de dependencias** | Pasar la lista de ingredientes como argumento al validator | Rompe la dependencia en un sentido. Cambia la firma de la función. |
| **Reestructurar** | Mover lo compartido a un tercer módulo del que dependan ambos | La solución más limpia en un proyecto real. Aquí no se usa porque el enunciado exige que los ingredientes estén en el spellbook y que los dos archivos se necesiten. |

En código real, una dependencia circular suele ser **una señal de que el diseño se puede mejorar**. Reestructurar es lo ideal; las otras técnicas son parches útiles cuando eso no es posible.

### Por qué el `__init__.py` de `grimoire` está vacío

Un `__init__.py` se ejecuta siempre que se importa algo de su paquete. Si el de `grimoire` importara algo del grimorio dark, **cualquier** import del paquete, incluido el del grimorio light, dispararía la explosión. Lo que pones en un `__init__.py` afecta a todos los que usan el paquete.

### Cómo se valida un hechizo

```python
def validate_ingredients(ingredients: str) -> str:
    val_ing = light_spell_allowed_ingredients()
    result = "INVALID"
    for i in val_ing:
        if i in ingredients.lower():
            result = "VALID"
    return f'{ingredients} - {result}'
```

Un hechizo es válido si contiene al menos un ingrediente permitido, sin distinguir mayúsculas. El spellbook usa ese resultado para registrar o rechazar:

```
Spell recorded: Fantasy (Earth, wind and fire - VALID)
Spell rejected: Test (bats and frogs - INVALID)
```

**Limitación:** la comprobación busca **subcadenas**, así que `"a chair"` se considera válido porque contiene `"air"`. Para comparar palabras completas habría que pasar a minúsculas, separar con `split()`, quitar la puntuación de cada palabra (para que `"earth,"` quede en `"earth"`) y comparar con igualdad exacta. A cambio, se dejarían de aceptar variantes como `"fires"`. Para el objetivo del ejercicio, la versión simple es suficiente.

---

## Calidad de código

- **Anotaciones de tipo en todas las funciones**, comprobadas con mypy.
- **flake8 sin errores.** Los `__init__.py` usan `__all__` para que los imports de re-exportación no se marquen como "no usados".
- **Compatibilidad con Python 3.10.** Los f-strings no anidan comillas del mismo tipo (`f"{f("x")}"`), porque eso solo es válido desde Python 3.12 (PEP 701).
- **El único error de mypy es intencionado**, en `ft_alembic_4.py`:

  ```
  error: Module has no attribute "create_earth"
  ```

  mypy detecta el problema **sin ejecutar nada**, leyendo el `__init__.py`. Python lo confirma **al ejecutar**, con el `AttributeError`. Es el mismo hecho visto en dos momentos distintos.

- **Un import fuera de la cabecera, sin romper flake8.** En `ft_kaboom_1.py` los mensajes deben imprimirse antes de la explosión, así que el import tiene que ir después de los `print`. Un import a mitad de archivo da `E402`, pero dentro de una función es legal, así que el código está en una función `main()`.

---

## Resumen de conceptos

**Paquete.** Una carpeta con `__init__.py`. Ese archivo se ejecuta al importar cualquier cosa del paquete y define lo que ve quien hace `import paquete`.

**`__all__`.** La lista de nombres públicos de un paquete. Controla `from paquete import *` y marca los imports del `__init__.py` como re-exportaciones intencionadas.

**API pública.** Que una función exista en un módulo no significa que el paquete la ofrezca. `alchemy.create_earth()` falla aunque `alchemy.elements.create_earth()` funcione.

**`sys.path`.** Python busca los módulos en esas carpetas, y la primera es la del script que se ejecuta. Por eso los imports del proyecto funcionan sin tocar nada.

**`sys.modules`.** La caché de módulos ya importados. Un módulo se ejecuta una sola vez; las siguientes importaciones lo reutilizan.

**Absolutos y relativos.** Los absolutos parten de `sys.path`; los relativos (`.`, `..`) parten del paquete actual y solo funcionan dentro de un paquete, nunca en un script ejecutado directamente.

**Dependencia circular.** Explota cuando un módulo pide un nombre concreto a otro que está parcialmente inicializado. Se evita retrasando el import, importando el módulo en vez del nombre, inyectando la dependencia o, idealmente, reestructurando el código.

---

## Autor

**Gabriel Merchán Romero**, estudiante del Common Core en 42 Madrid.
[GitHub](https://github.com/GabrielMerchan)
