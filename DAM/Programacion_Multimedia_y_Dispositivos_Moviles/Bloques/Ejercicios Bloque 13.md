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

# Bloque 13 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[08 - POO III]] · [[06 - POO I]] · [[07 - POO II]]
> Bloque anterior: [[Ejercicios Bloque 12]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque13/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 8.7, 8.10 y 8.11 de [[08.1 - Ejercicios 8 POO III|el boletín 8]]. El código parte de esas soluciones, con más pruebas.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque13/Ejercicio13.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas y los mensajes de error son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Sobrecarga del operador `+` en `ComplexNumber`]]
- [[#Ejercicio 2 · Conexión perezosa con `by lazy`]]
- [[#Ejercicio 3 · Singleton perezoso `Database`]]

---

## Ejercicio 1 · Sobrecarga del operador `+` en `ComplexNumber`

> [!question] Enunciado
> Define una clase llamada `ComplexNumber` para representar números complejos. Cada número complejo consta de una parte real y una parte imaginaria: en la representación `a + bi`, `a` es la parte real y `b` la parte imaginaria (`i` es una constante que debe acompañar a la parte imaginaria).
>
> Sobrecarga en la clase `ComplexNumber` el operador `+` para sumar dos números complejos, con la fórmula:
>
> $$(a + bi) + (c + di) = (a + c) + (b + d)i$$

### Clases y métodos introducidos
- **Sobrecarga de operadores**: en Kotlin, `a + b` se traduce a la llamada `a.plus(b)`. Si una clase define un método `plus` marcado con `operator`, sus objetos se pueden sumar con `+`.
- `operator fun plus(other: ComplexNumber): ComplexNumber`: recibe el número de la derecha del `+` y devuelve el resultado.
- `+=` sale gratis: si existe `plus`, `x += y` se traduce a `x = x + y` (con `x` declarada como `var`).
- `override fun toString()`: cambia cómo se imprime el objeto, para que salga `3.0 + 2.0i`.

> **Términos explicados:** [[08 - POO III#7. Sobrecarga de operadores|sobrecarga de operadores]] · [[07 - POO II#Data class|`data class`]] · [[06 - POO I#12. Sobrescribir métodos y propiedades|`override`]]

#### Ejemplo simple de funcionamiento
```kotlin
data class Money(val euros: Int) {
    operator fun plus(other: Money) = Money(euros + other.euros)
}

fun main() {
    println(Money(5) + Money(3))   // Money(euros=8)
}
```

### Código fuente (`Ejercicio13.1/src/Main.kt`)

```kotlin
data class ComplexNumber(val real: Double, val imaginary: Double) {

    // (a + bi) + (c + di) = (a + c) + (b + d)i
    operator fun plus(other: ComplexNumber): ComplexNumber =
        ComplexNumber(real + other.real, imaginary + other.imaginary)

    // Formato a + bi (o a - bi si la parte imaginaria es negativa)
    override fun toString(): String =
        if (imaginary >= 0) "$real + ${imaginary}i" else "$real - ${-imaginary}i"
}

fun main() {
    val a = ComplexNumber(3.0, 2.0)
    val b = ComplexNumber(1.5, -4.0)
    val sum = a + b    // equivale a a.plus(b)
    println("($a) + ($b) = $sum")
    println("a sigue valiendo: $a")

    // += también funciona: se traduce a total = total + b
    var total = ComplexNumber(0.0, 0.0)
    total += a
    total += b
    total += ComplexNumber(1.0, 1.0)
    println("Suma acumulada: $total")
}
```

### Explicación paso a paso
1. **La clase:** guarda `real` (`a`) e `imaginary` (`b`) como `Double`. Es `data class` para tener `equals` y `copy` gratis; con una clase normal, la suma funcionaría igual.
2. **`plus`:** aplica la fórmula del enunciado, sumando las partes reales por un lado y las imaginarias por otro. Devuelve un número **nuevo**: `a` y `b` no cambian.
3. **`operator`:** sin esta palabra, `plus` sería un método normal y `a + b` no compilaría.
4. **`toString()`:** sobrescribe el de la `data class` para mostrar el formato matemático. Si la parte imaginaria es negativa, escribe `- 4.0i` en vez de `+ -4.0i`.
5. **Pruebas:** una suma con parte imaginaria negativa, la comprobación de que `a` no ha cambiado y una suma acumulada con `+=`.

> [!tip] Prueba
> ```text
> (3.0 + 2.0i) + (1.5 - 4.0i) = 4.5 - 2.0i
> a sigue valiendo: 3.0 + 2.0i
> Suma acumulada: 5.5 - 1.0i
> ```
> Suma acumulada: reales 3 + 1,5 + 1 = 5,5; imaginarias 2 − 4 + 1 = −1.

> [!note]- 🧠 Por qué funciona
> - `+` es como una «puerta» que Kotlin traduce a `plus`. Al escribir `operator fun plus`, le dices a Kotlin qué hay detrás de esa puerta para tus objetos.
> - En Java no se pueden sobrecargar operadores: tendrías que escribir `a.plus(b)` siempre. Kotlin solo deja sobrecargar los operadores de su tabla, cada uno con su nombre fijo (`plus`, `minus`, `times`…).
> - `total += a` funciona aunque no se haya definido `plusAssign`: como `total` es `var`, Kotlin lo convierte en `total = total.plus(a)`.

---

## Ejercicio 2 · Conexión perezosa con `by lazy`

> [!question] Enunciado
> Define una clase `Database` que represente una conexión a una base de datos. La clase debe tener una propiedad `connection` que se **inicialice perezosamente**. La inicialización de `connection` debe simular una conexión a la base de datos imprimiendo un mensaje en la consola.
>
> La clase también debe tener un método `executeQuery(query: String)` que imprima la consulta recibida y después el estado de la conexión.
>
> Demuestra el uso de la clase `Database` en una función `main`, ejecutando varias consultas.

### Clases y métodos introducidos
- **Inicialización perezosa** (*lazy*): el valor no se calcula al crear el objeto, sino **la primera vez que se lee** la propiedad. Las siguientes lecturas devuelven el valor guardado, sin volver a calcularlo.
- `val connection: String by lazy { … }`: la propiedad **delega** en `lazy`. La lambda se ejecuta una sola vez y lo que devuelve (su última expresión) es el valor de la propiedad.
- Solo sirve con `val`: comprobado con el compilador, `var x: String by lazy { … }` no compila.

> **Términos explicados:** [[08 - POO III#11. Inicialización perezosa con lazy|`lazy`]] · [[08 - POO III#12. lazy vs. lateinit|`lazy` vs `lateinit`]] · [[10 - Programación funcional#5. Expresiones lambda|lambdas]]

#### Ejemplo simple de funcionamiento
```kotlin
class Report {
    val data: String by lazy {
        println("Calculando…")       // solo se imprime una vez
        "Resultado"
    }
}

fun main() {
    val report = Report()
    println(report.data)   // Calculando…  /  Resultado
    println(report.data)   // Resultado (ya no recalcula)
}
```

### Código fuente (`Ejercicio13.2/src/Main.kt`)

```kotlin
class Database {
    // La lambda solo se ejecuta la primera vez que se lee connection
    val connection: String by lazy {
        println(">> Conectando con la base de datos...")
        "Conexión activa"
    }

    fun executeQuery(query: String) {
        println("Ejecutando: $query")
        println("Estado de la conexión: $connection")
    }
}

fun main() {
    val database = Database()
    println("Objeto Database creado (todavía sin conexión)")

    database.executeQuery("SELECT * FROM users")
    database.executeQuery("SELECT * FROM products")
    database.executeQuery("DELETE FROM logs")
}
```

### Explicación paso a paso
1. **`connection`:** es `val` y delega en `lazy`. La lambda simula la conexión: imprime un mensaje y devuelve `"Conexión activa"`, que pasa a ser el valor de la propiedad.
2. **Crear el objeto no conecta:** `Database()` no ejecuta la lambda. Por eso «Objeto Database creado» sale **antes** que el mensaje de conexión.
3. **Primera consulta:** al imprimir el estado se lee `connection` por primera vez. Entonces se ejecuta la lambda y aparece `>> Conectando…`.
4. **Consultas siguientes:** `connection` ya tiene valor y se devuelve directamente. El mensaje de conexión **no se repite**.

> [!tip] Prueba
> ```text
> Objeto Database creado (todavía sin conexión)
> Ejecutando: SELECT * FROM users
> >> Conectando con la base de datos...
> Estado de la conexión: Conexión activa
> Ejecutando: SELECT * FROM products
> Estado de la conexión: Conexión activa
> Ejecutando: DELETE FROM logs
> Estado de la conexión: Conexión activa
> ```
> Si se declara `var connection: String by lazy { … }`, **no compila**. Error real de `kotlinc`: `type 'Lazy<String>' has no method 'setValue(…)', so it cannot serve as a delegate for var (read-write property)`.

> [!note]- 🧠 Por qué funciona
> - `lazy` es como encender la calefacción solo cuando entras en casa, y no nada más comprarla. Si nunca entras (nunca lees `connection`), nunca se enciende; y una vez encendida, se queda así.
> - Conectar a una base de datos es lento. Con `lazy`, si el programa nunca hace una consulta, no pierde tiempo conectando.
> - Fíjate en el **orden** de la salida: `Ejecutando: …` aparece antes que `>> Conectando…`. La lambda no se ejecuta al empezar `executeQuery`, sino justo en la línea donde se lee `connection`.

---

## Ejercicio 3 · Singleton perezoso `Database`

> [!question] Enunciado
> Crea una clase `Database` que implemente el **patrón Singleton** en Kotlin, donde la construcción del objeto se haga de forma perezosa usando `by lazy`. El constructor de la clase recibe como argumento una cadena con la URL de la base de datos.
>
> Además, la clase dispone del método `conectar()`, que imprime un mensaje indicando que se está conectando a la base de datos con la URL proporcionada, y del método `desconectar()`, que imprime un mensaje indicando que se está desconectando de esa URL.
>
> En la función `main`, crea dos variables que correspondan a la instancia singleton de dicha clase y llama a los métodos `conectar()` y `desconectar()`. Además, comprueba que ambas variables referencian el mismo objeto usando el operador `===`.

### Clases y métodos introducidos
- **Patrón Singleton**: garantiza que de una clase solo exista **un objeto** en todo el programa.
- `private constructor`: nadie de fuera de la clase puede hacer `Database("…")`. Así se impide crear más objetos.
- `companion object` con `val instance by lazy { … }`: la única puerta de entrada al objeto. Se crea la primera vez que alguien lo pide y después siempre se devuelve el mismo.
- `===`: comprueba si dos variables apuntan **al mismo objeto** en memoria.

> **Términos explicados:** [[08 - POO III#11. Inicialización perezosa con lazy|`lazy`]] · [[06 - POO I#17. Objetos compañeros|`companion object`]] · [[06 - POO I#15. Modificadores de visibilidad|constructor `private`]] · [[06 - POO I#16. Declaraciones de objetos|`object` (singleton sin parámetros)]]

#### Ejemplo simple de funcionamiento
```kotlin
class Printer private constructor() {
    companion object {
        val instance: Printer by lazy { Printer() }
    }
}

fun main() {
    println(Printer.instance === Printer.instance)   // true
    // Printer()                                     // ERROR: constructor privado
}
```

### Código fuente (`Ejercicio13.3/src/Main.kt`)

```kotlin
// Constructor privado: desde fuera no se puede hacer Database("...")
class Database private constructor(private val url: String) {

    fun conectar() {
        println("Conectando a la base de datos en $url")
    }

    fun desconectar() {
        println("Desconectando de la base de datos en $url")
    }

    companion object {
        private const val DEFAULT_URL = "jdbc:mysql://localhost:3306/dam"

        // Única instancia: se construye la primera vez que alguien la pide
        val instance: Database by lazy {
            println(">> Creando la única instancia de Database")
            Database(DEFAULT_URL)
        }
    }
}

fun main() {
    println("Inicio del programa (la instancia aún no existe)")

    val db1 = Database.instance
    val db2 = Database.instance

    db1.conectar()
    db2.desconectar()

    // === compara referencias: ¿apuntan al mismo objeto en memoria?
    println("¿db1 y db2 son el mismo objeto? ${db1 === db2}")
}
```

### Explicación paso a paso
1. **Constructor privado:** recibe la URL, como pide el enunciado, pero solo se puede llamar **desde dentro** de la clase (incluido su `companion object`).
2. **`instance`:** está en el `companion object`, así que se usa como `Database.instance`. Con `by lazy`, el objeto se crea la primera vez que se pide.
3. **La URL:** la lambda de `lazy` no recibe parámetros, así que la URL se define como constante privada (`DEFAULT_URL`) y se pasa al constructor desde dentro.
4. **`main()`:** «Inicio del programa» sale **antes** que `>> Creando…`: la instancia no existe hasta que `db1` la pide. `db2` recibe el mismo objeto, sin crear otro.
5. **`===`:** confirma que `db1` y `db2` son el mismo objeto (`true`). Por eso `desconectar()` con `db2` usa la misma URL que `conectar()` con `db1`.

> [!tip] Prueba
> ```text
> Inicio del programa (la instancia aún no existe)
> >> Creando la única instancia de Database
> Conectando a la base de datos en jdbc:mysql://localhost:3306/dam
> Desconectando de la base de datos en jdbc:mysql://localhost:3306/dam
> ¿db1 y db2 son el mismo objeto? true
> ```
> Si desde `main()` se intenta `Database("jdbc:otra")`, **no compila**. Error real de `kotlinc`: `cannot access 'constructor(url: String): Database': it is private in 'Database'`.

> [!note]- 🧠 Por qué funciona
> - Es como el director de un instituto: solo hay uno, y cuando alguien pregunta por él siempre le presentan **al mismo**. El constructor privado es la norma que impide «nombrar» otro director desde fuera.
> - `lazy` guarda el objeto la primera vez y después lo devuelve siempre. Eso es justo lo que necesita un singleton: crear uno y reutilizarlo.
> - El mensaje `>> Creando…` sale **una sola vez** aunque se pida la instancia dos veces. Es la prueba de que el segundo acceso no ha creado nada.

> [!warning] ¿Por qué no `object Database`?
> En el [[Ejercicios Bloque 8#Ejercicio 4 · Singleton `ConfigurationManager`|Bloque 8]] se hizo un singleton con `object`, que es la forma más sencilla en Kotlin. Pero un `object` **no puede tener constructor con parámetros**, y este enunciado pide que el constructor reciba la URL. Por eso aquí se usa una clase con constructor privado y `by lazy`.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Sobrecargar `+` | `operator fun plus(o: T): T` | `a + b` se traduce a `a.plus(b)`. |
| `+=` con `plus` | `var x …; x += y` | Se traduce a `x = x + y`. |
| Cambiar cómo se imprime | `override fun toString()` | `println(obj)` usa este texto. |
| Inicialización perezosa | `val p: T by lazy { … }` | La lambda se ejecuta en la primera lectura; después se reutiliza el valor. |
| `lazy` solo con `val` | `var p by lazy` → error | `Lazy` no tiene `setValue`. |
| Constructor privado | `class A private constructor(…)` | Nadie de fuera puede crear objetos. |
| Singleton perezoso | `companion object { val instance by lazy { A(…) } }` | Un único objeto, creado cuando se pide. |
| Misma referencia | `a === b` | `true` si son el mismo objeto. |

## Relaciones

- Teoría: [[08 - POO III]] · [[06 - POO I]] · [[07 - POO II]]
- Bloque anterior: [[Ejercicios Bloque 12]] · Bloque siguiente: [[Ejercicios Bloque 14]]
- Mismos enunciados en el boletín: [[08.1 - Ejercicios 8 POO III#Ejercicio 8.7 · Sobrecarga del operador + en ComplexNumber|8.7]] · [[08.1 - Ejercicios 8 POO III#Ejercicio 8.10 · Conexión perezosa con lazy|8.10]] · [[08.1 - Ejercicios 8 POO III#Ejercicio 8.11 · Singleton perezoso con by lazy|8.11]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Sobrecargar un operador con `operator fun` y saber a qué método se traduce
- [ ] Explicar por qué `+=` funciona aunque solo exista `plus`
- [ ] Declarar una propiedad `by lazy` y saber cuándo se ejecuta su lambda
- [ ] Explicar por qué `lazy` solo sirve con `val`
- [ ] Implementar un singleton con constructor privado y `by lazy`
- [ ] Saber cuándo basta con `object` y cuándo hace falta un singleton con constructor
