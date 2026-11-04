---
asignatura: PMDM
tema: 11
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-colecciones
  - DAM/pmdm/ejercicios
---

# Bloque 15 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[11 - Colecciones]] · [[10 - Programación funcional]]
> Bloque anterior: [[Ejercicios Bloque 14]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque15/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 11.1–11.6 de [[11.1 - Ejercicios 11 Colecciones|el boletín 11]]. El código parte de esas soluciones, con algunas pruebas más.
> - El enunciado copiado numeraba dos ejercicios como «3» (el de `Employee` es el **5**); aquí van numerados del 1 al 6.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque15/Ejercicio15.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Crear colecciones]]
- [[#Ejercicio 2 · Convertir entre colecciones]]
- [[#Ejercicio 3 · Operador corchete y operadores `+` y `-`]]
- [[#Ejercicio 4 · Métodos de listas con `testScores`]]
- [[#Ejercicio 5 · Procesamiento funcional de empleados]]
- [[#Ejercicio 6 · Secuencia infinita de usuarios premium]]

---

## Ejercicio 1 · Crear colecciones

> [!question] Enunciado
> - Define un `listOf` llamado `productNames` con al menos cinco nombres de productos (`String`).
> - Define un `setOf` llamado `uniqueCategories` con al menos tres categorías (`String`). Repite una categoría para comprobar que el `Set` elimina los duplicados.
> - Define un `mapOf` llamado `priceMap` cuyas claves sean los nombres de los productos (de `productNames`) y cuyos valores sean sus precios (`Double`).
> - Crea un `mutableListOf` llamado `shoppingList` a partir de los dos primeros elementos de `productNames`.
> - Crea un `mutableMapOf` llamado `stockLevels` con los pares `("ProductA" to 10)` y `("ProductB" to 5)`.
> - Usa la función `List()` con una lambda para crear una `List<Int>` de tamaño 5 llamada `inventoryIds`. La lambda debe asignar a cada elemento su índice más 100 (100, 101, 102…).
>
> En la función `main`:
> - Imprime el tamaño de `uniqueCategories` para confirmar que se han eliminado los duplicados.
> - Añade un nuevo producto (`"ProductC"`) a `shoppingList`.
> - Actualiza el stock de `"ProductA"` en `stockLevels` a 15.
> - Imprime `inventoryIds` y `stockLevels` después de las modificaciones.

### Clases y métodos introducidos
- **Solo lectura**: `listOf`, `setOf`, `mapOf`. No tienen `add`, `remove` ni `put`.
- **Mutables**: `mutableListOf`, `mutableMapOf`. Sí se pueden modificar.
- `Set`: colección **sin repetidos**. Si añades un elemento que ya está, lo ignora.
- `Map`: pares **clave → valor**. Se crean con `clave to valor`.
- `List(5) { it + 100 }`: crea una lista de 5 elementos calculando cada uno a partir de su índice (`it`).
- `map[clave] = valor`: añade o actualiza el valor de una clave.

> **Términos explicados:** [[11 - Colecciones#2. Interfaces de colecciones|tipos de colecciones]] · [[11 - Colecciones#3. Creación de colecciones|crear colecciones]] · [[11 - Colecciones#5. Operadores sobrecargados en colecciones|operador `[]`]]

#### Ejemplo simple de funcionamiento
```kotlin
val colors = setOf("rojo", "azul", "rojo")
println(colors)                    // [rojo, azul]
val squares = List(4) { it * it }
println(squares)                   // [0, 1, 4, 9]
val ages = mapOf("Ana" to 20, "Luis" to 31)
println(ages["Ana"])               // 20
```

### Código fuente (`Ejercicio15.1/src/Main.kt`)

```kotlin
// Colecciones de solo lectura
val productNames = listOf("ProductA", "ProductB", "ProductC", "ProductD", "ProductE")
val uniqueCategories = setOf("Electrónica", "Hogar", "Electrónica", "Deporte")   // "Electrónica" repetida
val priceMap = mapOf(
    "ProductA" to 19.99,
    "ProductB" to 5.50,
    "ProductC" to 120.0,
    "ProductD" to 45.25,
    "ProductE" to 8.75,
)

// Colecciones mutables
val shoppingList = mutableListOf(productNames[0], productNames[1])
val stockLevels = mutableMapOf("ProductA" to 10, "ProductB" to 5)

// List(tamaño) { índice -> valor }
val inventoryIds = List(5) { it + 100 }

fun main() {
    // El Set descarta el duplicado: 3 categorías, no 4
    println("uniqueCategories: $uniqueCategories (tamaño ${uniqueCategories.size})")

    shoppingList.add("ProductC")
    stockLevels["ProductA"] = 15

    println("shoppingList: $shoppingList")
    println("priceMap: $priceMap")
    println("inventoryIds: $inventoryIds")
    println("stockLevels: $stockLevels")
}
```

### Explicación paso a paso
1. **Solo lectura:** `productNames`, `uniqueCategories` y `priceMap` no se van a modificar. `uniqueCategories` recibe 4 valores, uno repetido.
2. **Mutables:** `shoppingList` se crea con los dos primeros nombres (`productNames[0]` y `[1]`) y `stockLevels` con sus dos pares.
3. **`List(5) { it + 100 }`:** para cada índice del 0 al 4 calcula `índice + 100`.
4. **`main()`:** comprueba el tamaño del `Set` (3, no 4), añade `"ProductC"`, cambia el stock con `stockLevels["ProductA"] = 15` e imprime el resultado.

> [!tip] Prueba
> ```text
> uniqueCategories: [Electrónica, Hogar, Deporte] (tamaño 3)
> shoppingList: [ProductA, ProductB, ProductC]
> priceMap: {ProductA=19.99, ProductB=5.5, ProductC=120.0, ProductD=45.25, ProductE=8.75}
> inventoryIds: [100, 101, 102, 103, 104]
> stockLevels: {ProductA=15, ProductB=5}
> ```

> [!note]- 🧠 Por qué funciona
> - Un `Set` es como la lista de invitados de una fiesta: apuntar dos veces a la misma persona no hace que venga dos veces.
> - `shoppingList` es `val` y aun así se le puede hacer `add`. `val` impide **cambiar de lista** (reasignar la variable), pero no impide modificar el contenido de una lista mutable.
> - `stockLevels["ProductA"] = 15` **sustituye** el 10, porque en un mapa cada clave aparece una sola vez.

---

## Ejercicio 2 · Convertir entre colecciones

> [!question] Enunciado
> - Define un `listOf` llamado `rawNames` con estos nombres (con duplicados y variaciones de mayúsculas): `"Alice"`, `"bob"`, `"Alice"`, `"charlie"`, `"Bob"`.
> - Aplica la función `map` a `rawNames` para convertir todos los nombres a minúsculas.
> - Aplica `toSet()` al resultado para obtener un conjunto de nombres únicos en minúsculas. Guárdalo en una variable inmutable llamada `normalizedNames` e imprímelo.
> - Aplica `toMutableList()` a `normalizedNames` para obtener una lista que se pueda modificar. Guárdala en una variable mutable llamada `editableList`.
> - Añade un nuevo nombre (`"david"`) a `editableList` e imprímela.

### Clases y métodos introducidos
- `map { it.lowercase() }`: crea una lista **nueva** con cada nombre en minúsculas.
- `toSet()`: crea un `Set` a partir de la lista, eliminando los repetidos.
- `toMutableList()`: crea una lista **nueva y modificable** con los mismos elementos.

> **Términos explicados:** [[11 - Colecciones#4. Obtener una colección a partir de otra|obtener una colección a partir de otra]] · [[11 - Colecciones#7. Procesamiento funcional de listas|`map`]]

#### Ejemplo simple de funcionamiento
```kotlin
val letters = listOf("A", "b", "a")
println(letters.map { it.lowercase() }.toSet())   // [a, b]
```

### Código fuente (`Ejercicio15.2/src/Main.kt`)

```kotlin
fun main() {
    val rawNames = listOf("Alice", "bob", "Alice", "charlie", "Bob")

    // map crea una lista en minúsculas; toSet elimina los repetidos
    val normalizedNames = rawNames.map { it.lowercase() }.toSet()
    println("normalizedNames: $normalizedNames")

    // toMutableList crea una lista NUEVA que sí se puede modificar
    var editableList = normalizedNames.toMutableList()
    editableList.add("david")
    println("editableList: $editableList")
}
```

### Explicación paso a paso
1. **`map`:** `["Alice", "bob", "Alice", "charlie", "Bob"]` → `["alice", "bob", "alice", "charlie", "bob"]`. Ahora los repetidos son **idénticos**.
2. **`toSet()`:** elimina los repetidos → `[alice, bob, charlie]`. Por eso hay que pasar a minúsculas **antes**: `"Bob"` y `"bob"` son cadenas distintas y el `Set` se quedaría con las dos.
3. **`toMutableList()`:** como un `Set` de solo lectura no admite `add`, se crea una lista mutable con su contenido.
4. **`add("david")`:** se añade al final y se imprime.

> [!tip] Prueba
> ```text
> normalizedNames: [alice, bob, charlie]
> editableList: [alice, bob, charlie, david]
> ```

> [!note]- 🧠 Por qué funciona
> - Cada función (`map`, `toSet`, `toMutableList`) devuelve una colección **nueva**: `rawNames` sigue teniendo sus 5 nombres originales. Es como pasar un texto a limpio: el borrador no cambia.
> - El orden se conserva: `toSet()` mantiene el orden de la primera aparición de cada elemento.

> [!tip] «Variable mutable» frente a «lista mutable»
> El enunciado pide una **variable mutable**, así que `editableList` se declara con `var` (el boletín usa `val`). Son dos cosas distintas:
> - `var` → la **variable** puede apuntar a otra lista más adelante.
> - `MutableList` → la **lista** puede cambiar su contenido (`add`, `remove`…).
>
> Para hacer `add` basta con que la lista sea mutable; con `val` también funcionaría.

---

## Ejercicio 3 · Operador corchete y operadores `+` y `-`

> [!question] Enunciado
> Define las siguientes estructuras:
> - Una lista mutable llamada `inventory` con: `"Laptop"`, `"Monitor"`, `"Mouse"`.
> - Un mapa mutable llamado `prices` con: `"Laptop" to 1200.0`, `"Monitor" to 300.0`.
> - Una variable (`var`) que contenga una lista **inmutable** llamada `ordersToday`, con: `"Laptop"`, `"Monitor"`.
>
> Usando el **operador corchete**:
> - **Lectura:** imprime el precio del `"Laptop"` desde el mapa `prices`.
> - **Escritura:** cambia el elemento del índice 2 de `inventory` de `"Mouse"` a `"Keyboard"`.
> - **Nueva clave/valor:** añade al mapa `prices` el producto `"Keyboard"` con un precio de 50.0.
>
> Después:
> - **Creación inmutable (`+`):** crea una nueva lista `newOrder` resultado de añadir `"Keyboard"` a `ordersToday`. Imprime `newOrder`.
> - **Reasignación mutable (`+=`):** usa `+=` para añadir `"Charger"` a la variable `ordersToday`.
> - **Resta y reasignación (`-=`):** usa `-=` para eliminar `"Monitor"` de la variable `ordersToday`.
> - Imprime el estado final de `ordersToday` e `inventory`.

### Clases y métodos introducidos
- **Operador `[]`**: es sobrecarga de operadores, como en el [[Ejercicios Bloque 13#Ejercicio 1 · Sobrecarga del operador `+` en `ComplexNumber`|Bloque 13]].
	- `prices["Laptop"]` → `prices.get("Laptop")`.
	- `inventory[2] = "Keyboard"` → `inventory.set(2, "Keyboard")`.
	- `prices["Keyboard"] = 50.0` → `prices.put("Keyboard", 50.0)`.
- **`lista + elemento`**: devuelve una lista **nueva** con el elemento añadido. La original no cambia.
- **`lista - elemento`**: lista nueva sin ese elemento.
- **`+=` / `-=` con `var` y lista de solo lectura**: se traducen a `ordersToday = ordersToday + "Charger"`, es decir, se crea una lista nueva y la variable pasa a apuntar a ella.

> **Términos explicados:** [[11 - Colecciones#5. Operadores sobrecargados en colecciones|operadores en colecciones]] · [[08 - POO III#7. Sobrecarga de operadores|sobrecarga de operadores]]

#### Ejemplo simple de funcionamiento
```kotlin
var fruits = listOf("manzana")
val more = fruits + "pera"     // [manzana, pera]; fruits sigue igual
fruits += "kiwi"               // fruits = fruits + "kiwi" → [manzana, kiwi]
```

### Código fuente (`Ejercicio15.3/src/Main.kt`)

```kotlin
fun main() {
    val inventory = mutableListOf("Laptop", "Monitor", "Mouse")
    val prices = mutableMapOf("Laptop" to 1200.0, "Monitor" to 300.0)
    var ordersToday = listOf("Laptop", "Monitor")     // var + lista de solo lectura

    // Operador corchete
    println("Precio del Laptop: ${prices["Laptop"]}")  // lectura: prices.get("Laptop")
    inventory[2] = "Keyboard"                          // escritura: inventory.set(2, "Keyboard")
    prices["Keyboard"] = 50.0                          // nueva clave: prices.put("Keyboard", 50.0)

    // Operadores + y -
    val newOrder = ordersToday + "Keyboard"            // lista nueva; ordersToday no cambia
    println("newOrder: $newOrder")

    ordersToday += "Charger"                           // ordersToday = ordersToday + "Charger"
    ordersToday -= "Monitor"                           // ordersToday = ordersToday - "Monitor"

    println("ordersToday: $ordersToday")
    println("inventory: $inventory")
    println("prices: $prices")
}
```

### Explicación paso a paso
1. **Corchete en un mapa:** `prices["Laptop"]` lee el precio. `prices["Keyboard"] = 50.0` añade una clave nueva (si ya existiera, cambiaría su valor).
2. **Corchete en una lista:** `inventory[2] = "Keyboard"` sustituye el elemento de la posición 2. La lista tiene que ser mutable.
3. **`+`:** `newOrder` es una lista nueva de 3 elementos; `ordersToday` sigue teniendo 2.
4. **`+=` y `-=`:** `ordersToday` es una lista de **solo lectura**, así que no puede cambiar por dentro. Lo que cambia es la **variable**: cada operación crea una lista nueva y `ordersToday` pasa a apuntar a ella. Por eso tiene que ser `var`.
5. **Estado final:** `ordersToday` = `[Laptop, Charger]` (se añadió Charger y se quitó Monitor).

> [!tip] Prueba
> ```text
> Precio del Laptop: 1200.0
> newOrder: [Laptop, Monitor, Keyboard]
> ordersToday: [Laptop, Charger]
> inventory: [Laptop, Monitor, Keyboard]
> prices: {Laptop=1200.0, Monitor=300.0, Keyboard=50.0}
> ```

> [!note]- 🧠 Por qué funciona
> - Con una lista de solo lectura, `+=` es como cambiar de cuaderno: copias lo que tenías, añades la línea nueva y tiras el viejo. Con una lista mutable, en cambio, se escribiría la línea en el mismo cuaderno.
> - Si `ordersToday` fuera `val`, `ordersToday += "Charger"` no compilaría: no se puede reasignar un `val`, y una lista de solo lectura no tiene `add`.
> - `prices["Laptop"]` devuelve un `Double?`: si la clave no existiera, daría `null` en vez de lanzar una excepción.

---

## Ejercicio 4 · Métodos de listas con `testScores`

> [!question] Enunciado
> Define un `listOf<Int>` llamado `testScores` con al menos seis puntuaciones (por ejemplo, 85, 92, 78, 95, 88, 70). Después:
>
> 1. Imprime el número total de puntuaciones.
> 2. Imprime el índice de la última puntuación.
> 3. Encuentra la posición del 95 e imprímela.
> 4. Intenta obtener el elemento del índice 10 e imprime el resultado.
> 5. Obtén el elemento del índice 10 de forma que, si el índice no existe, una lambda devuelva el valor 50 (la puntuación de «suspenso»). Imprime el resultado.
> 6. Comprueba si la puntuación 78 está en la lista e imprime el booleano.
> 7. Obtén una lista nueva de solo tres puntuaciones barajadas al azar. Imprímela.
> 8. Crea una lista con todas las puntuaciones excepto la última.
> 9. Obtén una cadena con los valores en el formato `[85 | 92 | ...]` e imprímela.

### Clases y métodos introducidos

| Tarea | Método | Resultado |
| --- | --- | --- |
| Número de elementos | `size` | `Int` |
| Índice del último | `lastIndex` | `size - 1` |
| Posición de un valor | `indexOf(95)` | índice o `-1` si no está |
| Índice que puede no existir | `getOrNull(10)` | el elemento o `null` |
| Índice con valor por defecto | `getOrElse(10) { 50 }` | el elemento o lo que devuelva la lambda |
| ¿Contiene? | `78 in lista` | `Boolean` (llama a `contains`) |
| Barajar y coger 3 | `shuffled().take(3)` | lista nueva |
| Todos menos el último | `dropLast(1)` | lista nueva |
| Unir con formato | `joinToString(separator, prefix, postfix)` | `String` |

> **Términos explicados:** [[11 - Colecciones#6. Métodos y propiedades de listas|métodos y propiedades de listas]] · [[03 - Funciones#8. Argumentos con nombre|argumentos con nombre]]

#### Ejemplo simple de funcionamiento
```kotlin
val letters = listOf("a", "b", "c")
println(letters.getOrNull(5))                  // null
println(letters.getOrElse(5) { "?" })          // ?
println(letters.joinToString("-"))             // a-b-c
```

### Código fuente (`Ejercicio15.4/src/Main.kt`)

```kotlin
fun main() {
    val testScores = listOf(85, 92, 78, 95, 88, 70)

    println("Número de puntuaciones: ${testScores.size}")
    println("Índice de la última: ${testScores.lastIndex}")
    println("Posición del 95: ${testScores.indexOf(95)}")

    // testScores[10] lanzaría IndexOutOfBoundsException
    try {
        println(testScores[10])
    } catch (e: IndexOutOfBoundsException) {
        println("testScores[10] → excepción: ${e.message}")
    }
    // getOrNull devuelve null si el índice no existe
    println("Elemento en el índice 10: ${testScores.getOrNull(10)}")
    // getOrElse ejecuta la lambda si el índice no existe
    println("Índice 10 o suspenso: ${testScores.getOrElse(10) { 50 }}")

    println("¿Está el 78? ${78 in testScores}")                    // contains(78)
    println("Tres al azar: ${testScores.shuffled().take(3)}")       // cambia en cada ejecución

    val allButLast = testScores.dropLast(1)
    println("Todas menos la última: $allButLast")

    println(testScores.joinToString(separator = " | ", prefix = "[", postfix = "]"))
}
```

### Explicación paso a paso
1. **`size` y `lastIndex`:** 6 elementos, así que el último está en el índice 5 (se empieza a contar en 0).
2. **`indexOf(95)`:** el 95 es el cuarto elemento → índice 3.
3. **Índice 10, tres formas:**
	- `testScores[10]` → lanza `IndexOutOfBoundsException` (capturada para verla).
	- `getOrNull(10)` → `null`, sin excepción.
	- `getOrElse(10) { 50 }` → como no existe, ejecuta la lambda y devuelve 50.
4. **`78 in testScores`:** `true`.
5. **`shuffled().take(3)`:** baraja una **copia** de la lista y se queda con las tres primeras. El resultado cambia en cada ejecución.
6. **`dropLast(1)`:** lista nueva sin el último (el 70).
7. **`joinToString`:** une los elementos con `" | "` entre ellos y añade `[` y `]` en los extremos. Se usan argumentos con nombre para que se lea qué es cada cosa.

> [!tip] Prueba
> ```text
> Número de puntuaciones: 6
> Índice de la última: 5
> Posición del 95: 3
> testScores[10] → excepción: Index 10 out of bounds for length 6
> Elemento en el índice 10: null
> Índice 10 o suspenso: 50
> ¿Está el 78? true
> Tres al azar: [85, 88, 92]
> Todas menos la última: [85, 92, 78, 95, 88]
> [85 | 92 | 78 | 95 | 88 | 70]
> ```
> «Tres al azar» saldrá distinto cada vez que lo ejecutes.

> [!note]- 🧠 Por qué funciona
> - `getOrNull` y `getOrElse` son el equivalente para listas de `?.` y `?:`: en vez de que el programa reviente con un índice que no existe, decides tú qué pasa.
> - Ninguna de estas funciones modifica `testScores`: `shuffled`, `take` y `dropLast` devuelven listas nuevas. Por eso funcionan con una lista de solo lectura.

---

## Ejercicio 5 · Procesamiento funcional de empleados

> [!question] Enunciado
> Define la siguiente *data class*:
>
> ```kotlin
> data class Employee(val name: String, val department: String, val salary: Double)
> ```
>
> Define una `listOf` llamada `employees` con al menos seis instancias que cubran dos o tres departamentos y con salarios variados.
>
> En la función `main`, resuelve estas tareas en orden, **encadenando llamadas** cuando sea posible:
> 1. Filtra la lista para quedarte solo con los empleados del departamento `"IT"`.
> 2. Transforma la lista filtrada en una lista de solo sus nombres.
> 3. Guarda y muestra la lista de nombres de IT.
> 4. Comprueba si **todos** los empleados tienen un salario superior a 60000.0. Muestra el resultado.
> 5. Cuenta cuántos empleados hay en el departamento `"HR"`. Muestra el resultado.
> 6. Ordena la lista completa por salario, de mayor a menor.
> 7. Obtén solo los dos empleados mejor pagados. Imprime su nombre y salario.
> 8. Encuentra el primer empleado cuyo nombre empiece por `'A'`. Muestra su nombre, o un mensaje si es `null`.

### Clases y métodos introducidos
- `filter { … }` y `map { … }`: filtrar y transformar (ya vistos en el [[Ejercicios Bloque 12#Ejercicio 5 · `forEach`, `filter`, `map` y `sumOf` sobre un carrito|Bloque 12]]).
- `all { … }`: `true` si **todos** los elementos cumplen la condición.
- `count { … }`: cuántos elementos la cumplen.
- `sortedByDescending { … }`: lista nueva ordenada de mayor a menor según lo que devuelva la lambda.
- `take(2)`: los dos primeros.
- `find { … }`: el **primer** elemento que cumple la condición, o `null` si no hay ninguno.
- `startsWith("A")`: ¿empieza la cadena por "A"?

> **Términos explicados:** [[11 - Colecciones#7. Procesamiento funcional de listas|procesamiento funcional de listas]] · [[05 - Operaciones con tipos nullables#3. Operador Elvis `?:`|Elvis para el `null` de `find`]]

#### Ejemplo simple de funcionamiento
```kotlin
val numbers = listOf(4, 9, 2, 7)
println(numbers.all { it > 1 })                    // true
println(numbers.count { it % 2 == 0 })             // 2
println(numbers.sortedByDescending { it }.take(2)) // [9, 7]
println(numbers.find { it > 100 })                 // null
```

### Código fuente (`Ejercicio15.5/src/Main.kt`)

```kotlin
data class Employee(val name: String, val department: String, val salary: Double)

val employees = listOf(
    Employee("Ana", "IT", 72000.0),
    Employee("Bruno", "HR", 48000.0),
    Employee("Carla", "IT", 85000.0),
    Employee("David", "Sales", 61000.0),
    Employee("Alberto", "HR", 53000.0),
    Employee("Elena", "IT", 67000.0),
)

fun main() {
    // filter + map encadenados
    val itNames = employees
        .filter { it.department == "IT" }
        .map { it.name }
    println("Empleados de IT: $itNames")

    val allAbove60k = employees.all { it.salary > 60000.0 }
    println("¿Todos cobran más de 60000? $allAbove60k")

    val hrCount = employees.count { it.department == "HR" }
    println("Empleados de HR: $hrCount")

    // Ordenar de mayor a menor salario y quedarse con los dos primeros
    println("Los dos mejor pagados:")
    employees
        .sortedByDescending { it.salary }
        .take(2)
        .forEach { println("  ${it.name}: ${it.salary}") }

    // find devuelve el primero que cumple, o null
    val firstWithA = employees.find { it.name.startsWith("A") }
    println("Primer empleado que empieza por A: ${firstWithA?.name ?: "ninguno"}")

    // Mismo find, sin coincidencias, para ver el mensaje de null
    val firstWithZ = employees.find { it.name.startsWith("Z") }
    println("Primer empleado que empieza por Z: ${firstWithZ?.name ?: "ninguno"}")
}
```

### Explicación paso a paso
1. **Datos:** 6 empleados en 3 departamentos (IT, HR y Sales), con salarios de 48 000 a 85 000.
2. **Tareas 1–3:** `filter` y `map` encadenados dan los nombres de IT: `[Ana, Carla, Elena]`.
3. **Tarea 4:** `all` → `false`, porque Bruno y Alberto cobran menos de 60 000.
4. **Tarea 5:** `count` → 2 empleados en HR.
5. **Tareas 6–7:** `sortedByDescending { it.salary }` ordena de mayor a menor salario, `take(2)` se queda con Carla y Ana, y `forEach` las imprime. Todo en una cadena.
6. **Tarea 8:** `find` devuelve Ana (la primera de la lista que empieza por A, antes que Alberto). Con `?.name ?: "ninguno"` se cubre el caso `null`, que se prueba aparte buscando una Z.

> [!tip] Prueba
> ```text
> Empleados de IT: [Ana, Carla, Elena]
> ¿Todos cobran más de 60000? false
> Empleados de HR: 2
> Los dos mejor pagados:
>   Carla: 85000.0
>   Ana: 72000.0
> Primer empleado que empieza por A: Ana
> Primer empleado que empieza por Z: ninguno
> ```

> [!note]- 🧠 Por qué funciona
> - Encadenar llamadas es como una receta: «filtra, luego transforma, luego ordena, luego coge dos». Cada paso trabaja con lo que devuelve el anterior, y `employees` no se toca.
> - `find` devuelve `Employee?` porque puede no encontrar a nadie. Por eso hace falta `?.` y `?:`, como en el [[Ejercicios Bloque 6#Ejercicio 1 · `getNameLength` con llamadas seguras|Bloque 6]].
> - `all` y `find` paran en cuanto saben la respuesta: `all` en el primer `false`, `find` en el primer acierto.

---

## Ejercicio 6 · Secuencia infinita de usuarios premium

> [!question] Enunciado
> Define la siguiente constante para simular el ID de usuario que buscamos:
>
> ```kotlin
> const val TARGET_ID = 500
> ```
>
> Define una función *top-level* `isPremium(id: Int)` que reciba el ID de un usuario y devuelva un `Boolean`. Debe imprimir un mensaje que simule la verificación costosa en una base de datos, `"Checking premium status for ID: $id"`, y devolver `true` si el ID es par y `false` si no.
>
> Crea una **secuencia infinita** de IDs de usuario, empezando en 1 e incrementando de 1 en 1. Filtra la secuencia para quedarte solo con los usuarios premium. Limita la búsqueda, ya que solo necesitamos llegar hasta el usuario con ID 500. Obtén el nombre de cada usuario (`"User-${it}"`) y, finalmente, busca el nombre `"User-500"`.
>
> Guarda el resultado de toda la cadena en una variable `foundUser` e imprímela. Observa y comenta cuántas veces se ejecutó el mensaje `"Checking premium status for ID: ..."`.

### Clases y métodos introducidos
- `generateSequence(1) { it + 1 }`: una secuencia **infinita** (1, 2, 3…). No se calcula entera: cada número se genera solo cuando alguien lo pide.
- **Operaciones intermedias** (`takeWhile`, `filter`, `map`): en una secuencia solo **describen** los pasos; no hacen nada todavía.
- **Operación terminal** (`find`): es la que pone todo en marcha, pidiendo elementos de uno en uno.
- `takeWhile { it <= TARGET_ID }`: deja pasar elementos mientras se cumpla la condición. Es el «límite» de la búsqueda.
- **Perezosa** (*lazy*, la secuencia) frente a **ansiosa** (*eager*, la `List`): la lista hace cada paso con **todos** los elementos antes de pasar al siguiente; la secuencia lleva **cada elemento** por todos los pasos y se para en cuanto tiene la respuesta.

> **Términos explicados:** [[11 - Colecciones#8. Secuencias|secuencias]] · [[08 - POO III#3. Constantes conocidas en tiempo de compilación|`const val`]] · [[08 - POO III#2. Top-level properties|*top-level properties*]]

#### Ejemplo simple de funcionamiento
```kotlin
val firstBig = generateSequence(1) { it * 2 }   // 1, 2, 4, 8, 16…
    .find { it > 100 }
println(firstBig)                                // 128 (solo se generan 8 números)
```

### Código fuente (`Ejercicio15.6/src/Main.kt`)

```kotlin
const val TARGET_ID = 500

var premiumChecks = 0    // contador para comprobar cuántas veces se llama a isPremium

// Simula una consulta costosa a la base de datos
fun isPremium(id: Int): Boolean {
    premiumChecks++
    println("Checking premium status for ID: $id")
    return id % 2 == 0
}

fun main() {
    // Versión con Sequence (perezosa)
    val foundUser = generateSequence(1) { it + 1 }   // 1, 2, 3, ... (infinita)
        .takeWhile { it <= TARGET_ID }               // limita la búsqueda hasta el ID 500
        .filter { isPremium(it) }                    // solo usuarios premium (ID par)
        .map { "User-$it" }                          // ID -> nombre
        .find { it == "User-$TARGET_ID" }            // terminal: aquí empieza a trabajar todo

    println("foundUser = $foundUser")
    val sequenceChecks = premiumChecks

    // Comparación: lo mismo con una List (eager) de IDs 1..1000
    premiumChecks = 0
    val foundWithList = (1..1000).toList()
        .filter { isPremium(it) }                    // ¡se comprueban los 1000 antes de seguir!
        .map { "User-$it" }
        .find { it == "User-$TARGET_ID" }

    println("foundWithList = $foundWithList")
    println("Comprobaciones con Sequence: $sequenceChecks")
    println("Comprobaciones con List 1..1000: $premiumChecks")
}
```

### Explicación paso a paso
1. **`isPremium`:** imprime el mensaje, suma 1 a un contador (`premiumChecks`, para no tener que contar 500 líneas a mano) y devuelve si el ID es par.
2. **La secuencia:** hasta llegar a `find`, nada se ejecuta. `find` pide el primer elemento: el 1 pasa `takeWhile`, llega a `filter` (`isPremium(1)` → `false`) y se descarta. Luego el 2: pasa el filtro, `map` lo convierte en `"User-2"` y `find` lo rechaza. Y así sucesivamente.
3. **El 500:** `isPremium(500)` → `true`, `map` da `"User-500"` y `find` lo acepta. **La secuencia se para**: el 501 nunca llega a generarse.
4. **`takeWhile`:** es el límite que pide el enunciado. Aunque `"User-500"` no existiera, la búsqueda acabaría en el 500 y `find` devolvería `null`, en vez de quedarse en un bucle infinito.
5. **Comparación con `List`:** con una lista hay que partir de un rango **finito** (aquí 1..1000), y `filter` comprueba **los 1000** IDs antes de que `find` empiece a buscar.

> [!tip] Prueba (resumida: la salida real tiene 1504 líneas)
> ```text
> Checking premium status for ID: 1
> Checking premium status for ID: 2
> ... (una línea por cada ID hasta el 500)
> Checking premium status for ID: 500
> foundUser = User-500
> Checking premium status for ID: 1
> ... (una línea por cada ID hasta el 1000)
> foundWithList = User-500
> Comprobaciones con Sequence: 500
> Comprobaciones con List 1..1000: 1000
> ```

> [!warning] ¿Cuántas veces se ejecuta `isPremium`? (respuesta comprobada)
> El enunciado termina diciendo que, con la secuencia, «solo se verifica el 500». **No es así**: al ejecutarlo, `isPremium` se llama **500 veces**, una por cada ID del 1 al 500. El filtro tiene que comprobar cada ID para saber si es premium, y el 500 es el elemento número 500 de la secuencia.
>
> La ventaja real de la secuencia es otra:
> - **Se para en cuanto encuentra el resultado.** Con la `List` de 1..1000 se comprueban los 1000 IDs aunque el buscado sea el 500.
> - **Permite trabajar con algo infinito.** Con una `List` no se puede: habría que decidir antes cuántos IDs crear.
>
> Lo que sí es cierto: con una `List` de exactamente 1..500 también serían 500 llamadas. La diferencia aparece cuando no sabes dónde está lo que buscas.

> [!note]- 🧠 Por qué funciona
> - La `List` trabaja como una cadena de montaje por **lotes**: primero filtra todas las piezas, luego las transforma todas y luego busca. La secuencia trabaja **pieza a pieza**: cada pieza recorre la cadena entera antes de que entre la siguiente, y en cuanto sale la que buscabas, se apaga la máquina.
> - Por eso, con una secuencia, el orden de los pasos importa: poner `takeWhile` **antes** de `filter` evita llamar a `isPremium` con IDs mayores que 500.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Crear colecciones | `listOf` · `setOf` · `mapOf` · `mutableListOf` · `mutableMapOf` | Solo lectura o mutables; el `Set` no admite repetidos. |
| Lista calculada | `List(5) { it + 100 }` | Cada elemento a partir de su índice. |
| Convertir | `toSet()` · `toMutableList()` | Siempre crean una colección nueva. |
| Operador `[]` | `m["k"]` · `l[2] = x` · `m["k"] = v` | `get` · `set` · `put`. |
| `+` / `-` | `lista + x` · `lista - x` | Lista nueva; la original no cambia. |
| `+=` con lista de solo lectura | `var l = listOf(…); l += x` | `l = l + x`: la variable tiene que ser `var`. |
| Acceso seguro | `getOrNull(i)` · `getOrElse(i) { … }` | Sin `IndexOutOfBoundsException`. |
| Consultas | `size` · `lastIndex` · `indexOf` · `in` | Tamaño, último índice, posición y pertenencia. |
| Funcionales | `filter` · `map` · `all` · `count` · `sortedByDescending` · `take` · `find` | Encadenables; no modifican la original. |
| Unir | `joinToString(separator, prefix, postfix)` | Lista → `String` con formato. |
| Secuencia | `generateSequence(1) { it + 1 }` | Infinita y perezosa; trabaja elemento a elemento y para al terminar. |

## Relaciones

- Teoría: [[11 - Colecciones]] · [[10 - Programación funcional]]
- Bloque anterior: [[Ejercicios Bloque 14]]
- Mismos enunciados en el boletín: [[11.1 - Ejercicios 11 Colecciones]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Crear cada tipo de colección y saber cuáles se pueden modificar
- [ ] Explicar la diferencia entre `val` con lista mutable y `var` con lista de solo lectura
- [ ] Usar `[]`, `+`, `-`, `+=` y `-=` en listas y mapas
- [ ] Acceder a un índice que puede no existir sin que el programa falle
- [ ] Encadenar `filter`, `map`, `sortedByDescending` y `take`
- [ ] Explicar cuántas veces se ejecuta el filtro en una secuencia y por qué
