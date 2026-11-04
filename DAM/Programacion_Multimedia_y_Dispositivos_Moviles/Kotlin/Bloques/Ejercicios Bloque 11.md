---
asignatura: PMDM
tema: 8
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/ejercicios
---

# Bloque 11 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[08 - POO III]] · [[06 - POO I]]
> Bloque anterior: [[Ejercicios Bloque 10]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque11/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 8.3, 8.5 y 8.6 de [[08.1 - Ejercicios 8 POO III|el boletín 8]]. El código parte de esas soluciones, con más casos de prueba.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque11/Ejercicio11.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas y los mensajes de error son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Constantes en el `companion object` de `PhysicsConstants`]]
- [[#Ejercicio 2 · *Extension function* `reverseWords`]]
- [[#Ejercicio 3 · *Extension property* `vowelCount`]]

---

## Ejercicio 1 · Constantes en el `companion object` de `PhysicsConstants`

> [!question] Enunciado
> Define una clase `PhysicsConstants` cuyo *companion object* contenga constantes físicas importantes:
>
> - La velocidad de la luz en el vacío (`c`) en metros por segundo (valor: `299_792_458`).
> - La constante de Planck (`h`) en julios por segundo (valor: `6.62607015e-34`).
> - La constante de gravitación universal (`G`) en metros cúbicos por kilogramo por segundo al cuadrado (valor: `6.67430e-11`).
>
> Luego, define una función `main` que imprima estos valores constantes.

### Clases y métodos introducidos
- `const val`: una **constante conocida en tiempo de compilación**. Su valor tiene que ser un literal de tipo primitivo (`Int`, `Double`…) o `String`, y el compilador lo copia directamente allí donde se usa. Equivale a `public static final` en Java.
- `companion object`: sus miembros se usan con el nombre de la clase (`PhysicsConstants.SPEED_OF_LIGHT`), sin crear ningún objeto. La clase hace de **espacio de nombres**.
- **UPPER_SNAKE_CASE**: la convención para nombrar constantes, en mayúsculas y con `_` entre palabras.
- Literales: `299_792_458` (el `_` solo ayuda a leer) y notación científica `6.62607015e-34` (= 6,62607015 × 10⁻³⁴).

> **Términos explicados:** [[08 - POO III#3. Constantes conocidas en tiempo de compilación|`const val` y UPPER_SNAKE_CASE]] · [[06 - POO I#17. Objetos compañeros|`companion object`]] · [[02 - Jerarquia de tipos#2. Tipos numéricos|literales numéricos]]

#### Ejemplo simple de funcionamiento
```kotlin
class Circle {
    companion object {
        const val PI = 3.14159
    }
}

fun main() {
    println(Circle.PI * 2 * 2)   // área de un círculo de radio 2
}
```

### Código fuente (`Ejercicio11.1/src/Main.kt`)

```kotlin
class PhysicsConstants {
    companion object {
        // Velocidad de la luz en el vacío (c), en m/s
        const val SPEED_OF_LIGHT = 299_792_458
        // Constante de Planck (h), en J·s
        const val PLANCK_CONSTANT = 6.62607015e-34
        // Constante de gravitación universal (G), en m³/(kg·s²)
        const val GRAVITATIONAL_CONSTANT = 6.67430e-11
    }
}

fun main() {
    println("c = ${PhysicsConstants.SPEED_OF_LIGHT} m/s")
    println("h = ${PhysicsConstants.PLANCK_CONSTANT} J·s")
    println("G = ${PhysicsConstants.GRAVITATIONAL_CONSTANT} m³/(kg·s²)")
}
```

### Explicación paso a paso
1. **Dónde van:** las tres constantes están dentro del `companion object`, así que pertenecen a la **clase** y no a cada objeto. Se usan como `PhysicsConstants.SPEED_OF_LIGHT`.
2. **Nombres:** en UPPER_SNAKE_CASE y descriptivos (`SPEED_OF_LIGHT` mejor que `C`). Un comentario indica a qué símbolo físico corresponde cada una.
3. **Tipos:** no se escriben; se deducen del literal. `299_792_458` es un `Int` y los otros dos, `Double`.
4. **`const`:** se puede usar porque los tres valores son literales de tipo primitivo, conocidos antes de ejecutar el programa.
5. **Salida:** se imprimen con plantillas de cadena y su unidad.

> [!tip] Prueba
> ```text
> c = 299792458 m/s
> h = 6.62607015E-34 J·s
> G = 6.6743E-11 m³/(kg·s²)
> ```
> Al imprimir, Kotlin muestra los `Double` muy pequeños en notación científica con `E` mayúscula y quita el cero final de `6.67430`. Para un `Double`, `6.67430` y `6.6743` son el mismo número.

> [!note]- 🧠 Por qué funciona
> - `const val` es como un dato impreso en el libro de física: está fijado antes de abrirlo y nunca cambia. El compilador sustituye cada `PhysicsConstants.SPEED_OF_LIGHT` por `299792458` directamente.
> - `const` solo se permite en el nivel superior del archivo, en un `object` o en un `companion object`. Si lo pones como propiedad normal de la clase, **no compila**. Error real de `kotlinc`: `const 'val' is only allowed on top level, in named objects, in companion objects or companion blocks`.
> - Diferencia con un `val` normal: un `val` puede recibir un valor calculado al ejecutar (`val now = System.currentTimeMillis()`); un `const val`, no.

> [!warning] Una errata del enunciado
> El enunciado dice que la constante de Planck está en «julios **por** segundo», pero su unidad es el **julio·segundo** (J·s, julios *multiplicados* por segundos). «Julios por segundo» (J/s) son vatios, una unidad de potencia. En el código se ha puesto la unidad correcta, `J·s`.

---

## Ejercicio 2 · *Extension function* `reverseWords`

> [!question] Enunciado
> Define una *extension function* para la clase `String` llamada `reverseWords` que permita invertir el orden de las palabras en la cadena. Una palabra se define como una secuencia de caracteres alfanuméricos separados por espacios (ver el método `split()`).
>
> Realiza una función `main` en la que se demuestre el uso de `reverseWords()`.

### Clases y métodos introducidos
- ***Extension function*** `fun String.reverseWords()`: **añade** un método a una clase que no es tuya (`String`) sin modificarla ni heredar de ella. Se llama con punto, como cualquier método: `"hola mundo".reverseWords()`.
- Dentro de la función, `this` es la cadena sobre la que se llama (el **receptor**), y se puede omitir: `trim()` equivale a `this.trim()`.
- `split(Regex("\\s+"))`: parte la cadena por **uno o más** espacios seguidos y devuelve una `List<String>`.
- `reversed()`: devuelve la lista al revés.
- `joinToString(" ")`: une los elementos de una lista en un `String`, con `" "` entre cada uno.

> **Términos explicados:** [[08 - POO III#5. Extension functions|*extension functions*]] · [[11 - Colecciones#6. Métodos y propiedades de listas|métodos de listas]] · [[02 - Jerarquia de tipos#6. Strings|`String`]]

#### Ejemplo simple de funcionamiento
```kotlin
// Añadimos a Int un método que no tiene
fun Int.isEven(): Boolean = this % 2 == 0

fun main() {
    println(4.isEven())   // true
    println(7.isEven())   // false
}
```

### Código fuente (`Ejercicio11.2/src/Main.kt`)

```kotlin
// Extension function: se define fuera de String, pero se llama como si fuera un método suyo
fun String.reverseWords(): String =
    trim()                      // quita espacios al principio y al final
        .split(Regex("\\s+"))   // separa por uno o más espacios
        .reversed()             // invierte el orden de la lista de palabras
        .joinToString(" ")      // vuelve a unirlas con un espacio

fun main() {
    val sentence = "Kotlin es un lenguaje   moderno"
    println("Original:  $sentence")
    println("Invertida: ${sentence.reverseWords()}")

    // Más casos: espacios en los extremos, una sola palabra y cadena vacía
    println("[${"  hola mundo  ".reverseWords()}]")
    println("[${"Kotlin".reverseWords()}]")
    println("[${"".reverseWords()}]")
}
```

### Explicación paso a paso
1. **Declaración:** `fun String.reverseWords(): String` indica que la función «pertenece» a `String` y devuelve otro `String`. Es una función de expresión única (`=`), encadenando cuatro pasos.
2. **`trim()`:** quita los espacios del principio y del final. Sin esto, `"  hola"` daría una «palabra» vacía al partirla.
3. **`split(Regex("\\s+"))`:** separa por cualquier grupo de espacios. `"lenguaje   moderno"` (tres espacios) da `["lenguaje", "moderno"]` y no `["lenguaje", "", "", "moderno"]`, que es lo que pasaría con `split(" ")`.
4. **`reversed()`:** `["Kotlin", "es", "un", "lenguaje", "moderno"]` pasa a `["moderno", "lenguaje", "un", "es", "Kotlin"]`.
5. **`joinToString(" ")`:** vuelve a formar la frase, con un único espacio entre palabras.
6. **Pruebas:** la frase del ejemplo (con espacios de sobra), una con espacios en los extremos, una sola palabra y la cadena vacía. Los corchetes `[ ]` dejan ver si sobra algún espacio.

> [!tip] Prueba
> ```text
> Original:  Kotlin es un lenguaje   moderno
> Invertida: moderno lenguaje un es Kotlin
> [mundo hola]
> [Kotlin]
> []
> ```

> [!note]- 🧠 Por qué funciona
> - Una *extension function* es como ponerle una funda con un botón nuevo al móvil: el móvil (la clase `String`) no cambia por dentro, pero ahora tiene un botón más que puedes pulsar.
> - Por dentro, el compilador la convierte en una función normal que recibe la cadena como primer parámetro: `reverseWords(sentence)`. Por eso **no puede acceder** a lo privado de `String`: solo usa lo que es público.
> - `Regex("\\s+")` es una **expresión regular**: `\s` significa «un espacio en blanco» y `+` «uno o más». En el código se escribe `\\s` porque `\` hay que escaparlo dentro de un `String` ([[Programación basica/Tema 9/Expresiones regulares|ver expresiones regulares en Java]]).

---

## Ejercicio 3 · *Extension property* `vowelCount`

> [!question] Enunciado
> Define una *extension property* para la clase `String` llamada `vowelCount` que permita obtener el número de vocales de la cadena.

### Clases y métodos introducidos
- ***Extension property*** `val String.vowelCount: Int`: añade una **propiedad** a `String`. Se usa sin paréntesis: `"hola".vowelCount`.
- **Sin campo de respaldo**: como no es un miembro real de la clase, no tiene dónde guardar un valor. El valor se **calcula** cada vez en un `get()`.
- `lowercase()`: pasa la cadena a minúsculas para no tener que comparar con `A`, `E`… por separado.
- `c in "aeiou…"`: `in` sobre un `String` comprueba si el carácter está en esa cadena (llama a `contains`).

> **Términos explicados:** [[08 - POO III#6. Extension properties|*extension properties*]] · [[06 - POO I#7. Propiedades calculadas|propiedades calculadas]] · [[06 - POO I#8. Campo de respaldo|campo de respaldo]]

#### Ejemplo simple de funcionamiento
```kotlin
// Propiedad nueva para String: la última letra
val String.lastChar: Char
    get() = this[length - 1]

fun main() {
    println("Kotlin".lastChar)   // n
}
```

### Código fuente (`Ejercicio11.3/src/Main.kt`)

```kotlin
// Extension property: no tiene backing field, así que se calcula en el getter
val String.vowelCount: Int
    get() {
        var count = 0
        for (c in this.lowercase()) {
            // "in" sobre un String se traduce a contains(c)
            if (c in "aeiouáéíóúü") {
                count++
            }
        }
        return count
    }

fun main() {
    val text = "Programación Multimedia"
    println("\"$text\" tiene ${text.vowelCount} vocales")

    // Más casos: mayúsculas, ü, sin vocales y cadena vacía
    println("\"AEIOU\" → ${"AEIOU".vowelCount}")
    println("\"Pingüino\" → ${"Pingüino".vowelCount}")
    println("\"Brrr\" → ${"Brrr".vowelCount}")
    println("\"\" → ${"".vowelCount}")
}
```

### Explicación paso a paso
1. **Declaración:** `val String.vowelCount: Int` crea una propiedad de solo lectura para cualquier `String`. No lleva `= valor`, sino un `get()`.
2. **El getter:** cada vez que se lee `text.vowelCount`, se ejecuta el bloque `get()`. Recorre la cadena en minúsculas carácter a carácter.
3. **Las vocales:** cada carácter se busca en `"aeiouáéíóúü"`. Se incluyen las acentuadas y la `ü` porque los textos son en español: `"Programación"` tiene una `ó`.
4. **Resultado:** se cuenta cada vocal encontrada y se devuelve el total.
5. **Pruebas:** un texto con tildes, mayúsculas (`"AEIOU"`), la `ü` de `"Pingüino"`, una palabra sin vocales y la cadena vacía.

> [!tip] Prueba
> ```text
> "Programación Multimedia" tiene 10 vocales
> "AEIOU" → 5
> "Pingüino" → 4
> "Brrr" → 0
> "" → 0
> ```
> Si escribes `val String.vowelCount: Int = 0`, **no compila**. Error real de `kotlinc`: `extension property cannot be initialized because it has no backing field`.

> [!note]- 🧠 Por qué funciona
> - Una propiedad normal es como una caja donde se guarda un valor. Una *extension property* no tiene caja (no hay *backing field*), así que cada vez que la miras **se calcula de nuevo**. Por eso no puede tener `= 0` ni `field`.
> - Pasar a minúsculas primero hace que `"AEIOU"` cuente 5 sin tener que añadir las mayúsculas a la lista de vocales.
> - Aunque se escriba como propiedad (`text.vowelCount`), por dentro es una función: igual que en el ejercicio 2, `String` no cambia.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Constante de compilación | `const val NAME = literal` | Solo primitivos o `String`; solo en el nivel superior, `object` o `companion object`. |
| Espacio de nombres | `Clase.CONSTANTE` (desde el `companion object`) | Se usa sin crear objetos. |
| UPPER_SNAKE_CASE | `SPEED_OF_LIGHT` | Convención para constantes. |
| *Extension function* | `fun Tipo.nombre(): R { … }` | Añade un método sin modificar la clase; `this` es el receptor. |
| *Extension property* | `val Tipo.nombre: T get() = …` | Sin campo de respaldo: se calcula en cada lectura. |
| Partir por espacios | `split(Regex("\\s+"))` | Varios espacios seguidos cuentan como uno. |
| Unir una lista | `lista.joinToString(" ")` | Un `String` con el separador entre elementos. |
| Carácter en un texto | `c in "aeiou"` | Llama a `contains(c)`. |

## Relaciones

- Teoría: [[08 - POO III]] · [[06 - POO I]]
- Bloque anterior: [[Ejercicios Bloque 10]] · Bloque siguiente: [[Ejercicios Bloque 12]]
- Mismos enunciados en el boletín: [[08.1 - Ejercicios 8 POO III#Ejercicio 8.3 · Constantes const en un companion object|8.3]] · [[08.1 - Ejercicios 8 POO III#Ejercicio 8.5 · Extension function reverseWords|8.5]] · [[08.1 - Ejercicios 8 POO III#Ejercicio 8.6 · Extension property vowelCount|8.6]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Declarar constantes con `const val` en un `companion object`
- [ ] Saber dónde se permite `const` y con qué tipos
- [ ] Crear una *extension function* y llamarla con punto
- [ ] Explicar por qué una extensión no puede usar lo privado de la clase
- [ ] Crear una *extension property* con `get()` y explicar por qué no admite inicializador
- [ ] Partir un texto en palabras con `split` aunque haya varios espacios seguidos
