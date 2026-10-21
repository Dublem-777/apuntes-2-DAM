---
asignatura: PSyP
tema: 2
tipo: ejercicio
estado: pendiente
fecha: 2026-10-20
tags:
  - DAM/ejercicio
  - DAM/psyp/subprocesos
  - DAM/psyp/flujos
---

# Simulacro · Examen práctico Tema 2 (PSyP)

> [!info] Asignatura
> [[DAM/Programacion_de_Servicios_y_Procesos/Indice|Programación de Servicios y Procesos]] · Tema 2 · Gestión de procesos · Simulacro con las reglas que ha dado el profesor: **todo dentro de funciones**, con **huecos en las líneas** y **líneas completas** que escribir.

> [!tip] Material de examen
> - 📝 [[Simulacro practico tema 2|Simulacro]] ← **estás aquí**
> - ✅ [[Simulacro practico tema 2 - Soluciones|Soluciones del simulacro]]: ábrelo **solo** al terminar
> - 🐣 [[Explicacion desde cero temas 1 y 2#Parte 4 · Recetario de funciones típicas|Recetario de funciones]] · 🧠 [[Guia examen temas 1 y 2|Guía]] · 💻 [[Practicos temas 1 y 2|Prácticos]]

## Instrucciones

- ⏱️ **Tiempo: 1 hora.** Hazlo **en papel**, sin mirar apuntes ni el IDE.
- Hay dos tipos de hueco:

| Tipo | Cómo se ve | Qué escribes | Puntos |
| --- | --- | --- | --- |
| **Hueco en línea** | `____(7)____` | Solo lo que falta en ese hueco (una palabra, un operador, un método...) | 0,25 |
| **Línea completa** | `// [L3] comentario` seguido de una línea `_______` | La **línea entera** de Java que hace lo que dice el comentario, con su `;` | 0,5 |

- Hay **24 huecos en línea** (6 puntos) y **12 líneas completas** (6 puntos), en total **12 puntos**. Tu nota es `puntos / 12 × 10`.
- Los `import` ya están puestos: no hace falta que los escribas.
- Si una línea completa admite varias soluciones, vale cualquiera que **compile y haga lo que pide el comentario**.

---

## Enunciado

**Proyecto: Calculadora de notas distribuida**

Crear una aplicación Java multiproceso con dos partes:

1. **`GradeCalculator.java`**: aplicación "trabajadora" que calcula la **media** o la **nota máxima** de las notas que recibe.
2. **`GradeManager.java`**: aplicación que lanza **dos** `GradeCalculator`, les envía las notas y recoge sus resultados.

### Parte 1: `GradeCalculator`

- Debe recibir **exactamente un** argumento: `"average"` o `"max"`. Si no, escribe `Error: Invalid mode` en la **salida de error** y termina con el valor **1**.
- Debe comprobar si existe la variable de entorno **`VERBOSE`**.
- Lee **línea a línea** su entrada estándar. Cada línea tiene el formato `nombre;nota` (por ejemplo, `Ana;7.5`).
	- Si una línea no tiene ese formato o la nota no es un número entre 0 y 10, escribe `Invalid line: <línea>` en la salida de error y **la ignora**.
	- Si `VERBOSE` vale `TRUE`, por cada línea válida escribe en la salida de error `[PID: 12345] Processed: Ana -> 7,50`.
- Cuando no quedan más líneas, escribe en su **salida estándar** dos líneas: `Students: N` y `Result: X,XX` (la media o la máxima, según el modo).
- Termina con **0** si todas las líneas eran válidas y con **2** si hubo **alguna línea inválida**.

### Parte 2: `GradeManager`

- Define una lista de notas, con alguna inválida a propósito.
- Construye el comando de forma **portable**, usando las propiedades `java.home` y `java.class.path`.
- Configura un `ProcessBuilder` para la **media**: su salida de error debe ser **la misma que la de GradeManager**, y la variable `VERBOSE` debe valer `TRUE`.
- Configura otro `ProcessBuilder` para el **máximo**, con el directorio de trabajo `./reports` y la salida de error redirigida al fichero `max_err.log` de ese directorio.
- Inicia ambos procesos y muestra sus **PIDs**.
- Envía a cada uno las notas, **una por línea**, y **cierra** la comunicación.
- Lee **todas** las líneas que produce cada calculadora.
- Espera a cada proceso **como máximo 5 segundos**. Si no ha terminado, lo **destruye**.
- Muestra los resultados e indica, según el código de salida, si cada proceso terminó **OK**, **OK con líneas inválidas**, por **tiempo agotado** o con **error**.

---

## Parte 1 · `GradeCalculator` (hijo)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class GradeCalculator {

    private String mode;              // "average" o "max"
    private boolean verbose;          // true si VERBOSE vale TRUE
    private int students;             // nº de líneas válidas procesadas
    private double sum;               // suma de notas (para la media)
    private double max;               // nota máxima encontrada
    private boolean invalidFound;     // true si alguna línea era inválida

    // Devuelve true si llega exactamente un argumento y es "average" o "max"
    public boolean validateArgs(String[] args) {
        if (args.____(1)____ != 1) {
            return false;
        }
        return args[0].equals("average") ____(2)____ args[0].equals("max");
    }

    // Devuelve true si la variable de entorno VERBOSE existe y vale TRUE
    public boolean isVerbose() {
        // [L1] Guarda en "value" el valor de la variable de entorno VERBOSE
        ______________________________________________________
        return value ____(3)____ null && value.____(4)____("TRUE");
    }

    // Extrae la nota de una línea "nombre;nota". Devuelve -1 si la línea no es válida
    public double parseGrade(String line) {
        String[] parts = line.____(5)____(";");
        if (parts.length != 2) {
            return -1;
        }
        try {
            double grade = Double.____(6)____(parts[1].trim());
            if (grade < 0 || grade > 10) {
                return -1;
            }
            return grade;
        } catch (____(7)____ e) {
            return -1;
        }
    }

    // Lee líneas de la entrada estándar hasta que el padre cierre la tubería
    public void processInput() throws IOException {
        BufferedReader input = new BufferedReader(
                new InputStreamReader(System.____(8)____, StandardCharsets.UTF_8));
        String line;
        // [L2] Cabecera del bucle: lee una línea en "line" y repite mientras no sea null
        ______________________________________________________ {
            double grade = parseGrade(line);
            if (grade < 0) {
                System.____(9)____.println("Invalid line: " + line);
                invalidFound = true;
                ____(10)____;                     // salta al siguiente ciclo del bucle
            }
            students++;
            sum += grade;
            if (grade > max) {
                max = grade;
            }
            if (verbose) {
                System.err.printf("[PID: %d] Processed: %s -> %.2f%n",
                        ProcessHandle.____(11)____().pid(), line.split(";")[0], grade);
            }
        }
    }

    public void run(String[] args) {
        if (!validateArgs(args)) {
            System.err.println("Error: Invalid mode");
            System.exit(____(12)____);
        }
        mode = args[0];
        // [L3] Guarda en el atributo "verbose" si el modo depuración está activo
        ______________________________________________________
        try {
            processInput();
        } catch (IOException e) {
            System.err.println("Read error: " + e.getMessage());
            System.exit(1);
        }
        double result = mode.equals("average") ? (students > 0 ? sum / students : 0) : max;
        System.out.println("Students: " + students);
        System.out.printf("Result: %.2f%n", result);
        // [L4] Termina con 2 si hubo alguna línea inválida y con 0 si no (en una sola línea)
        ______________________________________________________
    }

    public static void main(String[] args) {
        new GradeCalculator().run(args);
    }
}
```

---

## Parte 2 · `GradeManager` (padre)

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class GradeManager {

    private static final int TIMEOUT_SECONDS = 5;

    private final List<String> grades;

    public GradeManager() {
        // Notas a procesar ("nombre;nota"). "Luis;diez" es inválida a propósito
        grades = List.of("Ana;7.5", "Pedro;4.25", "Luis;diez", "Marta;9", "Juan;6");
    }

    // Comando portable: <java.home>/bin/java -cp <classpath> GradeCalculator <mode>
    public List<String> buildCommand(String mode) {
        String javaPath = System.getProperty("____(13)____")
                + File.separator + "bin" + File.separator + "java";
        // Ruta absoluta: el hijo "max" cambia de directorio y un classpath relativo dejaría de valer
        String classPath = new File(System.getProperty("____(14)____")).getAbsolutePath();

        List<String> command = new ArrayList<>();
        command.add(javaPath);
        command.add("____(15)____");
        command.add(classPath);
        command.add("GradeCalculator");
        command.add(mode);
        return command;
    }

    // Calculadora de media: errores por la consola del padre y VERBOSE=TRUE
    public ProcessBuilder configureAverageCalculator() {
        ProcessBuilder pb = new ProcessBuilder(buildCommand("average"));
        // [L5] Los errores del hijo deben salir por la misma salida de error que el padre
        ______________________________________________________
        // [L6] El hijo debe tener la variable de entorno VERBOSE con valor TRUE
        ______________________________________________________
        return pb;
    }

    // Calculadora de máximo: directorio ./reports y errores a reports/max_err.log
    public ProcessBuilder configureMaxCalculator() {
        ProcessBuilder pb = new ProcessBuilder(buildCommand("max"));
        File reports = new File("./reports");
        reports.mkdirs();                                  // si no existe, start() fallaría
        pb.____(16)____(reports);
        pb.____(17)____(new File(reports, "max_err.log"));
        return pb;
    }

    // Envía cada nota como una línea y cierra la entrada del hijo
    public void sendGrades(Process process, List<String> lines) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(
                new ____(18)____(process.____(19)____(), StandardCharsets.UTF_8))) {
            for (String line : lines) {
                // [L7] Escribe el texto de la línea en el flujo
                ______________________________________________________
                // [L8] Escribe el salto de línea
                ______________________________________________________
            }
        }
    }

    // Lee TODAS las líneas que el hijo escribe en su salida estándar
    public List<String> readAllOutput(Process process) throws IOException {
        List<String> output = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.____(20)____(), StandardCharsets.UTF_8))) {
            String line;
            // [L9] Cabecera del bucle: lee una línea en "line" y repite mientras no sea null
            ______________________________________________________ {
                output.add(line);
            }
        }
        return output;
    }

    // Espera como mucho TIMEOUT_SECONDS. Si no termina, lo destruye y devuelve -1
    public int waitWithTimeout(Process process) throws InterruptedException {
        // [L10] Espera como mucho TIMEOUT_SECONDS segundos y guarda en "finished" si terminó
        ______________________________________________________
        if (!finished) {
            process.____(21)____();
            return -1;
        }
        return process.____(22)____();
    }

    // Traduce el código de salida a un mensaje
    public String describeExitCode(int code) {
        if (code == 0) {
            return "OK";
        } else if (code == 2) {
            return "OK con líneas inválidas";
        } else if (code == -1) {
            return "Tiempo agotado";
        }
        return "Error (código " + code + ")";
    }

    public void run() {
        try {
            Process average = configureAverageCalculator().____(23)____();
            Process max = configureMaxCalculator().start();

            System.out.println("PID average: " + average.____(24)____());
            System.out.println("PID max: " + max.pid());

            sendGrades(average, grades);
            sendGrades(max, grades);

            List<String> averageOutput = readAllOutput(average);
            List<String> maxOutput = readAllOutput(max);

            // [L11] Espera a la calculadora de media con timeout y guarda su código en "averageExit"
            ______________________________________________________
            int maxExit = waitWithTimeout(max);

            System.out.println("Average calculator -> " + averageOutput
                    + " · " + describeExitCode(averageExit));
            System.out.println("Max calculator -> " + maxOutput
                    + " · " + describeExitCode(maxExit));
        } catch (IOException e) {
            System.err.println("I/O error: " + e.getMessage());
        } catch (InterruptedException e) {
            // [L12] Restaura el estado de interrupción del hilo actual
            ______________________________________________________
            System.err.println("Wait interrupted.");
        }
    }

    public static void main(String[] args) {
        new GradeManager().run();
    }
}
```

---

## Salida esperada

Si lo has completado bien, al ejecutar `GradeManager` sale algo como esto (los PIDs cambian en cada ejecución):

```text
PID average: 7075
PID max: 7087
[PID: 7075] Processed: Ana -> 7,50
[PID: 7075] Processed: Pedro -> 4,25
Invalid line: Luis;diez
[PID: 7075] Processed: Marta -> 9,00
[PID: 7075] Processed: Juan -> 6,00
Average calculator -> [Students: 4, Result: 6,69] · OK con líneas inválidas
Max calculator -> [Students: 4, Result: 9,00] · OK con líneas inválidas
```

Además, en `reports/max_err.log` queda escrita la línea `Invalid line: Luis;diez`, porque los errores de la calculadora de máximo van a ese fichero y no a la consola.

> [!question] Antes de mirar las soluciones, responde con tus palabras (sin puntos)
> 1. ¿Por qué solo aparecen mensajes `[PID: ...]` de **uno** de los dos procesos?
> 2. ¿Qué pasaría si en `sendGrades` quitaras el `try (...)` y no cerraras nunca el writer?
> 3. ¿Por qué `isVerbose()` compara con `null` **antes** de llamar a `equals`?
> 4. ¿Por qué se usa `waitFor(TIMEOUT_SECONDS, TimeUnit.SECONDS)` y luego `exitValue()`, en vez de `waitFor()` a secas?

## Guía relacionada

- ✅ **Soluciones** → [[Simulacro practico tema 2 - Soluciones]]
- 🐣 **Recetario de funciones** → [[Explicacion desde cero temas 1 y 2#Parte 4 · Recetario de funciones típicas|Explicación desde cero → Parte 4]]
- 💻 **Prácticos resueltos** → [[Practicos temas 1 y 2]]
- 📄 **Examen del año pasado** → [[Examen año pasado]]
