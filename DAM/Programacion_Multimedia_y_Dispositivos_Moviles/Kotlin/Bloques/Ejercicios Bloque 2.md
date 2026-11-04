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

# Bloque 2 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[01 - Introduccion a Kotlin]] · [[02 - Jerarquia de tipos]] · [[04 - Estructuras básicas]]
> Bloque anterior: [[Ejercicios Bloque 1]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque02/`

> [!note] Sobre las soluciones
> Soluciones didácticas desarrolladas para este bloque con conceptos explicados en los temas anteriores. Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque02/Ejercicio2.K/` (ver **Ruta fuente**).

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Tres números en orden]]
- [[#Ejercicio 2 · Mayúscula, minúscula o no letra]]

---

## Ejercicio 1 · Tres números en orden

> [!question] Enunciado
> Realiza un programa que solicite por consola tres números enteros y los muestre por pantalla en orden.
>
> *Nota:* los `if` en Kotlin tienen una estructura similar a la de Java.

### Clases y métodos introducidos
- `readln().toInt()`: lee una línea y la convierte a `Int`. Lanza `NumberFormatException` si el texto no es un número entero.
- `if` como **sentencia**: igual que en Java, `if (condición) { … }`. Aquí lo usamos solo para decidir si hay que intercambiar dos valores.
- **Intercambio con variable auxiliar** (`temp`): para cambiar el contenido de dos variables hace falta una tercera, igual que para cambiar el agua de dos vasos hace falta un vaso vacío.

> **Términos explicados:** [[01 - Introduccion a Kotlin#6.1 readln() y compañía|`readln()` y conversiones]] · [[01 - Introduccion a Kotlin#5.1 Los dos grupos: val y var|`val` y `var`]] · [[04 - Estructuras básicas#1. La estructura `if`|estructura `if`]]

#### Ejemplo simple de funcionamiento
```kotlin
var a = 9
var b = 4
if (a > b) {          // están al revés: los intercambiamos
    val temp = a      // guardamos a para no perderlo
    a = b
    b = temp
}
println("$a, $b")     // 4, 9
```

### Código fuente (`Ejercicio2.1/src/Main.kt`)

```kotlin
fun main() {
    // Pedimos los tres números. Son var porque los vamos a reordenar
    print("Introduce el primer número: ")
    var first: Int = readln().toInt()
    print("Introduce el segundo número: ")
    var second: Int = readln().toInt()
    print("Introduce el tercer número: ")
    var third: Int = readln().toInt()

    // Paso 1: ordenamos first y second
    if (first > second) {
        val temp = first
        first = second
        second = temp
    }

    // Paso 2: llevamos el menor de todos a first
    if (first > third) {
        val temp = first
        first = third
        third = temp
    }

    // Paso 3: ordenamos los dos que quedan
    if (second > third) {
        val temp = second
        second = third
        third = temp
    }

    println("Los números en orden son: $first, $second, $third")
}
```

### Explicación paso a paso
1. **Lectura:** cada número se lee con `readln().toInt()`. Son `var` y no `val` porque el programa va a cambiar su contenido al ordenarlos.
2. **Idea general:** en vez de escribir los 6 casos posibles (a<b<c, a<c<b…), comparamos **parejas** y, si están al revés, las intercambiamos. Con tres comparaciones basta para ordenar tres números.
3. **Paso 1 (`first` vs `second`):** al acabar, `first ≤ second`.
4. **Paso 2 (`first` vs `third`):** si `third` es menor, pasa a `first`. Ahora `first` es **el menor de los tres**, porque ya era menor que `second` y ahora también lo es que `third`.
5. **Paso 3 (`second` vs `third`):** el menor ya está colocado, solo falta ordenar los otros dos.
6. **Intercambio:** dentro de cada `if`, `temp` guarda uno de los valores antes de pisarlo. Es `val` porque solo se asigna una vez y vive solo dentro de las llaves del `if`.
7. **Salida:** con plantillas de cadena (`$first`), como en el Bloque 1.

> [!tip] Prueba
> ```text
> Introduce el primer número: 7
> Introduce el segundo número: 2
> Introduce el tercer número: 5
> Los números en orden son: 2, 5, 7
> ```
> Traza: `7,2,5` → paso 1 → `2,7,5` → paso 2 (2 > 5? no) → `2,7,5` → paso 3 → `2,5,7`.

> [!note]- 🧠 Por qué funciona
> - Tras el **paso 1**, `first ≤ second`.
> - El **paso 2** deja en `first` el mínimo de `first` y `third`. Como `first` ya era ≤ `second`, ese valor es el mínimo de los tres y ya no se moverá.
> - El **paso 3** solo toca `second` y `third`, así que al acabar `second ≤ third`.
> - Resultado: `first ≤ second ≤ third` para **cualquier** combinación de entrada, también con números repetidos (si son iguales, `>` es falso y no se intercambian).

> [!tip] Comparación con Java
> El `if` es idéntico al de Java, como dice el enunciado. La diferencia está en las variables: en Java escribirías `int temp = first;`; en Kotlin, `val temp = first` y el tipo `Int` se deduce solo.

---

## Ejercicio 2 · Mayúscula, minúscula o no letra

> [!question] Enunciado
> Realiza un programa que solicite por consola una cadena de caracteres y diga, para cada carácter, si está en mayúscula, si está en minúscula o si no es una letra (la **ñ no cuenta** como letra). Para ello debe comprobar que el **código numérico** del carácter está en el rango de códigos que va de la `A` a la `Z` o de la `a` a la `z`.

### Clases y métodos introducidos
- `for (character in text)`: recorre un `String` carácter a carácter. Cada vuelta, `character` es un `Char`.
- `Char.code`: devuelve el código Unicode del carácter como `Int` (`'A'.code == 65`). En Kotlin un `Char` **no es un número**, así que no se puede comparar directamente con un `Int` como en Java: hay que pedirle su `code`.
- Rangos `a..b`: `'A'.code..'Z'.code` es el rango `65..90`, y `x in rango` comprueba si `x` está dentro.
- `when` con sujeto: como un `switch` de Java, pero cada rama puede ser una condición `in rango`.

> **Términos explicados:** [[02 - Jerarquia de tipos#3. Caracteres|`Char` y su `code`]] · [[02 - Jerarquia de tipos#4. Rangos y progresiones|rangos]] · [[02 - Jerarquia de tipos#6. Strings|recorrer un `String`]] · [[04 - Estructuras básicas#3. `when` con sujeto|`when` con sujeto]] · [[04 - Estructuras básicas#6. Bucles `for` y `repeat`|bucle `for`]]

#### Ejemplo simple de funcionamiento
```kotlin
println('A'.code)                    // 65
println('z'.code)                    // 122
println('ñ'.code)                    // 241: fuera de 65..90 y de 97..122
println(70 in 'A'.code..'Z'.code)    // true (70 es la 'F')
```

### Código fuente (`Ejercicio2.2/src/Main.kt`)

```kotlin
fun main() {
    print("Introduce una cadena: ")
    val text: String = readln()

    // Rangos de códigos: de la A a la Z (65–90) y de la a a la z (97–122)
    val upperCaseCodes = 'A'.code..'Z'.code
    val lowerCaseCodes = 'a'.code..'z'.code

    // Recorremos la cadena carácter a carácter
    for (character in text) {
        when (character.code) {
            in upperCaseCodes -> println("'$character' está en mayúscula")
            in lowerCaseCodes -> println("'$character' está en minúscula")
            else -> println("'$character' no es una letra")
        }
    }
}
```

### Explicación paso a paso
1. **Lectura:** `readln()` devuelve la línea completa como `String`, espacios incluidos.
2. **Rangos:** en vez de escribir los números mágicos `65..90` y `97..122`, los calculamos con `'A'.code..'Z'.code`. Se lee mejor y no hace falta saberse la tabla ASCII.
3. **Recorrido:** el `for … in` da cada carácter del texto, uno por vuelta.
4. **Clasificación con `when`:** el sujeto es `character.code`, que es un `Int`. La primera rama cuyo rango lo contenga es la que se ejecuta; si no entra en ninguno, salta el `else`.
5. **La ñ:** su código es 241, que no está en ninguno de los dos rangos, así que cae en el `else`, tal como pide el enunciado. Lo mismo pasa con las vocales con tilde (`'á'.code == 225`).
6. **Salida:** `'$character'` mete el carácter en el mensaje entre comillas simples, para que se vean también los espacios.

> [!tip] Prueba
> ```text
> Introduce una cadena: Año 2!
> 'A' está en mayúscula
> 'ñ' no es una letra
> 'o' está en minúscula
> ' ' no es una letra
> '2' no es una letra
> '!' no es una letra
> ```

> [!note]- 🧠 Por qué funciona
> - Las letras inglesas están **seguidas** en la tabla de códigos: `A`=65 … `Z`=90 y `a`=97 … `z`=122. Por eso basta con dos rangos para reconocerlas.
> - Entre 91 y 96 hay símbolos (`[`, `\`, `]`, `^`, `_`, `` ` ``) que no entran en ningún rango: por eso no se puede usar un único rango `65..122`.
> - `when` evalúa las ramas en orden y se queda con la primera que cumple, igual que una cadena de `if … else if … else`.

> [!warning] Por qué no usar `isUpperCase()` / `isLetter()`
> Kotlin tiene `character.isUpperCase()` e `isLetter()`, pero consideran letras la `ñ`, la `Ñ` y las vocales con tilde. El enunciado pide que la ñ **no** cuente y que se compruebe el **código numérico**, así que hay que usar `code` y rangos.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Leer un entero | `readln().toInt()` | Convierte la línea a `Int`; lanza `NumberFormatException` si no es válida. |
| Intercambio | `val temp = a; a = b; b = temp` | Una variable auxiliar evita perder uno de los valores. |
| Ordenar 3 valores | 3 `if` por parejas | (1,2), (1,3), (2,3): al acabar quedan de menor a mayor. |
| Código de un carácter | `Char.code` | Devuelve el código Unicode como `Int` (`'A'.code == 65`). |
| Rango | `a..b` / `x in a..b` | Intervalo cerrado; `in` comprueba si un valor está dentro. |
| Recorrer un `String` | `for (c in text)` | Da un `Char` en cada vuelta. |
| `when` con sujeto | `when (x) { in r -> … else -> … }` | Ejecuta la primera rama que cumple; `else` recoge el resto. |

## Relaciones

- Teoría: [[01 - Introduccion a Kotlin]] · [[02 - Jerarquia de tipos]] · [[04 - Estructuras básicas]]
- Bloque anterior: [[Ejercicios Bloque 1]] · Bloque siguiente: [[Ejercicios Bloque 3]]
- Boletín con el mismo estilo: [[04.1 - Ejercicios 4 Estructuras básicas]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Intercambiar dos variables con una auxiliar
- [ ] Ordenar tres números con tres comparaciones por parejas
- [ ] Obtener el código de un `Char` con `.code`
- [ ] Comprobar si un valor está en un rango con `in`
- [ ] Clasificar con `when` y ramas `in rango`
