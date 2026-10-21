# 01.1 · Ejercicios 1: Introducción a Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 1: Kotlin
> Apuntes relacionados: [[01 - Introduccion a Kotlin]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/`

---

## Índice de Ejercicios

- [[#Ejercicio 1.1 · Ordenar tres números enteros por consola]]

---

## Ejercicio 1.1 · Ordenar tres números enteros por consola

> [!question] Enunciado
> Realiza un programa que solicite por consola tres números enteros, y los muestre por pantalla en orden.  
> *Nota:* Los `if` en Kotlin tienen una estructura similar a Java. No utilices Kotlin Playground porque no permite introducir datos interactivos por consola.

### Clases y métodos introducidos
- `readln()`: lee una línea completa introducida por el usuario desde la entrada estándar como `String`.
- `String.toInt()`: convierte una cadena de caracteres al tipo numérico `Int`. Lanza `NumberFormatException` si el texto no representa un número entero válido.

#### Ejemplo simple de funcionamiento
```kotlin
print("Introduce tu edad: ")
val entrada: String = readln()
val edad: Int = entrada.toInt()
println("El año que viene tendrás ${edad + 1} años")
```

### Código fuente (`Ejercicio1.1/src/Main.kt`)

```kotlin
fun main() {
    print("Escribe el primer número: ")
    val numero1 : Int = readln().toInt()
    print("Escribe el segundo número: ")
    val numero2 : Int = readln().toInt()
    print("Escribe el tercer número: ")
    val numero3 : Int = readln().toInt()

    if (numero1 > numero2 && numero1 > numero3) {
        if (numero2 > numero3) {
            print("$numero3 - $numero2 - $numero1")
        } else {
            print("$numero2 - $numero3 - $numero1")
        }
    }

    if (numero2 > numero1 && numero2 > numero3) {
        if (numero1 > numero3) {
            print("$numero3 - $numero1 - $numero2")
        } else {
            print("$numero1 - $numero3 - $numero2")
        }
    }

    if (numero3 > numero1 && numero3 > numero2) {
        if (numero1 > numero2) {
            print("$numero1 - $numero1 - $numero3")
        } else {
            print("$numero1 - $numero2 - $numero3")
        }
    }
}
```

### Explicación paso a paso
1. **Lectura y parseo encadenado:** Se usa `readln().toInt()` para leer la línea y convertirla directamente al tipo `Int`, almacenándola en variables inmutables (`val`).
2. **Comparación mediante `if` anidados:** Se evalúa qué número es el mayor mediante operadores lógicos `&&`. Una vez determinado el mayor, un segundo nivel condicional decide el orden relativo de los otros dos números.
3. **Plantillas de cadenas (String Templates):** Se interpolan los valores usando `$numeroX` sin necesidad de concatenar con `+`.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Lectura por consola | `readln()` | Devuelve una línea completa como `String` (requiere JVM, no Kotlin Playground). |
| Parseo | `String.toInt()` / `.toDouble()` | Convierte texto a número; lanza `NumberFormatException` si no es válido. |
| Condicionales | `if / else` anidados | En Kotlin `if` es también una expresión (visto en [[03 - Funciones]]). |
| Plantillas de cadena | `"$x"` / `"${expr}"` | Interpola variables y expresiones sin concatenar con `+`. |

---

# 02.1 · Ejercicios 2: Jerarquía de Tipos

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 2: Jerarquía de tipos
> Apuntes relacionados: [[02 - Jerarquia de tipos]] · Boletín anterior: [[01.1 - Ejercicios 1 Introduccion a Kotlin]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/`

---

## Índice de Ejercicios

- [[#Ejercicio 2.1 · Tipo Number y análisis de pérdida de precisión en conversiones]]
- [[#Ejercicio 2.2 · Números gigantes con BigInteger]]
- [[#Ejercicio 2.3 · Tipo Char, código Unicode y seguridad de tipos]]
- [[#Ejercicio 2.4 · Rangos cerrados, abiertos, progresiones y operador in]]
- [[#Ejercicio 2.5 · Evaluación en cortocircuito frente a evaluación completa en booleanos]]
- [[#Ejercicio 2.6 · Procesamiento de cadenas, filtrado por código ASCII y cadenas multilínea]]
- [[#Ejercicio 2.7 · Tipos nullables frente a no-nullables]]
- [[#Ejercicio 2.8 · Jerarquía de tipos: Any y Any?]]
- [[#Ejercicio 2.9 · Media de un array de notas (DoubleArray)]]
- [[#Ejercicio 2.10 · Variable Any? con contenido aleatorio y rangos]]

---

## Ejercicio 2.1 · Tipo Number y análisis de pérdida de precisión en conversiones

> [!question] Enunciado
> Realiza un programa que defina una variable de tipo `Number`, inicializada con un valor de tipo `Double`, `Float` o `Int`.  
> Después realiza la conversión de la variable a los tres tipos hacia tres variables distintas.  
> Finalmente, compara el valor original convertido a `Double` y el resultado de la conversión del valor original a `Int` y vuelto a convertir a `Double`, para comprobar si se ha producido pérdida de información. Haz lo mismo para comprobar si se produce pérdida al pasar a `Float`.  
> Cambia el literal de inicialización de la variable de tipo `Number` para probar con diferentes posibilidades.

### Clases y métodos introducidos
- `Number`: superclase abstracta de todos los tipos numéricos primitivos en Kotlin (`Byte`, `Short`, `Int`, `Long`, `Float`, `Double`).
- `Number.toDouble()`: convierte cualquier subtipo numérico a `Double` (64 bits, coma flotante IEEE 754).
- `Number.toFloat()`: convierte a `Float` (32 bits, coma flotante).
- `Number.toInt()`: convierte a `Int` (32 bits enteros), **truncando** la parte decimal (descarta todo lo que va tras la coma).

#### Ejemplo simple de funcionamiento
```kotlin
val num: Number = 45.789
val entero: Int = num.toInt()          // Truncado: 45
val decimal: Double = num.toDouble()    // 45.789
val recuperado: Double = entero.toDouble() // 45.0

val hayPerdida: Boolean = (decimal != recuperado) // true (se perdieron los decimales)
println("¿Pérdida al truncar?: $hayPerdida")
```

### Código fuente (`Ejercicio2.1/src/Main.kt`)

```kotlin
fun analizarPerdida(original: Number) {
    val valorDouble : Double = original.toDouble()
    println("A doble = $valorDouble")
    val valorFloat : Float = original.toFloat()
    println("A Float = $valorFloat")
    val valorInt : Int = original.toInt()
    println("A Int = $valorInt")

    val intADouble: Double = valorInt.toDouble()
    val perdidaInt: Boolean = valorDouble != intADouble
    println("Original -> $valorDouble  vs  Vuelta -> $intADouble")
    if (perdidaInt) {
        println("Hubo perdida")
    } else {
        println("No hubo perdida")
    }

    val floatADouble: Double = valorFloat.toDouble()
    val perdidaFloat: Boolean = valorDouble != floatADouble
    println("Original -> $valorDouble  vs  Vuelta -> $floatADouble")
    if (perdidaFloat) {
        println("Hubo perdida")
    } else {
        println("No hubo perdida")
    }
}

fun main() {
    val numero1: Number = 123.456789012345
    analizarPerdida(numero1)

    val numero2: Number = 45.5f
    analizarPerdida(numero2)

    val numero3: Number = 42
    analizarPerdida(numero3)

    val numero4: Number = 100.0
    analizarPerdida(numero4)
}
```

### Explicación paso a paso
1. **Polimorfismo numérico:** El parámetro `original: Number` acepta cualquier subtipo numérico sin sobrecargar la función.
2. **Conversión explícita obligatoria:** En Kotlin **no existe conversión implícita** entre tipos numéricos (no se puede asignar un `Int` a un `Double` directamente); se deben usar los métodos `.toDouble()`, `.toFloat()` o `.toInt()`.
3. **Comprobación de pérdida:** Al convertir de `Double` a `Int`, se eliminan los decimales. Al volver a `Double`, la comparación `!=` revela la pérdida. Al pasar de `Double` a `Float`, la mantisa se recorta de 53 bits a 24 bits, produciendo diferencias de precisión en números con muchos decimales.

---

## Ejercicio 2.2 · Números gigantes con BigInteger

> [!question] Enunciado
> Crea una variable que contenga un número entero muy grande (más de 25 dígitos) como un `String`.  
> Convierte ese `String` a `BigInteger` usando algún método disponible.  
> Súmale a este `BigInteger` el número 99, convertido previamente a `BigInteger` con algún método factoría disponible.  
> Imprime el resultado final de la suma.

### Clases y métodos introducidos
- `java.math.BigInteger`: clase para aritmética de enteros de precisión arbitraria (sin límite de 64 bits de `Long`).
- `String.toBigInteger()`: función de extensión propia de Kotlin para parsear cadenas numéricas a `BigInteger`.
- `BigInteger.valueOf(Long)`: método estático factoría para crear un `BigInteger` a partir de un entero estándar (`Long`).
- `operator fun plus (+)`: en Kotlin, la clase `BigInteger` sobrecarga el operador `+`, permitiendo escribir `a + b` en lugar del imperativo Java `a.add(b)`.

#### Ejemplo simple de funcionamiento
```kotlin
import java.math.BigInteger

val numCadena: String = "999999999999999999999999999999"
val big1: BigInteger = numCadena.toBigInteger()
val big2: BigInteger = BigInteger.valueOf(1L)
val suma: BigInteger = big1 + big2 // Sobrecarga de operador '+'

println("Suma exacta: $suma")
```

### Código fuente (`Ejercicio2.2/src/Main.kt`)

```kotlin
import java.math.BigInteger

fun main() {
    val numeroGrande: String = "1000000000000000000001"
    val numeroGrandeANumero : BigInteger = numeroGrande.toBigInteger()
    val noventaYNueve : BigInteger = BigInteger.valueOf(99L)
    val resultado : BigInteger = numeroGrandeANumero + noventaYNueve

    println("Numero original: $numeroGrande")
    println("Numero a sumar: $noventaYNueve")
    println("Resultado final: $resultado")
}
```

### Explicación paso a paso
1. **Límite de tipos primitivos:** Un número de más de 25 dígitos supera el valor máximo de `Long` ($2^{63}-1 \approx 9 \times 10^{18}$), por lo que provocaría desbordamiento inmediato de compilarse como primitivo.
2. **Conversión y factoría:** Se utiliza `.toBigInteger()` sobre la cadena de texto y `BigInteger.valueOf(99L)` para el incremento pequeño.
3. **Operador `+` sintáctico:** Gracias a la sobrecarga de operadores de Kotlin, `numeroGrandeANumero + noventaYNueve` es equivalente a la llamada Java `.add()`, manteniendo el código legible.

---

## Ejercicio 2.3 · Tipo Char, código Unicode y seguridad de tipos

> [!question] Enunciado
> Crea una variable llamada `initialLetter` de tipo `Char` y asígnale el carácter `'K'`.  
> Crea una variable `tab` de tipo `Char` y asígnale el carácter de tabulación.  
> Crea una variable `asciiCode` de tipo `Int`. Asígnale el valor Unicode de `initialLetter` usando la propiedad adecuada de `Char`.  
> Crea una variable `codeForSymbol` de tipo `Int` y asígnale el valor Unicode del carácter correspondiente al signo de dólar.  
> Intenta escribir una condición `if` para verificar si `initialLetter` es igual al número 75. Comenta esta línea de código inmediatamente después de escribirla, y explica en un comentario (con una sola frase) por qué genera un error de compilación.  
> Imprime `initialLetter`, `tab`, `asciiCode` y `codeForSymbol`.

### Clases y métodos introducidos
- `Char`: tipo de dato que representa un carácter UTF-16 de 16 bits.
- `Char.code`: propiedad que devuelve el punto de código numérico Unicode (`Int`) correspondiente al carácter.
- Caracteres de escape: `'\t'` (tabulación), `'\n'` (salto de línea), etc.

#### Ejemplo simple de funcionamiento
```kotlin
val letra: Char = 'A'
val puntoUnicode: Int = letra.code // 65
println("El código de '$letra' es $puntoUnicode")

// Error en Kotlin: los tipos no son comparables directamente
// if (letra == 65) { ... } -> Compile Error: Operator '==' cannot be applied to 'Char' and 'Int'
if (letra.code == 65) {
    println("Es la letra con código 65")
}
```

### Código fuente (`Ejercicio2.3/src/Main.kt`)

```kotlin
fun main() {
    val initialLetter: Char = 'K'
    val tab: Char = '\t'
    val asciiCode: Int = initialLetter.code
    val codeForSymbol: Int = '$'.code

//    if (initialLetter == 75) {
//        println("son iguales")
//    } else {
//        println("no son iguales")
//    }
// Da error, ya que no se pueden comparar un tipo char con un tipo int

    if (initialLetter.code == 75) {
        println("son iguales")
    } else {
        println("no son iguales")
    }

    println(initialLetter)
    println(tab)
    println(asciiCode)
    println(codeForSymbol)
}
```

### Explicación paso a paso
1. **Diferencia con Java:** En Java, `char` es un tipo entero numérico encubierto y se puede hacer `if ('K' == 75)`. En Kotlin, **`Char` no es un número**: es un tipo diferenciado de primera clase.
2. **Propiedad `.code`:** Para obtener el valor numérico hay que consultar explícitamente `.code` (sustituye a la antigua función `.toInt()` de versiones viejas de Kotlin).
3. **Seguridad estática de tipos:** La comparación `initialLetter == 75` es rechazada por el compilador porque `==` exige compatibilidad de tipos entre ambos operandos.

---

## Ejercicio 2.4 · Rangos cerrados, abiertos, progresiones y operador in

> [!question] Enunciado
> Crea una variable llamada `closedRange` que contenga los números enteros desde 10 hasta 15, ambos inclusive, usando la sintaxis abreviada. Imprime este rango.  
> Crea una variable llamada `openRange` que contenga las letras desde `'A'` hasta `'D'`, excluyendo `'D'`, usando la sintaxis abreviada. Recorre e imprime cada carácter dentro de este rango usando un bucle `for`.  
> Crea una variable llamada `evenProgression` que contenga los números pares desde 20 hasta 10, en orden descendente, con un salto (paso) de 2. Recorre e imprime cada número de esta progresión.  
> Crea una variable `isInRange` que verifique si el número 12 está dentro de `closedRange`. Imprime el resultado de esta verificación (debería ser `true`).

### Clases y métodos introducidos
- `IntRange` / `CharRange`: tipos que representan secuencias acotadas de valores.
- Operador `..`: rango cerrado (incluye ambos extremos: `a..b` $\rightarrow [a, b]$).
- Operador `..<`: rango semiabierto (excluye el extremo final: `a..<b` $\rightarrow [a, b)$).
- Función infija `downTo`: progresión descendente desde un máximo hasta un mínimo.
- Función infija `step`: establece el incremento o decremento de la progresión.
- Operador `in` / `!in`: comprueba pertenencia de un elemento a un rango o colección de forma concisa.

#### Ejemplo simple de funcionamiento
```kotlin
val cerrado: IntRange = 1..5        // 1, 2, 3, 4, 5
val semiabierto: IntRange = 1..<5   // 1, 2, 3, 4
val regresivo = 10 downTo 0 step 2  // 10, 8, 6, 4, 2, 0

val estaDentro: Boolean = 3 in semiabierto // true
println("¿3 está en 1..<5?: $estaDentro")
```

### Código fuente (`Ejercicio2.4/src/Main.kt`)

```kotlin
fun main() {
    val closedRange: IntRange = 10..15
    println(closedRange)

    val openRange: CharRange = 'A'..<'D'
    for (char in openRange) {
        print(char)
    }

    println()

    val evenProgression: IntProgression = 20 downTo 10 step 2
    for (numero in evenProgression) {
        print("$numero ")
    }

    println()

    val isInRange: Boolean = 12 in closedRange
    println(isInRange)
}
```

### Explicación paso a paso
1. **Rango cerrado con `..`:** `10..15` incluye el 10 y el 15.
2. **Rango semiabierto con `..<`:** `'A'..<'D'` genera únicamente `'A'`, `'B'` y `'C'`.
3. **Progresión con `downTo` y `step`:** Al recorrer hacia abajo, el operador `..` no funciona (produciría un rango vacío). Se utiliza la palabra clave `downTo` y se define el salto con `step 2`.
4. **Comprobación de rango con `in`:** `12 in closedRange` traduce internamente a `12 >= 10 && 12 <= 15`, pero con una sintaxis limpia y expresiva.

---

## Ejercicio 2.5 · Evaluación en cortocircuito frente a evaluación completa en booleanos

> [!question] Enunciado
> Define dentro de la función `main` tres variables booleanas: `isReady` inicializada a `true`, `isProcessing` inicializada a `false`, e `isExpensive` inicializada a `true`.  
> Ahora, crea una variable `shortCircuitResult` que use el operador `&&` para evaluar la expresión: `isProcessing && isExpensive`.  
> Después, crea una variable `fullEvalResult` que use el método `and` (con sintaxis infija) para evaluar exactamente la misma expresión: `isProcessing and isExpensive`.  
> Por último, crea una variable `isNotReady` que sea el resultado de negar (`!`) la variable `isReady`.  
> Finalmente, imprime los valores de `shortCircuitResult`, `fullEvalResult` e `isNotReady` para demostrar cómo operan los diferentes operadores lógicos.

### Clases y métodos introducidos
- `Boolean`: tipo booleano con valores `true` o `false`.
- Operador `&&` (cortocircuito): si el primer operando es `false`, el segundo **no se evalúa**.
- Función infija `Boolean.and(other)`: operación lógica AND **sin cortocircuito**; evalúa siempre obligatoriamente ambos operandos.
- Operador `!`: negación lógica unaria.

#### Ejemplo simple de funcionamiento
```kotlin
fun operacionCostosa(): Boolean {
    println("Ejecutando operación costosa...")
    return true
}

val condicion: Boolean = false
// Con && (cortocircuito): la función NUNCA llega a ejecutarse
val r1: Boolean = condicion && operacionCostosa()

// Con .and() / infijo and: la función SIEMPRE se ejecuta
val r2: Boolean = condicion and operacionCostosa()
```

### Código fuente (`Ejercicio2.5/src/Main.kt`)

```kotlin
fun main() {
    val isReady: Boolean = true
    val isProcessing: Boolean = false
    val isExpensive: Boolean = true

    val shorCircuitResult: Boolean = isProcessing && isExpensive

    val fullEvalResult: Boolean = isProcessing.and(isExpensive)

    val isNotReady: Boolean = !isReady

    println(shorCircuitResult)
    println(fullEvalResult)
    println(isNotReady)
}
```

### Explicación paso a paso
1. **Cortocircuito (`&&` / `||`):** Es el operador habitual en programación. Si el resultado ya está determinado por el operando izquierdo, se detiene la ejecución del derecho (útil para evitar excepciones como `objeto != null && objeto.metodo()`).
2. **Evaluación completa (`and` / `or`):** Son funciones miembro de `Boolean` utilizables en notación infija (`a and b`). Garantizan que ambas expresiones se evalúan siempre, independientemente de que el lado izquierdo sea `false`.
3. **Negación (`!`):** Invierte el valor del booleano `isReady` de `true` a `false`.

---

## Ejercicio 2.6 · Procesamiento de cadenas, filtrado por código ASCII y cadenas multilínea

> [!question] Enunciado
> Realiza un programa que solicite por consola una cadena de caracteres y diga para cada carácter si está en mayúscula, si está en minúscula o no es una letra (la 'ñ' no cuenta como letra en este criterio básico), comprobando que el código numérico correspondiente al carácter esté en el rango numérico de los códigos de la `'A'` a la `'Z'`, o de la `'a'` a la `'z'`.  
> Realiza los siguientes pasos complementarios:
> - Define dos variables `String`: `firstName` inicializada a `"Alan"`, `lastName` a `"Turing"`, y una variable `yearOfBirth` de tipo `Int` con el valor `1912`.
> - Crea una variable `fullName` concatenando `firstName`, un espacio y `lastName`.
> - Accede al primer carácter de `fullName` usando indexación o método de primer elemento e imprime su valor.
> - Compara mediante operador de igualdad si `firstName` es igual a `"Alan"`.
> - Define una variable `biography` como una cadena multilínea que use `trimMargin()` con el prefijo `|` conteniendo los datos anteriores.

### Clases y métodos introducidos
- `CharSequence.first()`: método que devuelve el primer carácter (`Char`) de una cadena.
- `String.trimMargin(marginPrefix)`: elimina los espacios en blanco que sirven de sangría antes de un carácter delimitador (por defecto `|`).
- Literales de cadena sin formato / multilínea: encerrados entre triples comillas `""" ... """`, conservan saltos de línea sin necesidad de `\n`.

#### Ejemplo simple de funcionamiento
```kotlin
val nombre = "Kotlin"
val inicial: Char = nombre.first() // 'K'

val ficha: String = """
    |Lenguaje: $nombre
    |Inicial: $inicial
""".trimMargin()
println(ficha)
```

### Código fuente (`Ejercicio2.6/src/Main.kt`)

```kotlin
fun main() {
    print("Introduce una cadena de caracteres: ")
    val cadena: String = readln()

    // Códigos ASCII: 'A'-'Z' (65..90), 'a'-'z' (97..122)
    val abecedarioMayus: IntRange = 65..90
    val abecedarioMinus: IntRange = 97..122

    for (c in cadena) {
        if (c.code in abecedarioMayus) {
            println("$c es una letra mayúscula")
        }
        if (c.code in abecedarioMinus) {
            println("$c es una letra minúscula")
        }
        if (c.code !in abecedarioMinus && c.code !in abecedarioMayus){
            println("$c no es una letra")
        }
    }

    println("--------------------------------------------------------------")

    val firstName: String = "Alan"
    val lastname: String = "Turing"
    val yearOfBirth: Int = 1912

    val fullName: String = "$firstName $lastname"

    val firstChar: Char = fullName.first()
    println(firstChar)

    val isSameName: Boolean = firstName == "Alan"
    println(isSameName)

    println("--------------------------------------------------------------")

    val biography: String = """
        |Full Name: [Valor de fullName]. 
        |Year: [Valor de yearOfBirth]. 
        |The first letter is: [$firstChar]
    """.trimMargin()

    println(biography)
}
```

### Explicación paso a paso
1. **Iteración sobre cadenas:** Un `String` en Kotlin se recorre directamente con `for (c in cadena)`.
2. **Filtrado por código numérico:** Mediante `c.code in abecedarioMayus` se clasifica el carácter según su posición en la tabla ASCII.
3. **Cadenas multilínea con `trimMargin`:** Permiten escribir textos largos o estructurados (como JSON, SQL o plantillas) manteniendo el código fuente bien indentado en el IDE sin que esos espacios se trasladen a la salida real por consola.

---

## Ejercicio 2.7 · Tipos nullables frente a no-nullables

> [!question] Enunciado
> Declara una variable `userName` de tipo `String?` y asígnale el valor `null` inicialmente.  
> Luego, declara otra variable inmutable, `defaultName`, de tipo `String` (no nullable) y asígnale el valor `"Guest"`.  
> A continuación, intenta asignar el valor de `userName` a una nueva variable inmutable, `finalName`, de tipo `String` y observa el error de compilación que se produce.  
> Finalmente, comenta la línea que causa el error y explica en un comentario de una sola línea, en español, por qué el compilador de Kotlin detiene esta asignación.

### Clases y métodos introducidos
- `Tipo?` (Tipo Nullable): indica que la variable puede almacenar una referencia válida o el valor especial `null`.
- `Tipo` (Tipo No Nullable): garantiza en tiempo de compilación que la variable **nunca puede contener `null`**, eliminando de raíz las excepciones `NullPointerException` en tiempo de ejecución.

#### Ejemplo simple de funcionamiento
```kotlin
var puedeSerNulo: String? = "Texto"
puedeSerNulo = null // Válido

var noPuedeSerNulo: String = "Texto"
// noPuedeSerNulo = null // Error de compilación inmediato: Null can not be a value of a non-null-typed String

// Tampoco se puede asignar directamente un nullable a un no-nullable:
// noPuedeSerNulo = puedeSerNulo // Error de compilación: Type mismatch
```

### Código fuente (`Ejercicio2.7/src/Main.kt`)

```kotlin
fun main() {
    val userName: String? = null
    val defaultName: String = "Guest"
    
    // var finalName: String = userName
    // Este error se produce porque no se le puede asignar un nulo a un tipo no nullable.
}
```

### Explicación paso a paso
1. **Sistema de tipos nulos (Null Safety):** En la jerarquía de tipos de Kotlin, `String` es un subtipo estricto de `String?`. Todo `String` es un `String?`, pero no todo `String?` es un `String`.
2. **Error en tiempo de compilación:** El compilador detecta que `userName` tiene la potencialidad de contener `null`. Dado que `finalName` está declarada como `String` estricto (no nullable), la asignación directa es rechazada antes de que el programa pueda llegar a ejecutarse.

---

## Ejercicio 2.8 · Jerarquía de tipos: Any y Any?

> [!question] Enunciado
> Declara una variable inmutable `firstVariable` a la que asignas un literal numérico entero, y otra variable inmutable `secondVariable` a la que asignas la cadena de texto `"Hello World"`.  
> A continuación, declara una tercera variable inmutable, `thirdVariable`, de tipo explícito `Any`, y asígnale el valor de `firstVariable`.  
> Finalmente, declara una última variable, `fourthVariable`, de tipo explícito `Any?`, asígnale el valor `null`, y luego, en una línea posterior, intenta asignarle el valor de `secondVariable`.

### Clases y métodos introducidos
- `Any`: cúspide de la jerarquía de tipos no-nulos en Kotlin. Todos los tipos no-nulos (`Int`, `String`, `Boolean`, clases personalizadas) heredan directa o indirectamente de `Any` (análogo a `Object` en Java).
- `Any?`: cúspide absoluta de toda la jerarquía de Kotlin. Acepta cualquier valor de cualquier tipo, además del valor `null`.

#### Ejemplo simple de funcionamiento
```kotlin
val obj1: Any = 100         // Int es subtipo de Any
val obj2: Any = "Cadena"    // String es subtipo de Any
// val obj3: Any = null     // ERROR: Any no admite null

var universal: Any? = null  // Válido: Any? admite null
universal = obj2            // Válido: Any? también admite cualquier objeto no-nulo
```

### Código fuente (`Ejercicio2.8/src/Main.kt`)

```kotlin
fun main() {
    var firstVariable: Int = 4
    var secondVariable: String = "Hello World"
    var thirdVariable: Any = firstVariable
    var fourthVariable: Any? = null
    fourthVariable = secondVariable
}
```

### Explicación paso a paso
1. **`Any` como supertipo raíz:** Al declarar `thirdVariable: Any = firstVariable`, se produce una conversión hacia arriba segura (*upcasting*). Dado que `Int` hereda de `Any`, la asignación es totalmente válida.
2. **`Any?` como supertipo universal con soporte de nulos:** `fourthVariable` puede empezar valiendo `null` y en cualquier momento posterior recibir una cadena (`String`), un número o cualquier otra instancia de la JVM, porque todos son compatibles con `Any?`.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Superclase Numérica | `Number` | Base de `Int`, `Double`, `Float`, etc. Requiere conversión explícita (`toInt()`, etc.). |
| Precisión Arbitraria | `BigInteger` | Soporta enteros de tamaño infinito; permite operadores `+`, `-`, `*`. |
| Caracteres | `Char` | **No es un número**. Se consulta su valor Unicode con la propiedad `.code`. |
| Rangos | `..`, `..<`, `downTo`, `step` | Generan progresiones de valores; comprobación instantánea con `in`. |
| Evaluación Lógica | `&&` vs `and` | `&&` cortocircuita (detiene evaluación); `and` evalúa ambos lados. |
| Null Safety | `T` vs `T?` | `T` garantiza ausencia total de nulos; `T?` admite `null`. |
| Raíz de la Jerarquía | `Any` / `Any?` | `Any` para cualquier objeto no-nulo; `Any?` para absolutamente cualquier valor o `null`. |

## Relaciones

- Teoría del tema: [[01 - Introduccion a Kotlin]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

---

## Ejercicio 2.9 · Media de un array de notas (DoubleArray)

> [!question] Enunciado
> Realiza un programa que solicite las notas de 4 exámenes, los almacene en un array, y después recorra el array y obtenga y muestre por pantalla la media aritmética de las notas.

### Clases y métodos introducidos
- `DoubleArray(n)`: constructor de array primitivo de `Double` de tamaño fijo `n`, inicializado a `0.0`.
- `array[i] = v` / `array[i]`: acceso por índice a elementos del array.
- `xs.size`: propiedad con la longitud del array.
- **Bucle indexado** `for (i in 0 ..< xs.size)` frente a **bucle de recorrido** `for (x in xs)`.

#### Ejemplo simple de funcionamiento
```kotlin
fun main() {
    val notas = DoubleArray(3)          // [0.0, 0.0, 0.0]
    notas[0] = 8.5
    notas[1] = 6.0
    notas[2] = 10.0

    for (i in 0 ..< notas.size) {       // indexado: necesito la posición
        println("nota[$i] = ${notas[i]}")
    }
    for (n in notas) {                  // recorrido: solo el valor
        print("$n ")
    }
}
```

### Código fuente (`Ejercicio2.9/src/Main.kt`)

```kotlin
fun main() {
    val notas: DoubleArray = DoubleArray(4)

    for (i in 0 ..< notas.size) {
        print("Introduce la nota del examen ${i + 1}: ")
        notas[i] = readln().toDouble()
    }

    var suma: Double = 0.0
    for (nota in notas) {
        suma += nota
    }

    val media: Double = suma / notas.size
    println("La media de las notas es: $media")
}
```

### Explicación paso a paso
1. **Array de tamaño fijo con valores por defecto:** `DoubleArray(4)` reserva 4 huecos ya inicializados en `0.0`, así se puede escribir directamente `notas[i]` sin crear el array elemento a elemento.
2. **Por qué el primer bucle es indexado:** para pedir cada nota hace falta el índice (lectura y escritura), y se muestra `i + 1` porque el usuario cuenta los exámenes desde 1 mientras el array empieza en 0.
3. **`..<` (semiabierto):** recorre `0, 1, 2, 3` sin tocar la posición 4, evitando el error típico `ArrayIndexOutOfBoundsException` del clásico `i <= size`.
4. **El segundo bucle es de recorrido puro** (`for (nota in notas)`): solo interesa el valor para acumular en `suma`, que debe ser `var` porque se modifica en cada vuelta.
5. **Media:** `suma / notas.size` — división `Double / Int`; el `Int` se promueve a `Double` en la operación. Con las notas 5, 7, 6, 8 la salida real es `La media de las notas es: 6.5`.

> [!tip] Alternativa de librería
> Todo el bloque de acumulación se resume en `notas.average()`, pero el ejercicio pide recorrer el array a mano para practicar los dos estilos de `for`.

---

## Ejercicio 2.10 · Variable Any? con contenido aleatorio y rangos

> [!question] Enunciado
> Crea un programa que declare una variable de tipo `Any?` que podrá contener un valor entero, una cadena de texto o `null`, dependiendo de un número aleatorio entre 0 y 100 generado con `Random.nextInt(lim_inf, lim_sup_no_incluido)` (comprobando que se importa `kotlin.random.Random`). Si el número está en `[0, 33]`, asigna `null`; en `[34, 66]`, el valor `5`; en `[67, 100]`, la cadena `"Baldomero"`. Muestra por pantalla el número generado y el tipo de contenido de la variable.

### Clases y métodos introducidos
- `kotlin.random.Random.nextInt(inicio, hasta)`: entero pseudoaleatorio en `[inicio, hasta)` — la frontera superior **no** se incluye.
- `var valor: Any?`: variable del supertipo universal nullable; puede cambiar de tipo de contenido en vuelo porque `Int`, `String` y `null` son subtipos de `Any?`.
- `valor in rangoInt`: operador `in` sobre `IntRange` (el `Any?` se desempaqueta a `Int` para la comparación).
- `asignación de reemplazo de contenido`: tras `valor = null` / `valor = 5` / `valor = "Baldomero"`, la variable contiene un tipo distinto del original.

#### Ejemplo simple de funcionamiento
```kotlin
import kotlin.random.Random

fun main() {
    // Random.nextInt(1, 10) nunca devuelve 10
    for (i in 1..5) {
        val n: Int = Random.nextInt(1, 10)
        println("$n en [1,10): ${n in 1..9}")
    }

    var caja: Any? = Random.nextInt(0, 100)  // empieza siendo Int
    caja = "ahora es String"                  // Any? admite cualquier reemplazo
    println(caja)
}
```

### Código fuente (`Ejercicio2.10/src/Main.kt`)

```kotlin
import kotlin.random.Random

fun main() {
    var valor: Any? = Random.nextInt(0, 100)
    val rangoBajo: IntRange = 0..33
    val rangoMedio: IntRange = 34..66
    val rangoAlto: IntRange = 67..100

    if (valor in rangoBajo) {
        println("Salió $valor")
        valor = null
        println("la variable es nula: $valor")
    }

    if (valor in rangoMedio) {
        println("Salió $valor")
        valor = 5
        println("La variable es un número entero: $valor")
    }

    if (valor in rangoAlto) {
        println("Salió $valor")
        valor = "Baldomero"
        println("La variable es una cadena de texto: $valor")
    }
}
```

### Explicación paso a paso
1. **Una variable, tres tipos:** `Any?` es la cúspide de la jerarquía ([[02 - Jerarquia de tipos]]). Guardar primero un `Int` y luego reemplazarlo por `null`, otro `Int` o un `String` es legal porque todos son subtipos de `Any?`.
2. **El aleatorio manda:** `Random.nextInt(0, 100)` genera `0..99`; ese valor inicial determina qué rama se activa. Los tres `IntRange` hacen legible la partición del enunciado.
3. **`valor in rangoMedio` sobre `Any?`:** funciona porque en ese punto el contenido *real* sigue siendo un `Int` (el primer `if` no lo tocó); Kotlin desempaqueta (*unboxing*) para comparar. Si el contenido no fuera numérico, la comprobación `in` lanzaría excepción en tiempo de ejecución — aquí el flujo la protege.
4. **Encadenamiento de reemplazos:** si el sorteo cae en `0..33`, el primer bloque asigna `null`, y los dos `if` restantes ya no se activan porque `null in 34..66` es `false`. Los tres bloques son mutuamente excluyentes por construcción de los rangos.
5. **Salida real (típica):** p. ej. con 71 sorteado → `Salió 71` y `La variable es una cadena de texto: Baldomero`. Como solo se imprime un bloque por ejecución, hay que relanzar el programa para ver los tres casos (o sustituir los tres `if` por un `when (valor)`).

> [!warning] Dos detalles del enunciado vs el código
> - `nextInt(0, 100)` **nunca genera 100**, así que el `rangoAlto = 67..100` tiene un valor imposible; en la práctica cubre `67..99`.
> - En la rama nula, el programa imprime `la variable es nula` con minúscula (el enunciado pedía `"La variable es nula"`), y muestra el `null` interpolado (`la variable es nula: null`).

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Array primitivo con tamaño | `DoubleArray(4)` | Longitud fija, valores por defecto `0.0`; escritura por índice. |
| Bucle indexado | `for (i in 0 ..< xs.size)` | Acceso a posición; `..<` evita el fuera-de-límite. |
| Bucle de recorrido | `for (x in xs)` | Solo valores, más simple cuando no interesa el índice. |
| Aleatoriedad | `Random.nextInt(a, b)` | Entero en `[a, b)`; requiere `import kotlin.random.Random`. |
| Caja universal | `var v: Any?` | Admite cualquier tipo y `null`; se puede reemplazar el contenido por otro tipo. |
| Pertenencia | `v in 34..66` | `in` delega en el rango; con `Any?` desempaca si el contenido real es numérico. |

## Relaciones

- Teoría del tema: [[02 - Jerarquia de tipos]] — `Any?`, `IntRange`, arrays primitivos
- Bloque anterior de ejercicios: [[01.1 - Ejercicios 1 Introduccion a Kotlin]] (2.1–2.8)
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Crear un `IntArray` de 5 huecos vacíos y recorrerlo escribiendo por índice
- [ ] Diferenciar `for (i in 0 ..< v.size)` de `for (e in v)` y decir cuál usar en cada caso
- [ ] Explicar por qué `Random.nextInt(0, 100)` no puede devolver 100
- [ ] Justificar por qué `var caja: Any?` puede pasar de `Int` a `String` sin error
- [ ] Predecir qué imprimen los tres `if` encadenados cuando el sorteo sale 20

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Superclase Numérica | `Number` | Base de `Int`, `Double`, `Float`, etc. Requiere conversión explícita (`toInt()`, etc.). |
| Precisión Arbitraria | `BigInteger` | Soporta enteros de tamaño infinito; permite operadores `+`, `-`, `*`. |
| Caracteres | `Char` | **No es un número**. Se consulta su valor Unicode con la propiedad `.code`. |
| Rangos | `..`, `..<`, `downTo`, `step` | Generan progresiones de valores; comprobación instantánea con `in`. |
| Evaluación Lógica | `&&` vs `and` | `&&` cortocircuita (detiene evaluación); `and` evalúa ambos lados. |
| Null Safety | `T` vs `T?` | `T` garantiza ausencia total de nulos; `T?` admite `null`. |
| Raíz de la Jerarquía | `Any` / `Any?` | `Any` para cualquier objeto no-nulo; `Any?` para absolutamente cualquier valor o `null`. |
| Arrays primitivos | `DoubleArray(n)` | Longitud fija, valores por defecto; acceso por índice y recorrido con `for`. |
| Aleatoriedad | `Random.nextInt(a, b)` | Entero en `[a, b)`; requiere `import kotlin.random.Random`. |

---

---
asignatura: PMDM
tema: 3
tipo: ejercicio
estado: completado
fecha: 2026-09-23
tags:
- DAM/ejercicio
- DAM/pmdm/kotlin
- DAM/pmdm/ejercicios
---

# 03.1 · Ejercicios 3: Funciones en Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 3: Kotlin
> Apuntes relacionados: [[03 - Funciones]] · Boletín anterior: [[02.1 - Ejercicios 2 Jerarquia de Tipos]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/`

---

## Índice de Ejercicios

- [[#Ejercicio 3.1 · Función isPrime con retornos anticipados]]
- [[#Ejercicio 3.2 · Sintaxis multilínea de parámetros y trailing comma]]
- [[#Ejercicio 3.3 · Tipo de retorno implícito Unit]]
- [[#Ejercicio 3.4 · throw como rama de una expresión (tipo Nothing)]]
- [[#Ejercicio 3.5 · Función de expresión única: año bisiesto]]
- [[#Ejercicio 3.6 · Sobrecarga de funciones: sumValues]]
- [[#Ejercicio 3.7 · Parámetros con valores por defecto]]
- [[#Ejercicio 3.8 · Argumentos con nombre y mezcla de estilos]]
- [[#Ejercicio 3.9 · Parámetro vararg no posicionado al final]]
- [[#Ejercicio 3.10 · Spread operator (*) sobre varargs]]
- [[#Ejercicio 3.11 · Funciones infijas (infix)]]

---

## Ejercicio 3.1 · Función isPrime con retornos anticipados

> [!question] Enunciado
> Realiza un programa en el que se define una función `isPrime` que reciba un número entero y retorne si es número primo o no. La función `main()` deberá llamar a la función `isPrime` varias veces con valores diferentes para probarla.

### Clases y métodos introducidos
- `fun nombre(param: Tipo): Boolean`: función con parámetro y tipo de retorno explícito.
- **Retornos anticipados** (*guard clauses*): varios `return` a lo largo del cuerpo; en cuanto se ejecuta uno, la función termina.
- `while`: bucle condicionado, usado aquí para probar divisores.
- `arrayOf(...)`: crea un `Array<Int>` con los valores enumerados.

#### Ejemplo simple de funcionamiento
```kotlin
fun esPar(n: Int): Boolean {
    if (n < 0) return false   // cláusula de guarda: salida temprana
    return n % 2 == 0
}

fun main() {
    println(esPar(4))  // true
    println(esPar(7))  // false
}
```

### Código fuente (`Ejercicio3.1/src/Main.kt`)

```kotlin
fun isPrime(entero: Int): Boolean {
    if (entero <= 1) return false

    if (entero == 2) return true

    if (entero % 2 == 0) return false

    var i = 3
    while (i * i <= entero) {
        if (entero % i == 0) {
            return false
        }
        i += 2
    }
    return true
}

fun main() {
    val testNumbers = arrayOf(-5, 0, 1, 2, 3, 4, 7, 9, 13, 17, 25, 29)

    for (num in testNumbers) {
        if (isPrime(num)) {
            println("El número $num es primo")
        } else {
            println("El número $num no es primo")
        }
    }
}
```

### Explicación paso a paso
1. **Descarte por exclusión:** los tres primeros `if` resuelven sin bucle los casos rápidos (números ≤ 1 no son primos, el 2 sí, todos los pares no). Cada `return` corta la ejecución inmediatamente.
2. **Límite `i * i <= entero`:** solo hay que probar divisores hasta la raíz cuadrada; si ningún divisor `i` divide al número, es primo. Se comparan `i * i` en lugar de calcular `sqrt()`, evitando coma flotante.
3. **`i += 2`:** como los pares ya quedaron descartados, el bucle solo prueba impares (3, 5, 7, …), reduciendo el trabajo a la mitad.
4. **Banco de pruebas:** `arrayOf(-5, 0, 1, …)` incluye casos límite (negativos, 0, 1, 2, cuadrados como 9 y 25) y se recorre con `for (num in testNumbers)`.

---

## Ejercicio 3.2 · Sintaxis multilínea de parámetros y trailing comma

> [!question] Enunciado
> Define una función llamada `calculateMetrics` que acepte exactamente tres parámetros en el siguiente orden: `dataList` de tipo `List<Int>`, `includeAverage` de tipo `Boolean`, y `precisionDigits` de tipo `Int`. Escribe la declaración de la función usando una sintaxis multilínea para los parámetros y asegúrate de incluir el *trailing comma* después del último parámetro. Luego imprime por separado los tres valores que recibe. Finalmente, llama a la función desde `main` utilizando también sintaxis multilínea para los argumentos y el correspondiente *trailing comma*.

### Clases y métodos introducidos
- **Trailing comma:** coma final permitida tanto en la lista de parámetros como en la de argumentos (Kotlin ≥ 1.4).
- **Declaración multilínea:** un parámetro por línea, con sangría, entre `(` y `)`.
- `List<Int>` / `listOf(...)`: lista inmutable de enteros (tipo de la jerarquía de colecciones).

#### Ejemplo simple de funcionamiento
```kotlin
fun registrar(
    id: Int,
    nombre: String,   // ← cada parámetro en su línea
) {                   // ← trailing comma tras el último
    println("$id: $nombre")
}

fun main() {
    registrar(
        1,
        "Kotlin",
    )
}
```

### Código fuente (`Ejercicio3.2/src/Main.kt`)

```kotlin
fun calculateMetrics(
    dataList: List<Int>,
    includeAverage: Boolean,
    precisionDigits: Int,
) {
    println("$dataList, $includeAverage, $precisionDigits")
}

fun main() {
    calculateMetrics(
        listOf(1, 2, 3),
        true,
        4,
    )
}
```

### Explicación paso a paso
1. **Legibilidad:** con tres o más parámetros, partir la firma en varias líneas hace que cada uno se lea como una entrada independiente.
2. **Utilidad real del trailing comma:** si mañana se añade un cuarto parámetro, solo hay que **agregar una línea**; la anterior queda intacta. En el control de versiones (Git) el *diff* muestra `+1 línea` en lugar de `-1/+2` (la vieja última línea modificada por la coma).
3. **Simetría llamada/declaración:** los argumentos se escriben en el mismo formato multilínea, en el mismo orden (*positional arguments*).

---

## Ejercicio 3.3 · Tipo de retorno implícito Unit

> [!question] Enunciado
> Define dos funciones llamadas `printWelcomeMessage` y `logActivity`. `printWelcomeMessage` debe aceptar un único parámetro `user` de tipo `String` e imprimir un mensaje de bienvenida personalizado. `logActivity` no debe aceptar parámetros, solo imprimir la cadena `"Activity logged"`. No especifiques un tipo de retorno explícito para ninguna de las dos. En `main`, guarda el resultado de cada llamada en variables inmutables `resultOne` y `resultTwo` e imprime sus valores.

### Clases y métodos introducidos
- **Ausencia de tipo de retorno:** si no se escribe `: Tipo`, la función devuelve `Unit` implícitamente.
- `Unit`: tipo con un único valor (análogo funcional a `void` de Java, pero **es un tipo real**), por lo que se puede asignar a una variable.

#### Ejemplo simple de funcionamiento
```kotlin
fun saludar() {          // sin tipo de retorno explícito
    println("hola")
}

fun main() {
    val resultado = saludar()   // válido: saludar() devuelve Unit
    println(resultado)          // imprime: kotlin.Unit
}
```

### Código fuente (`Ejercicio3.3/src/Main.kt`)

```kotlin
fun printWelcomeMessage(user: String) {
    println("Hola, bienvenido $user")
}

fun logActivity() {
    println("Activity logged")
}

fun main() {
    val resultOne = printWelcomeMessage("Daniel")
    val resultTwo = logActivity()
    println("$resultOne, $resultTwo")
}
```

### Explicación paso a paso
1. **`Unit` inferido:** ninguna de las dos funciones declara tipo de retorno, así que el compilador asigna `Unit` automáticamente (equivale a escribirlas como `fun logActivity(): Unit`).
2. **Una llamada con efecto secundario también es una expresión:** `val resultOne = printWelcomeMessage(...)` compila porque la llamada devuelve un valor (`Unit`), aunque ese valor no sirva de nada.
3. **Salida:** al interpolar, `Unit` se imprime como su `toString()`: `kotlin.Unit, kotlin.Unit`. El mensaje de bienvenida y el log aparecen **antes**, porque las funciones los imprimen en el momento de la llamada.
4. **Diferencia con Java:** `void` es una palabra reservada que significa "nada" y no se puede asignar; `Unit` es un objeto, lo que mantiene uniforme la regla *toda expresión Kotlin devuelve algo*.

---

## Ejercicio 3.4 · throw como rama de una expresión (tipo Nothing)

> [!question] Enunciado
> Define una función `validateValue` que acepte un único parámetro `inputNumber` de tipo `Int` y devuelva un `String`. Dentro, utiliza una expresión `if`: si `inputNumber` es mayor que cero, retorna `"Value is positive"`; si no, debe lanzar una `IllegalArgumentException` con el mensaje `"Input must be greater than zero"`. Asegúrate de que el `if` se use como una expresión y que la excepción actúe como la rama `else`.

### Clases y métodos introducidos
- `throw IllegalArgumentException(mensaje)`: lanza una excepción de forma explícita.
- `IllegalArgumentException`: excepción estándar para argumentos que violan una restricción de la función.
- **`throw` es una expresión de tipo `Nothing`:** como nunca produce valor (abandona el flujo), es válida en cualquier rama de una expresión, incluido un `else` donde se espera un `String`.

#### Ejemplo simple de funcionamiento
```kotlin
fun mitad(n: Int): Int =
    if (n % 2 == 0) n / 2
    else throw IllegalArgumentException("n debe ser par")

fun main() {
    println(mitad(8))      // 4
    println(mitad(7))      // lanza la excepción
}
```

### Código fuente (`Ejercicio3.4/src/Main.kt`)

```kotlin
fun validateValue(inputNumber: Int): String {
    if (inputNumber > 0) return "Value is positive"
    else throw IllegalArgumentException("Input must be greater than zero")
}

fun main() {
    println(validateValue(4))
    println(validateValue(0))
}
```

### Explicación paso a paso
1. **Contrato de la función:** la firma promete un `String`. La rama `then` lo cumple (`return "Value is positive"`); la rama `else` no lo incumple porque `throw` **no retorna nunca**: su tipo `Nothing` es subtipo de todo, así que el compilador acepta el `if` completo.
2. **`return` también es `Nothing`:** por eso `if (...) return x else throw ...` es simétrico: ambas ramas abandonan la función.
3. **Comportamiento en `main`:** `validateValue(4)` imprime `Value is positive`; `validateValue(0)` lanza la excepción y, al no haber `try/catch`, termina el programa con el mensaje `Input must be greater than zero`.

---

## Ejercicio 3.5 · Función de expresión única: año bisiesto

> [!question] Enunciado
> Realiza un programa en el que definas una función `isLeapYear` que reciba un año e indique si es bisiesto o no, calculándolo mediante una única expresión. Prueba la función con distintos valores.

### Clases y métodos introducidos
- **Cuerpo de expresión única:** `fun f(x: T): R = expresión` — no hay `return` explícito ni llaves; el valor de la expresión es el retorno.
- `intArrayOf(...)`: crea un `IntArray` (array de primitivos, sin *boxing*).
- **`if` como expresión:** `val result = if (cond) "a" else "b"` — asigna el valor de la rama elegida.

#### Ejemplo simple de funcionamiento
```kotlin
fun dobleDe(x: Int): Int = x * 2      // una sola expresión, sin return

fun main() {
    val etiqueta = if (dobleDe(3) > 5) "grande" else "pequeña"
    println(etiqueta)                  // grande
}
```

### Código fuente (`Ejercicio3.5/src/Main.kt`)

```kotlin
fun isLeapYear(year: Int): Boolean = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)

fun main() {
    val TestYear = intArrayOf(
        2024, // Bisiesto: divisible por 4 y no por 100
        2025, // No bisiesto: no divisible por 4
        2000, // Bisiesto: divisible por 400
    )

    for (year in TestYear) {
        val result = if (isLeapYear(year)) "es bisiesto" else "no es bisiesto"
        println("El anio $year $result")
    }
}
```

### Explicación paso a paso
1. **La regla bisiesta en una expresión:** divisible por 4 **y no** por 100, **o** divisible por 400. Los paréntesis documentan los dos bloques lógicos; el `&&` y `||` cortocircuitan de izquierda a derecha.
2. **Inferencia:** con cuerpo de `=` el tipo de retorno se infiere de la expresión (aquí `Boolean`); en este caso igual se declaró explícito, que es lo recomendable en funciones públicas.
3. **`if`-expresión en el bucle:** `val result = if (...) ... else ...` sustituye al `if/else` con dos `println`; solo hay que escribir la salida una vez.
4. **Banco de pruebas:** los tres años elegidos no son aleatorios — cubren las tres ramas de la fórmula (regla general, caso de exclusión por 100 y excepción de los 400).

---

## Ejercicio 3.6 · Sobrecarga de funciones: sumValues

> [!question] Enunciado
> Define tres funciones sobrecargadas en el ámbito principal, todas con el nombre `sumValues`: la primera acepta dos `Int` y retorna su suma como `Int`; la segunda acepta un array de `Double` llamado `doubleValues` y retorna la suma como `Double`; la tercera acepta un `String` `prefix` y un `Int` `count` y retorna una `String` con el `prefix` repetido `count` veces. En `main`, prueba cada versión y guarda los resultados en `resultInt`, `resultDouble` y `resultString`.

### Clases y métodos introducidos
- **Sobrecarga (*overloading*):** varias funciones con el mismo nombre y **distinta firma**.
- **Firma:** nombre + número y tipos de parámetros. El tipo de retorno **no** forma parte de la firma.
- `doubleArrayOf(...)`: crea un `DoubleArray`.
- Ligadura estática: qué versión se llama se decide **en tiempo de compilación** según los argumentos.

#### Ejemplo simple de funcionamiento
```kotlin
fun decirHola() = println("Hola")
fun decirHola(nombre: String) = println("Hola, $nombre")
fun decirHola(nombre: String, formal: Boolean) =
    println(if (formal) "Buenas tardes, $nombre" else "Hola, $nombre")

fun main() {
    decirHola()                 // versión sin parámetros
    decirHola("Ana")            // versión con String
    decirHola("Ana", true)      // versión con String + Boolean
}
```

### Código fuente (`Ejercicio3.6/src/Main.kt`)

```kotlin
fun sumValues(firstNumber: Int, secondNumber: Int): Int {
    return firstNumber + secondNumber
}

fun sumValues(doubleValues: DoubleArray): Double {
    var suma = 0.0
    for (value in doubleValues) {
        suma += value
    }
    return suma
}

fun sumValues(prefix: String, count: Int): String {
    var sumaCadena: String = ""
    for (i in 0 ..< count) {
        sumaCadena += prefix
    }
    return sumaCadena
}

fun main() {
    val resultInt = sumValues(3, 2)
    val resultDouble = sumValues(doubleArrayOf(2.3, 3.2))
    val resultString = sumValues("A-", 3)

    println(resultInt)
    println(resultDouble)
    println(resultString)
}
```

### Explicación paso a paso
1. **Tres firmas distintas conviven:** `(Int, Int)`, `(DoubleArray)` y `(String, Int)` — el compilador desambigua cada llamada de `main` por los tipos reales de los argumentos.
2. **La tercera versión "suma" cadenas:** Kotlin **no permite sobrecargar solo el tipo de retorno**, pero sí reutilizar el nombre para operaciones conceptualmente similares con parámetros distintos.
3. **`for (i in 0 ..< count)` + `+=`:** repite el prefijo concatenando sobre una variable `var` (`""` + "A-" + "A-" + "A-" → `"A-A-A-"`). Es el equivalente manual de `prefix.repeat(count)`.
4. **Convención frente a Java:** en Java la sobrecarga es la única vía para tener `sum(int,int)` y `sum(double[])`; en Kotlin suele sustituirse por *valores por defecto* y `varargs` (ejercicios 3.7 y 3.9), pero sigue siendo necesaria cuando cambian los tipos.

---

## Ejercicio 3.7 · Parámetros con valores por defecto

> [!question] Enunciado
> Define una función `configurePrintJob` que acepte tres parámetros inmutables: `fileName` de tipo `String` sin valor por defecto (obligatorio), `pageSize` de tipo `Int` con valor por defecto `200`, e `isColorMode` de tipo `Boolean` con valor por defecto `false`. Dentro, imprime una línea con el valor de cada parámetro. En `main`, realiza cuatro llamadas: solo el obligatorio; obligatorio + `pageSize` en orden; el obligatorio más `isColorMode` con argumento nombrado (dejando `pageSize` por defecto); y los tres completos.

### Clases y métodos introducidos
- **Valor por defecto:** `param: Tipo = valor` en la firma; la llamada puede omitirlo.
- **Argumentos con nombre:** `isColorMode = true` en el lugar del valor posicional.

#### Ejemplo simple de funcionamiento
```kotlin
fun cafe(tamano: String = "pequeño", azucar: Boolean = false) {
    println("Café $tamano, azucar=$azucar")
}

fun main() {
    cafe()                                    // tamaño y azúcar por defecto
    cafe("grande")                            // cambia solo el primero
    cafe(azucar = true)                       // con nombre: saltarse uno
    cafe("mediano", true)                     // los dos
}
```

### Código fuente (`Ejercicio3.7/src/Main.kt`)

```kotlin
fun configurePrintJob(
    fileName: String,
    pageSize: Int = 200,
    isColorMode: Boolean = false,
) {
    println("$fileName, $isColorMode, $pageSize")
}

fun main() {
    configurePrintJob("NombreDeEjemplo")
    configurePrintJob("NombreDeEjemplo2", 120)
    configurePrintJob("NombreDeEjemplo3", isColorMode = true)
    configurePrintJob("NombreDeEjemplo4", 230, true)
}
```

### Explicación paso a paso
1. **Orden obligatorio → opcionales:** `fileName` va primero porque en Kotlin los parámetros sin valor por defecto deben declararse **antes** que los que lo tienen; así las llamadas posicionales siguen siendo posibles. (Ojo: el `println` los imprime en orden `fileName, isColorMode, pageSize`, no en el orden de la firma.)
2. **Llamada 1:** `("…")` → `pageSize=200`, `isColorMode=false` (defectos).
3. **Llamada 2:** el segundo argumento posacional encaja en `pageSize=120`; el tercero queda por defecto.
4. **Llamada 3:** para saltarse `pageSize` y tocar solo `isColorMode` hay que usar **argumento nombrado** (`isColorMode = true`); posicionalmente ese `true` iría a `pageSize` y no compilaría.
5. **Llamada 4:** las tres posiciones cubiertas, los defectos no intervienen. Sustituye a las 3-4 sobrecargas que exigiría Java.

---

## Ejercicio 3.8 · Argumentos con nombre y mezcla de estilos

> [!question] Enunciado
> Define la función `generateReport(reportTitle: String, startDate: String, endDate: String = "Today", detailedView: Boolean = true, watermarkText: String? = null)` que imprima todos sus parámetros separados por comas. En `main`, llámala tres veces: (1) `reportTitle` y `startDate` posicionales y `watermarkText` por nombre, con el resto por defecto; (2) los tres `String` en orden invertido usando solo argumentos nombrados; (3) mezcla: dos posicionales y `detailedView` por nombre.

### Clases y métodos introducidos
- **Argumentos nombrados sin orden fijo:** cuando un parámetro se pasa con nombre, el orden de escritura puede invertirse (solo en llamadas Kotlin).
- **Regla de la mezcla:** todo argumento posicional debe ir **antes** del primer nombrado.
- **Default con tipo nullable:** `watermarkText: String? = null` — un opcional cuyo "no informado" se distingue de cadena vacía.

#### Ejemplo simple de funcionamiento
```kotlin
fun ficha(nombre: String, edad: Int, ciudad: String = "unknown") {
    println("$nombre, $edad, $ciudad")
}

fun main() {
    ficha(ciudad = "Riga", nombre = "Ada", edad = 36)  // orden invertido: OK (todos con nombre)
    // ficha(ciudad = "Riga", "Ada")                   // ERROR: posicional después de nombrado
}
```

### Código fuente (`Ejercicio3.8/src/Main.kt`)

```kotlin
fun generateReport(
    reportTitle: String,
    startDate: String,
    endDate: String = "Today",
    detailedView: Boolean = true,
    watermarkText: String? = null,
) {
    println("$reportTitle, $startDate, $endDate, $detailedView, $watermarkText")
}

fun main() {
    generateReport("Titulo1", "Today", watermarkText = "Dan")
    generateReport(endDate = "Tomorrow", startDate = "Today", reportTitle = "Titulo2")
    generateReport("Titulo3", "Yesterday", detailedView = true)
}
```

### Explicación paso a paso
1. **Llamada 1:** dos posicionales llenan `reportTitle` y `startDate`; el salto hasta `watermarkText` se hace con nombre, y `endDate`/`detailedView` conservan sus defectos → `"Titulo1, Today, Today, true, Dan"`.
2. **Llamada 2:** al estar **todos** los argumentos nombrados, el orden de escritura es irrelevante; `endDate` va primero pese a ser el tercero en la firma, y `watermarkText` queda en `null` → `"Titulo2, Today, Tomorrow, true, null"`.
3. **Llamada 3:** posicionales primero y el nombrado al final respeta la regla de mezcla → `"Titulo3, Yesterday, Today, true, null"` (el `true` explícito coincide con el defecto, pero obliga a escribirlo el enunciado).
4. **Por qué `watermarkText: String? = null`:** patrón habitual — un valor opcional donde `null` significa "sin marca de agua", y cualquier cadena (incluso `""`) significa "activarla".

---

## Ejercicio 3.9 · Parámetro vararg no posicionado al final

> [!question] Enunciado
> Define una función `analyzeScores` que acepte, en este orden: `minThreshold: Int`, `scores` marcado como `vararg Int`, y `sortAscending: Boolean = true`. Dentro, imprime `minThreshold` e itera `scores` imprimiendo cada puntuación. En `main`, haz dos llamadas: la primera con `minThreshold` y cuatro puntuaciones (defectos activados); la segunda con `minThreshold`, dos puntuaciones y `sortAscending = false` **con nombre**, para que el compilador no lo confunda con una puntuación más.

> [!warning] Detalle del código real
> En la fuente la función se escribió `analyizeScores` (con `i` de más) en lugar de `analyzeScores`. No es error de compilación — es un *typo* que sobrevive porque definición y llamadas coinciden. Aquí se reproduce tal cual está en el repositorio.

### Clases y métodos introducidos
- `vararg nombre: Tipo`: parámetro de aridad variable; dentro de la función `scores` es un `IntArray`.
- **`vararg` no último:** si detrás hay otro parámetro (`sortAscending`), ese último **debe pasarse con nombre** o tener default; si no, el compilador no sabe dónde termina la lista variable.
- `String.repeat(n)`: devuelve la cadena repetida `n` veces.

#### Ejemplo simple de funcionamiento
```kotlin
fun etiqueta(prefijo: String, vararg partes: String, sufijo: String = "!") {
    println("$prefijo ${partes.joinToString("+")} $sufijo")
}

fun main() {
    etiqueta("Lote", "A", "B", "C")                    // sufijo por defecto
    etiqueta("Lote", "A", "B", sufijo = "?")           // sufijo con nombre
    println("-".repeat(5))                             // "-----"
}
```

### Código fuente (`Ejercicio3.9/src/Main.kt`)

```kotlin
fun analiyzeScores(
    minThreshold: Int,
    vararg scores: Int,
    sortAscending: Boolean = true,
) {
    println("minThreshold: $minThreshold")
    println("sortAscending: $sortAscending")
    print("scores: ")

    for (score in scores) {
        print("$score ")
    }

    println("\n" + "-".repeat(30))

}

fun main() {
    analiyzeScores(5, 4, 3, 2, 1)
    analiyzeScores(4, 3, 2, sortAscending = false)
}
```

### Explicación paso a paso
1. **Ligadura de la llamada 1:** `5` va a `minThreshold` (posicional, antes del vararg) y `4, 3, 2, 1` se acumulan en `scores`; `sortAscending` usa el defecto `true`.
2. **Ligadura de la llamada 2:** `4` es el umbral, y `3, 2` las puntuaciones… hasta que aparece `sortAscending = false` con nombre, lo que **corta** la recolección del vararg. Sin el nombre, un último argumento posicional sería ambiguo: el compilador no puede decidir si pertenece al `vararg` o a `sortAscending`, así que exige nombre.
3. **Recorrido del vararg:** `for (score in scores)` funciona igual que sobre un array normal porque `scores` **es** un `IntArray`.
4. **`"\n" + "-".repeat(30)`:** separador de 30 guiones precedido de salto de línea, para delimitar visualmente cada bloque de salida.

---

## Ejercicio 3.10 · Spread operator (*) sobre varargs

> [!question] Enunciado
> Escribe una función `calculateAverage` que reciba una lista variable de números enteros y calcule su media aritmética; `main()` la llamará con los valores de un `IntArray` definido previamente. Define además `combineData(dataChunks: vararg Int)` que imprima cada valor en una línea. En `main`, declara `initialSet` (10, 20, 30) y `extraSet` (40, 50) y llama a `combineData` pasándole, en una sola línea, todos los elementos de ambos arrays.

### Clases y métodos introducidos
- **Spread operator `*`:** desempaqueta un array en argumentos individuales de un `vararg` (`f(*arr)` ≡ `f(arr[0], arr[1], …)`).
- Varios `*` en una misma llamada: se concatenan en orden.
- **División entera:** `Int / Int` en Kotlin (como en Java) **trunca** el resultado.

#### Ejemplo simple de funcionamiento
```kotlin
fun suma(vararg nums: Int): Int {
    var total = 0
    for (n in nums) total += n
    return total
}

fun main() {
    val datos = intArrayOf(1, 2, 3)
    println(suma(*datos))              // 6  (equivale a suma(1, 2, 3))
    println(suma(0, *datos, 99))       // 105 (mezcla posiciones y spreads)
}
```

### Código fuente (`Ejercicio3.10/src/Main.kt`)

```kotlin
fun calculateAverage(vararg numbers: Int): Int {
    var sumaNotas: Int = 0

    for (number in numbers) {
        sumaNotas += number
    }

    return sumaNotas / numbers.size
}

fun combineData(vararg dataChuncks: Int) {
    for (dataChunk in dataChuncks) {
        println(dataChunk)
    }
}

fun main() {
    val arrayNotas: IntArray = intArrayOf(3, 3, 5)
    println("La media de es ${calculateAverage(*arrayNotas)}")
    val initialSet: IntArray = intArrayOf(10, 20, 30)
    val extraSet: IntArray = intArrayOf(40, 50)
    combineData(*initialSet, *extraSet)
}
```

### Explicación paso a paso
1. **`calculateAverage(*arrayNotas)`:** el spread convierte el `IntArray` en la secuencia `3, 3, 5` que recoge `vararg numbers`. Sin la `*` habría un error de tipos (`IntArray` no es `Int`).
2. **Media entera:** `(3+3+5) / 3 = 11 / 3 = 3` — división entre `Int`, se pierde el decimal. Para una media exacta harían falta `Double` o `.average()`.
3. **Dos spreads seguidos:** `combineData(*initialSet, *extraSet)` imprime `10, 20, 30, 40, 50` uno por línea; el orden de los argumentos es el orden de aparición.
4. **Typo heredado de la fuente:** el parámetro se llama `dataChuncks` (con `n` de más) tanto en la firma como en el bucle; Kotlin no lo detecta porque definición y uso coinciden.
5. **Nota de la librería estándar:** pasar una `List` a un `vararg` exige antes convertirla (`*lista.toTypedArray()`); con `IntArray`/`DoubleArray` el `*` funciona directamente.

---

## Ejercicio 3.11 · Funciones infijas (infix)

> [!question] Enunciado
> Escribe una clase `De0a100` que represente un rango de enteros de 0 a 100 y defina una función infija `contains` que verifique si un número está dentro del rango. Define otra clase simple `ActionExecutor` (sin propiedades ni constructor) con una función `infix perform(actionName: String)` que imprima `"Executing action: "` seguido del nombre. En `main`, crea una instancia de `ActionExecutor` y llama a `perform` dos veces para la acción `"Cleanup"`: con notación estándar (punto y paréntesis) y con notación infija.

### Clases y métodos introducidos
- `infix fun`: permite llamar a la función **sin punto ni paréntesis**: `objeto nombre argumento`.
- **Requisitos de `infix`:** ser método (de clase o de extensión), tener **exactamente un** parámetro, y que el parámetro no sea `vararg` ni tenga valor por defecto.
- Convención de nombres de clases: **PascalCase** (`De0a100`), no `de0a100`.

#### Ejemplo simple de funcionamiento
```kotlin
class Mensajeria {
    infix fun enviar(texto: String) {
        println("Enviado: $texto")
    }
}

fun main() {
    val m = Mensajeria()
    m.enviar("Hola")      // notación estándar
    m enviar "Hola"       // notación infija (idéntica llamada)
}
```

### Código fuente (`Ejercicio3.11/src/Main.kt`)

```kotlin
class de0a100 {
    val rango: IntRange = 0..100

    infix fun contains(value: Int): Boolean {
        return value in rango
    }
}

class ActionExecutor {
    infix fun perform(actionName: String) {
        println("Executing action: $actionName")
    }
}

fun main() {
    val executionInstance = ActionExecutor()
    executionInstance.perform("Cleanup")
    executionInstance perform "Cleanup"
}
```

### Explicación paso a paso
1. **`infix fun contains(value: Int)`:** al llamarse `contains`, además de la forma infija (`rangoDe0a100 contains 42`) queda habilitado el **operador** `in`: `42 in rangoDe0a100` se traduce a `rangoDe0a100.contains(42)`. Así se implementan rangos y colecciones propios compatibles con `in`.
2. **Las dos llamadas son la misma llamada:** `executionInstance.perform("Cleanup")` y `executionInstance perform "Cleanup"` producen salida idéntica; la infija es azúcar sintáctica para expresiones que se leen como frases.
3. **El `main` no ejercita `de0a100`:** queda solo definida la clase. Prueba mínima: `val d = de0a100(); println(42 in d); println(d contains 101)` → `true`, `false`.
4. **Infracción de convención detectada:** la fuente declara `class de0a100` en minúscula (el enunciado pedía `De0a100`). Kotlin no lo prohíbe, pero rompe PascalCase del resto de clases y se recomienda corregirlo.
5. **Ejemplos de infix ya conocidas:** `to` (`"a" to 1`), `step` (`1 step 2`), `in` — todas cumplen los tres requisitos.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Retornos anticipados | `if (cond) return x` | Cada `return` corta la función; patrón de cláusulas de guarda. |
| Multilínea + coma final | `p: Int,` (última línea) | Diffs Git limpios: añadir parámetro = añadir línea. |
| Tipo Unit | `fun f() { }` | Sin tipo de retorno explícito → `Unit`, valor real asignable e imprimible. |
| Tipo Nothing | `throw E(...)` | Expresión que nunca retorna; válida como rama `else` de cualquier expresión. |
| Expresión única | `fun f(): T = expr` | El valor de la expresión es el retorno; `if`-expresión asignable. |
| Sobrecarga | mismo nombre, otra firma | Ligadura estática; el retorno no distingue versiones. |
| Valores por defecto | `p: T = valor` | Obligatorios antes que opcionales; sustituyen sobrecargas Java. |
| Argumentos nombrados | `p = valor` | Orden libre si todos son nombrados; posicionales solo al principio. |
| vararg | `vararg p: T` | Es un array dentro; si no es el último, lo posterior exige nombre. |
| Spread | `f(*arr)` | Desempaqueta arrays en argumentos; combinable varios por llamada. |
| infix | `infix fun p(x: T)` | Sin punto ni paréntesis; 1 parámetro, no vararg ni default. |

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Retornos anticipados | `if (cond) return x` | Cada `return` corta la función; patrón de cláusulas de guarda. |
| Multilínea + coma final | `p: Int,` (última línea) | Diffs Git limpios: añadir parámetro = añadir línea. |
| Tipo Unit | `fun f() { }` | Sin tipo de retorno explícito → `Unit`, valor real asignable e imprimible. |
| Tipo Nothing | `throw E(...)` | Expresión que nunca retorna; válida como rama `else` de cualquier expresión. |
| Expresión única | `fun f(): T = expr` | El valor de la expresión es el retorno; `if`-expresión asignable. |
| Sobrecarga | mismo nombre, otra firma | Ligadura estática; el retorno no distingue versiones. |
| Valores por defecto | `p: T = valor` | Obligatorios antes que opcionales; sustituyen sobrecargas Java. |
| Argumentos nombrados | `p = valor` | Orden libre si todos son nombrados; posicionales solo al principio. |
| vararg | `vararg p: T` | Es un array dentro; si no es el último, lo posterior exige nombre. |
| Spread | `f(*arr)` | Desempaqueta arrays en argumentos; combinable varios por llamada. |
| infix | `infix fun p(x: T)` | Sin punto ni paréntesis; 1 parámetro, no vararg ni default. |

