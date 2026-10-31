---
asignatura: PMDM
tema: 3
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-funciones
  - DAM/pmdm/ejercicios
---

# Bloque 3 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[02 - Jerarquia de tipos]] · [[03 - Funciones]] · [[04 - Estructuras básicas]]
> Bloque anterior: [[Ejercicios Bloque 2]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque3/`

> [!note] Sobre las soluciones
> Soluciones didácticas desarrolladas para este bloque con conceptos explicados en los temas anteriores. Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque3/Ejercicio3.K/` (ver **Ruta fuente**). Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Media de 4 notas con un array]]
- [[#Ejercicio 2 · Variable `Any?` según un número aleatorio]]
- [[#Ejercicio 3 · Función `isPrime`]]
- [[#Ejercicio 4 · Función `isLeapYear` en una única expresión]]
- [[#Ejercicio 5 · Función `calculateCompoundInterest`]]
- [[#Ejercicio 6 · Llamada con argumentos con nombre]]

---

## Ejercicio 1 · Media de 4 notas con un array

> [!question] Enunciado
> Realiza un programa que solicite las notas de 4 exámenes, las almacene en un array y después recorra el array y obtenga y muestre por pantalla la media aritmética de las notas (ver tema *Estructuras básicas*).

### Clases y métodos introducidos
- `DoubleArray(4)`: crea un array de 4 `Double` rellenos con `0.0`. Es la versión para primitivos de `Array<Double>`, igual que `double[]` en Java (los apuntes recomiendan usar estas clases cuando el tipo es primitivo).
- `array.indices`: el rango de posiciones válidas, `0..3`. Se usa cuando necesitamos el **índice** para escribir en el array.
- `for (grade in grades)`: recorre directamente los **valores**, como el *for-each* de Java.
- `array.size`: número de elementos (en Java, `length`).

> **Términos explicados:** [[02 - Jerarquia de tipos#10. Arrays|arrays e `IntArray`/`DoubleArray`]] · [[04 - Estructuras básicas#6. Bucles `for` y `repeat`|bucle `for`]] · [[01 - Introduccion a Kotlin#6.1 readln() y compañía|`readln()` y conversiones]]

#### Ejemplo simple de funcionamiento
```kotlin
val numbers = intArrayOf(10, 20, 30)
for (i in numbers.indices) println("Posición $i → ${numbers[i]}")  // con índice
for (n in numbers) println(n)                                       // solo valores
println(numbers.size)                                               // 3
```

### Código fuente (`Ejercicio3.1/src/Main.kt`)

```kotlin
fun main() {
    // Array de 4 posiciones para las notas (DoubleArray porque son decimales)
    val grades = DoubleArray(4)

    // Rellenamos el array pidiendo cada nota por consola
    for (i in grades.indices) {
        print("Introduce la nota del examen ${i + 1}: ")
        grades[i] = readln().toDouble()
    }

    // Recorremos el array para sumar todas las notas
    var sum = 0.0
    for (grade in grades) {
        sum += grade
    }

    // Media = suma / número de notas
    val average = sum / grades.size
    println("La media de las notas es ${"%.2f".format(average)}")
}
```

### Explicación paso a paso
1. **Crear el array:** `DoubleArray(4)` reserva 4 huecos. `grades` es `val` porque la **referencia** al array no cambia, aunque sí cambie su contenido (como un `final` en Java).
2. **Rellenarlo:** recorremos `grades.indices` (0, 1, 2, 3) porque necesitamos la posición para escribir en `grades[i]`. Mostramos `i + 1` para que el usuario vea «examen 1» y no «examen 0».
3. **Sumar:** segundo recorrido, ahora con *for-each*, porque solo hacen falta los valores. `sum` es `var` y empieza en `0.0` (un `Double`; si pusiéramos `0`, sería `Int` y no podríamos sumarle decimales).
4. **Media:** `sum / grades.size`. Usar `size` en vez de un `4` fijo hace que el programa siga funcionando si cambias el tamaño del array.
5. **Salida:** `"%.2f".format(average)` deja 2 decimales, como en el Bloque 1.

> [!tip] Prueba
> ```text
> Introduce la nota del examen 1: 7.5
> Introduce la nota del examen 2: 6
> Introduce la nota del examen 3: 8.25
> Introduce la nota del examen 4: 9
> La media de las notas es 7,69
> ```
> (7.5 + 6 + 8.25 + 9) / 4 = 30.75 / 4 = 7.6875 → `7,69`.

> [!note]- 🧠 Por qué funciona
> - El enunciado pide **dos fases**: primero guardar y después recorrer. Por eso hay dos bucles y no se suma mientras se lee.
> - Como `grades` es un `DoubleArray`, `sum / grades.size` divide un `Double` entre un `Int`, y el resultado es `Double`: no se pierden los decimales.
> - Kotlin también tiene `grades.average()`, que hace lo mismo en una línea, pero el enunciado pide recorrer el array, así que el bucle es lo que se evalúa.

---

## Ejercicio 2 · Variable `Any?` según un número aleatorio

> [!question] Enunciado
> Crea un programa en Kotlin que declare una variable de tipo `Any?` que podrá contener un valor entero, una cadena de texto o `null`, dependiendo de un número aleatorio entre 0 y 100 generado con la función `Random.nextInt(lim_inf, lim_sup_no_incluido)` (comprueba que se importa el paquete `kotlin.random.Random` al principio del programa).
>
> - Si el número está en el rango **[0, 33]**, asigna `null` a la variable.
> - Si está en el rango **[34, 66]**, asigna el valor `5`.
> - Si está en el rango **[67, 100]**, asigna la cadena `"Baldomero"`.
>
> El programa deberá mostrar el número aleatorio generado y el tipo de contenido de la variable: `"La variable es nula"` si contiene `null`, `"La variable es un número entero"` si contiene un `Int` y `"La variable es una cadena de texto"` si contiene un `String`.

### Clases y métodos introducidos
- `import kotlin.random.Random`: el generador aleatorio propio de Kotlin (no confundir con `java.util.Random`, que se usó en [[04.1 - Ejercicios 4 Estructuras básicas|el boletín 4]]).
- `Random.nextInt(desde, hasta)`: entero aleatorio con `desde` **incluido** y `hasta` **excluido**. Para que pueda salir el 100, hay que pedir `nextInt(0, 101)`.
- `Any?`: la raíz de **todos** los tipos de Kotlin, admitiendo además `null`. Puede guardar un `Int`, un `String` o nada.
- `when` como **expresión**: devuelve un valor que se asigna directamente a la variable.
- `is`: comprueba el tipo real del contenido (como `instanceof` en Java, pero también vale para `Int`).

> **Términos explicados:** [[02 - Jerarquia de tipos#9. Los tipos Any y Any?|`Any` y `Any?`]] · [[02 - Jerarquia de tipos#11. Comprobación de tipo|operador `is`]] · [[04 - Estructuras básicas#4. `when` como expresión|`when` como expresión]] · [[02 - Jerarquia de tipos#4. Rangos y progresiones|rangos]]

#### Ejemplo simple de funcionamiento
```kotlin
import kotlin.random.Random

val dice = Random.nextInt(1, 7)          // 1..6 (el 7 no se incluye)
val anything: Any? = if (dice > 3) "alto" else 2
println(anything is String)              // true si salió 4, 5 o 6
```

### Código fuente (`Ejercicio3.2/src/Main.kt`)

```kotlin
import kotlin.random.Random

fun main() {
    // Número aleatorio entre 0 y 100 (el límite superior, 101, no se incluye)
    val randomNumber = Random.nextInt(0, 101)

    // Según el rango, la variable guarda null, un Int o un String
    val value: Any? = when (randomNumber) {
        in 0..33 -> null
        in 34..66 -> 5
        else -> "Baldomero"   // 67..100
    }

    println("Número aleatorio generado: $randomNumber")

    // Comprobamos qué tipo de contenido tiene la variable
    when (value) {
        null -> println("La variable es nula")
        is Int -> println("La variable es un número entero")
        is String -> println("La variable es una cadena de texto")
    }
}
```

### Explicación paso a paso
1. **Import:** la primera línea trae `kotlin.random.Random`. Es lo que el enunciado pide comprobar: IntelliJ la añade sola al escribir `Random` si eliges la opción de `kotlin.random`.
2. **Número aleatorio:** `Random.nextInt(0, 101)` da de 0 a 100, los dos incluidos, porque el segundo límite se excluye.
3. **Asignación con `when`:** el `when` es una expresión, así que su resultado va directo a `value`. Las ramas `in 0..33` y `in 34..66` usan rangos cerrados; lo que queda (67..100) cae en el `else`.
4. **Tipo `Any?`:** sin la anotación `: Any?`, Kotlin no sabría qué tipo dar a una variable que puede ser `null`, `Int` o `String`. `Any?` es el único tipo que admite las tres cosas.
5. **Comprobar el contenido:** segundo `when` con sujeto `value`. La rama `null` compara con `null`; `is Int` e `is String` miran el tipo real del objeto guardado.

> [!tip] Prueba (6 ejecuciones reales)
> ```text
> Número aleatorio generado: 8   → La variable es nula
> Número aleatorio generado: 89  → La variable es una cadena de texto
> Número aleatorio generado: 46  → La variable es un número entero
> Número aleatorio generado: 26  → La variable es nula
> Número aleatorio generado: 28  → La variable es nula
> Número aleatorio generado: 37  → La variable es un número entero
> ```
> Cada ejecución saca un número distinto: ejecútalo varias veces para ver los tres casos.

> [!note]- 🧠 Por qué funciona
> - El **tipo declarado** de `value` es `Any?`, pero el objeto que guarda dentro sigue siendo un `Int` o un `String`. `is` pregunta por ese objeto real, no por la etiqueta de la variable.
> - El orden importa: si `value` es `null`, la rama `null` lo atrapa antes de llegar a los `is`.
> - El segundo `when` es una **sentencia** (su resultado no se usa), así que Kotlin no obliga a poner `else` aunque `Any?` pueda tener otros tipos.

> [!warning] Trampa típica
> `Random.nextInt(0, 100)` **nunca** devuelve 100, porque el segundo límite está excluido. El enunciado dice «entre 0 y 100» y el último rango es [67, 100], así que hay que usar `101`.

---

## Ejercicio 3 · Función `isPrime`

> [!question] Enunciado
> Realiza un programa en el que se defina una función `isPrime` que reciba un número entero y retorne si es primo o no. La función `main()` deberá llamar a `isPrime` varias veces con valores diferentes para probarla (ver tema *Estructuras básicas* si lo necesitas).

### Clases y métodos introducidos
- `fun isPrime(number: Int): Boolean`: función de **nivel superior** (fuera de cualquier clase). En Kotlin no hace falta `static` ni una clase envolvente: se llama directamente desde `main()`.
- `return` anticipado: en cuanto sabemos la respuesta, salimos de la función.
- `%` (resto): `number % divisor == 0` significa que `divisor` divide a `number` exactamente.
- `intArrayOf(...)`: crea un `IntArray` con los valores de prueba.

> **Términos explicados:** [[03 - Funciones#1. Definición de funciones|definir funciones]] · [[04 - Estructuras básicas#7. Bucles `while`, `break` y `continue`|bucle `while`]] · [[02 - Jerarquia de tipos#10. Arrays|`intArrayOf`]]

#### Ejemplo simple de funcionamiento
```kotlin
fun isEven(number: Int): Boolean {
    return number % 2 == 0
}

fun main() {
    println(isEven(4))   // true
    println(isEven(7))   // false
}
```

### Código fuente (`Ejercicio3.3/src/Main.kt`)

```kotlin
// Devuelve true si number es primo
fun isPrime(number: Int): Boolean {
    // Los menores que 2 (negativos, 0 y 1) no son primos
    if (number < 2) return false

    // Basta con probar divisores hasta la raíz cuadrada del número
    var divisor = 2
    while (divisor * divisor <= number) {
        if (number % divisor == 0) return false   // tiene un divisor: no es primo
        divisor++
    }
    return true
}

fun main() {
    val testNumbers = intArrayOf(-7, 0, 1, 2, 3, 4, 9, 17, 25, 97, 100)
    for (number in testNumbers) {
        println("¿$number es primo? ${isPrime(number)}")
    }
}
```

### Explicación paso a paso
1. **Casos especiales:** un primo es un número mayor que 1 que solo se divide entre 1 y entre sí mismo. Por eso lo primero es descartar los menores que 2.
2. **Buscar divisores:** probamos `divisor = 2, 3, 4…`. Si alguno divide exactamente (`resto == 0`), el número **no** es primo y devolvemos `false` en ese momento.
3. **Hasta la raíz cuadrada:** la condición `divisor * divisor <= number` hace que se pare en √number. Para 97 solo se prueban del 2 al 9, en vez de 95 números.
4. **Si el bucle termina** sin encontrar divisores, el número es primo: `return true`.
5. **Pruebas:** `main()` recorre un array con casos variados (negativo, 0, 1, el primo par 2, cuadrados como 9 y 25, primos grandes…) e imprime el resultado de cada llamada.

> [!tip] Prueba
> ```text
> ¿-7 es primo? false
> ¿0 es primo? false
> ¿1 es primo? false
> ¿2 es primo? true
> ¿3 es primo? true
> ¿4 es primo? false
> ¿9 es primo? false
> ¿17 es primo? true
> ¿25 es primo? false
> ¿97 es primo? true
> ¿100 es primo? false
> ```

> [!note]- 🧠 Por qué funciona
> - Si `number = a × b` y los dos fueran mayores que √number, su producto superaría a `number`. Así que **al menos uno de los dos factores es ≤ √number**, y basta con buscar hasta ahí.
> - Usamos `divisor * divisor <= number` en vez de calcular la raíz porque así todo son enteros y no hay problemas de redondeo con decimales.
> - Los cuadrados de primos (9 = 3×3, 25 = 5×5) son el caso límite: el divisor es exactamente la raíz. Por eso la condición lleva `<=` y no `<`.

---

## Ejercicio 4 · Función `isLeapYear` en una única expresión

> [!question] Enunciado
> Realiza un programa en el que definas una función `isLeapYear` que reciba un año e indique si es bisiesto o no, calculándolo mediante **una única expresión**. Prueba la función con distintos valores.

### Clases y métodos introducidos
- **Función de expresión única**: `fun nombre(...): Tipo = expresión`. No lleva llaves ni `return`: el valor de la expresión es lo que devuelve la función.
- `&&` y `||`: «y» y «o» lógicos, con cortocircuito, igual que en Java.

> **Términos explicados:** [[03 - Funciones#5. Funciones cuyo cuerpo es una única expresión|funciones de una única expresión]] · [[02 - Jerarquia de tipos#5. Booleanos|booleanos y operadores lógicos]]

#### Ejemplo simple de funcionamiento
```kotlin
// Las dos funciones son equivalentes
fun double(x: Int): Int {
    return x * 2
}
fun doubleShort(x: Int): Int = x * 2
```

### Código fuente (`Ejercicio3.4/src/Main.kt`)

```kotlin
// Bisiesto: divisible entre 4 y no entre 100, o divisible entre 400
fun isLeapYear(year: Int): Boolean = (year % 4 == 0 && year % 100 != 0) || year % 400 == 0

fun main() {
    val testYears = intArrayOf(1900, 2000, 2023, 2024, 2026, 2100, 2400)
    for (year in testYears) {
        println("¿$year es bisiesto? ${isLeapYear(year)}")
    }
}
```

### Explicación paso a paso
1. **La regla del calendario:** un año es bisiesto si es divisible entre 4, **salvo** los que terminan en 00, que solo lo son si además son divisibles entre 400.
2. **Traducida a código:** `(divisible entre 4 Y NO entre 100) O divisible entre 400`.
3. **Una única expresión:** toda la condición devuelve un `Boolean`, así que la función se escribe con `=` en una sola línea, sin `if` ni `return`.
4. **Pruebas:** elegimos años de cada caso: normales (2023, 2026), bisiestos normales (2024), siglos no bisiestos (1900, 2100) y siglos bisiestos (2000, 2400).

> [!tip] Prueba
> ```text
> ¿1900 es bisiesto? false
> ¿2000 es bisiesto? true
> ¿2023 es bisiesto? false
> ¿2024 es bisiesto? true
> ¿2026 es bisiesto? false
> ¿2100 es bisiesto? false
> ¿2400 es bisiesto? true
> ```

> [!note]- 🧠 Por qué funciona
> - 2024: `2024 % 4 == 0` ✅ y `2024 % 100 != 0` ✅ → la primera parte es `true`.
> - 1900: divisible entre 4 pero también entre 100 → la primera parte es `false`; `1900 % 400` es 300 → `false`. No es bisiesto.
> - 2000: la primera parte es `false` (es divisible entre 100), pero `2000 % 400 == 0` → `true`.
> - Los paréntesis no son obligatorios (`&&` tiene más prioridad que `||`), pero dejan clara la regla y evitan errores al leerla.

---

## Ejercicio 5 · Función `calculateCompoundInterest`

> [!question] Enunciado
> Escribe una función en Kotlin llamada `calculateCompoundInterest` que retorne el monto acumulado de una inversión con interés compuesto. La fórmula es:
>
> $$A = P \cdot \left(1 + \frac{r}{n}\right)^{n \cdot t}$$
>
> donde:
> - `A` es el monto acumulado después del tiempo `t`.
> - `P` es el capital inicial.
> - `r` es la tasa de interés anual (en decimal).
> - `n` es el número de veces que se capitaliza el interés por año. **Por defecto 4** (capitalización trimestral).
> - `t` es el número de años. **Por defecto 1**.

### Clases y métodos introducidos
- **Argumentos por defecto**: `timesPerYear: Int = 4`. Si quien llama no pasa ese argumento, se usa el 4. Sustituye a la sobrecarga de métodos que haría falta en Java.
- `Double.pow(n)`: potencia, de `kotlin.math`. Hay que importarlo con `import kotlin.math.pow`. En Kotlin `^` **no** es la potencia.
- **Trailing comma**: la coma después del último parámetro es válida y facilita añadir parámetros nuevos.

> **Términos explicados:** [[03 - Funciones#7. Argumentos por defecto|argumentos por defecto]] · [[03 - Funciones#5. Funciones cuyo cuerpo es una única expresión|función de una única expresión]] · [[03 - Funciones#2. Trailing comma|trailing comma]]

#### Ejemplo simple de funcionamiento
```kotlin
import kotlin.math.pow

fun greet(name: String, greeting: String = "Hola") = "$greeting, $name"

fun main() {
    println(greet("Daniel"))              // Hola, Daniel
    println(greet("Daniel", "Buenas"))    // Buenas, Daniel
    println(2.0.pow(3))                   // 8.0
}
```

### Código fuente (`Ejercicio3.5/src/Main.kt`)

```kotlin
import kotlin.math.pow

// A = P * (1 + r / n)^(n * t)
// timesPerYear (n) vale 4 por defecto y years (t) vale 1 por defecto
fun calculateCompoundInterest(
    principal: Double,
    rate: Double,
    timesPerYear: Int = 4,
    years: Int = 1,
): Double = principal * (1 + rate / timesPerYear).pow(timesPerYear * years)

fun main() {
    // Solo los obligatorios: trimestral (n = 4) durante 1 año
    val oneYear = calculateCompoundInterest(1000.0, 0.05)
    println("1000 € al 5 % durante 1 año: ${"%.2f".format(oneYear)} €")

    // Cambiando también los años: trimestral durante 10 años
    val tenYears = calculateCompoundInterest(1000.0, 0.05, 4, 10)
    println("1000 € al 5 % durante 10 años: ${"%.2f".format(tenYears)} €")
}
```

### Explicación paso a paso
1. **Nombres de los parámetros:** en inglés y descriptivos (`principal` = P, `rate` = r, `timesPerYear` = n, `years` = t) en vez de letras sueltas, siguiendo el estilo del curso.
2. **Obligatorios primero:** `principal` y `rate` no tienen valor por defecto; `timesPerYear` y `years` sí (4 y 1, como dice el enunciado).
3. **La fórmula:** `rate / timesPerYear` divide un `Double` entre un `Int` y da `Double`. Le sumamos 1 y lo elevamos con `.pow(timesPerYear * years)`.
4. **Expresión única:** la función solo calcula un valor, así que se escribe con `=`.
5. **Pruebas:** la primera llamada solo pasa los obligatorios (usa n = 4 y t = 1); la segunda los pasa todos.

> [!tip] Prueba
> ```text
> 1000 € al 5 % durante 1 año: 1050,95 €
> 1000 € al 5 % durante 10 años: 1643,62 €
> ```
> Comprobación a mano del primer caso: 1000 · (1 + 0.05/4)⁴ = 1000 · 1.0125⁴ ≈ 1050.95.

> [!note]- 🧠 Por qué funciona
> - Al llamar `calculateCompoundInterest(1000.0, 0.05)`, Kotlin asigna los argumentos **por posición** (`principal`, `rate`) y rellena los que faltan con sus valores por defecto.
> - Los parámetros con valor por defecto se ponen **al final** para poder omitirlos sin tener que nombrar nada.
> - Existe `pow(Int)` además de `pow(Double)`, así que `timesPerYear * years` (un `Int`) se puede pasar directamente.

> [!warning] `^` no es potencia
> En Kotlin (y en Java) `^` no eleva a una potencia: en Java es el XOR de bits, y en Kotlin ni siquiera es un operador (el XOR se escribe `xor`). Para potencias se usa siempre `pow()`.

---

## Ejercicio 6 · Llamada con argumentos con nombre

> [!question] Enunciado
> Realiza un programa que llame a la función `calculateCompoundInterest` del ejercicio anterior, de manera que **como primer argumento** se pase explícitamente el número de veces que se capitaliza al año y después el resto de parámetros obligatorios.

### Clases y métodos introducidos
- **Argumentos con nombre**: `nombreParametro = valor`. Permiten pasar los argumentos **en cualquier orden**, porque Kotlin los asigna por nombre y no por posición.
- Regla de mezcla: se pueden combinar argumentos con nombre y por posición **solo si respetan el orden** de los parámetros. Si un argumento con nombre va fuera de su sitio, el resto también tiene que llevar nombre.

> **Términos explicados:** [[03 - Funciones#8. Argumentos con nombre|argumentos con nombre]] · [[03 - Funciones#7. Argumentos por defecto|argumentos por defecto]]

#### Ejemplo simple de funcionamiento
```kotlin
fun describe(name: String, age: Int) = "$name tiene $age años"

fun main() {
    println(describe(age = 20, name = "Daniel"))   // Daniel tiene 20 años
}
```

### Código fuente (`Ejercicio3.6/src/Main.kt`)

```kotlin
import kotlin.math.pow

// Misma función que en el ejercicio 5
fun calculateCompoundInterest(
    principal: Double,
    rate: Double,
    timesPerYear: Int = 4,
    years: Int = 1,
): Double = principal * (1 + rate / timesPerYear).pow(timesPerYear * years)

fun main() {
    // timesPerYear va primero, así que todos los argumentos llevan nombre
    val monthly = calculateCompoundInterest(timesPerYear = 12, principal = 1000.0, rate = 0.05)
    println("1000 € al 5 % con capitalización mensual (1 año): ${"%.2f".format(monthly)} €")
}
```

### Explicación paso a paso
1. **La función** es la misma del ejercicio 5. Se copia porque cada ejercicio es un proyecto/archivo independiente.
2. **Primer argumento:** `timesPerYear = 12` (capitalización mensual). Va con nombre porque en la definición es el **tercer** parámetro, no el primero.
3. **Resto de obligatorios:** `principal = 1000.0` y `rate = 0.05`, también con nombre (ver el aviso de abajo).
4. **`years`** no se pasa, así que vale 1 por defecto.

> [!tip] Prueba
> ```text
> 1000 € al 5 % con capitalización mensual (1 año): 1051,16 €
> ```
> Sale un poco más que la trimestral del ejercicio 5 (1050,95 €): cuantas más veces se capitaliza, antes empiezan los intereses a generar más intereses.

> [!warning] No se puede mezclar aquí
> Puede parecer que basta con nombrar solo el primero: `calculateCompoundInterest(timesPerYear = 12, 1000.0, 0.05)`. **No compila.** Error real de `kotlinc`:
> ```text
> error: mixing named and positional arguments is not allowed unless the order
> of the arguments matches the order of the parameters.
> ```
> Como `timesPerYear` está fuera de su posición, los argumentos que vienen detrás ya no pueden ir por posición: hay que nombrarlos todos.

> [!note]- 🧠 Por qué funciona
> - Con argumentos con nombre, el compilador empareja cada valor con su parámetro **por nombre**: el orden en la llamada deja de importar.
> - Los parámetros con valor por defecto (`years`) se pueden saltar aunque se usen nombres.
> - Ventaja extra: la llamada se lee sola. `timesPerYear = 12` dice mucho más que un `12` suelto entre otros números.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Array de primitivos | `DoubleArray(4)` / `intArrayOf(...)` | Tamaño fijo; versión eficiente de `Array<Double>` / `Array<Int>`. |
| Recorrer un array | `for (i in a.indices)` / `for (x in a)` | Con índice (para escribir) o por valores (para leer). |
| Aleatorio | `Random.nextInt(desde, hasta)` | `desde` incluido, `hasta` **excluido**; paquete `kotlin.random`. |
| Tipo universal | `Any?` | Admite cualquier valor, incluido `null`. |
| Comprobar tipo | `is Int` / `is String` | Mira el tipo real del objeto guardado. |
| `when` como expresión | `val x = when (n) { in r -> … else -> … }` | Devuelve el valor de la rama elegida. |
| Primo | `divisor * divisor <= n` | Basta con buscar divisores hasta √n. |
| Función de expresión | `fun f(x: Int) = …` | Sin llaves ni `return`. |
| Bisiesto | `(y % 4 == 0 && y % 100 != 0) \|\| y % 400 == 0` | Siglos solo si son divisibles entre 400. |
| Argumento por defecto | `n: Int = 4` | Se puede omitir al llamar. |
| Potencia | `base.pow(exp)` | `import kotlin.math.pow`; `^` no es potencia. |
| Argumento con nombre | `f(n = 12, p = 1000.0)` | Cualquier orden; si uno va fuera de su sitio, todos con nombre. |

## Relaciones

- Teoría: [[02 - Jerarquia de tipos]] · [[03 - Funciones]] · [[04 - Estructuras básicas]]
- Bloque anterior: [[Ejercicios Bloque 2]] · Bloque siguiente: [[Ejercicios Bloque 4]]
- Boletines con el mismo estilo: [[03.1 - Ejercicios 3 Funciones]] · [[04.1 - Ejercicios 4 Estructuras básicas]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Crear un `DoubleArray`, rellenarlo por índice y recorrerlo por valores
- [ ] Generar un aleatorio con `Random.nextInt` incluyendo el límite superior
- [ ] Usar `Any?` y distinguir su contenido con `when` + `is`
- [ ] Comprobar si un número es primo buscando divisores hasta √n
- [ ] Escribir una función de una única expresión
- [ ] Definir argumentos por defecto y llamar con argumentos con nombre
- [ ] Saber cuándo se pueden mezclar argumentos con nombre y por posición
