---
asignatura: PMDM
tema: 8
tipo: tema
estado: completo
fecha: 2026-10-25
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/kotlin-delegacion
---

# 08 · Programación Orientada a Objetos III

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 8 · Kotlin  
> Ejercicios: [[08.1 - Ejercicios 8 POO III]] · Tema anterior: [[07 - POO II]]

> [!info] Material de referencia
> [POO en Kotlin III](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b08%20-%20POO%20en%20Kotlin%20III/)

## Índice del tema

- [[#1. Top-level functions]]
- [[#2. Top-level properties]]
- [[#3. Constantes conocidas en tiempo de compilación]]
- [[#4. lateinit]]
- [[#5. Extension functions]]
- [[#6. Extension properties]]
- [[#7. Sobrecarga de operadores]]
- [[#8. Delegación de implementación de interfaces]]
- [[#9. Property delegation]]
- [[#10. Delegación básica a otra propiedad del mismo objeto]]
- [[#11. Inicialización perezosa con lazy]]
- [[#12. lazy vs. lateinit]]
- [[#13. Otros delegados predefinidos]]
	- [[#13.1 Delegates.notNull()]]
	- [[#13.2 Delegates.observable()]]
	- [[#13.3 Delegates.vetoable()]]

---

## 1. Top-level functions

En Kotlin no es necesario crear las típicas clases de utilidad que sólo contienen métodos estáticos, ya que **podemos definir una función fuera de cualquier clase**. Estas funciones son conocidas como _top-level functions_.

El ejemplo más característico de _top-level function_ es el método `main()` en Kotlin, que, a diferencia de en Java, no es necesario incluir dentro de una clase `Main`. Sin embargo, en aplicaciones Android el desarrollador no definirá esta función `main()`, que sólo será usada internamente por parte del _framework_.

> [!tip] Sugerencia
> En Kotlin podemos definir el método `main` con dos firmas distintas: `fun main(args: Array<String>)`, o de una manera más simple `fun main()`.

Por ejemplo, supongamos que dentro de un paquete llamado `utils` creamos un fichero kotlin `PrintUtils.kt` y dentro de él definimos la siguiente función:

**Top-level function**

```kotlin
// Función definida fuera de cualquier clase (top-level)
fun greet() {
    print("Hello")
}

fun main() {
    greet()
}
```

Cuando se compile el fichero correspondiente, se creará una clase, llamada por defecto `PrintUtilsKt`, proveniente del nombre del fichero y el sufijo `Kt`, que contendrá un método estático correspondiente a la función, dado que la máquina virtual de Java JVM sólo puede ejecutar código que esté contenido en clases. De hecho podríamos llamar a método estático a través del nombre de la clase, como en `PrintUtilsKt.greet()`.

Si queremos que el nombre de la clase generada sea diferente, usaremos la anotación `@file:JvmName("NewName")` como primera línea del fichero para indicar el nombre deseado.

> [!note] Comparación con Java
> En Java, una función "suelta" no existe: haríamos una clase de utilidad con métodos `static` (como `Math.max()`). En Kotlin escribimos la función directamente en el fichero y el compilador genera por nosotros esa clase `PrintUtilsKt` con el método estático. Es decir: lo que en Java escribimos a mano, Kotlin lo genera solo.

Si necesitamos usar una _top-level function_ desde un paquete diferente a en el que está definido, será necesario que la importemos con una instrucción `import`.

[Explicación en video](https://www.youtube.com/embed/MF3dXgRwke8)

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.1 · Top-level functions y visibilidad private|Ejercicio 8.1 · Top-level functions y visibilidad private]]

## 2. Top-level properties

De forma similar a como sucede con las _top-level functions_, en Kotlin **podemos declarar una propiedad fuera de cualquier clase**. Estas propiedades son conocidas como **_top-level properties_** o propiedades de primer nivel. **Las _top-level properties_ deben ser forzosamente inicializadas al declararlas**, independiente de que el tipo pueda contener `null` o no, o de si se trata de una propiedad `val` o `var`.

Aunque no suele ser muy habitual, almacenar datos de manera individual fuera de cualquier clase puede ser útil en algunos casos. Por ejemplo, supongamos que queremos contabilizar el número de veces que se realiza una determinada operación:

**Top-level property**

```kotlin
// Fuera de cualquier clase
var opCount = 0

fun performOperation() {
    // Podemos acceder a la propiedad desde cualquier función
    opCount++
}

fun reportOperationCount() {
    // Podemos acceder a la propiedad desde cualquier función
    println("Operation performed $opCount times")
}

fun main() {
    performOperation()
    reportOperationCount()
}
```

Si necesitamos usar una _top-level property_ desde un paquete diferente a en el que está definido, será necesario que la importemos con una instrucción `import`.

[Explicación en video](https://www.youtube.com/embed/bqT4HF5bxMQ)

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.2 · Top-level property como contador de sesiones|Ejercicio 8.2 · Top-level property como contador de sesiones]]

## 3. Constantes conocidas en tiempo de compilación

En la mayoría de las ocasiones, las variables candidatas a ser definidas como _top-level properties_ corresponderán a lo que se conoce como **constantes conocidas en tiempo de compilación**, que son aquellas cuyo valor se conoce incluso antes de ejecutar el programa. Por ejemplo, el valor del número PI, el nombre que le vamos a asignar a la base de datos, etc.

Además de como _top-level properties_, estas constantes pueden definirse como propiedades del _companion object_ de una determinada clase, de manera que el nombre de dicha clase sirva de espacio de nombres (_namespace_) para la constante.

Los identificadores de este tipo de constantes se definen normalmente en mayúsculas con un guión bajo entre las palabras que lo conforma. Este estilo de escritura de identificadores recibe el nombre de **UPPER_SNAKE_CASE** (estilo de nomenclatura de serpiente en mayúsculas).

Cuando una propiedad de un _companion object_ o una _top-level property_ representa un valor constante conocido en tiempo de compilación que corresponda a un valor de tipo primitivo o de tipo `String` podemos agregar el modificador `const` antes de la definición de la propiedad.

Al usar el modificador `const`, se producirá una optimización consistente en que **siempre que sea posible el compilador** hará un uso _inline_ de ella, es decir que **reemplazará las referencias que se hagan a la constante por el valor correspondiente**.

Dado que dicha optimización se lleva a cabo en tiempo de ejecución, solo puede llevarse a cabo con valores que representen literales de tipos primitivos. De hecho, para poder usar `const`, la propiedad debe cumplir con una serie de requisitos:

- Debe estar definida fuera de cualquier clase o como propiedad de un `object`, por ejemplo un _companion object_.
- Debe estar inicializada a un valor de tipo primitivo o `String`.
- No puede tener definido un _getter_ personalizado.

> [!note] Comparación con Java
> `const val MAX_SALARY = 2000` equivale a `public static final int MAX_SALARY = 2000;` en Java: una constante cuyo valor el compilador copia directamente donde se usa.

Veamos un ejemplo donde definimos una dos constantes conocidas en tiempo de compilación, una como _top-level property_ y otra como propiedad de un _companion object_:

**Modificador const**

```kotlin
class Boss {

    companion object {
        const val ALIAS = "boss"
    }

}
const val MAX_SALARY = 2000;

fun main() {
    println(MAX_SALARY)
    println(Boss.ALIAS)
}
```

> [!tip] Sugerencia
> Para definir una constante conocida en tiempo de compilación usa `const` siempre que se trate de un tipo primitivo o de `String`. Si es de otro tipo, defínela como si se trata de una constante conocida en tiempo de ejecución.

[Explicación en video](https://www.youtube.com/embed/4AYIsPX4Wyw)

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.3 · Constantes const en un companion object|Ejercicio 8.3 · Constantes const en un companion object]]

## 4. lateinit

Como ya estudiamos, las propiedades miembros de una clase deben ser inicializadas durante la instanciación, ya sea en el constructor primario, en la propia declaración de la propiedad, en un bloque de inicialización `init` o en un constructor secundario.

Sin embargo, en algunas ocasiones esto no es posible o no es conveniente, como por ejemplo cuando usamos inyección de dependencias, cuando configuramos pruebas unitarias o cuando no gestionamos nosotros el constructor de la clase, como en el caso de las actividades y fragmentos de Android.

Una posible solución consistiría en declarar la propiedad usando un tipo _nullable_ e inicializarla al valor `null`, de manera que cuando tengamos disponible el valor al que realmente queríamos inicializar la propiedad simplemente se le asigne. Por ejemplo:

**Tipo nullable con nulo inicial y reinicialización**

```kotlin
class MyTest {

    // Inicializamos la variable a null.
    var subject: TestSubject? = null

    @SetUp
    fun setup() {
        // Reinicializamos la variable.
        subject = TestSubject()
    }

    @Test
    fun test() {
        subject.method()
    }
}
```

El inconveniente de esta solución es que hemos tenido que cambiar el tipo de la propiedad hacia uno _nullable_, ya que hemos usado `null` como valor inicial. Este cambio de tipo afectará a todo el código que haga uso de dicha propiedad, obligándonos a usar el operador de llamada segura `?.` o el operador `!!`, incluso aunque sepamos que su valor por es `null` porque le hayamos dado el valor deseado antes de usarlo.

Para solucionar este inconveniente, Kotlin proporciona **la palabra reservada `lateinit`**, que permite **informar al compilador de que la propiedad que se está declarando en ese momento será inicializada más adelante, sin tener por ello que modificar su tipo hacia uno _nullable_**. Por ejemplo:

**Propiedad lateinit con inicialización tardía**

```kotlin
class MyTest {

    // Se inicializará más adelante.
    lateinit var subject: TestSubject

    @SetUp
    fun setup() {
        subject = TestSubject()
    }

    @Test
    fun test() {
        subject.method()
    }
}
```

Este modificador puede ser usado solamente con propiedades que cumplan con una serie de requisitos:

- Deben ser `var`, ya que su valor cambiará al inicializarla posteriormente.
- No pueden tener _getter_ o _setter_ personalizado.
- No pueden estar declaradas en el constructor primario de una clase.
- El tipo de la variables debe ser no _nullable_ y no corresponder a un tipo primitivo.

> [!warning] Aviso
> Al usar `lateinit` estamos haciendo la promesa al compilador de que más adelante vamos a inicializar la variable y que lo haremos antes de intentar acceder a ella para obtener su valor. Si no cumplimos dicha promesa, en tiempo de ejecución se lanzará la excepción específica `UninitializedPropertyAccessException`.

Podemos usar la palabra reservada `lateinit` no solo en propiedades miembro de una clase, sino también en _top-level properties_, y en variables locales de funciones.

[Explicación en video](https://www.youtube.com/embed/7a7kb-8f1YI)

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.4 · Propiedad lateinit y UninitializedPropertyAccessException|Ejercicio 8.4 · Propiedad lateinit y UninitializedPropertyAccessException]]

## 5. Extension functions

Una de las novedades más interesantes de Kotlin es la introducción de las conocidas como _extension functions_ (funciones de extensión).

> [!definition] Extension function
> Una _extension function_ es una **función que puede ser llamada como si fuera un método de una determinada clase, aunque en realidad está definida fuera de ella**.

Su definición es similar a la de cualquier función, pero escribiendo el nombre de la clase o interface que queremos extender, seguido de un punto `.` y del nombre de la función. Dicha clase corresponderá a lo que se conoce como tipo del receptor (_receiver_).

> [!definition] Receiver
> El receptor (_receiver_) de una _extension function_ corresponde al **objeto sobre el que se está ejecutando la función**, es decir, el que se indica antes del operador `.` en la llamada.

**Para representar al receptor dentro del código de la función se usa la palabra reservada `this`**, sobre el que podremos realizar las operaciones necesarias. Dentro de la _extension function_ el receptor se conoce como _extension receiver_.

Veamos un ejemplo de definición de una _extension function_:

**Extension function**

```kotlin
// Fuera de cualquier clase en el archivo Main.kt
// Extension function donde el receptor es un objeto de la clase String.
fun String.lastChar(): Char = this.get(this.length - 1)

fun main() {
    val name: String = "Baldomero"
    println("El último carácter del nombre es: ${name.lastChar()}")
}
```

Al igual que en el caso de los métodos tradicionales de una clase, **podemos ahorrarnos la referencia explícita a `this` para acceder a métodos o propiedades del receptor desde dentro del código de la _extension function_**. Así, la definición de la _extension function_ anterior podría simplificarse de la siguiente manera:

**Referencia implícita a this en extension function**

```kotlin
// Fuera de cualquier clase en el archivo Main.kt
// Extension function donde el receptor es un objeto de la clase String.
fun String.lastChar(): Char = get(length - 1)

fun main() {
    val name: String = "Baldomero"
    println("El último carácter del nombre es: ${name.lastChar()}")
}
```

Podemos definir _extension functions_ sobre tipos que no controlamos, como por ejemplo la clase `String`. De esta manera podremos extender API externas con nuestras propias funciones. Este mecanismo funcionará independiente de que la clase correspondiente al tipo del receptor haya sido escrita en Java, en Kotlin o en cualquier otro lenguaje de la JVM, mientras sea compilada hacia una clase Java.

La gran ventaja de las _extension functions_ es que **podemos usarlas como si se trataran de métodos de la clase correspondiente**, es decir, sobre cualquier objeto de dicha clase, y además **el IDE es capaz de sugerirnos su empleo cuando escribimos el operador `.` tras el identificador de objeto**. El objeto sobre el que se ejecuta es conocido como _dispatch receiver_.

Veamos un ejemplo de uso de la _extension function_ definida anteriormente:

**Llamada a una extension function**

```kotlin
val message: String = "Baldomero"
// Como el objeto message es de la clase String, la extension fuction
// lastChar() está disponible para dicho objeto, aunque en realidad esté
// definida fuera de la clase String.
val last: Char = message.lastChar()
```

Como vemos, en el código de la _extension function_ podemos acceder directamente a los miembros (métodos y propiedades) públicos de la clase que se está "mejorando", como si fueran métodos reales de la clase.

Desde el punto de vista del código cliente, la llamada a un método real de un objeto de la clase y la llamada a una _extension function_ sobre un objeto de la clase es similar. La principal diferencia es que **las _extension functions_ deben ser importadas de forma independiente**. Por este motivo, pueden estar localizadas en paquetes diferentes.

Cuando definimos una _extension function_, **en realidad no estamos añadiendo nada a la clase correspondiente al tipo del receptor**. Tan solo corresponde a lo que se conoce como _syntactic sugar_ (azúcar sintáctico), es decir, una sintaxis más atractiva para una funcionalidad ya existente.

Cuando se compila la definición de una _extension funcion_ a _bytecode_ **se convierte en un método estático fuera de la clase correspondiente al tipo del receptor, con un primer parámetro correspondiente al _extension receiver_ (receptor), y en el que todas las referencias, explícitas o implícitas a `this` se convierten en referencias a dicho parámetro**. De igual forma, **la llamada** a una _extension function_ se compila de manera que **se convierte en una llamada a dicho método estático, pasando como primer argumento el _dispatch receiver_ (el receptor)**. Así, el ejemplo anterior es totalmente equivalente a:

**Equivalencia con metodo estático**

```kotlin
// Definición como método "estático"
fun lastChar(dispatchReceiver: String): Char = dispatchReceiver.get(dispatchReceiver.length - 1)

fun main() {
    val name: String = "Baldomero"
    // La diferencia está en la forma de llamar al método
    println("El último carácter del nombre es: ${lastChar(name)}")
}
```

Como vemos, repecto a la llamada, la diferencia entre una _extension function_ y una función normal es que una _extension function_ se llama sobre un objeto, mientras que en una función normal el objeto se pasa como argumento.

El hecho de que una _extension function_ no sea más que una sintaxis alternativa a una función con el receptor como primer parámetro, y que no pertenezca realmente a la clase correspondiente al tipo del receptor, tiene una serie de consecuencias.

En primer lugar, las _extension functions_ **no pueden acceder a los miembros `private` o `protected` de la clase, ya que no pertenecen a ella**, de manera que no se rompe la encapsulación que le se haya establecido a la clase original.

Por otra parte, al corresponder en realidad a funciones estáticas fuera de la clase del tipo del receptor, **las _extension functions_ son resueltas estáticamente en tiempo de compilación**. Es decir, La función que debe ser llamada se determina en tiempo de compilación, atendiendo al tipo declarado de la expresión en la que está invocando la función (polimorfismo estático), y NO atendiendo al resultado de evaluar la expresión en tiempo de ejecución (polimorfismo dinámico).

**Resolución de llamadas a extension function en tiempo de compilación**

```kotlin
open class C

class D: C()

fun C.foo() = "c"

fun D.foo() = "d"

fun printFoo(c: C) {
    println(c.foo())
}

fun main() {
    // Muestra c a pesar de que el objeto real es de la clase D
    // porque el parámetro de printFoo es de tipo C.
    printFoo(D()) 
}
```

En el ejemplo anterior se muestra por pantalla `c`, porque en tiempo de compilación el tipo del parámetro `c` de la función `printFoo()` es la clase `C`, y por tanto se ejecuta el método `foo()` de la clase `C`, a pesar de que en tiempo de ejecución en realidad se reciba un objeto de la clase `D`.

Si se crea una _extension function_ de una clase con el mismo nombre y los mismos parámetros (misma firma) que un método de dicha clase, cuando lo llamemos siempre se ejecutará el método, es decir, **el método real prevalece frente a la _extension function_ en caso de conflicto** por tener la misma firma.

Como sabemos, los métodos normales de un variable _nullable_ no pueden ser llamados directamente con el operador punto `.`, sino que debemos usar el operador de llamada segura `?.`. Sin embargo, en el caso de las _extension functions_ no tenemos dicha limitación, porque digamos que las _extension functions_ se definen sobre tipos, y no sobre clases.

Así, **podemos definir una _extension function_ que extienda un tipo _nullable_, y llamarla como si de un método de dicha clase se tratase usando el operador `.`**. Por ejemplo, para el tipo `String?` la librería estándar define la _extension function_ `orEmpty()` que retorna el valor si no es `null` o una cadena vacía en caso contrario. Al ser una _extension function_ podremos llamarla directamente con el operador punto `.`, como por ejemplo en `myNullableString.orEmpty()`.

También **podemos crear _extension functions_ para que se apliquen sobre el _companion object_ de una clase**, incluso si dicha clase no la hemos creado nosotros. **Al definir la _extension function_ deberemos usar el nombre real del _companion object_** (el nombre por defecto es `Companion`), y no simplemente el nombre de la clase. Sin embargo, **en la llamada podemos especificar simplemente el nombre de la clase**:

**Extension function de un companion object**

```kotlin
fun String.Companion.greet(name: String) {
    println("Hello $name")
}

fun main() {
    String.greet("Baldomero")
}
```

Evidentemente, **para poder definir una _extension function_ sobre un _companion object_, éste ha debido ser definido en la clase, incluso no se haya definido cuerpo para él**.

El uso más habitual de las _extension functions_ es para agregar métodos a APIs no desarrolladas por nosotros. Sin embargo, en algunas ocasiones, **en clases o interfaces creadas por nosotros, es preferible definir _extension functions_ frente a definir dicho código como métodos miembros, con el objetivo de no "ensuciar" la clase o interfaz con métodos adicionales que escapen del objetivo principal de ésta**, de manera que la clase o interfaz quede más pequeña, legible y concisa. Esta **decisión de diseño** ha sido empleada frecuentemente en la librería estándar de Kotlin, en la que existen numerosas _extension functions_, ya que **en términos de rendimiento en ejecución no hay una diferencia significativa**.

El ejemplo más característico de ésto es cuando queremos crear una función de conversión entre dos clases relacionadas. Supongamos que tenemos una clase `Product` y una clase `ProductJson` (de comunicación con una API externa), y queremos crear una función `toProduct()` para convertir desde `ProductJson` a `Product`. Debemos decidir si definirla como método miembro de la clase `ProductJson` o como _extension function_ de `ProductJson`. Veamos la comparación:

**Mejora de legibilidad con extension functions**

```kotlin
data class Product(val id: String, val title: String)

// Como método
data class ProductJsonWithMethod(
    val id: String,
    val title: String,
    val img: String,
) {
    fun toProduct() = Product(
        id = this.id,
        title = this.title,
    )
}

// Como extension function
data class ProductJsonWithoutMethod(
    val id: String,
    val title: String,
    val img: String,
)

fun ProductJsonWithoutMethod.toProduct() = Product(
    id = this.id,
    title = this.title,
)

fun main() {
    val productJson1 = ProductJsonWithMethod("1", "Producto1", "URL1")
    val product1 = productJson1.toProduct()
    println(product1)
    val productJson2 = ProductJsonWithoutMethod("2", "Producto2", "URL2")
    val product2 = productJson2.toProduct()
    println(product2)
}
```

En este caso parece más elegante hacerlo como _extension function_ ya que el objetivo de la clase `ProductJson` es realmente describir las propiedades recibidas desde una llamada a la API, por lo que su código quedará mucho más limpio si dicha funcionalidad de conversión se define fuera de la misma.

> [!tip] Sugerencia
> No debemos volvernos locos y definir _extension functions_ para todo. Debemos tener en cuenta que las _extension functions_ que definamos no pertenecerán a la librería estándar de Kotlin, por lo que **puede que el resto de desarrolladores con los que trabajemos no sepan que las hemos creado**. Su abuso puede producir una polución en el espacio de nombres, que dificulte la determinación del origen del método, y por tanto la comprensión del código y la navegación a través de él En todo caso, las _extension functions_ deberían estar **bien documentadas** para poder ser usadas por el equipo de desarrollo.

Sin embargo, es evidente de las _extension functions_ son muy útiles para "mejorar" o ampliar clases de un determinado _framework_ o librería, a cuyas definiciones no tenemos acceso.

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.5 · Extension function reverseWords|Ejercicio 8.5 · Extension function reverseWords]]

[Explicación en video](https://www.youtube.com/embed/0tz7bzHHqXs)

## 6. Extension properties

Además de _extension functions_ podemos crear _extension properties_ (propiedades de extensión). Por ejemplo, la librería estándar define la siguiente _extension property_ para las listas:

**Extension property**

```kotlin
val <T> List<T>.lastPosition: Int
    get() = size - 1

fun main() {
    val students: List<String> = listOf("Baldomero", "Germán Ginés", "Godolfredo")
    // La diferencia está en la forma de llamar al método
    println("El índice del último elemento de la lista es: ${students.lastPosition}")
}
```

Dado que la extensiones no son miembros reales de la clase, **no pueden contener un _backing field_** (campo de respaldo), por lo que en las _extension properties_ **no está permitido el uso de inicializadores, y los _getter_ y _setter_ personalizados no pueden hacer referencia al _backing field_**.

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.6 · Extension property vowelCount|Ejercicio 8.6 · Extension property vowelCount]]

## 7. Sobrecarga de operadores

Como sabemos, Kotlin define un conjunto predefinido de operadores, cada uno de ellos con su representación simbólica, como por ejemplo `+`, `*`, etc., y una determinada precedencia entre ellos.

Sin embargo, y a diferencia de en otros lenguajes de programación, en Kotlin la ejecución de la mayoría de dichos operadores (no todos) es traducida internamente a llamadas a métodos o expresiones complejas predeterminadas. Por ejemplo, `a + b` se traduce directamente a la llamada `a.plus(b)`, `a[i]` se traduce a `a.get(i)`, etc. Veamos cuál es la traducción realizada para cada operador:

|Expresión|Se traduce a|
|---|---|
|`a + b`|`a.plus(b)`|
|`a - b`|`a.minus(b)`|
|`a * b`|`a.times(b)`|
|`a / b`|`a.div(b)`|
|`a % b`|`a.rem(b)`|
|`a..b`|`a.rangeTo(b)`|
|`a..<b`|`a.rangeUntil(b)`|
|`a in b`|`b.contains(a)`|
|`a !in b`|`!b.contains(a)`|
|`a[i]`|`a.get(i)`|
|`a[i] = b`|`a.set(i, b)`|
|`a()`|`a.invoke()`|
|`a += b`|`a.plusAssign(b)`|
|`a -= b`|`a.minusAssign(b)`|
|`a *= b`|`a.timesAssign(b)`|
|`a /= b`|`a.divAssign(b)`|
|`a %= b`|`a.remAssign(b)`|
|`a == b`|`a?.equals(b) ?: (b === null)`|
|`a != b`|`!(a?.equals(b) ?: (b === null))`|
|`a > b`|`a.compareTo(b) > 0`|
|`a < b`|`a.compareTo(b) < 0`|
|`a >= b`|`a.compareTo(b) >= 0`|
|`a <= b`|`a.compareTo(b) <= 0`|
|`+a`|`a.unaryPlus()`|
|`-a`|`a.unaryMinus()`|
|`!a`|`a.not()`|
|`++a`|`a.inc(); a`|
|`a++`|`val tmp = a; a.inc(); tmp`|
|`--a`|`a.dec(); a`|
|`a--`|`val tmp = a; a.dec(); tmp`|

> [!definition] Igualdad referencial
> El operador `===` es lo que se conoce como igualdad referencial, y hace referencia a que las variables situadas a izquierda y a derecha de él apuntan al mismo objeto en memoria.

La **sobrecarga de operadores** es un concepto en programación que permite a los desarrolladores **definir comportamientos personalizados para operadores existentes** en un lenguaje de programación. En lugar de limitarse a los comportamientos predeterminados de los operadores proporcionados por el lenguaje, la sobrecarga de operadores **permite que los objetos y tipos definidos por el desarrollador se comporten de manera similar a los tipos primitivos en el uso de operadores** aritméticos, de comparación, y otros operadores.

En Kotlin, para conseguir la sobrecarga de operadores, simplemente debemos **definir en nuestras propias clases los métodos indicados en la tabla** anterior, **marcándolos con la palabra reservada `operator`**, gracias a lo que podremos usar el símbolo correspondiente a dicho operador con objetos de esas clases.

Por ejemplo, si hemos creado una clase `Point` para representar un punto, podemos crearle un método `operator fun plus(point: Point): Point`, de manera que podamos usar el operador `+` para crear un nuevo punto cuyas coordendas correspondan a la suma de las coordenadas de los dos puntos que se "suman":

**Sobrecarga del operador `+` en clase `Point`**

```kotlin
data class Point(val x: Double, val y: Double) { 
    operator fun plus(point: Point) = Point(x + point.x, y + point.y)
} 

fun main() {
    val point1 = Point(2.0, 3.0)
    val point2 = Point(5.0, 8.0)
    val point3 = point1 + point2
    println(point3)
}
```

Cuando usamos un operador binario sobrecargado, el método en el que se traduce **es siempre ejecutado sobre el operando izquierdo que precede al operador, y el operando derecho posterior a él es el que se pasa como argumento de llamada al método**. Así, cuando usamos el operador `+` con una operando izquierdo de la clase `Point` Kotlin llama al método `plus()` sobre la instancia del operando izquierdo, pasándole como argumento el operando derecho, que en este caso es otro punto.

Este aspecto hace que **en casos en los que los operandos del operador binario sean de distinto tipo, el orden en el que se especifiquen sea especialmente relevante**, ya que siempre se tratará de ejecutar la sobrecarga de operador definido para el tipo del operando de la izquierda. Por ejemplo, podemos hacer `"Baldomero" + 3`, puesto que la clase `String` tiene sobrecargado el operador `plus()` para recibir como argumento un entero y producir la concatención `Baldomero3`. Sin embargo, no podemos hacer `3 + "Manolo"`, porque la clase `Int` no tiene sobrecargado el operador `plus()` para recibir como argumento una cadena de caracteres.

**Podemos definir varios métodos que actúen con el mismo operador y que reciban distintos tipos de parámetros**. Es decir, que podemos sobrecargar varias veces el mismo operador, siempre y cuando la firma del método no sea la misma. Por ejemplo, vamos a ampliar el ejemplo anterior añadiendo un segundo método operador `plus()` que reciba como argumento un `Double` en vez de un `Point`. De esta manera podremos usar el operador `+` para "sumar" un `Double` a un `Point`:

**Sobrecarga múltiple del operador `+` en clase `Point`**

```kotlin
data class Point(val x: Double, val y: Double) { 
    operator fun plus(point: Point) = Point(x + point.x, y + point.y)

    operator fun plus(vector: Double) = Point(x + vector, y + vector) 
} 

fun main() {
    val point1 = Point(2.9, 5.0)
    val point2: Point = point1 + 3.1
    println(point2)
}
```

Debemos tener en cuenta que **los métodos a los que se traducen los operadores de asignación aritmética, deben modificar el estado del objeto existente**.

Por último, debemos destacar que **podemos usar un bucle `for` con el operador `in` sobre cualquier objeto que tenga definido el método `operator fun iterator(): Iterator<T>`**, como es el caso de `Range` o de `List`.

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.7 · Sobrecarga del operador + en ComplexNumber|Ejercicio 8.7 · Sobrecarga del operador + en ComplexNumber]]

## 8. Delegación de implementación de interfaces

La delegación de implementación de interfaz es un patrón de diseño en el que **una clase delega la implementación de los métodos de una interfaz a otro objeto**. Esto **permite que una clase reutilice** la funcionalidad de **la interfaz sin** necesidad de **implementar directamente** todos los métodos en sí misma, **sino a través de la implementación de otro objeto delegado**.

Veamos un ejemplo, donde se crea una interfaz que representa a una criatura, y una clase con la implementación por defecto de una criatura `Creature`, esto es, una criatura genérica `GenericCreature`. Finalmente queremos crear una clase que representa un duende `Goblin`, cuyo comportamiento como criatura corresponde al de una criatura genérica:

**Ejemplo del patrón delegación**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

class Goblin : Creature {
    private val delegate = GenericCreature(2, 1)
    override val attackPower: Int = delegate.attackPower 
    override val defensePower: Int = delegate.defensePower
    override fun attack() { delegate.attack() }
    // ...
}

fun main() {
    val goblin = Goblin()
    println(goblin.defensePower) // 1 
    goblin.attack() // Attacking with 2
}
```

Como vemos en el ejemplo anterior, en la clase `Goblin` se crea un objeto delegado (que también podríamos haber pasado al constructor de la clase), y se delega en él toda la implementación de la interfaz `Creature`, tanto en lo relativo a sus propiedades como a su método. Es evidente, que las líneas de código mediante las que se hace la delegación de la implementación de la interfaz al objeto delegado corresponden a código repetitivo y tedioso (_boilerplate code_).

Para evitarnos generar ese _boilerplate code_, **en Kotlin, la delegación de implementación de interfaz se realiza utilizando la palabra clave `by` en la declaración de la clase, justo después del identificador de la interfaz que se quiere implementar, seguido del objeto al que se delega** la implementación de la interfaz (que evidentemente debe implementarla).

**Delegación de implementación de interfaces con `by`**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

class Goblin : Creature by GenericCreature(2, 1) {
    // ...
}

fun main() {
    val goblin = Goblin()
    println(goblin.defensePower) // 1 
    goblin.attack() // Attacking with 2
}
```

**Internamente**, al compilar **se generarán** en la clase todos **los métodos de implementación** de la interfaz, **que simplemente llamarán al método correspondiente del objeto delegado**.

El objeto delegado puede proporcionarse de diferentes formas:

1. **Construir el objeto delegado sobre la marcha directamente en el `by` sin usar parámetros del constructor de la clase que delega** (ver ejemplo anterior).

2. **Construir el objeto delegado sobre la marcha directamente en el `by` usando parámetros del constructor de la clase que delega**:

**Construir el objeto delegado en el by con parámetros del constructor**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

// El delegado se proporciona en el by y usa parámetros del constructor
class Goblin( 
    att: Int,
    def: Int
) : Creature by GenericCreature(att, def) {
    // ...
}

fun main() {
    val goblin = Goblin(2, 1)
    println(goblin.defensePower) // 1 
    goblin.attack() // Attacking with 2
}
```

3. **El objeto delegado se recibe ya construído como parámetro del constructor primario y se usa en el `by`**:

**Recibir el delegado ya construido como parámetro del constructor**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

// El delegado se recibe como argumento del constructor
class Goblin(
    creature: Creature
) : Creature by creature {
    // ...
}

fun main() {
    val goblin = Goblin(GenericCreature(2, 1))
    println(goblin.defensePower) // 1 
    goblin.attack() // Attacking with 2
}
```

4. **El objeto delegado se puede recibir ya construído como parámetro del constructor primario, pero se proporciona uno por defecto, y se usa en el `by`**:

**Poder recibir el delegado ya construido como parámetro del constructor pero proporcionar uno por defecto**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

// El delegado se recibe como argumento del constructor, pero se 
// proporciona uno por defecto
class Goblin(
    val creature: Creature = GenericCreature(2, 1)
) : Creature by creature {
    // ...
}

fun main() {
    val goblin = Goblin()
    println(goblin.defensePower) // 1 
    goblin.attack() // Attacking with 2
}
```

5. **Se usa en el `by` como objeto delegado un objeto externo**:

**Se usa en el `by` como objeto delegado un objeto externo**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

// Se establece como delegado un objeto externo ya construído
val creature = GenericCreature(2, 1)
class Goblin : Creature by creature {
    // ...
}

fun main() {
    val goblin = Goblin()
    println(goblin.defensePower) // 1 
    goblin.attack() // Attacking with 2
}
```

También **podemos sobrescribir manualmente en la clase los métodos de la interfaz**, lo que provocará que en tiempo de compilación NO se genere el método por defecto para la delegación de dicho método. **Si dentro del método sobrescrito debemos llamar al objeto delegado, deberemos definirlo como una propiedad de la clase**.

**Delegación de implementación de interfaces con `by`**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower") 
    }
}

// La ejecución del método attack no será delegada directamente al objeto delegado
class Goblin(
    private val creature: Creature = GenericCreature(2, 1)
) : Creature by creature { 
    override fun attack() {
        println("It will be special Goblin attack!")
        creature.attack()
    }
}

fun main() {
    val goblin = Goblin()
    println(goblin.defensePower)
    goblin.attack() 
}
```

El enfoque de la delegación **promueve la composición sobre la herencia**, ya que permite que una clase adquiera el comportamiento definido por una interfaz a través de la composición de objetos, en lugar de extender directamente una clase base. Esto mejora la modularidad y flexibilidad del código, ya que las clases pueden cambiar fácilmente la implementación de la interfaz delegada sin afectar su propia implementación.

Así, el ejemplo anterior usando herencia quedaría de la siguiente manera:

**Ejemplo anterior usando herencia**

```kotlin
interface Creature {
    val attackPower: Int 
    val defensePower: Int 
    fun attack()
}

open class GenericCreature(
    override val attackPower: Int, 
    override val defensePower: Int,
) : Creature {
    override fun attack() {
        println("Attacking with $attackPower")
    }
}

class Goblin : GenericCreature(2, 1) { 
    // ...
}

fun main() {
    val goblin = Goblin()
    println(goblin.defensePower)
    goblin.attack() 
}
```

Aunque usar herencia parece más sencillo, su empleo tiene ciertas consecuencias y limitaciones que hacen que sea más adecuado usar la delegación, para favorecer el principio de preferir la composición frente a la herencia. Los principales motivos son:

- Solo podemos heredar de una única clase, pero **podemos implementar varias interfaces por delegación**.
- En muchas ocasiones la herencia supone una relación demasiado fuerte entre las clases. Por ejemplo, puede que no queramos que un duende `Goblin` sea una criatura genérica `GenericCreature`, porque no podemos garantizar que un duende `Goblin` vaya a comportarse siempre como una criatura genérica `GenericCreature`.

Es posible definir una clase que implemente dos interfaces, de manera que la implementación de cada una de ellas se delega a un objeto delegado diferente. En dicha clases se están agregando los tipos y el comportamiento de la dos clases correspondientes a los objetos delegados, por lo que podríamos decir que la clase que estamos definiendo representa lo que se conoce como un tipo de intersección de tipos (_intersection type_).

De hecho, si una clase implementa dos interfaces por delegación y ambas interfaces tienen el mismo método con la misma firma, deberemos forzosamente sobrescribir manualmente dicho método en la clase, para resolver el conflicto que se generaría, ya que al sobrescribirlo manualmente no se generarán los métodos de delegación por defecto. Por ejemplo:

**Clase que implementa varias interfaces por delegación**

```kotlin
interface Attack { 
    val attack: Int
    val defense: Int 
}

interface Defense { 
    val defense: Int
}

class Dagger : Attack {
    override val attack: Int = 1
    override val defense: Int = -1 
}

class LeatherArmour : Defense { 
    override val defense: Int = 2
}

class Goblin(
    private val attackDelegate: Attack = Dagger(),
    private val defenseDelegate: Defense = LeatherArmour(), 
) : Attack by attackDelegate, Defense by defenseDelegate {
    // We must override this property
    override val defense: Int = defenseDelegate.defense + attackDelegate.defense
}

fun main() {
    val goblin = Goblin()
    println("Defense: ${goblin.defense}")
    println("Attack: ${goblin.attack}") 
}
```

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.8 · Delegación de interfaces con by|Ejercicio 8.8 · Delegación de interfaces con by]]

## 9. Property delegation

Como ya sabemos, a la combinación del campo y de los métodos de acceso se le conoce tradicionalmente como propiedad (_property_). Kotlin incorpora directamente el concepto de propiedad, evitándonos la necesidad de definir un campo y sus métodos de acceso.

Para una determina propiedad no es obligatorio que ésta esté sustentada por un determinado _backing field_ (campo de respaldo) que almacene su valor, ya que puede estar simplemente definida por un método de acceso _get_, si se trata de una propiedad de sólo lectura, y adicionalmente un método de acceso _set_, si se trata de una propiedad de lectura y escritura.

Pues bien, Kotlin nos permite **delegar los métodos de acceso _get_ y _set_ de una propiedad a otro objeto _delegate_ (delegado), a lo que se conoce como _property delegation_ (delegación de propiedad)**.

De esta manera, **cuando se trate de acceder para lectura a la propiedad, internamente se llamará al método `getValue()` del objeto _delegate_, y si se trata de acceder para escritura a la propiedad, internamente se llamará al método `setValue()` del objeto _delegate_**.

Para realizar la delegación de propiedad se usa la sintaxis `val/var <property name>: <Type> by <expression>`, donde `expression` debe retornar un objeto _delegate_. Por ejemplo:

**Delegación de propiedad**

```kotlin
class Example {

    // Cuando se acceda a la propiedad p, en realidad se estarán llamando
    // a métodos del objeto Delegate.
    var p: String by MyDelegate()
}
```

Internamente, el código anterior se compilará a algo parecido a:

**Resultado de la compilación de la delegación de propiedad**

```kotlin
class Example {

    var delegate: Delegate()
    var p: String
        get() = delegate.getValue(this, ::example)
        set(value) {
            delegate.setValue(this, ::example, value)
        }
}
```

**Para que un objeto pueda actuar como _delegate_ de una propiedad definida con `val`, será necesario que el _delegate_ posea una función de operador `operator fun getValue(thisRef: R, property: KProperty<*>): T`. Para que pueda actuar como _delegate_ de una propiedad `var`, además de `getValue()`, deberá poseer la función de operador `operator fun setValue(thisRef: R, property: KProperty<*>, value: T)`**, donde:

- `T` es el tipo de la propiedad.
- `thisRef` corresponde al objeto propietario de la propiedad. Nos da información sobre dónde se está usando la función y quién puede usarla.
- `R` corresponde al tipo del objeto propietario de la propiedad.
- `property` corresponde a la propiedad que se quiere obtener. Se usa sobre todo para obtener su nombre y algunas veces información sobre sus anotaciones.
- `value` corresponde al valor que se quiere establecer para la propiedad.

Por ejemplo podríamos definir una clase delegada que imprime por pantalla el valor de la propiedad cada vez que se accede a él y cada vez que se cambia:

**Clase delegada**

```kotlin
import kotlin.reflect.KProperty

class LoggingProperty<T>(var value: T) { 

    operator fun getValue(
        thisRef: Any?, 
        prop: KProperty<*>
    ): T {
        println("${prop.name} getter returned $value")
        return value
    }

    operator fun setValue(
        thisRef: Any?, 
        prop: KProperty<*>,
        newValue: T 
    ) {
        val name = prop.name
        println("$name changed from $value to $newValue") 
        value = newValue
    }

}

fun main() {
    var attempts: Int by LoggingProperty(0)
    attempts = attempts + 1
    println("Attempts: $attempts")
}
```

Kotlin proporciona la interfaz `ReadOnlyProperty`, que define la función de operador `getValue()`, para simplificarnos la creación de objetos delegados para propiedades `val`. También tenemos disponible la interfaz `ReadWriteProperty`, que define tanto la función operador `getValue()` como la función operador `setValue()`, que podemos usar para crear clases delegadas para propiedades `var`. Por tanto, en el ejemplo anterior podríamos haber hecho que la clase `MyDelegate` implementase `ReadWriteProperty`.

Así, podríamos haber definido la clase delegada `LoggingProperty` de la siguiente manera:

**Clase delegada que implementa interfaz ReadWriteProperty**

```kotlin
import kotlin.reflect.KProperty
import kotlin.properties.ReadWriteProperty

class LoggingProperty<T>(
    var value: T
) : ReadWriteProperty<Any?, T> {
    override fun getValue( 
        thisRef: Any?,
        property: KProperty<*>
    ): T {
        println("${property.name} getter returned $value")
        return value 
    }

    override fun setValue(
        thisRef: Any?,
        property: KProperty<*>,
        value: T 
    ) {
        val name = property.name
        println("$name changed from ${this.value} to $value") 
        this.value = value
    }

}

fun main() {
    var attempts: Int by LoggingProperty(0)
    attempts = attempts + 1
    println("Attempts: $attempts")
}
```

Las funciones `getValue()` y `setValue()` del objeto delegado pueden proporcionarse no solo en forma de funciones miembro, sino también con _extension functions_, lo cual resulta bastante útil si queremos hacer que objetos de clases no creadas por nosotros y que no implementan inicialmente dicha funcionalidad puedan actuar como delegados. Por ejemplo:

**Creación de clase delegada mediante extension function**

```kotlin
public inline operator fun <T> Lazy<T>.getValue(
    thisRef: Any?, property: KProperty<*>
): T = value
```

Debemos tener en cuenta que no sólo podemos delegar propiedades miembros de una clase, sino también _top-level properties_, e incluso aquellas definidas dentro de una función o dentro de un bloque de código.

Otra opción interesante es que el objeto que indiquemos junto a `by` para delegar la propiedad no implemente los métodos `getValue()` y `setValue()` directamente, sino que actúe como proveedor de un objeto delegado. Para ello, deberá implementar la función operador `provideDelegate()` que debe retornar el objeto delegado que debe usarse (que deberá implementar `getValue()` y `setValue()`). Así, siguiendo el ejemplo anterior, podríamos usar un proveedor del objeto delegado de la siguiente forma:

**Proveedor de objeto delegado**

```kotlin
import kotlin.reflect.KProperty
import kotlin.properties.PropertyDelegateProvider

class LoggingPropertyProvider<T>( private val value: T) {

    operator fun provideDelegate( 
        thisRef: Any?,
        property: KProperty<*>
    ): LoggingProperty<T> = LoggingProperty(value)

}

class LoggingProperty<T>(var value: T) { 

    operator fun getValue(
        thisRef: Any?, 
        prop: KProperty<*>
    ): T {
        println("${prop.name} getter returned $value")
        return value
    }

    operator fun setValue(
        thisRef: Any?, 
        prop: KProperty<*>,
        newValue: T 
    ) {
        val name = prop.name
        println("$name changed from $value to $newValue") 
        value = newValue
    }

}

fun main() {
    var attempts: Int by LoggingProperty(0)
    attempts = attempts + 1
    println("Attempts: $attempts")
}
```

> [!warning] Ojo con el ejemplo
> En el `main` del ejemplo de los apuntes se sigue usando `by LoggingProperty(0)`, así que el proveedor no llega a usarse. Para que actúe el proveedor habría que escribir `var attempts: Int by LoggingPropertyProvider(0)`: Kotlin llama primero a `provideDelegate()` y la propiedad queda delegada en el `LoggingProperty` que este devuelve.

La ventaja de un proveedor de delegación, como en el caso anterior, es que dicho objeto, al no ser realmente un objeto delegado puede ser, por ejemplo, inmutable, y proporcionar un objeto delegado mutable.

Para crear un proveedor de delegación también podemos hacer que la clase implemente la interfaz `PropertyDelegateProvider`. Los dos parámetros de tipo de la interfaz representan el tipo del receptor, y el tipo de la propiedad que se delega. Por ejemplo:

**Proveedor de objeto delegado que implementa PropertyDelegateProvider**

```kotlin
import kotlin.reflect.KProperty
import kotlin.properties.PropertyDelegateProvider

class LoggingPropertyProvider<T>(
    private val value: T
) : PropertyDelegateProvider<Any?, LoggingProperty<T>> {

    override fun provideDelegate(
        thisRef: Any?,
        property: KProperty<*>
    ): LoggingProperty<T> = LoggingProperty(value)

}

class LoggingProperty<T>(var value: T) { 

    operator fun getValue(
        thisRef: Any?, 
        prop: KProperty<*>
    ): T {
        println("${prop.name} getter returned $value")
        return value
    }

    operator fun setValue(
        thisRef: Any?, 
        prop: KProperty<*>,
        newValue: T 
    ) {
        val name = prop.name
        println("$name changed from $value to $newValue") 
        value = newValue
    }

}

fun main() {
    var attempts: Int by LoggingProperty(0)
    attempts = attempts + 1
    println("Attempts: $attempts")
}
```

[Explicación en video](https://www.youtube.com/embed/vLrLCwrecQg)

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.9 · Delegado de propiedad UpperCaseDelegate|Ejercicio 8.9 · Delegado de propiedad UpperCaseDelegate]]

## 10. Delegación básica a otra propiedad del mismo objeto

La forma más básica de delegación usando `by` que nos ofrece Kotlin es delegar la implementación de una propiedad de una clase a otra propiedad de la propia clase, como en el siguiente ejemplo:

**Delegación de una propiedad en otra de la misma clase**

```kotlin
class Sample {
    private var _value: String = "Initial Value"
    var value: String by ::_value
}

fun main() {
    val sample = Sample()
    println(sample.value)
    sample.value = "Baldomero"
    println(sample.value)
}
```

Esto puede útil por ejemplo, cuando se incorpora una nueva propiedad como alias de otra existente.

## 11. Inicialización perezosa con lazy

La inicialización perezosa (_lazy initialization_) es un patrón de diseño que retrasa la creación o el cálculo de un objeto hasta el preciso instante en que se necesita por primera vez. Esto optimiza el rendimiento y el uso de recursos, especialmente cuando la inicialización es costosa y no siempre necesaria.

Kotlin integra este patrón de forma nativa a través de la delegación de propiedades con la función constructora `lazy()` que construye un objeto delegado que implementa dicho comportamiento y gestionará la inicialización de una propiedad. Esta función recibe como argumento una _lambda_, que será ejecutada cuando sea necesario inicializar la propiedad, de manera que el valor retornado por la _lambda_ será establecido como valor inicial de la propiedad.

Internamente, el objeto delegado posee una propiedad interna, que se inicializa con un valor especial UNINITIALIZED_VALUE, indicativo de que la propiedad que delega aún no ha sido inicializada. Cada vez que leemos al propiedad, se comprueba el valor de la propiedad interna:

- Si posee el valor especial UNINITIALIZED_VALUE, se ejecuta la _lambda_ proporcionada a la función constructora `lazy()`, y el valor que es retornado por dicha lambda se establece como valor de la propiedad interna y se devuelve como valor de la propiedad que delega.
- Si posee un valor distinto a UNINITIALIZED_VALUE, es porque la propiedad ya ha sido inicializada, y se retorna el valor de la propiedad interna como valor de la propiedad que delega. Por tanto, cualquier acceso futuro a la propiedad devolverá directamente el valor almacenado, sin volver a ejecutar la _lambda_.

Sólo podemos usar la función `lazy` con propiedades de sólo lectura definidas con `val`, ya que solo tenemos definida como _extension function_ `getValue ()`, pero NO `setValue()`, lo cual es lógico, ya que su propósito es inicializar un valor una única vez.

**Uso de lazy() para inicialización perezosa de una propiedad**

```kotlin
fun obtenerDatosPesados(): String {
    println("Calculando datos pesados... (esto solo se verá una vez)")
    // ...
    return "¡Datos listos!"
}

class ProcesadorDeDatos {
    // La lambda { obtenerDatosPesados() } no se ejecuta aquí, sino la primera
    // vez que se lea la propiedad.
    val datos: String by lazy { obtenerDatosPesados() }

    fun usarDatos() {
        println("Vamos a usar los datos...")
        println(datos) // <-- PRIMER ACCESO: Se ejecuta la lambda
    }

    fun usarDatosDeNuevo() {
        println("Vamos a usar los datos otra vez...")
        println(datos) // <-- SEGUNDO ACCESO: Se devuelve el valor ya guardado
    }
}

fun main() {
    val procesador = ProcesadorDeDatos()
    procesador.usarDatos()
    procesador.usarDatosDeNuevo()
}
```

Por defecto, la inicialización de `lazy` es segura en entornos multihilo (_thread-safe_). Esto significa que si varios hilos intentan acceder a la propiedad al mismo tiempo, solo uno de ellos ejecutará la _lambda_ de inicialización. Los demás esperarán a que termine y recibirán el resultado.

Podemos personalizar este comportamiento pasando un parámetro de tipo `LazyThreadSafetyMode` a la función `lazy()`. Podemos usar los siguientes valores de la enumeración `LazyThreadSafetyMode`:

- **`LazyThreadSafetyMode.SYNCHRONIZED` (por defecto):** Bloqueo seguro. Solo un hilo inicializa el valor.
- **`LazyThreadSafetyMode.PUBLICATION`:** Varios hilos pueden ejecutar la _lambda_ simultáneamente, pero solo el valor devuelto por el primer hilo que termine será utilizado. Útil si la inicialización es rápida pero el bloqueo es costoso.
- **`LazyThreadSafetyMode.NONE`:** Sin seguridad. Si varios hilos acceden a la vez, el comportamiento es indefinido. Úsalo solo cuando estés seguro de que la propiedad siempre se accederá desde un único hilo.

**Especificar el modo de seguridad en lazy**

```kotlin
// Este delegado no usará bloqueos, optimizando el rendimiento en un entorno de un solo hilo.
val datosRapidos: String by lazy(LazyThreadSafetyMode.NONE) { "Cálculo rápido" }
```

Utilizar la inicialización perezosa es una decisión estratégica con beneficios claros:

- **Arranque más rápido:** El tiempo de creación de la clase se reduce, ya que se posponen las inicializaciones pesadas. Por tanto, la clase en la que se encuentra la propiedad tarda menos en estar disponible.
- **Ahorro de recursos:** Si una propiedad nunca se usa en un determinado flujo de ejecución, su costosa inicialización nunca se realiza, ahorrando memoria y tiempo de CPU. Si una propiedad no es usada en el código, el IDE nos informará de ello.
- **Inicialización en el momento correcto:** Permite inicializar propiedades cuyo valor depende de un estado que solo está disponible después de la construcción del objeto. En algunos casos, algunos objetos deben ser creados más adelante, una vez haya sido creada la instancia de la clase. Un ejemplo característico de esto es la inicialización de las propiedades correspondiente a las vistas de la interfaz de usuario de una actividad Android, cuyo valor sólo puede ser obtenido una vez haya sido creado el propio objeto actividad y se haya llamado al método `setContentView()` de la misma para establecer la interfaz.

Por este motivo el uso de `lazy()` está recomendado cuando se cumplan a la vez todas estas condiciones:

1. La propiedad es de **solo lectura (`val`)**.
2. El **cálculo o creación** del valor es costoso (consume tiempo, memoria o recursos externos).
3. **No se garantiza** que la propiedad vaya a ser utilizada siempre.
4. El valor se necesita **más de una vez**. Si solo se va a usar una vez, una función o un _getter_ personalizado podría ser más apropiado.

[Explicación en video](https://www.youtube.com/embed/6A7dUtQq1hk)

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.10 · Conexión perezosa con lazy|Ejercicio 8.10 · Conexión perezosa con lazy]]  
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.11 · Singleton perezoso con by lazy|Ejercicio 8.11 · Singleton perezoso con by lazy]]

## 12. lazy vs. lateinit

Como vemos, `lazy` ofrece una alternativa a `lateinit` a la hora de definir una propiedad para la que en el momento de la definición no podemos establecer su valor inicial. Pero, ¿cuándo se recomienda usar una o la otra?.

> [!tip] Sugerencia
> En general, se recomienda usar `lazy` si la obtención del valor de inicialización es costosa y es posible que nunca vaya a producirse, y usar `lateinit` en cualquier otro caso.

Debemos tener en cuenta además las restricciones establecidas por `lazy`y `lateinit`, como por ejemplo que `lazy` sólo puede usarse para definir propiedades `val`, y `lateinit` sólo puede usarse para definir propiedad `var lateinit` que no sea de tipo primitivo o de tipo _nullable_.

Una ventaja adicional de usar `lazy` frente a usar `lateinit` es que la propiedad será forzosamente de referencia inmutable `val`, por lo que no podremos modificarla por error, mientras que con `lateinit` será de referencia mutable `var`, lo que implica que podremos modificarla, incluso aunque no debiéramos.

A continuación se muestra un tabla comparativa entre ambos:

|lateinit var|by lazy|
|---|---|
|Puede inicializarse desde cualquier lugar en el que el objeto sea accesible|Sólo puede ser inicializado desde dentro de la lambda|
|Es posible inicializarlo varias veces|Sólo se puede inicializar una vez|
|No es _thread-safe_ por defecto|_Thread-safe_ por defecto, y se garantiza que el código de inicialización es llamado una única vez|
|Sólo se puede usar con variables mutables `var`|Sólo se puede usar con variables inmutables `val`|
|No se puede usar con tipos primitivos|Se puede usar en tipos primitivos|

## 13. Otros delegados predefinidos

La librería estándar de Kotlin proporciona un conjunto de clases de delegados predefinidas, accesibles a través de funciones constructoras dentro del objeto `Delegates`, que cubren casos de uso comunes en el desarrollo de software.

Como ya sabemos, para que una clase actúe como delegada, debe implementar los operadores `getValue()` y, si es una propiedad mutable (`var`), el operador `setValue()`. Estos operadores son invocados automáticamente por el compilador de Kotlin cuando se accede o se modifica la propiedad delegada.

Las funciones constructoras que vamos a estudiar a continuación devuelven instancias de clases internas que cumplen precisamente con estos requisitos, y que implementan una determinada política de delegación. Estas funciones constructoras son parte del `object` denominado `Delegates` y proporcionan soluciones listas para usar para la gestión del ciclo de vida y la observación de propiedades mutables (`var`).

### 13.1 Delegates.notNull()

La función constructora `Delegates.notNull<T>()` crea un delegado que internamente almacena el valor de la propiedad. Se utiliza para propiedades mutables (`var`) de tipo no nulo (`T`) que no pueden inicializarse en el constructor de la clase. A cambio, se delega su inicialización al objeto delegado. Es un patrón común en escenarios como la inyección de dependencias o durante una fase de configuración posterior a la construcción del objeto.

Su funcionamiento es el siguiente. La propiedad no tiene asignado inicialmente ningún valor. Internamente el delegado tiene una propiedad de tipo `T?` inicializada a `null`, pero si se trata de acceder al valor de la propiedad y el delegado tiene `null` en su propiedad interna, lanza la excecpión `IllegalStateException`. Cada vez que se le asigna un valor a la propiedad, el delegado lo almacena como valor de su propia interna, y devuelve el valor de dicha propiedad interna cada vez que se lee la propiedad (a no ser que sea `null` en cuyo caso lanza la excepción comentada).

Luego básicamente, este delegado nos permite definir una propiedad de un tipo no nullable, pero no inicializarla en el momento de la definición.

**Uso de Delegates.notNull() para inicialización tardía de un tipo primitivo**

```kotlin
import kotlin.properties.Delegates

class ConfigManager {
    // No se puede usar lateinit, por ser de tipo Int.
    var puerto: Int by Delegates.notNull()

    fun configurar(puerto: Int) {
        this.puerto = puerto // Asignación de valor (inicialización)
        println("Puerto configurado a ${this.puerto}")
    }
}

fun main() {
    val manager = ConfigManager()
    // ERROR DE EJECUCIÓN: Intentar leer 'manager.puerto' aquí lanzaría IllegalStateException.
    println("Puerto actual: ${manager.puerto}")
    manager.configurar(8080)
    // Ahora se puede acceder de forma segura
    println("Puerto actual: ${manager.puerto}")
}
```

Como vemos, la funcionalidad de este delegado se asemeja bastante al de la palabra reservada `lateinit`. Ambos resuelven el mismo problema, pero tienen diferencias sutiles:

|Característica|`var ... by Delegates.notNull()`|`lateinit var`|
|---|---|---|
|**Naturaleza**|Función de la biblioteca estándar|Palabra clave del lenguaje|
|**Excepción por fallo**|`IllegalStateException`|`UninitializedPropertyAccessException`|
|**Tipos Primitivos**|✅ **Funciona** con `Int`, `Boolean`, etc.|❌ **No funciona con tipos "primitivos"** (requiere tipos de objeto)|
|**Rendimiento**|Ligeramente más lento (despreciable)|Ligeramente más rápido (comprobación nativa)|

Por tanto, la recomendación es usar **`lateinit`** como opción predeterminada para propiedades de tipo objeto, ya que es más idiomático y ligeramente más eficiente, reservando el uso de **`Delegates.notNull()`** a cuando necesitamos trabajar con tipos "primitivos" (`Int`, `Double`, `Boolean`...) o preferimos la semántica de un objeto delegado explícito.

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.12 · Delegates.notNull() con un Boolean|Ejercicio 8.12 · Delegates.notNull() con un Boolean]]

### 13.2 Delegates.observable()

La función `Delegates.observable(valor_inicial, lambda)` es una función constructora de un objeto delegado que actúa como herramienta poderosa para reaccionar a los cambios en el valor de una propiedad. Esta función recibe dos parámetros: el valor inicial que debe tomar la propiedad, y una _lambda_ que será ejecutada cada vez que se asigne un nuevo valor a la propiedad.

Esta _lambda_ recibe tres parámetros:

- `prop`: Los metadatos de la propiedad (`KProperty<*>`).
- `oldValue`: El valor que tenía la propiedad _antes_ de la asignación.
- `newValue`: El nuevo valor que se le está asignando.

Este delegado es perfecto para implementar el patrón _Observer_, donde necesitamos ejecutar una acción justo después de que haya cambiado el valor de una determinada propiedad, como por ejemplo actualizar la interfaz de usuario, notificar a otros componentes o registrar el cambio de valor en un _log_.

Internamente el objeto delegado dispone de una propiedad interna del mismo tipo que el de la propiedad que delega, cuyo valor inicial corresponderá al valor proporcionado a la función constructora `Delegates.observable()`. Cada vez que se lee el valor de la propiedad, el delegado devuelve el valor de la propiedad interna. Por otra parte, cada vez que se asigna un nuevo valor a la propiedad, dicho valor se establece como valor de la propiedad interna del delegado, y se ejecuta la lambda proporcionada a la función constructora `Delegates.observable()`, pasándole como argumento la propiedad, el valor que tenía la propiedad interna antes de la asignación, y el nuevo valor que se le acaba de asignar.

**Uso del delegado Delegates.observable() para observando cambios en el valor de una propiedad**

```kotlin
import kotlin.properties.Delegates

class Tarea {
    var estado: String by Delegates.observable("<sin asignar>") { prop, oldValue, newValue ->
        println("${prop.name} ha cambiado de '$oldValue' a '$newValue'")
    }
}

fun main() {
    val tarea = Tarea()
    println("Estado inicial: ${tarea.estado}") // Se lee el valor sin activar el observer
    tarea.estado = "En progreso"
    tarea.estado = "Completada"
    tarea.estado = "Archivada"
}
```

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.13 · Delegates.observable() para el estado de conexión|Ejercicio 8.13 · Delegates.observable() para el estado de conexión]]

### 13.3 Delegates.vetoable()

La función constructora `Delegates.vetoable()` construye un objeto delegado muy similar al que construye `Delegates.observable()`, pero con una capacidad adicional crucial: puede **vetar o rechazar un cambio** en el valor de una propiedad.

Esta función también recibe dos parámetros: el valor inicial que debe tomar la propiedad, y una _lambda_ que será ejecutada cada vez que se asigne un nuevo valor a la propiedad.

Esta _lambda_ recibe tres parámetros:

- `prop`: Los metadatos de la propiedad (`KProperty<*>`).
- `oldValue`: El valor que tenía la propiedad _antes_ de la asignación.
- `newValue`: El nuevo valor que se le está asignando.

Sin embargo, y a diferencia de en el caso de `Delegates.observable()`, esta _lambda_ debe devolver un `Boolean`. Si devuelve `true`, el nuevo valor se asigna a la propiedad. Si devuelve `false`, la asignación se ignora y la propiedad conserva su valor anterior, pero NO se lanza ninguna excepción, simplemente la asignación no se lleva a cabo.

Por tanto la ejecución de la lamba se realiza antes de una posible almacenamiento del nuevo valor de la propiedad en la propiedad interna del objeto delegado. En esto difiere respecto a `Delegates.observable()`, donde la _lambda_ se ejecuta después de haber almacenado el nuevo valor en la propiedad interna.

Este delegado es ideal para implementar lógica de validación. Te permite asegurar que una propiedad solo acepte valores que cumplan ciertas condiciones, manteniendo el objeto en un estado consistente.

**Uso de Delegates.vetoable() para validar la asignación a una propiedada**

```kotlin
import kotlin.properties.Delegates

class Jugador {
    // La puntuación no puede ser negativa.
    var puntuacion: Int by Delegates.vetoable(0) { prop, oldValue, newValue ->
        if (newValue >= 0) {
            println("Aceptando cambio de ${prop.name}: $oldValue -> $newValue")
            true // Aceptamos el cambio
        } else {
            println("VETANDO cambio de ${prop.name}: El valor $newValue es negativo.")
            false // Rechazamos el cambio
        }
    }
}

fun main() {
    val jugador = Jugador()
    println("Puntuación inicial: ${jugador.puntuacion}")
    jugador.puntuacion = 100 // Cambio válido
    println("Puntuación actual: ${jugador.puntuacion}")
    jugador.puntuacion = -50 // Cambio inválido
    println("Puntuación final: ${jugador.puntuacion}")
}
```

> [!example] Práctica
> [[08.1 - Ejercicios 8 POO III#Ejercicio 8.14 · Delegates.vetoable() para validar temperaturas|Ejercicio 8.14 · Delegates.vetoable() para validar temperaturas]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Top-level function | `fun greet() { … }` fuera de una clase | Sustituye a las clases de utilidad con métodos `static` de Java. |
| Top-level property | `var opCount = 0` fuera de una clase | Obligatorio inicializarla al declararla. |
| Constante de compilación | `const val MAX = 2000` | Solo primitivos o `String`, top-level o dentro de un `object`. |
| `lateinit` | `lateinit var x: Tipo` | `var` no nullable y no primitiva; si se lee sin inicializar → `UninitializedPropertyAccessException`. |
| Extension function | `fun String.lastChar() = …` | Se llama como un método, pero es estática: no ve lo `private` y se resuelve en compilación. |
| Extension property | `val <T> List<T>.lastPosition get() = …` | Sin _backing field_: solo _getter_/_setter_ calculados. |
| Sobrecarga de operadores | `operator fun plus(p: Point)` | Cada símbolo se traduce a un método (`a + b` → `a.plus(b)`). |
| Delegación de interfaz | `class Goblin : Creature by GenericCreature(2, 1)` | Composición en lugar de herencia; se pueden delegar varias interfaces. |
| Delegación de propiedad | `var p: String by MyDelegate()` | El delegado aporta `getValue()` (y `setValue()` si es `var`). |
| Delegar en otra propiedad | `var value: String by ::_value` | Alias de una propiedad existente. |
| `lazy` | `val datos by lazy { … }` | Se calcula en el primer acceso y se guarda; solo `val`; _thread-safe_ por defecto. |
| `Delegates.notNull()` | `var puerto: Int by Delegates.notNull()` | Como `lateinit` pero vale para primitivos; falla con `IllegalStateException`. |
| `Delegates.observable()` | `by Delegates.observable(inicial) { prop, old, new -> … }` | Reacciona **después** de cada asignación. |
| `Delegates.vetoable()` | `by Delegates.vetoable(inicial) { prop, old, new -> Boolean }` | Decide **antes** de asignar: `false` rechaza el cambio. |

## Relaciones

- Ejercicios del tema: [[08.1 - Ejercicios 8 POO III]]
- [[07 - POO II]] — interfaces, `data class` y clases abstractas que aquí se delegan y extienden.
- [[06 - POO I]] — propiedades, `field`, `companion object` y visibilidad.
- [[05 - Operaciones con tipos nullables]] — alternativa nullable a `lateinit` y operadores `?.` y `!!`.
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar qué genera el compilador al escribir una _top-level function_ (`PrintUtilsKt`).
- [ ] Saber qué requisitos debe cumplir una propiedad para llevar `const`.
- [ ] Enumerar las restricciones de `lateinit` y la excepción que lanza.
- [ ] Explicar por qué una _extension function_ no puede acceder a miembros `private` y por qué se resuelve en compilación.
- [ ] Traducir operadores a sus métodos (`+`, `[]`, `in`, `+=`, `==`...).
- [ ] Usar `by` para delegar una interfaz y sobrescribir solo algún método.
- [ ] Crear un delegado de propiedad con `getValue()`/`setValue()` o con `ReadWriteProperty`.
- [ ] Decidir entre `lazy` y `lateinit` según la tabla comparativa.
- [ ] Diferenciar `Delegates.notNull()`, `observable()` y `vetoable()`.
