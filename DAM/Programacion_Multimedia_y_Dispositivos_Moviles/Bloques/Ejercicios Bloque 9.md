---
asignatura: PMDM
tema: 7
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/ejercicios
---

# Bloque 9 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[07 - POO II]] · [[06 - POO I]]
> Bloque anterior: [[Ejercicios Bloque 8]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque9/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 7.1, 7.2 y 7.4 de [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2|el boletín 7]], y el código parte de esas soluciones.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque9/Ejercicio9.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · `data class` `Product` y `copy()`]]
- [[#Ejercicio 2 · Desestructuración de `Employee`]]
- [[#Ejercicio 3 · Clase abstracta `Animal`]]

---

## Ejercicio 1 · `data class` `Product` y `copy()`

> [!question] Enunciado
> Define una *data class* llamada `Product` para gestionar los datos de un producto en el almacén, con las siguientes propiedades: `id`, `name`, `price` y `quantity`.
>
> Crea una función `updateProduct()` que reciba un producto y devuelva un **nuevo** producto en el que el precio esté incrementado en el porcentaje recibido como argumento. Para ello debe usarse el método `copy()` de la *data class*.

### Clases y métodos introducidos
- `data class`: una clase pensada para **guardar datos**. A partir de las propiedades del constructor primario, Kotlin genera automáticamente:
	- `toString()` legible: `Product(id=1, name=Teclado, …)`.
	- `equals()` / `hashCode()`: dos productos son iguales (`==`) si tienen los mismos datos.
	- `copy()`: crea otro objeto igual, cambiando solo lo que le digas.
	- `component1()`, `component2()`…: los usa la desestructuración (ejercicio 2).
- `copy(price = …)`: usa **argumentos con nombre**; las propiedades que no nombras se copian tal cual.
- `===` vs `==`: `===` pregunta si son **el mismo objeto**; `==` pregunta si tienen **los mismos datos**.

> **Términos explicados:** [[07 - POO II#Data class|`data class`, `copy()` y métodos generados]] · [[03 - Funciones#8. Argumentos con nombre|argumentos con nombre]]

#### Ejemplo simple de funcionamiento
```kotlin
data class Point(val x: Int, val y: Int)

fun main() {
    val a = Point(1, 2)
    val b = a.copy(y = 5)
    println(a)              // Point(x=1, y=2)
    println(b)              // Point(x=1, y=5)
    println(a == Point(1, 2))   // true: mismos datos
}
```

### Código fuente (`Ejercicio9.1/src/Main.kt`)

```kotlin
data class Product(
    val id: Int,
    val name: String,
    val price: Double,
    val quantity: Int,
)

// Devuelve un producto NUEVO con el precio incrementado en el porcentaje indicado
fun updateProduct(product: Product, percentage: Double): Product {
    require(percentage >= 0.0) { "Percentage must be non-negative" }
    return product.copy(price = product.price * (1 + percentage / 100))
}

fun main() {
    val keyboard = Product(1, "Teclado", 50.0, 8)
    val updated = updateProduct(keyboard, 10.0)

    println("Original:    $keyboard")
    println("Actualizado: $updated")
    println("Precio con 2 decimales: ${"%.2f".format(updated.price)}")
    println("¿Son el mismo objeto? ${keyboard === updated}")
    println("¿Tienen los mismos datos? ${keyboard == updated}")
    println("¿Igual a otro Teclado de 50 €? ${keyboard == Product(1, "Teclado", 50.0, 8)}")
}
```

### Explicación paso a paso
1. **La data class:** las cuatro propiedades van en el constructor primario con `val`. Son inmutables: para «cambiar» un producto se crea otro.
2. **`updateProduct`:** recibe el producto y el porcentaje. `require` rechaza porcentajes negativos, porque el enunciado habla de **incrementar**.
3. **El cálculo:** subir un 10 % es multiplicar por `1 + 10 / 100 = 1.1`. `copy(price = …)` crea un producto nuevo con ese precio y con el mismo `id`, `name` y `quantity`.
4. **El original no cambia:** `keyboard` sigue valiendo 50 €. Como las propiedades son `val`, la única forma de tener otro precio es otro objeto.
5. **Pruebas:** se imprimen los dos productos (gracias al `toString()` generado) y se comparan con `===` y `==`.

> [!tip] Prueba
> ```text
> Original:    Product(id=1, name=Teclado, price=50.0, quantity=8)
> Actualizado: Product(id=1, name=Teclado, price=55.00000000000001, quantity=8)
> Precio con 2 decimales: 55,00
> ¿Son el mismo objeto? false
> ¿Tienen los mismos datos? false
> ¿Igual a otro Teclado de 50 €? true
> ```

> [!warning] ¿Por qué `55.00000000000001` y no `55.0`?
> Un `Double` guarda los números en binario, y `1.1` no se puede representar exacto en binario (igual que 1/3 no se puede escribir exacto en decimal: 0,3333…). Por eso `50.0 * 1.1` da `55.00000000000001`. Pasa igual en Java.
> - Para **mostrarlo**, se formatea: `"%.2f".format(price)` → `55,00`.
> - En programas reales con dinero se usa `BigDecimal`, que sí es exacto ([[02 - Jerarquia de tipos#Precisión ilimitada: BigDecimal y BigInteger|ver BigDecimal]]).
>
> La explicación del 7.1 en el boletín dice que el resultado «es 55»: al ejecutarlo sale este `55.00000000000001`.

> [!note]- 🧠 Por qué funciona
> - `copy()` es como fotocopiar una ficha y corregir solo una casilla: la ficha original sigue igual y tienes una nueva con el cambio.
> - `keyboard == Product(1, "Teclado", 50.0, 8)` es `true` aunque sean **dos objetos distintos**, porque el `equals()` generado compara los datos. En una clase normal (sin `data`) daría `false`, porque compararía si son el mismo objeto.
> - `keyboard === updated` es `false`: `copy()` siempre crea un objeto nuevo.

---

## Ejercicio 2 · Desestructuración de `Employee`

> [!question] Enunciado
> Define una *data class* llamada `Employee` para gestionar los empleados de una empresa, con las propiedades `id`, `name`, `position` y `salary`.
>
> Implementa una función `main` que cree una instancia de `Employee` y después imprima los detalles del empleado (nombre y salario) utilizando el **operador de desestructuración** para extraer las propiedades de la instancia.

### Clases y métodos introducidos
- **Desestructuración**: `val (a, b, c, d) = objeto` crea varias variables de golpe, cada una con una propiedad del objeto, **por orden** (la primera variable recibe la primera propiedad del constructor, y así sucesivamente).
- `_`: «esta posición no me interesa». Sirve para saltarse propiedades sin crear una variable que no se va a usar.
- Por dentro, `val (a, b) = obj` llama a `obj.component1()` y `obj.component2()`, que la `data class` genera sola.

> **Términos explicados:** [[07 - POO II#Desestructuración|desestructuración]] · [[07 - POO II#Data class|`componentN()` en las data class]]

#### Ejemplo simple de funcionamiento
```kotlin
data class Book(val title: String, val pages: Int)

fun main() {
    val (title, pages) = Book("El Quijote", 1200)
    println("$title tiene $pages páginas")   // El Quijote tiene 1200 páginas
}
```

### Código fuente (`Ejercicio9.2/src/Main.kt`)

```kotlin
data class Employee(
    val id: Int,
    val name: String,
    val position: String,
    val salary: Double,
)

fun main() {
    val employee = Employee(1, "Ada Lovelace", "Programadora", 4200.0)

    // Desestructuración: cada variable recibe una propiedad, por orden.
    // _ descarta las que no necesitamos (id y position)
    val (_, name, _, salary) = employee

    println("Nombre: $name")
    println("Salario: $salary €")
}
```

### Explicación paso a paso
1. **La data class:** cuatro propiedades en este orden: `id` (1.ª), `name` (2.ª), `position` (3.ª) y `salary` (4.ª).
2. **Desestructuración:** `val (_, name, _, salary) = employee` va posición por posición:
	- 1.ª (`id`) → `_`, se descarta.
	- 2.ª (`name`) → variable `name`.
	- 3.ª (`position`) → `_`, se descarta.
	- 4.ª (`salary`) → variable `salary`.
3. **Salida:** se usan las dos variables nuevas como cualquier otra.

> [!tip] Prueba
> ```text
> Nombre: Ada Lovelace
> Salario: 4200.0 €
> ```

> [!note]- 🧠 Por qué funciona
> - La desestructuración va **por posición, no por nombre**. Si escribieras `val (name, salary) = employee`, `name` recibiría el `id` (1) y `salary` el `name` ("Ada Lovelace"). Los nombres de las variables los eliges tú; lo que cuenta es el orden.
> - Por eso hacen falta los `_`: marcan las posiciones que te saltas para que `salary` caiga en la cuarta.
> - Solo funciona con clases que tengan funciones `componentN()`. Las `data class` las generan; una clase normal no las tiene y no se podría desestructurar.

---

## Ejercicio 3 · Clase abstracta `Animal`

> [!question] Enunciado
> Define una **clase abstracta** llamada `Animal` para representar diferentes tipos de animales en un zoológico, con las siguientes propiedades y métodos:
>
> - Propiedad `name` (`String`): nombre del animal.
> - Propiedad `age` (`Int`): edad del animal.
> - Método abstracto `makeSound()`: debe ser implementado por las subclases para definir el sonido que hace el animal.
> - Método `info()`: debe imprimir el nombre y la edad del animal.
>
> Luego, define dos subclases concretas llamadas `Lion` y `Elephant` que hereden de `Animal` y proporcionen implementaciones para el método `makeSound()`.
>
> Implementa una función `main` que cree una instancia de `Lion` y otra de `Elephant`, y llame a `info()` y `makeSound()` para cada una.

### Clases y métodos introducidos
- `abstract class`: una clase **incompleta** que sirve de molde. No se pueden crear objetos de ella directamente, solo de sus subclases.
- `abstract fun makeSound()`: un método **sin cuerpo**. Cada subclase está **obligada** a implementarlo con `override`.
- Método normal (`info()`): con cuerpo, lo heredan todas las subclases sin tener que escribirlo otra vez.
- Las clases abstractas son `open` sin escribirlo: se puede heredar de ellas directamente.

> **Términos explicados:** [[07 - POO II#Clases abstractas|clases abstractas]] · [[06 - POO I#11. Herencia|herencia]] · [[06 - POO I#12. Sobrescribir métodos y propiedades|`override`]]

#### Ejemplo simple de funcionamiento
```kotlin
abstract class Shape {
    abstract fun area(): Double
}

class Square(val side: Double) : Shape() {
    override fun area(): Double = side * side
}

fun main() {
    println(Square(3.0).area())   // 9.0
    // Shape()                    // ERROR: no se puede instanciar una clase abstracta
}
```

### Código fuente (`Ejercicio9.3/src/Main.kt`)

```kotlin
abstract class Animal(val name: String, val age: Int) {
    // Sin cuerpo: cada subclase debe decir qué sonido hace
    abstract fun makeSound()

    // Con cuerpo: lo heredan todas las subclases tal cual
    fun info() {
        println("$name tiene $age años")
    }
}

class Lion(name: String, age: Int) : Animal(name, age) {
    override fun makeSound() {
        println("$name ruge: ¡Roaaar!")
    }
}

class Elephant(name: String, age: Int) : Animal(name, age) {
    override fun makeSound() {
        println("$name barrita: ¡Prrrú!")
    }
}

fun main() {
    val lion = Lion("Simba", 5)
    val elephant = Elephant("Dumbo", 12)

    lion.info()
    lion.makeSound()
    elephant.info()
    elephant.makeSound()
}
```

### Explicación paso a paso
1. **`Animal`:** recibe `name` y `age` como propiedades. Declara `makeSound()` como `abstract`, porque «un animal» en general no tiene un sonido concreto. `info()` sí tiene cuerpo, porque imprimir nombre y edad es igual para todos.
2. **`Lion` y `Elephant`:** heredan de `Animal` pasando `name` y `age` al constructor del padre. Cada una implementa `makeSound()` con `override` y su propio sonido.
3. **`info()` no se repite:** las subclases lo heredan tal cual. Solo escriben lo que las diferencia.
4. **`main()`:** crea un león y un elefante y llama a los dos métodos en cada uno.

> [!tip] Prueba
> ```text
> Simba tiene 5 años
> Simba ruge: ¡Roaaar!
> Dumbo tiene 12 años
> Dumbo barrita: ¡Prrrú!
> ```
> Si en `main()` intentas `Animal("X", 1)`, **no compila**. Error real de `kotlinc`: `cannot create an instance of an abstract class`.

> [!note]- 🧠 Por qué funciona
> - Una clase abstracta es como un formulario con un hueco obligatorio: `Animal` deja escrito lo común (`info()`) y deja en blanco `makeSound()`. Cada subclase tiene que rellenar ese hueco o no compila.
> - No se puede crear un `Animal` a secas porque le falta el cuerpo de `makeSound()`: si existiera, ¿qué haría al llamarlo?
> - A diferencia del [[Ejercicios Bloque 8#Ejercicio 2 · Jerarquía de empleados|Bloque 8]], aquí no hace falta poner `open`: las clases abstractas (y sus métodos abstractos) ya se pueden heredar y sobrescribir.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Data class | `data class P(val a: Int, …)` | Genera `toString`, `equals`/`hashCode`, `copy` y `componentN`. |
| Copia con cambios | `p.copy(price = 10.0)` | Objeto nuevo; lo no nombrado se copia igual. |
| Igualdad de datos | `a == b` | En data class compara los datos. |
| Mismo objeto | `a === b` | `true` solo si son el mismo objeto en memoria. |
| Desestructuración | `val (x, _, z) = p` | Por posición; `_` descarta una propiedad. |
| Clase abstracta | `abstract class A` | No se instancia; sirve de base. |
| Método abstracto | `abstract fun f()` | Sin cuerpo; las subclases deben hacer `override`. |
| Decimales en `Double` | `50.0 * 1.1` → `55.00000000000001` | Para mostrar, `"%.2f".format(x)`. |

## Relaciones

- Teoría: [[07 - POO II]] · [[06 - POO I]]
- Bloque anterior: [[Ejercicios Bloque 8]] · Bloque siguiente: [[Ejercicios Bloque 10]]
- Mismos enunciados en el boletín: [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.1 · Data class y método copy()|7.1]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.2 · Desestructuración de data class|7.2]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.4 · Clases abstractas|7.4]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Saber qué métodos genera una `data class`
- [ ] Crear un objeto modificado con `copy()` sin tocar el original
- [ ] Diferenciar `==` de `===`
- [ ] Desestructurar una data class saltándose propiedades con `_`
- [ ] Declarar una clase abstracta con un método abstracto y otro normal
- [ ] Explicar por qué `50.0 * 1.1` no da exactamente `55.0`
