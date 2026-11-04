---
asignatura: PMDM
tema: 9
tipo: tema
estado: completo
fecha: 2026-10-25
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-genericos
---

# 09 · Genéricos en Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 9 · Kotlin  
> Ejercicios: [[09.1 - Ejercicios 9 Genéricos]] · Tema anterior: [[08 - POO III]]

> [!info] Material de referencia
> [Genéricos en Kotlin](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b09%20-%20Genericos%20en%20Kotlin/)

## Índice del tema

- [[#1. Introducción a los genéricos]]
- [[#2. Funciones parametrizadas]]
- [[#3. Clases e interfaces parametrizadas]]
- [[#4. Genéricos y tipos nullables]]
- [[#5. Parámetros de tipo y herencia]]
- [[#6. Type erasure (borrado de tipo)]]
- [[#7. Restricciones en los parámetros de tipo]]
- [[#8. Star projection]]
- [[#9. Varianza (invarianza, covarianza y contravarianza)]]

---

## 1. Introducción a los genéricos

En las primeras versiones de Java, las estructuras de datos, como las listas, estaban diseñadas para aceptar elementos de cualquier tipo de dato. De hecho, si accedíamos a un elemento de una lista, se nos devolvía un objeto de tipo `Object`, lo que, en el mejor de los casos, nos obligaba a hacer _cast_ para convertir el objeto al tipo deseado.

**Lista sin genéricos de las primeras versiones de Java**

```java
void main() {
    List list = new ArrayList();
    list.add("Hello");
    String element = (String) list.get(0); // We need casting because get returns an Object
    System.out.println(element);
}
```

Como es de suponer, el uso de esas listas es complejo. Sería preferible poder especificar el tipo de los elementos de la lista, para poder estar seguros de que la lista solo puede contener elementos del tipo adecuado y no sea necesario hacer conversión de tipos cuando obtengamos un elemento de la lista. Éste fue uno de los principales motivos por los que Java introdujo los genéricos en su versión 5.

**Lista genérica en Java**

```java
void main() {
    List<String> list = new ArrayList<>();
    list.add("Hello");
    String element = list.get(0);
    System.out.println(element);
}
```

Dado que **Kotlin** fue creado mucho tiempo después, fue diseñado desde el inicio con soporte para genéricos y **todas las listas son genéricas**, de manera, que **estamos obligados a indicar el tipo** de los elementos cuando declaramos la lista.

El **polimorfismo paramétrico** es un concepto en programación orientada a objetos que se refiere a la **capacidad de escribir código que funcione de manera genérica con varios tipos de datos**. En el contexto de Kotlin, esto se logra a través de los tipos genéricos, que permiten escribir funciones, clases o interfaces que pueden trabajar con diferentes tipos de datos sin necesidad de repetir código.

Por ejemplo, en Kotlin puedes definir una función que trabaje con una lista de cualquier tipo de elementos utilizando un tipo genérico, como en el siguiente ejemplo:

**Función parametrizada en Kotlin**

```kotlin
fun <T> printList(list: List<T>) {
    for (element in list) {
        println(element)
    }
}

fun main() {
    val myList: List<String> = listOf("Baldomero", "Llegate", "Ligero")
    printList(myList)
}
```

En este caso, `<T>` indica que `T` es un parámetro de tipo, que durante la llamada puede recibir cualquier tipo de dato, como `Int`, `String`, etc. Esto permite que la función `printList` pueda ser utilizada con listas de enteros, de cadena, de clases propias, etc. Esto es una forma de polimorfismo paramétrico, ya que la misma función puede trabajar con diferentes tipos de datos, adquiriendo distintas "formas" dependiendo de los argumentos que se proporcionen durante la llamada para los parámetros de tipo(de ahí lo de polimorfismo).

**El polimorfismo paramétrico es una forma de polimorfismo estático**, ya que **se resuelve en tiempo de compilación**. Esto implica que, por ejemplo, en la llamada a una función genérica, el compilador debe tener claro los argumentos que se suministran para sus parámetros de tipo, para analizar si la llamada es correcta.

Debemos tener en cuenta que para mantener la compatibilidad con versiones antiguas, cuando Java incorporó los genéricos hizo que la especificación de tipos fuera opcional, de manera que si no se especifica se crea lo que se conoce como un _raw type_ (tipo en bruto), aunque evidentemente no se recomienda este uso de los genéricos.

Sin embargo, **dado que Kotlin incluye los genéricos desde su primera versión, los _raw types_ no están permitidos**, por lo que **es obligatorio especificar el tipo o que el compilador lo infiera a la hora de instanciar un genérico**.

> [!note] Comparación con Java
> En Java `List list = new ArrayList();` compila (con un aviso) y crea un _raw type_. En Kotlin `val list: List = listOf("A")` **no compila**: hay que escribir `List<String>` o dejar que el compilador lo infiera (`listOf("A")` ya es `List<String>`).

## 2. Funciones parametrizadas

De igual forma que los parámetros nos permiten en una función definir los elementos con la que ésta va a trabajar, **al declarar una función también podemos especificar parámetros de tipo para indicar los tipos de datos con los que queremos que trabaje** la función.

Para ello, la declaración incluirá, **después de la palabra reservada `fun` y antes del identificador** de la misma, **una lista de parámetros de tipo** con el formato `<T1, T2, ...>`. Por convención, los identificadores de los parámetros de tipo se escriben en **mayúscula** y suelen corresponder a una **única letra** (si solo hay un parámetro de tipo se le suele llamar `T`, por la palabra _type_).

**Estos parámetros de tipo pueden ser usados en el resto de la declaración de la función para**, por ejemplo **especificar el tipo de un determinado parámetro o el tipo de retorno de la función**. Por ejemplo:

**Definición de una función parametrizada**

```kotlin
fun <T> myFunction(input: T) {
    println(input)
}

fun main() {
    // Al llamar se proporciona el argumento de tipo
    myFunction<Int>(23)
    // El argumento de tipo se infiere del argumento proporcionado
    myFunction(23)
}
```

En la definición anterior, el parámetro de tipo `T` es usado para declarar el tipo del parámetro `input`.

Al igual que sucede con los parámetros de una función, para los que debemos proporcionar argumentos durante una llamada a la función, **cuando llamemos a una función parametrizada deberemos proporcionar argumentos para los parámetros de tipo** definidos en ella.

Para establecer los argumentos para los parámetros de tipo, **en la llamada, después del nombre de la función, podemos proporcionar una lista de tipos** con el formato `<Tipo1, Tipo2`>, con tantos tipos como parámetros de tipo tenga definida la función.

En el ejemplo `Int` se está usando como argumento del parámetro de tipo `T`.

No obstante, en muchas ocasiones, como el anterior, **el compilador puede inferir (adivinar) el argumento a partir de los tipos de los elementos proporcionados en la llamada**. Así, podemos llamar a la función genérica anterior sin indicar explícitamente el argumento para `T`, ya que el compilador puede inferirlo a partir del tipo del argumento proporcionado en la llamada para el parámetro `input`, y determinar que en este caso se trata del tipo `Int`.

Los parámetros de tipo en las funciones genéricas son de gran utilidad para el compilador, ya que les permite comprobar e inferir correctamente, por ejemplo, los tipos de los argumentos y el tipo de retorno de la función, de manera que el compilador nos protege de tratar de llevar a cabo operaciones ilegales, haciendo nuestros programas más seguros.

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.1 · Función genérica swapValues|Ejercicio 9.1 · Función genérica swapValues]]

## 3. Clases e interfaces parametrizadas

Podemos crear **clases genéricas añadiendo una lista de parámetros de tipo** con el formato `<T1, T2, ...>` **después del nombre de la clase**. Podemos **usar dichos parámetros por toda la clase**, como por ejemplo al especificar la clase de la que hereda, o la interfaz que implementa, o en el cuerpo de la clase, especialmente a la hora de especificar propiedades, y tipos de parámetros y de retorno de métodos de la clase. Por ejemplo:

**Definición de una clase parametrizada**

```kotlin
class ValueWithHistory<T>(
    private var value: T
) {
    private var history: List<T> = listOf(value)

    fun setValue(value: T) {
        this.value = value
        this.history += value // New immutable list
    }

    fun currentValue(): T = value

    fun history(): List<T> = history
}

fun main() {
    val letter = ValueWithHistory<String>("A")
    letter.setValue("B")
    println(letter.history()) // [A, B]
    val letter2: ValueWithHistory<Any> = ValueWithHistory("A")
}
```

**Cuando creemos una instancia de la clase deberemos proporcionar los argumentos para los parámetros de tipo, aunque en algunas ocasiones el compilador será capaz de inferirlos**, por ejemplo a partir de los tipos de los argumentos proporcionados para los parámetros del constructor, o del tipo de la variable a la que se asigna la instancia a crear. Así en el ejemplo anterior, con `letter2` no indicamos el argumento de tipo en el constructor (`ValueWithHistory("A")`), porque el compilador lo deduce del tipo de la variable (`ValueWithHistory<Any>`).

**Las interfaces también pueden ser genéricas**, lo que tiene consecuencias similares al caso de la clases: lo parámetros de tipo especificados pueden ser usados dentro del cuerpo de la interfaz como tipo de propiedades, tipo parámetros de métodos y tipo de retorno de métodos. Por ejemplo:

**Declaración y uso de una interfaz parametrizada**

```kotlin
interface MyConsumer<T> {
    fun consume(value: T)
}

fun main() {
    val myConsumer = object : MyConsumer<String> {
        override fun consume(value: String) {
            println(value)
        }
    }
    myConsumer.consume("Hello")
}
```

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.2 · Clase genérica DataStore|Ejercicio 9.2 · Clase genérica DataStore]]

## 4. Genéricos y tipos nullables

Debemos tener en cuenta que **los argumentos suministrados para parámetros de tipo pueden corresponder a tipos nullables**. Por ejemplo, para la clase anterior podemos crear la siguiente instancia:

**Creación de instancias de una clase parametrizada proporcionando un tipo nullable**

```kotlin
class ValueWithHistory<T>(
    private var value: T
) {
    private var history: List<T> = listOf(value)

    fun setValue(value: T) {
        this.value = value
        this.history += value // New immutable list
    }

    fun currentValue(): T = value

    fun history(): List<T> = history
}

fun main() {
    val letter = ValueWithHistory<String?>(null)
    letter.setValue("B")
    println(letter.history()) // [null, B]
}
```

Por otra parte, **cuando usamos un parámetro de tipo dentro de una clase, interfaz o función, podemos especificar su versión nullable a partir de él**. Así, aunque el parámetro de tipo sea `T`, dentro de la clase o función podemos hacer referencia a su versión nullable `T?`. Por ejemplo:

**Especificación como nullable de un parámetro de tipo**

```kotlin
class Box<T> {
    var value: T? = null
    fun getOrThrow(): T = value!!
}    

fun main() {
    val box = Box<String>()
    box.value = "Hello"
    println(box.getOrThrow())
}
```

El caso contrario también puede hacerse, esto es, **especificar que aunque el argumento recibido para el parámetro sea de tipo nullable, queremos representar su versión no nullable**. Para ello **especificaremos `T & Any`**. Por ejemplo:

**Especificación de la versión no nullable de un parámetro de tipo**

```kotlin
// Aunque el argumento para T sea un tipo nullable, la función retornará siempre 
// la versión no nullable del argumento recibido.
fun <T> T.orThrow(): T & Any = this ?: throw Error()

fun main() {
    val myString: String? = "Baldomero"
    val myStringNotNull: String = myString.orThrow()
    println(myStringNotNull)
}
```

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.3 · Clase NullableWrapper con T?|Ejercicio 9.3 · Clase NullableWrapper con T?]]

## 5. Parámetros de tipo y herencia

**Las clases pueden heredar de clases parametrizadas y/o implementar interfaces parametrizadas. Las interfaces puede a su vez heredar de interfaces parametrizadas**. En todos estos casos, al declarar la clase o interfaz es obligatorio especificar los argumentos para los parámetros de tipo de las clases o interfaces parametrizadas de las que heredan o implementan.

De hecho, es muy habitual que una clase o interfaz parametrizada herede de otra clase o interfaz parametrizada, y también es muy común, aunque no obligatorio, que use su propio parámetro de tipo como argumento del parámetro de tipo de la clase o interfaz de la que hereda. Por ejemplo, la interfaz `MutableList<E>` hereda de las interfaces `List<E>` y de `MutableCollection<E>`, y lo especificamos de la siguiente manera (en la estrucuturas de datos el parámetro de tipo recibe el nombre `E` de elemento en vez de `T`):

**Uso de parámetro de tipo como argumento de un parámetro de tipo de una clase o interfaz de la que se hereda**

```kotlin
// El parámetro de tipo E de MutableBox es usado como argumento para el parámetro
// de tipo de Box y Wrapper
interface Box<E> {
    fun get(): E
}
interface Wrapper<E> {
    fun wrapped(value: E)
}
interface MutableBox<E> : Box<E>, Wrapper<E> {
    fun set(value: E)
}

fun main() {
    val box: MutableBox<String> = object : MutableBox<String> {
        private var value: String? = null
        override fun get(): String = value!!
        override fun set(value: String) {
            this.value = value
        }
        override fun wrapped(value: String) {
            this.value = "Wrapped $value"
        }
    }
    box.set("Hello")
    println(box.get()) // Hello
    box.wrapped("World")
    println(box.get()) // Wrapped World
}
```

En estos casos, debemos tener en cuenta que los parámetros de tipo de la clase hija y de la clase padre son completamente independientes y no debemos confundirlos, incluso si tienen el mismo nombre.

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.4 · Jerarquía genérica Container y SimpleStorage|Ejercicio 9.4 · Jerarquía genérica Container y SimpleStorage]]

## 6. Type erasure (borrado de tipo)

**Los genéricos** fueron añadidos en Java 5 por su conveniencia para los desarrolladores, pero **en realidad nunca fueron implementados dentro de la JVM** (máquina virtual de Java), principalmente por mantener la compatiblidad con el código existente de versiones anteriores a Java 5, que usaba, por ejemplo, listas no parametrizadas.

Por este motivo, se optó por realizar con los genéricos lo que se conoce como **_type erasure_** (borrado de tipos), que indica que **al compilar** el código a _bytecode_ **se pierde la información sobre los tipos especificados para los genéricos**, de manera que en _bytecode_ un `List<String>` es representado como un `List`, y que un `List<Double>` también es representado como un `List`.

Esta pérdida de información implica que **vamos a tener una serie de restricciones en tiempo de ejecución**, ya que realmente no se va a conocer el tipo de la clase o interfaz parametrizada. Por ejemplo: **NO vamos a poder comprobar si el tipo del elemento es un tipo de terminado usando `is`, ni vamos a poder instanciar objetos del tipo parametrizado mediante `T()`, ni llamar a métodos del objeto compañero de éste**, etc., ya que la información sobre qué tipo real corresponde al parámetro tipo no está disponible en tiempo de ejecución.

**Consecuencias del type erasure**

```kotlin
import kotlin.reflect.typeOf

fun <T> example(a: Any) {
    val check = a is T // ERROR
    val ref = T::class // ERROR
    val type = typeOf<T>() // ERROR
    val instance = T() // ERROR
}

fun main() {
    example<String>("Hello")
}
```

Sin embargo, como veremos más adelante, **Kotlin puede superar algunas de estas limitaciones a través de las conocidas como _inline functions_ con argumentos de tipo materializables (_reified_)**, que estudiaremos dentro de poco.

## 7. Restricciones en los parámetros de tipo

Una funcionalidad muy importante de los genéricos es que **podemos restringir los parámetros de tipo para que solo puedan recibir como argumento tipos que sean de un determinado tipo o subtipo de éste**. Por ejemplo, si queremos crear una función `fun <T> maxOf(valor1: T, valor2: T)` genérica que calcule el máximo de dos valores de tipo `T`, debemos exigir que el tipo que pasemos como argumento del parámetro de tipo `T` sea un `Comparable<T>` o un subtipo de él, ya que para obtener el máximo es necesario que los dos valores pasados como argumento se puedan comparar.

Para restringir los argumentos que podemos pasar a un parámetro de tipo, al especificar este último deberemos indicar que es un subtipo del tipo al que queramos restringir, **usando `: tipo`**, de la siguiente forma:

**Función parametrizada con parámetro de tipo restringido**

```kotlin
import java.math.BigDecimal

fun <T : Comparable<T>> maxOf(a: T, b: T): T {
    return if (a >= b) a else b
}

// Clase no comparable
class A { }

fun main() {
    val maximum = maxOf(BigDecimal("10.00"), BigDecimal("11.00"))
    println(maximum) // 11.00
    maxOf(A(), A()) // ERROR de compilación: A no es Comparable<A>
}
```

Podemos usar la restricción de parámetro de tipo **no solo en funciones parametrizadas sino también en clases e interfaces parametrizadas**. Así en el siguiente ejemplo la clase `ListAdapter` debe recibir como argumento para el parámetro de tipo `T` el tipo `ItemAdapter` o alguno de sus subtipos:

**Clase parametrizada con parámetro de tipo restringido**

```kotlin
open class ListAdapter<T : Item>( /*...*/ ) { 
    // ...
}

interface Item { }
class MyItemType: Item { }
class NotAnItemType {}
class MyListAdapter: ListAdapter<MyItemType> { }
class NotMyListAdapter: ListAdapter<NotAnItemType> { } // ERROR DE COMPILACIÓN

fun main() {
    val adapter = MyListAdapter<MyItemType>()
    val notAdapter = NotMyListAdapter<NotAnItemType>()
}
```

> [!warning] Ojo con el ejemplo
> Además del error intencionado (`NotAnItemType` no es un `Item`), el ejemplo de los apuntes no compila tal cual: al heredar hay que llamar al constructor (`ListAdapter<MyItemType>()`), y `MyListAdapter` no es genérica, así que se instancia con `MyListAdapter()`, sin `<MyItemType>`.

Algo muy importante cuando restringimos los argumentos posibles de un parámetro de tipo es que **dentro de la función, clase o interfaz parametrizada, estamos completamente seguros de que el parámetro de tipo debe ser el tipo al que se ha restringido o un subtipo de éste, por lo que podemos usar con seguridad las propiedades y métodos de dicho tipo**, ya que obligatoriamente estarán presentes en un objeto cuyo tipo corresponda al parámetro de tipo.

Por ejemplo, en el código de la función `maxOf` anterior estamos seguros de los parámetros `a` y `b` tienen que ser de un tipo que implemente forzosamente la interfaz `Comparable<T>`. Por tanto, el compilador nos va a permitir ejecutar sobre ellos métodos de la interfaz `Comparable<T>`, ya que el compilador sabe que `a` y `b` forzosamente implementan esa interfaz:

**Función parametrizada con parámetro de tipo restringido**

```kotlin
import java.math.BigDecimal

fun <T : Comparable<T>> maxOf(a: T, b: T): T {
    return if (a.compareTo(b) > 0) a else b
}

fun main() {
    val maximum = maxOf(BigDecimal("10.00"), BigDecimal("11.00"))
    println(maximum) // 11.00
}
```

En muy raras ocasiones debemos restringir los posibles argumentos para un parámetro de tipo estableciendo **varias restricciones**, en cuyo caso **usaremos `where T: tipo1, T: tipo2`** para especificarlas. Así, en el siguiente ejemplo establecemos que el argumento que se indique para el parámetro de tipo `T` debe implementar tanto la interfaz `Animal` como la interfaz `GoodTempered`:

**Función parametrizada con parámetro de tipo restringido con varias restricciones**

```kotlin
interface Animal {
    fun feed()
}

interface GoodTempered {
    fun pet()
}

class Dog : Animal, GoodTempered {
    override fun feed() {
        println("Feeding the dog")
    }
    override fun pet() {
        println("Petting the dog")
    }
}

class Crocodrile : Animal {
    override fun feed() {
        println("Feeding the crocodrile")
    }
}

fun <T> petAndFeed(animal: T) where T : Animal, T : GoodTempered {
    animal.pet()
    animal.feed()
}

fun main() {
    val dog = Dog()
    petAndFeed(dog)
    val crocodrile = Crocodrile()
    // ERROR DE COMPILACIÓN: Crocodrile no implementa GoodTempered
    petAndFeed(crocodrile)
}
```

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.5 · Restricciones con Identifiable, Loggable y where|Ejercicio 9.5 · Restricciones con Identifiable, Loggable y where]]

## 8. Star projection

En algunas ocasiones, el argumento que debemos pasar a un parámetro de tipo no nos es significativo. Por ejemplo, si simplemente queremos verificar que una variable es una lista, realmente nos da quien de qué tipo sean los elementos de dicha lista. Sin embargo la sintaxis nos obliga a pasar un argumento para dicho parámetro de tipo, ya que, a diferencia de en Java, en Kotlin es obligatorio que indiquemos explícitamente el argumento con el que sustituir un parámetro de tipo a no ser que el compilador sea capaz de inferirlo.

En estos casos **podemos usar `*` como argumento para el parámetro de tipo, que representa "cualquier tipo", o dicho de otra forma, que no estamos interesados en dicho tipo**. A esta opción se le conoce como **_star projection_** (proyección estrella).

**Comprobación de tipo lista con star projection**

```kotlin
fun main() {
    val list = listOf("A", "B")
    println(list is List<*>) // true
}
```

También **podemos usar la _star projection_ al indicar el tipo de una función**. Por ejemplo, en la siguiente función nos es indiferente el tipo de los elementos de la lista, porque lo único que queremos es imprimir su tamaño:

**Parámetro con tipo lista con star projection**

```kotlin
fun printSize(list: List<*>) {
    println(list.size)
}

fun main() {
    printSize(listOf("A", "B"))
    printSize(listOf(1, 2, 3))
}
```

Cuando usamos la _star projection_ como argumento, `*` será equivalente a `Any?` cuando se obtenga datos de la clase parametrizada, y será equivalente a `Nothing` cuando se use como tipo de parámetros de métodos de la clase parametrizada. Por este motivo no es lo mismo una `MutableList<Any?>` que una `MutableList<*>`.

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.6 · Star projection en inspectContainer|Ejercicio 9.6 · Star projection en inspectContainer]]

## 9. Varianza (invarianza, covarianza y contravarianza)

Como hemos visto, el hecho de que un tipo A sea subtipo de otro tipo B significa que puede emplearse un objeto del tipo A en sustitución de uno de tipo B. Digamos que **"es un subtipo de ..." significa a efectos prácticos "se puede usar donde se espera un ..."**. Por ejemplo: si un el tipo `Cat` es un subtipo del tipo `Animal`, podemos usar un objeto `Cat` allá donde se nos requiera un objeto `Animal`.

Si embargo, cuando usamos los genéricos la cosa se complica. Así, podríamos hacernos la siguiente pregunta: ¿Si `Cat` es un subtipo de `Animal`, podemos usar una lista de gatos `List<Cat>` siempre en sustitución de una lista de animales `List<Animal>`?. La respuesta depende de las operaciones que se puedan hacer con la lista, aunque en la mayoría de las ocasiones, la respuesta es NO. El motivo tiene que ver con la varianza, como vamos a estudiar.

Supongamos que pedimos una bolsa de frutas de la queremos sacar frutas, y nos dan como respuesta una bolsa de manzanas. Hemos sustuido algo más genérico que pedimos (fruta) por algo más concreto (manzana). Como lo que originalmente queríamos era sacar frutas de la bolsa, lo que nos entregan, una bolsa de manzanas, nos será válida, porque cada manzana que saquemos de la bolsa será una fruta, ya que una manzana es una fruta. Este es el concepto de **covarianza**, y funciona cuando vamos a sacar elementos (**`out`**).

Supongamos ahora que pedimos un exprimidor de naranjas, al que se le puedan meter naranjas para que nos haga zumo. Sin embargo, nos entregan en respuesta un exprimidor de cualquier fruta. He sustituido algo más concreto que pedimos (naranja) por algo más genérico (fruta). Como lo que originalmente queríamos era meter naranjas en el exprimidor, lo que nos entregan, nos será válido, porque cada naranja que metamos en el exprimidor de frutas es una fruta con la que hacer zumo. Estes es el concepto de **contravarianza**, y funciona cuando vamos a meter elementos (**`in`**).

La **varianza** se refiere a **cómo la subtipificación de tipos que utilizan otros tipos** (por ejemplo una lista de elementos de un determinado tipo) **se relaciona con la subtipificación de los tipos que utilizan** (el tipo de los elementos de la lista).

En la **covarianza** la subtipificación de tipos que utilizan otros tipos (la bolsa de la que sacar elementos) sigue el **mismo sentido** que la subtipificación de tipos del tipo que usan (el tipo de elementos de la bolsa). De ahí que la palabra covarianza tenga el prefijo **"co"**, ya que **ambos varían en el mismo sentido**. Así, en el primer ejemplo, si una manzana es un subtipo de fruta, una bolsa de la que extraer manzanas es un subtipo de una bolsa de la que extraer frutas. Ambas subtipificaciones van en el mismo sentido.

Formalmente, **la covarianza significa que si A es un subtipo de B, entonces un tipo I que usa A es un subtipo de un tipo I que usa B**.

Por ejemplo, **en la interfaz `Iterator<T>` el tipo `T` es covariante, ya que solo se utiliza como tipo de salida**, y no tiene ningún método público que reciba un parámetro de dicho tipo. Digamos que la intefaz **"produce" elementos de tipo `T`, pero nunca los "consume"**.

**Ejemplo de uso de interfaz parametrizable con tipo covariante**

```kotlin
public interface Iterator<out T> {
    public operator fun next(): T
    public operator fun hasNext(): Boolean
}
```

El hecho de que se haya definido el parámetro de tipo `T` como covariante permite que, por ejemplo, podamos asignar a una variable de tipo `Iterator<Any>` una de tipo `Iterator<Int>`, ya que es seguro hacerlo, puesto que nunca se puede pasar un valor de tipo `Any` a dicho objeto, ya que la interfaz no incluye ningún método o propiedad para ello:

**Ejemplo de definición de interfaz parametrizable con tipo covariante**

```kotlin
val intIterator: Iterator<Int> = listOf(1, 2, 3).iterator()
val anyIterator: Iterator<Any> = intIterator
```

En la **contravarianza** la subtipificación de tipos que utilizan otros tipos (el exprimidor para hacer zumo que recibe elementos) va **en el sentido contrario** a la subtipificación de tipos del tipo que usan (el tipo de elementos que se le echan). De ahí que la palabra contravarianza tenga el prefijo **"contra"**, ya que **va en sentido contrario**. Así, en el segundo ejemplo, aunque una naranja es un subtipo de fruta (un sentido), un exprimidor a la que se le echa naranjas es un supertipo de un exprimidor al que se le echa fruta (sentido contrario). Como vemos las dos subtipificaciones van en sentido contrario. Recuerda que "es un subtipo de ..." significa a efectos prácticos "se puede usar donde se espera un ...".

Formalmente, **la contravarianza significa que si A es un subtipo de B, entonces un tipo I que usa B es un subtipo de un tipo I que usa A**. Se invierte.

Por ejemplo, en esta **interfaz `Comparator<T>` el tipo `T` es contravariante, ya que solo se utiliza como tipo de entrada**, y no tiene ningún método público o getter de propiedad pública de dicho tipo. Digamos que la intefaz "consume" elementos de tipo `T`, pero nunca los "produce".

**Ejemplo de definición de interfaz parametrizable con tipo contravariante**

```kotlin
public interface Comparator<in T> {
    fun compare(a: T, b: T): Int
}
```

El hecho de que se haya definido el parámetro de tipo `T` como contravariante permite que, por ejemplo, podamos asignar a una variable de tipo `Comparator<Int>` y expresión de tipo `Comparator<Any>`, ya que es seguro hacerlo, puesto que nunca se puede obtener un valor de tipo `Any` a través de dicho objeto, ya que la interfaz no incluye ningún método o propiedad para ello:

**Ejemplo de uso de interfaz parametrizable con tipo contravariante**

```kotlin
val anyComparator: Comparator<Any> = Comparator { _, _ -> -1 }
val intComparator: Comparator<Any> = anyComparator
```

> [!warning] Ojo con el ejemplo
> El texto dice que asignamos a un `Comparator<Int>`, pero el código de los apuntes declara `intComparator` como `Comparator<Any>`, así que en realidad no se ve la contravarianza. Y si lo cambias a `Comparator<Int>`, **no compila**: en Kotlin/JVM, `Comparator` es el `java.util.Comparator` de Java, que no lleva `in`. Para verlo funcionar hay que usar una interfaz propia (comprobado con `kotlinc`):
>
> ```kotlin
> interface MyComparator<in T> {
>     fun compare(a: T, b: T): Int
> }
>
> fun main() {
>     val anyComparator: MyComparator<Any> = object : MyComparator<Any> {
>         override fun compare(a: Any, b: Any): Int = a.hashCode() - b.hashCode()
>     }
>     // Contravarianza: un comparador de Any sirve como comparador de Int
>     val intComparator: MyComparator<Int> = anyComparator
>     println(intComparator.compare(1, 2))
> }
> ```

Entonces, **¿siempre se puede usar covarianza y contravarianza? La respuesta es un contundente NO**, si es que queremos mantener la seguridad del tipo.

Para entenderlo, modifiquemos nuestro primer ejemplo. Supongamos que pedimos una bolsa de frutas de la que no solo queremos sacar frutas, sino en la que además queremos meter frutas, y nos entregan como respuesta una bolsa de manzanas. Hemos sustuido algo más genérico que pedimos (fruta) por algo más concreto (manzana). ¿Es seguro en este caso, aplicar la convarianza? Pues NO, porque si nos entregan una bolsa de manzanas en sustitución de una bolsa de fruta, no vamos a poder meter en ella una fruta que no sea una manzana. **La covarianza solo es segura si el tipo solo se usa como tipo de salida**.

Cuando hablamos de que un tipo solo actúa como tipo de salida, nos referimos a que solo aparece como tipo de retorno de métodos públicos (y no como tipo de parámetros de esos métodos), o como tipo de propiedades con getter público. Podríamos decir que la función, clase o interfaz parametrizada solo es "productora" de valores de este tipo.

El método `sacar(): T` de la bolsa retorna un elemento del tipo `T`, esto es, `T` actúa como tipo de salida (_out type_), y en ese caso es seguro usar la covarianza, porque si nos entregan una bolsa de manzanas en sustitución de una bolsa de frutas, cuando llame al método `sacar()` se me devolverá una manzana, que es una fruta.

Sin embargo, el método `meter(elemento: T)` de la bolsa recibe un elemento de tipo `T`, esto es, `T` actúa como tipo de entrada (_in type_), y en ese caso NO es seguro usar la covarianza, porque si nos entregan una bolsa de manzanas en sustitución de una bolsa de frutas, cuando llamara al método `meter(fruta)` proporcionándole cualquier fruta, se produciría un error en tiempo de ejecución, ya que la bolsa que le he entregado solo admite manzanas. Por tanto la covarianza NO es seguro si el tipo se usa como tipo de entrada.

De igual forma, modifiquemos nuestro segundo ejemplo, para suponer que al exprimidor de zumos, no solamente pudiéramos meterle naranjas, sino que también quisiéramos sacar naranjas de él. En ese caso el método `meter(elemento: T)` es seguro de usar con contravarianza, ya que si me entregan un exprimidor de fruta en sustitución de un exprimidor de naranjas, puede meter una naranja en el exprimidor de fruta porque una naranja es una fruta. Sin embargo, el método `sacar(): T` para sacar una naranja del exprimidor no será seguro si usamos contravarianza, ya que si nos entregan un exprimidor de fruta en sustitución de un exprimidor de naranjas, el elemento retornado por el método `sacar()` puede ser cualquier fruta, y yo espero específicamente una naranja. Por tanto, **la contravarianza solo es segura si el tipo solo se usa como tipo de entrada**.

Cuando hablamos de que un tipo solo actúa como tipo de entrada, nos referimos a que solo aparece como tipo de parámetros de métodos públicos (y no como tipo de retorno de esos métodos ni como tipo de propiedades con getter público). Podríamos decir que la función, clase o interfaz parametrizada solo es "consumidora" de valores de este tipo.

¿Y entonces qué podemos hacer en estos casos en los que tenemos operaciones donde el tipo `T` es tipo de salida y operaciones en los que `T` es tipo de salida? La respuesta es sencilla: no permitir ni la covarianza ni la contravarianza, o lo que es lo mismo, la **invarianza**. De hecho, en realidad como la invarianza es la opción más segura, aunque también la más restrictiva, es el comportamiento por defecto cuando no usamos ni `out` ni `in` al especificar un parámetro de tipo.

En el fondo, el hecho de indicar `out` o `in` es simplemente una forma que tiene el desarrollador de informar (prometer) al compilador del uso que se va a dar a dicho parámetro de tipo, para que el compilador no sea tan restrictivo en la comprobación de tipos en el código cliente de la función, clase o interfaz parametrizada. De hecho, si por ejemplo usamos `out` y después usamos dicho parámetro de tipo como tipo de entrada, se nos mostrará un error de compilación.

> [!note] Comparación con Java
> En Java la varianza se indica **en cada uso** con comodines: `List<? extends Fruta>` equivale a `out` (covarianza) y `List<? super Manzana>` equivale a `in` (contravarianza). En Kotlin se puede indicar **una sola vez en la declaración** (`interface Producer<out T>`), y así no hay que repetirlo cada vez que se usa el tipo.

Por tanto, **la invarianza significa que el hecho de que A sea un subtipo de B, no implica que un tipo I que usa A tenga ningún tipo de relación de subtipo/supertipo con un tipo I que usa B**.

Pongámonos en el caso de la estructura de datos lista. Si queremos que una lista de gatos sea un subtipo de una lista de animales, entonces el parámetro de tipo debe ser covariante. Pero para mantener la seguridad del tipo eso requeriría que la lista sea solo de lectura, es decir, que actúe únicamente como fuente de datos. Esto, en cierta manera es posible, si creamos un tipo de datos correspondiente a una lista inmutable (en la que no se pueden cambiar sus datos), podemos aplica covarianza, ya que no habrá ninguna operación de reciba un elemento del tipo `T`, sino todo operaciones que retornen elementos de tipo `T`, de manera que el tipo `T` será un tipo única de salida (_out type_). Este es el caso de la interfaz `List<T>` definida en la librería estándar de Kotlin, que representa listas inmutables.

**Definición en la interfaz List en la librería estándar de Kotlin**

```kotlin
public interface List<out E> : Collection<E> {
    override val size: Int
    override fun isEmpty(): Boolean
    override fun contains(element: @UnsafeVariance E): Boolean
    override fun iterator(): Iterator<E>
    override fun containsAll(elements: Collection<@UnsafeVariance E>): Boolean
    public operator fun get(index: Int): E
    public fun indexOf(element: @UnsafeVariance E): Int
    public fun lastIndexOf(element: @UnsafeVariance E): Int
    public fun listIterator(): ListIterator<E>
    public fun listIterator(index: Int): ListIterator<E>
    public fun subList(fromIndex: Int, toIndex: Int): List<E>
}
```

Al indicar un parámetro de tipo como covariante o contravariante, el compilador establece restricciones sobre el uso que se puede dar a dicho parémtro de tipo dentro de la clase, interface o función parametrizada, de manera que, por ejemplo, produce un error de compilación si usamos un parámetro de tipo convariente como tipo de un parámetro de un método.

Sin embargo, hay ocasiones en las que, debido a la funcionalidad del método, es seguro usar un parámetro de tipo convariante en posiciones de entrada, ya que el valor recibido no será almacenado ni, por tanto, podrá ser retornado, con lo que no podrían violarse la covarianza indicada. Sin embargo, el compilador no es capaz por sí solo de saber que en ese caso es segura dicha varianza.

Para estos casos aplica la **anotación `@UnsafeVariance` a un parámetro de tipo, para que el desarrollador pueda indicarle al compilador que el uso de dicho parámetro tipo en el método tal y como está, a pesar de la varianza especificada para él**. Este el el caso de, por ejemplo, el método `fun contains(element: @UnsafeVariance E): Boolean` de la interfaz `List<out E>`, que recibe como parámetro un elemento del tipo `E` convariante, algo que el compilador debería prohibir. Sin embargo, dado que el elemento solo se va a utilizar para comprobar si está o no en la lista, y no se va a almacenar ni retornar, es seguro usarlo como tipo de entrada al método aunque sea convariante.

Hablemos ahora de la posibilidad de que quisíeramos que la lista fuera contravariante. Esto obligaría, para que fuera segura, que la lista fuera solo de escritura, de manera que solo tuviera operaciones que reciban elementos de tipo `T`, pero no operaciones que retornaran elementos de tipo `T`, de manera que `T` fuera un tipo solo de entrada (_in type_), es decir, que actúe únicamente como consumidor de datos. Pero esto no tiene sentido: ¿para qué queremos una lista en la que podemos meter elementos, pero no podemos sacarlos ni consultarlos?.

Por tanto, en el caso de que queramos una lista mutable en la que se puedan tanto meter como sacar elementos, ésta deberá ser invariante, si es que queremos mantener la seguridad de tipos. Este es el caso de la interfaz `MutableList<T>` definida en la librería estándar de Kotlin, que representa listas mutables.

**Definición en la interfaz MutableList en la librería estándar de Kotlin**

```kotlin
public interface MutableList<E> : List<E>, MutableCollection<E> {
    override fun add(element: E): Boolean
    override fun remove(element: E): Boolean
    override fun addAll(elements: Collection<E>): Boolean
    public fun addAll(index: Int, elements: Collection<E>): Boolean
    override fun removeAll(elements: Collection<E>): Boolean
    override fun retainAll(elements: Collection<E>): Boolean
    override fun clear(): Unit
    public operator fun set(index: Int, element: E): E
    public fun add(index: Int, element: E): Unit
    public fun removeAt(index: Int): E
    override fun listIterator(): MutableListIterator<E>
    override fun listIterator(index: Int): MutableListIterator<E>
    override fun subList(fromIndex: Int, toIndex: Int): MutableList<E>
}
```

La mayoría de los lenguajes de programación que admiten varianza permiten contravarianza en entrada y covarianza en salida. En Kotlin, **para indicar que un tipo `T` es covariante especificaremos antes de él la palabra reservada `out`, para indicar que se trata de un tipo de salida. Para indicar que se trata de un tipo contravariante, usaremos la palabra reservada `in`, haciendo constar que se trata de un tipo de entrada**. Si queremos el que el tipo sea invariante, simplemente no especificaremos ninguna palabra clave, ya que se trata del comportamiento por defecto.

En Kotlin, podemos usar `out` e `in` al especificar los tipos en clases parametrizables, interfaces parametrizables y funciones top-level parametrizables. Las funciones top-level pueden ser contravariantes en la entrada y covariantes en la salida, es decir, contravariantes en los tipos de los parámetros y covariantes en los tipos de retorno.

Veamos un resumen de convarianza, contravarianza e invarianza:

- La **covarianza** es para los tipos que **producen** o **dan** valores. Piensa en un grifo del que solo sale líquido.

    - **Símil**: Necesitamos un `Grifo<Líquido>` y nos pasan un `Grifo<Cerveza>`. ¿Nos sirve?. Sí, perfectamente, porque cada vez que abramos el grifo, saldrá `Cervez`, y la cerveza es un `Liquido`. La relación se mantiene en la misma dirección: si `Cerveza` se puede usar como `Líquido`, un `Grifo<Cerveza>` se puede usar como `Grifo<Líquido>`.
    - **Palabra clave**: `out` (fuera/salida), porque el valor solo **sale** del objeto.
    - **Regla nemotécnica**: **`out` = Salida = Productor = Covarianza.**
- La **contravarianza** es para los tipos que **consumen** o **aceptan** valores. Piensa en una licuadora en el que solo echas fruta.

    - **Símil**: Necesitamos una `Licuadora<Manzana>` y nos pasan una `Licuadora<Fruta>`. ¿Nos sirve?. Sí, perfectamente, porque una `Licuadora<Fruta>` está preparada para recibir cualquier fruta, así que sin duda podemos licuar nuestras manzanas. La relación de tipos se invierte (va a la "contra"): si `Manzana` se puede usar como `Fruta`, una `Licuadora<Fruta>` se puede usar como `Licuadora<Manzana>`.
    - **Palabra clave**: `in` (dentro/entrada), porque el valor solo **entra** en el objeto.
    - **Regla nemotécnica**: **`in` = Entrada = Consumidor = Contravarianza.**
- La **invarianza** es para los tipos que **producen y consumen** valores. Piensa en una bolsa, donde podemos meter elementos pero tambien sacarlos.

    - **Símil**: Necesitamos una `Bolsa<Fruta>` donde puedes meter y sacar frutas. Si nos pasan una `Bolsa<Manzana>`. ¿Nos sirve?. No, es peligroso. Podríamos sacar una `Manzana` (que es una `Fruta`, con eso no hay problema), pero si intentamos meter una `Pera` (que es una `Fruta`) en la `Bolsa<Manzana>`, romperíamos la bolsa, porque solo está preparada para manzanas. La jerarquía de tipos no se mueve. `Bolsa<Manzana>` y `Bolsa<Fruta>` no tienen ninguna relación de subtipo entre ellos. Son tipos completamente diferentes.
    - **Palabra clave**: Ninguna. Es el comportamiento por defecto (cuando no usas ni `in` ni `out`).
    - **Regla memotécnica**: **Invarianza = Inflexible o Inmóvil = Entrada y Salida = Productor y Consumidor.**

|Varianza|Palabra Clave|Dirección del Flujo|Símil|Relación de Tipos (`Manzana` es `Fruta`, `Cerveza` es `Líquido`)|
|---|---|---|---|---|
|**Covarianza**|`out`|Solo **Salida** (Productor)|Grifo|`Grifo<Cerveza>` **es un** `Grifo<Liquido>` (Misma dirección)|
|**Contravarianza**|`in`|Solo **Entrada** (Consumidor)|Licuadora|`Licuadora<Fruta>` **es un** `Licadora<Manzana>` (Dirección contraria)|
|**Invarianza**|(ninguna)|**Entrada y Salida**|Bolsa|`Bolsa<Manzana>` **no es** `Bolsa<Fruta>` (no puedes meter en ella una `Pera`)|

> [!example] Práctica
> [[09.1 - Ejercicios 9 Genéricos#Ejercicio 9.7 · Varianza con DataProducer y DataConsumer|Ejercicio 9.7 · Varianza con DataProducer y DataConsumer]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Función parametrizada | `fun <T> printList(list: List<T>)` | El parámetro de tipo va entre `fun` y el nombre; el argumento suele inferirse. |
| Clase / interfaz parametrizada | `class Box<T>(var value: T)` · `interface MyConsumer<T>` | `T` se usa en propiedades, parámetros y retornos. |
| Sin _raw types_ | `List<String>`, nunca `List` | Kotlin obliga a indicar o inferir el argumento de tipo. |
| Tipos nullables | `Box<String?>`, `T?`, `T & Any` | `T` puede ser nullable; `T?` lo hace nullable y `T & Any` lo hace no nullable. |
| Herencia con genéricos | `interface MutableBox<E> : Box<E>` | Al heredar hay que dar argumento a los parámetros de tipo del padre. |
| _Type erasure_ | `a is T`, `T()` → error | En ejecución no se conoce `T`: no se puede comprobar ni instanciar. |
| Restricción (_upper bound_) | `fun <T : Comparable<T>> maxOf(a: T, b: T)` | Solo admite `T` del tipo indicado o subtipos, y permite usar sus métodos. |
| Varias restricciones | `where T : Animal, T : GoodTempered` | `T` debe cumplir todas. |
| _Star projection_ | `List<*>` | "Cualquier tipo": se lee como `Any?` y no se puede escribir (`Nothing`). |
| Covarianza | `interface Producer<out T>` | Solo produce `T`: `Producer<Manzana>` sirve como `Producer<Fruta>`. |
| Contravarianza | `interface Consumer<in T>` | Solo consume `T`: `Consumer<Fruta>` sirve como `Consumer<Manzana>`. |
| Invarianza | `class Bolsa<T>` (por defecto) | Produce y consume: `Bolsa<Manzana>` y `Bolsa<Fruta>` no se relacionan. |
| `@UnsafeVariance` | `contains(element: @UnsafeVariance E)` | Permite usar un tipo `out` como entrada cuando es seguro. |

## Relaciones

- Ejercicios del tema: [[09.1 - Ejercicios 9 Genéricos]]
- [[02 - Jerarquia de tipos]] — subtipos, `Any`, `Any?` y `Nothing`, base de la varianza.
- [[05 - Operaciones con tipos nullables]] — `?:` y `!!`, que aparecen con `T?` y `T & Any`.
- [[07 - POO II]] — interfaces y _object expressions_ usadas en los ejemplos.
- [[08 - POO III]] — _extension functions_ genéricas como `fun <T> T.orThrow()`.
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar qué es el polimorfismo paramétrico y por qué se resuelve en compilación.
- [ ] Declarar y llamar a una función genérica, con y sin argumento de tipo explícito.
- [ ] Crear una clase genérica y dejar que el compilador infiera `T`.
- [ ] Distinguir `Box<String?>`, `T?` y `T & Any`.
- [ ] Explicar qué es el _type erasure_ y qué impide hacer con `T`.
- [ ] Restringir un parámetro de tipo con `:` y con `where`.
- [ ] Saber qué se puede leer y escribir en una `List<*>`.
- [ ] Decidir si un parámetro de tipo debe ser `out`, `in` o invariante.
- [ ] Explicar por qué `List<out E>` es covariante y `MutableList<E>` invariante.
