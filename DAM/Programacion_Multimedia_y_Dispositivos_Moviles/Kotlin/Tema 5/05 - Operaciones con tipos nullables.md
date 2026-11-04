---
asignatura: PMDM
tema: 5
tipo: tema
estado: completo
fecha: 2026-09-30
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-nullables
---

# 5 · Operaciones con tipos nullables en Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 5 · Kotlin  
> Material de referencia: [Operaciones con tipos nullables en Kotlin](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b05%20-%20Operaciones%20con%20tipos%20nullables%20en%20Kotlin/)

## Índice del tema

- [[#1. Smart cast hacia tipos no nullables]]
- [[#2. Operador de llamada segura `?.`]]
- [[#3. Operador Elvis `?:`]]
- [[#4. Operador de aserción no nula `!!`]]
- [[#5. Operadores de cast `as` y `as?`]]

---

## 1. Smart cast hacia tipos no nullables

Una variable nullable, como `String?`, puede contener una cadena o `null`. No se puede acceder directamente a sus propiedades o métodos sin demostrar antes que el valor no es nulo.

Una comprobación explícita permite al compilador aplicar un **smart cast**: dentro de la rama donde se sabe que la variable no es `null`, se trata como su tipo no nullable.

```kotlin
val texto: String? = if (random.nextBoolean()) null else "Kotlin"

val longitud = if (texto != null) texto.length else 0
```

También se puede aprovechar el cortocircuito de `&&`: la expresión de la derecha solo se evalúa si `texto != null` es verdadero.

```kotlin
val texto: String? = if (random.nextBoolean()) null else "Kotlin"

if (texto != null && texto.isNotEmpty()) {
    println("Cadena de ${texto.length} caracteres")
} else {
    println("Cadena nula o vacía")
}
```

El smart cast solo se aplica cuando el compilador puede garantizar que el valor no cambió desde la comprobación. Funciona, por ejemplo, con un `val` local y con ciertos `var` locales que no pueden modificarse en ese punto. Puede no funcionar con propiedades o variables mutables cuyo valor podría cambiar entre la comprobación y el acceso.

Si no se puede demostrar la estabilidad del valor, puede guardarse en una variable local inmutable o utilizarse una operación nullable apropiada. Los casts explícitos `as` y `as?` se explican más adelante; no sustituyen automáticamente una comprobación segura.

[Vídeo: explicación del smart cast](https://www.youtube.com/embed/KxxCsrr8CQg)

---

## 2. Operador de llamada segura `?.`

El operador de llamada segura `?.` accede a una propiedad o método solo si el objeto no es `null`. Si el objeto es `null`, la expresión completa devuelve `null`.

```kotlin
val texto: String? = if (random.nextBoolean()) null else "Kotlin"
val longitud: Int? = texto?.length
```

El resultado también es nullable: `texto?.length` tiene tipo `Int?`, porque puede producir una longitud o `null`.

Las llamadas seguras se pueden encadenar. Si cualquier elemento de la cadena es `null`, el resultado es `null` y no se evalúan los accesos siguientes.

```kotlin
val nombreJefe: String? = persona?.departamento?.jefe?.nombre
```

También se pueden usar en el lado izquierdo de una asignación. La asignación y la expresión de la derecha solo se evalúan si el receptor existe.

```kotlin
persona?.departamento?.jefe = obtenerResponsable()
```

> [!warning] Evita los errores silenciosos
> Una llamada como `objeto?.guardar()` no hace nada si `objeto` es `null`. Usa `?.` cuando la ausencia del objeto sea válida; si representa un error de estado o de datos, gestiona ese caso explícitamente en lugar de ocultarlo.

[Vídeo: operador de llamada segura](https://www.youtube.com/embed/T8g3tvv3ZBA)

---

## 3. Operador Elvis `?:`

El operador Elvis `?:` devuelve el valor de la izquierda cuando no es `null`; de lo contrario, devuelve el valor de la derecha. Es útil para proporcionar un valor predeterminado y obtener un resultado no nullable.

```kotlin
val texto: String? = if (random.nextBoolean()) null else "Kotlin"
val longitud: Int = texto?.length ?: 0
```

Se puede colocar después de una cadena de llamadas seguras. Si algún elemento de la cadena es `null`, se devuelve el valor predeterminado.

```kotlin
val nombre: String = persona?.departamento?.jefe?.nombre ?: "Sin nombre"
```

Las expresiones aritméticas tienen mayor precedencia que `?:`. Para sumar el valor nullable y otro número, hacen falta paréntesis:

```kotlin
val suma = (valorNullable ?: 0) + incremento
```

En Kotlin, `throw` y `return` son expresiones de tipo `Nothing`: interrumpen el flujo normal y no producen un valor. Por eso pueden aparecer a la derecha de `?:`.

```kotlin
fun nombreObligatorio(persona: Persona): String =
    persona.nombre ?: throw IllegalArgumentException("Falta el nombre")

fun buscarNombre(id: Int): String {
    return obtenerNombre(id) ?: return "Desconocido"
}
```

`Nothing` es un subtipo de cualquier tipo, lo que permite combinar esas expresiones con el tipo esperado por la expresión Elvis.

[Vídeo: operador Elvis](https://www.youtube.com/embed/pYKtw8jeNBc)

---

## 4. Operador de aserción no nula `!!`

El operador `!!` convierte una expresión nullable en su equivalente no nullable. Si el valor es `null`, lanza `NullPointerException`.

```kotlin
val nombre: String? = obtenerNombre()
val longitud: Int = nombre!!.length
```

Usa `!!` solo si el contrato del programa garantiza que el valor existe en ese punto. Si esa garantía falla, el programa termina con una excepción que normalmente aporta poco contexto. En muchos casos es preferible una comprobación explícita, `?:`, `requireNotNull()` o `checkNotNull()`.

- `requireNotNull(valor)` lanza `IllegalArgumentException` si el argumento es `null`; si no, devuelve el valor no nullable.
- `checkNotNull(valor)` lanza `IllegalStateException` si el estado actual contiene `null`; si no, devuelve el valor no nullable.

```kotlin
val nombre = requireNotNull(obtenerNombre()) {
    "El nombre es obligatorio"
}
```

> [!warning] Evita `!!`
> No uses `!!` solo para silenciar un error del compilador. Comprueba si el tipo debería ser nullable y qué comportamiento necesita el programa cuando el valor falta.

[Vídeo: operador `!!`](https://www.youtube.com/embed/f7qjGJxceWA)

---

## 5. Operadores de cast `as` y `as?`

Un **up-cast** usa un valor de un subtipo donde se espera un supertipo; suele ser implícito. Un **down-cast** intenta recuperar un subtipo concreto desde un valor de tipo más general y requiere un cast explícito.

El operador `as` es un cast inseguro: si el objeto no es del tipo solicitado, lanza `ClassCastException`. Si se intenta convertir `null` a un tipo no nullable, también se produce una excepción.

```kotlin
val valor: Any = "Kotlin"
val texto: String = valor as String
```

Se puede convertir un nullable a un tipo nullable compatible:

```kotlin
val valor: Any? = if (random.nextBoolean()) null else "Kotlin"
val texto: String? = valor as String?
```

El operador `as?` es un cast seguro. Devuelve `null` si la conversión no es posible, por lo que su resultado siempre debe tratarse como nullable.

```kotlin
val valor: Any? = if (random.nextBoolean()) 42 else "Kotlin"
val texto: String? = valor as? String
```

Se puede combinar `as?` con Elvis para indicar un valor predeterminado o interrumpir el flujo si el cast falla.

```kotlin
val texto: String = valor as? String ?: "Tipo no compatible"

val persona: Persona = valor as? Persona ?: return
```

Usa comprobaciones `is` con smart cast cuando resulte suficiente. Reserva `as` para casos donde el tipo esté garantizado; `as?` es preferible cuando el cast puede fallar y el programa debe gestionar ese caso.

[Vídeo: operadores `as` y `as?`](https://www.youtube.com/embed/cprGooqPJcE)

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Smart cast | `if (valor != null) valor.length` | Tras una comprobación estable, el compilador permite tratar el valor como no nullable. |
| Llamada segura | `valor?.propiedad` | Devuelve `null` si el receptor es `null`; el resultado es nullable. |
| Llamadas encadenadas | `a?.b?.c` | Evita acceder a los elementos siguientes si uno es `null`. |
| Elvis | `valor ?: predeterminado` | Usa la izquierda si no es nula; si no, evalúa la derecha. |
| Salida desde Elvis | `valor ?: return` / `valor ?: throw ...` | `return` y `throw` son expresiones de tipo `Nothing`. |
| Aserción no nula | `valor!!` | Fuerza el tipo no nullable; lanza `NullPointerException` si falta el valor. |
| Cast inseguro | `valor as Tipo` | Falla con excepción si el objeto no tiene el tipo esperado. |
| Cast seguro | `valor as? Tipo` | Devuelve `null` si la conversión falla. |

## Relaciones

- [[02 - Jerarquia de tipos]] — jerarquía de tipos, `Any`, `Any?` y `Nothing`.
- [[03 - Funciones]] — funciones, retornos y expresiones de tipo `Nothing`.
- [[05.1 - Ejercicios 5 Operaciones con tipos nullables]] — ejercicios resueltos del tema.
- [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar cuándo se puede aplicar un smart cast y qué significa que una variable sea estable.
- [ ] Predecir el tipo y el resultado de una llamada segura.
- [ ] Encadenar llamadas seguras y proporcionar un valor predeterminado con Elvis.
- [ ] Explicar la diferencia entre `!!`, `requireNotNull()` y una llamada segura.
- [ ] Comparar los errores de `as` con el resultado de `as?`.
- [ ] Usar `return` o `throw` a la derecha de `?:` y explicar el papel de `Nothing`.
