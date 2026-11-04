---
asignatura: PMDM
tema: 7
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/ejercicios
---

# Bloque 10 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[07 - POO II]] · [[06 - POO I]]
> Bloque anterior: [[Ejercicios Bloque 9]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque10/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 7.5, 7.6 y 7.7 de [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2|el boletín 7]]. El código parte de esas soluciones, ampliado para cubrir todo lo que pide el enunciado.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque10/Ejercicio10.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Enumeración `OrderStatus`]]
- [[#Ejercicio 2 · Interfaces `Device` y `SmartDevice`]]
- [[#Ejercicio 3 · `EventManager` con *object expressions*]]

---

## Ejercicio 1 · Enumeración `OrderStatus`

> [!question] Enunciado
> Define una enumeración llamada `OrderStatus` para gestionar los diferentes estados de un pedido en una tienda. La enumeración debe contener los siguientes estados y sus propiedades asociadas:
>
> - `PENDING`, con la propiedad `description` como `"Order has been received"`.
> - `PROCESSING`, con la propiedad `description` como `"Order is being processed"`.
> - `SHIPPED`, con la propiedad `description` como `"Order has been shipped"`.
> - `DELIVERED`, con la propiedad `description` como `"Order has been delivered"`.
> - `CANCELLED`, con la propiedad `description` como `"Order has been cancelled"`.
>
> Cada estado debe tener un método `printStatus()` que imprima el nombre del estado y su descripción.
>
> Implementa una clase llamada `Order` para representar un pedido, con las propiedades `id` y `status` (de tipo `OrderStatus`).
>
> Implementa una función `main` que cree una instancia de `Order` con un estado inicial, imprima el estado inicial del pedido, actualice el estado del pedido a otro estado y vuelva a imprimirlo.

### Clases y métodos introducidos
- `enum class`: un tipo con un **número cerrado de valores** posibles. Un pedido no puede estar en un estado que no esté en la lista.
- **Enum con propiedades**: `enum class OrderStatus(val description: String)`. Cada constante pasa su valor al constructor: `PENDING("Order has been received")`.
- **Métodos en un enum**: después de la última constante va un `;` y luego los métodos, que tienen todas las constantes.
- `name` y `ordinal`: propiedades que tiene todo enum. `name` es el nombre de la constante (`"PENDING"`) y `ordinal` su posición, empezando en 0.
- `OrderStatus.entries`: lista con todas las constantes, en orden.

> **Términos explicados:** [[07 - POO II#Enumeraciones|enumeraciones, `name`, `ordinal` y `values()`]]

#### Ejemplo simple de funcionamiento
```kotlin
enum class Size(val centimeters: Int) {
    SMALL(20), MEDIUM(30), LARGE(40);

    fun describe() = "$name mide $centimeters cm"
}

fun main() {
    println(Size.MEDIUM.describe())   // MEDIUM mide 30 cm
}
```

### Código fuente (`Ejercicio10.1/src/Main.kt`)

```kotlin
// Cada constante del enum tiene su propia descripción
enum class OrderStatus(val description: String) {
    PENDING("Order has been received"),
    PROCESSING("Order is being processed"),
    SHIPPED("Order has been shipped"),
    DELIVERED("Order has been delivered"),
    CANCELLED("Order has been cancelled");   // el ; separa las constantes de los métodos

    fun printStatus() {
        println("$name: $description")
    }
}

// status es var porque el estado del pedido cambia
class Order(val id: Int, var status: OrderStatus)

fun main() {
    val order = Order(42, OrderStatus.PENDING)
    print("Pedido ${order.id} → ")
    order.status.printStatus()

    order.status = OrderStatus.SHIPPED
    print("Pedido ${order.id} → ")
    order.status.printStatus()

    // Todos los estados posibles, con entries
    println("Estados posibles:")
    for (status in OrderStatus.entries) {
        println("  ${status.ordinal}. ${status.name}")
    }
}
```

### Explicación paso a paso
1. **El enum:** `OrderStatus` tiene una propiedad `description` en su constructor. Cada una de las 5 constantes la rellena con su texto.
2. **El `;`:** tras `CANCELLED(…)` hay un punto y coma. Es **obligatorio** cuando el enum tiene métodos: separa la lista de constantes del resto del cuerpo.
3. **`printStatus()`:** usa `name` (que Kotlin da gratis a cada constante) y `description`. Como está en el cuerpo del enum, lo tienen las 5 constantes sin repetirlo.
4. **`Order`:** `id` es `val` porque un pedido no cambia de número, y `status` es `var` porque sí cambia de estado.
5. **`main()`:** crea el pedido en `PENDING` y lo imprime, lo pasa a `SHIPPED` y lo vuelve a imprimir. Al final recorre `entries` para mostrar todos los estados con su `ordinal`.

> [!tip] Prueba
> ```text
> Pedido 42 → PENDING: Order has been received
> Pedido 42 → SHIPPED: Order has been shipped
> Estados posibles:
>   0. PENDING
>   1. PROCESSING
>   2. SHIPPED
>   3. DELIVERED
>   4. CANCELLED
> ```

> [!note]- 🧠 Por qué funciona
> - Cada constante de un enum es un **objeto único** de la clase `OrderStatus`, creado una sola vez. `OrderStatus.SHIPPED` es siempre el mismo objeto, por eso se comparan con `==` sin problema.
> - Si usaras un `String` para el estado (`"shipped"`), nada te impediría escribir `"shiped"` por error. Con un enum, `OrderStatus.SHIPED` **no compila**: el compilador solo acepta los estados que existen.
> - `order.status.printStatus()` llama al método **de la constante actual**: la misma línea imprime cosas distintas según el estado del pedido.

> [!tip] `entries` y `values()`
> Tus apuntes usan `OrderStatus.values()`, que devuelve un **array** nuevo cada vez que se llama. Desde Kotlin 1.9 existe `OrderStatus.entries`, que devuelve una **lista** y es lo que recomienda ahora Kotlin. Para recorrer los estados, los dos funcionan igual.

---

## Ejercicio 2 · Interfaces `Device` y `SmartDevice`

> [!question] Enunciado
> Define una interfaz llamada `Device` para representar dispositivos electrónicos, con las siguientes propiedades y métodos:
>
> - Propiedad `brand` (`String`): marca del dispositivo.
> - Método `turnOn()` con código por defecto que imprima `"Turning on the device"`.
> - Método `turnOff()` sin implementación.
>
> Luego, define otra interfaz llamada `SmartDevice` que herede de `Device` y añada:
>
> - Propiedad `os` (`String`): sistema operativo del dispositivo.
> - Método `connectToWiFi()` con código por defecto que imprima `"Connecting to WiFi"`.
>
> Implementa una clase llamada `Smartphone` que implemente la interfaz `SmartDevice`, proporcione una implementación para los métodos requeridos y **sobrescriba alguno de los métodos con implementación por defecto**.
>
> Implementa una función `main` que cree una instancia de `Smartphone` y llame a todos los métodos disponibles para la instancia.

### Clases y métodos introducidos
- `interface`: un **contrato**, una lista de lo que una clase se compromete a tener. A diferencia de Java (antes de Java 8), una interfaz de Kotlin puede traer **métodos con código por defecto**.
- **Propiedad en una interfaz**: `val brand: String` sin valor. La clase que implementa la interfaz tiene que darle valor con `override val`.
- **Herencia de interfaces**: `interface SmartDevice : Device`. `SmartDevice` incluye todo lo de `Device` más lo suyo.
- `class Smartphone(…) : SmartDevice`: implementa la interfaz. Sin paréntesis tras `SmartDevice`, porque las interfaces no tienen constructor.
- `super.turnOn()`: llama al código por defecto de la interfaz desde la versión sobrescrita.

> **Términos explicados:** [[07 - POO II#Interfaces|interfaces, propiedades y métodos por defecto]] · [[06 - POO I#12. Sobrescribir métodos y propiedades|`override` y `super`]]

#### Ejemplo simple de funcionamiento
```kotlin
interface Greeter {
    val name: String
    fun greet() = println("Hola, soy $name")   // código por defecto
}

class Robot(override val name: String) : Greeter

fun main() {
    Robot("R2D2").greet()   // Hola, soy R2D2
}
```

### Código fuente (`Ejercicio10.2/src/Main.kt`)

```kotlin
interface Device {
    val brand: String                                      // propiedad abstracta
    fun turnOn() = println("Turning on the device")        // con código por defecto
    fun turnOff()                                          // sin implementación
}

// SmartDevice hereda todo lo de Device y añade más
interface SmartDevice : Device {
    val os: String
    fun connectToWiFi() = println("Connecting to WiFi")
}

class Smartphone(
    override val brand: String,
    override val os: String,
) : SmartDevice {
    // Obligatorio: turnOff() no tenía implementación
    override fun turnOff() = println("Turning off the $brand smartphone")

    // Opcional: sobrescribimos turnOn() reutilizando el código por defecto
    override fun turnOn() {
        super.turnOn()
        println("$brand is booting $os")
    }
}

fun main() {
    val phone = Smartphone("Pixel", "Android")
    println("Marca: ${phone.brand} · Sistema: ${phone.os}")
    phone.turnOn()
    phone.connectToWiFi()
    phone.turnOff()
}
```

### Explicación paso a paso
1. **`Device`:** tres miembros de tres tipos distintos.
	- `brand`: propiedad sin valor, que la pondrá cada clase.
	- `turnOn()`: método **con** código por defecto, que se puede usar tal cual o cambiar.
	- `turnOff()`: método **sin** código, que cada clase está obligada a implementar.
2. **`SmartDevice : Device`:** hereda los tres y añade `os` (sin valor) y `connectToWiFi()` (con código por defecto).
3. **`Smartphone`:** al implementar `SmartDevice`, tiene que cumplir **todo** lo que falta:
	- `brand` y `os` → `override val` en el constructor.
	- `turnOff()` → obligatorio implementarlo.
	- `turnOn()` → no era obligatorio, pero el enunciado pide sobrescribir alguno con código por defecto. Llama a `super.turnOn()` para mantener el mensaje original y añade el suyo.
	- `connectToWiFi()` → no se toca: se usa el de la interfaz.
4. **`main()`:** muestra las dos propiedades y llama a los tres métodos disponibles.

> [!tip] Prueba
> ```text
> Marca: Pixel · Sistema: Android
> Turning on the device
> Pixel is booting Android
> Connecting to WiFi
> Turning off the Pixel smartphone
> ```
> Si borras `override fun turnOff()`, **no compila**. Error real de `kotlinc`: `class 'Smartphone' is not abstract and does not implement abstract member` (seguido del nombre del método que falta).

> [!note]- 🧠 Por qué funciona
> - Una interfaz es como el carné de conducir: dice qué tienes que saber hacer (frenar, girar…), pero no cómo es tu coche. `Smartphone` firma el contrato de `SmartDevice` y, con él, también el de `Device`.
> - Los métodos con código por defecto son la «configuración de fábrica»: si la clase no dice nada, se usa esa. Por eso `connectToWiFi()` funciona sin escribirlo en `Smartphone`.
> - Diferencia con una clase abstracta ([[Ejercicios Bloque 9#Ejercicio 3 · Clase abstracta `Animal`|Bloque 9]]): una clase puede implementar **varias** interfaces, pero solo puede heredar de **una** clase. Además, las interfaces no guardan estado: `brand` no tiene valor hasta que lo da la clase.

---

## Ejercicio 3 · `EventManager` con *object expressions*

> [!question] Enunciado
> Define una interfaz llamada `EventListener` para manejar eventos en una aplicación. La interfaz debe contener el método `onEventOccurred(event: String)`, que recibe una cadena con la descripción del evento.
>
> Luego, define una clase llamada `EventManager` que gestione los eventos, con los métodos:
>
> - `registerListener(listener: EventListener)`: registra un `EventListener`.
> - `triggerEvent(event: String)`: desencadena un evento, notificando a todos los `EventListener` registrados.
>
> Implementa una función `main` que:
> - Cree una instancia de `EventManager`.
> - Use una ***object expression*** para crear un `EventListener` anónimo que imprima los eventos recibidos.
> - Use otra *object expression* para crear una **subclase anónima** de `EventManager` que añada una funcionalidad adicional al método `triggerEvent()`.
> - Registre el `EventListener` y desencadene un evento llamando a `triggerEvent()`.

### Clases y métodos introducidos
- ***Object expression*** `object : Tipo { … }`: crea **un objeto de una clase sin nombre** en el momento, implementando una interfaz o heredando de una clase. Sirve cuando solo necesitas un objeto así y no merece la pena declarar una clase entera. Es como las clases anónimas de Java (`new EventListener() { … }`).
- `object : EventManager() { … }`: subclase anónima. Lleva paréntesis porque llama al constructor de la clase padre, que tiene que ser `open`.
- `mutableListOf<EventListener>()`: la lista donde el gestor guarda a quién avisar.
- **Patrón observador** (*observer*): unos objetos (los *listeners*) se apuntan a otro (el gestor) para que les avise cuando pase algo.

> **Términos explicados:** [[07 - POO II#Anonymous object expression|*object expressions*]] · [[07 - POO II#Interfaces|interfaces]] · [[06 - POO I#11. Herencia|herencia y `open`]] · [[06 - POO I#12. Sobrescribir métodos y propiedades|`override` y `super`]]

#### Ejemplo simple de funcionamiento
```kotlin
interface Greeter {
    fun greet()
}

fun main() {
    val spanish = object : Greeter {          // objeto de una clase sin nombre
        override fun greet() = println("¡Hola!")
    }
    spanish.greet()                            // ¡Hola!
}
```

### Código fuente (`Ejercicio10.3/src/Main.kt`)

```kotlin
interface EventListener {
    fun onEventOccurred(event: String)
}

// open: para poder crear subclases (también anónimas)
open class EventManager {
    private val listeners = mutableListOf<EventListener>()

    fun registerListener(listener: EventListener) {
        listeners.add(listener)
    }

    open fun triggerEvent(event: String) {
        for (listener in listeners) {
            listener.onEventOccurred(event)
        }
    }
}

fun main() {
    // Object expression 1: un EventListener anónimo
    val listener = object : EventListener {
        override fun onEventOccurred(event: String) {
            println("Evento recibido: $event")
        }
    }

    // Instancia normal de EventManager
    val manager = EventManager()
    manager.registerListener(listener)
    manager.triggerEvent("Inicio de sesión")

    // Object expression 2: subclase anónima de EventManager con funcionalidad extra
    var triggeredCount = 0
    val loggingManager = object : EventManager() {
        override fun triggerEvent(event: String) {
            triggeredCount++
            println("[LOG] Disparando evento nº $triggeredCount: \"$event\"")
            super.triggerEvent(event)
        }
    }
    loggingManager.registerListener(listener)
    loggingManager.triggerEvent("Compra realizada")
    loggingManager.triggerEvent("Cierre de sesión")
}
```

### Explicación paso a paso
1. **`EventListener`:** interfaz con un único método, `onEventOccurred`. Cualquier objeto que quiera enterarse de los eventos tiene que implementarlo.
2. **`EventManager`:** guarda los *listeners* en una lista privada. `registerListener` añade uno; `triggerEvent` recorre la lista y llama a `onEventOccurred` de cada uno. La clase y `triggerEvent` son `open` para poder sobrescribirlos.
3. **Primera *object expression*:** `object : EventListener { … }` crea el *listener* sin declarar una clase `ConsoleListener` aparte. Su respuesta a un evento es imprimirlo.
4. **Instancia normal:** `EventManager()` registra el *listener* y dispara `"Inicio de sesión"`: solo se imprime `Evento recibido: …`.
5. **Segunda *object expression*:** `object : EventManager() { … }` es una subclase anónima que sobrescribe `triggerEvent`. Antes de avisar a nadie, suma 1 a un contador e imprime una línea de registro. Después llama a `super.triggerEvent(event)` para que se haga el aviso normal.
6. **El contador:** `triggeredCount` es una variable de `main()`, y el objeto anónimo puede leerla y modificarla. Por eso cuenta 1 y luego 2.

> [!tip] Prueba
> ```text
> Evento recibido: Inicio de sesión
> [LOG] Disparando evento nº 1: "Compra realizada"
> Evento recibido: Compra realizada
> [LOG] Disparando evento nº 2: "Cierre de sesión"
> Evento recibido: Cierre de sesión
> ```
> El gestor normal solo avisa; el anónimo, además, registra y numera cada evento.

> [!note]- 🧠 Por qué funciona
> - Es como un grupo de WhatsApp: el gestor es el grupo, los *listeners* son los miembros y `triggerEvent` es mandar un mensaje. Todos los apuntados lo reciben.
> - El gestor no sabe **qué** hace cada *listener* con el evento: solo sabe que tiene un `onEventOccurred`. Gracias a la interfaz, podrías registrar otro que guardara los eventos en un fichero sin tocar `EventManager`.
> - La subclase anónima añade comportamiento **sin cambiar** la clase original: `manager` sigue funcionando como siempre. `super.triggerEvent(event)` hace que no haya que copiar el bucle de aviso.

> [!warning] Cambio respecto a la solución del boletín
> El 7.7 del boletín solo crea la subclase anónima. Aquí se crea también una instancia normal de `EventManager`, porque el enunciado pide las dos cosas («cree una instancia de `EventManager`» y «otra *object expression* para crear una subclase anónima»). Así además se ve la diferencia entre las dos.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Enum con propiedad | `enum class E(val d: String) { A("…"), B("…"); }` | Cada constante lleva su valor; `;` antes de los métodos. |
| Propiedades de un enum | `name`, `ordinal` | Nombre de la constante y posición (desde 0). |
| Todas las constantes | `E.entries` (o `E.values()`) | Lista (o array) en orden de declaración. |
| Interfaz | `interface I { val p: T; fun f(); fun g() = … }` | Contrato; puede traer código por defecto. |
| Herencia de interfaces | `interface B : A` | `B` incluye todo lo de `A`. |
| Implementar | `class C(override val p: T) : I` | Hay que implementar todo lo que no tenga código. |
| Llamar al código por defecto | `super.f()` | Reutiliza la versión de la interfaz o del padre. |
| *Object expression* | `object : Interfaz { … }` | Objeto de una clase anónima, creado en el momento. |
| Subclase anónima | `object : Clase() { override … }` | La clase padre tiene que ser `open`. |
| Patrón observador | lista de *listeners* + bucle que los avisa | El gestor avisa sin saber qué hace cada uno. |

## Relaciones

- Teoría: [[07 - POO II]] · [[06 - POO I]]
- Bloque anterior: [[Ejercicios Bloque 9]] · Bloque siguiente: [[Ejercicios Bloque 11]]
- Mismos enunciados en el boletín: [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.5 · Enumeraciones con propiedades|7.5]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.6 · Interfaces y herencia de interfaces|7.6]] · [[07.1 - Ejercicios 7 Programación Orientada a Objetos 2#Ejercicio 7.7 · Object expressions y gestión de eventos|7.7]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Declarar un enum con propiedades y un método común
- [ ] Explicar para qué sirve el `;` en un enum
- [ ] Recorrer las constantes con `entries` y usar `name` y `ordinal`
- [ ] Declarar interfaces con propiedades, métodos por defecto y métodos sin código
- [ ] Implementar una interfaz que hereda de otra y usar `super` para reutilizar el código por defecto
- [ ] Crear objetos anónimos con `object : Interfaz` y `object : Clase()`
- [ ] Explicar el patrón observador con el ejemplo de `EventManager`
