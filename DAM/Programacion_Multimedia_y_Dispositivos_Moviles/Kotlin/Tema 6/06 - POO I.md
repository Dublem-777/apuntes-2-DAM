---
asignatura: PMDM
tema: 6
tipo: tema
estado: completo
fecha: 2026-09-30
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-poo
---

# 06 · Programación Orientada a Objetos I

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 6 · Kotlin
> Ejercicios resueltos: [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1]]

## Índice del tema

- [[#1. Clases]]
- [[#2. Constructor primario y bloques de inicialización]]
- [[#3. Instanciación]]
- [[#4. Constructores secundarios]]
- [[#5. Propiedades]]
- [[#6. Getters y setters personalizados]]
- [[#7. Propiedades calculadas]]
- [[#8. Campo de respaldo]]
- [[#9. Campos de respaldo explícitos]]
- [[#10. Propiedades de respaldo]]
- [[#11. Herencia]]
- [[#12. Sobrescribir métodos y propiedades]]
- [[#13. Clases anidadas]]
- [[#14. Clases internas]]
- [[#15. Modificadores de visibilidad]]
- [[#16. Declaraciones de objetos]]
- [[#17. Objetos compañeros]]

---

## 1. Clases

Las **clases** en Kotlin se declaran usando la palabra clave `class` con la sintaxis `class NombreDeClase([parámetros]) { cuerpo }`, donde el encabezado y el cuerpo son opcionales, y el cuerpo viene delimitado por un par de llaves. Así, la definición mínima de una clase sería:

Definición de una clase


|   |
|---|
|`class Person`|

Como vemos en el ejemplo anterior, **no es obligatorio definir un constructor primario**, en cuyo caso Kotlin definirá internamente un constructor primario sin parámetros para nosotros (si no se trata de una clase abstracta).

## 2. Constructor primario y bloques de inicialización

Una clase en Kotlin puede tener un **constructor primario**, que **forma parte de la cabecera de la clase**. Dicho constructor primario recibirá como parámetros los argumentos con los que se quiere construir un objeto de dicha clase:

Constructor primario


|   |
|---|
|`class Person constructor(firstName: String) {     // ... }`|

Si el constructor principal no tiene ninguna anotación o modificadores de visibilidad, podemos omitir la palabra clave `constructor`, quedando el ejemplo anterior de la siguiente manera:

Omisión de constructor en el constructor primario


|   |
|---|
|`class Person(firstName: String) {     // ... }`|

Un aspecto importante es que **el constructor primario no puede contener ningún código**. Si queremos añadir un determinado código de inicialización podemos definir dentro del cuerpo de la clase uno o más **bloques inicializadores**, para lo que usa la palabra reservada `init`.

Bloque init

```kotlin
class Person(firstName: String) {
    val firstName: String
    init {
        this.firstName = firstName
        println("${firstName} created")
    }
}
```

Ten en cuenta que **los parámetros del constructor primario se pueden utilizar tanto en los bloques de inicialización como en la inicialización de los campos (_fields_) definidos dentro del cuerpo de la clase**. Así, el ejemplo anterior puede acortarse de la siguiente manera:

Inicialización con argumentos del constructor primario

```kotlin
class Person(firstName: String) {
    val firstName: String = firstName
    init {
        println("${firstName} created")
    }
}
```

Durante el proceso creación de la instancia se sigue el siguiente orden:

1. Primero se asignarán a los parámetros del constructor primario los valores correspondientes a los argumentos suministrados durante la instanciación.
2. Posteriormente se procederá a ejecutar las operaciones de inicialización que aparezcan dentro del cuerpo de la clase, lo que incluye la inicialización de los campos que se hayan especificado y los bloques de inicialización que se hayan definido.
3. Estas operaciones de inicialización se ejecutarán en el orden estricto en el que aparezcan dentro del cuerpo de la clase.

Orden de ejecución en la construcción

```kotlin
class InitOrderDemo(message: String) {
    val firstProperty = message
    init {
        println("First initializer block that prints ${firstProperty}")
    }
    val secondProperty = "Second property: ${message.length}".also(::println)
    init {
        println("Second initializer block that prints ${message.length}")
    }
}
```

Así, en el ejemplo anterior, si hacemos `InitOrderDemo("hello")`, primero se asignará el valor `"hello"` , suministrado durante la instanciación, al parámetro `name`, después se procederá a inicializar el campo `firstProperty`, después se ejecutará el primer bloque de inicialización, después se procederá a inicializar el campo `secondProperty` y finalmente se ejecutará el segundo bloque de inicialización.

Para evitarnos tener que definir un campo en el cuerpo de la clase cuyo valor inicial corresponda a un parámetro del constructor primario, Kotlin nos proporciona una **sintaxis más concisa, consistente en incluir la definición del campo dentro del propio constructor primario**, sustituyendo al parámetro:

Definición de campos en el constructor primario

```kotlin
class Person(
    val firstName: String,
    val lastName: String,
    var age: Int,
)
fun main() {
    val person = Person("Baldomero", "Llégate Ligero", 45)
    println("${person.firstName} ${person.lastName} tiene ${person.age} años")
}
```

En el ejemplo anterior se define el campo `firstName`, cuyo valor inicial corresponderá al argumento suministrado durante la instanciación, sin que tengamos que hacerlo explícitamente.

**Los campos declarados en el constructor principal pueden corresponder a referencias mutables**, indicándolo con la palabra reservada `var`, **o a referencias inmutables**, indicándolo con la palabra reservada `val`.

Aviso

**Si el constructor tiene anotaciones o modificadores de visibilidad, es obligatorio indicar la palabra reservada `constructor` a la hora de especificar el constructor primario**, precedido por las anotaciones o modificador de visibilidad correspondiente:

Debemos usar constructor al indicar modificador de visibilidad

```kotlin
// Al usar el modificador de visibilidad protected en el constructor
// no podemos omitir la palabra reservada constructor.
open class Person protected constructor(
    val firstName: String,
    val lastName: String,
    var age: Int
)
class Employee(
    firstName: String,
    lastName: String,
    age: Int,
    val salary: Double) : Person(firstName, lastName, age)
fun main() {
    val employee = Employee("Baldomero", "Llégate Ligero", 45, 2000.0)
    println("${employee.firstName} ${employee.lastName} tiene ${employee.age} años")
}
```

Vídeo

[Explicación en video](https://www.youtube.com/embed/5yyQjfsQwMI)

## 3. Instanciación

Para crear una instancia de una clase, llamamos al constructor como si fuera una función regular:

Instanciación


|   |
|---|
|`val person = Person("Baldomero", "Llégate Ligero", 45)`|

Aviso

Kotlin **no tiene la palabra reservada `new`**.

Vídeo

[Explicación en video](https://www.youtube.com/embed/3Y9pJD_Trv4)

## 4. Constructores secundarios

La clase también puede declarar **constructores secundarios** dentro de su cuerpo, para lo que se usará la palabra reservada `constructor`.

Constructor secundario

```kotlin
class Person {
    val name: String
    constructor(name: String) {
        this.name = name
    }
}
fun main() {
    val person = Person("Baldomero")
    println(person.name)
}
```

**Si la clase tiene definido un constructor primario, entonces cada constructor secundario necesita delegar la construcción del objeto al constructor principal** (llamarlo), ya sea directa o indirectamente (a través de otro constructor secundario). Dicha delegación se lleva a cabo usando `this()` de la siguiente manera:

Constructor secundario debe llamar al primario

```kotlin
class Person(val firstName: String) {
    var fullTime: Boolean = true
    // Se delega la construcción del objeto al constructor primario.
    constructor(firstName: String, fullTime: Boolean) : this(firstName) {
        this.fullTime = fullTime
    }
}
fun main() {
    val person = Person("Baldomero")
    println("${person.firstName} does ${if (person.fullTime) "" else "not "}work full time")
}
```

Otro aspecto importante es que **los constructores secundarios no pueden definir propiedades**, es decir, que no podemos usar las palabras reservadas `val` y `var` en la definición de sus parámetros. Las propiedades solo pueden declararse en el constructor primario o en el cuerpo de la clase, no en la lista de parámetros de un constructor secundario. Así, en el ejemplo anterior, la propiedad `fullTime` debe declararse explícitamente en el cuerpo de la clase.

En Java, el uso más frecuente de los constructores secundarios es proporcionar argumentos a propiedades que son opcionales. Sin embargo, en Kotlin no será necesario, ya que **es posible indicar los valores por defecto para las propiedades en el constructor primario**. Así, el ejemplo anterior podría quedar como:

Argumentos por defecto en constructor primario

```kotlin
class Person(val firstName: String, val fullTime: Boolean = true) {
    // No es necesario definir constructores secundarios para
    // propiedades opcionales.
    // ...
}
fun main() {
    val person = Person("Baldomero")
    println("${person.firstName} does ${if (person.fullTime) "" else "not "}work full time")
}
```

**Si todos los parámetros del constructor primario tienen valores por defecto, el compilador generará un constructor adicional sin parámetros que utilizará los valores por defecto**. Esto hace que sea más sencillo usar Kotlin con librerías que instancian clases a través de constructores sin parámetros.

Constructor primario con todos los parámetros con argumento por defecto

```kotlin
class Person(val firstName: String = "Desconocido") {
    // ...
}
fun main() {
    val person = Person()
    println(person.firstName)
}
```

Debemos tener en cuenta que **el código incluido dentro del constructor secundario se ejecutará después de ejecutar el constructor primario y después de ejecutar los bloques de inicialización e inicialización de propiedades (en el orden en el que aparezcan)**. Incluso si la clase no tiene un constructor primario, los bloques de inicialización y la inicialización de propiedades se ejecutarán antes que el código del constructor secundario.

Vídeo

[Explicación en video](https://www.youtube.com/embed/3rEVnbNCzTA)

## 5. Propiedades

En Java, los datos gestionados por un objeto son almacenados en campos (_fields_). En base al concepto de **encapsulación**, los campos no deben ser accedidos directamente desde fuera de la clase, porque en ese caso perdemos el control sobre su estado. En vez de eso, los campos se suelen definir como privados, y su acceso debe realizarse a través de un par de métodos conocidos como **métodos de acceso** (_accessor methods_).

Así, para permitir el acceso a un determinado dato desde fuera del código de la clase, se crea en ella un **método _getter_** y, opcionalmente, un **método _setter_** que, respectivamente, lea y escriba el dato. El método _setter_ puede contener lógica adicional de validación del valor que se quiere escribir en el campo.

Aunque el conjunto de campo privado, _getter_ y _setter_ consigue la encapsulación, suele suponer la escritura de mucho código _boilerplate_ en la clase.

Para evitar este código _boilerplate_ Kotlin incorpora el concepto de **propiedad** (_property_), evitándonos la necesidad de definir por un lado el campo y por otro sus métodos de acceso.

Así, una propiedad es una variable definida dentro de una clase que es encapsulada automáticamente. En Kotlin, **todas las variables definidas dentro de una clase son propiedades**, no simplemente campos, como ocurre en Java.

Propiedad

A la combinación de un campo y de sus métodos de acceso se le conoce como propiedad.

Algunos lenguajes, como JavaScript tienen soporte integrado para propiedades, pero en el caso de Java no es así. Así que en Kotlin/JVM, **los métodos de acceso por defecto deben ser generados automáticamente para cada propiedad**, esto es, un _getter_ para una propiedad de solo lectura y un _getter_ y un _setter_ para una propiedad de lectura y escritura.

Así, una propiedad se declara de la misma manera que una variable: **con la palabra reservada `val` si queremos crear una referencia inmutable, o con `var` si queremos que la referencia sea mutable**, y por tanto pueda referenciar a otro objeto más adelante. Por ejemplo:

Definición de propiedades

```kotlin
class Person(
    val name: String,
    var isMarried: Boolean
) {
    var fullTime: Boolean = true
}
fun main() {
    val person = Person("Baldomero", true)
    person.isMarried = false
    person.fullTime = false
    println("${person.name} is ${if (person.isMarried) "" else "not "}married and does ${if (person.fullTime) "" else "not "}work full time")
}
```

Básicamente, cuando declaramos una propiedad como las anteriores, **internamente se crea un campo, conocido como _backing field_** en el que almacenar el valor, pero también se están declarando los correspondientes métodos de acceso.

**En el caso de una propiedad declarada con `val` se creará internamente un método _getter_. Para una propiedad declarada con `var` además se creará un _setter_.**

La **implementación por defecto** de dichos métodos de acceso es trivial: **el método _getter_ simplemente retornará el valor del campo y el método _setter_ tan solo establecerá un nuevo valor en el campo**.

**Para usar una propiedad de un objeto desde fuera de la clase simplemente usaremos su nombre a continuación de operador punto**, como si se trata de un campo público de una clase Java, aunque en realidad internamente se estará llamando al método _getter_ o _setter_ correspondiente, que por defecto son públicos. Por ejemplo:

Acceso a propiedades

```kotlin
val person = Person("Baldomero", true)
person.isMarried = false
person.fullTime = false
println("Name: ${person.name}, Married: ${person.isMarried}, FullTime: ${person.fullTime}")
```

Sugerencia

**Kotlin permite incluso usar la sintaxis de propiedad para acceder a propiedades de clases definidas en Java**. Por ejemplo si una clase Java define los métodos de acceso `getName()` y `setName()`, podremos acceder a ellos a través de una propiedad `name`, y si define los métodos `isMarried()` y `setMarried()`, podremos usar la propiedad `isMarried` desde código Kotlin.

Vídeo

[Explicación en video](https://www.youtube.com/embed/2d-I7h8wF0U)

## 6. Getters y setters personalizados

Como hemos comentado, Kotlin nos proporciona una implementación por defecto trivial para los métodos _getter_ y _setter_ de las propiedades.

Sin embargo, Kotlin nos proporciona una sintaxis específica para **poder crear nuestra propia implementación personalizada del _getter _y del_ setter_**.

Gracias a esta personalización seremos capaces de, por ejemplo, lanzar una excepción en el _setter_ si el valor que nos han pasado no tiene sentido para la propiedad, o modificar el acceso a nuestro _getter_ o _setter_ para que sea privado y por tanto no pueda usarse desde fuera de la clase, entre otras.

Debemos tener en cuenta la sintaxis que debemos emplear para personalizar el _getter_ y el _setter_ de una propiedad NO puede usarse si dicha propiedad está definida en el constructor primario de la clase. Por tanto, **si queremos personalizar el _getter_ o el _setter_ de la propiedad estamos obligados a definir la propiedad en el cuerpo de la clase**.

La sintaxis completa de la declaración de una propiedad es la siguiente:

Sintaxis de definición de una propiedad en el cuerpo de la clase

|   |
|---|
|`val\|var identificador[: <Tipo>] [= valor_inicial]     [[modif_acceso] get[() { }]]    [[modif_acceso] set[(value) { }]] // Solo si la prop es var`|

En la sintaxis anterior los corchetes hacen referencia a que su contenido es opcional. Así, vemos que el tipo de la propiedad es opcional, si se puede inferir del valor inicial o del valor de retorno del _getter_ personalizado.

Cuando definimos un _getter_ personalizado, podemos usar una sintaxis de expresión única, o un body con llaves y una instrucción `return`.

**Un _getter_ personalizado debe respetar la visibilidad y el tipo de la propiedad.** Puede lanzar excepciones, aunque conviene reservarlas para errores excepcionales. Evita cálculos costosos: el _getter_ se ejecuta cada vez que se consulta la propiedad. Por ejemplo, el siguiente código da un error de compilación:

El getter personalizado debe tener la misma visibilidad que la propia propiedad

```kotlin
class Worker(val name: String, initialSalary: Float) {
    // ERROR DE COMPILACIÓN: Getter debe tener la misma visibilidad que la propiedad
    var salary: Float = initialSalary
        private get
}
fun main()  {
    val worker = Worker("Baldomero", 1000f)
}
```

En este caso la solución consiste en definir la propia propiedad como privada, en cuyo caso no es necesario definir un getter personalizado:

Propiedad privada

```kotlin
class Worker(val name: String, initialSalary: Float) {
    private var salary: Float = initialSalary
}
fun main()  {
    val worker = Worker("Baldomero", 1000f)
}
```

Debemos fijarnos también en que **solo debemos especificar un _setter_ personalizado si la propiedad ha sido definida usando `var`**, ya que no tienen sentido en el caso de propiedades `val`, que son de referencia inmutable. Si lo hiciéramos no se generaría el setter, aunque no daría un error de compilación.

**El _setter_ puede tener una visibilidad más restringida que el definido para la propiedad, pero nunca una visibilidad más amplia**. Por ejemplo podemos tener un _setter_ privado para una propiedad pública, pero no podemos tener un setter público para una propiedad privada.

El setter personalizado no puede tener mayor visibilidad que la propia propiedad

```kotlin
class Worker(val name: String, initialSalary: Float) {
    // ERROR DE COMPILACIÓN: Setter debe tener la misma o menor visibilidad que la propiedad
    private var salary: Float = initialSalary
        public set
}
fun main()  {
    val worker = Worker("Baldomero", 1000f)
}
```

El cuerpo del _getter_ o del _setter_ es opcional, en cuyo caso se usará la implementación por defecto. Normalmente cuando omitimos el cuerpo del _getter_ o del _setter_ es porque habremos especificado un modificador de acceso para cambiar el nivel de acceso a la implementación por defecto del mismo.

Así, en el siguiente ejemplo hacemos que el salario de un trabajador no pueda ser modificado desde fuera de la propia clase, aunque se usará la implementación por defecto del _setter_:

Propiedad con setter privado

```kotlin
class Worker(val name: String, initialSalary: Float) {
    var salary: Float = initialSalary
        private set
    fun updateSalary(factor: Float) {
        salary *= factor
    }
    // ...
}
fun main()  {
    val worker = Worker("Baldomero", 1000f)
    worker.updateSalary(1.1f)
    println("Salario: ${worker.salary}")
    // ERROR DE COMPILACIÓN: salary es privada
    worker.salary = 2000f
}
```

En el código anterior el salario inicial es pasado como argumento al constructor de la clase, pero `initialSalary` no es una propiedad, ya que no lo hemos definido con `val` o `var`.

El setter tiene visibilidad privada, por lo que solo puede usarse desde dentro de la clase. En código JVM, los detalles de generación y optimización de los accesores dependen del compilador.

**El _getter_ de una propiedad debe retornar un valor del tipo de la propiedad**, no puede ser de un tipo distinto. Cada vez que queramos acceder al valor de la propiedad se ejecutará el _getter_ correspondiente.

Por su parte, el _setter_, si posee cuerpo, recibirá un valor del tipo de la propiedad, al que normalmente llamaremos `value`, aunque no es estrictamente necesario.

Toda asignación a una propiedad `var` mediante su accesor ejecuta el _setter_ personalizado. **La inicialización directa de la propiedad en su declaración asigna el valor al campo de respaldo (_field_) sin ejecutar el setter**. El motivo es que en el momento de la construcción, el objeto está en un estado parcialmente inicializado. Si el setter intentara acceder a otras propiedades que aún no han recibido su valor, la aplicación podría fallar. Para evitar este riesgo, Kotlin asegura una inicialización más simple y directa.

Propiedad con setter personalizado

```kotlin
class Rectangle(width: Double, height: Double) {
    // Los setters solo se activan al modificar, no al crear
    var width: Double = width
        set(value) {
            require(value >= 0) { "El ancho no puede ser negativo" }
            field = value
        }
    var height: Double = height
        set(value) {
            require(value >= 0) { "La altura no puede ser negativa" }
            field = value
        }
    override fun toString(): String {
        return "Rectángulo(ancho=$width, altura=$height)"
    }
}
fun main() {
    // Esta línea funciona y crea un objeto en estado inválido
    val r = Rectangle(-10.0, 50.0)
    println("Objeto creado con éxito: $r") // Imprime: Rectángulo(ancho=-10.0, altura=50.0)
    // El setter sí falla si intentamos asignarle un valor negativo
    try {
        r.width = -5.0
    } catch (e: IllegalArgumentException) {
        println("Error al modificar: ${e.message}")
    }
}
```

Por tanto, para que una clase sea verdaderamente robusta, debemos combinar dos mecanismos de validación, uno en el bloque `init` y otro en el _setter_:

Propiedad con setter personalizado

```kotlin
class Rectangle(width: Double, height: Double) {
    // Los setters solo se activan al modificar, no al crear
    var width: Double = width
        set(value) {
            require(value >= 0) { "El ancho no puede ser negativo" }
            field = value
        }
    var height: Double = height
        set(value) {
            require(value >= 0) { "La altura no puede ser negativa" }
            field = value
        }
    init {
        require(width >= 0) { "El ancho no puede ser negativo" }
        require(height >= 0) { "La altura no puede ser negativa" }
    }
    override fun toString(): String {
        return "Rectángulo(ancho=$width, altura=$height)"
    }
}
fun main() {
    // Esta línea ahora lanza un error y crea un objeto en estado inválido
    val r = Rectangle(-10.0, 50.0)
    println("Objeto creado con éxito: $r") // Imprime: Rectángulo(ancho=-10.0, altura=50.0)
    // El setter también falla si intentamos asignarle un valor negativo
    r.width = -5.0
}
```

La inicialización de una propiedad en su declaración escribe directamente en el campo de respaldo y no ejecuta su _setter_. Por ello, valida los argumentos iniciales en `init` y usa el _setter_ para validar cambios posteriores. No hace falta reasignar las propiedades desde `init` para activar el _setter_.

```kotlin
class Rectangle(width: Double, height: Double) {
    var width: Double = width
        set(value) {
            require(value >= 0.0) { "El ancho no puede ser negativo" }
            field = value
        }

    var height: Double = height
        set(value) {
            require(value >= 0.0) { "La altura no puede ser negativa" }
            field = value
        }

    init {
        require(width >= 0.0) { "El ancho no puede ser negativo" }
        require(height >= 0.0) { "La altura no puede ser negativa" }
    }
}
```

El bloque `init` rechaza dimensiones inválidas desde la construcción; los _setters_ mantienen la misma regla ante modificaciones posteriores.

Vídeo

[Explicación en video](https://www.youtube.com/embed/ADXOoheUkd0)

## 7. Propiedades calculadas

Gracias a esta sintaxis podemos crear **propiedades que realmente no almacenan ningún valor, es decir que no tienen asociado ningún campo (_backing field_)**. A este tipo de propiedades se les conoce como _computed properties_ o **propiedades calculadas**.

Así, en el siguiente ejemplo vamos a definir una clase rectángulo que tiene dos propiedades definidas en su constructor, correspondientes a la anchura y la altura del rectángulo. Pero además definimos una propiedad calculada que nos indica si el rectángulo es cuadrado o no:

Definición de propiedad calculada

```kotlin
class Rectangle(val height: Int, val width: Int) {
    val isSquare
        get() = height == width
}
fun main() {
    val rectangle = Rectangle(4, 4)
    println("Is it a square? ${rectangle.isSquare}")
}
```

En el ejemplo anterior, las propiedades `height` y `width` son propiedades para las que se crea un campo (_backing field_) y cuyos métodos de acceso corresponden a la implementación por defecto.

Sin embargo, la propiedad `isSquare` corresponde a una propiedad calculada, para la que no se crea un campo, ya que su valor se calcula a partir de las propiedades `height` y `width` ejecutando el _getter_ correspondiente cada vez que tratemos de obtener su valor.

Además, en este caso, no se está indicando explícitamente el tipo de la propiedad, que se infiere a partir del tipo de retorno del getter.

El uso de una propiedad calculada es exactamente igual al de cualquier otra propiedad:

Sugerencia

Cabría preguntarse si no sería mejor simplemente definir un método en la clase que retornara si el rectángulo es un cuadrado o no. En realidad en términos de implementación o de rendimiento el resultado es exactamente el mismo. En algunos casos el uso de una propiedad calculada puede mejorar la legibilidad.

En general, el criterio que debe seguirse es definir una propiedad calculada si ésta realmente describe una característica de la entidad que la clase está modelando. En caso contrario, se recomienda definir un método en la clase.

**Las propiedades calculadas no tienen por qué ser únicamente de referencia inmutable**. En el siguiente ejemplo se define una propiedad calculada correspondiente a la representación en cadena de un rectángulo, en formato `{anchura}x{altura}`. Cuando se obtiene el valor de la propiedad se construye la cadena resultante a partir de la anchura y la altura. Cuando se establece el valor de la propiedad, en realidad no se almacena el valor, sino que se extraen los datos correspondientes a la anchura y altura y se almacenan en sus respectivas propiedades:

Propiedad calculada de referencia mutable

```kotlin
class Rectangle(var height: Int, var width: Int) {
    val isSquare
        get() = height == width
    var stringRepresentation: String
        get() = "${width}x${height}"
        set(value) {
            val values = value.split("x")
            width = values[0].toIntOrNull() ?: throw IllegalArgumentException("Correct format: {width}x{height}")
            height = values[1].toIntOrNull() ?: throw IllegalArgumentException("Correct format: {width}x{height}")
        }
}
fun main() {
    val rect = Rectangle(1, 2)
    rect.stringRepresentation = "3x3"
    displayRect(rect)
    rect.stringRepresentation = "3x4"
    displayRect(rect)
}
fun displayRect(rect: Rectangle) {
    println("Is it a square? ${if (rect.isSquare) "Yes" else "No"}. It's ${rect.stringRepresentation}")
}
```

No debemos confundir una _computed property_ con una propiedad normal cuyo valor inicial provenga del valor de otras propiedades, ya que en éste último caso la evaluación se realiza una única vez durante la instanciación, mientras que en el caso de una _computed property_ el _getter_ es ejecutado cada vez que se consulta el valor de la propiedad. Por ejemplo:

Propiedad calculada de referencia mutable

```kotlin
class User {
    var name: String = ""
    var surname: String = ""
    val fullName1: String
        get() = "$name $surname"
    val fullName2: String = "$name $surname"
}
fun main() {
    val user = User()
    user.name = "Baldo"
    user.surname = "Mero"
    println(user.fullName1) // Baldo Mero
    println(user.fullName2) // ""
    user.surname = "Merillo"
    println(user.fullName1) // Baldo Merillo
    println(user.fullName2) // ""
}
```

Vídeo

[Explicación en video](https://www.youtube.com/embed/9kpzyRkXtOQ)

## 8. Campo de respaldo

A diferencia de en Java, Kotlin no permite declarar campos en las clases, sino que tienen que se definidos como propiedades.

Sin embargo, para cada propiedad que deba almacenar un valor, Kotlin define internamente un campo, al que se conoce como _backing field_ (campo de respaldo).

**Si hemos creado un _getter_ o _setter_ personalizado para la propiedad y queremos referirnos al campo que se haya creado para ella deberemos usar la palabra reservada `field`**.

Cuidado

Si dentro del _getter_ o _setter_, en vez de usar la palabra reservada `field` usamos directamente el nombre del propiedad estaremos creando un bucle infinito.

Veamos un ejemplo en el que hacemos que no se pueda pasar un valor negativo para la altura o anchura del rectángulo:

Acceso al backing field desde setter personalizado

```kotlin
class Rectangle(height: Int, width: Int) {
    init {
        require (height >= 0 && width >= 0) {"Both sides must be a non negative number"}
    }
    var width = width
        set(value) {
            require(value >= 0) { "Must receive a non negative number" }
            field = value
        }
    var height = height
        set(value) {
            require(value >= 0) { "Must receive a non negative number" }
            field = value
        }
    val isSquare
        get() = height == width
}
fun main() {
    val rectangle = Rectangle(4, 4)
    println("Is it a square? ${rectangle.isSquare}")
    rectangle.width = -4
    println("Is it a square? ${rectangle.isSquare}")
}
```

En el ejemplo anterior, si se intenta asignar a la propiedad `height` o la propiedad `width` un valor no positivo se lanzará una excepción.

Kotlin creará un _backing field_ para una propiedad solamente cuando sea realmente necesario, es decir, cuando se use el getter o el setter por defecto, o el _getter_ o _setter_ personalizado haga uso de la palabra reservada `field`. En otro caso, no se creará el _backing field_.

Por ejemplo, para la propiedad `isSquare` de la clase anterior no se crea un _backing field_, ya que no almacena ningún valor. De hecho no cumple con ninguno de los criterios para que se le cree el _backing field_, ya que no usa la implementación por defecto del _getter_, la implementación personalizada no hace referencia a `field` y, dado que es una propiedad `val`, no puede tener _setter_.

**Las propiedades para las que se crea un _backing field_ deben ser inicializadas obligatoriamente durante la instanciación**, ya sea en el constructor primario, en la propia declaración de la propiedad, en un bloque de inicialización `init` o en un constructor secundario.

Vídeo

[Explicación en video](https://www.youtube.com/embed/oH5v3XQxgIU)

## 9. Campos de respaldo explícitos

Algunas versiones recientes del compilador ofrecen una sintaxis para declarar un campo de respaldo explícito y permitir que una propiedad publique un tipo más general que el campo usado internamente. Su disponibilidad depende de la versión y de las opciones del compilador; no debe asumirse como sintaxis portable.

> [!warning] Compatibilidad
> Antes de usar `field = ...`, comprueba que la versión de Kotlin del proyecto lo admite y si requiere habilitar una característica experimental. Para código portable, usa la propiedad de respaldo convencional de la sección siguiente.

El objetivo es exponer, por ejemplo, una vista `List<String>` de solo lectura y mantener internamente una colección mutable. La sintaxis explícita tiene restricciones: no admite un _getter_ personalizado, la propiedad debe ser `val`, no puede ser `open`, delegada ni constante, y el tipo del campo debe ser un subtipo del tipo público de la propiedad.

En apuntes y código que deban funcionar en distintas versiones, la propiedad de respaldo es la alternativa más compatible y clara.

## 10. Propiedades de respaldo

Algunas veces queremos exponer una propiedad de una manera diferente a como está definida y dicha forma no cabe dentro del esquema anterior de _backing field_. En esos casos no tenemos más remedio que definir dos propiedades, una propiedad privada que sea la que realmente almacene el valor, conocida como _backing property_ (propiedad de respaldo), y otra propiedad pública que es la que se incluye en la "interfaz" de la clase.

Sugerencia

Normalmente se hace que los identificadores de las _backing properties_ comiencen por el carácter `_`, de manera que el programador tenga pistas sobre que se trata de una propiedad privada que no pertenecerá a la interfaz de la clase.

En el ejemplo siguiente usamos esta técnica para no exponer el hecho de que la propiedad pueda ser `null`, así que tenemos dos propiedades, una privada, que puede ser nula y otra pública, que trabaja internamente con la privada, pero que no puede ser nula, y que lanzará un error si para cuando se accede a ella la propiedad privada es `null`:

Backing property

```kotlin
class MyClass {
    // Propiedad privada que puede ser nula (no accesible desde fuera)
    private var _table: Map<String, Int>? = null
    // Propiedad pública accesible desde fuera que no puede ser nula.
    val table: Map<String, Int>
        get() {
            if (_table == null) {
                _table = HashMap() // Los tipos son inferidos automáticamente.
            }
            return _table ?: throw AssertionError("Set to null by another thread")
        }
}
fun main() {
    val myClass = MyClass()
    // ERROR DE COMPILACIÓN: Propiedad _table no accesible desde fuera
    val table1: Map<String, Int>? = myClass._table
    val table2: Map<String, Int> = myClass.table
}
```

Ten en cuenta

El acceso a propiedades privadas es optimizado por el compilador para que internamente no se llamen a los _getter_ y _setter_, sino directamente al _backing field_, evitando la sobrecarga adicional de la llamada a estos métodos.

Vídeo

[Explicación en video](https://www.youtube.com/embed/9O-E1TLQOYo)

## 11. Herencia

Todas las clases en Kotlin heredan de la superclase raíz **`Any`**, que **es la superclase por defecto para una clase en cuya definición no hayamos indicado la clase de la que hereda**:

Herencia implícita de Any

```kotlin
// Hereda implícitamente de Any
class Example {
    // ...
}
fun main() {
    println("Example is an Any: ${Example() is Any}")
}
```

Ten en cuenta

La clase `Any` de Kotlin no es exactamente igual que la clase `Object` de Java, ya que sólo contiene los métodos `equals()`, `hashCode()` y `toString()`.

Podemos indicar explícitamente en la cabecera de la clase hija la clase padre de la que hereda de la siguiente manera.

Herencia explícita

```kotlin
// Con open hacemos que se pueda heredar de esta clase
open class Base(val propBase: Int) {
    // ...
}
// La clase Derived hereda de Base
// El constructor primario llama al constructor de la superclase
class Derived(propBase: Int, val propDerived: String) : Base(propBase) {
    // ...
}
fun main() {
    val derived = Derived(51, "Baldomero")
    println("${derived.propDerived} - ${derived.propBase}")
}
```

Aviso

Sólo se permite heredar de una única clase, **no se permite la herencia múltiple**.

Por defecto, todas las clases en Kotlin son finales, por lo que si queremos que se pueda heredar de dicha clase es necesario que lo indiquemos expresamente en su definición mediante la **palabra reservada `open`**, como se muestra en el ejemplo anterior.

Ten en cuenta

`open` es justamente lo contrario a la palabra reservada `final` de Java.

**Si la clase derivada tiene un constructor primario, a la hora de indicar la superclase se debe llamar al constructor de ésta**, pudiendo usar como argumentos los parámetros del constructor de la clase derivada.

Así, en el ejemplo anterior, a la hora de especificar que la clase `Derived` hereda de la clase `Base` se llama al constructor primario de ésta última usando el parámetro `p` del constructor primario de la clase `Derived`.

Vídeo

[Explicación en video](https://www.youtube.com/embed/MSttzwYggf4)

## 12. Sobrescribir métodos y propiedades

A diferencia de en Java, en Kotlin debemos indicar explícitamente que un determinado método de una clase puede ser sobrescrito en una clase que herede de ella. Para ello, **en la definición del método o propiedad usaremos la palabra reservada `open`**.

A la hora de sobrescribir un método de la clase base en una clase derivada usaremos la **palabra reservada `override`**:

Sobrescritura de métodos

```kotlin
// Debemos usar open en la clase para que se pueda extender.
open class Base {
    // Debemos usar open en el método para que pueda ser sobrescrito
    // en una clase hija.
    open fun v() {
        println("Método original de la clase padre")
    }
    fun nv() {
        System.out.println("Método no sobrecargado de la clase padre");
    }
}
class Derived() : Base() {
    // Debemos usar override para indicar que se está sobrescribiendo
    // un método heredado.
    override fun v() {
        println("Método sobrecargado en la clase hija")
    }
}
fun main() {
    var myVar: Base = Derived()
    myVar.v()
    myVar.nv()
    myVar = Base()
    myVar.v()
}
```

Aviso

A diferencia de en Java, en Kotlin es obligatorio usar la palabra reservada `override` para poder sobrescribir un método.

Los métodos que no sean definidos explícitamente con `open` en la clase base no podrán ser sobrescritos en una clase derivada. Por ejemplo el método `nv()` de clase `Base` del ejemplo anterior no puede ser sobrescrito. Si definimos un método como `open` en una clase que no se ha definido como `open` se producirá un error de compilación.

Otro aspecto importante es que **un método definido con `override` es a su vez, por defecto, `open`,** por lo que puede sobrescrito por subclases, siempre y cuando la clase también este indicada como `open`.

Si queremos evitar que un método `override` pueda a su vez se sobrescrito por una subclase, debemos usar la **palabra reservada `final`**:

Método final que no puede ser sobrescrito

```kotlin
// Debemos usar open en la clase para que se pueda extender.
open class Base {
    // Debemos usar open en el método para que pueda ser sobrescrito
    // en una clase hija.
    open fun v() {
        println("Método original de la clase padre")
    }
    fun nv() {
        System.out.println("Método no sobrecargado de la clase padre");
    }
}
open class Derived() : Base() {
    // Este método sobrescribe el método v() de la clase Base, pero no
    // podrá ser sobrescrito por subclases que hereden de AnotherDerived.
    final override fun v() {
        println("Método sobrecargado en la clase hija")
    }
}
class AnotherDerived() : Derived() {
    // NO PUEDE SOBRESCRIBIR el método v() de la clase Base, porque Derived
    // lo estableció como final
    override fun v() {
        println("Método sobrecargado en la clase nieta")
    }
}
fun main() {
    var myVar: Base = Derived()
    myVar.v()
    myVar.nv()
    myVar = Base()
    myVar.v()
    myVar = AnotherDerived()
    myVar.v()
}
```

Vídeo

[Explicación en video](https://www.youtube.com/embed/mjZqitNyKmM)

## 13. Clases anidadas

En Kotlin, **podemos definir clases dentro de clases, lo que se conoce como clase anidada**. Los motivos principales para definir una clase anidada tienen que ver con la organización y cohesión del código, o con la encapsulación y el ocultamiento.

Una clase anidada normal **no requiere una instancia de la clase externa** y no puede acceder directamente a las propiedades ni métodos de una instancia externa. Este es el comportamiento por defecto en Kotlin; para asociar la clase anidada a una instancia hay que declararla con `inner`.

Este tipo de clases podrían ser definidas perfectamente fuera de la clase externa, pero se define como clase anidada para mejorar la agrupación lógica de clases y evitar conflictos de nombres.

Veamos un ejemplo en el que dentro de `Project` definimos una clase anidada normal `Task`, sin el modificador `inner`. Para crear un objeto `Project.Task` no necesitamos crear antes un objeto `Project`. Podríamos perfectamente haber definido la clase `Task` fuera de la clase `Project`, entonces ¿por qué la hemos definido dentro de `Project`? Pues básicamente para afianzar la idea de que corresponde a una tarea de proyecto y no una tarea en general, y además conseguir que no haya conflicto de nombre con alguna otra clase que se pueda llamar `Task` con otro cometido.

Clase anidada normal, sin referencia a la clase externa

```kotlin
class Project(val name: String, val budget: Double) {
    // No lleva inner: no conserva una instancia de Project.
    class Task(val title: String, val status: String) {
        fun getTaskDetails(): String {
            return "Task: $title, Status: $status"
        }
    }
    fun createReport(): String {
        return "Project: $name, Budget: $budget"
    }
}
fun main() {
    // Crear una tarea (no es necesario disponer de un objeto Project)
    val task = Project.Task("Design Homepage", "Pending")
    println(task.getTaskDetails())
}
```

## 14. Clases internas

Las **clases internas (`inner`)** requieren una instancia de la clase externa y conservan una referencia a ella. A diferencia de las clases anidadas normales, una instancia `inner` queda asociada a una instancia concreta de la clase externa. Por este motivo, la clase interna tiene acceso directo a los métodos y propiedades de la instancia de la clase externa.

Este es el comportamiento por defecto de las clases anidadas en Java, pero en Kotlin, para que una clase anidada sea interna, debemos usar el modificador `inner` al definirla.

Clase anidada no estática

```kotlin
class Project(val name: String, val budget: Double) {
    // Clase interna con el modificador inner
    inner class Task(val title: String, val status: String) {
        fun getTaskDetails(): String {
            return "Task: $title, Status: $status"
        }
        // Método que accede a la propiedad de la clase externa
        fun getProjectBudget(): Double {
            return this@Project.budget
        }
    }
    fun createReport(): String {
        return "Project: $name, Budget: $budget"
    }
}
fun main() {
    val project = Project("Website Redesign", 15000.0)
    // Crear una tarea de ese objeto project
    val task = project.Task("Design Homepage", "Pending")
    println(task.getTaskDetails())
    println(task.getProjectBudget())
    println(project.createReport())
}
```

## 15. Modificadores de visibilidad

Cuando diseñamos nuestras clases, se considera una buena práctica hacer la visibilidad de las clases y elementos tan restrictiva como sea posible, para lo que usaremos los conocidos como **modificadores de visibilidad**.

Para los miembros de una clase (propiedades o métodos), tenemos los siguientes modificadores:

- `public`: Será visible allá donde la clase sea visible. Es el modificador de visibilidad por defecto.
- `private`: Será visible solo dentro de la clase.
- `protected`: Será visible dentro de la clase y de sus subclases.
- `internal`: Será visible desde cualquier archivo del mismo módulo de compilación.

Estos modificadores de visibilidad podemos aplicárselos tanto a las propiedades definidas en el contructor primario como a las definidas en el cuerpo de la clase. También podemos aplicárselos al constructor primario y a los métodos de la clase.

Para las funciones y propiedades _top-level_, tendremos los siguientes modificadores de visibilidad:

- `public`: Visible en todas partes. Es el modificador de visibilidad por defecto.
- `private`: Visible solo dentro del mismo archivo.
- `internal`: Visible dentro del mismo módulo.

Como norma general, si usamos un elemento solo en el mismo archivo o clase, debemos hacerlo `private`, para restringir al máximo el acceso al mismo.

En el caso de las propiedades, debemos tener en cuenta que, **por defecto, la visibilidad de su _getter_ y su _setter_ será la misma que la de la propiedad**, y que el _backing field_ siempre será privado. Por ejemplo, la siguiente propiedad es privada:

Propiedad privada

```kotlin
class View {
    private var isVisible: Boolean = true
    fun show() {
        isVisible = true
        println("View is visible")
    }
    fun hide() {
        isVisible = false
        println("View is invisible")
    }
}
fun main() {
    val view = View()
    view.hide()
    view.show()
    // ERROR DE COMPILACIÓN: La propiedad isVisible es privada para get y set
    println(view.isVisible)
    view.isVisible = false
}
```

De hecho **el _getter_ siempre deberá tener la misma visibilidad que la propiedad**, pero en el caso del _setter_ podemos modificarla especificando el modificador de visibilidad antes de la palabra clave `set`. Por ejemplo, podemos convertir en `private` el _setter_ de una propiedad con visibilidad `public`:

Setter privado para una propiedad pública

```kotlin
class View {
    var isVisible: Boolean = true
        private set
    fun show() {
        isVisible = true
        println("View is visible")
    }
    fun hide() {
        isVisible = false
    }
}
fun main() {
    val view = View()
    println(view.isVisible) // true
    view.hide()
    println(view.isVisible) // false
    // ERROR DE COMPILACIÓN: La propiedad isVisible es privada para set
    view.isVisible = true // ERROR
    view.show()
    println(view.isVisible)
}
```

Debemos tener en cuenta que un módulo no es lo mismo que un paquete. En Kotlin, **un módulo se define como un conjunto de archivos de código fuente de Kotlin que se compilan de forma conjunta como una unidad**. Por tanto un módulo puede corresponder, por ejemplo, a un _souce set_ de Gradle, un projecto Maven o un módulo de IntelliJ.

Los creadores de librerías utilizan el modificador `internal` para elementos que desean que sean visibles en su módulo, pero que no quieren exponer a los usuarios de la librería.

También es útil en proyectos multimódulo para limitar el acceso a dentro de un determinado módulo, de manera que no pueda ser accedido desde otros módulos (como sucedería si fueran `public`).

## 16. Declaraciones de objetos

El **patrón _Singleton_ (único)** es un patrón de diseño que se aplica cuando queramos que sólo sea posible crear un único objeto de una determinada clase. En Java, se implementa normalmente haciendo que el constructor de la clase sea privado, de manera que solo se pueda instanciar el objeto desde dentro de su propio código, proporcionando un método estático accesible desde fuera que crea o devuelve la instancia única cuando se solicita por primera vez.

Sin embargo, Kotlin simplifica este proceso enormemente mediante la sintaxis conocida como _object declaration_ (declaración de objeto), que **usa la palabra clave `object` en vez de `class`**:

Definición de un singleton con object

```kotlin
// Se define un singleton (objeto único de esa clase)
object DataProviderManager {
    // El singleton puede contener métodos.
    fun registerDataProvider(provider: String) {
        // ...
    }
    // También puede contener propiedades.
    val allDataProviders: Collection<String>
        get() = listOf("Baldomero", "Llégate Ligero")
}
fun main() {
    println(DataProviderManager.allDataProviders)
}
```

Al igual que la declaración de una variable o propiedad, la declaración de objeto NO es una expresión, es decir no devuelve ningún valor. En este caso es obligatorio especificar un nombre (identificador) para el _object_, a diferencia de como ocurre los las _anonymous object expresions_, que veremos más adelante.

En realidad una declaración de objeto es bastante similar a la declaración de una clase:

- Puede incluir declaración de propiedades, de métodos y bloques de inicialización.
- Puede heredar de otra clase e implementar interfaces.
- Puede estar incluida dentro de otra clase (como si de una clase anidada se tratase)

Sin embargo, **una declaración de objeto no puede contener ningún tipo de constructor, ni primario ni secundario**.

Además, **no podemos hacer que una clase herede de un _object_**.

Sugerencia

Si, atendiendo al diseño de la aplicación, el constructor necesita recibir algún parámetro, tendremos que declarar una clase normal en vez de una declaración de objecto, e implementar explícitamente el patrón _singleton_ en ella.

**Para obtener una referencia al objeto (_singleton_) que hemos definido tan sólo tenemos que usar el nombre del mismo**, en este caso `DataProviderManager`.

Acceso a un singleton definido con object


|   |
|---|
|`val manager = DataProviderManager`|

Una vez obtenida dicha referencia, podremos llamar a sus métodos y propiedades de la misma variable que para cualquier otra variable, es decir, a través del operador `.`. Normalmente es innecesario almacenar en una variable la referencia al _singleton_, ya que podremos acceder al objeto directamente. Por ejemplo:

Acceso a las propiedades de un singleton object


|   |
|---|
|`DataProviderManager.registerDataProvider(provider)`|

Ten en cuenta

La instancia de un `object` se inicializa la primera vez que se accede a ella. La inicialización está sincronizada, por lo que es segura frente a accesos simultáneos durante la creación.

Vídeo

[Explicación en video](https://www.youtube.com/embed/aJuF6RrBaq4)

## 17. Objetos compañeros

A diferencia de en Java, **las clases en Kotlin no pueden tener propiedades ni métodos estáticos**.

Aviso

Kotlin no define la palabra reservada `static`.

Como hemos visto, en algunas ocasiones podemos solventar esta carencia usando en su lugar propiedades o funciones de primer nivel (_top-level properties_ o _top-level functions_). Así, podemos representar un campo _public static_ de Java como una propiedad fuera de cualquier clase, y un método _public static_ como una función fuera de cualquier clase.

Sin embargo, **el uso de propiedades o funciones _top-level_ no es exactamente equivalente a los métodos estáticos de Java**, en primer lugar porque en Kotlin no están asociados con ningún nombre de clase y, en segundo lugar, **porque los métodos del primer nivel NO pueden acceder a los miembros privados de una clase**, como por ejemplo a un constructor privado, mientras que en Java los métodos estáticos definidos dentro de dicha clase sí que pueden hacerlo.

Aunque no tenemos elementos estáticos en Kotlin, **podemos simularlo declarando un `object` anidado dentro de la clase**. Al igual que ocurre con las clases anidadas, los `object` anidados son por defecto estáticos, lo que significa que no están asociados a un objeto o instancia de la clase externa, por lo que podremos acceder a los elementos del `object` sin una referencia a un objeto de la clase externa.

Acceso a un object definido dentro de una clase

```kotlin
class Boss {
    object Static {
        const val ALIAS = "boss"
        private var name = "Bruce Springsteen"
        fun showName() {
            println("The $ALIAS is $name")
        }
    }
}
fun main() {
    val alias = Boss.Static.ALIAS
    println(alias)
    Boss.Static.showName()
}
```

Como vemos, el uso no es tan adecuado como en el caso de los miembros estáticos en Java, pero podemos mejorarlo. **Si usamos la palabra reservada `companion` antes de la palabra `object` en la declaración del objeto, podremos acceder a las propiedades y métodos de dicho objeto simplemente especificando el nombre de la clase**. Además, al declarar el objeto como _companion object_ (objeto compañero), su identificador es opcional.

El objeto compañero recibe el nombre `Companion` si no se especifica otro. Kotlin permite acceder a sus miembros usando directamente el nombre de la clase; no son miembros estáticos de Java, aunque `@JvmStatic` puede generar miembros estáticos en bytecode JVM:

Companion object

```kotlin
class Boss {
    companion object {
        const val ALIAS = "boss"
        private var name = "Bruce Springsteen"
        fun showName() {
            println("The $ALIAS is $name")
        }
    }
}
fun main() {
    Boss.showName()
    // También podemos acceder así
    Boss.Companion.showName()
}
```

De esta manera, podemos acceder a los miembros del _companion object_ de una clase como si se tratasen de miembros estáticos de la clase, aunque en realidad corresponden a métodos de un objeto (_singleton_) definido dentro de ella.

Podemos incluir diferentes declaraciones de `object` dentro de una clase, pero sólo una ellas puede ser marcada como _companion object_.

Aunque con la definición de un _companion object_ podemos simular la funcionalidad de los miembros estáticos en Java, no son exactamente lo mismo. De hecho, un _companion object_ puede heredar de otra clase e implementar interfaces, algo que no es posible con los métodos estáticos de Java.

Ten en cuenta

En realidad un _companion object_ es más parecido a una variable estática de una clase anidada estática con constructor privado, como podemos apreciar en el código Java equivalente. Dicha clase anidada puede heredar de otra clase e implementar interfaces.

Vídeo

[Explicación en video](https://www.youtube.com/embed/eL7pr-VVp7U)

## Esquema resumen de conceptos clave

| Bloque | Conceptos | Idea clave |
| --- | --- | --- |
| Clases y construcción | Clases, constructores, `init` | Crear objetos válidos desde el momento de su construcción. |
| Propiedades | `val`, `var`, accesores, `field` | Encapsular estado y validar sus modificaciones. |
| Herencia | `open`, `override`, `super` | Reutilizar y especializar comportamiento. |
| Clases anidadas | Anidadas e `inner` | Elegir si una clase necesita una instancia externa. |
| Visibilidad | `public`, `private`, `protected`, `internal` | Limitar el acceso al ámbito necesario. |
| Objetos | `object`, `companion object` | Compartir una instancia o miembros asociados a una clase. |

## Relaciones

- Ejercicios del tema: [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1]]
- [[02 - Jerarquia de tipos]] — clases, tipos y relaciones de herencia.
- [[03 - Funciones]] — funciones miembro, parámetros y `vararg`.
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar el orden de inicialización de constructor primario, propiedades e `init`.
- [ ] Distinguir parámetro de constructor y propiedad declarada con `val` o `var`.
- [ ] Validar valores iniciales y cambios posteriores de una propiedad.
- [ ] Diferenciar propiedades calculadas y almacenadas.
- [ ] Explicar el propósito de `field` y de una propiedad de respaldo.
- [ ] Crear una subclase y sobrescribir un miembro abierto.
- [ ] Distinguir clases anidadas de clases `inner`.
- [ ] Aplicar los modificadores de visibilidad según su alcance.
- [ ] Diferenciar declaración `object` y `companion object`.
