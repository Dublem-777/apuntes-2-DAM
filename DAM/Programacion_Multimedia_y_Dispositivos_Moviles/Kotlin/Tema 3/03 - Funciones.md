---
asignatura: PMDM
tema: 3
tipo: tema
estado: completo
fecha: 2026-09-23
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-funciones
---

# 3 · Funciones en Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 3 · Kotlin
> Fuente original: `Documentos/Notas/Funciones.md`

## Índice del tema

- [[#1. Definición de funciones]]
- [[#2. Trailing comma]]
- [[#3. El tipo Unit]]
- [[#4. Los tipos Nothing y Nothing?]]
- [[#5. Funciones cuyo cuerpo es una única expresión]]
- [[#6. Sobrecarga de funciones]]
- [[#7. Argumentos por defecto]]
- [[#8. Argumentos con nombre]]
- [[#9. varargs]]
- [[#10. Spread operator]]
- [[#11. Notación infija (infix)]]

---

## 1. Definición de funciones

Se definen con la palabra reservada `fun`, seguida del nombre, la lista de parámetros entre paréntesis, el tipo de retorno (precedido de `:`) y el cuerpo:

```kotlin
fun doubleOf(x: Int): Int {
    return 2 * x
}
```

Cada parámetro sigue la sintaxis `nombreParam: tipo`, separados por coma, y **el tipo es obligatorio**:

```kotlin
fun multiply(value1: Int, value2: Int): Int {
    return value1 * value2
}
```

```kotlin
val theDouble = doubleOf(3)
val multiplication = multiply(3, 2)
```

> [!warning] Los parámetros son inmutables
> Dentro del cuerpo de la función los parámetros se tratan como variables de referencia **inmutables** (como `final` en Java): asignarles un valor produce error de compilación.

**Identificadores con backticks**: si el nombre quiere ser una palabra reservada o contener espacios, se rodea de \`\` (tanto en la definición como en la llamada). Uso habitual: funciones de test en lenguaje natural:

```kotlin
@Test
fun `should show error dialog when no items loaded`() {
    // ...
}
```

**Formato multilínea**: cuando la definición es demasiado larga, un parámetro por línea y la declaración entre líneas separadas:

```kotlin
fun veryLongFunction(
    param1: Param1Type,
    param2: Param2Type,
    param3: Param3Type
): ResultType {
    // body
}
```

---

## 2. Trailing comma

Desde Kotlin 1.4 se permite una **coma adicional al final** de la lista de parámetros de una declaración, de la lista de argumentos de una llamada, y en otros contextos (ramas del `when`, desestructuración…).

```kotlin
fun reformat(
    str: String,
    uppercaseFirstLetter: Boolean,
    wordSeparator: Char, // trailing comma
) {
    println("$str, $uppercaseFirstLetter, $wordSeparator")
}

fun main() {
    reformat(
        "Hola",
        true,
        'H', // trailing comma
    )
}
```

Ventajas:

- Facilita **añadir o reordenar** elementos sin tocar las comas de los demás.
- Especialmente útil con la sintaxis multilínea: se pueden intercambiar líneas de parámetros/argumentos fácilmente.
- En control de versiones (Git) **minimiza las líneas modificadas**: la línea del antiguo último elemento no cambia al añadir una nueva.

> [!warning] Aviso
> Hay desarrolladores totalmente en contra de esta notación: conviene **consensuar su uso con el equipo**.

---

## 3. El tipo Unit

En Kotlin **todas las funciones tienen tipo de retorno**, por lo que toda llamada a una función es una *expresión*. Si no se especifica el tipo de retorno, será `Unit`, y el valor retornado por defecto será el objeto `Unit`.

```kotlin
fun sayHelloTo(name: String) {
    println("Hello $name")
    // No es necesario hacer return Unit o simplemente return, aunque se puede hacer
}
```

- Función sin `return` ≡ función terminada en un `return` sin valor → retorna implícitamente el objeto `Unit`.
- No es necesario retornar `Unit` explícitamente ni declararlo.

> [!note] Unit ≠ void
> `void` en Java es sólo una palabra reservada que indica ausencia de retorno; `Unit` es realmente una **clase con una única instancia** (*singleton* — un `object` en Kotlin), usable como argumento de genéricos. En Java el equivalente sería la clase `Void` (no confundir con `void`).
> El nombre viene de los lenguajes funcionales: "sólo una instancia o unidad".
> `Unit` no ocupa un lugar especial en la jerarquía: hereda implícitamente de `Any`.

---

## 4. Los tipos Nothing y Nothing?

Hay funciones cuyo retorno no tiene sentido porque **nunca terminan satisfactoriamente**: bucles infinitos, funciones que terminan el programa o que siempre lanzan excepción. Para ellas existe el tipo `Nothing`:

```kotlin
// El tipo de retorno de la función es Nothing porque nunca retornará.
fun fail(message: String): Nothing {
    throw IllegalStateException(message)
}

fun main() {
    fail("Se ha producido un error")
}
```

- `Nothing` es un *empty type* (tipo vacío): **no contiene ningún valor** y no puede instanciarse. Sólo tiene sentido como tipo de retorno (o dentro del tipo de retorno de una función parametrizada).
- Es **subtipo de todos los tipos no nullables** → puede incluirse una expresión que retorna `Nothing` dentro de cualquier otra expresión.

`throw` es una expresión que retorna `Nothing`, así que cabe dentro de una expresión de tipo `Float`:

```kotlin
val glassesSold = 0
val orangesUsed = 2
val fruitPerGlass: Float =
    if (glassesSold > 0) orangesUsed.toFloat() / glassesSold
    else throw IllegalStateException()
```

`return` también es una expresión (a diferencia de Java, donde es una sentencia) que retorna `Nothing` → se puede incluir dentro de cualquier expresión:

```kotlin
fun generateReport(orangesUsed: Int, glassesSold: Int): String {
    val fruitPerGlass: Float =
        if (glassesSold > 0) orangesUsed.toFloat() / glassesSold
        else return "No glasses sold"
    return "Used $fruitPerGlass oranges per glass"
}

fun main() {
    println(generateReport(3, 2))
    println(generateReport(3, 0))
}
```

**Nothing?**: subtipo de todos los tipos nullables y supertipo de `Nothing`. Es el tipo de la referencia nula `null`, lo que permite asignar `null` a cualquier tipo nullable.

> [!note] La referencia nula
> La referencia especial que representa `null` se denomina *referencia nula*: no apunta a ningún objeto válido en memoria y no tiene valor asociado en sentido tradicional. Internalmente suele ser un puntero a una dirección que no corresponde a ningún objeto válido (el detalle depende de la plataforma/entorno de ejecución).

---

## 5. Funciones cuyo cuerpo es una única expresión

Si el cuerpo es una única expresión cuyo valor se retorna, se pueden omitir las llaves y el `return`, sustituyéndolos por `=`:

```kotlin
fun doubleOf(x: Int): Int = x * 2
```

El tipo de retorno puede omitirse si el compilador lo infiere:

```kotlin
fun doubleOf(x: Int) = x * 2
```

Reglas del tipo de retorno:

| Forma | ¿Obligatorio declarar el tipo? |
| --- | --- |
| Bloque de código `{ … }` | Sí, **salvo** que sea `Unit` (entonces es opcional) |
| Única expresión con `=` | No si puede inferirse |

> [!tip] Sugerencia
> No omitas el tipo de retorno salvo que sea completamente obvio: su ausencia resta legibilidad al código.

---

## 6. Sobrecarga de funciones

Se pueden definir varias funciones con el **mismo nombre en el mismo ámbito** (fichero o clase) si tienen **firma distinta**: diferentes tipos o diferente número de parámetros. El tipo de retorno **NO** forma parte de la firma.

- Al llamar a una función sobrecargada, Kotlin decide **en tiempo de compilación** a qué versión enlazar la llamada, según cantidad y tipos de los argumentos → **ligadura estática o temprana** (*binding*).
- Si el compilador no puede decidir con certeza (ambigüedad) → error de compilación.
- La sobrecarga de funciones es una forma de **polimorfismo estático**; otras formas: sobrecarga de operadores, de constructores, referencias a método.

---

## 7. Argumentos por defecto

Un parámetro puede definir un **valor por defecto** que se usará si la llamada no suministra el argumento correspondiente:

```kotlin
fun printArguments(x: Int = 0, y: Int = 1) {
    println("x vale $x, y vale $y")
}

fun main() {
    printArguments()      // x vale 0, y vale 1
    printArguments(4)     // x vale 4, y vale 1
    printArguments(y = 8) // x vale 0, y vale 8
    printArguments(4, 8)  // x vale 4, y vale 8
}
```

> [!note] Ten en cuenta
> - Los valores por defecto **evitan sobrecargar métodos** por este motivo, como hay que hacer en Java.
> - Las expresiones por defecto se evalúan **bajo demanda en cada llamada**, sólo cuando no se pasa argumento para ese parámetro. A diferencia de Python, NO se almacenan de manera estática → es seguro usar objetos mutables (p. ej. una lista mutable) como valor por defecto.

El valor por defecto de un parámetro puede usar el valor de un **parámetro anterior** en la lista:

```kotlin
fun printArguments(x: Int = 0, y: Int = x + 1) {
    println("x vale $x, y vale $y")
}
```

Si un parámetro con valor por defecto **precede** a uno obligatorio, el valor por defecto sólo podrá usarse pasando los argumentos **con nombre**:

```kotlin
// El parámetro y es obligatorio, pero le precede uno opcional
fun printArguments(x: Int = 0, y: Int) {
    println("x vale $x, y vale $y")
}

fun main() {
    // ERROR DE COMPILACIÓN: parámetro y obligatorio
    printArguments()
    // ERROR DE COMPILACIÓN: parámetro y obligatorio (4 se asigna a x)
    printArguments(4)
    printArguments(y = 8)   // OK
    printArguments(4, 8)    // OK
}
```

> [!tip] Sugerencia
> Declara primero los parámetros obligatorios y después los opcionales con valores por defecto.

> [!warning] Aviso
> La sintaxis de argumentos con nombre **no funciona al llamar a funciones Java**: el bytecode de Java no siempre conserva los nombres exactos de los parámetros.

---

## 8. Argumentos con nombre

| Concepto | Definición |
| --- | --- |
| *Positional arguments* | La asociación argumento↔parámetro se hace por la **posición relativa** en las listas. Es la de prácticamente todos los lenguajes (Java, Kotlin) |
| *Named arguments* | La asociación se especifica **explícitamente** con el formato `parametro = argumento`. El **orden es indiferente** mientras todos se pasen con nombre |

Dada esta función:

```kotlin
fun reformat(
    str: String,
    normalizeCase: Boolean = true,
    upperCaseFirstLetter: Boolean = true,
    divideByCamelHumps: Boolean = false,
    wordSeparator: Char = ' '
) {
    // ...
}
```

Llamadas posicionales:

```kotlin
// Argumento sólo para el primer parámetro; el resto, por defecto
reformat(myString)
// Un argumento para cada parámetro
reformat(myString, true, true, false, '_')
```

Llamadas con nombre:

```kotlin
fun main() {
    val myString = "Hello"
    // Paso con nombre en un orden distinto al de la lista de parámetros
    reformat(normalizeCase = true,
             upperCaseFirstLetter = true,
             str = myString,
             divideByCamelHumps = false,
             wordSeparator = '_')
    // Especialmente útil cuando sólo pasamos valor a algunos parámetros
    reformat(str = myString, wordSeparator = '_')
}
```

**Mezcla** de posicional y con nombre: válida, pero respetando el orden de definición:

```kotlin
reformat(myString, wordSeparator = '_')   // Llamada válida
reformat(wordSeparator = '_', myString)    // Llamada NO válida
```

> [!tip] Sugerencia — cuándo usar named arguments
> - Cuando la función tenga **más de 2 o 3 parámetros**.
> - Cuando varios parámetros tengan valores por defecto y no se vayan a especificar para todos.
> - Cuando se quiera **cambiar el orden** de los argumentos respecto a la lista de parámetros.

Ventajas: legibilidad (evita errores de orden entre parámetros del mismo tipo). Inconvenientes: llamadas más largas y verbosas; si se **renombra** un parámetro hay que actualizar todas las llamadas con nombre (los IDE lo resuelven con refactorización automática).

---

## 9. varargs

`vararg` indica que un parámetro (normalmente el último) se asocia a una **lista variable de argumentos**:

```kotlin
fun printStrings(vararg strings: String) {
    for (string in strings)
        println(string)
}

fun main() {
    printStrings("Hola", "Adiós")
}
```

> [!note] Ten en cuenta
> - Dentro de la función, el parámetro `vararg` se trata como un `Array<String>`.
> - Sólo puede haber **un** parámetro `vararg` por función.
> - Si el `vararg` **no es el último**, los argumentos de los parámetros posteriores deben pasarse **con nombre** (o ser una lambda fuera de los paréntesis); si no, se considerarían parte de la lista variable.

> [!tip] Sugerencia
> Coloca el `vararg` el último — o el penúltimo si la función tiene un parámetro lambda, en cuyo caso la lambda va al final.

---

## 10. Spread operator

Para pasar los elementos de un array como argumentos del parámetro `vararg`, se **descompone** el array con el *spread operator*: `*` delante del nombre:

```kotlin
fun main() {
    val words = arrayOf("Hola", "Adiós")
    printStrings(*words)          // equivale a printStrings("Hola", "Adiós")
}
```

NO funciona directamente con otras colecciones (`List`, `Set`): hay que convertirlas antes con `toTypedArray()` (el `*spread` tiene menor precedencia que el operador `.`):

```kotlin
fun main() {
    val words: List<String> = listOf("Hola", "Adiós")
    printStrings(*words.toTypedArray())
}
```

---

## 11. Notación infija (infix)

Las funciones declaradas con `infix` pueden llamarse en **notación infija**: `operando1 operador operando2` (la notación habitual de fórmulas aritméticas/lógicas binarias), sin `.` ni paréntesis.

Requisitos para declarar una función `infix`:

1. Debe ser un **método de clase** o una **extension function** — nunca una *top-level function* (hace falta un objeto receptor).
2. **Un único parámetro**.
3. El parámetro no puede ser `vararg` ni tener valor por defecto.

```kotlin
class MyStringCollection {

    infix fun add(s: String) {
        println("Add $s to $this")
    }
}

fun main() {
    val myStringCollection = MyStringCollection()
    // Llamada válida habitual
    myStringCollection.add("abc")
    // Llamada válida usando notación infix
    myStringCollection add "abc"
}
```

> [!note] Precedencia y receptor
> - Menor precedencia que operadores aritméticos, casts y `rangeTo`; mayor que `&&`, `||`, `is` e `in`.
> - En notación infix es **obligatorio especificar siempre el receptor** y el parámetro. Si el receptor es el objeto actual, se usa `this`:

```kotlin
class MyStringCollection {

    infix fun add(s: String) {
        println("Add $s to $this")
    }

    fun build() {
        this add "abc"
        add("abc")
        // ERROR DE COMPILACIÓN: se debe especificar el receptor
        add "abc"
    }
}

fun main() {
    MyStringCollection().build()
}
```

---

## Esquema

- `fun nombre(param: Tipo): Retorno { … }`; parámetros inmutables (como `final`); backticks para nombres con espacios (tests); un parámetro por línea en declaraciones largas.
- Trailing comma (1.4+): añadir/reordenar sin tocar comas, diffs más limpios en Git; consensus con el equipo.
- `Unit`: retorno por defecto; clase singleton (`object`) que hereda de `Any`, ≠ `void`.
- `Nothing`: tipo vacío, subtipo de todo no-nullable; funciones que nunca retornan; `throw` y `return` son expresiones de tipo `Nothing`. `Nothing?`: tipo de `null`, supertipo de `Nothing`, subtipo de todo nullable.
- Cuerpo de expresión única: `fun f() = expr`, retorno inferible; con bloque es obligatorio (salvo `Unit`).
- Sobrecarga: misma firma ≠ (tipos/número de parámetros); el retorno NO es parte de la firma; ligadura estática en compilación; polimorfismo estático.
- Valores por defecto: sustituyen a sobrecargas de Java; evaluación bajo demanda (seguro con mutables); pueden usar parámetros anteriores; declarar antes los obligatorios; con nombre = no vale para funciones Java.
- *Positional* vs *named arguments*; mezcla posible respetando el orden.
- `vararg`: un solo parámetro por función, dentro es `Array<T>`; si no es el último → named args; último o penúltimo (antes de lambda).
- Spread `*array`; con listas: `*list.toTypedArray()`.
- `infix`: método o extension, 1 parámetro, no vararg/default; receptor obligatorio (`this`); precedencia intermedia.

## Relaciones

- [[02 - Jerarquia de tipos]] — `Unit`, `Nothing`, `Any` y la jerarquía de tipos que se menciona aquí
- [[01 - Introduccion a Kotlin]] — `fun main()` como punto de entrada; nivel de archivo
- [[04 - Estructuras básicas]] — `if`/`when` como expresiones; `is` visto en el tema 2
- [[03 - Funciones]] → siguiente tema natural: lambdas y funciones de orden superior en [[10 - Programación funcional]]
- Extension functions y top-level functions: [[06 - POO I]]

## Para repasar

- [ ] Partes de la definición de una función y por qué los parámetros son inmutables
- [ ] Para qué sirve el trailing comma y su relación con Git
- [ ] Diferencia entre `Unit` y `void` (y `Unit` vs `Void` de Java)
- [ ] Por qué `return` y `throw` pueden usarse dentro de una expresión (tipo `Nothing`)
- [ ] Cuándo es obligatorio declarar el tipo de retorno
- [ ] Qué forma parte de la firma de una función (y qué no)
- [ ] Cuándo falla una llamada con un parámetro opcional antes de uno obligatorio
- [ ] Diferencias positional vs named arguments; reglas de la mezcla
- [ ] Restricciones de `vararg` (posición, cantidad, tratamiento interno)
- [ ] Pasar una `List` a un `vararg`: `*list.toTypedArray()`
- [ ] Los 3 requisitos de una función `infix` y por qué hace falta receptor
