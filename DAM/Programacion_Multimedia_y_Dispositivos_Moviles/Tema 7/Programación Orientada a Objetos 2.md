---
asignatura: PMDM
tema: 7
tipo: tema
estado: completo
fecha: 2026-09-30
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-poo
---

# 07 · Programación Orientada a Objetos II

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 7 · Kotlin  
> Ejercicios: [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2]]

> [!info] Material de referencia
> [POO en Kotlin II](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b07%20-%20POO%20en%20Kotlin%20II/)

## Índice del tema

- [[#Data class]]
- [[#Desestructuración]]
- [[#Pair y Triple]]
- [[#Data object declarations]]
- [[#Clases abstractas]]
- [[#Enumeraciones]]
- [[#Interfaces]]
- [[#Anonymous object expression]]
- [[#Sealed classes]]
- [[#Sealed class vs enum]]
- [[#Sealed interfaces]]
- [[#Inline value classes]]

---

## Data class

A menudo tenemos que crear clases cuyo propósito principal es simplemente contener datos, y además no participan de la herencia.

En dichas clases se suele implementar funcionalidad estándar derivada de los datos contenidos en ella, como, por ejemplo, los métodos `equals()`, `hashCode()` o `toString()`.

En Java, ese tipo de clases suelen recibir el nombre de **POJOs** (_Plain Old Java Objects_, Objeto Java Viejo y Simple). En Kotlin, se denominan **_data classes_ (clases de datos)** y para definirlas usaremos la palabra reservada `data`.

Al definir una clase como _data class_, el compilador generará automáticamente para nosotros los métodos mencionados anteriormente, sin que tengamos que hacer nada.

Por ejemplo, al definir la siguiente clase:
**Data class**

```kotlin
data class User(val name: String, val age: Int)
fun main() {
    val user = User("Baldomero", 20)
    println("user.name vale ${user.name}")
    println("user.age vale ${user.age}")
    println("user.toString() vale ${user.toString()}")
    println("user.component1() vale ${user.component1()}")
    println("user.component2() vale ${user.component2()}")
}
```

El compilador generará automáticamente dentro de la clase los siguientes métodos:

- El método `equals()`, cuya implementación comprueba ambos objetos son de tipo definido con `data`, y compara los dos objetos propiedad a propiedad (en vez de simplemente comparar la dirección de memoria, como ocurren en `Any`).
- El método `hashCode()`, calculado en base a los códigos _hash_ de las propiedades definidas en el constructor primario (en vez de a partir de la dirección en memoria, como ocurre en `Any`).
- El método `toString()` con el formato de salida `"User(name=John, age=42)"`.
- Los métodos `component1()` y `component2()`, que retornan las correspondientes propiedades, en el orden en el que aparecen en la declaración.
- El método `copy()`, que permite crear una copia de un objeto, modificando alguno de los datos si es necesario.

Las _data classes_ deben cumplir una serie de requisitos:

- El constructor primario debe contener al menos un parámetro. Si necesitamos un constructor vacío podemos asignar al parámetro un valor por defecto.
- Todos los parámetros del constructor primario deben definir propiedades, es decir deben ser marcados con `val` o `var`.
- No pueden ser marcadas con `abstract`, `open`, `sealed` o `inner`.

Como vemos en el ejemplo anterior, es muy habitual que no necesitemos definir el cuerpo de una _data class_ porque el compilador de Kotlin generará para nosotros toda la funcionalidad que necesitamos. Sin embargo, si queremos, **podemos proporcionar en el cuerpo de la clase nuestra propia implementación de los métodos `equals()`, `hashCode()` o `toString()`**, en cuyo caso el compilador no generará la implementación por defecto de los mismos. Por ejemplo:
**Sobrescritura de métodos en data class**

```kotlin
data class User(val name: String, val age: Int) {
    override fun toString(): String = "$name ($age)"
}
fun main() {
    val user = User("Baldomero", 20)
    println("user.toString() vale ${user.toString()}")
}
```

> [!warning] Aviso
> Para los métodos `component1()`, `component2()`, ..., y el método `copy()` está prohibido proporcionar una implementación personalizada.

Las propiedades de una _data class_ puede ser definidas usando tanto `val` como `var`. En general, Kotlin promulga la **inmutabilidad**, por lo que es muy habitual las _data classes_ solo contengan propiedades `val`.

Además, gracias al método `copy()` que tienen todas las _data classes_ es muy fácil crear una copia de un objeto de esa clase. El método `copy()` define un parámetro opcional por cada propiedad de la _data class_, cuyo argumento por defecto corresponderá al valor de dicha propiedad en el objeto sobre el que ejecutemos el método.

De esta manera podemos crear tanto una copia exacta de nuestro objeto, simplemente no indicando ningún argumento, o crear una copia indicando nuevos valores para determinadas propiedades. Debemos tener en cuenta que `copy()` **realiza lo que se conoce como _shallow copy_**, es decir que cuando se copia una propiedad, la propiedad en la nueva copia apuntará al mismo objeto, por lo que si dicho objeto es mutable, al cambiar alguna de las propiedades de dicho objeto desde una copia, la otra copia también verá los efectos. Sin embargo si el objeto es inmutable no tendremos ese problema. Por ello, podemos decir que el uso de `copy()` está pensado especialmente para promover la inmutabilidad.

Por ejemplo, podemos crear las siguientes copias de un objeto de la _data class_ anterior de la siguiente manera:
**Método copy() de un data class**

```kotlin
data class User(val name: String, val age: Int)
fun main() {
    val user = User("Baldomero", 20)
    val userCopy = user.copy()
    val derivedUser = user.copy(age = 23)
    println("user.toString() vale ${user.toString()}")
    println("userCopy.toString() vale ${userCopy.toString()}")
    println("derivedUser.toString() vale ${derivedUser.toString()}")
}
```

Debemos tener en cuenta que las _data classes_ **pueden heredar de otra clase e implementar interfaces**, pero **no se puede heredar de ellas**, ya que no podemos definirlas usando la palabra reservada `open`. Además, no pueden ser abstractas, ya que no podemos usar `abstract` al definirlas, ni tener una referencia a la clase externa si están definidas dentro de otra clase, ya que no podemos definirlas usando `inner`.

Las _data class_ **pueden tener otros métodos y propiedades**, aunque no es habitual.

El **constructor primario de una data class no puede recibir parámetros que no sean propiedades**. La regla fundamental de una _data class_ es que todos los parámetros de su constructor primario deben ser declarados como propiedades, es decir, deben ir precedidos por `val` o `var`. El motivo es que el propósito de una _data class_ es actuar como un contenedor de datos.

El compilador **utiliza exclusivamente las propiedades definidas en el constructor primario para generar automáticamente los métodos `equals()`, `hashCode()`, `toString()`, `componentN()` y `copy()`**, por lo que si queremos que una determinada propiedad no sea tenida en cuenta en la generación, bastará con definirla en el cuerpo de la clase.
**Propiedades no incluidas en los métodos generados**

```kotlin
data class User(val name: String) {
    // Esta propiedad no es tenida en cuenta en la generación de los métodos.
    var age: Int = 0
}
```

A partir del ejemplo anterior, dado que la propiedad `age` no es tenida en cuenta en la generación del método `equals()`, dos personas serán consideradas como iguales si tienen el mismo nombre, aunque tengan edades diferentes.

Una _data class_ puede tener constructores secundarios, igual que cualquier otra clase.

Otro aspecto que debemos tener en cuenta es que si las propiedades de una _data class_ son mutables, no será posible mantener una restricción invariante entre varias de dichas propiedades mutables, ya que se podrán modificar independientemente. De ahí, que por lo general se recomiende que las _data class_ incluya únicamente propiedes `val`.

Kotlin data class vs. Java record

La versión 16 de Java incorporó los `record` (registros), que al igual que las `data class` de Kotlin, sirven para simplificar la creación de clases que almacenan datos. Sin embargo hay una serie de diferencias importantes entre ellos:

- Las `data class` funcionan con cualquier versión de la JVM, mientras que `record` solo funciona a partir de Java 16.
- Las `data class` pueden heredar de otras clases, mientras que los `record` son `final` por defecto, por lo que no pueden heredar de otras clases.
- Las `data class` no son estrictamente inmutables; los parámetros de los constructores pueden ser `val` (inmutables) o `var` (mutables), lo que permite modificar los atributos. Sin embargo, los campos de los `record` son siempre inmutables.
- Las `data class` generan el método `copy()` y los métodos `component1()`, `component2()`, etc., mientras que los `record` no generan dichos métodos.
- Las `data class` pueden tener constructores secundarios, mientras que los `record` tienen un único constructor canónico y no pueden tener constructores secundarios (aunque podemos sobrecargar el constructor canónico con lógica personalizada).
- Los constructores de las `data class` pueden tener parámetros opcionales con argumentos por defecto, mientras que el constructor canónico de un `record` debe incluir todos los componentes.

[Vídeo: explicación]

[Explicación en video](https://www.youtube.com/embed/jVFOpuVV3As)

## Desestructuración

Como acabamos de ver, el _bytecode_ generado por el compilador de Kotlin para la _data class_ también incluirá un método `componentN()` por cada una de las propiedades definidas en el constructor primario de la clase.

Cada uno de estos métodos retornará el campo correspondiente a la una propiedad. Así, **`component1()` retornará el valor de la primera propiedad** que haya sido definida en el constructor primario de la _data class_, **`component2()` retornará el valor de la segunda**, y así sucesivamente.

El objetivo de la existencia de estos métodos es permitir usar objetos de esta clase en una expresión de **declaración por desestructuración**.

Desestructuración

La desestructuración, existente también en otros lenguajes de programación, como JavaScript, permite **asignar a una lista de variables individuales las propiedades o valores de una determinada estructura, en una única operación de asignación**, en vez de tener que acceder individualmente a cada uno de las propiedades o valores de la estructura y realizar una operación de asignación para cada una de ellas.

Así, si tenemos un objeto de la clase `User` que posee tres propiedades, `name`, `age` y `siblings`, podemos asignar a variables individuales cada una de estas propiedades haciendo uso de una operación de desestructuración:
**Desestructuración**

```kotlin
data class User(val name: String, val age: Int, val siblings: Int)
fun main() {
    val jane = User("Jane", 35, 2)
    // Se declaran las variables name, age y siblings, y se le asigna como valores
    // las propiedades del objeto jane (en el orden en el que están definidas)
    // en la data class User.
    val (name, age, siblings) = jane
    println("$name, $age years old, $siblings siblings")
}
```

Así, en el ejemplo anterior, en una única operación de asignación se está asignando el valor de la propiedad `name` del usuario `jane` a la variable `name`, el valor de la propiedad `age` del usuario `jane` a la variable `age` y el valor de la propiedad `siblings` del usuario `jane` a la variable `siblings`.

Por defecto, todas las _data classes_ permiten usar la operación de desestructuración, ya que contienen los métodos `component1()`, `component2()`, etc. En realidad **estos métodos pueden ser implementados por cualquier clase para la que queramos que se pueda llevar a cabo desestructuración, ya que se trata de métodos para sobrecarga de operadores**.

La operación de desestructuración en Kotlin No permite elegir exactamente a qué propiedades del objeto queremos acceder. Siempre usa las primeras `n` propiedades, donde `n` es el número de variables que se indican en la operación. Es decir, que **es posicional**. Por ejemplo:
**La desestructuración es posicional**

```kotlin
data class User(val name: String, val age: Int, val siblings: Int)
fun main() {
    val jane = User("Jane", 35, 2)
    // Se obtiene el nombre y la edad
    val (name, age) = jane
    println("$name, $age years old")
}
```

El problema de esto es que es sencillo cometer errores. Así, en el siguiente ejemplo, podemos pensar que estamos obteniendo el nombre y el número de hermanos, pero en realidad estaremos obteniendo el nombre y la edad, ya que la desestructuración se hace de forma posicional por orden de definición de las propiedades:
**Errores en desestructuración posicional**

```kotlin
val jane = User("Jane", 35, 2)
// Ojo, se obtiene el nombre Y LA EDAD!!!
val (name, siblings) = jane
println("$name, $siblings siblings")
```

Gracias a que en el ejemplo anterior hemos usado como nombres de las variables destinatarias de la desestructuración los mismos que las propiedades del objeto, el IDE será capaz de mostrarnos un _warning_ indicando que el nombre de la varible `siblings` coincide con el de una propiedad distinta a la que se le está asignando. Sin embargo, no es más que un _warning_, por lo que el código compila correctamente, aunque no haga lo que debe.

También debemos tener en cuenta que si cambiamos el orden de definición de las propidades en la _data class_ deberemos también cambiar todas las instrucciones en la que se haga desestructuraciónd de dicha _data class_. De ahí, que por lo general la desestructuración posicional se considere peligrosa.

**Si tan solo necesitamos desestructurar un subconjunto de propiedades del objeto, podemos usar el carácter `_` como nombre de variable de aquellas propiedades para las que no estemos interesados**. Por ejemplo, si no estamos interesados en la edad, pero si en el nombre y en el número de hermanos, podemos hacer:
**Omisión de propiedades en desestructuración posicional**

```kotlin
data class User(val name: String, val age: Int, val siblings: Int)
fun main() {
    val jane = User("Jane", 35, 2)
    // Se obtiene el nombre y el número de hermanos
    val (name, _, siblings) = jane
    println("$name, $siblings siblings")
}
```

[Vídeo: explicación]

[Explicación en video](https://www.youtube.com/embed/9zmexFhkESk)

## Pair y Triple

Kotlin proporciona en su librería estándar varias _data class_ predefinidas para manejar conjuntos pequeños y genéricos de datos. Las más comunes son `Pair<A, B>` y `Triple<A, B, C>`, diseñadas como contenedores inmutables para dos o tres valores de cualquier tipo, respectivamente.

Aunque son herramientas útiles, su uso debe ser medido. La recomendación principal es favorecer la creación de _data class_ personalizadas siempre que los datos tengan un significado o una relación conceptual. Una clase como `data class Point(val x: Int, val y: Int)` es inmensamente más legible y segura que `Pair<Int, Int>`.

La forma más directa de crearun objeto de estas clases es a través de su constructor. Los valores se acceden a través de las propiedades `first`, `second` y `third` (en el caso de `Triple<A, B, C>`).
**Creación de Pair y Triple a través del constructor**

```kotlin
fun main() {
    val contact = Pair("EMAIL", "student@university.com")
    val coordinates = Triple(40.4167, -3.70325, 15)
    println(contact.first) // EMAIL
    println(contact.second) // student@university.com
    println(coordinates.first) // 40.4167
}
```

Kotlin ofrece además la _extension function_ infija `to`, que permite crear un `Pair` de forma muy legible a partir de un valor de cualquier tipo. No existe un equivalente para crear un `Triple`. Además, al ser _data classes_, tanto `Pair` como `Triple` soportan la desestructuración, que permite extraer sus valores directamente en variables.
**Creación de Pair con la función to y desestructuración de Pair y Triple**

```kotlin
fun main() {
    // Creación de un Pair usando la función infija 'to'
    val userRole = "admin" to 1
    // Desestructuración para acceder a los datos
    val (roleName, roleId) = userRole
    println("$roleName has ID $roleId") // Muestra "admin has ID 1"
    val location = Triple("Madrid", "Spain", 2025)
    val (city, country, year) = location
    println("City: $city, Country: $country, Year: $year")
}
```

Además, las clase `Pair` y `Triple` incluyen un método muy práctico, `toList()`, que permite obtener una lista con los datos de un `Pair` o `Triple`.
**Método toList() de Pair o Triple**

```kotlin
fun main() {
    val dimensions = Pair(1920, 1080)
    val dimensionList = dimensions.toList() // Devuelve una List<Int> con [1920, 1080]
    println(dimensionList)
}
```

El uso de `Pair` y `Triple` es ideal en ámbitos locales y privados, donde la falta de nombres de propiedad no afecta a la legibilidad general. Por ejemplo, para devolver múltiples valores de una función privada. De esa manera evitamos la creación de una _data class_ que solo se usará una vez.
**Uso de un Pair como tipo de retorno de una función que calcula el mínimo y el máximo**

```kotlin
private fun findMinMax(numbers: List<Int>): Pair<Int, Int>? {
    if (numbers.isEmpty()) return null
    return numbers.minOrNull()!! to numbers.maxOrNull()!!
}
fun main() {
    val (min, max) = findMinMax(listOf(5, 1, 9, 3)) ?: (0 to 0)
    println("Min: $min, Max: $max")
}
```

También podemos usar `Pair` y `Triple` como resultado intermedio en expresiones. El ejemplo del `when` es un caso de uso excelente, ya que el `Pair` existe solo dentro de ese contexto limitado.
**Uso local de Pair como resultado intermedio en expresión**

```kotlin
import kotlin.random.Random
fun main() {
    val degrees = Random.nextInt(45)
    val (description, color) = when {
        degrees < 15 -> "cold" to "Blue"
        degrees < 30 -> "mild" to "Yellow"
        else -> "hot" to "Red"
    }
    println("$description - $color")
}
```

Sin embargo, debemos evitar el uso de `Pair` o `Triple` en situaciones donde la claridad del código a largo plazo es crucial, como por ejemplo en APIs públicas o propiedades de una clase, donde exponer un `Pair<String, String>` en una función o propiedad es ambiguo. ¿Qué representa en ese caso `first` y `second`? Esto obliga a quien use el código a adivinar el contexto. Por este motivo, en esos casos es mucho más adecuado definir una _data class_ personalizada.

Otro caso en el que NO está recomendado el uso de `Pair` o `Triple` es cuando estemos anidándolos. Si nos encontramos escribiendo `Pair<String, Triple<Int, Int, Boolean>>`, es una señal inequívoca de que necesitamos una _data class_ personalizada.

La ventaja de usar _data classes_ personalizadas es que, de esa forma, propocionamos nombres significativos a los datos en forma de propiedades, lo que hace que nuestro código sea mucho más legible. Además, si queremos restringir el acceso a la _data class_ personalizada a un fichero o a una clase concreta, podemos asingarle a la _data class_ el modificador de visibilidad `private`.

## Data object declarations

Desde Kotlin 1.8, podemos usar el modificador `data` al declarar un `object`, en cuyo caso se generará automáticamente para él el método `toString()`, cuyo valor de retorno corresponderá al nombre del objeto como cadena de caracteres.
**Uso local de Pair**

```kotlin
data object ABC
fun main() {
    println(ABC) // ABC
}
```

## Clases abstractas

Para definir un clase abstracta en Kotlin, es decir, una clase que posee uno o más miembros abstractos que no poseen implementación, usaremos la palabra reservada `abstract,` tanto en el miembro correspondiente como en la propia clase.

Es importante resaltar no es necesario añadir la palabra reservada `open` ni a la clase abstracta ni a sus miembros abstractos, ya que que **toda clase abstracta es por defecto heredable y todo miembro abstracto es por definición sobrescribible**.
**Clases abstractas**

```kotlin
abstract class AbstractClass {
    abstract fun abstractMethod()
    // Puede tener métodos no abstracto
    fun concreteMethod() {
        println("Soy un método concreto de la clase AbstractClass")
    }
}
class ConcreteClass : AbstractClass() {
    override fun abstractMethod() {
        println("Soy la clase ConcreteClass")
    }
}
fun main() {
    // ERROR DE COMPILACIÓN: No se puede instanciar una clase abstracta
    val obj = AbstractClass()
    val concrete = ConcreteClass()
    concrete.abstractMethod()
    concrete.concreteMethod()
}
```

Las clases abstractas se definen como superclases de otras clases, de manera que las clases no que hereden de ella deberán implementar (o indicar como abstractos) dichos métodos abstractos.

Una clase abstracta puede contener también métodos no abstractos que deberán tener cuerpo del método, y que podrán ser llamados desde otros métodos de la clase. Por tanto, las clases abstractas se pueden usar como plantillas de implementación parcial para otras clases.

Al igual que ocurre en Java, **las clases abstractas no son instanciables**, por lo que no podemos llamar a su constructor.

## Enumeraciones

En Kotlin, **una enumeración corresponde a una clase que define un tipo de datos cuyas posibles instancias son descritas durante la propia declaración de la enumeración, asignándoles un identificador**, sin que sea posible instanciar la clase desde otro código distinto a la propia declración. **Cada instancia será un objeto de dicha clase** independiente del resto de instancias de la enumeración.

Para definir una enumeración usaremos `enum class`. En esto Kotlin difiere de Java, en donde solo indicamos `enum`. **Las instancias que se declaran en la enumeración deben separarse por coma `,`**. El identificador con el que designamos cada una de las instancias de la enumeración sigue habitualmente el estilo UPPER_SNAKE_CASE, es decir, todo en mayúscula separando cada palabra con un guión bajo, ya que deberían representar valores constantes.

El orden en el que se declaran las instancias dentro de la clase enumeración es importante, ya la clase enumeración mantiene registro de dicho orden, de manera que **cada instancia de la enumeración tiene asociado un número de orden concreto** dentro dentro de la enumeración, comenzando por el valor `0`.

Para acceder a una determinada instancia de una enumeración, usaremos el formato `idEnumeracion.idInstancia`.

Veamos un ejemplo:
**Enumeraciones**

```kotlin
enum class Direction {
    NORTH, SOUTH, WEST, EAST
}
fun main() {
    println("${Direction.NORTH}, ${Direction.SOUTH}, ${Direction.WEST}, ${Direction.EAST}")
}
```

Si no queremos tener que escribir el nombre de la enumeración a la hora de hacer referencia a una de sus instancias, podemos importar todas las instancias de la enumeración haciendo:
**Importar estáticamente todas las instancias de una enumeración**

```kotlin
import ch02.directions.Direction.*
```

Al igual que en el caso de las clases abstractas, **no es posible instanciar un objeto de la clase enumeración llamando al constructor**, ya que las únicas instancias posibles de dicha clase son las que han sido declaradas dentro de ella.
Las instancias de una enumeración son **inicializadas de forma perezosa** (_lazy initialization_), lo que significa que solo se crean cuando se utilizan por primera vez. Por ejemplo, en el ejemplo anterior, la instancia correspondiente a `Direction.NORTH` solo llegará a crearse en memoria cuando en ejecución se haga referencia a ella.
Si usamos `when` como expresión para evaluar una variable cuyo tipo corresponda a una enumeración, e indicamos una rama para cada una de las posibles instancias, entonces no será necesario especificar una rama `else`, ya que el _when_ será exhaustivo, al estar todas las opciones posibles cubiertas. Por ejemplo:
**`when` exhaustivo con una enumeración**

```kotlin
import Direction.*

enum class Direction {
    NORTH, SOUTH, WEST, EAST
}

fun getDirectionTranslation(direction: Direction) = when (direction) {
    NORTH -> "Norte"
    SOUTH -> "Sur"
    WEST -> "Oeste"
    EAST -> "Este"
}

fun main() {
    println(getDirectionTranslation(Direction.NORTH))
    println(getDirectionTranslation(Direction.SOUTH))
    println(getDirectionTranslation(Direction.WEST))
    println(getDirectionTranslation(Direction.EAST))
}
```

Todas las _enum class_ tienen las siguientes funciones predefinidas en su _companion object_:

- `values()`, que retorna un array con todas las instancias de la enumeración, en el orden en el que fueron declarados. Por ejemplo, `Direction.values()` retorna el array [`Direction.NORTH`, `Direction.SOUTH`, `Direction.WEST`, `Direction.EAST`]
- `valueOf(string)`, obtiene la instancia de la enumeración cuyo identificador corresponde a la cadena de texto recibida (siendo case-sensitive), o lanza una excepción si no lo encuentra. Por ejemplo `Direction.valueOf("NORTH")` retorna el objeto correspondiente a `Direction.NORTH`.

También existen funciones _top-level_ similares: `enumValues<T>()` y `enumValueOf<T>(string)`, donde `T` es el tipo de clase enumeración.

Cada instancias de cualquier enumeración tiene dos propiedades:

- `name`, que corresponde al nombre (identificador) de dicha instancia en la enumeración.
- `ordinal`, que corresponde a la posición de dicha instancia en la lista de valores de la enumeración (el primero es el `0`).

Cada _enum class_ es en realidad una subclase que de la clase abstracta `Enum`, que define las propiedades `name` y `ordinal`, y define su propia implementación de los métodos `toString()`, `equals()` y `hashCode()`. Además, a diferencia de en el caso de las _data class_, la clase `Enum` también **implementa el método `compareTo()` para comparar instancias de la enumeración basándose en su orden** en la lista de instancias.

Dado que una enumeración es una clase y las instancias que declaramos en ella son objetos, la enumeración **puede tener un constructor** que puede ser usado a la hora de definir las constantes. También puede contener propiedades y métodos, como cualquier otra clase.

Si la clase enumeración incluye la definición de métodos, **para separar la lista de instancias con respecto a los métodos definidos, debemos usar carácter punto y coma `;` después de la lista de instancias**. Este es uno de los pocos lugares en Kotlin donde estamos obligados a usar el punto y coma (el otro es como separador cuando ponemos varias instruccions en la misma línea).

Las propiedades definidas en la clase enumeración son evidentemete accesibles desde las instancias de la misma. **Se recomienda que las propiedades de las enumeraciones sean siempre `val`**, para que no se puedan cambiar, **dado que un valor de una enumeración representa un valor constante**.

Así, es posible definir un constructor primario para la clase enumeración, en cuyo caso debemos especificar los valores correspondientes a la hora de crear las instancias dentro de la propia clase enumeración.

Veamos un ejemplo:
**Acceso a propiedades de la enumeración**

```kotlin
enum class Color(val r: Int, val g: Int, val b: Int) {
    RED(255, 0, 0),
    ORANGE(255, 165, 0),
    // FÍJATE BIEN EN EL ; FINAL
    YELLOW(255, 255, 0);
    fun rgb() = (r * 256 + g) * 256 + b
    override fun toString(): String = "rgb($r, $g, $b)"
}
fun main() {
    println("${Color.ORANGE} ${Color.ORANGE.rgb()} ${Color.RED.r}")
}
```

Además, la clase enumeración puede definir métodos abstractos, que cada constante sobrescribirá de la forma que cree oportuna. Por ejemplo:
**Enumeración con métodos abstractos**

```kotlin
enum class Color(val r: Int, val g: Int, val b: Int) {
    RED(255, 0, 0) {
        override fun print() {
            println("I'm red")
        }
    },
    ORANGE(255, 165, 0) {
        override fun print() {
            println("I'm orange")
        }
    },
    YELLOW(255, 255, 0) {
        override fun print() {
            println("I'm yellow")
        }
    };
    // Debe ser implementado por cada constante.
    abstract fun print()
}
fun main() {
    Color.ORANGE.print()
}
```

Las enumeraciones **no pueden extender ninguna clase**, ya que internamente extienden la clase `Enum`, aunque sí que **pueden implementar interfaces**, en cuyo caso deben implementar las propiedades y métodos abstractos de éstas. Esta implementación puede realizarse **a nivel de la propia clase enumeración**, de manera que todas las instancias usarán esa implementación, **o una implementación específica para cada una de las instancias**, en cuyo caso cada instancia corresponde a una especie de object que implementa la interfaz.

Así, en el siguiente ejemplo definimos una enumeración `IntArithmetics` que implementa dos interfaces. La primera de ellas, `BinaryOperator`, es implementada a nivel de cada constante de la enumeración, de manera que cada constante tiene su propia implementación del método `apply()`. La segunda interfaz, `IntBinaryOperator`, es implementada de manera global para todas las instancias de la enumeración, con una única implementación del método `applyAsInt()`.
**Las enumeraciones pueden implementar interfaces**

```kotlin
import java.util.function.BinaryOperator
import java.util.function.IntBinaryOperator
enum class IntArithmetics : BinaryOperator<Int>, IntBinaryOperator {
    PLUS {
        override fun apply(t: Int, u: Int): Int = t + u
    },
    TIMES {
        override fun apply(t: Int, u: Int): Int = t * u
    };
    // Implementación para todas las instancias de la enumeración.
    override fun applyAsInt(t: Int, u: Int) = apply(t, u)
}
fun main() {
    println("2 + 3 = ${IntArithmetics.PLUS.apply(2, 3)}")
    println("2 + 3 = ${IntArithmetics.PLUS.applyAsInt(2, 3)}")
}
```

Esta opción no es muy popular, y normalmente se prefiere usar un constructor primario con un parámetro de tipo función o una _extension function_.

## Interfaces

Las interfaces en Kotlin son muy parecidas a las de Java 8, en el sentido de que **pueden contener tanto declaraciones de métodos abstractos como métodos con implementación por defecto**. De esta manera, lo que distigue básicamente a una interfaz de una clase abstracta es que la interfaz no puede almacenar estado, mientras que las clases abstractas sí pueden.

**No es necesario usar la palabra reservada `abstract` en la declaración de la propia interfaz ni de sus métodos**, porque, por definición, una interfaz y sus métodos y propiedades son abstractos. **Tampoco es necesario usar la palabra reservada `open`**, porque una interfaz es heredable por definición.

**Un método de una interfaz puede contener una implementación por defecto**. Sin embargo, **no usaremos ninguna palabra reservada para indicarlo**, simplemente proporcionaremos un cuerpo al método correspondiente, a diferencia de en Java 8, donde estamos obligados a marcar dichos métodos con la palabra reservada `default`.

Veamos un ejemplo de definición de una interfaz:
**Interfaces**

```kotlin
// No es necesario usar open con las interfaces
interface MyInterface {
    // No es necesario usar abstract ni open con los métodos de las interfaces.
    fun method1()
    fun method2() {
        // Implementación por defecto.
        // ...
    }
}
fun main() {}
```

**Para indicar que una clase implementa una interfaz**, lo indicaremos de forma similar a cuando indicamos que una clase hereda de otra, es decir, **en la cabecera de definción de la clase tras el carácter `:`**.

Al implementar una interfaz, la clase está obligada a sobrescribir todos los métodos y propiedades abstractas del mismo. A diferencia de en Java, en Kotlin **es obligatorio usar la palabra reservada `override`**.

**No estamos obligados a sobrescribir los métodos de la interfaz que dispongan de una implementación por defecto, pero podemos hacerlo si nos interesa**. Si desde el método que sobrescribe queremos llamar a la implementación por defecto del método en la interfaz, usaremos la palabra reservada `super` con el formato `super.metodo()`. Si la clase implementara dos interfaces con el mismo método con la misma firma y quisiéramos llamar desde el método que sobrescribe a la implementación por defecto de una de las dos interfaces haríamos `super<NombreInterfaz>.metodo()`.

Veamos un ejemplo de implementación de la interfaz anterior:
**Implementación de interfaz con métodos por defecto**

```kotlin
interface MyInterface {
    fun method1()
    fun method2() {
        // Implementación por defecto.
        println("Esta es la implementación por defecto")
    }
}
class Child : MyInterface {
    override fun method1() {
        println("Implementación de la clase")
    }
    // Usará la implementación por defecto del método method2()
    // de la interfaz MyInterface
}
fun main() {
    val child = Child()
    child.method1()
    child.method2()
}
```

**Una clase puede heredar de una única clase e implementar una o más interfaces**, para lo que indicaremos dichos elementos **separados por coma `,`** en la definción de la clase, indicando siempre **primero la clase padre de la que hereda**, si es que hereda de alguna clase. Por ejemplo:
**Implementación de varias interfaces**

```kotlin
open class Parent {
    // ...
}
interface MyInterface {
    fun method1()
    fun method2() {
        // Implementación por defecto.
        println("Esta es la implementación por defecto")
    }
}
interface AnotherInterface {
    fun anotherMethod1()
}
class Child : Parent(), MyInterface, AnotherInterface {
    override fun method1() {
        println("Esta es la implementación de la clase Child de method1")
    }
    override fun anotherMethod1() {
        println("Esta es la implementación de la clase Child de anotherMethod1")
    }
    // Usará la implementación por defecto del método method2()
    // de la interfaz MyInterface
}
fun main() {
    val child = Child()
    child.method1()
    child.method2()
    child.anotherMethod1()
}
```

Las interfaces también **pueden declarar propiedades**, para indicar que cualquier clase que la implemente deberá definir dichas propiedades. La declaración de la propiedad en la interfaz puede tener la forma de una **declaración tradicional de una propiedad, o de propiedad con _getter _personalizado, pero NO puede implicar la creación de un_ backing field_**.

Recordemos, que una interfaz no tiene estado, a diferencia de una clase abstracta, por lo que las propiedades declaradas en un interfaz, son solo una declaración de obligatoriedad de definición de dichas propiedades en las clases que implementen la interfaz, y NO implican que la interfaz en sí tenga estado (ni que se cree un _backing field_ para la propiedad en la interfaz).

Las clases que implementen la interfaz deberán definir las propiedades declaradas en la interfaz, en forma de propiedades con o sin _backing field_. **Una propiedad `val` de la interfaz podrá ser implementada en forma en forma de propiedad `var` en la clase implementadora**, porque la implementación cumple con lo requerido por la interfaz, al tener un _getter_. **Al implementar una propiedad de una interfaz también debemos usar la palabra reservada `override`**.
**Interfaz con declaración de propiedades**

```kotlin
interface MyInterface {
    // No puede tener un backing field para almacenar estado,
    // por lo que no podemos inicializarla.
    val prop: Int
    // Tiene un getter personalizado, pero no almacena estado.
    val propertyWithImplementation: String
        get() = "foo"
}
class Child : MyInterface {
    // Implementación de la propiedad abstracta, dándole valor.
    override val prop: Int = 29
}
fun main() {
    val child = Child()
    println(child.prop)
    println(child.propertyWithImplementation)
}
```

Una interfaz puede extender de otras interfaces, incluso proporcionando implementaciones por defecto para los miembros heredados:

**Herencia en interfaces**

```kotlin
interface Named {

    val name: String

}

interface Person : Named {

    val firstName: String

    val lastName: String

    // Sobrescribe la propiedad name de la interfaz Named,

    // proporcionándole una implementación por defecto.

    override val name: String get() = "$firstName $lastName"

}

data class Employee(

    // Como no se sobrescribe la propiedad name se usará para ella

    // la implementación por defecto definida en la interfaz Person.

    override val firstName: String,

    override val lastName: String,

    val position: String

) : Person

fun main() {

    val employee = Employee("John", "Doe", "Programmer")

    println(employee.name)

}
```

[Vídeo: explicación]

[Explicación en video](https://www.youtube.com/embed/LJmc_w4-yX0)

## Anonymous object expression

En algunas ocasiones se necesita **personalizar una determinada clase o interfaz específicamente para la ocasión, sin tener ni siquiera que molestarnos en establecer un nombre para ella, para obtener una instancia de dicha clase personalizada**, cuyo tiempo de vida será realmente corto.

En Kotlin, podemos crear algo similar a la sintaxis de las clases anónimas inline de Java usando la palabra reservada `object`, con la sintaxis conocida como **_anonymous object expression_ (expresión de objeto anónimo)**:
**Expresión de objeto anónimo que hereda de clase**

```kotlin
abstract class MouseAdapter {
    abstract fun mouseClicked(e: Int)
    abstract fun mouseEntered(e: Int)
}
fun main() {
    // Se crea una instancia de una clase que se está creando en ese momento y
    // que extiende de MouseAdapter, sobrescribiendo algunos de sus métodos.
    // FÍJATE bien en los paréntesis de la primera línea
    val listener = object: MouseAdapter() {
        override fun mouseClicked(e: Int) {
            println("Mouse Clicked")
        }
        override fun mouseEntered(e: Int) {
            println("Mouse Entered")
        }
    }
    listener.mouseClicked(2)
    listener.mouseEntered(5)
}
```

En el ejemplo anterior se está creando una instancia de una clase anónima que extiende de la clase `MouseAdapter`, y se sobrescriben algunos de sus métodos para personalizar la clase. Si estamos heredando de una clase estamos obligados a llamar a su constructor primario, de ahí el par de paréntesis `MouseAdapter()`.

**Cuando deseamos crear una instancia de una clase anónima que tan solo implementa una determinada interfaz, no hay que llamar al constructor de la clase padre, porque no lo hay**, así que no se debe indicar el par de paréntesis. Así, en el siguiente ejemplo creamos un objeto de una clase anónima que implementa la interfaz `ActionListener`, que es pasado como argumento al contructor de la clase `Timer` de la librería _Swing_:
**Expresión de objeto anónimo que implementa interfaz**

```kotlin
interface ActionListener {
    fun actionPerformed(e: Int)
}
fun main() {
    // Se crea una instancia de una clase que implementa la interfaz ActionListener
    // FÍJATE bien en la ausencia de paréntesis en la primera línea.
    val listener = object : ActionListener {
        override fun actionPerformed(e: Int) {
            println("Action Performed")
        }
    }
    listener.actionPerformed(2)
}
```

[Vídeo: explicación]

[Explicación en video](https://www.youtube.com/embed/h0q7q-Rt1-Q)

## Sealed classes

Como sabemos, las clases e interfaces no se usan únicamente para representar un conjunto de datos u operaciones, sino que también podemos usarlas para representar jerarquías, gracias a la herencia y al polimorfismo dinámico.

Por defecto, las clases abiertas y las interfaces permiten representar lo que se conoce como jerarquias no restringidas, es decir, abiertas a ser extendidas tanto como queramos. Sin embargo, hay ocasiones en las que de antemano **conocemos exactamente qué subtipos concretos queremos que existan de un determinado tipo abstracto, y no queremos que se puedan crear otros subtipos adicionales**. Estas jerarquías semicerradas se conocen como **jerarquías restringidas**.

Para diseñar estas jerarquías restringidas, podríamos declarar el tipo abstracto como una interfaz o una clase abstracta, y después, para los subtipos concretos, declarar las clases concretas, de manera que éstas implementen la interfaz o extiendan la clase abstracta.

El problema es que cuando usamos una interfaz normal o una clase abstracta normal para definir el tipo, no hay ninguna garantía de que las clases creadas como subtipos de éste sean los únicos subtipos que se puedan crear. Es decir, no podemos evitar que se declaren nuevos subtipos adicionales, ya que, al tratarse de una clase abstracta, está completamente abierta a ser extendida por cualquier subtipo. Por tanto, las interfaces y clases abstractas normales no nos sirven para representar jerarquías restringidas. Para solucionar este problema, aparece el concepto de clase o interfaz sellada (_sealed_).

Una **_sealed class_**, que podríamos traducir como clase sellada, se usa para representar una jerarquía restringida de clases, donde la clase padre tiene restringida su extensión, de manera que **la clase sellada solo puede tener unas determinadas subclases directas**, indicadas explícitamente, y **conocidas en tiempo de compilación**.

**Por definición, una _sealed class_ es abstracta, por lo que no puede ser instanciada y puede contener métodos y propiedades abstractos**. Sin embargo no es necesario usar la palabra `abstract` en la definición de la clase sellada, aunque sí que deberemos indicarla en los miembros abstractos que definamos en ella. Podríamos decir que una _sealed class_ es una clase abstracta con herencia directa restringida y predefinida en tiempo de compilación.

Para declarar una _sealed class_ se usará la palabra reservada `sealed` delante de `class`, como en `sealed class Post`.

**Las subclases hijas directas de una _sealed class_ pueden ser `class`, `abstract class`, `data class`, `object`, `open class`, e incluso `sealed class`**. Sin embargo, no pueden ser `enum`, objetos anónimos (_object expresion_) o ser locales a una función.

**Podemos definir las subclases hijas directas que pueda tener una _sealed class_ fuera de cualquier otra clase o como clases internas anidadas dentro de otra** (opción más habitual). En todo caso, **deben estar definidas en el mismo paquete y módulo** que la propia _sealed class_.

De esta manera, los clientes de tu librería o módulo no pueden agregar sus propias subclases directas de tu _sealed class_, ni crear clases locales o _object expresions_ (objetos anónimos) que las extiendan.

Así en el siguiente ejemplo queremos definir un tipo `Post` (publicación en red social) genérico que se concretiza en cuatro tipos de publicaciones: `Status` (estado actual), `Image` (publicación de una imagen), `Video` (publicación de video) y `Heading` (publicación de cabecera de la red social). No existen otros tipos de publicaciones.

Para ello, definiremos la _sealed class_ `Post`, y sus subclases `Status`, `Image`, `Video` y `Heading`. Se ha optado por definir los tipos de publicaciones como subclases anidadas dentro de la propia clase `Post`:
**Definición de una sealed class y sus clases hijas anidadas**

```kotlin
import kotlin.random.Random
sealed class Post {
    data class Status(val text: String): Post()
    data class Image(
        var url: String,
        var caption: String
    ) : Post()
    data class Video(
        var url: String,
        var timeDuration: Int,
        var encoding: String
    ): Post()
    object Headline : Post()
}
fun main() {
    val post: Post = if (Random.nextBoolean()) Post.Status("Inactivo") else Post.Headline
    when (post) {
        is Post.Status -> println("Status: ${post.text}")
        is Post.Headline -> println("It's a headline")
        else -> println("El post no es ni status ni headline")
    }
}
```

Debemos tener en cuenta de que **el hecho de que un clase sea subclase de una _sealed class_ no impide que podamos heredar de dicha subclase**. Esto es, lo que queda restringido al definir una _sealed class_ es las subclases hijas que ésta puede tener, pero no la jerarquía de clases que puedan extender de dichas clases hijas De hecho, las clases que extiendan de las subclases de la _sealed class_ pueden estar definidas en cualquier otro paquete. No obstante, en el ejemplo anterior ninguna de la clases hijas es heredable, al tratarse de _data classes_ y _objects_.

También podíamos haber definido las clases hijas de la clase sellada como clases de primer nivel, siempre que se encuentren en el mismo paquete que la clase sellada, aunque normalmente está recomendado definidas comoo clases internas.
**Definición de una sealed class y sus clases hijas como clases top-level**

```kotlin
import kotlin.random.Random
sealed class Post
data class Status(val text: String) : Post()
data class Image(
    var url: String,
    var caption: String
) : Post()
data class Video(
    var url: String,
    var timeDuration: Int,
    var encoding: String
) : Post()
object Headline : Post()
fun main() {
    val post: Post = if (Random.nextBoolean()) Status("Inactivo") else Headline
    when (post) {
        is Status -> println("Status: ${post.text}")
        Headline -> println("It's a headline")
        else -> println("El post no es ni status ni headline")
    }
}
```

Una _sealed class_ se diferencia de una clase abstracta `abstract class` en que no puede ser extendida por clases que no hayan sido indicadas explícitamente al compilar la propia _sealed class_, mientras que en el caso de una clase abstracta sí que es posible. Si en el ejemplo anterior definiéramos `Post` como una clase abstracta normal, nada impediría a otro desarrolaldor definir otra subclase de `Post`, por ejemplo una llamada `Audio`, cuando supuestamente la red social no permite ese tipo de publicaciones.

Los constructores de las _sealed classes_ son, por defecto `protected`, aunque también pueden ser `private`.

Cuando se usa una variable cuyo tipo corresponde a una _sealed class_ con una expresión `when` y se define una rama de comparación de tipo para cada subclase hija, no es necesario definir una rama `else`, ya que el compilador es capaz de determinar que la expresión `when` ha sido exhaustiva, al cubrirse todas las posibilidades. Además, gracias al _smart cast_, en cada rama tendremos el objeto convertido a la subclase correspondiente a dicha rama, por lo que podremos acceder directamente a las propiedades de la subclase.

Por ejemplo, supongamos que queremos crear una función que retorne un texto para un determinado _post_:
**Uso de when con una sealed class**

```kotlin
import kotlin.random.Random
sealed class Post {
    data class Status(val text: String): Post()
    data class Image(
        var url: String,
        var caption: String
    ) : Post()
    data class Video(
        var url: String,
        var timeDuration: Int,
        var encoding: String
    ): Post()
    object Headline : Post()
}
fun getPostText(post: Post): String = when(post) {
    // No es necesaria una rama else porque se cubren todas las posibilidades.
    // En cada rama se realiza smart cast al tipo correspondiente.
    is Post.Status -> post.text
    is Post.Image -> post.caption
    is Post.Video -> post.url
    // Como Headline es un object, no tenemos que preguntar si
    // es de una clase, sino que podemos preguntar directamente
    // si es el objeto en sí.
    Post.Headline -> "Headline"
}
fun main() {
    val post: Post = if (Random.nextBoolean()) Post.Status("Inactivo") else Post.Headline
    println("Post text: ${getPostText(post)}")
}
```

Debemos tener en cuenta que si en el `when` no usamos una rama `else` y posteriormente agregamos una subclase adicional a la _sealed class_, el `when` marcará un error de compilación, por lo que deberemos arreglarlo agregando una rama que tenga en cuenta el nuevo subtipo.

Esta circunstancia juega a nuestro favor en el caso de que se trate de código propio, porque nos obliga a arreglar el problema en tiempo de compilación. Sin embargo, cuando la _sealed class_ forma parte de la API pública de una librería o módulo compartido, al agregar una nueva subclase hace que el código de los módulos cliente que contengan `when` exhaustivos sobre dicha _sealed class_ sin rama `else`, dejará de funcionar, convirtiendo el cambio que hemos realizado en la librería en lo que se conoce como un _breaking change_ (cambio que hace que se "rompa" código existente, esto es, que deje de funcionar).

## Sealed class vs enum

Si comparamos una _sealed class_ con una _enum class_ nos daremos cuenta de que mientras **en una clase _enum_ se está restringiendo la instanciación de objetos de dicha clase, en una _sealed class_ lo que se está restringiendo es la herencia directa de ella**, ya que las únicas clases que pueden heredar directamente de dicha clase deben ser especificadas en tiempo de compilación.

De hecho, en una enumeración todas sus instancias son del mismo tipo y llaman al mismo constructor, el de la enumeración, si es que éste existe. Sin embargo, cada subclase hija de una _sealed class_ corresponde a un subtipo distinto, puede poseer su propio constructor, que puede ser distinto del constructor del resto de subtipos.

Respecto a la instanciación, no debemos olvidar que no podremos crear instancias de una _sealed class_, al ser abstracta por definición, pero sí podemos crear tantas instancias como queramos de las subclases directas de una _sealed class_, a no ser que dicha clase hija corresponda a un `object`, que representa un objeto _singleton_. Sin embargo, en el caso de una clase enumeración, las instancias exitentes serán únicamente aquellas definidas en la propia declaración de la enumeración, y no podremos instanciarla desde otro código.

## Sealed interfaces

También es posible crear _sealed interfaces_, es decir, interfaces selladas. Usaremos una **_sealed interface_** para representar una jerarquía restringida, donde la interfaz padre tiene restringida su implementación y su extensión, de manera que **la interfaz se sellada solo puede ser implementada por unas determinadas subclases directas y extendida directamente por unas determinadas interfaces** indicadas explícitamente, y **conocidas en tiempo de compilación**.

Las clases que implementen la interfaz sellada y las interfaces que la extiendan directamente deberán estar definidas en el mismo módulo que ella.

Las _sealed interfaces_ pueden ser **usadas en casos concretos en los que no es posible o necesario usar _sealed classes_**. Por ejemplo, podemos hacer que un `enum` implemente una _sealed interface_, ya que los `enum` pueden implementar interfaces, pero no podemos hacer que herede de una _sealed class_, ya que los `enum` no pueden heredar de otras clases.

Por otra parte, como sabemos, una clase no puede heredar de más de una clase, pero si puede implementar varias interfaces, así que podemos hacer que una clase implemente varias _sealed interfaces_, pero no podemos hacer que herede de varias _sealed classes_.

Por ejemplo, supongamos que vamos a realizar un par de peticiones para hacer login y cargar los datos del usuario. Cada petición puede producir tipos concretos de errores, pero además se pueden producir errores genéricos. Si queremos modelar lo anterior con _sealed classes_ haríamos:

**Ejemplo con varias sealed classes**

```kotlin
import kotlin.random.Random

sealed class CommonError // to reuse across hierarchies

object ServerError : CommonError()

object Forbidden : CommonError()

object Unauthorized : CommonError()

sealed class LoginError {

    data class InvalidUsername(val username: String) : LoginError()

    object InvalidPasswordFormat : LoginError()

    data class LoginCommonError(val error: CommonError) : LoginError()

}

sealed class GetUserError {

    data class UserNotFound(val userId: String) : GetUserError()

    data class InvalidUserId(val userId: String) : GetUserError()

    data class GetUserCommonError(val error: CommonError) : GetUserError()

}

fun getErrorMessage(loginError: LoginError): String = when (loginError) {

    is LoginError.InvalidUsername -> "Invalid username"

    LoginError.InvalidPasswordFormat -> "Invalid password format"

    is LoginError.LoginCommonError -> when (loginError.error) {

        Forbidden -> "Forbidden"

        ServerError -> "Server error"

        Unauthorized -> "Unauthorized"

    }

}

fun main() {

    val error: LoginError =

        if (Random.nextBoolean()) LoginError.InvalidUsername("Baldomero")

        else LoginError.LoginCommonError(Forbidden)

    println(getErrorMessage(error))

}
```

Como vemos, para procesar la respuesta tenemos que anidar un nuevo `when` en el caso de que se trate de un error común, para poder determinar cuál ha sido en concreto.

Sin embargo, si definimos `LoginError` y `GetUserError` como _sealed interfaces_, podemos hacer que `CommonError` implemente ambas interfaces. De esta manera procesar el error se vuelve más legible, ya que hemos aplanado la jerarquía de errores para todos los casos, gracias a que al ser _sealed interfaces_ en vez de _sealed classes_, una clase puede implementar varias de ellas:
**Ejemplo de sealed interfaces implementadas por una sealed class**

```kotlin
import kotlin.random.Random
sealed class CommonError : LoginError, GetUserError
object ServerError : CommonError()
object Forbidden : CommonError()
object Unauthorized : CommonError()
sealed interface LoginError {
    data class InvalidUsername(val username: String) : LoginError
    object InvalidPasswordFormat : LoginError
}
sealed interface GetUserError {
    data class UserNotFound(val userId: String) : GetUserError
    data class InvalidUserId(val userId: String) : GetUserError
}
fun getErrorMessage(loginError: LoginError): String = when (loginError) {
    is LoginError.InvalidUsername -> "Invalid username"
    LoginError.InvalidPasswordFormat -> "Invalid password format"
    Forbidden -> "Forbidden"
    ServerError -> "Server error"
    Unauthorized -> "Unauthorized"
}
fun main() {
    val error: LoginError =
        if (Random.nextBoolean()) LoginError.InvalidUsername("Baldomero")
        else Forbidden
    println(getErrorMessage(error))
}
```

Por otra parte, **si el tipo sellado necesita contener estado, entonces debemos usar una _sealed class_, ya que las interfaces no pueden contener estado**.

## Inline value classes

En muchas ocasiones definimos variables y parámetros de tipos básicos genéricos cuando en realidad sería más adecuado definir tipos más específicos. Por ejemplo, para una variable o parámetro correspondiente a la anchura se suele usar el tipo `Int`. Sin embargo no todos los valores posibles de un `Int` suponen una anchura válida. Así el valor `-1` es un entero válido, pero no es un anchura válida. Como consecuencia de ello, tendremos que validar desde código el valor recibido como anchura, para evitar que sea negativo. Incluso es posible que tengamos que validar dicho valor en varias partes de nuestro código.

Una alternativa para ello sería crear nuestro propio tipo `Width` para representar una anchura, mediante, por ejemplo, una clase o una _data class_, que internamente use una propiedad de tipo `Int` para almacenar el valor, pero que en la instanciación compruebe que el valor proporcionado es válido. Este tipo de clases que "envuelven" otra clase reciben el nombre de _wrapper_ (envoltura).

**Clase `Width`**

```kotlin
class Width(val value: Int) {
    init {
        require(value >= 0)
    }
}

fun main() {
    val width = Width(5)
    println(width.value)
}
```
El problema de esta opción es la sobrecarga en memoria en el _heap_ que supone crear objetos, cuando en realidad se podría usar un tipo básico, ya que los tipos considerados "primitivos" son optimizados en tiempo de ejecución.

Para resolver estos inconvenientes, Kotlin permite crear lo que se conoce como **_inline value class_**, que es una **clase que envuelve una única propiedad inmutable**, normalmente de un tipo básico, que debe ser **inicializada en el constructor primario**, y cuya característica principal es que **durante la compilación**, siempre que es posible, **las instancias de dicha clase son reemplazadas por dicha propiedad**, de manera que a efecto de _bytecode_ se usa en realidad el tipo de la propiedad de la _value class_.

Este es el motivo por el que se denominan _inline_ (en línea), porque la propiedad sustituye en línea al uso de los objetos de la clase. En cierta manera este funcionamiento es similar al _unboxing_ que se produce cuando un `Int` internamente es representado como un `int` primitivo cuando es posible.

De esta manera, una _inline value class_ **nos proporciona la seguridad de tipos asociada al uso de tipos específico, sin que ello suponga una sobrecarga en memoria en el _heap_ por creación de objetos**.

Para definir una _inline value class_ se usa la palabra reservada `value` delante de `class` y debemos usar la anotación `@JvmInline`. Por ejemplo:

**Width y Height como inline value classes**

```kotlin
@JvmInline
value class Width(val value: Int) {
    init {
        require(value >= 0)
    }
}

@JvmInline
value class Height(val value: Int) {
    init {
        require(value >= 0)
    }
}

class Rectangle(val width: Width, val height: Height) {
    val area: Int
        get() = width.value * height.value
}

fun main() {
    val width = Width(10)
    val height = Height(5)
    val rectangle = Rectangle(width, height)

    println("Width: ${rectangle.width.value}")
    println("Height: ${rectangle.height.value}")
    println("Area: ${rectangle.area}")
}
```

En el ejemplo anterior, hacemos que la validación de la anchura se deba realizar cuando se construye un `Width`, y no cuando se crea el rectángulo, o en cualquier otro método o función que reciba un `Width`.

Internamente, el Kotlin compiler genera un método estático factoría especial que maneja la lógica de construcción de la value class. Este método estático recibe un nombre modificado para ser único (_mangled_), contendrá la lógica del constructor primario y el bloque init que hayamos definido en la value class, y simplemente devolverá el valor subyacente (por ejemplo un `Int` en el caso de `Width`).

En el código cliente que llama al constructor de la value class, el compilador de Kotlin sustituye internamente esa llamada por una llamada al método estático creado, que simula la construcción y el comportamiento del init y la asignación del valor.

Las validaciones o cualquier otra lógica en el bloque init se integran directamente en este método de construcción. Esto significa que la validación ocurre en el momento de la creación de la "instancia" lógica de la value class.

Otra ventaja del uso de _inline value classes_ es que **evitan errores causados por accidentalmente intercambias valores incompatibles del mismo tipo**. Así, si en el ejemplo anterior el constructor de la clase `Rectangle` recibiera dos enteros, uno para la anchura y otro para altura, aumentamos la posibilidad de que se intercambien los valores deseados al llamar al constructor. Si en su lugar usamos `Width` y `Height`, el llamador debe pasar objetos de esas clases, reduciendo la posibilidad de error, al ser clases distintas.

El **inconviente** principal de las _inline value classes_ es **tener en nuestro código que explícitamente acceder a su propiedad para acceder al valor** que envuelve, como en el ejemplo anterior, que tenemos que acceder a `width.value`.

Sin embargo, debemos tener en cuenta que el método `toString()` de una inline value class en Kotlin retorna la representación `toString()` de su valor subyacente, por lo que cuando se quiere acceder al valor para simplemente mostrarlo pasándolo a cadena, no sería necesario acceder a la propiedad `value`, sino que podríamos usar el propio objeto.

Para mitigar el tener que estar accediendo a la propiedad `value`, podemos sobrescribir en la inline value class los operadores que queramos usar con objetos de dicha clase, como por ejemplo el operador `plus()`.

Además, podemos sobrescribir el método `toString()`para que muestre el valor subyacente, ya que la implementación por defecto retorna una cadena con el formato "ClassName(value)", por ejemplo `Width(5)`.

No se recomienda sobrecargar los operadores de comparación ni de igualdad con el tipo subyacente, ya que el objetivo principal de las inline value classes es diferenciarlas del tipo subyacente principalmente en lo relativo a la igualdad.

Width como inline value class con operadores sobrescritos

```kotlin
@JvmInline

value class Width(val value: Int) {

    init {

        require(value >= 0)

    }

    override fun toString(): String {

        return value.toString()

    }

    operator fun plus(other: Width): Width = Width(value + other.value)

    operator fun plus(other: Int): Width = Width(value + other)

}
```

```kotlin
@JvmInline

value class Height(val value: Int) {

    init {

        require(value >= 0)

    }

    override fun toString(): String {

        return value.toString()

    }

    operator fun plus(other: Height): Height = Height(value + other.value)

    operator fun plus(other: Int): Height = Height(value + other)

}

class Rectangle(val width: Width, val height: Height) {

    val area: Int

        get() = width.value * height.value

}

fun main() {

    val rectangle1 = Rectangle(Width(10), Height(5))

    val rectangle2 = Rectangle(Width(2), Height(3))

    val rectangle3 = Rectangle(rectangle1.width + rectangle2.width, rectangle1.height + 8)

    println("Rectangle3 Width: ${rectangle3.width.value}")

    println("Rectangle3 Height: ${rectangle3.height.value}")

    println("Rectangle3 Area: ${rectangle3.area}")    

}
```

Las _inline value classes_ tan solo permiten algunas de las opciones de una clase normal:

- NO puede heredarse de ellas.
- Pueden tener métodos y propiedades (aparte de la que representa el valor), pero dichas propiedades deben ser calculadas y NO pueden tener _backing field_, ni puede ser delegadas ni definidas como `lateinit`. Internamente se implementan como métodos estáticos.
- NO pueden heredar de otras clases.
- Pueden implementar interfaces. Puede usarse delegación en la implementación.
- Pueden tener bloques `init`, y desde la versión 1.9 de Kotlin, también constructores secundarios. Estos elementos son útiles para validar el valor de la propiedad principal.
- NO se puede comprobar la igualdad referencial (`===`) de dos instancias de la clase.
- Pueden tener párametros de tipo como tipo de la propiedad principal, en cuyo caso el compilador lo transforma en el _upper bound_ del tipo del parámetro de tipo.

En el código generado, el compilador de Kotlin crea una clase _wrapper_ para cada _inline value class_. Siempre que es posible, las instancias de dicha clase son representadas en tiempo de ejecución por el tipo de la propiedad principal de la clase inline, pero cuando no es posible, se usa una instancia de clase _wrapper_ que se ha creado para ella, como por ejemplo cuando se usa con genéricos, en la forma de tipo nullable, o como implementación de una interfaz.

Debemos tener en cuenta que definir una _inline value class_ NO es lo mismo que definir un _typealias_, ya una instancia de una _inline value class_ **NO se puede asignar a una variable del tipo de su propiedad principal** (el compilador no lo permite), mientras que en el caso de un _typealias_ sí es posible, ya que se tratan simplemente de dos nombres distintos para el mismo tipo.
