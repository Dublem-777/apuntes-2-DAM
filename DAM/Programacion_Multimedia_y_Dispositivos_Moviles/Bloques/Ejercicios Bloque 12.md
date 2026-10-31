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
  - DAM/pmdm/kotlin-funcional
  - DAM/pmdm/ejercicios
---

# Bloque 12 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[08 - POO III]] · [[10 - Programación funcional]] · [[11 - Colecciones]]
> Bloque anterior: [[Ejercicios Bloque 11]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque12/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 8.1, 8.2 y 8.4 de [[08.1 - Ejercicios 8 POO III|el boletín 8]] y 10.1 y 10.4 de [[10.1 - Ejercicios 10 Programación funcional|el boletín 10]]. El código parte de esas soluciones.
> - Al enunciado copiado le faltaban algunas palabras («dos *funciones top-level*», «una *propiedad miembro* … usando el modificador *`lateinit`*», «*sin inicializar previamente* `configName`»). Se han recuperado de los enunciados del boletín.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque12/Ejercicio12.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas y los mensajes de error son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · *Top-level functions* y visibilidad `private`]]
- [[#Ejercicio 2 · *Top-level property* como contador de sesiones]]
- [[#Ejercicio 3 · Propiedad `lateinit` en `AppService`]]
- [[#Ejercicio 4 · Función de orden superior `testBoth`]]
- [[#Ejercicio 5 · `forEach`, `filter`, `map` y `sumOf` sobre un carrito]]

---

## Ejercicio 1 · *Top-level functions* y visibilidad `private`

> [!question] Enunciado
> Crea un fichero de Kotlin para contener dos *top-level functions* de utilidad:
>
> - Una función *top-level* **`private`** llamada `padString(s: String, length: Int)` que devuelve la cadena `s` rellenada con espacios al final hasta alcanzar la `length` especificada.
> - Una función *top-level* **`public`** (por defecto) llamada `formatTitle(title: String)` que utiliza `padString` internamente para rellenar la cadena a una longitud de 20 y luego devuelve la cadena en mayúsculas.
>
> En otro archivo, con la función `main`, haz lo siguiente:
>
> - Llama a `formatTitle("Project Name")` e imprime el resultado.
> - En un comentario, explica por qué la llamada a `padString("Short", 10)` generaría un error de compilación si se hiciera en este archivo.

### Clases y métodos introducidos
- ***Top-level function***: una función escrita directamente en el fichero, fuera de cualquier clase. En Java haría falta una clase de utilidades con métodos `static`; en Kotlin no.
- **`private` en el nivel superior**: la función solo existe **dentro de su fichero**. Desde otro fichero es como si no estuviera.
- **Visibilidad por defecto (`public`)**: si no se pone nada, la función se puede usar desde cualquier fichero.
- `String.padEnd(length, ' ')`: rellena la cadena por la derecha con el carácter indicado hasta la longitud pedida.
- `String.uppercase()`: devuelve la cadena en mayúsculas.

> **Términos explicados:** [[08 - POO III#1. Top-level functions|*top-level functions*]] · [[06 - POO I#15. Modificadores de visibilidad|modificadores de visibilidad]]

#### Ejemplo simple de funcionamiento
```kotlin
// En MathUtils.kt
private fun square(x: Int) = x * x         // solo visible en MathUtils.kt
fun sumOfSquares(a: Int, b: Int) = square(a) + square(b)

// En Main.kt
fun main() {
    println(sumOfSquares(3, 4))   // 25
    // println(square(3))         // ERROR: square es private en MathUtils.kt
}
```

### Código fuente (`Ejercicio12.1/src/StringUtils.kt` y `Ejercicio12.1/src/Main.kt`)

**StringUtils.kt**
```kotlin
// private: solo es visible dentro de este fichero (StringUtils.kt)
private fun padString(s: String, length: Int): String = s.padEnd(length, ' ')

// public (visibilidad por defecto): se puede usar desde cualquier fichero
fun formatTitle(title: String): String = padString(title, 20).uppercase()
```

**Main.kt**
```kotlin
fun main() {
    // Los corchetes permiten ver los espacios de relleno
    println("[${formatTitle("Project Name")}]")

    // padString("Short", 10)
    // ↑ Error de compilación: padString se declaró private en StringUtils.kt.
    //   Una top-level function private solo es visible dentro del fichero
    //   en el que se declara, así que desde Main.kt no existe.
}
```

### Explicación paso a paso
1. **`StringUtils.kt`** es el «fichero de utilidades». Tiene dos funciones sueltas, sin ninguna clase alrededor.
2. **`padString`** es `private`: solo la pueden llamar las funciones de `StringUtils.kt`. Usa `padEnd` para añadir espacios hasta la longitud pedida.
3. **`formatTitle`** es pública: rellena el título hasta 20 caracteres con `padString` y lo pasa a mayúsculas. Puede usar `padString` porque está **en el mismo fichero**.
4. **`Main.kt`** llama a `formatTitle` e imprime el resultado entre corchetes, para que se vean los espacios de relleno.
5. **El comentario** explica por qué `padString("Short", 10)` no se puede llamar desde `Main.kt`: es `private` en otro fichero.

> [!tip] Prueba
> ```text
> [PROJECT NAME        ]
> ```
> «Project Name» tiene 12 caracteres, así que se añaden 8 espacios hasta llegar a 20.
>
> Si se descomenta `padString("Short", 10)` en `Main.kt`, **no compila**. Error real de `kotlinc`: `cannot access 'fun padString(s: String, length: Int): String': it is private in file`.

> [!note]- 🧠 Por qué funciona
> - `private` en el nivel superior es como una nota en la nevera de tu casa: la ve todo el que está en casa (el fichero), pero nadie de fuera.
> - `formatTitle` hace de «intermediaria»: es pública y usa por dentro la función privada. Quien llama a `formatTitle` no necesita saber que existe `padString`. Así puedes cambiar `padString` cuando quieras sin romper nada fuera del fichero.
> - Para probarlo en IntelliJ, crea los dos archivos en la misma carpeta `src/`: ambos están en el mismo paquete, así que `Main.kt` ve `formatTitle` sin `import`.

---

## Ejercicio 2 · *Top-level property* como contador de sesiones

> [!question] Enunciado
> Define una propiedad *top-level* mutable llamada `sessionCount` de tipo `Int`, inicializada a 0. Define las siguientes dos funciones *top-level*:
>
> - Una función llamada `startNewSession` que incrementa el valor de `sessionCount`.
> - Una función llamada `getSessionReport` que devuelve una `String` que diga: `"Total sessions started: [Valor de sessionCount]"`.
>
> En la función `main`, simula el uso de la aplicación:
>
> - Llama a `startNewSession()` tres veces.
> - Llama a `getSessionReport()` e imprime el resultado.
> - Llama a `startNewSession()` una vez más.
> - Llama a `getSessionReport()` e imprime el resultado.

### Clases y métodos introducidos
- ***Top-level property***: una variable declarada fuera de cualquier clase y función. La pueden leer y modificar todas las funciones del fichero.
- Tiene que **inicializarse al declararla** (`= 0`): no hay constructor que pueda darle valor después.

> **Términos explicados:** [[08 - POO III#2. Top-level properties|*top-level properties*]]

#### Ejemplo simple de funcionamiento
```kotlin
var clicks = 0              // top-level property

fun click() {
    clicks++
}

fun main() {
    click(); click()
    println(clicks)         // 2
}
```

### Código fuente (`Ejercicio12.2/src/Main.kt`)

```kotlin
// Top-level property: está fuera de cualquier clase y debe inicializarse al declararla
var sessionCount: Int = 0

fun startNewSession() {
    sessionCount++
}

fun getSessionReport(): String = "Total sessions started: $sessionCount"

fun main() {
    startNewSession()
    startNewSession()
    startNewSession()
    println(getSessionReport())

    startNewSession()
    println(getSessionReport())
}
```

### Explicación paso a paso
1. **`sessionCount`** es `var` porque cambia, y empieza en 0.
2. **`startNewSession()`** suma 1 con `++`. No recibe el contador como parámetro: lo ve directamente porque está en el nivel superior del fichero.
3. **`getSessionReport()`** devuelve el texto con el valor actual, usando una plantilla de cadena.
4. **`main()`** sigue el guion del enunciado: tres sesiones e informe (3), una más e informe (4).

> [!tip] Prueba
> ```text
> Total sessions started: 3
> Total sessions started: 4
> ```

> [!note]- 🧠 Por qué funciona
> - `sessionCount` vive **todo el programa** y es una sola. Por eso las dos funciones trabajan sobre el mismo contador: lo que una suma, la otra lo ve.
> - Es la alternativa de Kotlin a un atributo `static` de Java. En el [[Ejercicios Bloque 8#Ejercicio 5 · `User` con id automático|Bloque 8]] se hizo algo parecido con un `companion object`, pero allí el contador pertenecía a la clase `User`; aquí pertenece al fichero.

> [!warning] Con cuidado
> Una variable global que cualquier función puede modificar es cómoda, pero es difícil seguir quién la ha cambiado. En programas grandes conviene marcarla `private` y dejar que solo la toquen funciones como `startNewSession()`.

---

## Ejercicio 3 · Propiedad `lateinit` en `AppService`

> [!question] Enunciado
> Define una clase simple llamada `AppService`. Dentro de `AppService`, define una propiedad miembro llamada `configName` de tipo `String` usando el modificador **`lateinit`**.
>
> Define una función pública llamada `initializeConfig(name: String)` que se encargue de asignar el valor al campo `configName`.
>
> Define una función pública llamada `runService` que imprima un mensaje usando el valor de `configName`.
>
> En la función `main`:
>
> - Crea una instancia inmutable de `AppService` llamada `service`.
> - Llama a `service.initializeConfig("Production_Env")`.
> - Llama a `service.runService()`.
> - Crea una nueva instancia inmutable de `AppService` llamada `faultyService`.
> - Utiliza un bloque `try-catch` para llamar inmediatamente a `faultyService.runService()` sin inicializar previamente `configName`.
> - En el bloque `catch`, captura la excepción `UninitializedPropertyAccessException` e imprime un mensaje que explique por qué falló.

### Clases y métodos introducidos
- `lateinit var`: una propiedad **no nullable** que no se inicializa al crear el objeto, sino **más tarde**. Es una promesa al compilador: «le daré valor antes de usarla».
- Restricciones (comprobadas con el compilador): tiene que ser `var` y no puede ser de un tipo primitivo (`Int`, `Double`, `Boolean`…).
- `UninitializedPropertyAccessException`: la excepción que se lanza si se lee la propiedad antes de darle valor, es decir, si se rompe la promesa.
- **Instancia inmutable**: la referencia se declara con `val`. El objeto puede cambiar por dentro, pero la variable siempre apunta al mismo objeto.

> **Términos explicados:** [[08 - POO III#4. lateinit|`lateinit`]] · [[04 - Estructuras básicas#Capturar excepciones|`try-catch`]]

#### Ejemplo simple de funcionamiento
```kotlin
class Player {
    lateinit var nickname: String
}

fun main() {
    val player = Player()
    player.nickname = "Dani"     // se inicializa después de crear el objeto
    println(player.nickname)     // Dani
}
```

### Código fuente (`Ejercicio12.3/src/Main.kt`)

```kotlin
class AppService {
    // Prometemos al compilador que se inicializará antes de leerla
    lateinit var configName: String

    fun initializeConfig(name: String) {
        configName = name
    }

    fun runService() {
        println("Servicio en marcha con la configuración: $configName")
    }
}

fun main() {
    val service = AppService()
    service.initializeConfig("Production_Env")
    service.runService()

    val faultyService = AppService()
    try {
        // configName nunca se ha inicializado en este objeto
        faultyService.runService()
    } catch (e: UninitializedPropertyAccessException) {
        println("Fallo: se leyó configName antes de llamar a initializeConfig()")
        println("Mensaje de la excepción: ${e.message}")
    }
}
```

### Explicación paso a paso
1. **`lateinit var configName: String`:** el objeto se crea sin valor en `configName`, pero sin hacerla `String?`. Así, después no hace falta usar `?.` ni `!!` cada vez que se lee.
2. **`initializeConfig()`:** cumple la promesa, asignando el valor.
3. **`service`:** se inicializa y después se usa, así que todo va bien.
4. **`faultyService`:** se llama a `runService()` sin inicializar. Al leer `configName` dentro del mensaje, Kotlin lanza `UninitializedPropertyAccessException`.
5. **`catch`:** captura justo esa excepción y explica qué ha pasado, además de mostrar el mensaje de la propia excepción.

> [!tip] Prueba
> ```text
> Servicio en marcha con la configuración: Production_Env
> Fallo: se leyó configName antes de llamar a initializeConfig()
> Mensaje de la excepción: lateinit property configName has not been initialized
> ```
> Errores reales de `kotlinc` si se incumplen las restricciones:
> - `lateinit var count: Int` → `'lateinit' modifier is not allowed on properties of primitive types`.
> - `lateinit val name: String` → `'lateinit' modifier is allowed only on mutable properties`.

> [!note]- 🧠 Por qué funciona
> - `lateinit` es como reservar mesa en un restaurante: la mesa existe desde que reservas, pero hasta que no llegas no hay nadie sentado. Si el camarero va a servir antes de que llegues (leer antes de inicializar), se encuentra la mesa vacía: eso es la excepción.
> - La diferencia con `String?` está en **cuándo** te enteras del problema. Con `String?`, el compilador te obliga a gestionar el `null` cada vez. Con `lateinit`, no te obliga a nada, pero si fallas te enteras en ejecución, con una excepción clara.
> - Tiene que ser `var` porque se asigna después de construir el objeto. Y no admite primitivos porque Kotlin usa «está vacío» (`null` por dentro) para saber si se ha inicializado, y un `Int` primitivo de la JVM no puede valer `null`.

---

## Ejercicio 4 · Función de orden superior `testBoth`

> [!question] Enunciado
> Define una función de orden superior llamada `testBoth` que reciba dos enteros y una función de condición como parámetros. `testBoth` debe devolver un valor booleano que indique si **ambos** números cumplen la condición especificada.
>
> Prueba la función llamándola dos veces desde `main` con dos condiciones distintas pasadas como lambdas.

### Clases y métodos introducidos
- **Función de orden superior**: una función que **recibe otra función** como parámetro (o la devuelve).
- **Tipo función** `(Int) -> Boolean`: «una función que recibe un `Int` y devuelve un `Boolean`».
- **Lambda** `{ it % 2 == 0 }`: una función sin nombre escrita en el momento. Si tiene un solo parámetro, se puede llamar `it`.
- ***Trailing lambda***: si el último parámetro es una función, la lambda se puede escribir **fuera** de los paréntesis: `testBoth(4, 10) { … }`.

> **Términos explicados:** [[10 - Programación funcional#1. Tipos función|tipos función]] · [[10 - Programación funcional#5. Expresiones lambda|lambdas, `it` y *trailing lambda*]]

#### Ejemplo simple de funcionamiento
```kotlin
fun applyTwice(x: Int, operation: (Int) -> Int): Int = operation(operation(x))

fun main() {
    println(applyTwice(3) { it * 2 })   // (3 * 2) * 2 = 12
}
```

### Código fuente (`Ejercicio12.4/src/Main.kt`)

```kotlin
// Función de orden superior: recibe una función (Int) -> Boolean como parámetro
fun testBoth(first: Int, second: Int, condition: (Int) -> Boolean): Boolean =
    condition(first) && condition(second)

fun main() {
    // Condición 1: ¿son pares? (lambda con it y trailing lambda)
    val bothEven = testBoth(4, 10) { it % 2 == 0 }
    println("¿4 y 10 son pares? $bothEven")

    // Condición 2: ¿son positivos? (lambda con nombre de parámetro)
    val bothPositive = testBoth(3, -5) { number -> number > 0 }
    println("¿3 y -5 son positivos? $bothPositive")
}
```

### Explicación paso a paso
1. **El parámetro función:** `condition: (Int) -> Boolean` acepta cualquier función que reciba un entero y devuelva un booleano.
2. **El cuerpo:** aplica `condition` a cada número y une los resultados con `&&`: solo es `true` si **los dos** la cumplen.
3. **Primera llamada:** la lambda `{ it % 2 == 0 }` comprueba si un número es par. 4 y 10 lo son → `true`.
4. **Segunda llamada:** `{ number -> number > 0 }` hace lo mismo que `{ it > 0 }`, pero poniendo nombre al parámetro, que a veces se lee mejor. -5 no es positivo → `false`.
5. **Sintaxis:** en las dos llamadas la lambda va fuera de los paréntesis (*trailing lambda*), porque `condition` es el último parámetro.

> [!tip] Prueba
> ```text
> ¿4 y 10 son pares? true
> ¿3 y -5 son positivos? false
> ```

> [!note]- 🧠 Por qué funciona
> - `testBoth` es como un control de calidad: siempre hace lo mismo («¿pasan los dos?»), pero la **prueba concreta** se la das tú cada vez. Así una sola función sirve para pares, positivos, múltiplos de 3…
> - Sin funciones de orden superior harían falta `bothEven()`, `bothPositive()`… repitiendo el `&&` en cada una.
> - `&&` es perezoso: si la condición falla con el primer número, ni siquiera se comprueba el segundo.

---

## Ejercicio 5 · `forEach`, `filter`, `map` y `sumOf` sobre un carrito

> [!question] Enunciado
> Define una *data class* llamada `OrderLine` con dos propiedades inmutables: `productName` (`String`) y `price` (`Double`). Define una lista inmutable de `OrderLine` llamada `shoppingCart` con al menos tres elementos.
>
> En la función `main`, usa `shoppingCart` y las funciones de colección de Kotlin (`forEach`, `filter`, `map`) para hacer lo siguiente con la sintaxis más concisa posible:
>
> 1. **Impresión simple (`forEach`):** imprime el `productName` de cada artículo. Debe usar `it` y la sintaxis de *trailing lambda*.
> 2. **Filtrado y mapeo (desestructuración):** usa `filter` para quedarte solo con los artículos cuyo precio sea mayor o igual a 50.0. Con ese resultado, aplica `map` para crear una lista de `String` con solo el `productName`. La lambda de `filter` debe usar la **desestructuración del parámetro** para acceder al precio directamente (ignorando el nombre). La lambda de `map` debe usar `it`.
> 3. **Cálculo (`it` y *trailing lambda*):** usa `sumOf` para calcular la suma total de todos los precios de `shoppingCart`. Debe usar `it` y la sintaxis de *trailing lambda*.
>
> Finalmente, imprime los resultados de los puntos 2 y 3 con mensajes claros.

### Clases y métodos introducidos
- `listOf(…)`: crea una lista **inmutable** (sin `add` ni `remove`).
- `forEach { … }`: ejecuta la lambda con cada elemento. No devuelve nada.
- `filter { … }`: devuelve una lista **nueva** con los elementos para los que la lambda da `true`.
- `map { … }`: devuelve una lista **nueva** con el resultado de aplicar la lambda a cada elemento.
- `sumOf { … }`: suma lo que devuelve la lambda para cada elemento.
- **Desestructuración en una lambda**: `{ (_, price) -> … }` abre cada `OrderLine` en sus componentes. `_` ignora el nombre y `price` recibe el precio.

> **Términos explicados:** [[10 - Programación funcional#5. Expresiones lambda|lambdas y desestructuración de parámetros]] · [[11 - Colecciones#7. Procesamiento funcional de listas|`filter`, `map` y compañía]] · [[07 - POO II#Desestructuración|desestructuración]]

#### Ejemplo simple de funcionamiento
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { it % 2 == 0 })   // [2, 4]
println(numbers.map { it * 10 })          // [10, 20, 30, 40]
println(numbers.sumOf { it })             // 10
```

### Código fuente (`Ejercicio12.5/src/Main.kt`)

```kotlin
data class OrderLine(val productName: String, val price: Double)

val shoppingCart = listOf(
    OrderLine("Teclado", 45.99),
    OrderLine("Monitor", 189.90),
    OrderLine("Ratón", 19.95),
    OrderLine("Auriculares", 59.00),
)

fun main() {
    // 1. forEach con it y trailing lambda
    println("Productos del carrito:")
    shoppingCart.forEach { println("- ${it.productName}") }

    // 2. filter con desestructuración (ignorando el nombre) y map con it
    val expensiveProducts = shoppingCart
        .filter { (_, price) -> price >= 50.0 }
        .map { it.productName }

    // 3. sumOf con it y trailing lambda
    val total = shoppingCart.sumOf { it.price }

    println("Productos de 50 € o más: $expensiveProducts")
    println("Total del carrito: ${"%.2f".format(total)} €")
    println("Total sin formatear: $total")
}
```

### Explicación paso a paso
1. **Datos:** `OrderLine` es una `data class` con dos `val`. `shoppingCart` es una lista inmutable de cuatro artículos, declarada como *top-level property*.
2. **`forEach`:** recorre la lista y, para cada artículo (`it`), imprime su nombre. Lleva *trailing lambda* y, como es el único argumento, ni siquiera paréntesis.
3. **`filter` + `map` encadenados:**
	- `filter { (_, price) -> price >= 50.0 }` se queda con Monitor (189.90) y Auriculares (59.00). La desestructuración funciona porque `OrderLine` es `data class` (tiene `component1()` y `component2()`).
	- `.map { it.productName }` convierte esa lista de `OrderLine` en una lista de `String` con los nombres.
4. **`sumOf { it.price }`:** suma los cuatro precios.
5. **Salida:** el total se muestra con 2 decimales y, para ver por qué hace falta, también sin formatear.

> [!tip] Prueba
> ```text
> Productos del carrito:
> - Teclado
> - Monitor
> - Ratón
> - Auriculares
> Productos de 50 € o más: [Monitor, Auriculares]
> Total del carrito: 314,84 €
> Total sin formatear: 314.84000000000003
> ```
> Igual que en el [[Ejercicios Bloque 9#Ejercicio 1 · `data class` `Product` y `copy()`|Bloque 9]], la suma de `Double` arrastra un error minúsculo de redondeo: por eso se formatea con `"%.2f"`.

> [!note]- 🧠 Por qué funciona
> - `filter` y `map` funcionan como una cadena de montaje: la lista pasa por un filtro (quita lo que no vale) y después por una máquina que transforma cada pieza (de `OrderLine` a nombre). Cada paso devuelve una lista **nueva**; `shoppingCart` no cambia.
> - Con un `for` clásico harían falta una lista auxiliar, un `if` y un `add`. Con `filter` y `map`, la intención («los nombres de los caros») se lee directamente.
> - En `filter` el parámetro va entre paréntesis, `(_, price)`. Sin paréntesis, `{ _, price -> … }` serían **dos parámetros**, y `filter` solo pasa uno: no compilaría.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| *Top-level function* | `fun f() { … }` en el fichero | Sin clase alrededor; sustituye a los `static` de Java. |
| `private` en el nivel superior | `private fun f()` | Solo visible en su fichero (`it is private in file`). |
| *Top-level property* | `var x = 0` en el fichero | Una sola para todo el programa; hay que inicializarla. |
| `lateinit` | `lateinit var x: String` | Se inicializa después; solo `var` y no primitivos. |
| Leer `lateinit` sin valor | — | `UninitializedPropertyAccessException`. |
| Tipo función | `(Int) -> Boolean` | Parámetro que recibe una función. |
| Lambda | `{ it > 0 }` / `{ n -> n > 0 }` | Función sin nombre; `it` si hay un solo parámetro. |
| *Trailing lambda* | `f(a, b) { … }` | La última lambda va fuera de los paréntesis. |
| Colecciones funcionales | `forEach`, `filter`, `map`, `sumOf` | Recorren, filtran, transforman y suman sin bucles explícitos. |
| Desestructurar en lambda | `{ (_, price) -> … }` | Abre el elemento en sus componentes. |

## Relaciones

- Teoría: [[08 - POO III]] · [[10 - Programación funcional]] · [[11 - Colecciones]]
- Bloque anterior: [[Ejercicios Bloque 11]] · Bloque siguiente: [[Ejercicios Bloque 13]]
- Mismos enunciados en los boletines: [[08.1 - Ejercicios 8 POO III#Ejercicio 8.1 · Top-level functions y visibilidad private|8.1]] · [[08.1 - Ejercicios 8 POO III#Ejercicio 8.2 · Top-level property como contador de sesiones|8.2]] · [[08.1 - Ejercicios 8 POO III#Ejercicio 8.4 · Propiedad lateinit y UninitializedPropertyAccessException|8.4]] · [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.1 · Función de orden superior testBoth con lambdas|10.1]] · [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.4 · Lambdas con it, trailing lambda y desestructuración|10.4]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar qué significa `private` en una función de nivel superior
- [ ] Usar una *top-level property* compartida por varias funciones
- [ ] Declarar una propiedad `lateinit` y saber qué excepción lanza si se lee antes de tiempo
- [ ] Explicar las dos restricciones de `lateinit`
- [ ] Escribir una función de orden superior con un parámetro `(Int) -> Boolean`
- [ ] Pasar lambdas con `it`, con nombre y como *trailing lambda*
- [ ] Encadenar `filter` y `map` y desestructurar el parámetro de una lambda
