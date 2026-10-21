---
asignatura: PSyP
tema: 1-2
tipo: ejercicio
estado: completo
fecha: 2026-10-12
tags:
  - DAM/ejercicio
  - DAM/psyp/subprocesos
  - DAM/psyp/flujos
---

# Prácticos resueltos — Temas 1 y 2 (PSyP)

> [!info] Asignatura
> [[DAM/Programacion_de_Servicios_y_Procesos/Indice|Programación de Servicios y Procesos]] · Temas 1 y 2
> Examen **práctico en papel**: completar huecos de código. Aquí están los ejercicios **resueltos y explicados línea a línea**.

> [!tip] Las tres partes del material
> - [[Guia examen temas 1 y 2|🧠 Teoría y chuleta]]
> - [[Test de repaso temas 1 y 2|✅ Test de repaso]]
> - [[Practicos temas 1 y 2|💻 Prácticos resueltos]]


> [!note] Cómo están organizados
> Cada ejercicio tiene: **enunciado** → **código con huecos** (para hacer en papel) → **solución** → **explicación** de por qué cada pieza es así. La teoría necesaria está en [[Guia examen temas 1 y 2]] y las preguntas cortas en [[Test de repaso temas 1 y 2]].

---

> [!question] Instrucciones
> Tapa las soluciones y rellena los huecos **en papel**. Fíjate en el **estilo del curso**: `show()`, `Scanner`, `printf`, `throws`, `try-with-resources` para los flujos del subproceso.

## 1 · Filtro de líneas con un subproceso

**Enunciado.** `Filtro` recibe como argumento una cadena, lee líneas de la entrada estándar y escribe en la salida estándar solo las que la contienen. Termina al recibir el centinela `CENTINELA FIN`. El padre le pasa las líneas y recoge los resultados.

### 1.a · Programa hijo (`Filtro`)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;

public class Filtro {
    private static final String CENTINELA = "____(1)____";

    public static void main(String[] args) throws IOException {
        if (args.length == 0) {
            System.err.println("Uso: java Filtro <cadena-a-buscar>");
            System.____(2)____(1);            // termina con código 1
        }

        String cadenaBuscada = args____(3)____;

        try (BufferedReader entrada = new BufferedReader(
                    new InputStreamReader(System.____(4)____, StandardCharsets.UTF_8));
             PrintWriter salida = new PrintWriter(
                    new OutputStreamWriter(System.out, StandardCharsets.UTF_8), ____(5)____)) {

            String linea;
            while ((linea = entrada.____(6)____()) != null) {
                if (linea.equals(CENTINELA)) {
                    break;
                }
                if (linea.____(7)____(cadenaBuscada)) {
                    salida.println(linea);
                }
            }
        }
    }
}
```

> [!example]- ✅ Solución 1.a
> **(1)** `CENTINELA FIN` **(2)** `exit` **(3)** `[0]` **(4)** `in` **(5)** `true` (autoflush) **(6)** `readLine` **(7)** `contains`

> [!note]- 🧠 Por qué funciona (1.a)
> - **`System.exit(1)`**: por convención `0` = éxito y cualquier otro valor = error. Al hijo le falta un argumento obligatorio, así que termina con **1**.
> - **`System.in`**: es la **entrada estándar**, que el padre conecta a la tubería de su `getOutputStream()`. El hijo lee de ahí sin saber que viene de otro proceso.
> - **`System.out`** con `PrintWriter(..., true)`: el `true` activa el **autoflush**, imprescindible para que la línea de resultado llegue al padre **en cuanto se escribe** y no quede retenida en el búfer.
> - **`readLine() != null`**: `readLine()` devuelve `null` cuando el flujo se **cierra** (el padre cerró su `getOutputStream()`). Es la señal de "no hay más líneas".
> - **`equals(CENTINELA)` antes de `contains`**: el centinela **nunca** debe filtrarse ni mostrarse; se comprueba primero.
> - **`contains`**: distingue mayúsculas/minúsculas. La línea coincide si **contiene** la cadena buscada.

**Código completo resuelto (1.a):**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;

public class Filtro {
    private static final String CENTINELA = "CENTINELA FIN";

    public static void main(String[] args) throws IOException {
        if (args.length == 0) {
            System.err.println("Uso: java Filtro <cadena-a-buscar>");
            System.exit(1);
        }

        String cadenaBuscada = args[0];

        try (BufferedReader entrada = new BufferedReader(
                    new InputStreamReader(System.in, StandardCharsets.UTF_8));
             PrintWriter salida = new PrintWriter(
                    new OutputStreamWriter(System.out, StandardCharsets.UTF_8), true)) {

            String linea;
            while ((linea = entrada.readLine()) != null) {
                if (linea.equals(CENTINELA)) {
                    break;
                }
                if (linea.contains(cadenaBuscada)) {
                    salida.println(linea);
                }
            }
        }
    }
}
```

### 1.b · Programa padre (`ProgramaPadre`)

```java
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.util.*;

public class ProgramaPadre {
    private static final String CENTINELA = "CENTINELA FIN";

    public static void main(String[] args)
            throws ____(1)____, InterruptedException {
        Scanner teclado = new Scanner(System.in, StandardCharsets.UTF_8);

        System.out.print("Cadena que se buscará: ");
        String cadenaBuscada = teclado.____(2)____();

        List<String> lineas = new ____(3)____<>();
        String linea;
        while (!(linea = teclado.nextLine()).equals(CENTINELA)) {
            lineas.____(4)____(linea);
        }

        String ejecutableJava = Path.of(
                System.getProperty("____(5)____"), "bin",
                System.getProperty("os.name").toLowerCase().contains("win")
                        ? "java.exe" : "java")
                .toString();

        ProcessBuilder constructor = new ProcessBuilder(
                ejecutableJava,
                "-cp", System.getProperty("____(6)____"),
                "Filtro", cadenaBuscada);
        constructor.redirectError(ProcessBuilder.Redirect.____(7)____);
        Process proceso = constructor.____(8)____();

        // Enviar líneas al hijo
        try (BufferedWriter entradaProceso = new BufferedWriter(
                new OutputStreamWriter(proceso.____(9)____(), StandardCharsets.UTF_8))) {
            for (String texto : lineas) {
                entradaProceso.write(texto);
                entradaProceso.____(10)____();     // salto de línea
            }
            entradaProceso.write(CENTINELA);
            entradaProceso.newLine();
        }

        // Leer resultados
        List<String> resultados = new ArrayList<>();
        try (BufferedReader salidaProceso = new BufferedReader(
                new InputStreamReader(proceso.____(11)____(), StandardCharsets.UTF_8))) {
            String resultado;
            while ((resultado = salidaProceso.readLine()) != null) {
                resultados.add(resultado);
            }
        }

        int codigoSalida = proceso.____(12)____();

        if (codigoSalida ____(13)____ 0) {
            System.err.println("El filtro terminó con el código " + codigoSalida);
        }
    }
}
```

> [!example]- ✅ Solución 1.b
> **(1)** `IOException` **(2)** `nextLine` **(3)** `ArrayList` **(4)** `add` **(5)** `java.home` **(6)** `java.class.path` **(7)** `INHERIT` **(8)** `start` **(9)** `getOutputStream` **(10)** `newLine` **(11)** `getInputStream` **(12)** `waitFor` **(13)** `!=`

> [!note]- 🧠 Por qué funciona (1.b)
> - **`throws IOException, InterruptedException`**: crear el proceso y comunicarse por flujos puede lanzar `IOException`; `waitFor()` lanza `InterruptedException`. Ambas hay que declararlas o capturarlas.
> - **`java.home` + `java.class.path`**: construyen el comando **portable**. `java.home` da la ruta al JDK/JRE en uso (de ahí `bin/java` o `bin/java.exe`) y `java.class.path` el classpath actual, para que el hijo cargue `Filtro`.
> - **`new ProcessBuilder(ejecutable, "-cp", classpath, "Filtro", cadena)`**: cada token es un **argumento independiente**. Por eso la cadena buscada puede contener espacios sin romperse: no pasa por ningún shell.
> - **`redirectError(INHERIT)`**: los errores del hijo salen por el `stderr` **del padre** (se ven en consola).
> - **`start()`**: crea el proceso. A partir de aquí, **`getOutputStream()`** del padre es la entrada del hijo (usar `close()` del try-with-resources = fin de datos para el hijo) y **`getInputStream()`** es su salida.
> - **`newLine()`**: `readLine()` del hijo espera un salto de línea; sin él, el hijo no procesaría la línea.
> - **`waitFor()`**: devuelve el **código de salida**. `!= 0` = error (convención).

**Código completo resuelto (1.b):**

```java
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.util.*;

public class ProgramaPadre {
    private static final String CENTINELA = "CENTINELA FIN";

    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner teclado = new Scanner(System.in, StandardCharsets.UTF_8);

        System.out.print("Cadena que se buscará: ");
        String cadenaBuscada = teclado.nextLine();

        List<String> lineas = new ArrayList<>();
        String linea;
        while (!(linea = teclado.nextLine()).equals(CENTINELA)) {
            lineas.add(linea);
        }

        String ejecutableJava = Path.of(
                System.getProperty("java.home"), "bin",
                System.getProperty("os.name").toLowerCase().contains("win")
                        ? "java.exe" : "java")
                .toString();

        ProcessBuilder constructor = new ProcessBuilder(
                ejecutableJava,
                "-cp", System.getProperty("java.class.path"),
                "Filtro", cadenaBuscada);
        constructor.redirectError(ProcessBuilder.Redirect.INHERIT);
        Process proceso = constructor.start();

        try (BufferedWriter entradaProceso = new BufferedWriter(
                new OutputStreamWriter(proceso.getOutputStream(), StandardCharsets.UTF_8))) {
            for (String texto : lineas) {
                entradaProceso.write(texto);
                entradaProceso.newLine();
            }
            entradaProceso.write(CENTINELA);
            entradaProceso.newLine();
        }

        List<String> resultados = new ArrayList<>();
        try (BufferedReader salidaProceso = new BufferedReader(
                new InputStreamReader(proceso.getInputStream(), StandardCharsets.UTF_8))) {
            String resultado;
            while ((resultado = salidaProceso.readLine()) != null) {
                resultados.add(resultado);
            }
        }

        int codigoSalida = proceso.waitFor();

        if (codigoSalida != 0) {
            System.err.println("El filtro terminó con el código " + codigoSalida);
        }
    }
}
```

> [!warning] Peligro de interbloqueo
> Aquí el padre **envía todo y luego lee**. Funciona con pocos datos, pero si el hijo llenara el búfer de la tubería de salida y el padre siguiera escribiendo, ambos se bloquearían. La solución general es **leer y escribir concurrentemente** (hilos dedicados) o redirigir la salida a un fichero.

> [!example]- 🔗 Fuente
> - PSyP: [[2.3 - Flujos de comunicación]] · [[2.4 - Finalización de subprocesos]] · [[2.2 - Gestión de subprocesos]]
> - Programación básica:
>   - [[Programación basica/Tema 2/2.2 Lectura por teclado#3. Buffer de datos|2.2 → 3. Buffer de datos]] · [[Programación basica/Tema 2/2.2 Lectura por teclado#4. Ejemplo de Scanner y printf|2.2 → 4. Ejemplo de Scanner y printf]]
>   - [[Programación basica/Tema 2/2.1 Escritura en pantalla#2. El método printf|2.1 → 2. El método printf]] · [[Programación basica/Tema 2/2.1 Escritura en pantalla#1. Introducción|2.1 → 1. Introducción]]
>   - [[Programación basica/Tema 12/Colecciones#4. Clase ArrayList|Colecciones → 4. Clase ArrayList]]
>   - [[Programación basica/Tema 6/Excepciones#2. Try-catch|Excepciones → 2. Try-catch]] · [[Programación basica/Tema 6/Excepciones#10. Finally|Excepciones → 10. Finally]]
>   - [[Programación basica/Tema 1/1.4 Cadenas#5. Métodos de la clase String|1.4 → 5. Métodos de String (`contains`, `equals`)]]

## 2 · Analizador de textos distribuido

**Enunciado.** `CharacterCounter` cuenta vocales o consonantes de las líneas que recibe por `stdin` y escribe un total en `stdout`. `MainAnalyzer` lanza **dos** instancias (una por cada modo) y recoge sus resultados.

### 2.a · Programa hijo (`CharacterCounter`)

```java
import java.util.Scanner;

public class CharacterCounter {
    public static void main(String[] args) {
        if (args.length != 1
                || (!args[0].equals("vowels") && !args[0].equals("consonants"))) {
            System.____(1)____.println("Error: Invalid mode");
            System.exit(____(2)____);
        }

        String modo = args[0];
        String debug = System.____(3)____("DEBUG_MODE");
        boolean depurar = debug != null && debug.equals("____(4)____");

        String vocales = "aeiouAEIOU";
        int total = 0;

        Scanner entrada = new Scanner(System.in);
        while (entrada.____(5)____()) {                // ¿queda alguna línea?
            String linea = entrada.nextLine();
            int cuenta = 0;
            for (int i = 0; i < linea.____(6)____(); i++) {
                char c = linea.charAt(i);
                boolean esVocal = vocales.____(7)____(c) >= 0;
                if (modo.equals("vowels") == esVocal) {
                    cuenta++;
                }
            }
            total += cuenta;

            if (depurar) {
                System.err.printf("[PID: %d] Line parsed. Found %d %s%n",
                        ProcessHandle.current().____(8)____(), cuenta, modo);
            }
        }

        System.out.printf("Total %s: %d%n", modo, total);
        System.exit(____(9)____);
    }
}
```

> [!example]- ✅ Solución 2.a
> **(1)** `err` **(2)** `1` **(3)** `getenv` **(4)** `TRUE` **(5)** `hasNextLine` **(6)** `length` **(7)** `indexOf` **(8)** `pid` **(9)** `0`

> [!note]- 🧠 Por qué funciona (2.a)
> - **Validación del argumento**: `args.length != 1` o un modo distinto de `"vowels"`/`"consonants"` → mensaje en **`System.err`** y `System.exit(1)`.
> - **`System.getenv("DEBUG_MODE")`**: `getenv` lee una **variable de entorno** (del SO), no una propiedad de la JVM. Devuelve `null` si no existe, así que hay que comparar con `null` **antes** de usar `equals`.
> - **`scanner.hasNextLine()`**: pregunta si **queda línea** por leer; cuando el padre cierra su flujo, devuelve `false` y el bucle termina con normalidad.
> - **`length()` / `charAt(i)`**: recorren la línea carácter a carácter. Un carácter es vocal si `vocales.indexOf(c) >= 0`.
> - **`modo.equals("vowels") == esVocal`**: truco compacto → cuenta la línea que corresponde al modo (`vowels` cuenta vocales, `consonants` cuenta lo que **no** son vocales).
> - **`ProcessHandle.current().pid()`**: obtiene el **PID** del propio proceso para el mensaje de depuración.
> - **`System.exit(0)`**: terminación **correcta**.

> [!example]- 🔗 Fuente
> - PSyP: [[2.3 - Flujos de comunicación]] · [[2.2 - Gestión de subprocesos]]
> - Programación básica:
>   - [[Programación basica/Tema 2/2.2 Lectura por teclado#2. La clase Scanner|2.2 → 2. La clase Scanner (`hasNextLine`, `nextLine`)]]
>   - [[Programación basica/Tema 1/1.4 Cadenas#5. Métodos de la clase String|1.4 → 5. Métodos de String (`length`, `charAt`, `indexOf`, `equals`)]]
>   - [[Programación basica/Tema 1/1.1 · Introducción al lenguaje Java#13.4 Caracteres|1.1 → 13.4 Caracteres]]

> [!tip] Alternativa con `BufferedReader`
> Si el enunciado (o tus apuntes) usa `BufferedReader`, sustituye el `Scanner` por:
> ```java
> BufferedReader entrada = new BufferedReader(
>         new InputStreamReader(System.in, StandardCharsets.UTF_8));
> String linea;
> while ((linea = entrada.readLine()) != null) { ... }
> ```
> 🔗 Fuente: [[2.3 - Flujos de comunicación]] · [[Programación basica/Tema 2/2.2 Lectura por teclado#2. La clase Scanner|Programación básica → 2.2 · 2. La clase Scanner]]

> [!warning] Alternativa con `BufferedReader`
> Tus apuntes de PSyP leen con `BufferedReader` y `readLine()`:
> ```java
> BufferedReader entrada = new BufferedReader(
>         new InputStreamReader(System.in, StandardCharsets.UTF_8));
> String linea;
> while ((linea = entrada.readLine()) != null) { ... }
> ```
> En el examen sirve **cualquiera de las dos**; usa la que aparezca en el enunciado.

### 2.b · Programa padre (`MainAnalyzer`)

```java
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class MainAnalyzer {
    public static void main(String[] args) throws IOException, InterruptedException {
        List<String> texto = List.____(1)____(
                "En un lugar de la Mancha", "de cuyo nombre no quiero acordarme");

        String ejecutableJava = javaExecutable();

        ProcessBuilder pbVocales = new ProcessBuilder(
                ejecutableJava, "-cp", System.getProperty("java.class.path"),
                "CharacterCounter", "vowels");
        pbVocales.redirectError(ProcessBuilder.Redirect.____(2)____);       // mismo stderr que el padre
        pbVocales.environment().____(3)____("DEBUG_MODE", "TRUE");

        ProcessBuilder pbConsonantes = new ProcessBuilder(
                ejecutableJava, "-cp", System.getProperty("java.class.path"),
                "CharacterCounter", "consonants");
        pbConsonantes.____(4)____(new File("./logs"));                       // directorio de trabajo
        pbConsonantes.redirectError(
                ProcessBuilder.Redirect.____(5)____(new File("./logs/consonant_err.log")));

        Process vocales = pbVocales.____(6)____();
        Process consonantes = pbConsonantes.start();

        System.out.println("PID vocales: " + vocales.____(7)____());
        System.out.println("PID consonantes: " + consonantes.pid());

        // Enviar el texto a ambos contadores
        try (BufferedWriter outVocales = new BufferedWriter(
                     new OutputStreamWriter(vocales.getOutputStream(), StandardCharsets.UTF_8));
             BufferedWriter outConsonantes = new BufferedWriter(
                     new OutputStreamWriter(consonantes.getOutputStream(), StandardCharsets.UTF_8))) {
            for (String frase : texto) {
                outVocales.write(frase); outVocales.newLine();
                outConsonantes.write(frase); outConsonantes.newLine();
            }
        }   // cerrar los flujos señala el fin de la entrada

        String resultadoVocales = leerLinea(vocales);
        String resultadoConsonantes = leerLinea(consonantes);

        int salidaVocales = vocales.____(8)____();
        int salidaConsonantes = consonantes.waitFor();

        if (salidaVocales == 0 && salidaConsonantes == 0) {
            System.out.printf("Vowel Result: %s%n", resultadoVocales);
            System.out.printf("Consonant Result: %s%n", resultadoConsonantes);
            System.out.println("Ambos procesos terminaron con éxito.");
        } else {
            System.err.println("Algún proceso falló.");
        }
    }

    private static String leerLinea(Process p) throws IOException {
        try (BufferedReader in = new BufferedReader(
                new InputStreamReader(p.getInputStream(), StandardCharsets.UTF_8))) {
            return in.____(9)____();                 // lee la línea de resultado
        }
    }

    private static String javaExecutable() {
        return Path.of(System.getProperty("____(10)____"), "bin",
                System.getProperty("os.name").toLowerCase().contains("win")
                        ? "java.exe" : "java")
                .toString();
    }
}
```

> [!example]- ✅ Solución 2.b
> **(1)** `of` **(2)** `INHERIT` **(3)** `put` **(4)** `directory` **(5)** `to` **(6)** `start` **(7)** `pid` **(8)** `waitFor` **(9)** `readLine` **(10)** `java.home`

> [!note]- 🧠 Por qué funciona (2.b)
> - **`List.of(...)`**: crea la **lista de cadenas** que simula el texto a analizar.
> - **`redirectError(INHERIT)`** (vocales): los errores del contador de vocales salen por el `stderr` del padre.
> - **`environment().put("DEBUG_MODE", "TRUE")`**: configura una **variable de entorno del hijo**. Todo esto se hace **antes** de `start()`.
> - **`directory(new File("./logs"))`** (consonantes): establece el **directorio de trabajo** del subproceso.
> - **`Redirect.to(file)`**: redirige el `stderr` del hijo al **fichero** `./logs/consonant_err.log`.
> - **`start()`** de cada `ProcessBuilder` lanza un proceso **nuevo**; se guardan los dos `Process` para operar con ellos.
> - **`pid()`**: muestra los **PID** de ambos subprocesos.
> - **Envío de líneas + `close()`**: el try-with-resources cierra el `getOutputStream()` de cada proceso → el hijo detecta **fin de entrada** y deja de leer.
> - **`waitFor()`**: espera la terminación y devuelve el **código de salida**. Con ambos a `0` → éxito; si no, se informa del fallo.

> [!warning] Cuidado en el examen
> Este enunciado exige **leer el resultado de cada hijo** (su línea `Total vowels: …`). Hazlo **antes** de descartar los flujos o drenarlo con un hilo mientras escribes; si no, el hijo puede bloquearse al llenar la tubería.
> [!example]- 🔗 Fuente
> - PSyP: [[Examen año pasado]] · [[2.2 - Gestión de subprocesos]] · [[2.3 - Flujos de comunicación]] · [[2.5 - Información sobre procesos]]
> - Programación básica:
>   - [[Programación basica/Tema 4/4.1 Arrays unidimensionales#14. Argumentos variables|4.1 → 14. Argumentos variables (`args`)]] · [[Programación basica/Tema 12/Colecciones#3. Interfaz List|Colecciones → 3. Interfaz List]]
>   - [[Programación basica/Tema 2/2.1 Escritura en pantalla#2. El método printf|2.1 → 2. El método printf]]
>   - [[Programación basica/Tema 6/Excepciones#2. Try-catch|Excepciones → 2. Try-catch]]

## 3 · Pipeline de nombres y saludos

**Enunciado.** `greetpeople` lanza un **pipeline**: `names.jar` genera 8 nombres y `greeting.jar` los saluda. Los errores deben verse en el `stderr` de `greetpeople`.

```java
import java.util.*;

public class GreetPeople {
    public static void main(String[] args) throws Exception {
        List<ProcessBuilder> linea = List.of(
                new ProcessBuilder("java", "-jar", "names.jar", "____(1)____"),
                new ProcessBuilder("java", "-jar", "greeting.jar"));

        List<Process> procesos = ProcessBuilder.____(2)____(linea);

        // Mostrar las salidas del último proceso sin bloquear
        Process ultimo = procesos.get(procesos.____(3)____() - 1);
        ultimo.____(4)____().transferTo(System.out);

        // Los errores del primero se heredan para verlos en consola
        linea.get(0).redirectError(ProcessBuilder.Redirect.INHERIT);
    }
}
```

> [!example]- ✅ Solución 3
> **(1)** `8` **(2)** `startPipeline` **(3)** `size` **(4)** `getInputStream`
>
> 🔗 Fuente: [[2.Repaso - Pipeline]] · [[2.3 - Flujos de comunicación]] · [[Programación basica/Tema 12/Colecciones#3. Interfaz List|Programación básica → Colecciones · 3. Interfaz List]]

> [!note]- 🧠 Por qué funciona (3)
> - **`ProcessBuilder.startPipeline(List<ProcessBuilder>)`** (Java 9+) conecta la **salida estándar** de cada proceso con la **entrada estándar** del siguiente, como una tubería `|` de shell, y devuelve la lista de `Process` **en orden**.
> - **`procesos.size() - 1`**: el último proceso del pipeline es el que produce la salida final (`greeting.jar`).
> - **`getInputStream().transferTo(System.out)`**: lee su salida y la vuelca a la consola; se hace en el **último** proceso porque los flujos **internos** del pipeline no se redirigen individualmente.
> - **`redirectError(INHERIT)`** en el primer `ProcessBuilder`: los errores se ven en el `stderr` de `greetpeople`.
> - Si quieres configurar la **entrada del primero** o la **salida del último**, se hace sobre esos `ProcessBuilder` **antes** de `startPipeline`.

## 4 · Variantes cortas de repaso

> [!question] Huecos rápidos
> 1. `Runtime.getRuntime().____("ls")` → lanza un proceso (forma simple, obsoleta desde Java 18).
> 2. `System.____("PATH")` → lee una variable de entorno.
> 3. `System.____("os.name")` → lee una propiedad de la JVM.
> 4. `pb.environment().____("CUSTOM_ID", "123")` → inyecta una variable de entorno al hijo.
> 5. `p.waitFor(3, TimeUnit.SECONDS)` devuelve `true` si el proceso ____, `false` si sigue ____.
> 6. `p.destroy()` pide terminación; si sigue vivo, `p.____()` la fuerza.
> 7. `ProcessHandle.____()` → handle del proceso actual.
> 8. `ProcessHandle.____(pid)` → `Optional<ProcessHandle>`.
> 9. `ProcessHandle.Info.arguments()` devuelve un ____.
> 10. `Desktop.____()` comprueba si la API está disponible.

> [!example]- ✅ Soluciones 4
> **1.** `exec` **2.** `getenv` **3.** `getProperty` **4.** `put` **5.** terminó / activo **6.** `destroyForcibly` **7.** `current` **8.** `of` **9.** `Optional` **10.** `isDesktopSupported`

> [!note]- 🧠 Por qué (4)
> - **`exec` vs. `start`**: `Runtime.exec` lanza un proceso; `ProcessBuilder.start()` es la forma **recomendada**. El `exec(String)` único está obsoleto desde Java 18.
> - **`getenv` vs. `getProperty`**: `getenv` = entorno del **SO**; `getProperty` = config de la **JVM**.
> - **`waitFor(timeout, unit)`**: `true` si terminó a tiempo, `false` si sigue vivo.
> - **`destroyForcibly`**: fuerza la terminación si `destroy()` no bastó.
> - **`ProcessHandle.of(pid)`**: devuelve `Optional<ProcessHandle>` (el proceso puede no existir o no ser visible); `Info.arguments()` también devuelve `Optional`.
> - **`Desktop.isDesktopSupported()`**: hay que comprobarlo antes de usar la API (puede no estar disponible en *headless*).

> [!example]- 🔗 Fuente
> - PSyP: [[2.2 - Gestión de subprocesos]] · [[2.4 - Finalización de subprocesos]] · [[2.5 - Información sobre procesos]]
> - Programación básica:
>   - [[Programación basica/Tema 13/Programación funcional#12. Optional|Funcional → 12. Optional]]
>   - [[Programación basica/Tema 2/2.2 Lectura por teclado#1. La clase System|2.2 → 1. La clase System]]

---


---

## Guía relacionada

- 🧠 **Teoría y chuleta** → [[Guia examen temas 1 y 2|Guía de teoría: Temas 1 y 2]]
- ✅ **Test de repaso** → [[Test de repaso temas 1 y 2]]
- 💻 **Prácticos resueltos** → [[Practicos temas 1 y 2]]


## Relaciones

- [[Guia examen temas 1 y 2]] — teoría y API de referencia
- [[Test de repaso temas 1 y 2]] — preguntas tipo test
- [[Examen año pasado]] — enunciado completo del práctico de referencia
- [[2.Repaso - Ejercicio filtro con subproceso]] · [[2.Repaso - Pipeline]] · [[2.Repaso - Variables de entorno]] · [[2.Repaso - Valor de salida]] · [[2.Repaso - Comunicación con subprocesos]] · [[2.Respaso - Listar archivos con Runtime]] — ejercicios originales
