---
asignatura: PMDM
tema: 5
tipo: ejercicio
estado: completo
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/kotlin-nullables
  - DAM/pmdm/ejercicios
---

# Bloque 6 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[05 - Operaciones con tipos nullables]] · [[06 - POO I]] · [[03 - Funciones]]
> Bloque anterior: [[Ejercicios Bloque 5]]
> **Ruta fuente (boletín):** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Tema5-OperacionesConTiposNullables/` (`Ejercicio5.2/src/Main2.kt`, `Ejercicio5.4`, `Ejercicio5.7`)
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque06/`

> [!note] Sobre las soluciones
> - Son los mismos enunciados que los ejercicios 5.2, 5.4 y 5.7 de [[05.1 - Ejercicios 5 Operaciones con tipos nullables|el boletín 5]].
> - **Ejercicio 1:** tu código de `Ejercicio5.2/src/Main2.kt`, con una prueba corregida (ver el aviso del ejercicio).
> - **Ejercicio 2:** solución nueva, porque tu `Ejercicio5.4` no sigue el formato `Nickname: <nickname>` que pide este enunciado (ver el aviso).
> - **Ejercicio 3:** tu código de `Ejercicio5.7`, copiado tal cual.
> - Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque06/Ejercicio6.K/` (ver **Ruta fuente**).
> - Todo el código se ha **compilado y ejecutado** con `kotlinc` 2.4; las salidas de las pruebas son reales.

---

## Índice de Ejercicios

- [[#Ejercicio 1 · `getNameLength` con llamadas seguras]]
- [[#Ejercicio 2 · `formatName` con el operador Elvis]]
- [[#Ejercicio 3 · `sumIfAllIntegers` con `vararg` y `as?`]]

---

## Ejercicio 1 · `getNameLength` con llamadas seguras

> [!question] Enunciado
> Crea una clase llamada `Person` que contenga una propiedad `name` de tipo `String?` (ver tema *POO I*). Escribe una función en Kotlin llamada `getNameLength` que acepte un objeto de tipo `Person?` y devuelva la longitud del nombre si el objeto no es `null`, o `0` si el objeto es `null` o si el nombre dentro del objeto es `null`. Para ello debe usar el **operador de llamada segura**.

### Clases y métodos introducidos
- `class Person(val name: String?)`: clase con **constructor primario**. El `val` delante del parámetro lo convierte directamente en una propiedad. En Java harían falta el atributo, el constructor y el getter.
- `Person?` y `String?`: el `?` indica que la variable puede valer `null`. Sin `?`, el compilador no deja asignarle `null`.
- **Llamada segura** `?.`: `person?.name` devuelve `name` si `person` existe, o `null` si `person` es `null`, sin lanzar `NullPointerException`.
- **Elvis** `?:`: da un valor por defecto cuando lo de la izquierda es `null`.

> **Términos explicados:** [[06 - POO I#2. Constructor primario y bloques de inicialización|constructor primario]] · [[05 - Operaciones con tipos nullables#2. Operador de llamada segura `?.`|llamada segura]] · [[05 - Operaciones con tipos nullables#3. Operador Elvis `?:`|operador Elvis]]

#### Ejemplo simple de funcionamiento
```kotlin
val text: String? = null
println(text?.length)        // null (no lanza excepción)
println(text?.length ?: 0)   // 0
```

### Código fuente (`Ejercicio5.2/src/Main2.kt`)

```kotlin
class Person(val name: String?)

fun getNameLength(person: Person?): Int {
    return person?.name?.length ?: 0
}

fun main() {
    val person1: Person? = Person("Ana")
    val person2: Person? = Person(null)
    val person3: Person? = null

    println(getNameLength(person1))
    println(getNameLength(person2))
    println(getNameLength(person3))
}
```

### Explicación paso a paso
1. **La clase:** `Person` tiene una única propiedad, `name`, que puede ser `null` (una persona de la que no sabemos el nombre).
2. **La cadena de llamadas seguras:** `person?.name?.length` se lee de izquierda a derecha. Si `person` es `null`, se para y da `null`; si no, mira `name`. Si `name` es `null`, se para y da `null`; si no, da su `length`.
3. **Elvis al final:** el resultado de la cadena es `Int?`, porque puede ser `null`. `?: 0` lo convierte en `Int` devolviendo `0` en los dos casos de `null`.
4. **Pruebas:** los tres casos del enunciado: persona con nombre, persona sin nombre y persona `null`.

> [!tip] Prueba
> ```text
> 3
> 0
> 0
> ```
> `"Ana"` tiene 3 letras; los otros dos casos devuelven 0.

> [!note]- 🧠 Por qué funciona
> - Es como preguntar «¿cuánto mide el nombre de la persona?» con dos «si existe» encadenados: si no hay persona o no hay nombre, la respuesta es «nada» (`null`), y Elvis la cambia por 0.
> - Si escribieras `person.name.length` sin `?`, **no compilaría**: Kotlin detecta en tiempo de compilación que `person` y `name` pueden ser `null`. En Java, ese mismo código compilaría y fallaría al ejecutarlo con un `NullPointerException`.

> [!warning] Cambio respecto a tu proyecto
> En `Ejercicio5.2/src/Main2.kt`, `person3` está declarado como `Person(null)`, igual que `person2`, así que **el caso de una persona `null` nunca se probaba**. Aquí está corregido como `val person3: Person? = null`. La función `getNameLength` es exactamente la tuya.
>
> Ojo también: en esa carpeta, `Main.kt` contiene el ejercicio del mapa de configuración (`getConfigValue`, el 5.3) y `Main2.kt` este ejercicio.

---

## Ejercicio 2 · `formatName` con el operador Elvis

> [!question] Enunciado
> Escribe una función en Kotlin llamada `formatName` que acepte tres parámetros: un nombre (`firstName`), un apellido (`lastName`) y un apodo (`nickname`). Los parámetros `lastName` y `nickname` pueden ser `null`. La función debe devolver una cadena que siga estas reglas:
>
> - Si se proporciona el `nickname`, el formato debe ser `Nickname: <nickname>`.
> - Si no se proporciona el `nickname`, pero sí el `lastName`, el formato debe ser `<firstName> <lastName>`.
> - Si no se proporciona ni el `nickname` ni el `lastName`, el formato debe ser solo `<firstName>`.
>
> La función debe utilizar el **operador Elvis (`?:`)** para manejar los valores predeterminados de `nickname` y `lastName`.

### Clases y métodos introducidos
- **Elvis con un valor por defecto**: `lastName ?: ""` usa el apellido o, si es `null`, una cadena vacía.
- **Elvis con `return`**: `nickname ?: return fullName`. Si `nickname` es `null`, la función **termina ahí** y devuelve `fullName`. Funciona porque `return` es una expresión de tipo `Nothing` y puede ir a la derecha de `?:`.
- `String.trimEnd()`: quita los espacios del final de la cadena.

> **Términos explicados:** [[05 - Operaciones con tipos nullables#3. Operador Elvis `?:`|operador Elvis, también con `return`]] · [[03 - Funciones#4. Los tipos Nothing y Nothing?|el tipo `Nothing`]] · [[02 - Jerarquia de tipos#6. Strings|plantillas de cadena]]

#### Ejemplo simple de funcionamiento
```kotlin
fun greet(name: String?): String {
    val validName: String = name ?: return "Hola, desconocido"
    return "Hola, $validName"
}
// greet("Ana") → "Hola, Ana" · greet(null) → "Hola, desconocido"
```

### Código fuente (`Ejercicio6.2/src/Main.kt`)

```kotlin
fun formatName(firstName: String, lastName: String?, nickname: String?): String {
    // Elvis: si no hay apellido se usa "" y trimEnd() quita el espacio sobrante
    val fullName: String = "$firstName ${lastName ?: ""}".trimEnd()

    // Elvis con return: si no hay apodo, se devuelve el nombre completo
    val validNickname: String = nickname ?: return fullName
    return "Nickname: $validNickname"
}

fun main() {
    println(formatName("Ada", "Lovelace", "Enchantress"))
    println(formatName("Ada", "Lovelace", null))
    println(formatName("Ada", null, null))
    println(formatName("Ada", null, "Countess"))
}
```

### Explicación paso a paso
1. **Nombre completo:** `"$firstName ${lastName ?: ""}"` da `"Ada Lovelace"` si hay apellido, o `"Ada "` (con un espacio al final) si no lo hay. `trimEnd()` quita ese espacio y deja `"Ada"`. Así cubrimos las reglas 2 y 3 con una sola línea.
2. **El apodo:** `nickname ?: return fullName` funciona como una «puerta». Si no hay apodo, la función sale devolviendo el nombre completo. Si lo hay, `validNickname` recibe el apodo ya como `String` (no nullable).
3. **Regla 1:** si llegamos a la última línea es que hay apodo, así que devolvemos `"Nickname: $validNickname"`.
4. **Pruebas:** las tres reglas y un caso extra: apodo sin apellido, para comprobar que el apodo manda aunque falte el apellido.

> [!tip] Prueba
> ```text
> Nickname: Enchantress
> Ada Lovelace
> Ada
> Nickname: Countess
> ```

> [!note]- 🧠 Por qué funciona
> - El enunciado tiene una **prioridad**: primero el apodo y, si no, el nombre. El `?: return` la respeta: se calcula el nombre completo por si hace falta, pero solo se devuelve cuando no hay apodo.
> - Después de `val validNickname: String = nickname ?: return fullName`, el compilador **sabe** que `validNickname` no es `null` (por eso su tipo es `String` y no `String?`): si lo fuera, ya habríamos salido de la función.
> - Los dos `?:` hacen de «valor por defecto», como pide el enunciado: `""` para el apellido y `fullName` para el apodo.

> [!warning] Diferencia con tu proyecto
> Tu `Ejercicio5.4` devuelve `nickname ?: (lastName?.let { "$firstName $it" } ?: firstName)`. Con apodo devuelve solo `"Enchantress"`, **sin** el prefijo `Nickname: ` que exige este enunciado (el del boletín 5 no lo pedía). Además usa `let`, que no aparece en los apuntes del Tema 5. Si quieres mantener tu estilo, bastaría con cambiar el principio por `nickname?.let { "Nickname: $it" } ?: …`.

---

## Ejercicio 3 · `sumIfAllIntegers` con `vararg` y `as?`

> [!question] Enunciado
> Escribe una función en Kotlin llamada `sumIfAllIntegers` que acepte una cantidad variable de argumentos de tipo `Any` usando `vararg`. La función debe intentar convertir todos los argumentos a enteros (`Int`) usando el **operador seguro de conversión `as?`**. Si todos los argumentos se pueden convertir a enteros, debe devolver la suma de esos enteros. Si alguno no se puede convertir, debe devolver `null`.

### Clases y métodos introducidos
- `vararg values: Any`: lista variable de argumentos de **cualquier tipo**.
- **Cast seguro** `as?`: `value as? Int` devuelve el valor como `Int` si lo es, o `null` si no lo es, **sin lanzar excepción**. El cast normal `as` lanzaría `ClassCastException`.
- **Elvis con `return null`**: `value as? Int ?: return null` sale de la función en cuanto un valor no es `Int`.
- Tipo de retorno `Int?`: la función puede devolver una suma o `null`.

> **Términos explicados:** [[05 - Operaciones con tipos nullables#5. Operadores de cast `as` y `as?`|`as` y `as?`]] · [[05 - Operaciones con tipos nullables#3. Operador Elvis `?:`|Elvis con `return`]] · [[03 - Funciones#9. varargs|`vararg`]]

#### Ejemplo simple de funcionamiento
```kotlin
val a: Any = 42
val b: Any = "42"
println(a as? Int)   // 42
println(b as? Int)   // null (es un String, aunque parezca un número)
println(b as Int)    // ClassCastException
```

### Código fuente (`Ejercicio5.7/src/Main.kt`)

```kotlin
fun sumIfAllIntegers(vararg values: Any): Int? {
    var sum = 0

    for (value in values) {
        val integer = value as? Int ?: return null
        sum += integer
    }

    return sum
}

fun main() {
    println(sumIfAllIntegers(1, 2, 3, 4))
    println(sumIfAllIntegers(1, 2, "3", 4))
}
```

### Explicación paso a paso
1. **Firma:** `vararg values: Any` acepta enteros, cadenas, decimales… en cualquier cantidad. Devuelve `Int?` porque a veces la respuesta es «no se puede» (`null`).
2. **Recorrido:** para cada valor se intenta el cast seguro `value as? Int`.
3. **Si el cast falla:** da `null`, y Elvis ejecuta `return null`. La función termina sin mirar los demás argumentos.
4. **Si el cast funciona:** `integer` ya es un `Int` no nullable y se suma.
5. **Final:** si el bucle termina, todos eran `Int` y se devuelve la suma.

> [!tip] Prueba
> ```text
> 10
> null
> ```
> `1 + 2 + 3 + 4 = 10`. En la segunda llamada, `"3"` es un `String` (aunque contenga un número), así que el resultado es `null`.
>
> Pruebas extra con el mismo código: `sumIfAllIntegers()` → `0` (sin argumentos, el bucle no da ninguna vuelta), `sumIfAllIntegers(10, 2.5)` → `null` y `sumIfAllIntegers(5L, 1)` → `null`.

> [!note]- 🧠 Por qué funciona
> - `as?` + `?: return null` es la forma corta de: «intenta tratarlo como entero; si no puedes, abandona». Equivale a `if (value !is Int) return null`, seguido de usar `value` como `Int`.
> - `as?` **no convierte**, solo comprueba el tipo real: `"3"` no se transforma en `3` (para eso estaría `toInt()`), y `5L` (un `Long`) tampoco es un `Int`, aunque sea entero.
> - Al salir en el primer fallo, no se pierde tiempo sumando el resto: el resultado ya va a ser `null`.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Comportamiento fundamental |
| --- | --- | --- |
| Tipo nullable | `String?`, `Person?` | Puede valer `null`; el compilador obliga a tratarlo. |
| Propiedad en el constructor | `class Person(val name: String?)` | El `val` crea la propiedad directamente. |
| Llamada segura | `a?.b?.c` | Si algo es `null`, toda la cadena da `null`. |
| Elvis | `x ?: valorPorDefecto` | Usa la izquierda si no es `null`; si no, la derecha. |
| Elvis con salida | `x ?: return y` | Sale de la función si `x` es `null`; si no, `x` queda no nullable. |
| Cast seguro | `valor as? Int` | El valor como `Int` o `null`; nunca lanza excepción. |
| Cast inseguro | `valor as Int` | Lanza `ClassCastException` si no es `Int`. |
| Quitar espacios finales | `texto.trimEnd()` | `"Ada "` → `"Ada"`. |

## Relaciones

- Teoría: [[05 - Operaciones con tipos nullables]] · [[06 - POO I]] · [[03 - Funciones]]
- Bloque anterior: [[Ejercicios Bloque 5]] · Bloque siguiente: [[Ejercicios Bloque 7]]
- Mismos enunciados en el boletín: [[05.1 - Ejercicios 5 Operaciones con tipos nullables]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Declarar una propiedad nullable en el constructor primario
- [ ] Encadenar llamadas seguras y cerrar con Elvis
- [ ] Usar `?: return` para salir de una función cuando falta un valor
- [ ] Diferenciar `as` de `as?`
- [ ] Explicar por qué `"3" as? Int` y `5L as? Int` dan `null`
