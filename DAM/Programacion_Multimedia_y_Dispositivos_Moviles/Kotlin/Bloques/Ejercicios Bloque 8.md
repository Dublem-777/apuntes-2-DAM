---
asignatura: PMDM
tema: 6
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-poo
  - DAM/pmdm/ejercicios
---

# Bloque 8 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[06 - POO I]] · [[11 - Colecciones]]
> Bloque anterior: [[Ejercicios Bloque 7]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque08/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 6.7, 6.9, 6.11, 6.13 y 6.14 de [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1|el boletín 6]].
> - **Ejercicio 1:** solución nueva; tu `Ejercicio6.7` no cumple varios puntos del enunciado (ver el aviso).
> - **Ejercicio 2:** tu `Ejercicio6.9` con la errata `programmingLenguages` corregida y un `main()` con más casos.
> - **Ejercicios 3 y 5:** tus `Ejercicio6.11` y `Ejercicio6.14`, copiados tal cual.
> - **Ejercicio 4:** tu `Ejercicio6.13` con `describe()` reescrito usando `entries`, como pide el enunciado.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque08/Ejercicio8.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · `BankAccount` con historial de solo lectura]]
- [[#Ejercicio 2 · Jerarquía de empleados]]
- [[#Ejercicio 3 · Hotel con clase anidada e interna]]
- [[#Ejercicio 4 · Singleton `ConfigurationManager`]]
- [[#Ejercicio 5 · `User` con id automático]]

---

## Ejercicio 1 · `BankAccount` con historial de solo lectura

> [!question] Enunciado
> Define una clase en Kotlin llamada `BankAccount` que tenga las siguientes propiedades y métodos:
>
> - `accountHolder`: un valor no nulo de tipo `String` que representa el nombre del titular de la cuenta.
> - `balance`: un valor de tipo `Double` que representa el saldo de la cuenta y debe ser mayor o igual a 0. Si se intenta asignar un valor negativo, el setter debe lanzar una excepción `IllegalArgumentException` con el mensaje `Balance must be non-negative`.
> - `transactionHistory`: una lista de cadenas (`MutableList<String>`) que almacena el historial de transacciones realizadas sobre la cuenta. **Desde fuera, esta propiedad solo debe ser accesible para consulta, en forma de `List<String>`.**
> - `deposit(amount: Double)`: permite depositar dinero en la cuenta. Debe validar que la cantidad sea positiva (si no, lanza `IllegalArgumentException`), actualizar el saldo y registrar la transacción en `transactionHistory`.
> - `withdraw(amount: Double)`: permite retirar dinero de la cuenta. Debe validar que la cantidad sea positiva y que el saldo sea suficiente (si no, lanza `IllegalArgumentException`), actualizar el saldo y registrar la transacción en `transactionHistory`.

### Clases y métodos introducidos
- **Propiedad de respaldo** (*backing property*): dos propiedades para un mismo dato. Una **privada** que guarda de verdad la información (`_transactionHistory`, modificable) y otra **pública** que la expone de otra forma (`transactionHistory`, de solo lectura). Por convenio, la privada empieza por `_`.
- `MutableList<String>` vs `List<String>`: la primera tiene `add`, `remove`…; la segunda solo permite consultar. Una `MutableList` **es** una `List`, así que se puede devolver como tal.
- `mutableListOf()`: crea una lista modificable vacía.
- **Setter con validación**, como en el [[Ejercicios Bloque 7#Ejercicio 3 · Clase `Product` con descuento|Bloque 7]].

> **Términos explicados:** [[06 - POO I#10. Propiedades de respaldo|propiedades de respaldo]] · [[06 - POO I#6. Getters y setters personalizados|getters y setters]] · [[06 - POO I#15. Modificadores de visibilidad|`private`]] · [[11 - Colecciones#2. Interfaces de colecciones|`List` y `MutableList`]]

#### Ejemplo simple de funcionamiento
```kotlin
class Playlist {
    private val _songs: MutableList<String> = mutableListOf()
    val songs: List<String>
        get() = _songs

    fun addSong(title: String) {
        _songs.add(title)          // desde dentro sí se puede modificar
    }
}

fun main() {
    val playlist = Playlist()
    playlist.addSong("Imagine")
    println(playlist.songs)        // [Imagine]
    // playlist.songs.add("Otra")  // ERROR: List no tiene add
}
```

### Código fuente (`Ejercicio8.1/src/Main.kt`)

```kotlin
class BankAccount(val accountHolder: String, initialBalance: Double = 0.0) {
    // El setter impide que el saldo quede negativo
    var balance: Double = initialBalance
        set(value) {
            require(value >= 0.0) { "Balance must be non-negative" }
            field = value
        }

    // Propiedad de respaldo: la lista modificable solo se ve desde dentro
    private val _transactionHistory: MutableList<String> = mutableListOf()

    // Desde fuera solo se puede consultar, como List<String>
    val transactionHistory: List<String>
        get() = _transactionHistory

    // El setter no se ejecuta al inicializar: validamos aquí el saldo inicial
    init {
        require(initialBalance >= 0.0) { "Balance must be non-negative" }
    }

    fun deposit(amount: Double) {
        require(amount > 0.0) { "Deposit amount must be positive" }
        balance += amount
        _transactionHistory.add("Deposit: $amount")
    }

    fun withdraw(amount: Double) {
        require(amount > 0.0) { "Withdrawal amount must be positive" }
        require(amount <= balance) { "Insufficient funds" }
        balance -= amount
        _transactionHistory.add("Withdraw: $amount")
    }
}

fun main() {
    val account = BankAccount("Daniel", 100.0)
    account.deposit(30.0)
    account.withdraw(10.0)
    account.withdraw(120.0)   // se queda a 0: está permitido
    println("Titular: ${account.accountHolder} · Saldo: ${account.balance}")

    try {
        account.deposit(-5.0)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
    try {
        account.withdraw(50.0)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
    try {
        account.balance = -1.0
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    println("Historial:")
    for (transaction in account.transactionHistory) {
        println("- $transaction")
    }
}
```

### Explicación paso a paso
1. **Titular:** `val accountHolder: String` en el constructor. Es propiedad, no nula y no cambia.
2. **Saldo:** `var balance` con un setter que solo acepta valores `>= 0.0`, con el mensaje exacto del enunciado. El saldo inicial (opcional, `0.0` por defecto) se valida en `init`, porque el setter no se ejecuta al inicializar.
3. **Historial (lo importante):**
   - `_transactionHistory` es `private` y `MutableList`: solo la propia clase puede añadirle cosas.
   - `transactionHistory` es pública y de tipo `List<String>`: su getter devuelve la misma lista, pero «vista» como de solo lectura. Desde fuera no hay `add`.
4. **`deposit`:** valida que la cantidad sea positiva, suma con `balance += amount` (que pasa por el setter) y apunta la operación en la lista privada.
5. **`withdraw`:** valida que la cantidad sea positiva **y** que no supere el saldo (`amount <= balance`, así se puede retirar todo). Resta y apunta la operación.
6. **Pruebas:** operaciones normales, retirar el saldo entero (se queda a 0), un depósito negativo, una retirada sin fondos, un saldo negativo asignado directamente, y por último el historial recorrido con `for`.

> [!tip] Prueba
> ```text
> Titular: Daniel · Saldo: 0.0
> Error: Deposit amount must be positive
> Error: Insufficient funds
> Error: Balance must be non-negative
> Historial:
> - Deposit: 30.0
> - Withdraw: 10.0
> - Withdraw: 120.0
> ```
> Las operaciones que fallan **no** aparecen en el historial: `require` lanza la excepción antes de llegar al `add`.
>
> Si desde `main()` intentas `account.transactionHistory.add("…")`, **no compila**. Error real de `kotlinc`: `unresolved reference 'add' on receiver of type 'List<String>'`.

> [!note]- 🧠 Por qué funciona
> - Es como el extracto del banco: tú puedes **leerlo**, pero solo el banco puede **escribir** en él. La lista privada es el registro interno del banco; la pública es el extracto que te enseñan.
> - No se copia la lista: `transactionHistory` devuelve **el mismo objeto**, pero con un tipo (`List`) que no tiene métodos para modificarlo. Por eso siempre está al día.
> - El orden dentro de `deposit` y `withdraw` importa: primero se valida, luego se cambia el saldo y por último se apunta. Si falla una validación, no se toca nada.

> [!warning] Tu proyecto `Ejercicio6.7`
> Diferencias con este enunciado (comprobadas al ejecutarlo):
> 1. `transactionHistory` es un `String` construido con `+=`, no una `MutableList<String>` expuesta como `List<String>`.
> 2. El setter usa `require(value > 0)` con el mensaje `"Value must be non-negative"`: **`account.balance = 0.0` lanza la excepción**, y el mensaje no es el que pide el enunciado.
> 3. `withdraw` comprueba `balance > amount`: con 120 € **no deja retirar 120 €** («Insufficient funds»).
> 4. `accountHolder` no lleva `val`, así que no es una propiedad.

---

## Ejercicio 2 · Jerarquía de empleados

> [!question] Enunciado
> Diseña una jerarquía de clases para representar empleados en una empresa. La jerarquía debe incluir **al menos tres niveles** de clases, utilizando herencia para representar diferentes tipos de empleados:
>
> - **`Employee`** (clase base):
> 	- `name`: un valor no nulo de tipo `String` que representa el nombre del empleado.
> 	- `id`: un valor de tipo `Int` que representa el identificador del empleado.
> 	- `getDetails()`: un método que devuelve una cadena con el nombre y el id del empleado.
> - **`Manager`** (subclase de `Employee`):
> 	- `department`: un valor no nulo de tipo `String` que representa el departamento que gestiona.
> 	- `getDetails()`: sobrescribe el de la clase base para incluir el departamento.
> - **`Developer`** (subclase de `Employee`):
> 	- `programmingLanguages`: un `vararg` de cadenas con los lenguajes de programación que conoce.
> 	- `getDetails()`: sobrescribe el de la clase base para incluir los lenguajes de programación.

### Clases y métodos introducidos
- `open class`: en Kotlin las clases son **cerradas por defecto** (como `final` en Java). Solo se puede heredar de una clase marcada como `open`.
- `class Manager(…) : Employee(name, id)`: herencia. Tras los dos puntos se llama al **constructor de la clase padre**.
- `open fun` / `override fun`: el método del padre se marca como `open` para poder sobrescribirlo, y el del hijo como `override` (obligatorio, no es una anotación opcional como `@Override` en Java).
- `super.getDetails()`: llama a la versión del padre para reutilizarla.
- `vararg` en el constructor: `Developer("Lucía", 3, "Kotlin", "Java", "Python")`.

> **Términos explicados:** [[06 - POO I#11. Herencia|herencia y `open`]] · [[06 - POO I#12. Sobrescribir métodos y propiedades|`override` y `super`]] · [[03 - Funciones#9. varargs|`vararg`]]

#### Ejemplo simple de funcionamiento
```kotlin
open class Animal(val name: String) {
    open fun speak(): String = "$name hace un ruido"
}

class Dog(name: String) : Animal(name) {
    override fun speak(): String = "${super.speak()}: ¡guau!"
}

fun main() {
    println(Dog("Rex").speak())   // Rex hace un ruido: ¡guau!
}
```

### Código fuente (`Ejercicio6.9/src/Main.kt`, con la errata corregida)

```kotlin
open class Person(val name: String)

open class Employee(name: String, val id: Int): Person(name) {
    open fun getDetails(): String = "Empleado: $name (ID: $id)"
}

class Manager(
    name: String,
    id: Int,
    val department: String,
): Employee(name, id) {
    override fun getDetails(): String = "${super.getDetails()}, departamento: $department"
}

class Developer(
    name: String,
    id: Int,
    vararg programmingLanguages: String,
): Employee(name, id) {
    private var languageText = ""

    init {
        for (language in programmingLanguages) {
            if (languageText != "") {
                languageText += ", "
            }
            languageText += language
        }
    }

    override fun getDetails(): String = "${super.getDetails()}, lenguajes: $languageText"
}

fun main() {
    val employees: List<Employee> = listOf(
        Employee("Laura", 1),
        Manager("Daniel", 2, "Desarrollo"),
        Developer("Lucía", 3, "Kotlin", "Java", "Python"),
    )
    employees.forEach { println(it.getDetails()) }
}
```

### Explicación paso a paso
1. **Tres niveles:** `Person` (nivel 1) → `Employee` (nivel 2) → `Manager` y `Developer` (nivel 3). Con solo las tres clases del enunciado habría dos niveles, así que `Person` aporta el tercero y, de paso, la propiedad `name`.
2. **`Employee`:** recibe `name` y se lo pasa a `Person`; añade `id` como propiedad. `getDetails()` es `open` para que los hijos puedan cambiarla.
3. **`Manager`:** añade `department` y sobrescribe `getDetails()`. Con `super.getDetails()` reutiliza el texto del padre y solo añade el departamento.
4. **`Developer`:** recibe los lenguajes como `vararg`. En el `init` los une en un texto separado por comas (solo pone `", "` si ya había algo antes) y lo guarda en `languageText`, que usa su `getDetails()`.
5. **`main()`:** guarda los tres tipos en una `List<Employee>` y llama a `getDetails()` sobre cada uno.

> [!tip] Prueba
> ```text
> Empleado: Laura (ID: 1)
> Empleado: Daniel (ID: 2), departamento: Desarrollo
> Empleado: Lucía (ID: 3), lenguajes: Kotlin, Java, Python
> ```

> [!note]- 🧠 Por qué funciona
> - **Polimorfismo:** la lista es de tipo `List<Employee>`, pero cada objeto ejecuta **su propia** versión de `getDetails()`. Kotlin decide en tiempo de ejecución qué versión usar según el objeto real, no según el tipo de la variable.
> - `super.getDetails()` evita repetir el formato `"Empleado: … (ID: …)"` en cada hija. Si mañana cambias el formato en `Employee`, cambia en todas.
> - El `vararg` solo existe dentro del constructor: por eso se procesa en el `init` y se guarda en `languageText`, que sí es una propiedad.

> [!warning] Cambios respecto a tu proyecto
> - El parámetro se llamaba `programmingLenguages` y el texto decía `lenguages`. Ahora es `programmingLanguages`, como en el enunciado, y el texto dice `lenguajes`.
> - El `main()` original solo probaba `Manager` y un `Developer` con un único lenguaje. Este añade un `Employee` normal y un `Developer` con tres lenguajes, para ver las comas.
>
> `forEach { println(it.getDetails()) }` es una lambda: se explica en el [[10 - Programación funcional|Tema 10]]. Equivale a `for (employee in employees) println(employee.getDetails())`.

---

## Ejercicio 3 · Hotel con clase anidada e interna

> [!question] Enunciado
> Define un sistema para gestionar reservas en un hotel. El sistema debe incluir las siguientes clases:
>
> - **`Hotel`** (clase principal):
> 	- `name`: un valor no nulo de tipo `String` que representa el nombre del hotel.
> 	- `roomCount`: un valor de tipo `Int` que representa el número total de habitaciones.
> 	- `getHotelInfo()`: devuelve la información del hotel, con el nombre y el número de habitaciones.
> - **`Reservation`** (clase anidada **estática** dentro de `Hotel`):
> 	- `guestName`: un valor no nulo de tipo `String` con el nombre del huésped.
> 	- `roomNumber`: un valor de tipo `Int` con el número de habitación reservada.
> 	- `getReservationDetails()`: devuelve los detalles de la reserva, con el nombre del huésped y el número de habitación.
> - **`Employee`** (clase anidada **no estática** dentro de `Hotel`):
> 	- `employeeName`: un valor no nulo de tipo `String` con el nombre del empleado.
> 	- `position`: un valor de tipo `String` con el cargo del empleado en el hotel.
> 	- `getEmployeeDetails()`: devuelve los detalles del empleado, con el nombre y el cargo.
> 	- `getEmployeeTotalRooms()`: devuelve el número total de habitaciones del hotel en el que trabaja el empleado.
>
> Define una función `main()` que llame a los métodos de las clases descritas.

### Clases y métodos introducidos
- **Clase anidada** (`class` dentro de otra): en Kotlin es la «estática» de Java. **No** tiene acceso al objeto de fuera y se crea sin él: `Hotel.Reservation(…)`.
- **Clase interna** (`inner class`): la «no estática». Cada objeto va **ligado a un objeto de la clase externa** y puede usar sus propiedades. Se crea a partir de él: `hotelA.Employee(…)`.
- `this@Hotel`: «el `Hotel` al que pertenezco». Sirve para referirse al objeto externo desde la clase interna.

> **Términos explicados:** [[06 - POO I#13. Clases anidadas|clases anidadas]] · [[06 - POO I#14. Clases internas|clases internas e `inner`]]

#### Ejemplo simple de funcionamiento
```kotlin
class School(val name: String) {
    class Subject(val title: String)                 // anidada: no conoce a School
    inner class Student(val studentName: String) {   // interna: conoce a su School
        fun info() = "$studentName estudia en $name"
    }
}

fun main() {
    val subject = School.Subject("Kotlin")           // sin objeto School
    val school = School("IES El Saladillo")
    println(school.Student("Daniel").info())          // Daniel estudia en IES El Saladillo
}
```

### Código fuente (`Ejercicio6.11/src/Main.kt`)

```kotlin
class Hotel(val name: String, val roomCount: Int) {
    init {
        require(roomCount >= 0) {"roomCount cannot be negative"}
    }
    fun getHotelInfo(): String = "$name: $roomCount habitaciones"

    class Reservation(val guestName: String, val roomNumber: Int) {
        fun getReservationDetails(): String = "$guestName: habitación $roomNumber"
    }

    inner class Employee(val employeeName: String, val position: String) {
        fun getEmployeeDetails(): String = "$employeeName: $position"
        fun getEmployeeTotalRooms(): Int = this@Hotel.roomCount
    }
}

fun main() {
    val hotelA = Hotel("Hotel A", 200)
    println(hotelA.getHotelInfo())

    val reservationA = Hotel.Reservation("Daniel", 130)
    println(reservationA.getReservationDetails())

    val employeeA = hotelA.Employee("Paco", "Camarero")
    println(employeeA.getEmployeeDetails())
    println(employeeA.getEmployeeTotalRooms())
}
```

### Explicación paso a paso
1. **`Hotel`:** propiedades `name` y `roomCount` en el constructor, con una validación extra en `init` (no puede haber habitaciones negativas) y `getHotelInfo()`.
2. **`Reservation`:** es `class` a secas dentro de `Hotel`, es decir, **anidada (estática)**. Una reserva tiene sus propios datos y no necesita saber nada del hotel, así que se crea con `Hotel.Reservation("Daniel", 130)`, sin ningún hotel.
3. **`Employee`:** es `inner class`, es decir, **interna (no estática)**. Cada empleado trabaja en un hotel concreto, así que se crea a partir de él: `hotelA.Employee("Paco", "Camarero")`.
4. **`getEmployeeTotalRooms()`:** como `Employee` es interna, puede leer `roomCount` del hotel al que pertenece con `this@Hotel.roomCount`. Una clase anidada normal no podría.
5. **`main()`:** llama a los cuatro métodos que pide el enunciado.

> [!tip] Prueba
> ```text
> Hotel A: 200 habitaciones
> Daniel: habitación 130
> Paco: Camarero
> 200
> ```

> [!note]- 🧠 Por qué funciona
> - Un objeto de una `inner class` guarda por dentro una referencia al objeto externo que lo creó. Por eso `employeeA` «sabe» que trabaja en `hotelA` y puede leer sus 200 habitaciones.
> - Si quitas `inner`, la línea `this@Hotel.roomCount` deja de compilar: una clase anidada no tiene objeto externo al que referirse.
> - **Ojo, es al revés que en Java.** En Java, una clase dentro de otra es interna por defecto y hay que escribir `static` para que no lo sea. En Kotlin es anidada por defecto y hay que escribir `inner` para que sea interna.

---

## Ejercicio 4 · Singleton `ConfigurationManager`

> [!question] Enunciado
> Define un singleton `ConfigurationManager` que administre la configuración global de una aplicación. Usará un mapa privado `MutableMap<String, String>`, que se puede crear con la función `mutableMapOf()`. El `ConfigurationManager` debe permitir:
>
> - Almacenar un par clave-valor de configuración.
> - Obtener el valor asociado a una clave de configuración.
> - Obtener una cadena que represente el estado actual de todas las configuraciones almacenadas, usando la propiedad **`entries`** del mapa.

### Clases y métodos introducidos
- `object`: declara una clase y su **única instancia** a la vez (singleton). No se crea con `ConfigurationManager()`: se usa directamente por su nombre, `ConfigurationManager.set(…)`.
- `mutableMapOf<String, String>()`: crea un mapa (diccionario) modificable vacío. Cada **clave** tiene asociado un **valor**, como un `HashMap` de Java.
- `map[key] = value`: guarda un par. Si la clave ya existía, **sustituye** el valor.
- `map[key]`: devuelve el valor de esa clave o `null` si no existe. Por eso el tipo de retorno es `String?`.
- `map.entries`: todos los pares del mapa. Cada `entry` tiene `entry.key` y `entry.value`.

> **Términos explicados:** [[06 - POO I#16. Declaraciones de objetos|`object` (singleton)]] · [[11 - Colecciones#3. Creación de colecciones|crear un mapa]] · [[11 - Colecciones#5. Operadores sobrecargados en colecciones|operador `[]` en mapas]] · [[06 - POO I#15. Modificadores de visibilidad|`private`]]

#### Ejemplo simple de funcionamiento
```kotlin
val ages = mutableMapOf<String, Int>()
ages["Ana"] = 20
ages["Luis"] = 31
println(ages["Ana"])      // 20
println(ages["Pepe"])     // null
for (entry in ages.entries) println("${entry.key} tiene ${entry.value} años")
```

### Código fuente (`Ejercicio6.13/src/Main.kt`, con `describe()` usando `entries`)

```kotlin
object ConfigurationManager {
    private val settings = mutableMapOf<String, String>()

    fun set(key: String, value: String) {
        settings[key] = value
    }

    fun get(key: String): String? = settings[key]

    fun describe(): String {
        var text = ""
        // entries: cada par clave-valor del mapa
        for (entry in settings.entries) {
            text += "${entry.key} = ${entry.value}\n"
        }
        return text
    }
}

fun main() {
    ConfigurationManager.set("Theme", "dark")
    ConfigurationManager.set("language", "es")
    ConfigurationManager.set("Theme", "light")   // misma clave: se sustituye el valor

    println(ConfigurationManager.get("Theme"))
    println(ConfigurationManager.get("fontSize"))   // clave que no existe
    print(ConfigurationManager.describe())
}
```

### Explicación paso a paso
1. **Singleton:** `object ConfigurationManager` garantiza que solo hay **una** configuración en toda la aplicación. Da igual desde dónde la uses: siempre es la misma.
2. **Mapa privado:** `settings` es `private`, así que nadie puede tocarlo directamente; solo a través de los tres métodos.
3. **`set`:** `settings[key] = value` guarda el par. Volver a guardar `"Theme"` sustituye `"dark"` por `"light"`, porque en un mapa las claves no se repiten.
4. **`get`:** devuelve `settings[key]`, que es `null` si la clave no existe.
5. **`describe`:** recorre `settings.entries` y construye una línea `clave = valor` por cada par.

> [!tip] Prueba
> ```text
> light
> null
> Theme = light
> language = es
> ```

> [!note]- 🧠 Por qué funciona
> - `object` crea la instancia la primera vez que se usa y ya no se crea ninguna más: es como el tablón de anuncios de una clase, solo hay uno y todos leen y escriben en él.
> - El mapa funciona como un diccionario: buscas por la palabra (clave) y obtienes la definición (valor). Por eso `get` es inmediato y no hace falta recorrer nada.
> - `entries` es la forma de recorrer el mapa cuando necesitas **a la vez** la clave y el valor de cada par.

> [!warning] Cambio respecto a tu proyecto
> Tu `describe()` devolvía `settings.toString()`, que da `{Theme=light, language=es}`. Funciona, pero el enunciado pide usar la propiedad `entries`, y aquí está reescrito así. Además, el `main()` añade la sustitución de una clave y la consulta de una que no existe.

---

## Ejercicio 5 · `User` con id automático

> [!question] Enunciado
> Define una clase `User` de manera que el valor de su propiedad `id` se calcule automáticamente: el primer objeto que se cree de la clase `User` tendrá como id el 1, el segundo el 2, y así sucesivamente, **sin que el código que instancia la clase `User` tenga que hacer ningún cálculo**.

### Clases y métodos introducidos
- `companion object`: un objeto **compartido por todos los objetos de la clase**. Es lo que en Java sería lo `static`: hay una sola copia de su contenido para toda la clase.
- `nextIdValue++` (post-incremento): devuelve el valor **actual** y después le suma 1.
- `private` en el *companion*: el contador no se puede tocar desde fuera de la clase.

> **Términos explicados:** [[06 - POO I#17. Objetos compañeros|`companion object`]] · [[06 - POO I#15. Modificadores de visibilidad|`private`]]

#### Ejemplo simple de funcionamiento
```kotlin
class Ticket {
    companion object {
        var sold = 0          // una sola variable para todos los tickets
    }
    init {
        sold++
    }
}

fun main() {
    Ticket(); Ticket()
    println(Ticket.sold)      // 2
}
```

### Código fuente (`Ejercicio6.14/src/Main.kt`)

```kotlin
class User {
    val id: Int = nextId()

    companion object {
        private var nextIdValue = 1
        private fun nextId(): Int = nextIdValue++
    }
}

fun main() {
    val first = User()
    val second = User()
    val third = User()

    println(first.id)
    println(second.id)
    println(third.id)
}
```

### Explicación paso a paso
1. **Contador compartido:** `nextIdValue` vive en el `companion object`, así que hay **uno solo** para toda la clase. Empieza en 1.
2. **`nextId()`:** devuelve el valor actual del contador y lo incrementa (`nextIdValue++`). El primer `User` recibe 1 y el contador pasa a 2; el siguiente recibe 2 y pasa a 3…
3. **`val id = nextId()`:** se ejecuta al crear cada `User`. El código de `main()` solo escribe `User()`: no calcula nada.
4. **`private`:** ni el contador ni `nextId()` son accesibles desde fuera, así que nadie puede «saltarse» números o repetirlos.

> [!tip] Prueba
> ```text
> 1
> 2
> 3
> ```

> [!note]- 🧠 Por qué funciona
> - Es como la máquina de turnos de la carnicería: la máquina es una sola (el *companion*) y cada cliente que llega (`User()`) coge el siguiente número.
> - Si `nextIdValue` fuera una propiedad normal de `User`, cada objeto tendría **su propio** contador empezando en 1, y todos los usuarios tendrían id 1.
> - `id` es `val`: una vez asignado, el id de un usuario ya no cambia.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Propiedad de respaldo | `private val _x: MutableList<T>` + `val x: List<T> get() = _x` | Se modifica por dentro y solo se consulta por fuera. |
| Herencia | `open class A` · `class B : A(…)` | Las clases son cerradas por defecto; hace falta `open`. |
| Sobrescribir | `open fun` · `override fun` · `super.f()` | El hijo cambia el método y puede reutilizar el del padre. |
| Polimorfismo | `val e: Employee = Manager(…)` | Se ejecuta la versión del objeto real. |
| Clase anidada | `class A { class B }` → `A.B()` | «Estática»: no conoce al objeto externo. |
| Clase interna | `class A { inner class B }` → `a.B()` | Ligada a un objeto `A`; accede con `this@A`. |
| Singleton | `object Nombre { … }` | Una única instancia, accesible por su nombre. |
| Mapa | `mutableMapOf<K, V>()` · `m[k] = v` · `m[k]` | Clave → valor; `m[k]` da `null` si no existe. |
| Recorrer un mapa | `for (e in m.entries)` | `e.key` y `e.value` de cada par. |
| Miembros de clase | `companion object { … }` | Una copia compartida por todos los objetos (el `static` de Java). |

## Relaciones

- Teoría: [[06 - POO I]] · [[11 - Colecciones]]
- Bloque anterior: [[Ejercicios Bloque 7]] · Bloque siguiente: [[Ejercicios Bloque 9]]
- Mismos enunciados en el boletín: [[06.1 - Ejercicios 6 Programación Orientada a Objetos 1]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Exponer una `MutableList` privada como `List` de solo lectura
- [ ] Validar en el setter y en `init`, y explicar por qué hacen falta los dos
- [ ] Crear una jerarquía con `open`, `override` y `super`
- [ ] Diferenciar clase anidada e `inner class`, y cómo se instancia cada una
- [ ] Declarar un singleton con `object` y usar un mapa con `[]` y `entries`
- [ ] Generar ids automáticos con un `companion object`
