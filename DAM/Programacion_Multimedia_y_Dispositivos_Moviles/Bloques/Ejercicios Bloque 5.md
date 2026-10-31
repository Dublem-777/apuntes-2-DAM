---
asignatura: PMDM
tema: 4
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/ejercicios
---

# Bloque 5 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[02 - Jerarquia de tipos]] · [[04 - Estructuras básicas]]
> Bloque anterior: [[Ejercicios Bloque 4]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque05/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 4.4, 4.6 y 4.7 de [[04.1 - Ejercicios 4 Estructuras básicas|el boletín 4]].
> - **Ejercicio 2:** es tu código del proyecto `Ejercicio4.6`, copiado tal cual.
> - **Ejercicio 3:** tu proyecto del boletín no tenía el árbol con `repeat` (la carpeta `Ejercicio4.7` contiene el juego de adivinar), así que está hecho a partir de tu ejercicio 2, cambiando solo los bucles.
> - **Ejercicio 1:** solución propia (ver el aviso del ejercicio sobre el proyecto `Ejercicio4.4`).
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque05/Ejercicio5.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Función `name` con `when` sobre `Any?`]]
- [[#Ejercicio 2 · Árbol de Navidad con bucles]]
- [[#Ejercicio 3 · Árbol de Navidad con `repeat`]]

---

## Ejercicio 1 · Función `name` con `when` sobre `Any?`

> [!question] Enunciado
> Completa el siguiente código para que la función `name` devuelva:
>
> - `"Nothing"` si recibe `null`.
> - `"Small number"` si recibe el 1, el 2 o el 3.
> - `"Magic number"` si recibe el 7 o el 13.
> - `"Big number"` si es un número entre 4 y 100.
> - `"String"` si es de tipo cadena.
> - `"Integer"` si es de tipo `Int` o `Long`.
> - `"No idea"` en cualquier otro caso.
>
> ```kotlin
> fun name(a: Any?): String = when (a) {
>     // ...
> }
> ```

### Clases y métodos introducidos
- `when (a)` como **expresión**: su resultado es directamente el valor que devuelve la función (función de expresión única).
- Ramas por **valor**: `1, 2, 3 ->` compara `a` con cada valor; la coma significa «o».
- Ramas por **tipo**: `is String ->`, `is Int, is Long ->`.
- **Condición de guarda** (Kotlin 2.2): `is Int if a in 4..100 ->`. La rama solo se elige si se cumplen **las dos cosas**: que `a` sea `Int` y que esté entre 4 y 100.

> **Términos explicados:** [[04 - Estructuras básicas#3. `when` con sujeto|`when` con sujeto]] · [[04 - Estructuras básicas#4. `when` como expresión|`when` como expresión]] · [[04 - Estructuras básicas#5. Condiciones de guarda en `when`|condiciones de guarda]] · [[02 - Jerarquia de tipos#9. Los tipos Any y Any?|`Any?`]] · [[02 - Jerarquia de tipos#11. Comprobación de tipo|operador `is`]]

#### Ejemplo simple de funcionamiento
```kotlin
fun describe(x: Any?): String = when (x) {
    null -> "nada"
    0 -> "cero"
    is Int if x > 0 -> "entero positivo"
    is Int -> "entero negativo"
    else -> "otra cosa"
}
// describe(5) → "entero positivo" · describe(-2) → "entero negativo"
```

### Código fuente (`Ejercicio5.1/src/Main.kt`)

```kotlin
fun name(a: Any?): String = when (a) {
    null -> "Nothing"
    1, 2, 3 -> "Small number"
    7, 13 -> "Magic number"
    is Int if a in 4..100 -> "Big number"   // condición de guarda
    is String -> "String"
    is Int, is Long -> "Integer"
    else -> "No idea"
}

fun main() {
    // Valores de prueba de todos los tipos posibles, incluido null
    val values: Array<Any?> = arrayOf(null, 1, 2, 3, 7, 13, 4, 50, 100, "Kotlin", 101, 5L, -8, 1.5, 7.0, true)
    for (value in values) {
        println("$value → ${name(value)}")
    }
}
```

### Explicación paso a paso
1. **`null` primero:** es el caso más especial y no tiene tipo; lo atendemos antes que nada.
2. **Valores concretos:** `1, 2, 3` y `7, 13` comparan `a` por igualdad. Van **antes** que el rango 4–100, porque 7 y 13 también están dentro de él y queremos que digan «Magic number».
3. **Rango con guarda:** como `a` es `Any?`, no se puede escribir directamente `in 4..100` (un rango de `Int` solo sabe comprobar `Int`). Con `is Int if a in 4..100` primero se confirma que es `Int` y, gracias al *smart cast*, la guarda ya puede usarlo como entero.
4. **Tipos:** `is String` para cadenas e `is Int, is Long` para los enteros que no han entrado antes (101, -8, `5L`…).
5. **`else`:** cualquier otra cosa (`Double`, `Boolean`…) es «No idea». Como el `when` es una expresión, el `else` es obligatorio.
6. **Pruebas:** `main()` recorre un `Array<Any?>` con un valor de cada caso, incluidos los límites 4 y 100 y los que quedan fuera.

> [!tip] Prueba
> ```text
> null → Nothing
> 1 → Small number
> 2 → Small number
> 3 → Small number
> 7 → Magic number
> 13 → Magic number
> 4 → Big number
> 50 → Big number
> 100 → Big number
> Kotlin → String
> 101 → Integer
> 5 → Integer
> -8 → Integer
> 1.5 → No idea
> 7.0 → No idea
> true → No idea
> ```
> El `5` que da `Integer` es el `5L` (`Long`): al imprimir un `Long` no aparece la `L`.

> [!note]- 🧠 Por qué funciona
> - `when` prueba las ramas **en orden** y se queda con la primera que encaja. Por eso el orden de las ramas es lo que resuelve los solapamientos: 7 es número mágico y no «grande», y 50 es «grande» y no «Integer».
> - `1, 2, 3 ->` compara con `==`. Un `Long` `2L` **no** es igual al `Int` `2`, así que los `Long` nunca entran en las ramas de valores: van directos a «Integer». Igual pasa con `7.0`, que es un `Double`.
> - La guarda se evalúa **solo** si `is Int` es cierto, así que dentro de ella `a` ya es un `Int` y se puede comparar con el rango sin errores.

> [!warning] El proyecto `Ejercicio4.4` de `Programas_clase/`
> Tu versión del proyecto convierte el número a `Double` y usa `in 1.0..3.0 -> "Small number"`. Al ejecutarla, **`name(1.5)` devuelve `"Small number"`**, y el enunciado solo habla del 1, el 2 y el 3. Además, su `main()` termina con `println(5.5)` en vez de `println(name(5.5))`. Si quieres arreglarlo, cambia el rango por `1.0, 2.0, 3.0 ->` o usa la versión de arriba.

---

## Ejercicio 2 · Árbol de Navidad con bucles

> [!question] Enunciado
> Escribe un programa que solicite un valor entero correspondiente a la altura del árbol en filas y, usando bucles (**sin usar `repeat`**), muestre el árbol de Navidad correspondiente. La última fila siempre tiene **tres asteriscos**, ya que corresponde a la base del árbol (ver imagen en los apuntes).

### Clases y métodos introducidos
- `for (i in 0 until n)`: repite el bloque `n` veces, con `i` de `0` a `n - 1` (`until` excluye el límite superior).
- `print()` sin salto de línea y `println()` para terminar cada fila.
- Bucles **anidados**: un `for` para las filas y, dentro, otros dos para los espacios y los asteriscos de esa fila.

> **Términos explicados:** [[04 - Estructuras básicas#6. Bucles `for` y `repeat`|bucle `for`]] · [[02 - Jerarquia de tipos#4. Rangos y progresiones|rangos y `until`]] · [[03 - Funciones#1. Definición de funciones|funciones]]

#### Ejemplo simple de funcionamiento
```kotlin
for (row in 0 until 3) {
    for (col in 0 until row + 1) print("*")
    println()
}
// *
// **
// ***
```

### Código fuente (`Ejercicio4.6/src/Main.kt`)

```kotlin
fun treeConstruction(value: Int) {
    val filasHojas: Int = value -1
    val spaceLimit: Int = filasHojas - 1

    for (i in 0 until filasHojas) {
        val espacios = spaceLimit - i
        for (s in 0 until espacios) {
            print(" ")
        }

        val asteriscos = 2 * i + 1
        for (j in 0 until asteriscos) {
            print("*")
        }
        println()
    }

    val espaciosBase: Int = if (filasHojas >= 2) filasHojas - 2 else 0
    for (s in 0 until espaciosBase) {
        print(" ")
    }
    for (a in 0 until 3) {
        print("*")
    }
    println()
}

fun main() {
    print("Introduce la altura del arbol: ")
    val height: Int = readln().toInt()
    treeConstruction(height)
}
```

### Explicación paso a paso
1. **Copa y base:** la altura incluye la base, así que la copa tiene `filasHojas = value - 1` filas.
2. **Asteriscos de cada fila:** `2 * i + 1` da los impares 1, 3, 5, 7…, y así cada fila crece uno por cada lado.
3. **Espacios de cada fila:** la última fila de la copa no lleva espacios (`spaceLimit - i` llega a 0) y cada fila de arriba tiene uno más. Eso centra la copa.
4. **Base:** la punta está en la columna `filasHojas - 1`. Para que los 3 asteriscos de la base queden centrados debajo, empiezan una columna antes: `filasHojas - 2` espacios. Con árboles muy bajos (copa de 0 o 1 fila) ese número saldría negativo, así que se usa 0.
5. **`main()`** solo lee la altura y llama a `treeConstruction`.

> [!tip] Prueba (los espacios se ven como `·`)
> ```text
> Introduce la altura del arbol: 5
> ···*
> ··***
> ·*****
> *******
> ··***
> ```
> Con altura 7, la copa tiene 6 filas (hasta 11 asteriscos) y la base lleva 4 espacios: sigue centrada.

> [!note]- 🧠 Por qué funciona
> - Cada fila de la copa ocupa desde la columna `espacios` hasta `espacios + asteriscos - 1`. Su centro es `(spaceLimit - i) + i = spaceLimit`: **la misma columna en todas las filas**. Por eso la copa sale recta.
> - La base de 3 asteriscos tiene su centro en `espaciosBase + 1 = filasHojas - 1 = spaceLimit`: la misma columna que la copa.
> - Con altura 2 (copa de una sola fila, `*`) la base no queda centrada, porque haría falta un espacio **negativo**. Es el único caso que se descuadra.

> [!warning] Alturas no válidas
> Con altura 0 o negativa, `0 until filasHojas` es un rango vacío y solo se dibuja la base `***`. Si quieres rechazarlas, añade al principio de `main()` algo como `require(height >= 1) { "La altura debe ser al menos 1" }` ([[04 - Estructuras básicas#Validación con `require`, `check` y `error`|ver `require`]]).

---

## Ejercicio 3 · Árbol de Navidad con `repeat`

> [!question] Enunciado
> Realiza el mismo ejercicio anterior usando la función `repeat` en vez de bucles.

### Clases y métodos introducidos
- `repeat(n) { … }`: ejecuta el bloque `n` veces. No es un bucle del lenguaje, sino una **función** de la biblioteca estándar que recibe el número de veces y una lambda.
- `repeat(n) { i -> … }`: la lambda recibe el número de vuelta, empezando en `0`, igual que el `i` de `for (i in 0 until n)`.
- Si no necesitas el número de vuelta, no hace falta nombrarlo: `repeat(3) { print("*") }`.

> **Términos explicados:** [[04 - Estructuras básicas#6. Bucles `for` y `repeat`|`repeat`]]

#### Ejemplo simple de funcionamiento
```kotlin
repeat(3) { print("*") }   // ***
println()
repeat(3) { i -> print(i) } // 012
```

### Código fuente (`Ejercicio5.3/src/Main.kt`)

```kotlin
fun treeConstruction(value: Int) {
    val filasHojas: Int = value - 1
    val spaceLimit: Int = filasHojas - 1

    repeat(filasHojas) { i ->
        val espacios = spaceLimit - i
        repeat(espacios) {
            print(" ")
        }

        val asteriscos = 2 * i + 1
        repeat(asteriscos) {
            print("*")
        }
        println()
    }

    val espaciosBase: Int = if (filasHojas >= 2) filasHojas - 2 else 0
    repeat(espaciosBase) {
        print(" ")
    }
    repeat(3) {
        print("*")
    }
    println()
}

fun main() {
    print("Introduce la altura del arbol: ")
    val height: Int = readln().toInt()
    treeConstruction(height)
}
```

### Explicación paso a paso
1. **Misma lógica:** todos los cálculos (`filasHojas`, `espacios`, `asteriscos`, `espaciosBase`) son idénticos a los del ejercicio 2. Solo cambia **cómo se repite**.
2. **Filas de la copa:** `for (i in 0 until filasHojas)` pasa a ser `repeat(filasHojas) { i -> … }`. Aquí sí nombramos `i`, porque hace falta para calcular los espacios y los asteriscos.
3. **Espacios y asteriscos:** `for (s in 0 until espacios)` pasa a ser `repeat(espacios) { … }`. En el `for` la variable `s` no se usaba, así que con `repeat` ni siquiera se escribe.
4. **Base:** igual, `repeat(espaciosBase)` y `repeat(3)`.

> [!tip] Prueba
> ```text
> Introduce la altura del arbol: 5
>    *
>   ***
>  *****
> *******
>   ***
> ```
> Para las alturas 1, 3 y 5, la salida es **idéntica carácter a carácter** a la del ejercicio 2 (comprobado con `diff`).

> [!note]- 🧠 Por qué funciona
> - `repeat(n) { i -> … }` hace exactamente lo mismo que `for (i in 0 until n) { … }`: `n` vueltas con `i` de `0` a `n - 1`.
> - Con un número negativo o 0, `repeat` no ejecuta el bloque ni una vez (igual que un rango `0 until n` vacío). Por eso el comportamiento con alturas raras también coincide con el del ejercicio 2.

> [!tip] `for` vs. `repeat`
> | | `for (i in 0 until n)` | `repeat(n) { i -> }` |
> | --- | --- | --- |
> | Qué es | Estructura del lenguaje | Función que recibe una lambda |
> | Recorre | Cualquier rango, colección o `String` | Solo cuenta de `0` a `n - 1` |
> | `break` / `continue` | Sí | No (es una lambda) |
> | Cuándo usarlo | Cuando recorres algo | Cuando solo quieres «hazlo n veces» |

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Rama por valores | `1, 2, 3 -> …` | Compara el sujeto con `==`; la coma es «o». |
| Rama por tipo | `is String -> …` | Comprueba el tipo real; activa el *smart cast*. |
| Condición de guarda | `is Int if a in 4..100 -> …` | La rama solo entra si se cumplen tipo y guarda (Kotlin 2.2). |
| Orden de las ramas | primera que encaja | Resuelve los solapamientos (7 es «Magic», no «Big»). |
| `Int` vs `Long` | `2 == 2L` es `false` | Distinto tipo, distinta igualdad. |
| Bucle con contador | `for (i in 0 until n)` | `n` vueltas, `i` de 0 a `n - 1`. |
| Repetir n veces | `repeat(n) { i -> … }` | Igual que el `for`, pero es una función; sin `break`. |
| Fila centrada | espacios = `limite - i`, asteriscos = `2 * i + 1` | El centro de todas las filas cae en la misma columna. |

## Relaciones

- Teoría: [[02 - Jerarquia de tipos]] · [[04 - Estructuras básicas]]
- Bloque anterior: [[Ejercicios Bloque 4]] · Bloque siguiente: [[Ejercicios Bloque 6]]
- Mismos enunciados en el boletín: [[04.1 - Ejercicios 4 Estructuras básicas#Ejercicio 4.4 · Expresión `when` sobre `Any?`|4.4]] · [[04.1 - Ejercicios 4 Estructuras básicas#Ejercicio 4.6 · Árbol de Navidad con bucles|4.6]] · [[04.1 - Ejercicios 4 Estructuras básicas#Ejercicio 4.7 · Árbol de Navidad con `repeat`|4.7]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Ordenar las ramas de un `when` para resolver casos que se solapan
- [ ] Usar condiciones de guarda (`is Int if …`) en un `when` con sujeto
- [ ] Explicar por qué `2L` no entra en la rama `1, 2, 3`
- [ ] Dibujar una figura centrada con bucles anidados
- [ ] Pasar un `for` con contador a `repeat` y saber qué se pierde (`break`/`continue`)
