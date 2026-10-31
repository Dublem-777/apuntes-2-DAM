---
asignatura: PMDM
tema: 4
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-funciones
  - DAM/pmdm/ejercicios
---

# Bloque 4 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[03 - Funciones]] · [[04 - Estructuras básicas]] · [[06 - POO I]]
> Bloque anterior: [[Ejercicios Bloque 3]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque4/`

> [!note] Sobre las soluciones
> Soluciones didácticas desarrolladas para este bloque con conceptos explicados en los temas anteriores. Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque4/Ejercicio4.K/` (ver **Ruta fuente**). Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · `calculateAverage` con `vararg`]]
- [[#Ejercicio 2 · Clase `De0a100` con función infija `contains`]]
- [[#Ejercicio 3 · Clasificar a un trabajador por edad e ingresos]]
- [[#Ejercicio 4 · Rango de edad con `when` sin sujeto]]
- [[#Ejercicio 5 · Rango de edad con `when` con sujeto]]

---

## Ejercicio 1 · `calculateAverage` con `vararg`

> [!question] Enunciado
> Escribe una función en Kotlin llamada `calculateAverage` que reciba una lista variable de números enteros y calcule su media aritmética. El `main()` deberá llamar a la función con los valores incluidos en un `IntArray` definido previamente en el `main()`.

### Clases y métodos introducidos
- `vararg numbers: Int`: el parámetro acepta **cualquier cantidad** de enteros (0, 1, 5…). Dentro de la función, `numbers` se comporta como un `IntArray`. Equivale a `int... numbers` en Java.
- **Spread operator** `*`: `calculateAverage(*grades)` «desempaqueta» el array y pasa cada elemento como un argumento suelto. En Java se puede pasar el array tal cual; en Kotlin, **no**: hace falta el `*`.
- `IntArray.contentToString()`: muestra el contenido del array (`[7, 4, 9]`). Si imprimes el array directamente, sale una dirección de memoria, como en Java.
- `Int.toDouble()`: convierte la suma a `Double` para que la división no pierda los decimales.

> **Términos explicados:** [[03 - Funciones#9. varargs|`vararg`]] · [[03 - Funciones#10. Spread operator|spread operator]] · [[02 - Jerarquia de tipos#10. Arrays|`IntArray`]]

#### Ejemplo simple de funcionamiento
```kotlin
fun countArgs(vararg values: Int) = values.size

fun main() {
    println(countArgs())            // 0
    println(countArgs(5, 6, 7))     // 3
    val array = intArrayOf(1, 2)
    println(countArgs(*array))      // 2  (sin el * no compila)
}
```

### Código fuente (`Ejercicio4.1/src/Main.kt`)

```kotlin
// Recibe cualquier cantidad de enteros y devuelve su media
fun calculateAverage(vararg numbers: Int): Double {
    // Sin números no hay media: evitamos dividir entre 0
    if (numbers.isEmpty()) return 0.0

    var sum = 0
    for (number in numbers) {
        sum += number
    }
    // toDouble() para que la división conserve los decimales
    return sum.toDouble() / numbers.size
}

fun main() {
    val grades: IntArray = intArrayOf(7, 4, 9, 6, 8)

    // El spread operator (*) "desempaqueta" el array en argumentos sueltos
    val average = calculateAverage(*grades)
    println("La media de ${grades.contentToString()} es $average")

    // También se puede llamar con valores sueltos
    println("La media de 3, 4 es ${calculateAverage(3, 4)}")
}
```

### Explicación paso a paso
1. **Firma:** `vararg numbers: Int` recibe una lista variable de enteros y la función devuelve un `Double`, porque una media puede tener decimales aunque los datos sean enteros.
2. **Lista vacía:** como `vararg` admite **cero** argumentos, `calculateAverage()` es una llamada válida. Sin la comprobación `isEmpty()` dividiríamos `0.0 / 0` y saldría `NaN` (*Not a Number*).
3. **Suma:** recorremos `numbers` como cualquier array.
4. **División:** `sum` es `Int` y `numbers.size` también. Si dividiéramos directamente (`34 / 5`), daría `6`. Con `sum.toDouble()` da `6.8`.
5. **Llamada desde `main()`:** el enunciado pide definir antes un `IntArray`, así que lo pasamos con `*grades`. La segunda llamada demuestra que también acepta valores sueltos.

> [!tip] Prueba
> ```text
> La media de [7, 4, 9, 6, 8] es 6.8
> La media de 3, 4 es 3.5
> ```
> (7 + 4 + 9 + 6 + 8) / 5 = 34 / 5 = 6.8.

> [!note]- 🧠 Por qué funciona
> - Un `vararg` de `Int` llega a la función como un `IntArray`. Por eso se puede recorrer con `for` y usar `size` e `isEmpty()`.
> - El `*` es necesario porque, sin él, Kotlin entendería que intentas pasar **un solo argumento** de tipo `IntArray` a un parámetro que espera `Int` sueltos, y no compila.
> - Convertir **uno** de los dos operandos a `Double` es suficiente: `Double / Int` da `Double`.

---

## Ejercicio 2 · Clase `De0a100` con función infija `contains`

> [!question] Enunciado
> Escribe una clase en Kotlin llamada `De0a100` que represente un rango de números enteros de 0 a 100. Dentro de esta clase, define una función infija `contains` que permita verificar si un número entero está dentro del rango definido por la instancia de `De0a100`.

### Clases y métodos introducidos
- `class De0a100 { … }`: una clase con dos propiedades, `start` y `end`. El nombre lo fija el enunciado; por eso no está en inglés.
- `infix fun`: una función que se puede llamar **sin punto ni paréntesis**: `range contains 50` en vez de `range.contains(50)`. Requisitos: que sea un método de una clase (o una función de extensión), que tenga **un único parámetro** y que ese parámetro no sea `vararg` ni tenga valor por defecto.
- Instanciación sin `new`: `val range = De0a100()`.

> **Términos explicados:** [[03 - Funciones#11. Notación infija (infix)|notación infija]] · [[06 - POO I#1. Clases|clases]] · [[06 - POO I#3. Instanciación|instanciación]] · [[06 - POO I#5. Propiedades|propiedades]]

#### Ejemplo simple de funcionamiento
```kotlin
class Counter {
    var total = 0
    infix fun add(amount: Int) {
        total += amount
    }
}

fun main() {
    val counter = Counter()
    counter add 5          // lo mismo que counter.add(5)
    println(counter.total) // 5
}
```

### Código fuente (`Ejercicio4.2/src/Main.kt`)

```kotlin
// Representa el rango de enteros de 0 a 100
class De0a100 {
    val start = 0
    val end = 100

    // infix permite llamarla como: rango contains número
    infix fun contains(number: Int): Boolean = number >= start && number <= end
}

fun main() {
    val range = De0a100()

    // Llamada normal y llamada en notación infija
    println("¿50 está en el rango? ${range.contains(50)}")
    println("¿0 está en el rango? ${range contains 0}")
    println("¿100 está en el rango? ${range contains 100}")
    println("¿-1 está en el rango? ${range contains -1}")
    println("¿101 está en el rango? ${range contains 101}")
}
```

### Explicación paso a paso
1. **La clase:** `De0a100` guarda los límites del rango en dos propiedades `val`, `start = 0` y `end = 100`. Son `val` porque el rango no cambia.
2. **La función `contains`:** recibe un único `Int` y devuelve `true` si está entre `start` y `end`, **ambos incluidos** (`>=` y `<=`). Como solo calcula una expresión, se escribe con `=`.
3. **`infix`:** delante de `fun`, permite la llamada sin punto ni paréntesis.
4. **En `main()`:** creamos una instancia y comprobamos los dos estilos de llamada. Las pruebas incluyen los **límites** (0 y 100) y los valores justo fuera (-1 y 101), que es donde suelen estar los errores.

> [!tip] Prueba
> ```text
> ¿50 está en el rango? true
> ¿0 está en el rango? true
> ¿100 está en el rango? true
> ¿-1 está en el rango? false
> ¿101 está en el rango? false
> ```

> [!note]- 🧠 Por qué funciona
> - `range contains 50` y `range.contains(50)` compilan exactamente igual: `infix` solo cambia cómo se **escribe** la llamada.
> - `infix` necesita un receptor (el objeto a la izquierda), así que siempre se usa sobre una **instancia**: `range contains 0`, nunca `contains 0` a secas.
> - Por eso no puede ser una función de nivel superior: sin objeto receptor no habría nada a la izquierda del operador.

> [!tip] Para ir más allá: `in`
> Si en vez de `infix` la marcas como `operator fun contains(number: Int)`, Kotlin te deja escribir `50 in range`, igual que con los rangos `0..100`. El operador `in` llama por debajo a `contains`. Las dos palabras se pueden combinar: `infix operator fun contains(...)`.

---

## Ejercicio 3 · Clasificar a un trabajador por edad e ingresos

> [!question] Enunciado
> Escribe un programa que solicite una edad y unos ingresos y clasifique al trabajador, indicando por pantalla la categoría a la que pertenece, según estos criterios:
>
> - Si la persona tiene **menos de 18 años**: `"Menor de edad"`.
> - Si tiene **entre 18 y 64 años**:
> 	- Ingreso anual menor que 20.000 → `"Joven trabajador con bajo ingreso"`.
> 	- Ingreso anual entre 20.000 y 60.000 → `"Adulto trabajador con ingreso medio"`.
> 	- Ingreso anual superior a 60.000 → `"Adulto trabajador con alto ingreso"`.
> - Si tiene **65 años o más**:
> 	- Ingreso anual menor que 15.000 → `"Anciano con bajo ingreso"`.
> 	- Ingreso anual entre 15.000 y 40.000 → `"Anciano con ingreso medio"`.
> 	- Ingreso anual superior a 40.000 → `"Anciano con alto ingreso"`.

### Clases y métodos introducidos
- `when` **sin sujeto** usado como **expresión**: cada rama es una condición y el resultado (un `String`) se guarda en `category`.
- `when` **anidados**: dentro de una rama va otro `when`. Es la forma limpia de expresar «primero por edad y, dentro, por ingresos».
- Separador `_` en números: `20_000` es lo mismo que `20000`, pero se lee mejor (como el punto de los miles en español).

> **Términos explicados:** [[04 - Estructuras básicas#2. `when` como selección de condiciones|`when` sin sujeto]] · [[04 - Estructuras básicas#4. `when` como expresión|`when` como expresión]] · [[02 - Jerarquia de tipos#2. Tipos numéricos|literales numéricos]]

#### Ejemplo simple de funcionamiento
```kotlin
val temperature = 28
val description = when {
    temperature < 10 -> "Frío"
    temperature <= 25 -> "Templado"
    else -> "Calor"
}
println(description)   // Calor
```

### Código fuente (`Ejercicio4.3/src/Main.kt`)

```kotlin
fun main() {
    print("Introduce la edad: ")
    val age: Int = readln().toInt()
    print("Introduce los ingresos anuales: ")
    val income: Double = readln().toDouble()

    // Primero se decide por la edad y, dentro, por los ingresos
    val category = when {
        age < 18 -> "Menor de edad"
        age <= 64 -> when {
            income < 20_000 -> "Joven trabajador con bajo ingreso"
            income <= 60_000 -> "Adulto trabajador con ingreso medio"
            else -> "Adulto trabajador con alto ingreso"
        }
        else -> when {
            income < 15_000 -> "Anciano con bajo ingreso"
            income <= 40_000 -> "Anciano con ingreso medio"
            else -> "Anciano con alto ingreso"
        }
    }

    println("Categoría: $category")
}
```

### Explicación paso a paso
1. **Lectura:** la edad como `Int` y los ingresos como `Double`, porque pueden tener céntimos.
2. **Primer nivel (edad):** `age < 18` → menor. Si no, `age <= 64` ya implica 18–64, porque la rama anterior descartó a los menores. Lo que queda (`else`) son los de 65 o más.
3. **Segundo nivel (ingresos):** dentro de cada grupo de edad, otro `when` con el mismo truco: `< 20_000`, luego `<= 60_000` (20 000–60 000) y el resto, más de 60 000.
4. **Límites:** «entre 20.000 y 60.000» incluye los dos extremos, así que 20 000 y 60 000 son ingreso medio (`<` en la primera rama y `<=` en la segunda). Lo mismo con 15 000 y 40 000.
5. **Un único `println`:** como el `when` devuelve el texto, se imprime una sola vez al final en vez de repetir `println` en las 7 ramas.

> [!tip] Prueba (10 ejecuciones reales, con los límites)
> ```text
> 15 años, 0 €        -> Menor de edad
> 30 años, 12000 €    -> Joven trabajador con bajo ingreso
> 40 años, 20000 €    -> Adulto trabajador con ingreso medio
> 50 años, 60000 €    -> Adulto trabajador con ingreso medio
> 45 años, 60000.01 € -> Adulto trabajador con alto ingreso
> 64 años, 75000 €    -> Adulto trabajador con alto ingreso
> 65 años, 14999 €    -> Anciano con bajo ingreso
> 70 años, 15000 €    -> Anciano con ingreso medio
> 80 años, 40000 €    -> Anciano con ingreso medio
> 90 años, 50000 €    -> Anciano con alto ingreso
> ```

> [!note]- 🧠 Por qué funciona
> - `when` evalúa las ramas **de arriba abajo** y se queda con la primera verdadera. Por eso no hace falta escribir `age >= 18 && age <= 64`: si llegamos a esa rama, ya sabemos que `age >= 18`.
> - Como `when` es aquí una **expresión** (su valor se asigna a `category`), tiene que ser exhaustivo: el `else` garantiza que siempre devuelve algo.
> - Con `if/else if` anidados saldría lo mismo, pero con `when` cada nivel queda alineado y se ve la tabla del enunciado de un vistazo.

---

## Ejercicio 4 · Rango de edad con `when` sin sujeto

> [!question] Enunciado
> Realiza un programa que, usando una estructura `when` **como sentencia similar a `if else if`**, compruebe si la edad introducida está en el rango de 1 a 10, de 11 a 20, de 21 a 30, de 31 a 40, de 41 a 50 o superior, y muestre por pantalla en qué rango está.

### Clases y métodos introducidos
- `when { … }` **sin sujeto**: no lleva nada entre paréntesis y cada rama es una condición booleana completa (`age <= 10`). Funciona exactamente como una cadena de `if / else if / else`.
- `when` como **sentencia**: cada rama ejecuta un `println`, y el `when` no devuelve nada que se use.

> **Términos explicados:** [[04 - Estructuras básicas#2. `when` como selección de condiciones|`when` sin sujeto]] · [[04 - Estructuras básicas#1. La estructura `if`|`if` / `else if`]]

#### Ejemplo simple de funcionamiento
```kotlin
val n = 7
// Estas dos estructuras hacen lo mismo
if (n < 5) println("Pequeño") else if (n < 10) println("Mediano") else println("Grande")

when {
    n < 5 -> println("Pequeño")
    n < 10 -> println("Mediano")
    else -> println("Grande")
}
```

### Código fuente (`Ejercicio4.4/src/Main.kt`)

```kotlin
fun main() {
    print("Introduce la edad: ")
    val age: Int = readln().toInt()

    // when sin sujeto: cada rama es una condición, como un if / else if
    when {
        age < 1 -> println("Edad no válida")
        age <= 10 -> println("Está en el rango de 1 a 10")
        age <= 20 -> println("Está en el rango de 11 a 20")
        age <= 30 -> println("Está en el rango de 21 a 30")
        age <= 40 -> println("Está en el rango de 31 a 40")
        age <= 50 -> println("Está en el rango de 41 a 50")
        else -> println("Es mayor de 50")
    }
}
```

### Explicación paso a paso
1. **Edad no válida:** los rangos del enunciado empiezan en 1, así que primero descartamos 0 y los negativos. Sin esa rama, una edad de -3 diría «de 1 a 10».
2. **Cada rama solo mira el límite superior:** si llegamos a `age <= 20`, las ramas anteriores ya han descartado las edades `<= 10`, así que la edad está entre 11 y 20.
3. **`else`:** recoge todo lo que no entró antes, es decir, más de 50.
4. **Como sentencia:** cada rama imprime su mensaje directamente.

> [!tip] Prueba (mismas entradas que el ejercicio 5)
> ```text
> -3  -> Edad no válida
> 0   -> Edad no válida
> 1   -> Está en el rango de 1 a 10
> 10  -> Está en el rango de 1 a 10
> 11  -> Está en el rango de 11 a 20
> 20  -> Está en el rango de 11 a 20
> 25  -> Está en el rango de 21 a 30
> 40  -> Está en el rango de 31 a 40
> 41  -> Está en el rango de 41 a 50
> 50  -> Está en el rango de 41 a 50
> 51  -> Es mayor de 50
> 120 -> Es mayor de 50
> ```

> [!note]- 🧠 Por qué funciona
> - Igual que en una cadena de `else if`, el **orden** de las ramas es lo que hace que baste con `<=`. Si pusieras `age <= 50` la primera, todas las edades de 1 a 50 entrarían en ella.
> - El `when` no tiene *fall-through*: a diferencia del `switch` de Java, no hace falta `break`. Solo se ejecuta la primera rama que se cumple.

---

## Ejercicio 5 · Rango de edad con `when` con sujeto

> [!question] Enunciado
> Realiza un programa que, usando una estructura `when` **como sentencia de comprobación contra una expresión**, compruebe si la edad introducida está en el rango de 1 a 10, de 11 a 20, de 21 a 30, de 31 a 40, de 41 a 50 o superior, y muestre por pantalla en qué rango está.

### Clases y métodos introducidos
- `when (age) { … }` **con sujeto**: la expresión entre paréntesis se compara con cada rama. Las ramas no son condiciones completas, sino valores o rangos: `in 1..10`.
- `in a..b`: comprueba si el sujeto está en el rango cerrado `a..b`.
- `Int.MAX_VALUE`: el mayor `Int` posible (2 147 483 647). Sirve para escribir «de 51 en adelante» como un rango.

> **Términos explicados:** [[04 - Estructuras básicas#3. `when` con sujeto|`when` con sujeto]] · [[02 - Jerarquia de tipos#4. Rangos y progresiones|rangos]]

#### Ejemplo simple de funcionamiento
```kotlin
val day = 6
when (day) {
    in 1..5 -> println("Laborable")
    6, 7 -> println("Fin de semana")
    else -> println("Día no válido")
}
```

### Código fuente (`Ejercicio4.5/src/Main.kt`)

```kotlin
fun main() {
    print("Introduce la edad: ")
    val age: Int = readln().toInt()

    // when con sujeto: se compara age con el rango de cada rama
    when (age) {
        in 1..10 -> println("Está en el rango de 1 a 10")
        in 11..20 -> println("Está en el rango de 11 a 20")
        in 21..30 -> println("Está en el rango de 21 a 30")
        in 31..40 -> println("Está en el rango de 31 a 40")
        in 41..50 -> println("Está en el rango de 41 a 50")
        in 51..Int.MAX_VALUE -> println("Es mayor de 50")
        else -> println("Edad no válida")
    }
}
```

### Explicación paso a paso
1. **Sujeto:** `when (age)` indica que todas las ramas se comparan con `age`.
2. **Ramas con rangos:** cada rama es un rango **completo** (`in 11..20`), con sus dos límites. Aquí el orden de las ramas no importa, porque los rangos no se solapan.
3. **«Superior a 50»:** con sujeto no se puede escribir `> 50` en una rama. Lo expresamos como el rango `51..Int.MAX_VALUE`.
4. **`else`:** como todos los positivos ya están cubiertos, al `else` solo llegan el 0 y los negativos: edad no válida.

> [!tip] Prueba
> ```text
> Introduce la edad: 37
> Está en el rango de 31 a 40
> ```
> Con las mismas 12 entradas del ejercicio 4 la salida es **idéntica**: los dos programas son equivalentes.

> [!note]- 🧠 Por qué funciona
> - `in 31..40` se traduce a `age >= 31 && age <= 40`: el rango ya incluye los dos límites, así que cada rama es independiente de las demás.
> - En el ejercicio 4 cada rama dependía de las anteriores (solo miraba el límite superior). Aquí, en cambio, cada rango se basta por sí mismo.

> [!tip] Ejercicio 4 vs. ejercicio 5
> | | `when` sin sujeto (ej. 4) | `when` con sujeto (ej. 5) |
> | --- | --- | --- |
> | Cabecera | `when {` | `when (age) {` |
> | Rama | condición completa: `age <= 20` | valor o rango: `in 11..20` |
> | ¿Importa el orden? | Sí, cada rama depende de las anteriores | No, si los rangos no se solapan |
> | Equivale en Java a | `if / else if` | `switch` (pero con rangos) |

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Lista variable de argumentos | `fun f(vararg n: Int)` | Acepta 0 o más argumentos; dentro es un `IntArray`. |
| Spread operator | `f(*array)` | Pasa los elementos de un array como argumentos sueltos. |
| Mostrar un array | `array.contentToString()` | `[1, 2, 3]` en vez de una dirección de memoria. |
| Función infija | `infix fun contains(n: Int)` | Se llama `obj contains 5`; método con un único parámetro. |
| Operador `in` | `operator fun contains(...)` | Permite `5 in obj`. |
| `when` sin sujeto | `when { cond -> … }` | Como `if / else if`; el orden importa. |
| `when` con sujeto | `when (x) { in a..b -> … }` | Compara `x` con valores o rangos, como un `switch`. |
| `when` como expresión | `val r = when { … else -> … }` | Devuelve un valor; necesita `else`. |
| Separador de miles | `20_000` | Mismo valor que `20000`, más legible. |

## Relaciones

- Teoría: [[03 - Funciones]] · [[04 - Estructuras básicas]] · [[06 - POO I]]
- Bloque anterior: [[Ejercicios Bloque 3]] · Bloque siguiente: [[Ejercicios Bloque 5]]
- Boletines con el mismo estilo: [[03.1 - Ejercicios 3 Funciones]] · [[04.1 - Ejercicios 4 Estructuras básicas]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Declarar un parámetro `vararg` y llamarlo con un array usando `*`
- [ ] Evitar la división entera convirtiendo a `Double`
- [ ] Crear una clase con un método `infix` y llamarlo en notación infija
- [ ] Anidar `when` para decidir por dos criterios
- [ ] Usar `when` sin sujeto como un `if / else if`
- [ ] Usar `when` con sujeto y rangos `in a..b`
- [ ] Saber cuándo importa el orden de las ramas y cuándo no
