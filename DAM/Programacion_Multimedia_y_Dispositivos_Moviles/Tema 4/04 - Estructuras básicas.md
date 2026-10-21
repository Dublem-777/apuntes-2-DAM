---
asignatura: PMDM
tema: 4
tipo: tema
estado: completo
fecha: 2026-09-30
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-estructuras
---

# 4 · Estructuras básicas en Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 4 · Kotlin  
> Material de referencia: [Estructuras básicas de Kotlin](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/b04%20-%20Estructuras%20basicas%20de%20Kotlin/)

## Índice del tema

- [[#1. La estructura if]]
- [[#2. when como selección de condiciones]]
- [[#3. when con sujeto]]
- [[#4. when como expresión]]
- [[#5. Condiciones de guarda en when]]
- [[#6. Bucles for y repeat]]
- [[#7. Bucles while, break y continue]]
- [[#8. Excepciones]]

---

## 1. La estructura `if`

`if` permite ejecutar una rama cuando se cumple una condición y, opcionalmente, otra rama cuando no se cumple.

```kotlin
if (a < b) {
    println("a es menor que b")
} else {
    println("a no es menor que b")
}
```

En Kotlin, `if` con `else` también es una **expresión**: produce el valor de la última expresión de la rama seleccionada. Por eso puede usarse para inicializar una variable. Si una rama contiene varias instrucciones, la última expresión determina su resultado.

```kotlin
val mayor = if (a > b) a else b

val etiqueta = if (a > b) {
    println("a es mayor")
    "a"
} else {
    println("b es mayor o igual")
    "b"
}
```

Al usarse como expresión, `if` debe incluir `else`: el compilador debe poder obtener un valor en todos los casos. Kotlin no tiene operador ternario (`condicion ? valor1 : valor2`), porque `if` cubre ese uso.

Se pueden encadenar condiciones con `else if`, pero es una forma de anidar un `if` dentro de `else`. Para varias alternativas, `when` suele resultar más claro.

---

## 2. `when` como selección de condiciones

Sin sujeto, `when` comprueba las condiciones booleanas de arriba abajo. Ejecuta únicamente el cuerpo de la primera condición verdadera; no necesita `break` y no tiene *fall-through*.

```kotlin
val probabilidad = 70

when {
    probabilidad < 40 -> println("Poco probable")
    probabilidad <= 80 -> println("Probable")
    probabilidad < 100 -> println("Muy probable")
    else -> println("Seguro")
}
```

Cada rama tiene una condición, `->` y su cuerpo. Se pueden omitir las llaves si el cuerpo contiene una sola instrucción. El orden importa: una vez seleccionada una rama, no se evalúan las siguientes. `else` es la rama alternativa cuando ninguna condición anterior se cumple.

---

## 3. `when` con sujeto

Con sujeto, `when` compara una expresión con las condiciones de sus ramas. Estas pueden comprobar igualdad, pertenencia a rangos o colecciones, o tipo.

```kotlin
when (x) {
    1 -> println("x vale 1")
    2, 3 -> println("x vale 2 o 3")
    in 10..20 -> println("x está entre 10 y 20")
    !in 30..40 -> println("x no está entre 30 y 40")
    else -> println("No coincide con los casos anteriores")
}
```

Las condiciones pueden ser expresiones, no solo constantes. Por ejemplo, `limite + 1 -> ...`. También se puede comprobar el tipo con `is` o `!is`; dentro de esa rama el *smart cast* permite usar las propiedades del tipo comprobado.

```kotlin
when (valor) {
    is String -> println("Cadena de ${valor.length} caracteres")
    is Int -> println("Entero: $valor")
    else -> println("Otro tipo")
}
```

Una sentencia `when` que solo ejecuta código puede no cubrir todos los casos en muchos contextos; el compilador puede exigir exhaustividad para determinados tipos. Si `when` se usa como expresión, debe ser exhaustivo: debe cubrir todas las posibilidades, normalmente con `else` o enumerando todos los casos de un `enum` o tipo sellado.

---

## 4. `when` como expresión

El valor de la rama seleccionada se convierte en el resultado de la expresión `when`. En cuerpos con llaves, el resultado es el de la última expresión.

```kotlin
val descripcion = when (valor) {
    is String -> "Cadena de ${valor.length} caracteres"
    is Int -> "Entero incrementado: ${valor + 1}"
    else -> "Otro tipo"
}
```

También se puede escribir sin sujeto, como alternativa a una cadena `if`/`else if`:

```kotlin
val precio = when {
    cantidad in 1..10 -> "barato"
    cantidad > 30 -> "caro"
    else -> "normal"
}
```

En ambos casos, si el resultado se asigna o se devuelve, `when` debe ser exhaustivo.

---

## 5. Condiciones de guarda en `when`

Las condiciones de guarda permiten añadir una comprobación adicional a una rama de un `when` con sujeto. La condición principal se escribe primero y la guarda después de `if`. La rama se ejecuta solo si ambas se cumplen. Esta sintaxis está disponible desde Kotlin 2.2; el compilador debe usar una versión compatible.

```kotlin
fun alimentar(tipo: String, cazaRatones: Boolean) {
    when (tipo) {
        "Perro" -> println("Alimentar al perro")
        "Gato" if !cazaRatones -> println("Alimentar al gato")
        else -> println("Animal desconocido o gato cazador")
    }
}
```

Se pueden combinar guardas con `&&` y `||`; usa paréntesis para dejar clara la agrupación. También se puede escribir `else if condicion -> ...` para añadir una condición alternativa final.

```kotlin
when (animal) {
    is Gato if !animal.cazaRatones -> alimentarGato()
    is Perro -> alimentarPerro()
    else -> println("Animal no reconocido")
}
```

La comprobación `is Gato` permite el *smart cast* dentro de la guarda. Una rama `else` pertenece al `when` completo, no a la guarda de una rama. Si `when` es una expresión, debe seguir siendo exhaustivo.

---

## 6. Bucles `for` y `repeat`

`for` recorre cualquier objeto iterable, como colecciones, cadenas, rangos y progresiones. El tipo del elemento se infiere.

```kotlin
val nombres = listOf("Ada", "Grace")

for (nombre in nombres) {
    println(nombre)
}

for (i in 1..3) println(i)                 // Rango inclusivo: 1, 2, 3
for (i in 1..<4) println(i)                // Extremo final excluido: 1, 2, 3
for (i in 6 downTo 0 step 2) println(i)    // Descendente: 6, 4, 2, 0
```

Kotlin no tiene el `for` tradicional de Java con inicialización, condición e incremento. Para recorrer índices se pueden usar `indices` o `withIndex()`:

```kotlin
for (indice in nombres.indices) {
    println("El elemento $indice es ${nombres[indice]}")
}

for ((indice, nombre) in nombres.withIndex()) {
    println("El elemento $indice es $nombre")
}
```

Para ejecutar una acción sobre cada elemento se pueden usar `forEach` y `forEachIndexed`. Para repetir una acción un número fijo de veces, `repeat` recibe la cantidad y una lambda cuyo índice empieza en cero:

```kotlin
nombres.forEachIndexed { indice, nombre ->
    println("El elemento $indice es $nombre")
}

repeat(3) { indice ->
    println("Iteración ${indice + 1}")
}
```

---

## 7. Bucles `while`, `break` y `continue`

`while` comprueba la condición antes de cada iteración; puede no ejecutarse nunca. `do while` ejecuta el cuerpo al menos una vez y comprueba la condición después.

```kotlin
var cuenta = 3
while (cuenta > 0) {
    println(cuenta)
    cuenta--
}

do {
    println("Se ejecuta al menos una vez")
} while (false)
```

- `break` termina el bucle más interno.
- `continue` salta al inicio de la siguiente iteración.

---

## 8. Excepciones

Una excepción comunica una situación que interrumpe el flujo normal del programa. Si no se captura, se propaga por las llamadas y termina la ejecución. Puede contener un mensaje y una traza de pila (*stack trace*) útiles para localizar el origen del problema.

### Capturar excepciones

`try-catch` permite gestionar excepciones. Puede haber varios bloques `catch`; se ejecuta el primero cuyo tipo coincide. `finally` es opcional y se ejecuta tanto si ocurre una excepción como si no. Debe existir al menos un bloque `catch` o `finally`.

En Kotlin, `try-catch` es una expresión: devuelve el valor de la última expresión del bloque `try` o del `catch` ejecutado. `finally` sirve para liberar recursos o realizar tareas de cierre; no determina el valor de la expresión.

```kotlin
val texto = "42"
val numero = try {
    texto.toInt()
} catch (e: NumberFormatException) {
    0
} finally {
    println("Conversión terminada")
}
```

Kotlin no tiene *checked exceptions*: el compilador no obliga a capturarlas ni declararlas.

### Lanzar excepciones

`throw` lanza una excepción. Es una expresión de tipo `Nothing`, por lo que puede aparecer en una rama donde se espera otro tipo: esa rama nunca devuelve un valor.

```kotlin
fun dividir(dividendo: Int, divisor: Int): Int {
    if (divisor == 0) {
        throw IllegalArgumentException("El divisor no puede ser cero")
    }
    return dividendo / divisor
}
```

Se pueden definir excepciones propias heredando de `Exception` o de una subclase adecuada:

```kotlin
class SaldoInsuficienteException(mensaje: String) : Exception(mensaje)
```

### Validación con `require`, `check` y `error`

| Función | Uso | Excepción lanzada si falla |
| --- | --- | --- |
| `require(condicion)` | Validar un argumento o precondición | `IllegalArgumentException` |
| `check(condicion)` | Validar que el estado actual permite la operación | `IllegalStateException` |
| `error(mensaje)` | Indicar un estado interno imposible o un error de lógica | `IllegalStateException` |

Se puede proporcionar un mensaje de error mediante una lambda:

```kotlin
fun areaRectangulo(ancho: Double, alto: Double): Double {
    require(ancho >= 0) { "El ancho no puede ser negativo" }
    require(alto >= 0) { "El alto no puede ser negativo" }
    return ancho * alto
}

fun nombreOperacion(codigo: Int): String = when (codigo) {
    1 -> "Suma"
    2 -> "Resta"
    else -> error("Código de operación desconocido: $codigo")
}
```

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / regla | Idea clave |
| --- | --- | --- |
| `if` expresión | `if (cond) valor1 else valor2` | Devuelve el valor de la rama; como expresión necesita `else`. |
| `when` sin sujeto | `when { condicion -> ... }` | Selecciona la primera condición verdadera. |
| `when` con sujeto | `when (x) { valor -> ... }` | Admite igualdad, rangos (`in`), tipos (`is`) y alternativas con coma. |
| `when` expresión | `val x = when (...) { ... }` | Debe ser exhaustivo; cada rama aporta un valor. |
| Guarda | `caso if condicion -> ...` | La condición principal y la guarda deben cumplirse. |
| `for` | `for (x in iterable)` | Recorre rangos, colecciones, progresiones y cadenas. |
| Índices | `indices`, `withIndex()` | Recorren elementos con su posición. |
| `repeat` | `repeat(n) { indice -> ... }` | Ejecuta el bloque `n` veces; el índice comienza en cero. |
| `while` / `do while` | Condición antes / después | `do while` ejecuta el cuerpo al menos una vez. |
| `break` / `continue` | Dentro de un bucle | Termina bucle / pasa a siguiente iteración. |
| `try-catch-finally` | `try { ... } catch (...) { ... }` | Captura excepciones; `try-catch` puede producir un valor. |
| Validación | `require`, `check`, `error` | Argumentos, estado y errores internos, respectivamente. |

## Relaciones

- [[03 - Funciones]] — `if` y `when` como expresiones; `Nothing` y `throw`.
- [[04.1 - Ejercicios 4 Estructuras básicas]] — ejercicios del tema.
- [[02 - Jerarquia de tipos]] — jerarquía de tipos, `Any` y `Nothing`.
- [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar por qué un `if` usado como expresión necesita `else`.
- [ ] Diferenciar `when` con y sin sujeto y determinar qué rama se ejecuta.
- [ ] Explicar cuándo un `when` debe ser exhaustivo.
- [ ] Usar `in`, `is` y una condición de guarda en ramas de `when`.
- [ ] Recorrer una colección con `for`, `indices` y `withIndex()`.
- [ ] Comparar `while` con `do while` y explicar `break` y `continue`.
- [ ] Explicar cómo se elige un bloque `catch` y cuándo se ejecuta `finally`.
- [ ] Diferenciar `require`, `check` y `error`.
