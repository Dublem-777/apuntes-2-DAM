---
asignatura: PMDM
tema: 1
tipo: tema
estado: completo
fecha: 2026-09-17
tags:
  - DAM/tema
  - DAM/pmdm/kotlin-introduccion
---

# 1 · Introducción a Kotlin

> [!info] Asignatura
> [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Programación Multimedia y Dispositivos Móviles]] · Tema 1 · Kotlin
> Fuente original: `Documentos/Notas/Introducción a Kotlin.md`

## Índice del tema

- [[#1. El lenguaje Kotlin]]
- [[#2. IDEs]]
- [[#3. La función main()]]
- [[#4. Salida por consola]]
- [[#5. Variables]]
- [[#6. Entrada desde consola]]

---

## 1. El lenguaje Kotlin

### 1.1 ¿Qué es Kotlin?

**Kotlin** es un lenguaje de programación de **propósito general**, de **código abierto**, **multiplataforma**, **multiparadigma** y **estáticamente tipado**.

Cada término de la definición tiene su importancia:

| Característica | Qué significa |
| --- | --- |
| Propósito general | No está atado a un dominio concreto: backend, móvil, frontend… |
| Código abierto | El código fuente del compilador es libre y modificable |
| Multiplataforma | Compila a varios destinos: JVM, JavaScript o código máquina |
| Multiparadigma | Soporta programación estructurada, orientada a objetos y funcional |
| Estáticamente tipado | El tipo de cada variable se comprueba en **compilación**, no en ejecución |

- Desarrollado originalmente por **JetBrains**, ahora bajo la **Kotlin Foundation**.
- Existen **KEEP** (Kotlin Evolution and Enhancement Process): un procedimiento abierto al público para que cualquiera pueda examinar y opinar sobre las propuestas de modificación del diseño del lenguaje.

### 1.2 Compilación: los tres targets

Kotlin es un lenguaje **compilado**: el código fuente se compila a un lenguaje de nivel inferior.

| Target | Qué genera |
| --- | --- |
| Kotlin/JVM | Bytecode de la JVM |
| Kotlin/JS | JavaScript |
| Kotlin/Native | Código máquina |

### 1.3 Interoperabilidad con Java

**Kotlin/JVM y Java son completamente interoperables** (interoperar = trabajar conjuntamente):

- Cualquier **código Java** puede usarse en Kotlin/JVM.
- Cualquier **biblioteca de Java** (incluidas las basadas en anotaciones) es utilizable en Kotlin/JVM.
- Kotlin/JVM puede usar **clases, módulos, bibliotecas y la biblioteca estándar de Java**.
- Cualquier código de Kotlin/JVM puede usarse en Java — **excepto las *suspend functions*** (soporte de las corrutinas de Kotlin, no disponibles en Java).

> [!tip] Migración progresiva
> Se pueden **mezclar archivos Kotlin y Java en un mismo proyecto**. No hace falta migrar todo de golpe: se empieza usando Kotlin en las funcionalidades nuevas y en la refactorización de código antiguo. El propio compilador de Kotlin pasó de estar escrito íntegramente en Java a ser **solo un 10% Java**.

### 1.4 Dónde se usa Kotlin

- Alternativa a Java, JavaScript, C++, Objective-C… Aunque su mayor madurez está en la **JVM**, por lo que hoy se usa sobre todo como alternativa a Java.
- **Backend**: muy popular, p. ej. en el framework **Spring**.
- **Android**: prácticamente el lenguaje estándar de facto.
- **Kotlin Multiplatform**: un mismo equipo escribe código Kotlin para Android, iOS, frontend (con React) y backend → versatilidad y ahorro de costes. Las librerías se pueden crear una vez y publicar para varias plataformas.
- **Jetpack Compose**: conjunto de herramientas para construir **interfaces de usuario nativas en Kotlin**. Nació para Android, pero aprovecha la multiplataforma de Kotlin para vistas web, escritorio, iOS y otros destinos.

---

## 2. IDEs

| Herramienta | Para qué | Enlace |
| --- | --- | --- |
| **IntelliJ IDEA** | El IDE más popular para Kotlin | https://www.jetbrains.com/es-es/idea/ |
| **Android Studio** | Evolución de IntelliJ con aportaciones de Google, para Android | https://developer.android.com/studio?hl=es-419 |
| **Kotlin Playground** | Probar código Kotlin online | https://play.kotlinlang.org/ |

También se puede escribir Kotlin en otros editores: VS Code, Eclipse, Vim, Emacs, Sublime Text…

> [!tip] Ver el Java equivalente
> Para quien viene de Java, IntelliJ permite ver la equivalencia en Java del bytecode generado: **Tools → Kotlin → Show Kotlin Bytecode → Decompile**. Muy útil para entender qué "hay debajo" de cada sintaxis Kotlin.

---

## 3. La función main()

La función `main()` es el **punto de entrada** de cualquier programa Kotlin: al ejecutar el programa, el sistema empieza por ahí.

```kotlin
fun main() {
    println("Hello, World")
}
```

Si el programa necesita recibir **argumentos de entrada**:

```kotlin
fun main(args: Array<String>) {
    println("Hello, World")
}
```

Diferencias con Java:

| | Java | Kotlin |
| --- | --- | --- |
| Declaración | `public static void main(String[] args)` | `fun main(args: Array<String>)` |
| Contenedor | Obligatorio dentro de una clase | **Función de nivel superior**: no necesita clase |
| Modificadores | `public static void` | solo `fun` (por defecto es pública, y no hay `static`) |

> [!note] En el ejemplo, `fun` es la palabra reservada para declarar funciones y se estudia a fondo en el tema 3.

---

## 4. Salida por consola

| Función | Qué hace |
| --- | --- |
| `print(expr)` | Imprime la expresión por pantalla. Está **sobrecargada**: acepta cualquier tipo básico |
| `println(expr)` | Igual que `print` + **salto de línea** al final |

```kotlin
print("Hola")      // Hola
println(" Kotlin")  //  Kotlin -> y salta de línea
```

---

## 5. Variables

### 5.1 Los dos grupos: val y var

| Palabra | viene de | Tipo de referencia | ¿Se puede cambiar? |
| --- | --- | --- | --- |
| `var` | *variable* | **Mutable** | Sí: puede apuntar a distintos valores durante la ejecución |
| `val` | *value* | **Inmutable** | No: una vez asignado el valor inicial, no se cambia. Similar a una variable `final` de Java |

```kotlin
// Kotlin
val question = "¿De qué color es el caballo blanco de Santiago?"
var name = "Baldomero"
val answer: Int = 42
```

```java
// Java equivalente
final String question = "¿De qué color es el caballo blanco de Santiago?";
String name = "Baldomero";
final int answer = 42;
```

> [!tip] Sugerencia
> Declara las variables como inmutables (`val`) **siempre que sea posible**. Ventajas: menos efectos secundarios, código más predecible y más fácil de razonar (se verá más adelante).

### 5.2 Sin punto y coma

No es necesario `;` para terminar líneas (como en la mayoría de lenguajes modernos). Se puede usar para meter varias sentencias en la misma línea, pero **no se recomienda**: complica la legibilidad.

### 5.3 Inferencia de tipos

Se puede **omitir el tipo** en la declaración si el compilador es capaz de **inferirlo** (deducirlo) del valor inicial. También se puede indicar explícitamente:

```kotlin
var name = "Baldomero"     // el compilador infiere String
var answer: Int = 42       // tipo explícito
```

> [!tip] Sugerencia
> Solo omite el tipo cuando sea **muy obvio** cuál es el tipo inferido.

### 5.4 Inicialización obligatoria

Las variables deben inicializarse **forzosamente** durante la ejecución del bloque en el que estén definidas, **antes de cualquier instrucción que lea su valor**.

- A diferencia de Java, las variables de tipo referencial **NO se inicializan implícitamente a `null`**: siempre hay que inicializarlas explícitamente.
- No hace falta inicializarlas *en la propia línea de declaración*, sino en cualquier punto del mismo bloque antes de leerlas. Aun así, se recomienda inicializar en la declaración siempre que sea posible.

```kotlin
// Inicialización en la declaración
val value: Int = Random().nextInt(2)

// Inicialización en el mismo bloque, antes de cualquier lectura
val headsOrTails: String
if (value == 0) {
    headsOrTails = "Cara"
} else {
    headsOrTails = "Cruz"
}
println(headsOrTails)
```

El compilador verifica que **todos los caminos posibles** asignan valor antes del `println` (exhaustividad del `if/else`).

### 5.5 val protege la referencia, no el objeto

Una `val` no puede **apuntar a otro objeto**, pero el objeto referenciado **sí puede ser mutable**:

```kotlin
val languages = arrayListOf("Java")
languages.add("Kotlin")   // válido: mutamos el objeto, no cambiamos la referencia
```

> [!warning] Inmutable ≠ constante
> `val` = la **referencia** no se puede reasignar. Lo que contenga el objeto apuntado puede cambiar si el objeto es mutable (como `ArrayList`).

### 5.6 El tipo es estático

Una vez definida la variable —aunque el tipo lo haya inferido el compilador— **solo podrá contener objetos de ese tipo**:

```kotlin
var answer = 42
answer = "no answer"   // ERROR de compilación: answer solo puede referenciar objetos Int
```

> [!video]- Explicación en vídeo
> La fuente original enlaza un vídeo con la explicación de las variables.

---

## 6. Entrada desde consola

### 6.1 readln() y compañía

| Función / método | Qué devuelve | Si falla |
| --- | --- | --- |
| `readln()` | La línea leída como `String` (sin el salto de línea) | **Lanza excepción** |
| `readlnOrNull()` / `readLine()` | La línea como `String` | Devuelve `null` |

Para leer **otros tipos**: se lee como cadena y se convierte con los métodos de `String`:

| Conversión | Variante segura |
| --- | --- |
| `toInt()` | `toIntOrNull()` → `null` en vez de excepción |
| `toLong()` | `toLongOrNull()` |
| `toDouble()` | `toDoubleOrNull()` |
| `toFloat()` | `toFloatOrNull()` |
| `toBoolean()` | `toBooleanOrNull()` |

> [!warning] Los `toXxx()` lanzan excepción si la conversión no es posible; los `toXxxOrNull()` devuelven `null`.

### 6.2 Ejemplo completo

```kotlin
fun main() {
    print("Name: ")
    val name: String = readln()
    print("Age: ")
    val age: Int = readln().toInt()
    print("Height: ")
    val height: Double = readln().toDouble()
    println("Name: $name")
    println("Age: $age years old")
    println("Height: $height meters")
}
```

Nota: `$name` es la **interpolación de cadenas** (se sustituye el valor de la variable dentro del `"..."`), en lugar de concatenar con `+` como en Java.

### 6.3 Varios valores en una línea: split()

Leemos la línea entera y la separamos por el delimitador con `split()`, que devuelve una **lista de cadenas**; después convertimos cada elemento:

```kotlin
fun main() {
    println("Números (separados por espacio): ")
    val numbers: List<Int> = readln().split(' ').map { it.toInt() }
    println(numbers)
}
```

Desglose de la línea clave:

| Parte | Qué hace |
| --- | --- |
| `readln()` | Lee la línea entera como `String` |
| `.split(' ')` | La parte en una `List<String>` usando el espacio como delimitador |
| `.map { it.toInt() }` | Aplica `toInt()` a cada elemento (`it` = elemento actual) → `List<Int>` |

---

## Esquema

- Kotlin: propósito general, open source, multiplataforma (JVM/JS/Native), multiparadigma (estructurada + POO + funcional), estáticamente tipado. JetBrains → Kotlin Foundation; evolución abierta vía KEEP.
- Interoperabilidad total con Java (salvo suspend functions); migración progresiva mezclando ambos en un proyecto.
- Uso actual: alternativa a Java — backend (Spring), Android (estándar), multiplatform, Jetpack Compose.
- IDEs: IntelliJ IDEA (y Android Studio); playground online; `Show Kotlin Bytecode → Decompile`.
- `fun main()` sin clase; opcionalmente `args: Array<String>`.
- Salida: `print` / `println`. Entrada: `readln()` / `readlnOrNull()`, conversión `toXxx()` / `toXxxOrNull()`, `split()` para varios valores.
- Variables: `val` (inmutable, preferir) / `var` (mutable); sin `;`; inferencia de tipos; inicialización obligatoria antes de leer; el tipo es estático; `val` no impide mutar el objeto referenciado.

## Relaciones

- Ejercicios prácticos del tema: [[01.1 - Ejercicios 1 Introduccion a Kotlin]]
- [[02 - Jerarquía de tipos]] — tipos básicos y `Any` (pendiente)
- [[03 - Funciones]] — `fun`, parámetros, nivel de archivo (pendiente)
- Tema 1 de [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Acceso a Datos]] — comparación implícita Kotlin vs Java en cada fragmento

## Para repasar

- [ ] Explicar las 5 características de la definición de Kotlin y cada target de compilación
- [ ] Diferencias de `main()` y de las variables respecto a Java (val/var, final)
- [ ] Por qué `val languages = arrayListOf(...)` seguido de `add()` es válido
- [ ] Cuándo usar `readln()` vs `readlnOrNull()` y `toInt()` vs `toIntOrNull()`
- [ ] Probar en Kotlin Playground los ejemplos de variables e inicialización
