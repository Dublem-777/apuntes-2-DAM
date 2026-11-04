---
asignatura: PMDM
tema: 11
tipo: tema
estado: completo
fecha: 2026-10-25
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-colecciones
---

# 11 · Colecciones en Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 11 · Kotlin  
> Ejercicios: [[11.1 - Ejercicios 11 Colecciones]] · Tema anterior: [[10 - Programación funcional]]

> [!info] Material de referencia
> [Colecciones en Kotlin](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b11%20-%20Colecciones%20en%20Kotlin/)

## Índice del tema

- [[#1. Introducción]]
- [[#2. Interfaces de colecciones]]
- [[#3. Creación de colecciones]]
- [[#4. Obtener una colección a partir de otra]]
- [[#5. Operadores sobrecargados en colecciones]]
- [[#6. Métodos y propiedades de listas]]
- [[#7. Procesamiento funcional de listas]]
- [[#8. Secuencias]]

---

## 1. Introducción

Una **colección** es un grupo de 0 o más elementos, normalmente del mismo tipo (o subtipos) que están relacionados entre sí. En Kotlin tenemos tres tipos de colecciones principales:

- **Lista** (_list_): Es una colección ordenada de elementos a los que podemos acceder a partir de su posición o índice en la colección. Los elementos pueden aparecer más de una vez en una lista. El índice del primer elemento es `0` y el del último se puede obtener con la propiedad `lastIndex` de la lista, que es igual a `size - 1`.
- **Conjunto** (_set_): Es una colección de elementos únicos. Refleja la abstracción matemática del conjunto: un grupo de objetos sin repeticiones. Generalmente, el orden de los elementos en un set no tiene importancia.
- **Mapa** o diccionario (_map_): Es un conjunto de pares clave-valor. Las claves son únicas y cada una de ellas se asigna exactamente a un valor. Los valores pueden ser duplicados. Los mapas son útiles para almacenar conexiones lógicas entre objetos, por ejemplo, el ID de un empleado y su puesto.

Kotlin permite manipular colecciones independientemente del tipo exacto de objetos que contienen. Para ello, la biblioteca estándar de Kotlin ofrece interfaces, clases y funciones genéricas para crear y procesar colecciones de cualquier tipo.

> [!warning] Aviso
> Los arrays de Kotlin NO son un tipo de colección, estrictamente hablando, aunque la clase `Array<T>` posee métodos parecidos a los de las colecciones.

## 2. Interfaces de colecciones

La biblioteca estándar de Kotlin proporciona en el paquete `kotlin.collections` interfaces genéricas, clases y funciones para la creación, almacenamiento y gestión de colecciones de cualquier tipo. Veamos un diagrama con ellas, indicando cual extiende o implementa cuál.

> [!note] Diagrama no incluido
> En los apuntes originales aquí aparece la imagen "Colecciones en Kotlin" con la jerarquía de interfaces, que no se copió en el volcado. En resumen: `Iterable<T>` → `Collection<T>` → `List<T>` y `Set<T>`, cada una con su versión `Mutable…`; `Map<K, V>` va aparte y no hereda de `Collection`.

Para cada colección básica (lista, conjunto o mapa), en vez de definir una única interfaz, como ocurre en Java, Kotlin define un par de interfaces:

- Una interfaz que sólo permite realizar operaciones de lectura una vez creada la colección, por ejemplo `List<T>`, `Set<T>`, `Map<K, V>`, etc.
- Una interfaz que permite realizar tanto operaciones de lectura como de escritura una vez creada la colección. El nombre de estas interfaces comienzan siempre con la palabra `Mutable`, por ejemplo `MutableList<T>`, `MutableSet<T>`, `MutableMap<K, V>`, etc. y extienden sus correspondientes interfaces que solo permiten operaciones de lectura.

Las interfaces que sólo permiten operaciones de sólo lectura definen tipos covariantes, lo que implica que, si por ejemplo, `Rectangle` es un subtipo de `Shape`, entonces podemos usar un valor del tipo `List<Rectangle>` allá donde se requiera un `List<Shape>`.

Sin embargo, las interfaces que permiten operaciones de lectura y de escritura definen tipos invariantes, por lo que, mientras no se indique explícitamente, no podremos usar un `MutableList<Rectangle>` allá donde se requiera un `MutableList<Shape>`.

Las clases reales que se usan para operar sobre colecciones son dependientes de la plataforma. Por ejemplo, si estamos sobre la JVM, al crear una lista con la función `listOf()`, se creará un objeto de la clase `java.util.ArrayList`.

> [!note] Matiz comprobado con `kotlinc`
> En la JVM, `mutableListOf()` crea un `java.util.ArrayList`, pero `listOf("a", "b", "c")` crea un `java.util.Arrays$ArrayList` (una lista de tamaño fijo). `setOf()` y `mapOf()` crean `LinkedHashSet` y `LinkedHashMap`, que **conservan el orden de inserción**.

## 3. Creación de colecciones

La mayoría de los lenguajes tienen soporte para una característica llamada “literal de colección”, que es una sintaxis especial para crear un cierto tipo de colección basada en la lista de elementos proporcionada. En Kotlin, esta característica es realizada por _top-level functions_, cuyos nombres, por convención, comienzan con el nombre del tipo que producen (empezando con minúscula) y el sufijo `Of`.

Por ejemplo, tenemos la funciones `listOf()`, `setOf()` o `mapOf()`, y `mutableListOf()`, `mutableSetOf()` o `mutableMapOf()`, que reciben como argumento un _vararg_ de elementos. Estas funciones están parametrizadas con el tipo para los elementos de la colección, aunque normalmente podrá inferirse a partir de los valores proporcionados.

Si queremos construir colecciones vacías, tenemos las funciones `emptyList()`, `emptySet()` y `emptyMap()`.

También podemos crear una lista de un tamaño concreto con la función `List()` (de solo lectura) o `MutableList()` (mutable), que recibe como argumento un tamaño y una lambda para construir cada elemento a partir de su índice en la colección, que es llamada internamente por la función para rellenar la lista con el número de elementos indicado.

Si queremos que la implementación de la colección corresponda a una clase concreta, por ejemplo para una `List<T>` una `LinkedList<T>`, deberemos usar el constructor de dicha clase pasándole una colección.

**Construcción de colecciones**

```kotlin
import java.util.LinkedList

// Crean un List<String>
val list = listOf("Item1", "Item2", "Item3")
val emptyList = emptyList<String>()
val linkedList = LinkedList<String>(listOf("Item1", "Item2", "Item3"))

// Crean un MutableList<String>
val mutableList = mutableListOf("Item1", "Item2", "Item3")
val supplierList = List(3) { "Item${it + 1}" }
val supplierMutableList = MutableList(3) { "Item${it + 1}" }

// Crean un Set<String>
val theSet = setOf("Item1", "Item2", "Item3")
val emptySet = emptySet<String>()

// Crea un MutableSet<String>
val mutableSet = mutableSetOf("Item1", "Item2", "Item3")

// Crean un Map<String, Int>
val map = mapOf("A" to 18, "B" to 24)
val emptyMap = emptyMap<String, Int>()

// Crea un MutableMap<String, Int>
val mutableMap = mutableMapOf("A" to 18, "B" to 24)
```

[Explicación en video](https://www.youtube.com/embed/y6wp4c92DT4)

> [!example] Práctica
> [[11.1 - Ejercicios 11 Colecciones#Ejercicio 11.1 · Creación de colecciones|Ejercicio 11.1 · Creación de colecciones]]

## 4. Obtener una colección a partir de otra

También podemos obtener una colección a partir de otra. Para ello, tendremos disponibles en nuestra collección métodos que comienzan con el prefjio `to` seguido del tipo de colección al que queremos convertir, como por ejemplo `toSet()`, `toMutableList()`, `toMutableSet()`, etc.

**Obtener una colección a partir de otra**

```kotlin
val list = listOf("Item1", "Item2", "Item3")
val theSet = list.toSet()
val mutableList = list.toMutableList()
```

> [!example] Práctica
> [[11.1 - Ejercicios 11 Colecciones#Ejercicio 11.2 · Conversión entre colecciones con toSet y toMutableList|Ejercicio 11.2 · Conversión entre colecciones con toSet y toMutableList]]

## 5. Operadores sobrecargados en colecciones

Para acceder a un elemento de una lista podemos usar el operador corchete '[]' pasándole el índice del elemento al que acceder, ya que internamente se llamará al método `get(indice)` o `set(indice, valor)`, dependiendo de si se está accediendo para lectura o para escribir un valor.

De igual forma, en el caso de los mapas, podemos acceder a un elemento del mapa usar el operador corchete pasándole la clave del elemento, ya que internamente se llamará al método `get(clave)` o `put(clave, valor)`, dependiendo de si se está accediendo para lectura o para escribir un valor.

**Acceso a un elemento de una lista o mapa con operador []**

```kotlin
val mutableList = mutableListOf("Item1", "Item2", "Item3")
val mutableMap = mutableMapOf("A" to 18, "B" to 24)

println(mutableList[0])     // Item1
mutableList[0] = "New item"
println(mutableList[0])     // New item

println(mutableMap["B"])    // 24
mutableMap["B"] = 48
println(mutableMap["B"])    // 48
```

> [!note] Comparación con Java
> En Java no hay sobrecarga de operadores: se escribe `list.get(0)`, `list.set(0, "x")` o `map.put("B", 48)`. En Kotlin el operador `[]` llama a esos mismos métodos (`get`/`set`), como se vio en la [[08 - POO III#7. Sobrecarga de operadores|sobrecarga de operadores]].

Por otra parte, el operador `+` está sobrecargado en las colecciones para crear una nueva colección a partir de la colección existente más el elemento o la colección pasada como segundo operando. Internamente se crea una nueva colección, y se le agregan todos los elementos de la colección original más el elemento o elementos de la colección indicada como segundo operando. También podremos usar el operador `+=` si la colección está definida en una variable `var`.

De igual forma, el operador `-` está también sobrecargado en las colecciones para crear una nueva colección a partir de la colección existente excepto el elemento o los elementos de la colección pasada como segundo operando. Internamente se crea una nueva colección, y se le agregan todos los elementos de la colección original menos el elemento o elementos de la colección indicada como segundo operando. También podremos usar el operador `-=` si la colección original está definida en una variable `var`.

Veamos algunos ejemplos:

**Creación de nuevas colecciones con operadores `+` y `-`**

```kotlin
var list = listOf("Item1", "Item2", "Item3")
val newList = list + "Item4"
println(list)       // [Item1, Item2, Item3]
println(newList)    // [Item1, Item2, Item3, Item4]

// list "apuntará" a una nueva lista
list += listOf("Item5", "Item6")
list += setOf("Item7", "Item8")
println(list)       // [Item1, Item2, Item3, Item5, Item6, Item7, Item8]

list -= "Item5"
list -= listOf("Item2", "Item3")
println(list)       // [Item1, Item6, Item7, Item8]
```

> [!example] Práctica
> [[11.1 - Ejercicios 11 Colecciones#Ejercicio 11.3 · Operador corchete y operadores + y - en colecciones|Ejercicio 11.3 · Operador corchete y operadores + y - en colecciones]]

## 6. Métodos y propiedades de listas

A continuación mostramos algunas de las propiedades y métodos más habituales de una colección:

- `size`: Devuelve el el número de elementos de una colección. Si queremos obtener el último índice en una colección ordendada podemos usar `lastIndex`.
- `getOrNull(index)`: Obtiene el elemento cuya posición corresponde al índice indicado o si no existe retorna `null` (a diferencia del método `get(index)`, que en ese caso lanza una excepción `IndexOutOfBounds` exception). También tenemos el método `getOrElse(index, lambda)`, que recibe, además del índice, la lambda que será ejecutada si no se encuentre dicho elemento, y que deberá retornar el valor que en ese caso debe retornar el método.
- `indexOf(elemento)`: Devuelve el índice del elemento en la colección o `-1` si no se encuentra.
- `contains(element)`: Devuelve `true` si el elemento se encuentra en la colección. Es el método que es llamado internamente por el operador `in`.
- `shuffled()`: Devuelve una nueva lista a partir de la original, pero con los elementos ordenados en una posición aleatoria (barajar).
- `random()`: Devuelve un elemento aleatorio de la lista.
- `joinToString()`: Devuelve una cadena correspondiente a concatenar los elementos de la lista. Recibe varios parámetros opcionales que nos permiten indicar el separador entre elementos, un prefijo antes del primer elemento y un sujijo después del último elemento.
- `take(n)`, `takeLast(n)`: Devuelve una nueva lista con los primeros / últimos `n` elementos de la colección original.
- `drop(n)`, `dropLast(n)`: Devuelve una nueva lista con todos los elementos de la colección original excepto los primeros / últimos `n` elementos.

> [!example] Práctica
> [[11.1 - Ejercicios 11 Colecciones#Ejercicio 11.4 · Métodos y propiedades de listas con testScores|Ejercicio 11.4 · Métodos y propiedades de listas con testScores]]

## 7. Procesamiento funcional de listas

Una de las aplicaciones más útiles de la programación funcional es el procesamiento de colecciones para realizar operaciones con sus elementos. De hecho, éste ha sido una de las las razones principales por la que la mayoría de los lenguajes orientados a objetos modernos han introducido soporte para características de programación funcional.

El estilo de programación funcional ofrece muchos beneficios cuando se trata de procesar colecciones. Para la mayoría de las tareas, podemos utilizar funciones proporcionadas por la biblioteca estándar y personalizar su comportamiento pasando lambdas como argumentos a dichas funciones. Esto nos permite expresar operaciones comunes de manera consistente, utilizando un vocabulario de funciones que compartes con otros desarrolladores de Kotlin.

A continuación de muestran los nombres de los métodos correspondientes a las operaciones más habituales con listas para su procesamiento mediante programación funcional:

- `forEach(lambda)`: Ejecuta la lambda para cada elemento de la colección, que es pasado a la lambda.
- `map(lambda)`: Retorna una nueva lista cuyos elementos corresponden a aplicar la lambda a cada uno de los elementos de la lista original. La lambda recibe el lemento correspondiente.

**Método map()**

```kotlin
val numbers = listOf(1, 2, 3)
val result = numbers.map { it * 3 }    // [3, 6, 9]
```

- `onEach(lambda)`: Retorna una nueva lista cuyos elementos corresponden exactamente a los de la lista original, pero ejecuta la lambda recibida para cada uno de los elementos de la lista original, de manera que el elemento es pasado a la lambda.
- `flatMap(lambda)`: Cuando los elementos de la lista son a su vez listas de elementos, podemos usar este método para extraer todos los elementos de las sublistas y transformarlos usando la lambda, de manera que se retorne una nueva lista de elementos simples.
- `filter(lambda)`: Retorna una nueva lista cuyos elementos corresponden a aquellos elementos de la lista original para los que la ejecución de la lambda retorna `true`. La lamba recibe el elemento original.

**Método filter()**

```kotlin
val numbers = listOf("one", "two", "three", "four")
val result = numbers.filter { it.length > 3 }    // [three, four]
```

- `sortedBy(lambda)` y `sortedByDescending(lambda)`: Retorna una nueva lista cuyos elementos corresponden a los elementos de la lista original pero ordenados atendiendo al valor retornado por la lambda, que recibe el elemento original, y que debe retornar la propiedad por la que se deben ordenar los elementos.

**Método sortedBy()**

```kotlin
val numbers = listOf("one", "two", "three", "four")
val result = numbers.sortedBy { it.length }    // [one, two, four, three]
```

- `all(lambda_predicado)`: Retorna `true` si todos los elementos de la colección cumplen con el predicado correspondiente a la lambda, que recibe el elemento y retorna un booleano indicativo de si lo cumple o no. También tenemos el método `none(lambda_predicado)` que retorna `true` ni ningún elemento de la colección cumple el predicado, y `any(lambda_predicado)`, que retorna `true` si algún elemento lo cumple. Finalmente `count(lambda_predicado)` retorna cuántos elemntos cumplen el predicado.
- `find(lambda_predicado)` o `firstOrNull(lambda_predicado)`: Retorna el primer elemento de la colección que cumpla el predicado, o `null` si ninguno lo cumple. Si queremos devolver el último elemento de la colección que lo cumple, podemos usar `findLast(lambda_predicado)` o `lastOrNull(lambda_predicado)`.

> [!tip] Sugerencia
> Existen varios métodos adicionales para realizar operaciones más complejas, como particionar una colección en varias colecciones, fusionar varias colecciones en una, etc. Se recomienda estudiar bien las posibilidades existente en la libería estándar cuando tengamos que realizar estas operaciones.

> [!example] Práctica
> [[11.1 - Ejercicios 11 Colecciones#Ejercicio 11.5 · Procesamiento funcional de empleados|Ejercicio 11.5 · Procesamiento funcional de empleados]]

## 8. Secuencias

Una `Sequence<T>` en Kotlin representa una manera de computar datos de forma **perezosa** (_lazy_). A diferencia de las colecciones (`List`, `Set`), que procesan todos sus elementos y crean una nueva colección intermedia en cada paso de una cadena de operaciones, las `Sequence` procesan los elementos **uno a uno** y solo cuando se solicita un resultado.

Esto las hace especialmente útiles para:

- **Grandes conjuntos de datos:** Se reduce el uso de memoria al no crear colecciones intermedias.
- **Cadenas de operaciones complejas:** Se mejora el rendimiento porque se evita trabajo innecesario (evaluación mínima).
- **Secuencias infinitas:** Solo se evalúan los elementos que se necesitan.

Se pueden crear `Sequence` de varias maneras:

- A partir de una `Collection` existente usando la función de extensión `asSequence()`.
- Usando la función `sequenceOf()` para un conjunto fijo de elementos.
- Usando la función _builder_ `generateSequence()`.
- Usando el _builder_ `sequence { ... }` (ideal para lógica más compleja o secuencias infinitas).

**Crear secuencias**

```kotlin
fun main() {
    val lista = listOf(1, 2, 3, 4, 5) 
    val sequenceDesdeLista = lista.asSequence() 
    println(sequenceDesdeLista.toList()) // Salida: [1, 2, 3, 4, 5]  
    // Genera números hasta que el resultado es null 
    val sequencePotenciasDeDos = generateSequence(1) { it * 2 }
        .take(5) // Operación terminal para limitar la secuencia 
    println(sequencePotenciasDeDos.toList()) // Salida: [1, 2, 4, 8, 16]  
}
```

> [!warning] Ojo con los comentarios del ejemplo
> `generateSequence(1) { it * 2 }` termina cuando la lambda devuelve `null`; como aquí nunca lo hace, la secuencia es **infinita**. Y `take(5)` **no** es una operación terminal, como dice el comentario, sino **intermedia**: solo limita la secuencia a 5 elementos. La operación terminal que dispara el cálculo es `toList()`, en el `println` siguiente (así aparece también en la lista de abajo).

Las operaciones sobre `Sequence` se dividen en dos categorías cruciales:

- **Operaciones intermedias** (_intermediate operations_): Retornan otra `Sequence`. Se evalúan **perezosamente**; solo almacenan la lógica de la operación y no se ejecutan hasta que se llama a una operación terminal. Ejemplos: `map()`, `filter()`, `flatMap()`, `distinct()`, `take()`, `drop()`.
- **Operaciones terminales** (_terminal operations_): Retornan un resultado (una colección, un valor, etc.). Son las que disparan la evaluación real de toda la cadena de operaciones intermedias sobre los elementos. Ejemplos: `toList()`, `count()`, `sum()`, `maxOrNull()`, `forEach()`, `find()`, `first()`, `any()`, `all()`.

**Encadenamiento de operaciones intermedias y terminales**

```kotlin
fun main() {
    val numeros = listOf(1, 2, 3, 4, 5, 6).asSequence()
    val resultado = numeros
        .filter { it % 2 == 0 } // Intermedia: se guarda la lógica (filtra pares)
        .map { it * 2 }       // Intermedia: se guarda la lógica (multiplica por 2)
        .toList()             // Terminal: ¡Aquí se ejecuta todo!
    println(resultado) // Salida: [4, 8, 12]
}
```

El proceso del ejemplo anterior sería:

- toma el `1` (no pasa `filter`)
- toma el `2` (`filter -> 2`, `map -> 4`)
- toma el `3` (no pasa `filter`)
- toma el `4` (`filter -> 4`, `map -> 8`)
- y así sucesivamente, procesando cada elemento hasta el final de la cadena de forma individual.

Esta es la diferencia fundamental que debe entender cualquier desarrollador de Kotlin.

|Característica|Collection (List, Set)|Sequence (`Sequence<T>`)|
|---|---|---|
|**Evaluación**|**Ansiosa** (_Eager_)|**Perezosa** (_Lazy_)|
|**Flujo**|Por operación (_Horizontal_): Se aplica una operación a **todos** los elementos, luego la siguiente, etc.|Por elemento (_Vertical_): Se aplica **toda** la cadena de operaciones a un solo elemento, luego al siguiente, etc.|
|**Colecciones Intermedias**|Crea una nueva colección por cada operación intermedia.|**No** crea colecciones intermedias.|
|**Rendimiento/Memoria**|Preferible para conjuntos **pequeños**. Puede ser ineficiente con grandes datos o muchas transformaciones.|Preferible para conjuntos **grandes** y cadenas de operaciones complejas. Más eficiente en memoria.|
|**Uso**|Por defecto para la mayoría de los casos.|Cuando la eficiencia de memoria o la evaluación mínima son críticas.|

**Comparación de evaluación (ansiosa vs. perezosa)**

```kotlin
fun main() {
    val lista = listOf(1, 2, 3, 4)
    // Colección (Evaluación Ansiosa)
    println("--- Evaluación Ansiosa (Colección) ---")
    lista.filter {
        println("Lista - Filtro: $it")
        it > 2
    }.map {
        println("Lista - Mapa: $it")
        it * 10
    } // Se crea una lista de filtros, luego una lista de mapas
    // Sequence (Evaluación Perezosa)
    println("\n--- Evaluación Perezosa (Sequence) ---")
    lista.asSequence().filter {
        println("Sequence - Filtro: $it")
        it > 2
    }.map {
        println("Sequence - Mapa: $it")
        it * 10
    }.toList() // toList() obliga a la evaluación
    // Observarás que el 1 y el 2 solo pasan por 'Filtro' y no llegan a 'Mapa'.
}
```

> [!example] Práctica
> [[11.1 - Ejercicios 11 Colecciones#Ejercicio 11.6 · Secuencia infinita de usuarios premium|Ejercicio 11.6 · Secuencia infinita de usuarios premium]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Tipos de colección | `List` · `Set` · `Map` | Ordenada con repetidos · elementos únicos · pares clave-valor con claves únicas. |
| Solo lectura / mutable | `List<T>` / `MutableList<T>` | Las de solo lectura son covariantes (`out`); las mutables, invariantes. |
| Creación | `listOf()` · `mutableListOf()` · `setOf()` · `mapOf("A" to 1)` · `emptyList<T>()` | Funciones _top-level_ `xxxOf()`; el tipo suele inferirse. |
| Creación con lambda | `List(5) { it + 100 }` · `MutableList(3) { … }` | Construye cada elemento a partir de su índice. |
| Conversión | `toSet()` · `toList()` · `toMutableList()` | Crea una colección **nueva** del tipo pedido. |
| Operador `[]` | `lista[0]` · `lista[0] = x` · `mapa["B"] = 48` | Llama a `get`/`set` (listas) o `get`/`put` (mapas). |
| Operadores `+` y `-` | `lista + "x"` · `lista -= "x"` | Devuelven una colección nueva; con `var`, `+=`/`-=` reasignan la variable. |
| Consulta | `size` · `lastIndex` · `indexOf()` · `contains()`/`in` · `getOrNull()` · `getOrElse()` | Información y acceso seguro por índice. |
| Recorte y formato | `take()` · `drop()` · `shuffled()` · `random()` · `joinToString()` | Sublistas, orden aleatorio y conversión a texto. |
| Transformación | `map` · `flatMap` · `onEach` · `forEach` | Aplicar una lambda a cada elemento. |
| Filtrado y orden | `filter` · `sortedBy` · `sortedByDescending` | Seleccionar y ordenar por una propiedad. |
| Predicados | `all` · `any` · `none` · `count` · `find`/`firstOrNull` | Preguntas sobre los elementos. |
| Secuencias | `asSequence()` · `generateSequence()` · `sequence { }` | Evaluación **perezosa**, elemento a elemento, sin colecciones intermedias. |
| Intermedias / terminales | `map`, `filter`, `take` / `toList`, `count`, `find`, `first` | Las intermedias no hacen nada hasta que hay una terminal. |

## Relaciones

- Ejercicios del tema: [[11.1 - Ejercicios 11 Colecciones]]
- [[10 - Programación funcional]] — lambdas, `it` y _trailing lambda_, que se usan en todo el procesamiento de colecciones.
- [[09 - Genéricos]] — por qué `List<out E>` es covariante y `MutableList<E>` invariante.
- [[08 - POO III]] — sobrecarga de operadores (`[]`, `+`, `-`, `in`) y `lazy`, la misma idea de perezosa que las secuencias.
- [[02 - Jerarquia de tipos#10. Arrays|02 - Jerarquía de tipos → 10. Arrays]] — los arrays, que no son colecciones.
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Diferenciar `List`, `Set` y `Map`, y sus versiones `Mutable…`.
- [ ] Crear cada colección con su función `xxxOf()`, vacía o con `List(n) { … }`.
- [ ] Explicar qué hacen `+`, `-`, `+=` y `-=` con una colección de solo lectura en una `var`.
- [ ] Acceder por índice o clave con `[]` y de forma segura con `getOrNull`/`getOrElse`.
- [ ] Encadenar `filter`, `map`, `sortedByDescending` y `take`.
- [ ] Usar `all`, `any`, `none`, `count` y `find`.
- [ ] Explicar la diferencia entre evaluación ansiosa (colecciones) y perezosa (secuencias).
- [ ] Distinguir operaciones intermedias y terminales en una `Sequence`.
