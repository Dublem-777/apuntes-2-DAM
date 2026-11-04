---
asignatura: PMDM
tema: 1
tipo: ejercicio
estado: en curso
fecha: 2026-10-31
tags:
  - DAM/ejercicio
  - DAM/pmdm/kotlin
  - DAM/pmdm/ejercicios
---

# Bloque 1 · Ejercicios de Kotlin

> [!info] Origen
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Bloque de ejercicios de Kotlin
> Apuntes relacionados: [[01 - Introduccion a Kotlin]] · [[02 - Jerarquia de tipos]] · [[04 - Estructuras básicas]]
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Bloques/Bloque01/`

> [!note] Sobre las soluciones
> Soluciones didácticas desarrolladas para este bloque con conceptos explicados en los temas anteriores. Cada ejercicio tiene su proyecto de IntelliJ en `Programas_clase/…/Bloques/Bloque01/Ejercicio1.K/` (ver **Ruta fuente**).

---

## Índice de Ejercicios

- [[#Ejercicio 1 · Media de notas, mayor y menor]]

---

## Ejercicio 1 · Media de notas, mayor y menor

> [!question] Enunciado
> Realiza un programa en Kotlin que solicite por consola al usuario su nombre, su nota de Android, su nota de multihilo, su nota de optativa y calcule la media de las notas mostrando un mensaje por pantalla que diga "La media es:(valor)", no se puede utilizar concatenación. Además deberá mostrar en qué asignatura tiene la mayor nota y cuál la menor.

### Clases y métodos introducidos
- `readln()`: lee una línea completa introducida por el usuario como `String`.
- `String.toDouble()`: convierte el texto a `Double`. Usamos `Double` y no `Int` porque una nota puede tener decimales (`7.5`). Lanza `NumberFormatException` si el texto no es un número.
- Plantillas de cadena `"$variable"` y `"${expresión}"`: meten valores dentro del texto **sin concatenar con `+`**, que es justo lo que prohíbe el enunciado.
- `String.format()`: `"%.2f".format(average)` devuelve el número como texto con 2 decimales (igual que `String.format` en Java).

> **Términos explicados:** [[01 - Introduccion a Kotlin#6.1 readln() y compañía|`readln()` y conversiones]] · [[02 - Jerarquia de tipos#6. Strings|plantillas de cadena]] · [[01 - Introduccion a Kotlin#5.1 Los dos grupos: val y var|`val` y `var`]] · [[04 - Estructuras básicas#1. La estructura `if`|estructura `if`]]

#### Ejemplo simple de funcionamiento
```kotlin
val name = "Daniel"
val grade = 7.256
// Concatenación (NO permitida en el ejercicio)
println("Hola " + name)
// Plantilla de cadena (lo que hay que usar)
println("Hola $name, tu nota es ${"%.2f".format(grade)}") // Hola Daniel, tu nota es 7,26
```

### Código fuente (`Ejercicio1.1/src/Main.kt`)

```kotlin
fun main() {
    // Pedimos los datos al usuario
    print("Introduce tu nombre: ")
    val name: String = readln()
    print("Introduce tu nota de Android: ")
    val androidGrade: Double = readln().toDouble()
    print("Introduce tu nota de Multihilo: ")
    val multithreadingGrade: Double = readln().toDouble()
    print("Introduce tu nota de Optativa: ")
    val optionalGrade: Double = readln().toDouble()

    // Media de las tres notas
    val average: Double = (androidGrade + multithreadingGrade + optionalGrade) / 3

    // Mayor nota: suponemos que es la de Android y la comparamos con las demás
    var highestSubject = "Android"
    var highestGrade = androidGrade
    if (multithreadingGrade > highestGrade) {
        highestSubject = "Multihilo"
        highestGrade = multithreadingGrade
    }
    if (optionalGrade > highestGrade) {
        highestSubject = "Optativa"
        highestGrade = optionalGrade
    }

    // Menor nota: mismo razonamiento, pero buscando la más baja
    var lowestSubject = "Android"
    var lowestGrade = androidGrade
    if (multithreadingGrade < lowestGrade) {
        lowestSubject = "Multihilo"
        lowestGrade = multithreadingGrade
    }
    if (optionalGrade < lowestGrade) {
        lowestSubject = "Optativa"
        lowestGrade = optionalGrade
    }

    // Resultados con plantillas de cadena (sin concatenación)
    println("Hola, $name")
    println("La media es: ${"%.2f".format(average)}")
    println("Tu mayor nota es $highestGrade en $highestSubject")
    println("Tu menor nota es $lowestGrade en $lowestSubject")
}
```

### Explicación paso a paso
1. **Lectura de datos:** el nombre se guarda tal cual (`readln()` ya devuelve `String`). Las notas se leen y convierten en la misma línea con `readln().toDouble()`. Todas son `val` porque no van a cambiar una vez leídas.
2. **Cálculo de la media:** se suman las tres notas y se dividen entre `3`. Como las notas son `Double`, la división es decimal (con `Int` se perderían los decimales: `17 / 3` daría `5`).
3. **Buscar la mayor (algoritmo del "campeón"):** es como un torneo de rey de la pista: el primero (Android) empieza como ganador y cada aspirante que lo supera ocupa su sitio. Guardamos **dos datos** del ganador: el nombre de la asignatura (`highestSubject`) y su nota (`highestGrade`). Son `var` porque pueden cambiar durante las comparaciones.
4. **Buscar la menor:** el mismo esquema, cambiando `>` por `<`.
5. **Salida sin concatenación:** todos los mensajes usan plantillas: `$name` para variables simples y `${...}` cuando dentro va una expresión, como `"%.2f".format(average)`, que deja la media con 2 decimales.

> [!tip] Prueba
> ```text
> Introduce tu nombre: Daniel
> Introduce tu nota de Android: 8.5
> Introduce tu nota de Multihilo: 6
> Introduce tu nota de Optativa: 9
> Hola, Daniel
> La media es: 7,83
> Tu mayor nota es 9.0 en Optativa
> Tu menor nota es 6.0 en Multihilo
> ```
> La media sale con **coma** (`7,83`) porque `format` usa el idioma del sistema (español), mientras que un `Double` impreso directamente usa siempre punto (`9.0`).

> [!warning] Empates
> Si dos notas son iguales y son las mayores, se queda la **primera** que se comparó, porque usamos `>` estricto (un empate no "destrona" al campeón). Por ejemplo, con Android 9 y Optativa 9 dirá que la mayor es Android.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / Clase | Comportamiento fundamental |
| --- | --- | --- |
| Lectura por consola | `readln()` | Devuelve una línea completa como `String`. |
| Parseo decimal | `String.toDouble()` | Convierte texto a `Double`; lanza `NumberFormatException` si no es válido. |
| Plantillas de cadena | `"$x"` / `"${expr}"` | Interpolan valores sin concatenar con `+`. |
| Formato de decimales | `"%.2f".format(x)` | Devuelve el número como texto con 2 decimales (según el idioma del sistema). |
| Máximo / mínimo | `var` + `if` encadenados | Se parte de un candidato y se sustituye si otro lo supera. |

## Relaciones

- Teoría: [[01 - Introduccion a Kotlin]] · [[02 - Jerarquia de tipos]] · [[04 - Estructuras básicas]]
- Bloque siguiente: [[Ejercicios Bloque 2]]
- Boletín con el mismo estilo: [[01.1 - Ejercicios 1 Introduccion a Kotlin]]
- Índice de la asignatura: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Leer un número decimal por consola con `readln().toDouble()`
- [ ] Escribir mensajes con plantillas en lugar de concatenar
- [ ] Encontrar el mayor y el menor de varios valores guardando también "de quién" es
- [ ] Formatear un `Double` con 2 decimales
