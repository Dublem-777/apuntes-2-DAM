---
asignatura: PMDM
tema: 10
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/kotlin-funcional
  - DAM/pmdm/ejercicios
---

# Bloque 14 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[07 - POO II]] · [[09 - Genéricos]] · [[10 - Programación funcional]]
> Bloque anterior: [[Ejercicios Bloque 13]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque14/`

> [!note] Sobre las soluciones
> - Los ejercicios 1–4 son los mismos enunciados que el 7.8–7.11 de [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2|el boletín 7]]. Los ejercicios 5, 6, 7 y 9 son el 10.6, 10.10, 10.1 y 10.11 de [[10.1 - Ejercicios 10 Programación funcional|el boletín 10]]. El código parte de esas soluciones.
> - El ejercicio 7 (`testBoth`) ya salió en el [[Ejercicios Bloque 12#Ejercicio 4 · Función de orden superior `testBoth`|Bloque 12]]: aquí se prueba con otras condiciones.
> - El ejercicio 8 (`calculateAggregate`) no está en ningún boletín: solución nueva.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque14/Ejercicio14.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas y los mensajes de error son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · *Sealed class* `Payment`]]
- [[#Ejercicio 2 · *Sealed class* `UserAlert` y `when` exhaustivo]]
- [[#Ejercicio 3 · *Sealed interface* `ApiResponse`]]
- [[#Ejercicio 4 · *Inline value class* `PhoneNumber`]]
- [[#Ejercicio 5 · `fun interface` `DataValidator`]]
- [[#Ejercicio 6 · Función `inline` y *non-local return*]]
- [[#Ejercicio 7 · `testBoth` con dos condiciones]]
- [[#Ejercicio 8 · Función genérica `calculateAggregate`]]
- [[#Ejercicio 9 · Funciones `hacerCon1` a `hacerCon9`]]

---

## Ejercicio 1 · *Sealed class* `Payment`

> [!question] Enunciado
> Define una *sealed class* llamada `Payment` para representar diferentes formas de pago en una aplicación, con las siguientes subclases:
>
> - `CreditCardPayment`, con las propiedades `cardNumber`, `cardHolder` y `amount`.
> - `PaypalPayment`, con las propiedades `email` y `amount`.
> - `CashPayment`, con la propiedad `amount`.
>
> Luego, define una función `processPayment(payment: Payment)` que reciba un objeto de tipo `Payment` y procese el pago según su tipo. La función debe usar una estructura `when` para manejar los diferentes tipos de pago e imprimir un mensaje específico para cada uno.
>
> Además, implementa una función `main` que cree una instancia de cada tipo de pago (`CreditCardPayment`, `PaypalPayment` y `CashPayment`) y llame a `processPayment` para cada una.

### Clases y métodos introducidos
- `sealed class`: una clase abstracta cuyas subclases son **todas conocidas** por el compilador, porque tienen que declararse en el mismo paquete y módulo (en la práctica, el mismo archivo). Nadie puede añadir más desde fuera.
- **Subclases anidadas**: declaradas dentro de `Payment`, se usan como `Payment.CashPayment(…)`. Son `data class` para tener `toString`, `equals`…
- `when (payment) { is … -> }`: con una *sealed class*, el compilador sabe si has cubierto todos los subtipos.
- **Smart cast**: dentro de la rama `is Payment.PaypalPayment`, `payment` ya se trata como `PaypalPayment` y se puede leer `payment.email`.

> **Términos explicados:** [[07 - POO II#Sealed classes|*sealed classes*]] · [[07 - POO II#Data class|`data class`]] · [[02 - Jerarquia de tipos#11. Comprobación de tipo|`is` y *smart cast*]]

#### Ejemplo simple de funcionamiento
```kotlin
sealed class Shape {
    data class Circle(val radius: Double) : Shape()
    data class Square(val side: Double) : Shape()
}

fun area(shape: Shape): Double = when (shape) {
    is Shape.Circle -> 3.14 * shape.radius * shape.radius
    is Shape.Square -> shape.side * shape.side
}
```

### Código fuente (`Ejercicio14.1/src/Main.kt`)

```kotlin
sealed class Payment {
    data class CreditCardPayment(
        val cardNumber: String,
        val cardHolder: String,
        val amount: Double,
    ) : Payment()

    data class PaypalPayment(val email: String, val amount: Double) : Payment()

    data class CashPayment(val amount: Double) : Payment()
}

fun processPayment(payment: Payment) {
    // Gracias al smart cast, dentro de cada rama se accede a las propiedades del subtipo
    when (payment) {
        is Payment.CreditCardPayment ->
            println("Tarjeta de ${payment.cardHolder} (**** ${payment.cardNumber.takeLast(4)}): ${payment.amount} €")
        is Payment.PaypalPayment ->
            println("PayPal de ${payment.email}: ${payment.amount} €")
        is Payment.CashPayment ->
            println("Pago en efectivo: ${payment.amount} €")
    }
}

fun main() {
    processPayment(Payment.CreditCardPayment("4111222233334444", "Ada Lovelace", 25.0))
    processPayment(Payment.PaypalPayment("ada@example.com", 15.5))
    processPayment(Payment.CashPayment(10.0))
}
```

### Explicación paso a paso
1. **`Payment`:** es `sealed`, así que solo existen los tres tipos de pago declarados dentro. Cada subclase hereda de `Payment()` y tiene solo las propiedades que le tocan.
2. **`processPayment`:** el `when` comprueba con `is` de qué tipo es el pago. En cada rama, el *smart cast* permite leer las propiedades de ese tipo concreto.
3. **Tarjeta:** por seguridad, solo se muestran los 4 últimos dígitos con `takeLast(4)`, como en un ticket de compra real.
4. **`main()`:** crea un pago de cada tipo y los procesa.

> [!tip] Prueba
> ```text
> Tarjeta de Ada Lovelace (**** 4444): 25.0 €
> PayPal de ada@example.com: 15.5 €
> Pago en efectivo: 10.0 €
> ```

> [!note]- 🧠 Por qué funciona
> - Una *sealed class* es como un menú del día con platos fijos: el camarero (el compilador) sabe exactamente qué platos hay. Si mañana se añade `BizumPayment`, el compilador avisará en cada `when` que no lo tenga en cuenta.
> - Con una clase `open` normal, cualquiera podría crear subclases nuevas en otro archivo, y el compilador no podría saber si el `when` las cubre todas.

---

## Ejercicio 2 · *Sealed class* `UserAlert` y `when` exhaustivo

> [!question] Enunciado
> Define una `enum class` llamada `Priority` con tres valores posibles y ninguna propiedad adicional: `LOW`, `MEDIUM` y `HIGH`.
>
> Define una *sealed class* llamada `UserAlert`. **Dentro del mismo archivo**, define las siguientes subclases directas de `UserAlert`:
>
> - Una `data class` llamada `EmailAlert` con una propiedad `sender` (`String`) y una propiedad `priority` (`Priority`).
> - Una `data class` llamada `SmsAlert` con una propiedad `phoneNumber` (`String`) y una propiedad `priority` (`Priority`).
> - Un `object` llamado `SystemMaintenance`.
>
> Define una función *top-level* llamada `processAlert` que acepte un parámetro `alert` de tipo `UserAlert` y use una expresión `when` **exhaustiva** para imprimir un mensaje:
>
> - Si es `EmailAlert`, imprime el remitente y su prioridad.
> - Si es `SmsAlert`, imprime el número y su prioridad.
> - Si es `SystemMaintenance`, imprime `"Scheduled downtime starting now."`.
>
> **No debe haber rama `else`.** En la función `main`, crea una instancia de cada subclase de `UserAlert` y pásala a `processAlert`.

### Clases y métodos introducidos
- **Subclases en el nivel superior del archivo**: a diferencia del ejercicio 1, aquí van fuera de las llaves de `UserAlert`, y se usan sin prefijo (`EmailAlert(…)`). Siguen siendo «selladas» porque están en el mismo archivo.
- `object SystemMaintenance : UserAlert()`: un subtipo que no necesita datos, así que hay **un solo objeto**. En el `when` se compara directamente (`SystemMaintenance ->`), sin `is`.
- **`when` exhaustivo sin `else`**: como el compilador conoce todos los subtipos, no hace falta `else`. Si falta alguno, no compila.

> **Términos explicados:** [[07 - POO II#Sealed classes|*sealed classes* y `when` exhaustivo]] · [[07 - POO II#Enumeraciones|enumeraciones]] · [[06 - POO I#16. Declaraciones de objetos|`object`]]

#### Ejemplo simple de funcionamiento
```kotlin
sealed class TrafficLight
object Red : TrafficLight()
object Green : TrafficLight()

fun action(light: TrafficLight) = when (light) {   // sin else
    Red -> "Para"
    Green -> "Avanza"
}
```

### Código fuente (`Ejercicio14.2/src/Main.kt`)

```kotlin
enum class Priority { LOW, MEDIUM, HIGH }

sealed class UserAlert

// Subclases directas, en el mismo archivo que UserAlert
data class EmailAlert(val sender: String, val priority: Priority) : UserAlert()

data class SmsAlert(val phoneNumber: String, val priority: Priority) : UserAlert()

object SystemMaintenance : UserAlert()

fun processAlert(alert: UserAlert) {
    // when exhaustivo: cubre todos los subtipos, así que no necesita else
    when (alert) {
        is EmailAlert -> println("Email de ${alert.sender} (prioridad ${alert.priority})")
        is SmsAlert -> println("SMS al ${alert.phoneNumber} (prioridad ${alert.priority})")
        SystemMaintenance -> println("Scheduled downtime starting now.")
    }
}

fun main() {
    processAlert(EmailAlert("admin@example.com", Priority.HIGH))
    processAlert(SmsAlert("612345678", Priority.MEDIUM))
    processAlert(SystemMaintenance)
}
```

### Explicación paso a paso
1. **`Priority`:** un enum simple, solo con las tres constantes, como pide el enunciado.
2. **`UserAlert`:** la clase sellada, sin cuerpo. Sus tres subtipos se declaran justo debajo, en el mismo archivo.
3. **`EmailAlert` y `SmsAlert`:** `data class` con sus dos propiedades. **`SystemMaintenance`:** un `object`, porque un aviso de mantenimiento no tiene datos que lo distingan de otro.
4. **`processAlert`:** las dos primeras ramas usan `is` (son clases con muchos objetos posibles). La tercera compara con el objeto único `SystemMaintenance`. No hay `else`.
5. **`main()`:** una alerta de cada tipo.

> [!tip] Prueba
> ```text
> Email de admin@example.com (prioridad HIGH)
> SMS al 612345678 (prioridad MEDIUM)
> Scheduled downtime starting now.
> ```
> Si se borra la rama `SystemMaintenance ->`, **no compila**. Error real de `kotlinc`: `'when' expression must be exhaustive. Add the 'SystemMaintenance' branch or an 'else' branch.`

> [!note]- 🧠 Por qué funciona
> - Poner `else` sería como decir «y cualquier otra cosa»: el compilador ya no podría avisarte si mañana añades un subtipo nuevo. Sin `else`, cada subtipo nuevo te obliga a decidir qué hacer con él.
> - `SystemMaintenance` es un `object`, así que solo existe uno. Por eso basta con compararlo (`SystemMaintenance ->`), sin preguntar por su tipo.
> - Imprimir `alert.priority` muestra el `name` de la constante (`HIGH`), porque es lo que devuelve el `toString()` de un enum.

> [!tip] `object` o `data object`
> El boletín usa `data object SystemMaintenance`, que solo cambia cómo se imprime: `println(SystemMaintenance)` da `SystemMaintenance` en vez de algo como `SystemMaintenance@1b6d3586`. El enunciado pide un `object`, y para el `when` los dos funcionan igual ([[07 - POO II#Data object declarations|ver *data object*]]).

---

## Ejercicio 3 · *Sealed interface* `ApiResponse`

> [!question] Enunciado
> Define una *sealed interface* llamada `ApiResponse` para representar diferentes tipos de respuestas de una API, con las siguientes implementaciones:
>
> - Clase `SuccessResponse`, con la propiedad `data`, que contiene el texto de la respuesta.
> - Clase `ErrorResponse`, con las propiedades `errorCode` (código de error) y `errorMessage` (mensaje de error).
> - `object Loading`, que representa que se está obteniendo la respuesta.
>
> Luego, define una función `handleResponse(response: ApiResponse)` que maneje la respuesta según su tipo con una estructura `when`, imprimiendo un mensaje específico para cada uno.
>
> Implementa una función `main` que cree una instancia de cada tipo de respuesta (`SuccessResponse`, `ErrorResponse` y `Loading`) y llame a `handleResponse` para cada una.

### Clases y métodos introducidos
- `sealed interface`: igual que una *sealed class* (los tipos que la implementan son conocidos), pero es una **interfaz**: las clases la implementan sin paréntesis (`: ApiResponse`) y una clase puede implementar varias.
- `object Loading : ApiResponse`: un estado sin datos, con un único objeto.

> **Términos explicados:** [[07 - POO II#Sealed interfaces|*sealed interfaces*]] · [[07 - POO II#Sealed class vs enum|*sealed* frente a `enum`]]

#### Ejemplo simple de funcionamiento
```kotlin
sealed interface Result
data class Ok(val value: Int) : Result
data class Failure(val reason: String) : Result

fun describe(result: Result) = when (result) {
    is Ok -> "Valor: ${result.value}"
    is Failure -> "Fallo: ${result.reason}"
}
```

### Código fuente (`Ejercicio14.3/src/Main.kt`)

```kotlin
sealed interface ApiResponse {
    data class SuccessResponse(val data: String) : ApiResponse

    data class ErrorResponse(val errorCode: Int, val errorMessage: String) : ApiResponse

    object Loading : ApiResponse
}

fun handleResponse(response: ApiResponse) {
    when (response) {
        is ApiResponse.SuccessResponse -> println("Respuesta recibida: ${response.data}")
        is ApiResponse.ErrorResponse ->
            println("Error ${response.errorCode}: ${response.errorMessage}")
        ApiResponse.Loading -> println("Cargando respuesta...")
    }
}

fun main() {
    handleResponse(ApiResponse.Loading)
    handleResponse(ApiResponse.SuccessResponse("{\"user\": \"Ada\"}"))
    handleResponse(ApiResponse.ErrorResponse(404, "Not Found"))
}
```

### Explicación paso a paso
1. **`ApiResponse`:** *sealed interface* con sus tres implementaciones anidadas. Las clases implementan la interfaz con `: ApiResponse`, sin paréntesis, porque una interfaz no tiene constructor.
2. **`SuccessResponse`** lleva el texto de la respuesta; **`ErrorResponse`**, el código (`Int`) y el mensaje; **`Loading`**, nada, porque solo indica un estado.
3. **`handleResponse`:** un `when` exhaustivo, como en el ejercicio 2.
4. **`main()`:** las respuestas van en el orden en que llegarían en una app real: primero «cargando», después el resultado (éxito o error).

> [!tip] Prueba
> ```text
> Cargando respuesta...
> Respuesta recibida: {"user": "Ada"}
> Error 404: Not Found
> ```

> [!note]- 🧠 Por qué funciona
> - Es el patrón que se usa en Android para pintar la pantalla según el estado de una petición a internet: con `Loading` se enseña un círculo de carga, con `SuccessResponse` los datos y con `ErrorResponse` un aviso.
> - ¿Por qué no un `enum`? Porque cada estado lleva **datos distintos**: el éxito lleva texto y el error, código y mensaje. Las constantes de un enum tienen todas las mismas propiedades.
> - ¿*Sealed class* o *sealed interface*? Con interfaz, una clase podría ser a la vez `ApiResponse` y otra cosa (implementar varias). Con clase, solo puede heredar de una.

---

## Ejercicio 4 · *Inline value class* `PhoneNumber`

> [!question] Enunciado
> Define una *inline value class* llamada `PhoneNumber` que encapsule un número de teléfono como un `String`. La clase debe validar que el número tenga **exactamente 9 dígitos**. Si el número no es válido, debe lanzar una excepción en el momento de crear el objeto.
>
> Luego, define una función `printPhoneNumber()` que reciba un objeto de tipo `PhoneNumber` y muestre el número en la consola.
>
> Implementa una función `main` que intente crear una instancia de `PhoneNumber` con un número válido y otra con un número inválido, y maneje la excepción. Finalmente, deberá llamar a `printPhoneNumber()` con la instancia válida.

### Clases y métodos introducidos
- `@JvmInline value class PhoneNumber(val value: String)`: una clase que **envuelve un único valor**. En el código es un tipo propio (`PhoneNumber`), pero al ejecutarse, la JVM trabaja directamente con el `String` de dentro, sin crear un objeto extra.
- `init` + `require`: la validación se ejecuta al crear el valor, igual que en una clase normal.
- `Regex("\\d{9}").matches(value)`: `\d` es «un dígito» y `{9}` «exactamente 9 veces». `matches` exige que **toda** la cadena encaje.

> **Términos explicados:** [[07 - POO II#Inline value classes|*inline value classes*]] · [[06 - POO I#2. Constructor primario y bloques de inicialización|`init`]] · [[Programación basica/Tema 9/Expresiones regulares|expresiones regulares]]

#### Ejemplo simple de funcionamiento
```kotlin
@JvmInline
value class Euros(val amount: Double)

fun pay(price: Euros) = println("Pagas ${price.amount} €")

fun main() {
    pay(Euros(9.99))
    // pay(9.99)   // ERROR: un Double no es un Euros
}
```

### Código fuente (`Ejercicio14.4/src/Main.kt`)

```kotlin
@JvmInline
value class PhoneNumber(val value: String) {
    init {
        // Exactamente 9 caracteres y todos dígitos
        require(Regex("\\d{9}").matches(value)) {
            "Phone number must contain exactly 9 digits: '$value'"
        }
    }
}

fun printPhoneNumber(phoneNumber: PhoneNumber) {
    println("Teléfono: ${phoneNumber.value}")
}

fun main() {
    val validNumber = PhoneNumber("612345678")

    val invalidInputs = listOf("12345", "6123456789", "61234567a")
    for (input in invalidInputs) {
        try {
            PhoneNumber(input)
        } catch (e: IllegalArgumentException) {
            println("Número inválido → ${e.message}")
        }
    }

    printPhoneNumber(validNumber)
}
```

### Explicación paso a paso
1. **La clase:** `@JvmInline value class` con una sola propiedad, `value`. Una *value class* solo puede tener **una** propiedad en el constructor.
2. **Validación:** en el `init`, la expresión regular comprueba que haya exactamente 9 dígitos y nada más. Si no, `require` lanza `IllegalArgumentException` con un mensaje que incluye el valor rechazado.
3. **`printPhoneNumber`:** recibe un `PhoneNumber`, no un `String`, y muestra su `value`.
4. **`main()`:** crea el número válido y prueba **tres** inválidos (corto, largo y con una letra), capturando la excepción de cada uno. Al final imprime el válido, como pide el enunciado.

> [!tip] Prueba
> ```text
> Número inválido → Phone number must contain exactly 9 digits: '12345'
> Número inválido → Phone number must contain exactly 9 digits: '6123456789'
> Número inválido → Phone number must contain exactly 9 digits: '61234567a'
> Teléfono: 612345678
> ```

> [!note]- 🧠 Por qué funciona
> - Sin *value class*, un teléfono sería un `String` cualquiera, y nada impediría pasar un nombre donde se espera un teléfono. Con `PhoneNumber`, el compilador lo detecta, y además cualquier `PhoneNumber` que exista **ya está validado**.
> - Es como una etiqueta en un bote: por dentro sigue habiendo el mismo `String` (no ocupa más memoria), pero la etiqueta deja claro qué es y que ha pasado el control.
> - `matches` comprueba la cadena **entera**. Por eso `"6123456789"` (10 dígitos) se rechaza aunque contenga 9 dígitos seguidos.

---

## Ejercicio 5 · `fun interface` `DataValidator`

> [!question] Enunciado
> Define una `fun interface` llamada `DataValidator`, cuyo método abstracto se llame `isValid(input: String): Boolean`.
>
> Define una clase llamada `ValidationService` con una función `check(value: String, validator: DataValidator): Boolean` que:
>
> - Imprima el mensaje `"Checking value: '$value'"`.
> - Llame a `validator.isValid(value)` y devuelva el resultado.
>
> En la función `main`:
>
> - Crea una instancia inmutable de `ValidationService` llamada `service`.
> - Llama a `service.check` para verificar si la cadena `"kotlin"` tiene más de 5 caracteres, pasando la expresión lambda necesaria (recibe un `String` y devuelve un `Boolean`).
> - Llama a `service.check` para verificar si la cadena `"java"` contiene la letra `'a'`, pasando una segunda expresión lambda.
> - Finalmente, imprime los resultados de las dos llamadas.

### Clases y métodos introducidos
- `fun interface`: una interfaz con **un único método abstracto**. Gracias a eso, en vez de un objeto que la implemente, se le puede pasar **una lambda**.
- **Conversión SAM** (*Single Abstract Method*): Kotlin convierte la lambda `{ it.length > 5 }` en un objeto `DataValidator` cuyo `isValid` es esa lambda.

> **Términos explicados:** [[10 - Programación funcional#7. Interfaz fun interface|`fun interface`]] · [[10 - Programación funcional#6. Conversión SAM|conversión SAM]] · [[10 - Programación funcional#5. Expresiones lambda|lambdas]]

#### Ejemplo simple de funcionamiento
```kotlin
fun interface Greeter {
    fun greet(name: String): String
}

fun main() {
    val polite = Greeter { "Buenos días, $it" }   // lambda convertida en Greeter
    println(polite.greet("Daniel"))                // Buenos días, Daniel
}
```

### Código fuente (`Ejercicio14.5/src/Main.kt`)

```kotlin
fun interface DataValidator {
    fun isValid(input: String): Boolean
}

class ValidationService {
    fun check(value: String, validator: DataValidator): Boolean {
        println("Checking value: '$value'")
        return validator.isValid(value)
    }
}

fun main() {
    val service = ValidationService()

    // Cada lambda (String) -> Boolean se convierte en un DataValidator (conversión SAM)
    val isLongEnough = service.check("kotlin") { it.length > 5 }
    val containsA = service.check("java") { 'a' in it }

    println("¿\"kotlin\" tiene más de 5 caracteres? $isLongEnough")
    println("¿\"java\" contiene la letra 'a'? $containsA")
}
```

### Explicación paso a paso
1. **`DataValidator`:** `fun interface` con un solo método, `isValid`. Ese método único es lo que permite usar lambdas.
2. **`ValidationService.check`:** imprime el valor y delega la decisión en el validador. No sabe **qué** se comprueba: solo que el validador responde `true` o `false`.
3. **Primera llamada:** `{ it.length > 5 }` → `"kotlin"` tiene 6 letras → `true`.
4. **Segunda llamada:** `{ 'a' in it }` → `"java"` contiene `a` → `true`.
5. **Salida:** los dos `Checking value` salen primero, porque los resultados se guardan en variables y se imprimen al final.

> [!tip] Prueba
> ```text
> Checking value: 'kotlin'
> Checking value: 'java'
> ¿"kotlin" tiene más de 5 caracteres? true
> ¿"java" contiene la letra 'a'? true
> ```

> [!note]- 🧠 Por qué funciona
> - Sin `fun`, habría que escribir un objeto entero para cada validación: `object : DataValidator { override fun isValid(input: String) = input.length > 5 }`. La conversión SAM lo resume en `{ it.length > 5 }`.
> - ¿Por qué no usar directamente `(String) -> Boolean`, como en `testBoth`? Funcionaría igual, pero `DataValidator` da **nombre y significado** al contrato. Además, se puede usar desde Java, que no entiende los tipos función de Kotlin.

---

## Ejercicio 6 · Función `inline` y *non-local return*

> [!question] Enunciado
> Define una función *top-level* `inline` llamada `executeWithTimer` que reciba una lambda `action: () -> Unit` como único parámetro. Dentro, debe imprimir `"Starting timer..."`, ejecutar `action()` e imprimir `"Timer finished."`.
>
> En la función `main`:
>
> 1. Llama a `executeWithTimer` usando una lambda donde:
> 	- Se imprima `"Inside Action 1"`.
> 	- Se ejecute un `return` simple (*non-local return*).
> 	- Se imprima `"This should not be printed."`.
>
> 	Inmediatamente después de esta llamada, imprime `"Main continues here."` (observa si se ejecuta o no).
> 2. Llama a `executeWithTimer` por segunda vez, pero esta vez:
> 	- Usa una etiqueta de retorno (`return@executeWithTimer`) para forzar un retorno local (como un `break` en una función normal).
> 	- Imprime `"Inside Action 2"`.
>
> 	Inmediatamente después de esta llamada, imprime `"Main finished properly."`.

### Clases y métodos introducidos
- `inline fun`: el compilador **copia el cuerpo** de la función (y el de la lambda) en el lugar donde se llama, en vez de hacer una llamada normal.
- ***Non-local return***: un `return` dentro de una lambda pasada a una función `inline` **sale de la función que la contiene**, no solo de la lambda. Solo se permite con funciones `inline`.
- **Retorno local con etiqueta**: `return@executeWithTimer` sale **solo de la lambda** y la ejecución sigue después de la llamada.

> **Términos explicados:** [[10 - Programación funcional#11. Inline functions|funciones `inline` y *non-local return*]] · [[10 - Programación funcional#5. Expresiones lambda|retornos con etiqueta]]

#### Ejemplo simple de funcionamiento
```kotlin
fun findFirstEven(numbers: List<Int>) {
    numbers.forEach {                   // forEach es inline
        if (it % 2 == 0) {
            println("Primer par: $it")
            return                       // sale de findFirstEven, no solo del forEach
        }
    }
    println("No hay pares")
}
```

### Código fuente (`Ejercicio14.6/src/Main.kt`)

```kotlin
inline fun executeWithTimer(action: () -> Unit) {
    println("Starting timer...")
    action()
    println("Timer finished.")
}

fun nonLocalReturnDemo() {
    executeWithTimer {
        println("Inside Action 1")
        return                                   // non-local return: sale de nonLocalReturnDemo()
        println("This should not be printed.")
    }
    println("Main continues here.")              // no se ejecuta
}

fun localReturnDemo() {
    executeWithTimer {
        println("Inside Action 2")
        return@executeWithTimer                  // retorno local: solo sale de la lambda
    }
    println("Main finished properly.")           // sí se ejecuta
}

fun main() {
    nonLocalReturnDemo()
    println("-----")
    localReturnDemo()
}
```

### Explicación paso a paso
1. **`executeWithTimer`:** es `inline`. Imprime, ejecuta la lambda e imprime otra vez.
2. **Primera llamada (`nonLocalReturnDemo`):** se imprime «Inside Action 1» y llega el `return`. Como la función es `inline`, ese `return` **sale de `nonLocalReturnDemo()` entera**. Por eso no se imprimen ni «This should not be printed», ni «Timer finished», ni «Main continues here».
3. **Segunda llamada (`localReturnDemo`):** tras «Inside Action 2», `return@executeWithTimer` sale **solo de la lambda**. `executeWithTimer` continúa e imprime «Timer finished.», y después se imprime «Main finished properly.».
4. **¿Por qué dos funciones y no todo en `main`?** Ver el aviso de abajo.

> [!tip] Prueba
> ```text
> Starting timer...
> Inside Action 1
> -----
> Starting timer...
> Inside Action 2
> Timer finished.
> Main finished properly.
> ```
> «This should not be printed.» no sale nunca: el `return` ocurre antes. `kotlinc` lo compila sin errores ni avisos, aunque IntelliJ sí suele marcar esa línea en gris como código inalcanzable.

> [!warning] ¿Por qué no está todo en `main()`?
> El enunciado dice «en la función `main`», pero si el primer `return` se escribe directamente en `main`, ese `return` **termina `main`, y con ella todo el programa**: la segunda llamada nunca llegaría a ejecutarse. Comprobado: con todo en `main`, la salida se queda en `Starting timer...` / `Inside Action 1`. Por eso cada caso va en su propia función y `main()` llama a las dos.
>
> Sobre el orden de la segunda llamada: si `return@executeWithTimer` va **antes** de imprimir «Inside Action 2», ese mensaje nunca saldría. Por eso se imprime primero y después se hace el retorno local.

> [!note]- 🧠 Por qué funciona
> - `inline` es como copiar y pegar: el código de la lambda acaba escrito **dentro** de `nonLocalReturnDemo()`. Un `return` ahí es, literalmente, un `return` de esa función.
> - Sin `inline`, la lambda sería un objeto aparte y un `return` suelto no tendría sentido. Comprobado: quitando `inline`, el compilador da `'return' is prohibited here`.
> - `return@executeWithTimer` usa como etiqueta el nombre de la función que recibe la lambda: «sal de la lambda que le pasé a `executeWithTimer`».

---

## Ejercicio 7 · `testBoth` con dos condiciones

> [!question] Enunciado
> Define una función de orden superior llamada `testBoth` que reciba dos enteros y una función de condición como parámetros. `testBoth` debe devolver un valor booleano que indique si **ambos** números cumplen la condición especificada.
>
> Prueba la función llamándola dos veces desde `main` con dos condiciones distintas pasadas como lambdas.

### Clases y métodos introducidos
- Es el mismo enunciado que el [[Ejercicios Bloque 12#Ejercicio 4 · Función de orden superior `testBoth`|ejercicio 4 del Bloque 12]], donde se explica con detalle. Aquí se prueba con **otras condiciones**, para ver que la misma función sirve para cualquier comprobación.
- Tipo función `(Int) -> Boolean`, lambda con `it` y con nombre, y *trailing lambda*.

> **Términos explicados:** [[10 - Programación funcional#1. Tipos función|tipos función]] · [[10 - Programación funcional#5. Expresiones lambda|lambdas]]

### Código fuente (`Ejercicio14.7/src/Main.kt`)

```kotlin
// Función de orden superior: recibe una función (Int) -> Boolean como parámetro
fun testBoth(first: Int, second: Int, condition: (Int) -> Boolean): Boolean =
    condition(first) && condition(second)

fun main() {
    // Condición 1: ¿son múltiplos de 3?
    val bothMultiplesOf3 = testBoth(9, 21) { it % 3 == 0 }
    println("¿9 y 21 son múltiplos de 3? $bothMultiplesOf3")

    // Condición 2: ¿son mayores que 10?
    val bothGreaterThan10 = testBoth(15, 7) { number -> number > 10 }
    println("¿15 y 7 son mayores que 10? $bothGreaterThan10")
}
```

### Explicación paso a paso
1. **`testBoth`** aplica `condition` a los dos números y une los resultados con `&&`.
2. **Primera llamada:** `{ it % 3 == 0 }`. 9 y 21 son múltiplos de 3 → `true`.
3. **Segunda llamada:** `{ number -> number > 10 }`. 15 sí lo es, pero 7 no → `false`.

> [!tip] Prueba
> ```text
> ¿9 y 21 son múltiplos de 3? true
> ¿15 y 7 son mayores que 10? false
> ```

> [!note]- 🧠 Por qué funciona
> - La función no cambia entre el Bloque 12 y este: solo cambian las lambdas. Esa es la ventaja de las funciones de orden superior, que separan **qué se hace** (comprobar los dos) de **cómo se comprueba** (la condición).

---

## Ejercicio 8 · Función genérica `calculateAggregate`

> [!question] Enunciado
> Imagina que gestionas el inventario de una tienda y tienes una lista de productos. Necesitas calcular diferentes totales: el valor total del inventario (precio × stock), el peso total de todos los artículos (peso × stock) y la cantidad total de artículos.
>
> Define una **única función de orden superior genérica**, llamada `calculateAggregate`, que acepte una lista de cualquier tipo de elemento y una lambda (*selector*) que indique qué valor numérico (`Double`) se extrae o calcula de cada elemento. La función debe recorrer la lista, aplicar la lambda a cada elemento, sumar los resultados y devolver la suma total.
>
> Prueba la función desde `main` con distintas llamadas en las que uses las lambdas de distintas formas: **dentro de los paréntesis, fuera con paréntesis, fuera sin paréntesis y con `it`**.

### Clases y métodos introducidos
- **Función genérica** `fun <T> calculateAggregate(items: List<T>, selector: (T) -> Double)`: `T` es «cualquier tipo». La misma función vale para una lista de productos, de cadenas…
- **Selector**: la lambda que dice **qué** sumar de cada elemento. La función se encarga del **cómo** (recorrer y acumular).
- **Las cuatro formas de pasar la lambda:**
	1. Dentro de los paréntesis: `f(lista, { … })`.
	2. Fuera, con paréntesis (*trailing lambda*): `f(lista) { … }`.
	3. Con `it`: `f(lista) { it.stock.toDouble() }`.
	4. Fuera y **sin paréntesis**: solo si la lambda es el **único** argumento. Por eso se añade una versión *extension* de `List<T>`: `lista.aggregate { … }`.

> **Términos explicados:** [[09 - Genéricos#2. Funciones parametrizadas|funciones genéricas]] · [[10 - Programación funcional#1. Tipos función|tipos función]] · [[10 - Programación funcional#5. Expresiones lambda|lambdas y *trailing lambda*]] · [[08 - POO III#5. Extension functions|*extension functions*]]

#### Ejemplo simple de funcionamiento
```kotlin
fun <T> countIf(items: List<T>, condition: (T) -> Boolean): Int {
    var count = 0
    for (item in items) if (condition(item)) count++
    return count
}

fun main() {
    println(countIf(listOf(1, 2, 3, 4)) { it > 2 })          // 2
    println(countIf(listOf("sol", "mar", "cielo")) { it.length == 3 })   // 2
}
```

### Código fuente (`Ejercicio14.8/src/Main.kt`)

```kotlin
data class Product(val name: String, val price: Double, val weightKg: Double, val stock: Int)

// Función genérica de orden superior: suma lo que devuelva selector para cada elemento
fun <T> calculateAggregate(items: List<T>, selector: (T) -> Double): Double {
    var total = 0.0
    for (item in items) {
        total += selector(item)
    }
    return total
}

// Versión extension de List<T>: la lambda queda como único argumento.
// Necesita otro nombre: con el mismo, la JVM la vería igual que calculateAggregate(list, selector)
fun <T> List<T>.aggregate(selector: (T) -> Double): Double =
    calculateAggregate(this, selector)

fun main() {
    val inventory = listOf(
        Product("Portátil", 800.0, 2.1, 5),
        Product("Ratón", 20.0, 0.1, 30),
        Product("Monitor", 150.0, 4.5, 8),
    )

    // 1. Lambda dentro de los paréntesis
    val totalValue = calculateAggregate(inventory, { product -> product.price * product.stock })

    // 2. Trailing lambda: fuera de los paréntesis
    val totalWeight = calculateAggregate(inventory) { product -> product.weightKg * product.stock }

    // 3. Trailing lambda con it
    val totalUnits = calculateAggregate(inventory) { it.stock.toDouble() }

    // 4. Fuera y sin paréntesis (versión extension: la lambda es el único argumento)
    val totalUnitsAgain = inventory.aggregate { it.stock.toDouble() }

    println("Valor total del inventario: ${"%.2f".format(totalValue)} €")
    println("Peso total: ${"%.2f".format(totalWeight)} kg")
    println("Unidades totales: $totalUnits")
    println("Unidades totales (versión extension): $totalUnitsAgain")

    // Al ser genérica, sirve con cualquier tipo de lista
    val words = listOf("sol", "luna", "estrella")
    println("Letras en total: ${calculateAggregate(words) { it.length.toDouble() }}")
}
```

### Explicación paso a paso
1. **`Product`:** una `data class` con precio, peso y stock.
2. **`calculateAggregate`:** recorre la lista y, para cada elemento, suma lo que devuelva `selector(item)`. No sabe nada de productos: por eso es genérica (`T`).
3. **Los tres totales del enunciado:**
	- Valor: `price * stock` → 800·5 + 20·30 + 150·8 = **5800 €**.
	- Peso: `weightKg * stock` → 2,1·5 + 0,1·30 + 4,5·8 = **49,5 kg**.
	- Unidades: `stock` (pasado a `Double` con `toDouble()`, porque el selector debe devolver `Double`) → **43**.
4. **Las cuatro formas de lambda:** cada total usa una forma distinta, y el último se repite con la versión *extension* para poder escribir la lambda sin paréntesis.
5. **Genericidad:** la última llamada usa la misma función con una lista de `String`, sumando sus longitudes (3 + 4 + 8 = 15).

> [!tip] Prueba
> ```text
> Valor total del inventario: 5800,00 €
> Peso total: 49,50 kg
> Unidades totales: 43.0
> Unidades totales (versión extension): 43.0
> Letras en total: 15.0
> ```

> [!warning] Por qué la versión *extension* tiene otro nombre
> Al principio se llamó también `calculateAggregate`, y **no compiló**. Error real de `kotlinc`: `platform declaration clash: The following declarations have the same JVM signature`.
>
> Una *extension function* se compila como una función normal que recibe el receptor como **primer parámetro** (como se vio en el [[Ejercicios Bloque 11#Ejercicio 2 · *Extension function* `reverseWords`|Bloque 11]]). Así, `List<T>.calculateAggregate(selector)` y `calculateAggregate(list, selector)` quedan exactamente iguales para la JVM. Con otro nombre (`aggregate`), el problema desaparece.

> [!note]- 🧠 Por qué funciona
> - `calculateAggregate` es como una calculadora de caja registradora que suma lo que le digas: tú decides si suma precios, pesos o unidades (el selector), y ella siempre hace lo mismo, recorrer y acumular.
> - «Fuera sin paréntesis» solo es posible cuando la lambda es el **único** argumento, como en `forEach { … }`. Con dos parámetros, la lista tiene que ir entre paréntesis. La *extension* convierte la lista en el receptor (lo que va antes del punto), y así la lambda queda sola.

---

## Ejercicio 9 · Funciones `hacerCon1` a `hacerCon9`

> [!question] Enunciado
> Realiza las siguientes funciones y pruébalas llamándolas con una lambda que devuelva la cadena «recibida» invertida:
>
> 1. `hacerCon1`: no devuelve nada y recibe dos parámetros, una cadena y un parámetro de tipo función que no devuelve nada y que recibe como argumento la cadena del parámetro anterior.
> 2. `hacerCon2`: como la anterior, pero después de ejecutar la lambda recibida, devuelve la cadena recibida como argumento.
> 3. `hacerCon3`: como la anterior, pero devuelve una cadena, que es lo que devuelva el literal de función pasado como argumento.
> 4. `hacerCon4`: como `hacerCon2`, pero como *extension function* sobre `String`: no recibe la cadena como argumento, sino que se ejecuta «sobre ella».
> 5. `hacerCon5`: como `hacerCon3`, pero como *extension function* sobre `String`.
> 6. `hacerCon6`: como `hacerCon4`, pero que funcione con cualquier tipo `T` en vez de solo con `String`.
> 7. `hacerCon7`: como `hacerCon5`, pero con cualquier tipo `T`. El tipo de retorno también se generaliza a un tipo `R`.
> 8. `hacerCon8`: como `hacerCon6`, pero con un parámetro de **tipo función con receptor**.
> 9. `hacerCon9`: como `hacerCon7`, pero con un parámetro de **tipo función con receptor**.

### Clases y métodos introducidos
- `(String) -> Unit` frente a `String.() -> Unit`: en el primero, la cadena llega como **parámetro** (`it`). En el segundo es el **receptor**: dentro de la lambda es `this`, y se puede llamar a sus métodos directamente (`reversed()` en vez de `it.reversed()`).
- `fun <T> T.hacerCon6(…)`: *extension function* **genérica**, que vale para un receptor de cualquier tipo.
- Las cuatro últimas son, en realidad, las *scoping functions* de Kotlin escritas a mano:

| Función | Equivale a | La lambda recibe el objeto como | Devuelve |
| --- | --- | --- | --- |
| `hacerCon6` | `also` | `it` | el propio objeto |
| `hacerCon7` | `let` | `it` | lo que devuelva la lambda |
| `hacerCon8` | `apply` | `this` | el propio objeto |
| `hacerCon9` | `run` | `this` | lo que devuelva la lambda |

> **Términos explicados:** [[10 - Programación funcional#12. Literales de función con receptor (lambda with receiver)|literales de función con receptor]] · [[10 - Programación funcional#13. Scoping functions (with, run, apply, let, also)|*scoping functions*]] · [[09 - Genéricos#2. Funciones parametrizadas|funciones genéricas]] · [[08 - POO III#5. Extension functions|*extension functions*]]

#### Ejemplo simple de funcionamiento
```kotlin
val withParameter: (String) -> Int = { it.length }   // la cadena es it
val withReceiver: String.() -> Int = { length }       // la cadena es this

fun main() {
    println(withParameter("Kotlin"))   // 6
    println("Kotlin".withReceiver())   // 6
}
```

### Código fuente (`Ejercicio14.9/src/Main.kt`)

```kotlin
// 1. Recibe la cadena y una función que la usa sin devolver nada
fun hacerCon1(text: String, action: (String) -> Unit) {
    action(text)
}

// 2. Igual, pero devuelve la cadena recibida
fun hacerCon2(text: String, action: (String) -> Unit): String {
    action(text)
    return text
}

// 3. Devuelve lo que devuelva la función
fun hacerCon3(text: String, action: (String) -> String): String = action(text)

// 4. Como hacerCon2, pero como extension function de String
fun String.hacerCon4(action: (String) -> Unit): String {
    action(this)
    return this
}

// 5. Como hacerCon3, pero como extension function de String
fun String.hacerCon5(action: (String) -> String): String = action(this)

// 6. Como hacerCon4, pero para cualquier tipo T          (equivale a also)
fun <T> T.hacerCon6(action: (T) -> Unit): T {
    action(this)
    return this
}

// 7. Como hacerCon5, pero con T y un retorno genérico R   (equivale a let)
fun <T, R> T.hacerCon7(action: (T) -> R): R = action(this)

// 8. Como hacerCon6, pero con tipo función con receptor   (equivale a apply)
fun <T> T.hacerCon8(action: T.() -> Unit): T {
    action()          // se ejecuta sobre this: dentro de la lambda, this es el receptor
    return this
}

// 9. Como hacerCon7, pero con tipo función con receptor   (equivale a run)
fun <T, R> T.hacerCon9(action: T.() -> R): R = action()

fun main() {
    val word = "Kotlin"

    hacerCon1(word) { println("hacerCon1: ${it.reversed()}") }
    println("hacerCon2 devuelve: ${hacerCon2(word) { println("hacerCon2: ${it.reversed()}") }}")
    println("hacerCon3 devuelve: ${hacerCon3(word) { it.reversed() }}")
    println("hacerCon4 devuelve: ${word.hacerCon4 { println("hacerCon4: ${it.reversed()}") }}")
    println("hacerCon5 devuelve: ${word.hacerCon5 { it.reversed() }}")
    println("hacerCon6 devuelve: ${word.hacerCon6 { println("hacerCon6: ${it.reversed()}") }}")
    println("hacerCon7 devuelve: ${word.hacerCon7 { it.reversed() }}")
    println("hacerCon8 devuelve: ${word.hacerCon8 { println("hacerCon8: ${reversed()}") }}")
    println("hacerCon9 devuelve: ${word.hacerCon9 { reversed() }}")

    // Las versiones genéricas funcionan con cualquier tipo: aquí T = Int y R = String
    println("hacerCon7 con un Int: ${12345.hacerCon7 { it.toString().reversed() }}")
    println("hacerCon9 con un Int: ${12345.hacerCon9 { toString().reversed() }}")
}
```

### Explicación paso a paso
1. **`hacerCon1`–`hacerCon3`:** funciones normales. La cadena va como primer parámetro y la lambda como segundo. Cambia qué devuelven: nada, la cadena original o el resultado de la lambda.
2. **`hacerCon4`–`hacerCon5`:** lo mismo, pero como *extension* de `String`. Ahora la cadena es el receptor (`word.hacerCon4 { … }`) y dentro se usa `this`.
3. **`hacerCon6`–`hacerCon7`:** generalizan a cualquier tipo `T` (y `R` para el resultado). Por eso al final funcionan también con el `Int` 12345.
4. **`hacerCon8`–`hacerCon9`:** el parámetro es `T.() -> …`. Dentro de la lambda, el objeto es `this`, así que se escribe `reversed()` en vez de `it.reversed()`.
5. **Las que no devuelven el resultado de la lambda** (1, 2, 4, 6 y 8) imprimen la cadena invertida *dentro* de la lambda, porque su lambda es `-> Unit`. Las otras devuelven directamente la cadena invertida.

> [!tip] Prueba
> ```text
> hacerCon1: niltoK
> hacerCon2: niltoK
> hacerCon2 devuelve: Kotlin
> hacerCon3 devuelve: niltoK
> hacerCon4: niltoK
> hacerCon4 devuelve: Kotlin
> hacerCon5 devuelve: niltoK
> hacerCon6: niltoK
> hacerCon6 devuelve: Kotlin
> hacerCon7 devuelve: niltoK
> hacerCon8: niltoK
> hacerCon8 devuelve: Kotlin
> hacerCon9 devuelve: niltoK
> hacerCon7 con un Int: 54321
> hacerCon9 con un Int: 54321
> ```

> [!note]- 🧠 Por qué funciona
> - El ejercicio es una escalera: cada `hacerCon` cambia **una sola cosa** respecto a la anterior (qué devuelve, si es *extension*, si es genérica, si usa receptor). Al final de la escalera estás en `also`, `let`, `apply` y `run`, las funciones que usarás a diario en Android.
> - Con receptor (`T.() -> R`), la lambda se comporta como si fuera un método de `T`: por eso basta con `reversed()`, igual que dentro de una clase no hace falta escribir `this.` delante de sus métodos.
> - La diferencia entre «devuelve el objeto» (`also`/`apply`) y «devuelve lo de la lambda» (`let`/`run`) se ve en la salida: `hacerCon6` y `hacerCon8` devuelven `Kotlin`, mientras que `hacerCon7` y `hacerCon9` devuelven `niltoK`.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| *Sealed class* | `sealed class A` + subclases en el mismo archivo | Subtipos cerrados; `when` exhaustivo sin `else`. |
| *Sealed interface* | `sealed interface A` + `class B : A` | Igual, pero se implementa sin paréntesis y se pueden implementar varias. |
| `object` en un `when` | `SystemMaintenance ->` | Se compara directamente, sin `is`. |
| *Value class* | `@JvmInline value class P(val v: String)` | Tipo propio sin coste extra; una sola propiedad. |
| `fun interface` | `fun interface V { fun isValid(s: String): Boolean }` | Se puede crear con una lambda (conversión SAM). |
| `inline` + `return` | `inline fun f(a: () -> Unit)` | `return` en la lambda sale de la función que la contiene. |
| Retorno local | `return@nombreFuncion` | Sale solo de la lambda. |
| Función genérica | `fun <T> f(items: List<T>, sel: (T) -> Double)` | Sirve para listas de cualquier tipo. |
| Lambda sin paréntesis | `obj.f { … }` | Solo si la lambda es el único argumento. |
| Función con receptor | `T.() -> R` | Dentro de la lambda, el objeto es `this`. |
| *Scoping functions* | `also` · `let` · `apply` · `run` | = `hacerCon6` · `7` · `8` · `9`. |

## Relaciones

- Teoría: [[07 - POO II]] · [[09 - Genéricos]] · [[10 - Programación funcional]]
- Bloque anterior: [[Ejercicios Bloque 13]] · Bloque siguiente: [[Ejercicios Bloque 15]]
- Mismos enunciados en el boletín 7: [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.8 · Sealed class para formas de pago|7.8]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.9 · Jerarquía sellada y when exhaustivo|7.9]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.10 · Sealed interface para respuestas de API|7.10]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.11 · Inline value class para teléfono|7.11]]
- Mismos enunciados en el boletín 10: [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.6 · fun interface DataValidator|10.6]] · [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.10 · Inline function y non-local return|10.10]] · [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.1 · Función de orden superior testBoth con lambdas|10.1]] · [[10.1 - Ejercicios 10 Programación funcional#Ejercicio 10.11 · Funciones hacerCon con receptor|10.11]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Declarar una *sealed class* y una *sealed interface* y recorrerlas con un `when` sin `else`
- [ ] Explicar cuándo usar *sealed* en vez de `enum`
- [ ] Crear una *value class* que valide su valor en `init`
- [ ] Pasar una lambda donde se espera una `fun interface`
- [ ] Explicar la diferencia entre `return` y `return@etiqueta` dentro de una lambda `inline`
- [ ] Escribir una función genérica de orden superior y llamarla con las cuatro formas de lambda
- [ ] Relacionar `also`, `let`, `apply` y `run` con `hacerCon6`–`hacerCon9`
