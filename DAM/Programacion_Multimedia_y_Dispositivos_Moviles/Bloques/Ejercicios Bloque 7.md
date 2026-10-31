---
asignatura: PMDM
tema: 6
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/ejercicios
---

# Bloque 7 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[06 - POO I]] · [[04 - Estructuras básicas]]
> Bloque anterior: [[Ejercicios Bloque 6]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque07/`

> [!note] Sobre las soluciones
> - Los ejercicios 1 y 2 son los mismos enunciados que el 6.1 y el 6.2 de [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1|el boletín 6]].
> - **Ejercicio 1:** solución a partir de tu `Ejercicio6.2`, porque tu `Ejercicio6.1` rechaza un salario de 0 (ver el aviso del ejercicio).
> - **Ejercicio 2:** tu código de `Ejercicio6.2`, copiado tal cual.
> - **Ejercicio 3:** solución nueva; en tus proyectos del Tema 6 no había ningún `Product`.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque07/Ejercicio7.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Clase `Employee` con validación en `init`]]
- [[#Ejercicio 2 · Constructor secundario desde una cadena]]
- [[#Ejercicio 3 · Clase `Product` con descuento]]

---

## Ejercicio 1 · Clase `Employee` con validación en `init`

> [!question] Enunciado
> Define una clase en Kotlin llamada `Employee` que tenga las siguientes propiedades:
>
> - `firstName`: un valor no nulo de tipo `String`.
> - `lastName`: un valor no nulo de tipo `String`.
> - `salary`: un valor de tipo `Double` que debe ser mayor o igual a 0.
>
> El constructor primario debe aceptar los tres parámetros (`firstName`, `lastName` y `salary`). La clase debe incluir un bloque de inicialización (`init`) que verifique que `salary` es mayor o igual a 0. En caso contrario, debe lanzar una excepción `IllegalArgumentException` con el mensaje `Salary must be non-negative`.

### Clases y métodos introducidos
- **Constructor primario** con `val`: `class Employee(val firstName: String, …)` declara los parámetros del constructor **y** las propiedades a la vez. Sin `val`, serían solo parámetros y no se podría leer `employee.firstName` desde fuera.
- **Bloque `init`**: código que se ejecuta al crear el objeto, justo después del constructor primario. El constructor primario no puede tener código propio, así que las validaciones van aquí.
- `require(condición) { "mensaje" }`: si la condición es falsa, lanza `IllegalArgumentException` con ese mensaje. Es la forma corta de `if (!condición) throw IllegalArgumentException("mensaje")`.
- `try { … } catch (e: IllegalArgumentException) { … }`: captura la excepción para que el programa no termine.

> **Términos explicados:** [[06 - POO I#2. Constructor primario y bloques de inicialización|constructor primario e `init`]] · [[06 - POO I#5. Propiedades|propiedades]] · [[04 - Estructuras básicas#Validación con `require`, `check` y `error`|`require`]] · [[04 - Estructuras básicas#Capturar excepciones|`try-catch`]]

#### Ejemplo simple de funcionamiento
```kotlin
class Age(val years: Int) {
    init {
        require(years >= 0) { "Age must be non-negative" }
    }
}

fun main() {
    println(Age(20).years)   // 20
    Age(-1)                  // IllegalArgumentException: Age must be non-negative
}
```

### Código fuente (`Ejercicio7.1/src/Main.kt`)

```kotlin
class Employee(
    val firstName: String,
    val lastName: String,
    val salary: Double,
) {
    init {
        require(salary >= 0.0) { "Salary must be non-negative" }
    }
}

fun main() {
    val employee = Employee("Ada", "Lovelace", 4200.0)
    println("${employee.firstName} ${employee.lastName}: ${employee.salary}")

    val volunteer = Employee("Grace", "Hopper", 0.0)
    println("${volunteer.firstName} ${volunteer.lastName}: ${volunteer.salary}")

    try {
        Employee("Alan", "Turing", -5.0)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

### Explicación paso a paso
1. **Propiedades:** las tres van en el constructor primario con `val`. Son `String` y `Double` sin `?`, así que el compilador ya garantiza que no son `null`: eso cubre «valor no nulo» sin escribir nada más.
2. **Validación:** el bloque `init` se ejecuta en cuanto se crea el objeto. `require(salary >= 0.0)` deja pasar el 0 y los positivos; con un negativo lanza `IllegalArgumentException("Salary must be non-negative")`.
3. **Pruebas:** un empleado normal, el **caso límite** de salario 0 (que debe aceptarse) y un salario negativo, capturado con `try-catch` para mostrar el mensaje sin que el programa termine.

> [!tip] Prueba
> ```text
> Ada Lovelace: 4200.0
> Grace Hopper: 0.0
> Error: Salary must be non-negative
> ```

> [!note]- 🧠 Por qué funciona
> - El `init` forma parte de la construcción: si `require` lanza la excepción, **el objeto no llega a existir**. Es imposible tener un `Employee` con salario negativo.
> - Es como el control de una puerta: el objeto solo entra en el programa si pasa la validación.
> - En Java harías lo mismo dentro del constructor con `if (salary < 0) throw new IllegalArgumentException(...)`.

> [!warning] Tu proyecto `Ejercicio6.1`
> Tiene tres diferencias con el enunciado (comprobadas al ejecutarlo):
> 1. Usa `require(salary > 0)`, así que **`Employee("Daniel", "Madrid", 0.0)` lanza la excepción**, cuando el enunciado dice «mayor **o igual** a 0».
> 2. Los parámetros no llevan `val`, así que no son propiedades: `employee.salary` no compilaría.
> 3. Dentro del `require` hay un `throw`: `require(...) { throw IllegalArgumentException("…") }`. Funciona, pero sobra, porque `require` ya lanza la excepción; la lambda solo tiene que devolver el mensaje.
>
> Tu `Ejercicio6.2` ya lo tiene bien, y este ejercicio está hecho a partir de él.

---

## Ejercicio 2 · Constructor secundario desde una cadena

> [!question] Enunciado
> Agrega a la clase del ejercicio anterior un **constructor secundario** que acepte un único parámetro de tipo cadena con el formato `firstName-lastName-salary` y asigne cada valor a la propiedad correspondiente.

### Clases y métodos introducidos
- **Constructor secundario**: `constructor(text: String) : this(…)`. Se declara dentro del cuerpo de la clase y **tiene que llamar al primario** con `this(…)`.
- `String.split("-")`: parte la cadena por cada `-` y devuelve una lista: `"Ada-Lovelace-4200.0".split("-")` → `["Ada", "Lovelace", "4200.0"]`.
- `String.toDouble()`: convierte el trozo del salario a `Double`.

> **Términos explicados:** [[06 - POO I#4. Constructores secundarios|constructores secundarios]] · [[06 - POO I#2. Constructor primario y bloques de inicialización|constructor primario e `init`]] · [[02 - Jerarquia de tipos#6. Strings|`String`]]

#### Ejemplo simple de funcionamiento
```kotlin
class Point(val x: Int, val y: Int) {
    // "3,4" → Point(3, 4)
    constructor(text: String) : this(text.split(",")[0].toInt(), text.split(",")[1].toInt())
}

fun main() {
    val p = Point("3,4")
    println("${p.x}, ${p.y}")   // 3, 4
}
```

### Código fuente (`Ejercicio6.2/src/Main.kt`)

```kotlin
class Employee(
    val firstName: String,
    val lastName: String,
    val salary: Double,
) {
    init {
        require(salary >= 0.0) { "Salary must be non-negative" }
    }

    constructor(text: String): this(
        text.split("-")[0],
        text.split("-")[1],
        text.split("-")[2].toDouble(),
    )
}

fun main() {
    val employee = Employee("Ada-Lovelace-4200.0")
    println("${employee.firstName}, ${employee.lastName}, ${employee.salary}")
}
```

### Explicación paso a paso
1. **La clase del ejercicio 1** se mantiene igual: constructor primario con las tres propiedades y validación en `init`.
2. **Constructor secundario:** recibe un único `String`. No asigna las propiedades él mismo: las calcula y se las pasa al **primario** con `: this(…)`.
3. **Trocear la cadena:** `split("-")` separa por guiones. La posición `[0]` es el nombre, la `[1]` el apellido y la `[2]` el salario, convertido con `toDouble()`.
4. **La validación también se aplica:** como el secundario pasa por el primario, el `init` se ejecuta igual. Un salario negativo creado desde texto también se rechaza.
5. **`main()`:** crea el empleado desde `"Ada-Lovelace-4200.0"` e imprime sus tres propiedades.

> [!tip] Prueba
> ```text
> Ada, Lovelace, 4200.0
> ```

> [!note]- 🧠 Por qué funciona
> - En Kotlin, todo constructor secundario de una clase con constructor primario **debe delegar** en él (`: this(…)`). Así hay un único sitio donde se crean las propiedades y se valida, y no se puede saltar el `init`.
> - Los argumentos de `this(…)` se calculan **antes** de llamar al primario. Por eso no se puede declarar antes una variable con el resultado de `split` y hay que llamar a `split` en cada argumento.

> [!warning] Cadenas que rompen el formato (probadas)
> - **Salario negativo:** `"Alan-Turing--5.0"`. El `-` del número también es un separador: `split` da `["Alan", "Turing", "", "5.0"]`, y `"".toDouble()` lanza `NumberFormatException: empty String`. Con este formato no se puede escribir un salario negativo.
> - **Nombre con guion:** `"Jean-Paul-Sartre-100.0"` coge `"Sartre"` como salario y lanza `NumberFormatException`.
>
> Para un ejercicio de clase es suficiente; en un programa real se usaría un separador que no aparezca en los datos, como `;`.

---

## Ejercicio 3 · Clase `Product` con descuento

> [!question] Enunciado
> Define una clase en Kotlin llamada `Product` que tenga las siguientes propiedades:
>
> - `name`: un valor no nulo de tipo `String` que representa el nombre del producto.
> - `price`: un valor de tipo `Double` que representa el precio del producto y debe ser mayor o igual a 0. Se debe validar que el precio sea mayor o igual a 0; en caso contrario, debe lanzar una excepción `IllegalArgumentException` con el mensaje `Price must be non-negative`.
> - `discount`: un valor de tipo `Double` que representa el porcentaje de descuento aplicado al producto (debe estar entre 0 y 100). **El valor por defecto debe ser 0.** Se debe validar que esté en el rango de 0 a 100; en caso contrario, se debe lanzar una excepción `IllegalArgumentException` con el mensaje `Discount must be between 0 and 100`.
>
> Agrega a la clase los métodos:
>
> - `applyDiscount()`: aplica el descuento al precio actual del producto y actualiza el precio con el valor descontado.
> - `finalPrice()`: devuelve el precio final del producto después de aplicar el descuento.

### Clases y métodos introducidos
- **Argumento por defecto en el constructor**: `val discount: Double = 0.0`. Se puede crear `Product("Ratón", 20.0)` sin indicar el descuento.
- **Propiedad con setter personalizado**: `var price` se declara en el cuerpo de la clase con `set(value) { … field = value }`, para validar **cada vez** que cambie el precio. `field` es el valor guardado de la propiedad.
- `discount in 0.0..100.0`: comprueba con un rango que el descuento está entre 0 y 100, ambos incluidos.
- **Métodos**: funciones declaradas dentro de la clase, que trabajan con sus propiedades.

> **Términos explicados:** [[06 - POO I#6. Getters y setters personalizados|setter personalizado y `field`]] · [[06 - POO I#2. Constructor primario y bloques de inicialización|`init`]] · [[03 - Funciones#7. Argumentos por defecto|argumentos por defecto]] · [[02 - Jerarquia de tipos#4. Rangos y progresiones|rangos]]

#### Ejemplo simple de funcionamiento
```kotlin
class Thermostat(temperature: Int) {
    var temperature: Int = temperature
        set(value) {
            require(value in 10..30) { "Out of range" }
            field = value
        }
}

fun main() {
    val t = Thermostat(20)
    t.temperature = 25      // pasa por el setter: correcto
    t.temperature = 50      // IllegalArgumentException: Out of range
}
```

### Código fuente (`Ejercicio7.3/src/Main.kt`)

```kotlin
class Product(
    val name: String,
    price: Double,
    val discount: Double = 0.0,
) {
    // El setter valida cada cambio de precio posterior a la creación
    var price: Double = price
        set(value) {
            require(value >= 0.0) { "Price must be non-negative" }
            field = value
        }

    // El setter no se ejecuta al inicializar: validamos aquí los valores iniciales
    init {
        require(price >= 0.0) { "Price must be non-negative" }
        require(discount in 0.0..100.0) { "Discount must be between 0 and 100" }
    }

    // Precio con el descuento aplicado, sin modificar el producto
    fun finalPrice(): Double = price * (1 - discount / 100)

    // Actualiza el precio con el valor descontado
    fun applyDiscount() {
        price = finalPrice()
    }
}

fun main() {
    val laptop = Product("Portátil", 800.0, 25.0)
    println("${laptop.name}: precio ${laptop.price} € · precio final ${laptop.finalPrice()} €")
    laptop.applyDiscount()
    println("Tras aplicar el descuento: ${laptop.price} €")

    val mouse = Product("Ratón", 20.0)   // sin descuento: usa el valor por defecto 0
    println("${mouse.name}: precio final ${mouse.finalPrice()} €")

    try {
        Product("Teclado", -10.0)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    try {
        Product("Monitor", 150.0, 120.0)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    try {
        laptop.price = -1.0
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

### Explicación paso a paso
1. **`name` y `discount`** van en el constructor con `val`: no cambian nunca. `discount` tiene el valor por defecto `0.0`, como pide el enunciado.
2. **`price` es distinto:** `applyDiscount()` tiene que poder cambiarlo, así que es `var`. En el constructor va **sin** `val` (solo como parámetro) y la propiedad se declara en el cuerpo, porque así se le puede poner un **setter** que valide.
3. **Setter:** cada vez que se asigna un precio nuevo (`price = …`), se ejecuta `set(value)`. Si `value` es negativo, `require` lanza la excepción; si no, `field = value` lo guarda.
4. **`init`:** el setter **no** se ejecuta al dar el valor inicial (`= price`), así que el precio inicial y el descuento se validan aquí. El descuento se comprueba con el rango `0.0..100.0`.
5. **`finalPrice()`:** calcula `precio × (1 − descuento / 100)`. Con un 25 %: `800 × 0.75 = 600`. Solo calcula y **no cambia** el producto.
6. **`applyDiscount()`:** guarda en `price` el resultado de `finalPrice()`. Al asignarlo, pasa por el setter, que comprueba que no sea negativo.
7. **Pruebas:** precio y descuento normales, el descuento por defecto, un precio negativo, un descuento de 120 y un cambio de precio negativo **después** de crear el producto.

> [!tip] Prueba
> ```text
> Portátil: precio 800.0 € · precio final 600.0 €
> Tras aplicar el descuento: 600.0 €
> Ratón: precio final 20.0 €
> Error: Price must be non-negative
> Error: Discount must be between 0 and 100
> Error: Price must be non-negative
> ```
> El último error es `laptop.price = -1.0`: el setter también protege los cambios posteriores.

> [!note]- 🧠 Por qué funciona
> - Hay **dos momentos** en que el precio puede quedar mal: al crear el producto y al cambiarlo después. El `init` vigila el primero y el setter el segundo. Si solo validaras en `init`, `laptop.price = -1.0` se aceptaría.
> - `finalPrice()` y `applyDiscount()` reparten el trabajo: una **consulta** (calcula sin tocar nada) y una **acción** (modifica el objeto). `applyDiscount()` reutiliza `finalPrice()` para no repetir la fórmula.
> - Dentro de `init`, `price` se refiere al **parámetro** del constructor, que tiene el mismo valor que la propiedad recién inicializada.

> [!warning] `applyDiscount()` dos veces
> El descuento no se «gasta»: si llamas a `applyDiscount()` dos veces, el precio baja dos veces (800 → 600 → 450). Además, después de aplicarlo, `finalPrice()` vuelve a descontar sobre el precio ya rebajado. Así lo pide el enunciado («aplica el descuento al precio **actual**»), pero conviene saberlo si te preguntan por ello.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Propiedad en el constructor | `class A(val x: Int)` | Parámetro y propiedad a la vez; sin `val` solo es parámetro. |
| Bloque de inicialización | `init { … }` | Se ejecuta al crear el objeto; aquí van las validaciones. |
| Validar argumentos | `require(cond) { "msg" }` | Lanza `IllegalArgumentException("msg")` si `cond` es falsa. |
| Constructor secundario | `constructor(t: String) : this(…)` | Debe delegar en el primario; el `init` se ejecuta igual. |
| Trocear texto | `"a-b-c".split("-")` | Lista `["a", "b", "c"]`. |
| Setter personalizado | `var p = x; set(v) { …; field = v }` | Valida cada asignación posterior; no se ejecuta al inicializar. |
| Valor por defecto | `val discount: Double = 0.0` | Se puede omitir al crear el objeto. |
| Rango de validación | `x in 0.0..100.0` | Comprueba los dos límites a la vez, incluidos. |

## Relaciones

- Teoría: [[06 - POO I]] · [[04 - Estructuras básicas]]
- Bloque anterior: [[Ejercicios Bloque 6]] · Bloque siguiente: [[Ejercicios Bloque 8]]
- Mismos enunciados en el boletín: [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1#Ejercicio 6.1 · Validar salario en `init`|6.1]] · [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1#Ejercicio 6.2 · Constructor secundario desde una cadena|6.2]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Declarar propiedades en el constructor primario con `val`/`var`
- [ ] Validar en `init` con `require`
- [ ] Escribir un constructor secundario que delegue con `this(…)`
- [ ] Explicar por qué el setter no se ejecuta al inicializar la propiedad
- [ ] Separar un método de consulta (`finalPrice`) de uno que modifica (`applyDiscount`)
