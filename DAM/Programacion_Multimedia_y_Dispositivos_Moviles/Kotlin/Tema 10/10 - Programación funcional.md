---
asignatura: PMDM
tema: 10
tipo: tema
estado: completo
fecha: 2026-10-25
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-programacion-funcional
---

# 10 · Programación funcional en Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 10 · Kotlin  
> Ejercicios: [[10.1 - Ejercicios 10 Programación funcional]] · Tema anterior: [[09 - Genéricos]]

> [!info] Material de referencia
> [Programación funcional en Kotlin](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b10%20-%20Programacion%20funcional%20en%20Kotlin/)

## Índice del tema

- [[#1. Tipos función]]
- [[#2. Varianza en los tipos función]]
- [[#3. typealias]]
- [[#4. Instanciación de objetos de tipo función]]
- [[#5. Expresiones lambda]]
- [[#6. Conversión SAM]]
- [[#7. Interfaz fun interface]]
- [[#8. Funciones anónimas]]
- [[#9. Closures]]
- [[#10. Referencias a función]]
- [[#11. Inline functions]]
- [[#12. Literales de función con receptor (lambda with receiver)]]
- [[#13. Scoping functions (with, run, apply, let, also)]]
	- [[#13.1 with()]]
	- [[#13.2 T.run()]]
	- [[#13.3 T.apply()]]
	- [[#13.4 T.let()]]
	- [[#13.5 T.also()]]

---

## 1. Tipos función

En Kotlin las funciones son tratadas como ciudadanos de primera clase (_first-class citizens_), es decir, como si de cualquier otro objeto se tratara. Esto implica que **una función puede ser**:

- **almacenada en una variable** o en una estructura de datos,
- **pasada como argumento** de un parámetro de otra función,
- **retornada** por otras funciones.

Si una función es un objeto, entonces necesitamos un tipo que represente a dicha clase de objetos. Un **tipo función es un tipo que especifica que un objeto tiene que ser una función**. Sin embargo, no un único tipo función, ya que hay múltiples combinaciones de número de parámetros, tipos de los parámetros y tipos de retorno, es decir múltiples firmas.

Para facilitarnos la tarea de definir un tipo función, Kotlin nos proporciona una **sintaxis concreta** para indicar que el tipo de una variable, de un parámetro o de retorno de una función corresponde a funciones con una determinada firma.

Esta sintaxis tiene la forma : **`(tipoParam1, tipoParam2, ...) -> TipoRetorno`**. Si queremos referirnos a un tipo en el que la función que no recibe ningún parámetro, usaremos `() -> TipoRetorno`. El tipo de retorno de la función NO se puede omitir, incluso si se trata del tipo `Unit`. Veamos un ejemplo:

**Función con parámetro de tipo función**

```kotlin
fun operate(
    x: Int, 
    y: Int, 
    action: (Int, Int) -> Int // Tipo función que recibe dos enteros y retorna un entero
): Int {
    val result = action(x, y) // Invocación del parámetro de tipo función
    println("Result: ${result}")
    return result
}

fun main() {
    operate(8, 2, {x, y -> x + y})
    operate(8, 2, {x, y -> x - y})
    operate(8, 2, {x, y -> x / y})
    operate(8, 2, {x, y -> x * y})
}
```

Aunque no es necesario, la notación para definir un tipo de función **puede incluir también nombres para los parámetros**, lo que puede servir **para documentar** el significado de los mismos. Por ejemplo: `(x: Int, y: Int) -> Int`. Estos nombres en realidad son tan solo una conveniencia para los desarrolladores, ya que el IDE nos los mostrará en sus sugerencias, aunque en realidad no son necesarios desde un punto de vista técnico. En general, se considera una buena práctica usarlos cuando el significado de los parámetros no esté claro.

Si queremos especificar un **tipo de función _nullable_ debemos usar paréntesis**. Por ejemplo `((Int, Int) -> Int)?`. El tipo de la función puede ser aun más complejo, ya que pueden combinarse usando paréntesis. Por ejemplo, el siguiente tipo corresponde a una función que recibe un entero y que retorna una función que recibe un entero y no retornada nada: `(Int) -> ((Int) -> Unit)` (por defecto el operador `->` tiene asociatividad a la derecha). Además, NO existe una forma de indicar que uno de los parámetros de un tipo función sea opcional.

**Internamente**, los tipos función son **compilados a interfaces funcionales parametrizadas**, aunque a diferencia de en Java, esto es transparente para el desarrollador. Todas estas interfaces tienen definidas el **método `invoke()` correspondiente al operador de `()` de llamada a una función**.

Por ejemplo, cualquier tipo función que recibe dos parámetros y retorna algo se compila hacia una interfaz funcional en _bytecode_ cuya representación en Kotlin sería similar a ésta:

**Representación en Kotlin de una interfaz funcional equivalente a un tipo función que reciba dos parámetros y retorne algo**

```kotlin
/* La comentamos porque esta interfaz ya existe en Kotlin, y daría error
interface Function2<in P1, in P2, out R> {
    operator fun invoke(p1: P1, p2: P2): R
}
*/

fun operate(
    x: Int, 
    y: Int, 
    action: Function2<Int, Int, Int> // Interfaz equivalente al tipo función que recibe dos enteros y retorna un entero
): Int {
    val result = action(x, y) // Invocación del parámetro de tipo función
    println("Result: ${result}")
    return result
}

fun main() {
    operate(8, 2, {x, y -> x + y})
    operate(8, 2, {x, y -> x - y})
    operate(8, 2, {x, y -> x / y})
    operate(8, 2, {x, y -> x * y})
}
```

Así, para un tipo función `(Int) -> String` en el _bytecode_ se generaría una intefaz funcional equivalente `Function1<Int, String>`.

Al definir un tipo de función también podemos hacer uso de los parámetros de tipo de una función parametrizada, como vemos en el ejemplo inicial.

> [!note] Comparación con Java
> En Java no hay tipos función: una lambda siempre implementa una interfaz funcional (`Function<T, R>`, `BiFunction<T, U, R>`, `Runnable`…) y se ejecuta con su método (`apply()`, `run()`…). En Kotlin escribimos directamente `(Int, Int) -> Int` y la llamamos con `()` como si fuera una función normal.

**Para ejecutar una instancia de un tipo función que esté almacenada en una variable o parámetro usaremos su método `invoke()` o simplemente a través del operador `()`, pasándole tantos argumentos como parámetros disponga**. Por ejemplo si en una variable `f` tenemos almacenada una instancia de un tipo función `(Int) -> Unit`, podemos invocar a dicho código haciendo `f.invoke(x)` o `f(x)`, siendo `x` una expresión de tipo `Int`.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.1 · Función de orden superior testBoth con lambdas|Ejercicio 10.1 · Función de orden superior testBoth con lambdas]]

[Explicación en video](https://www.youtube.com/embed/mPLG5MBoTi0)

## 2. Varianza en los tipos función

En un tipo función, como por ejemplo `(Int) -> Any`, como era de esperar, **los tipos correspondientes a los parámetros son contravariantes** (`in`), ya que se tratan de tipos de entrada, lo que implica que podemos pasar cualquier supertipo del especificado, **mientras que el tipo de retorno es covariante** (`out`), ya que se trata de un tipo de salida, lo que implica que podemos retornar cualquier subtipo del especificado.

Así, como argumento de un tipo función como el anterior, podemos pasar una función con por ejemplo las firmas `(Int) -> Number`, `(Number) -> Any`, `(Number) -> Number`, `(Any) -> Number` y `(Number) -> Int`.

**Varianza en los tipos función**

```kotlin
fun printProcessedNumber(transformation: (Int) -> Any) { 
    println(transformation(42))
}

fun main() {
    val intToDouble: (Int) -> Number = { it.toDouble() }
    val numberAsText: (Number) -> String = { it.toString() }
    printProcessedNumber(intToDouble)
    printProcessedNumber(numberAsText)
}
```

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.2 · Varianza en tipos función con Message, Email y SMS|Ejercicio 10.2 · Varianza en tipos función con Message, Email y SMS]]

## 3. typealias

Si queremos tener un nombre más significativo para el tipo de la función podemos definir un **alias de tipo (_typealias_)** para darle un nombre alternativo mucho más sencillo de entender. Por ejemplo, el siguiente código define el nombre ClickHandler para un tipo de función que recibe dos parámetros, uno de tipo `Button` y otro de tipo `ClickEvent`, y que no retorna nada:

**typealias**

```kotlin
typealias IntBinaryOperation = (Int, Int) -> Int

fun operate(
    x: Int, 
    y: Int, 
    action: IntBinaryOperation // typealias para tipo función que recibe dos enteros y retorna un entero
): Int {
    val result = action(x, y) // Invocación del parámetro de tipo función
    println("Result: ${result}")
    return result
}

fun main() {
    operate(8, 2, {x, y -> x + y})
    operate(8, 2, {x, y -> x - y})
    operate(8, 2, {x, y -> x / y})
    operate(8, 2, {x, y -> x * y})
}
```

> [!warning] Aviso
> **Un _typealias_ NO define ningún tipo**, es tan solo un nuevo nombre que se le da a un tipo existente. De hecho, **durante la compilación los _typealias_ son reemplazados por el tipo real** correspondiente.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.3 · typealias MathOperation y función que devuelve función|Ejercicio 10.3 · typealias MathOperation y función que devuelve función]]

## 4. Instanciación de objetos de tipo función

Kotlin presenta varias formas de proporcionar una instancia de un tipo función:

- Mediante un literal en forma de expresión lambda.
- Mediante un literal en forma de expresión de función anónima.
- Mediante una referencia a función.
- Usando una instancia de una clase que implemente un determinado tipo función como interfaz.

Veamos un ejemplo:

**Instanciación de objetos de tipo función**

```kotlin
fun <T> operate(x: T, y: T, action: (T, T) -> T): T = action(x, y)

fun add(x: Int, y: Int): Int = x + y

val adding = fun(x: Int, y: Int): Int = x + y

class SumOperator: (Int, Int) -> Int {
    override operator fun invoke(x: Int, y: Int): Int = x + y
}

fun main() {
    val result1 = operate(5, 8) { x, y -> x + y } // Lambda
    val result2 = operate(5, 8, ::add) // Referencia a función top-level
    val result3 = operate(5, 8, Integer::sum) // Referencia a método estático
    val result4 = operate(5, 8, adding) // Función anónima
    val result5 = operate(5, 8, SumOperator())
    println("result1 vale $result1")
    println("result2 vale $result2")
    println("result3 vale $result3")
    println("result4 vale $result4")
    println("result5 vale $result5")
}
```

[Explicación en video](https://www.youtube.com/embed/7jHgfPMkD3Y)

## 5. Expresiones lambda

Una expresión _lambda_ es una expresión para crear un objeto que representa una función, a lo que se conoce como **literal función**. En Kotlin, las expresiones _lambda_ de Kotlin tienen la siguiente sintaxis: `{ params -> cuerpo }`. Como vemos se trata de una sintaxis diferente a la de las lambdas de Java 8.

> [!definition] Lambda
> Una _lambda_ es una subrutina definida, que no está identificada por ningún identificador. Dicha subrutina puede definir parámetros y retornar un valor.

> [!warning] Cuidado
> **En Kotlin todas las llaves que no formen parte de una estructura son expresiones lambdas (a diferencia de en Java, que indican un bloque de instrucciones). Así, en el siguiente ejemplo NO se está definiendo un bloque, sino una lambda:**

```kotlin
fun main() {
    {
        println("AAA")
    }
    println("Lo anterior es la definición de una lambda que no se está ejecutando")
}
```

Para ejecutar una lambda podemos usar el método `invoke(args)` sobre una variable que la referencie, o simplemente usar el operador `(args)` sobre dicha variable, ya que dicho operador en realidad corresponde a una llamada al método anterior. Veamos un ejemplo:

**Expresión lambda**

```kotlin
fun main() {
    // La variable sum referenciará una expresión lambda
    val sum: (Int, Int) -> Int = { x, y -> x + y }
    // Podemos ejecutar la expresión lambda a través de la variable sum 
    // usando el operador ()
    println(sum(1, 2))
    // En realidad el operador () usa el método invoke() de los "tipos función"
    println(sum.invoke(1, 2))
}
```

> [!warning] Aviso
> A diferencia de en Java, **en Kotlin las _lambdas_ se deben definir entre llaves, y su lista de parámetros NO usa paréntesis, aunque tenga varios**.

Aunque una _lambda_ puede ser referenciada por una variable, **lo más frecuente es declarar la expresión _lambda_ directamente a la hora de pasarla a la función**.

En el siguiente ejemplo vemos cómo pasar una expresión _lambda_ al método `maxByOrNull()` de una colección, que retorna el elemento mayor atendiendo al valor retornado cuando se pasa cada elemento al código suministrado a través de la expresión _lambda_, o `null` si la colección está vacía:

**Uso inline de una expresión lambda**

```kotlin
data class Student(val name: String, val age: Int)

fun main() {
    val students = listOf(Student("Alice", 29), Student("Bob", 27))
    // Estudiante de mayor edad
    val maxAgeStudent = students.maxByOrNull({ student: Student -> student.age })
    // Estudante con el nombre mayor según orden alfabético.
    val maxNameStudent = students.maxByOrNull({ student: Student -> student.name })
    println("Estudiante con mayor edad: ${maxAgeStudent!!.name} con ${maxAgeStudent!!.age} años")
    println("Estudiante con último nombre en orden alfabético: ${maxNameStudent!!.name}")
}
```

Como vemos en el ejemplo anterior, se define una expresión lambda que es pasada como argumento a la función `maxByOrNull()`. La definición de la función `maxByOrNull()` exige que la expresión lambda recibida como argumento debe recibir un parámetro del tipo correspondiente a la lista y retornar un valor que sea comparable.

Con objeto de hacer más corto el código anterior, Kotlin nos ofrece una serie de facilidades sintácticas.

La primera de ellas es que **en algunas ocasiones el compilador será capaz de inferir el tipo del parámetro recibido por la expresión _lambda_, por lo que no será necesario indicarlo explícitamente**. Así, en el ejemplo anterior, el tipo del parámetro de la lambda se infiere a partir del tipo de la lista sobre el que se aplica el método `maxByOrNull()`. Por tanto, podemos escribir nuestro código de una manera más corta:

**Expresión lambda con tipo de parámetros inferido**

```kotlin
data class Student(val name: String, val age: Int)

fun main() {
    val students = listOf(Student("Alice", 29), Student("Bob", 27))
    val maxAgeStudent = students.maxByOrNull({ student -> student.age })
    val maxNameStudent = students.maxByOrNull({ student -> student.name })
    println("Estudiante con mayor edad: ${maxAgeStudent!!.name} con ${maxAgeStudent!!.age} años")
    println("Estudiante con último nombre en orden alfabético: ${maxNameStudent!!.name}")
}
```

Por otra parte, **si el último parámetro de una función corresponde a tipo función, entonces al pasarle una expresión lambda como argumento podemos hacerlo fuera de los paréntesis**, por lo que el código anterior quedaría aún más corto:

**Expresión lambda fuera de los paréntesis de la llamada**

```kotlin
data class Student(val name: String, val age: Int)

fun main() {
    val students = listOf(Student("Alice", 29), Student("Bob", 27))
    val maxAgeStudent = students.maxByOrNull() { student -> student.age }
    val maxNameStudent = students.maxByOrNull() { student -> student.name }
    println("Estudiante con mayor edad: ${maxAgeStudent!!.name} con ${maxAgeStudent!!.age} años")
    println("Estudiante con último nombre en orden alfabético: ${maxNameStudent!!.name}")
}
```

Además, **si la expresión _lambda_ es el único parámetro de la llamada, podemos omitir los paréntesis**, con lo que nuestro código quedaría como:

**Omisión de paréntesis en la llamada**

```kotlin
data class Student(val name: String, val age: Int)

fun main() {
    val students = listOf(Student("Alice", 29), Student("Bob", 27))
    val maxAgeStudent = students.maxByOrNull { student -> student.age }
    val maxNameStudent = students.maxByOrNull { student -> student.name }
    println("Estudiante con mayor edad: ${maxAgeStudent!!.name} con ${maxAgeStudent!!.age} años")
    println("Estudiante con último nombre en orden alfabético: ${maxNameStudent!!.name}")
}
```

Por este motivo, **si una función recibe un parámetro de tipo función, se recomienda definir éste como último parámetro de la función**. A este técnica se le conoce como **_trailing lambda_**.

En los parámetros de una lambda, si el tipo correspondiente lo permite, **podemos usar desestructuración**. Por ejemplo:

**Desestructuración en parámetro de una lambda**

```kotlin
data class Student(val name: String, val age: Int)

fun main() {
    val students = listOf(Student("Alice", 29), Student("Bob", 27))
    val maxAgeStudent = students.maxByOrNull { (_, age) -> age }
    val maxNameStudent = students.maxByOrNull { (name, _) -> name }
    println("Estudiante con mayor edad: ${maxAgeStudent!!.name} con ${maxAgeStudent!!.age} años")
    println("Estudiante con último nombre en orden alfabético: ${maxNameStudent!!.name}")
}
```

Debemos tener en cuenta que **si la función define otros parámetros antes del parámetro para el que vamos a pasar una expresión _lambda_, deberemos especificar los argumentos correspondientes entre los paréntesis**. Por ejemplo:

**No podemos omitir paréntesis si hay otros argumentos**

```kotlin
fun main() {
    val items = listOf(2, 4, 6)
    val product1 = items.fold(1) { acc, e -> acc * e }
    // ERROR DE COMPILACIÓN
    val product2 = items.fold 1 { acc, e -> acc * e }
}
```

También recomendamos que **si una función define más de un parámetro de tipo función, al llamarla usemos la sintaxis de argumentos con nombre** (_named arguments_), para dejar claro qué lambda se establece como argumento de qué parámetro.

**Si un parámetro de la expresión lambda no va a ser usado en el cuerpo de la misma, podemos usar como nombre del parámetro el carácter '_'**. Por ejemplo:

**Parámetros sin nombre en expresión lambda**

```kotlin
fun main() {
    val map = mapOf(1 to "x", 2 to "y", 3 to "z")
    // No estamos interesados en el primer parámetro, que corresponde a la clave, sólo en el segundo, que es el valor.
    map.forEach { _, value -> println("$value") }
}
```

Finalmente, **si la expresión _lambda_ tiene un único parámetro y su tipo puede ser inferido por el compilador, entonces no es necesario definir el parámetro ni la flecha en la lambda, ya que si no lo declaramos el compilador le asignará automáticamente el identificador `it`**, que podremos usar en el cuerpo de la expresión _lambda_. Así, podríamos escribir nuestro código de la siguiente manera:

**it como nombre implícito del parámetro de la lambda**

```kotlin
data class Student(val name: String, val age: Int)

fun main() {
    val students = listOf(Student("Alice", 29), Student("Bob", 27))
    val maxAgeStudent = students.maxByOrNull { it.age }
    val maxNameStudent = students.maxByOrNull { it.name } 
    println("Estudiante con mayor edad: ${maxAgeStudent!!.name} con ${maxAgeStudent!!.age} años")
    println("Estudiante con último nombre en orden alfabético: ${maxNameStudent!!.name}")
}
```

> [!tip] Sugerencia
> **Utiliza la sintaxis con `it` sólo cuando el cuerpo de la lambda sea muy simple y evidente**. En caso contrario es preferible definir el nombre del parámetro de la lambda y usarlo en el cuerpo de la misma, ya que al dar un nombre significativo al parámetro aumentarás la legibilidad de tu código.

De igual forma, **no debemos utilizar la sintaxis `it` cuando estemos definiendo _lambdas_ dentro de otras _lambdas_**, ya que se vuelve muy poco evidente a quien haría referencia `it`.

> [!warning] Aviso
> **Si no estamos interesados en ningún parámetro de la _lambda_, pero ésta recibe varios parámetros NO podemos omitir los parámetros ni la flecha**, sino que tendremos que especificarlos obligatoriamente, aunque sea usando el carácter `_`.

En algunas ocasiones es obligatorio que indiquemos el tipo de los parámetros de la lambda, ya que el compilador no tiene contexto suficiente como para inferirlo.

> [!warning] Aviso
> Si la expresión _lambda_ es almacenada en una variable, tendremos que indicar el tipo de los parámetros de la lambda o el tipo de la variable en la que se almacena, o de lo contrario el compilador no tendrá contexto suficiente como para inferir el tipo de los parámetros cuando lo usemos en una función, como en `maxByOrNull(lambda)`.

**La inferencia de tipos en las lambdas no siempre es posible**

```kotlin
data class Student(val name: String, val age: Int)
fun main() {
    // Debemos indicar el tipo de los parámetros
    val byAge = { student: Student -> student.age }
    // o indicar el tipo de la variable
    val byName: (Student) -> String = { student -> student.name }
    val students = listOf(Student("Germán Ginés", 18), Student("Baldomero", 23))
    val oldestStudent = students.maxByOrNull(byAge)
    println("Oldest student: ${oldestStudent?.name ?: "Unknown"}")
    val lastStudentAlphabetically = students.maxByOrNull(byName)
    println("Last student alphabetically: ${lastStudentAlphabetically?.name ?: "Unknown"}")
}
```

En la definición de `byName` anterior estamos indicando que el tipo de dicha variable es una función que recibe un estudiante y retorna una cadena: es un tipo función, como los vistos en [[#1. Tipos función]].

Las expresiones lambdas fueron **diseñadas especialmente para implementar funciones cortas, en las que su cuerpo consiste básicamente en una expresión**. Sin embargo, hay ocasiones en la que tenemos una lambda dentro de cuyo cuerpo queremos realizar una salida anticipada del código de la lambda. En este caso, el problema es que **si usamos `return` dentro de una lambda, por defecto dicho return no retorna únicamente de la lambda sino de la función que la esté usando**. Si queremos que con el return se retorne únicamente de la lambda **deberemos usar `return@IdFuncionQueUsaLaLamba`**. Por ejemplo:

**Uso correcto de return en una lambda**

```kotlin
import kotlin.random.Random

fun onUserChange(action: (String?) -> Unit) {
    val user = if (Random.nextBoolean()) "Baldomero" else null
    action(user)
    println("El método onUserChange termina aquí")
}

fun main() {
    onUserChange { user ->
        if (user == null) return@onUserChange // Prueba a dejar solo return
        println("Hola $user")
    }
    println("El main termina aquí")
}
```

El uso anterior, aunque es posible, se recomienda una mala práctica. Es **mucho mejor definir una función con el código del cuerpo de la lambda y hacer que ésta simplmente la llame**. De esta manera, **dentro de la función creada podemos llamar a `return`** como en cualquier otra función y el cuerpo de la lambda tiene una única expresión, lo que la hace mucho más legible.

**Uso correcto de return en una lambda**

```kotlin
import kotlin.random.Random

fun onUserChange(action: (String?) -> Unit) {
    val user = if (Random.nextBoolean()) "Baldomero" else null
    action(user)
    println("El método onUserChange termina aquí")
}

fun main() {
    onUserChange { cheer(it) }
    println("El main termina aquí")
}

fun cheer(user: String?) {
    if (user == null) return
    println("Hola $user")
}
```

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.4 · Lambdas con it, trailing lambda y desestructuración|Ejercicio 10.4 · Lambdas con it, trailing lambda y desestructuración]]

[Explicación en video](https://www.youtube.com/embed/YbirafenYNI)

## 6. Conversión SAM

Una interfaz funcional es aquella que dispone de un único método abstracto, de ahí que también reciban el nombre de **SAM** (_Single Abstract Method_, único método abstracto).

Cuando tenemos una función con un parámetro cuyo tipo correponde a una interfaz funcional (y no a un tipo función), en principio no podríamos usar una lambda como argumento, ya que, como hemos dicho, en Kotlin una lambda es un literal de tipo función, y no un objeto que implemente una interfaz funcional. Por este motivo, en principio para pasar un argumento para dicho parámetro deberíamos crear un objeto anónimo que implemente la intefaz funcional.

Por ejemplo, supongamos que tenemos la siguiente interfaz funcional Java:

**Interfaz funcional Java**

```java
@FunctionalInterface
interface MyAction {
    void execute();
}
```

Y en Kotlin definimos una función que recibe un parámetro cuyo tipo corresponde a dicha interfaz funcional Java:

**Función Kotlin con parámetro cuyo tipo corresponde a la interfaz funcional**

```kotlin
fun runAction(action: MyAction) {
    action.execute()
}
```

En ese caso, en principio, para llamar a la función deberíamos usar como argumento un objeto anónimo que implemente la interfaz, pero no podríamos usar una lambda, ya el tipo del parámetro NO es un tipo función. Por ejemplo:

**Llamada a la función en Kotlin proporcionando como argumento un objeto anónimo que implementa la interfaz**

```kotlin
runAction(object : MyAction {
    override fun execute() {
        println("Action executed!")
    }
})
```

Como vemos esta sintaxis resulta bastante verbosa. Sería mucho mejor que pudiéramos usar una lambda, pero una lambda NO es un objeto que implemente la interfaz funcional. Pues bien, para solucionarlo, el compilador de Kotlin, en la llamada convierte automáticamente la lambda pasado como argumento en una instancia de la interfaz funcional, siempre que sea compatible. A esta conversión se le llama **conversión SAM**.

Gracias a dicha conversión SAM, la llamada a la función anterior puede realizarse proporcionando una lambda compatible:

**Llamada a la función en Kotlin proporcionando una lambda compatible con la interfaz**

```kotlin
runAction {
    println("Action executed with SAM conversion!")
}
```

La conversión SAM en Kotlin se lleva a cabo automáticamente cuando el tipo corresponde a una interfaz funcional definida en Java. Sin embargo, **por defecto NO se lleva a cabo si la interfaz está definida en Kotlin y contiene un único método abstracto**. Si queremos que dicha conversión se realice también con una interfaz funcional definida en Kotlin, **será necesario que definamos la interfaz como `fun interface`**.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.5 · Conversión SAM con fun interface DelayedTask|Ejercicio 10.5 · Conversión SAM con fun interface DelayedTask]]

## 7. Interfaz fun interface

Una `fun interface` en Kotlin es una interfaz con un único método abstracto, para la que se realizará conversión SAM cuando usamos una lambda como argumento de un parámetro cuyo tipo corresponda a la interfaz.

Por ejemplo, si la interfaz funcional del apartado anteiror anterior la tuviéramos definida en Kotlin, para que se lleve a cabo la conversión SAM deberíamos definirla de la siguiente manera:

**Interfaz funcional Kotlin**

```kotlin
fun interface MyAction {
    fun execute()
}

fun runAction(action: MyAction) {
    action.execute()
}

fun main() {
    runAction {
        println("Action executed with SAM conversion!")
    }
}
```

Definir una interfaz como fun interface y usar un tipo de función son dos formas diferentes de trabajar con funciones en Kotlin, pero cada enfoque tiene sus ventajas en función de las necesidades del diseño de tu código:

- Debemos usar `fun interface` cuando queramos crear una interfaz funcional compatible con Java, esto es, que pueda ser usada desde código Java, ya que Java no soporta directamente los tipos función de Kotlin.
- Al definir una `fun interface` estamos dándole un identificador que le aporta un significado al tipo, mientras que con los tipos función no tienen un identificador asociado.
- Al usar una `fun interface`, podemos aprovechar características de la orientación a objetos como la herencia, la implementación de múltiples interfaces, y el uso de clases anónimas.
- Dicho lo anterior, los tipos función tienen la ventaja clara de que son más directos y sencillos cuando no necesitamos asociar un identificador al tipo o cuando la función es pequeña, específica y ligera, como en el caso de _callbacks_ o transformaciones simples.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.6 · fun interface DataValidator|Ejercicio 10.6 · fun interface DataValidator]]

## 8. Funciones anónimas

Una **función anónima** es una expresión que retorna un objeto de un tipo función, es decir un literal de tipo función. Su sintaxis es similar a la de la definición de una función (incluyendo la opción de función que solo retorna una expresión), pero con algunas diferencias:

- No se le especifica ningún identificador a la función, por lo que el objeto retornado deberá asignarse a alguna variable.
- No puede tener parámetros de tipos, es decir, no puede ser una función genérica.
- No puede incluir argumentos por defecto para los parámetros.
- Los tipos de los parámetros se pueden inferir en algunos casos.

Veamos algunos ejemplos:

**Ejemplos de funciones anónimas**

```kotlin
fun main() {
    val add1 = fun(a: Int, b: Int): Int { return a + b }
    val add2 = fun(a: Int, b: Int) = a + b
    val add3: (Int, Int) -> Int = fun(a, b) = a + b

    println(add1(1, 2));
    println(add2(3, 4));
    println(add3(4, 5));

    operate(5, 6, add1)
    operate(7, 8, add2)
    operate(8, 9, add3)
}

fun operate(
    x: Int, 
    y: Int, 
    action: (Int, Int) -> Int // Tipo función que recibe dos enteros y retorna un entero
): Int {
    val result = action(x, y) // Invocación del parámetro de tipo función
    println("Result: ${result}")
    return result
}
```

**Cuando usamos `return` dentro de una función anónima, a diferencia del caso de las lambdas, estamos retornando únicamente del código de la función anónima**, y no de la función más interna que incluye la expresión lambda.

**El return dentro de una función anónima solo retorna de la función anónima, no de la función que la llamó**

```kotlin
import kotlin.random.Random

fun onUserChange(action: (String?) -> Unit) {
    val user = if (Random.nextBoolean()) "Baldomero" else null
    action(user)
    println("El método onUserChange termina aquí")
}

fun main() {
    val action = fun(user: String?) { 
        if (user == null) return // Solo retorna de esta función anónima
        println("Hola $user")
    }
    onUserChange(action)
    println("El main termina aquí")
}
```

La sintaxis de las expresiones lambda tiene un pequeño inconveniente: no permite especificar el tipo del valor retornado por la expresión. Normalmente esto no es problema porque en la mayoría de las ocasiones dicho tipo de retorno puede ser inferido automáticamente a partir del cuerpo de la expresión. Sin embargo, si debemos indicarlo explícitamente, no podremos usar una expresión lambda, sino una función anónima.

En Kotlin es poco habitual usar funciones anónimas, ya que **los desarrolladores prefieren usar las expresiones lambda, normalmente debido al concepto de _trailing lambda_ y la sintaxis tan elegante asociada a él** a la hora de llamar a funciones que recibe como argumento un objeto de tipo función.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.7 · testBoth con funciones anónimas|Ejercicio 10.7 · testBoth con funciones anónimas]]

## 9. Closures

Tanto las expresiones lambda, como las funciones anónimas, las expresiones `object` y las funciones locales, pueden **acceder y modificar las variables disponibles en el entorno en el que fueran definidas, y que están situadas fuera de su propio ámbito**. A este acceso a un ámbito externo es lo que se le conoce como **_closure_**.

En un _closure_, las variables del ámbito en el que se define, por ejemplo, la lambda, son **"capturadas"** (referenciadas), para que puedan ser usadas en el código de la propia lambda. A diferencia de en Java, donde las variables capturadas en el _closure_ son consideradas _final_, y por tanto no se pueden modificar, en el caso de Kotlin **las variables capturadas sí pueden ser modificadas si están definidas con `var`**.

Veamos un ejemplo:

**Ejemplo de closure**

```kotlin
fun makeCounter(): () -> Int {
    var i = 0
    return { i++ }
}

fun main() {
    val counter1 = makeCounter()
    val counter2 = makeCounter()

    println(counter1()) // 0
    println(counter1()) // 1
    println(counter2()) // 0
    println(counter2()) // 1
}
```

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.8 · Closure sequenceGenerator|Ejercicio 10.8 · Closure sequenceGenerator]]

## 10. Referencias a función

Como hemos dicho, **cuando usamos un literal de función en forma de expresión lambda o función anónima estamos creando un nuevo objeto de tipo función**. Sin embargo, en algunas ocasiones cuando queremos un objeto función, por ejemplo para pasarlo como argumento, queremos **referirnos a una función ya existente**. Para ello, Kotlin nos proporciona la sintaxis conocida como **referencia a función**. La sintaxis concreta de una referencia a función depende del tipo de función de la que se trate.

En el caso de querer **referenciar una función _top-level_** simplemente usamos `::idFuncion`. Por ejemplo:

**Referencia a función top-level**

```kotlin
fun <T> operate(x: T, y: T, action: (T, T) -> T): T = action(x, y)

fun add(x: Int, y: Int): Int = x + y

fun main() {
    val result = operate(5, 8, ::add)
    println(result)
}
```

**Si la función referenciada tiene argumentos por defecto, puede usarse una referencia a ella como objeto de tipos función donde no se incluya el tipo correspondiente al parámetro opcional**. Por ejemplo:

**Referencia a función top-level con argumentos por defecto**

```kotlin
fun <T> operateUnary(x: T, action: (T) -> T): T = action(x)

fun add(x: Int, y: Int = 0): Int = x + y

fun main() {
    val result = operateUnary(5, ::add)
    println(result)
}
```

En el caso que querer **referenciar un método del _companion object_** de un tipo o un método estático de una clase creada en Java, la sintaxis será `idTipo::idMetodo`. Esto también funciona para acceder a métodos estáticos de una clase Java. Por ejemplo para acceder al método estático `sum` de la clase `Integer` haremos lo siguiente:

**Referencia a método estático**

```kotlin
fun <T> operate(x: T, y: T, action: (T, T) -> T): T = action(x, y)

fun main() {
    val result = operate(5, 8, Integer::sum)
    println(result)
}
```

Cuando queremos obtener una **referencia a un método de una clase o interfaz** usamos la sintaxis `idTipo::idMetodo`. Como sabemos, los métodos deben ser ejecutados sobre un objeto (el receptor, _receiver_). En el caso de una referencia a método, **el receptor corresponderá al primer parámetro suministrado**.

**Referencia a método**

```kotlin
data class Number(val num: Int) {
    fun toFloat(): Float = num.toFloat()
    fun times(n: Int): Number = Number(num * n)
}

fun main() {
    val numberObject = Number(10)
    val floatRef: (Number) -> Float = Number::toFloat
    val multiplyRef: (Number, Int) -> Number = Number::times
    println(floatRef(numberObject))
    println(multiplyRef(numberObject, 4))
}
```

Cuando queremos obtener una referencia a método de una clase genérica, es obligatorio especificar explícitamente los argumentos para los parámetros de tipo. Así, por ejemplo debemos especificar `Box<String>::unbox` y NO podemos indicar simplemente `Box::unbox`.

La obtención y uso de una **referencia a una _extension function_ es exactamente igual a la de una referencia a método**, con la sintaxis `idTipo::idFuncion`:

**Referencia a extension function**

```kotlin
data class Number(val num: Int)

fun Number.toFloat(): Float = num.toFloat()
fun Number.times(n: Int): Number = Number(num * n)

fun main() {
    val numberObject = Number(10)
    val floatRef: (Number) -> Float = Number::toFloat
    val multiplyRef: (Number, Int) -> Number = Number::times
    println(floatRef(numberObject))
    println(multiplyRef(numberObject, 4))
}
```

También podemos obtener la **referencia a método de una instancia concreta** (_bounded function reference_), en vez de a un tipo de dato, para lo que usaremos la sintaxis `idInstancia::idMetodo`. En este caso, al hacer uso de la referencia NO es necesario pasar el objeto receptor como primer argumento, ya que la referencia ya se ha obtenido sobre dicho objeto receptor.

> [!warning] Ojo con el ejemplo
> En los apuntes originales las variables se declaraban como `(Number) -> Float` y `(Number, Int) -> Number`, y así **no compila** (comprobado con `kotlinc`): una referencia ligada a una instancia ya lleva el receptor dentro, así que su tipo pierde ese primer parámetro. Aquí se han corregido a `() -> Float` y `(Int) -> Number`.

**Referencia a método de instancia**

```kotlin
data class Number(val num: Int) {
    fun toFloat(): Float = num.toFloat()
    fun times(n: Int): Number = Number(num * n)
}

fun main() {
    val numberObject = Number(10)
    val floatRef: () -> Float = numberObject::toFloat
    val multiplyRef: (Int) -> Number = numberObject::times
    println(floatRef())
    println(multiplyRef(4))
}
```

Si tenemos un parámetro o variable de un tipo función que no recibe nada y retorna un objeto de un determinado tipo `() -> T`, podemos obtener un objeto de dicho tipo función mediante una referencia al constructor de dicho tipo `T`, con la sintaxis `::idClase`.

Por otro lado, para este caso, también podemos usar una referencia a una propiedad de un tipo, con la sintaxis `Tipo::idPropiedad`, en cuyo caso al usarla deberemos usar el receptor como argumento. También podemos obtener una referencia a una propiedad de una instancia concreta, con la sintaxis `idInstancia::idPropiedad`, en cuyo caso al usarla NO es necsario indicar el receptor como argumento, puesto que ya fue especificado al obtener la referencia a la propiedad.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.9 · Referencias a función con applyOperation|Ejercicio 10.9 · Referencias a función con applyOperation]]

## 11. Inline functions

**Cuando se pasa una lambda como argumento a una función, en realidad se crea un objeto de una clase anónima anónima para representar dicha lambda**. Esto puede generar un peor rendimiento respecto al uso de memoria, debido a la creación de estos objetos, y un incremento de trabajo del recolector de basura cuando su memoria debe marcarse como libre. Además, cada vez que la lambda es llamada desde el código de la función que la recibe como argumento, la ejecución debe saltar hacia el código de la lambda y cuando termina de ejecutarse, saltar de vuelta hacia el código de la función. Esto genera un pequeño coste de rendimiento de ejecución.

Por tanto, **las lambdas pueden producir una sobrecarga en términos de rendimiento y uso de memoria cuando se pasan como argumentos a una función** en Kotlin.

Sin embargo, Kotlin proporciona una característica llamada _inline functions_ (funciones en línea) para mitigar esta sobrecarga. **Cuando se declara una función con la palabra reservada `inline`**, la función no será llamada como cualquier otra función; en su lugar, **el compilador durante la compilación reemplazará cualquier llamada a la función por el código del cuerpo de la propia función, sustituyendo en éste el uso de los parámetros por los argumentos especificados en la llamada**.

Además, **cuando una _inline function_ tiene parámetros correspondientes a tipos función, por defecto, la llamada al método `invoke()` de dichos parámetros es reemplazada por el código del literal de función especificado como argumento**, tanto si se trata de una función anónima como de una expresión lambda, reemplazando los parámetros de ésta por los argumentos indicados.

Por tanto, dado que la llamada a la lambda desde dentro de la función es reemplazado por el cuerpo de la lambda directamente, **no se crean objetos para la lambda ni la ejecución salta desde una función a otra, mejorando el rendimiento**.

Veamos un ejemplo:

**Definición de una función inline**

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit) {
    for (index in 0 until times) {
        action(index)
    }
}

fun main() {
    repeat(10) {
        print(it)
    }
}
```

Cuando se compila el código anterior, se compila en algo similar a:

**Conversión de una función inline durante compilación**

```kotlin
fun main() {
    for (index in 0 until 10) {
        print(index)
    }
}
```

Como vemos, el resultado no es solo más eficiente, sino que además es necesario alojar mucho menos objetos. De hecho, **se ha convertido en una práctica estándar marcar como `inline` todas las funciones top-level functions con parámetros de tipo función**.

El hecho de que en una función inline la llamada a un parámetro de tipo función sea reemplazado por el código de la lambda pasada como argumento, tiene algunas implicaciones interesantes. En primer lugar, **si el cuerpo de la lambda contiene un `return`, dado que tanto la llamada a la función como la llamada a la lambda es reemplazada por el código correspondiente, el `return` producirá que se retorne de la función en la que se llamó a la función inline**. A esto se le conoce como _non-local return_ (retorno no local). Por ejemplo:

**Non-local return en una lambda usada en una función inline**

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit) {
    for (index in 0 until times) {
        action(index)
    }
}

fun main() {
    repeat(10) { index ->
        if (index == 4) return // Returns from main
        println(index)
    }
    println("main finished")
}
```

Para que el retorno sea local, simulando un `continue` en el bucle, al usar `return` tenemos que especifica como etiqueta el nombre de la función inline, de la siguiente manera:

**Local return en una lambda usada en una función inline**

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit) {
    for (index in 0 until times) {
        action(index)
    }
}

fun main() {
    repeat(10) { index ->
        if (index == 4) return@repeat // Returns from repeat (acts like a continue)
        println(index)
    }
    println("main finished")
}
```

Si queremos simular un `break`, de manera que se salga del bucle de la función inline, pero que no sea un non-local return, tenemos que definir una etiqueta fuera y especificarlad en el `return`.

**Local return en una lambda usada en una función inline para salir del bucle**

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit) {
    for (index in 0 until times) {
        action(index)
    }
}

fun main() {
    run {
        repeat(10) { index ->
            if (index == 4) return@run // Returns from repeat (acts like a break)
            println(index)
        }
    }
    println("main finished")
}
```

Sin embargo, desde Kotlin 2.2.0 podemos usar `break` y `continue` de manera no local, lo que implica que podemos usarlas dentro de lambdas pasadas como argumento en una función inline que ejecuta la lambda dentro de un bucle.

**Uso de break en una lambda empleada en una función inline**

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit) {
    for (index in 0 until times) {
        action(index)
    }
}

fun main() {
    repeat(10) { index ->
        if (index == 4) break;
        print(index)
    }
    println("main finished")
}
```

> [!warning] Este ejemplo de los apuntes no compila
> Comprobado con `kotlinc` 2.4: da `'break' and 'continue' are only allowed inside loops`, tanto sin opciones como con el _flag_ `-Xallow-breaks-and-continues-in-lambdas` (que ya ni existe) o con `-Xnon-local-break-continue`. El motivo es que el `break` de una lambda inline afecta a un **bucle que esté fuera de la lambda**, en la función que la escribe, y no al bucle que hay dentro de `repeat`. En `main` no hay ningún bucle, así que no hay nada de lo que salir. Desde Kotlin 2.2 esto es estable y **no necesita ningún _flag_**. Ejemplo que sí funciona:
>
> ```kotlin
> fun main() {
>     for (i in 1..3) {
>         listOf(10, 20, 30).forEach { value ->
>             if (i == 2) break           // sale del for exterior
>             println("i=$i value=$value")
>         }
>     }
>     println("main finished")
> }
> ```

Pero, para que podamos usar `break` y `continue` dentro de lambadas, debemos activar esa posiblidad explícitamente como opción de compilación en el archivo `build.gradle.kts`:

**Habilitar break y continue para lambdas en inline functions**

```kotlin
kotlin {
    compilerOptions {
        freeCompilerArgs.add("-Xallow-breaks-and-continues-in-lambdas")
    }
}
```

Hay ocasiones en las que queremos que se haga uso inline de una función, es decir, que la llamada a la función sea sustituida por su código, pero, por algún motivo, no podemos hacer uso inline de alguno de sus parámetros de tipo función. En esos casos, podemos usar marcar dicho parámetro con uno de los siguientes modificadores:

- `crossinline`: El parámetro tipo función tendrá un uso inline, pero no se permite el _non-local return_. Usamos este modificador cuando la función es usada en otro ámbito en el que no se permite el _non-local return_, como por ejemplo dentro de otra lambda que no está inline.
- `noinline`: El parámetro tipo función no tendrá un uso inline. Usamos este modificador cuando usamos esta función como argumento de otra función que no está inline.

Otro de las consecuencias del uso inline de una función es que, **en el caso de que ésta sea parametrizable, el compilador puede sustituir en tiempo de compilación el parámetro de tipo por el argumento suministrado para dicho tipo**. Veamos qué implicación tiene este hecho.

Como hemos visto, cuando se diseñaron los genéricos en Java, se optó por realizar con los genéricos lo que se conoce como _type erasure_ (borrado de tipos), que indica que al compilar el código a _bytecode_ se pierde la información sobre los tipos especificados como argumento para los genéricos, de manera que en _bytecode_ un `List<String>` es representado como un `List`, y que un `List<Double>` también es representado como un `List`.

Esta pérdida de información implica que vamos a tener una serie de restricciones en tiempo de ejecución, ya que realmente no se va a conocer el tipo de la clase o interfaz parametrirzada. Por ejemplo: NO vamos a poder comprobar si el tipo del elemento es un tipo de terminado usando `is`, ni vamos a poder instanciar objetos del tipo parametrizado mediante `T()`, ni llamar a métodos del objeto compañero de éste, etc., , ya que la información sobre qué tipo real corresponde al parámetro tipo no está disponible en tiempo de ejecución.

Sin embargo, pensemos ahora en el caso de una función inline parametrizable. Como hemos indicado, la llamada a dicha función será reemplazada en tiempo de compilación por el código de la propia función. **¿Pero dentro de ese reemplazo también se sustituye en dicho código las referencias al parámetro de tipo por el argumento de tipo suministrado? La respuesta es que sí siempre que dicho parámetro de tipo haya sido especificado en la función inline usando el modificador `reified`** (que podríamos traducir por "materializado").

La ventaja de que se realice en tiempo de compilación un reemplazo del parámetro de tipo por el argumento de tipo especificado en la llamada dentro del código de la función, es que **en tiempo de ejecución la información sobre el tipo correspondiente NO se ha borrado**, por algunas de las las operaciones que vimos que no eran posibles debido al _type erasure_ vuelven a ser posibles en el código de la función, siempre que ésta sea inline y el parámetro de tipo de marque con el modificador `reified`.

**Reified en función inline**

```kotlin
import kotlin.reflect.typeOf

fun main() {
    example("Baldomero")
}

inline fun <reified T> example(a: T) {
    val check = a is T
    println("check vale $check")
    val ref = T::class
    println("ref vale $ref")
    val type = typeOf<T>()
    println("type vale $type")
    //val instance = T() // ERROR
}
```

Como vemos en el ejemplo, **vamos a poder usar el operador `is` con el parámetro de tipo marcado como `reified`**.

También podemos **definir como `inline` una propiedad de una clase con _getter_ personalizado, para que cuando se acceda a la propiedad éste sea reemplazado por el _getter_ correspondiente**, lo que puede suponer una optimización de bajo nivel, aunque en realidad no es muy habitual. Por ejemplo:

**Propiedad inline**

```kotlin
class User(val name: String, val surname: String) {
    inline val fullName: String get() = "$name $surname"
}

fun main() {
    val user = User("A", "B")
    println(user.fullName) // translates to println("${user.name} ${user.surname}")
}
```

El uso del modificador `inline` en las funciones es útil, pero no debemos usarlo siempre, debido a su coste y sus limitaciones:

- No pueden usar elementos con una visibilidad más restrictiva que la propia función.
- No pueden ser recursivas.
- Hacen que el código de la aplicación crezca, lo que en algunos casos puede ser problemático.

Las razones principales para definir una función como inline son:

- Mejorar el rendimiento de funciones con parámetros de tipo función, permitiendo además el _non-local return_.
- Para permitir la "materialización" de parámetros de tipo (`reified`).

Por este motivo las funciones inline son **adecuadas para funciones de utilidad, especialmente para funciones _top-level_** o métodos redundantes que se emplean para simplificar el uso de métodos de otra clase.

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.10 · Inline function y non-local return|Ejercicio 10.10 · Inline function y non-local return]]

## 12. Literales de función con receptor (lambda with receiver)

Como hemos visto, Kotlin, a diferencia de Java, posee el concepto de **tipo función**, lo que significa que podemos definir variables o parámetros de una función como de un determinado tipo función.

Por otra parte, también hemos visto que las funciones anónimas se definen igual que una función normal, pero sin identificador, y que una instancia de una función anónima corresponde a un literal de función.

De igual forma, también podemos **definir una _extension function_ anónima, de forma similar a una _extension function_, pero sin identificador para la función**. Una instancia de una _extension function_ anónima representa a un literal de _extension function_, que **puede ser llamada** de una forma especial: **sobre un objeto receptor** (_receiver_).

**Extension function anónima**

```kotlin
val myAnonymousExtensionFunction = fun String.(other: String) = this + other

fun main() {
    println("A".myAnonymousExtensionFunction("B")) // Imprime AB
}
```

La ventaja principal de una _extension function_, incluyendo las anónimas, es que **en su cuerpo, `this` respresenta el objeto receptor** sobre el que se está ejecutando.

En el ejemplo anterior, cabría preguntarse **cuál es el tipo de la variable `myAnonymousExtensionFunction`**. La respuesta es lo que se conoce como un **tipo función con receptor** (_function type with receiver_), que se representa con la sintaxis `TipoReceptor.(listaTiposParámetros) -> TipoRetorno`. Por ejemplo, en el caso anterior, el tipo sería `String.(String) -> String`.

Como acabamos de ver, **una _extension function_ anónima es un literal de un tipo función con receptor**. Pero también podemos crear un literal de este tipo usando una lambda en vez de una función anónima. En este caso **NO existe una sintaxis especial** para ello: simplemente, cuando una expresión lambda se asocia a un parámetro o variable de tipo función con receptor, se convierte en lo que se conoce como **_lambda with receiver_** (lambda con receptor). Como consecuencia de ello, **el cuerpo de la lambda tiene un nuevo receptor, al que puede acceder a través de la palabra reservada `this`** (igual que en una _extension function_), y que corresponde al receptor sobre el que se ejecute la lambda.

**Lambda con receptor**

```kotlin
val myLambdaWithReceiver: String.(String) -> String = { this + it }

fun main() {
    println("A".myLambdaWithReceiver("B")) // Imprime AB
}
```

Pero ¿qué ocurre **si definimos el tipo de un parámetro de una función como un tipo función con receptor**? Pues que **la lambda que nos pasen como argumento cuando llamen a la función, puede usar `this` en su cuerpo para hacer referencia al objeto receptor** sobre el que nosotros hayamos llamado a la lambda.

Para comprender este concepto vamos a desarrollar una función llamada `buildMyString`, que retorne una cadena de caracteres construida ejecutando la lambda recibida, que recibe un objeto `StringBuilder` como argumento, y que la propia función le proporciona. Así nuestro objetivo será usar dicha función de la siguiente manera:

**Uso de la función buildMyString**

```kotlin
// Recibe una lambda con un argumento tipo StringBuilder y que no retorna nada,
// y retorna una cadena.
fun buildMyString(action: (StringBuilder) -> Unit): String {
    // Se crea el StringBuilder que va a ser usado internamente.
    val stringBuilder = StringBuilder()
    // Se ejecuta la lambda que me han pasado, y le paso como argumento
    // el StringBuilder que se acaba de crear.
    action(stringBuilder)
    // Se construye la cadena resultante y se retorna.
    return stringBuilder.toString()
}

fun main() {
    val s = buildMyString { stringBuilder ->
        // Todas las operaciones que deben realizarse sobre el StringBuilder
        // con el que trabaja internamente la función buildString.
        stringBuilder.append("Hello, ")
        stringBuilder.append("World! ")
        // La lambda no debe retornar nada.
    }
    println(s)
}
```

Como sabemos, cuando una lambda define un único parámetro, podemos usar directamente la palabra reservada `it` y así evitarnos tener que indicar su nombre explícitamente. De esta manera, el uso de la función quedaría así:

**Uso de la función buildMyString**

```kotlin
// Recibe una lambda con un argumento tipo StringBuilder y que no retorna nada,
// y retorna una cadena.
fun buildMyString(action: (StringBuilder) -> Unit): String {
    // Se crea el StringBuilder que va a ser usado internamente.
    val stringBuilder = StringBuilder()
    // Se ejecuta la lambda que me han pasado, y le paso como argumento
    // el StringBuilder que se acaba de crear.
    action(stringBuilder)
    // Se construye la cadena resultante y se retorna.
    return stringBuilder.toString()
}

fun main() {
    val s = buildMyString { 
        // Todas las operaciones que deben realizarse sobre el StringBuilder
        // con el que trabaja internamente la función buildString.
        it.append("Hello, ")
        it.append("World! ")
        // La lambda no debe retornar nada.
    }
    println(s)
}
```

Esta función, tal y como está definida, funciona correctamente pero su uso es un poco incómodo, porque como hemos visto en el ejemplo anterior, al indicar la lambda que queremos que se ejecute, tenemos que usar `it` todo el rato para acceder a los método del StringBuilder.

Pero, ¿y si pudiéramos especificar que la lambda que recibe la función `builderString` no es de un tipo función normal sino de un tipo función con receptor?. En ese caso, el objeto receptor sobre el que se ejecuta puede ser referenciado dentro del cuerpo de la lambda mediante `this`.

La primera línea de la definición de nuestra función quedaría así:

**Definición de la función buildMyString**

```kotlin
// Recibe un parametro de tipo función con receptor pero sin parámetros, donde el receptor es de tipo StringBuilder.
fun buildMyString(action: StringBuilder.() -> Unit): String {
    // ...
}
```

Debemos fijarnos en el tipo función ya no tiene ningún parámetro de tipo `StringBuilder`, sino que `StringBuilder` va a ser el tipo del receptor, es decir, el objeto sobre el que se va a ejecutar la acción representada por el parámetro `action`. Así, el código final de la definción de nuestra función `buildString` quedaría de la siguiente manera:

**Definición de la función buildMyString**

```kotlin
// Recibe una lambda con un receptor tipo StringBuilder y que no retorna nada,
// y retorna una cadena.
fun buildMyString(action: StringBuilder.() -> Unit): String {
    // Se crea el StringBuilder que va a ser usado internamente.
    val stringBuilder = StringBuilder()
    // Se ejecuta la lambda que me han pasado SOBRE el StringBuilder
    // que se acaba de crear (no se le pasa como argumento).
    stringBuilder.action()
    // Se construye la cadena resultante y se retorna.
    return stringBuilder.toString()
}
```

La ventaja real que tiene esta última definición se muestra de forma clara a la hora de usar la función anterior y pasar la lambda correspondiente, ya que como se trata de una lambda con receptor, dentro del cuerpo de la misma podemos referenciar al receptor mediante `this`, lo que en la práctica equivale a no tener ni siquiera que referenciarlo para ejecutar sus métodos. Así, llamaríamos a la función de la siguiente manera:

**Uso de la función buildMyString**

```kotlin
// Recibe una lambda con un receptor tipo StringBuilder y que no retorna nada,
// y retorna una cadena.
fun buildMyString(action: StringBuilder.() -> Unit): String {
    // Se crea el StringBuilder que va a ser usado internamente.
    val stringBuilder = StringBuilder()
    // Se ejecuta la lambda que me han pasado SOBRE el StringBuilder 
    // que se acaba de crear (no se le pasa como argumento).
    stringBuilder.action()
    // Se construye la cadena resultante y se retorna.
    return stringBuilder.toString()
}

fun main() {
    val s = buildMyString { 
        append("Hello, ")
        append("World! ")
    }
    println(s)
}
```

Los métodos `append()` se están ejecutando sobre el objeto `StringBuilder` que actúa como receptor. Dado que dentro del cuerpo de la lambda dicho receptor corresponde a this, no es necesario especificarlo al usar sus métodos, como en el caso del método`append()`.

La librería estándar de Kotlin posee varias funciones genéricas que hacen uso del concepto de tipos función con receptor y de lambda con receptor, que resultan muy interesantes, algunas de las cuales estudiaremos a continuación.

[Explicación en video](https://www.youtube.com/embed/bzW-PDuBAg4)

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.11 · Funciones hacerCon con receptor|Ejercicio 10.11 · Funciones hacerCon con receptor]]

## 13. Scoping functions (with, run, apply, let, also)

La librería estándar de Kotlin proporciona una serie de funciones y _extension functions_ muy útiles a la hora de acortar nuestro código, haciendo uso de expresiones lambda. A continuación estudiaremos las que se usan más habitualmente.

### 13.1 with()

Función que permite acceder desde la expresión lambda a un objeto que es pasado como argumento. Recibe como parámetro un objeto y una expresión lambda. Además el objeto recibido se establece como receptor en la expresión lambda, de manera que ésta pueda acceder a él a través de `this`. La función `with()` retorna el valor que haya retornado la expresión lambda.

La definición resumida de la función es:

**Definición de la función with()**

```kotlin
public inline fun <T, R> with(receiver: T, block: T.() -> R): R {
    return block()
}
```

Esta función nos puede resultar muy útil si queremos configurar un determinado objeto estableciendo algunas de sus propiedades y no queremos tener que repetir una y otra vez el identificador del objeto. Por ejemplo:

**Uso de la función with()**

```kotlin
data class Settings(var javaScriptEnabled: Boolean = false, var databaseEnabled: Boolean = false)

fun main() {
    val settings = Settings(false, false)
    with(settings) {
        // Se accede a las propiedades javaScriptEnabled y databaseEnabled del 
        // objeto settings, que dentro de la lambda está representado por this.
        javaScriptEnabled = true
        databaseEnabled = true
    }
    println(settings)
}
```

### 13.2 T.run()

_Extension function_, que permite acceder desde la expresión lambda al objeto sobre el que se ejecuta. Recibe como parámetro una expresión lambda. Además el objeto sobre el que se ejecuta `run()` se establece como receptor en la expresión lambda, de manera que ésta pueda acceder a él a través de `this`. La función `run()` retorna el valor que haya retornado la expresión lambda.

Su funcionamiento es similar a `with()`, pero se trata de una _extension function_, por lo que podemos usar el operador `?.` para ejecutarla sobre objetos de tipo _nullable_, como en `objeto?.run { }`.

La definición resumida de la función es:

**Definición de run()**

```kotlin
public inline fun <T, R> T.run(block: T.() -> R): R {
    return block()
}
```

Esta función nos puede resultar muy útil si queremos configurar un determinado objeto estableciendo algunas de sus propiedades y no queremos tener que repetir una y otra vez el identificador del objeto. Por ejemplo:

**Uso de la función run()**

```kotlin
data class Settings(var javaScriptEnabled: Boolean = false, var databaseEnabled: Boolean = false)

fun main() {
    val settings = Settings(false, false)
    settings.run {
        // Se accede a las propiedades javaScriptEnabled y databaseEnabled del 
        // objeto settings, que dentro de la lambda está representado por this.
        javaScriptEnabled = true
        databaseEnabled = true
    }
    println(settings)
}
```

### 13.3 T.apply()

Como acabamos de ver, `T.run()` retorna el valor retornado por la expresión lambda. Sin embargo, en algunas ocasiones lo que queremos es precisamente retornar el objeto receptor.

Aunque podríamos hacerlo explícitamente haciendo que la expresión lambda retornara `this`, la librería estándar de Kotlin nos ofrece una alternativa mejor, la función `T.apply()`, que funciona de manera similar a `T.run()` pero retorna el propio objeto receptor en vez del valor retornado por la expresión lambda.

Su definición resumida es:

**Definición de la función apply()**

```kotlin
public inline fun <T> T.apply(block: T.() -> Unit): T {
    block()
    return this
}
```

Esta función resulta muy útil para simular el patrón de diseño _builder_, ya que podemos configurar un objeto y luego retornarlo. Por ejemplo:

**Uso de la función apply()**

```kotlin
data class Settings(var javaScriptEnabled: Boolean = false, var databaseEnabled: Boolean = false) {
    fun activate() {
        javaScriptEnabled = true
        databaseEnabled = true
    }
}

fun createInstance() = 
        // Se crea el objetos, se establece alguna de sus propiedades, se llama a un uno de sus métodos y se retorna el objeto ya construido.
        // El objetos Settings es accesible desde la expresión lambda a través de this.
        Settings().apply { 
            javaScriptEnabled = true
            activate() 
        }

fun main() {
    val settings = createInstance()
    println(settings)
}
```

### 13.4 T.let()

En algunas ocasiones al usar las funciones `T.run()` y `apply()`, el hecho de que la función lambda pueda acceder al objeto sobre el que se ha ejecutado mediante `this` puede resultar un inconveniente, ya que dicho uso the `this` están enmascarando el valor de `this` que normalmente tiene fuera de la expresión lambda.

Para estos casos, quizás sería más oportuno que el objeto sobre el que se ejecutan fuera pasado como argumento a la expresión lambda, de manera que ésta pudiera acceder a él a través de la palabra reservada `it`.

Así, la librería estándar de Kotlin proporciona la función `T.let()`, con funcionalidad similar a `T.run()`, pero en la que el objeto sobre el que se ejecuta será pasado como argumento a la expresión lambda, y no como objeto receptor, de manera que dentro de la expresión lambda `this` seguirá teniendo el valor que tiene fuera de la expresión lambda.

Su definición resumida es:

**Definición de la función let()**

```kotlin
public inline fun <T, R> T.let(block: (T) -> R): R {
    return block(this)
}
```

Rehaciendo el ejemplo que hemos visto en `T.run()` empleando `let()`:

**Uso de la función let()**

```kotlin
data class Settings(var javaScriptEnabled: Boolean = false, var databaseEnabled: Boolean = false) {
    fun activate() {
        javaScriptEnabled = true
        databaseEnabled = true
    }
}

fun main() {
    val settings = Settings(false, false)
    settings.let {
    // El objeto Settings es pasado como argumento a la expresión lambda. Al ser el único
    // parámetro podemos acceder a él a través de it.
        it.activate()
        it.javaScriptEnabled = true
        it.databaseEnabled = false
    }
    println(settings)
}
```

Otro uso frecuentes de `let()` es como reemplazo de `if (object != null)`, aunque no hay que abusar de él:

**Uso de let() para acción tras comprobación de no null**

```kotlin
import kotlin.random.Random

fun main() {
    val text = if (Random.nextBoolean()) "text" else null
    // len tomará la longitud de text si no es null, o 0 en caso contrario.
    val len = text?.let {
        println("get length of $it")
        it.length
    } ?: 0
    println("length of $text is $len")
}
```

### 13.5 T.also()

La función `T.also()` proporciona una funcionalidad similar a `T.apply()`, pero en la que el objeto sobre el que se ejecuta será pasado como argumento a la expresión lambda, y no como objeto receptor, de manera que dentro de la expresión lambda `this` seguirá teniendo el valor que tiene fuera de la expresión lambda.

Su definición resumida es:

**Definición de la función also()**

```kotlin
public inline fun <T> T.also(block: (T) -> Unit): T {
    block(this)
    return this
}
```

Rehaciendo el ejemplo que estudiamos en `T.apply()` empleando `also()`:

**Uso de la función also()**

```kotlin
data class Settings(var javaScriptEnabled: Boolean = false, var databaseEnabled: Boolean = false) {
    fun activate() {
        javaScriptEnabled = true
        databaseEnabled = true
    }
}

fun createInstance() = 
        // Se crea el objetos, se establece alguna de sus propiedades, se llama a un uno de sus métodos y se retorna el objeto ya construido.
        // El objetos Settings es accesible desde la expresión lambda a través de this.
        Settings().also { 
            it.javaScriptEnabled = true
            it.activate() 
        }

fun main() {
    val settings = createInstance()
    println(settings)
}
```

|Función|Receptor en Lambda|Valor Retornado|Uso Típico|
|---|---|---|---|
|**`with`**|`this` (El objeto pasado)|Resultado de la Lambda (`R`)|Configurar un objeto sin repetir su nombre.|
|**`T.run`**|`this` (El objeto receptor)|Resultado de la Lambda (`R`)|Configuración + Cálculo, o uso con tipos _nullable_ (`?.run`).|
|**`T.apply`**|`this` (El objeto receptor)|El Objeto Receptor (`T`)|Configuración/Inicialización (_Builder Pattern_).|
|**`T.let`**|`it` (El objeto receptor)|Resultado de la Lambda (`R`)|Comprobación de nulos (`?.let`) o Mapeo/Ejecución donde `this` es necesario fuera.|
|**`T.also`**|`it` (El objeto receptor)|El Objeto Receptor (`T`)|Efectos secundarios (Logging, Trazabilidad) sin alterar la cadena de llamadas.|

[Explicación en video](https://www.youtube.com/embed/ME1omdQZaJE)

> [!example] Práctica
> [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.12 · Scoping functions sobre Order|Ejercicio 10.12 · Scoping functions sobre Order]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Tipo función | `(Int, Int) -> Int` · `() -> Unit` · `((Int) -> Int)?` | Las funciones son objetos: se guardan, se pasan y se devuelven. Se ejecutan con `f(x)` o `f.invoke(x)`. |
| Varianza en tipos función | `(Int) -> Any` acepta `(Number) -> Int` | Parámetros contravariantes (`in`), retorno covariante (`out`). |
| `typealias` | `typealias IntBinaryOperation = (Int, Int) -> Int` | Solo es otro nombre: no crea un tipo nuevo. |
| Lambda | `{ x, y -> x + y }` · `{ it.age }` | Parámetros sin paréntesis; el último valor es el resultado; `it` si hay un único parámetro. |
| _Trailing lambda_ | `lista.maxByOrNull { it.age }` | Si el último parámetro es una función, la lambda va fuera de los paréntesis. |
| `return` en lambdas | `return@onUserChange` | Un `return` sin etiqueta sale de la función que contiene la lambda (si es inline). |
| Conversión SAM | `fun interface MyAction { fun execute() }` | Una lambda se convierte en la interfaz; en Kotlin hace falta `fun interface`. |
| Función anónima | `fun(a: Int, b: Int): Int = a + b` | Como una función sin nombre; su `return` es local. |
| _Closure_ | `var i = 0; return { i++ }` | La lambda captura variables de fuera y, si son `var`, puede modificarlas. |
| Referencia a función | `::add` · `Integer::sum` · `Number::times` · `obj::times` | Usa una función existente como objeto función. |
| `inline` | `inline fun repeat(times: Int, action: (Int) -> Unit)` | Copia el cuerpo en cada llamada: sin objetos lambda y con _non-local return_. |
| `reified` | `inline fun <reified T> f(a: T)` | Evita el _type erasure_: permite `is T` y `T::class`. |
| Tipo función con receptor | `StringBuilder.() -> Unit` | Dentro de la lambda, `this` es el receptor. |
| `with` / `run` | `with(obj) { … }` · `obj.run { … }` | `this` = objeto; devuelven el resultado de la lambda. |
| `apply` | `obj.apply { … }` | `this` = objeto; devuelve el objeto (configurar). |
| `let` | `obj?.let { … } ?: valor` | `it` = objeto; devuelve el resultado (comprobar nulos). |
| `also` | `obj.also { log(it) }` | `it` = objeto; devuelve el objeto (efectos secundarios). |

## Relaciones

- Ejercicios del tema: [[10.1 - Ejercicios 10 Programación funcional]]
- [[03 - Funciones]] — declaración de funciones, parámetros por defecto y funciones de expresión única.
- [[08 - POO III]] — _extension functions_ y funciones _top-level_, base de las lambdas con receptor y de las _scoping functions_.
- [[09 - Genéricos]] — varianza (`in`/`out`) y _type erasure_, que aquí reaparecen en los tipos función y en `reified`.
- [[05 - Operaciones con tipos nullables]] — `?.` y `?:`, que se combinan con `let`.
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Escribir el tipo función de una variable, de un parámetro y de un retorno.
- [ ] Explicar por qué `(Int) -> Any` acepta una función `(Number) -> Int`.
- [ ] Simplificar una lambda paso a paso: tipos inferidos, _trailing lambda_, sin paréntesis e `it`.
- [ ] Diferenciar el `return` de una lambda, de una lambda con etiqueta y de una función anónima.
- [ ] Explicar cuándo hay conversión SAM y para qué sirve `fun interface`.
- [ ] Crear un _closure_ que guarde estado entre llamadas.
- [ ] Usar los cinco tipos de referencia: _top-level_, estática, de método, de _extension function_ y ligada a instancia.
- [ ] Explicar qué hace `inline`, qué es un _non-local return_ y para qué sirven `crossinline`, `noinline` y `reified`.
- [ ] Convertir una función con parámetro `(T) -> R` en una con receptor `T.() -> R`.
- [ ] Elegir entre `with`, `run`, `apply`, `let` y `also` según el receptor (`this`/`it`) y el valor devuelto.
