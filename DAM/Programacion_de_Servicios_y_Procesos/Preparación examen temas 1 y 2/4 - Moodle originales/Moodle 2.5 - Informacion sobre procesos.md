# Cuestionario del apartado 2-5

##### Estado

Finalizado

##### Comenzado

miércoles, 21 de octubre de 2026, 17:51

##### Completado

miércoles, 21 de octubre de 2026, 17:51

##### Duración

9 segundos

##### Puntos

0,00/37,00

##### Calificación

**0,00** de 10,00 (**0**%)

#### Pregunta 1

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la diferencia principal entre los métodos children() y descendants() de la interfaz ProcessHandle?

Pregunta 1Respuesta

a.

children() es exclusivo de la clase Process, mientras que descendants() solo se puede invocar desde ProcessHandle.

b.

children() devuelve una List, mientras que descendants() devuelve un Stream.

c.

children() devuelve un Stream solo con los subprocesos directos, mientras que descendants() incluye subprocesos directos, nietos y sucesivos.

d.

children() devuelve únicamente procesos vivos, mientras que descendants() devuelve procesos vivos y terminados.

#### Retroalimentación

Respuesta incorrecta.

children() se limita al primer nivel jerárquico, mientras que descendants() recorre recursivamente toda la arborescencia de procesos derivados.

La respuesta correcta es: children() devuelve un Stream solo con los subprocesos directos, mientras que descendants() incluye subprocesos directos, nietos y sucesivos.

#### Pregunta 2

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para recuperar la lista de argumentos proporcionados al comando que inició el subproceso, `ProcessHandle.Info` dispone del método Respuesta Pregunta 2, que devuelve un `Optional<String[]>`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Término en inglés para referirse a los parámetros de un comando o función.

La respuesta correcta es: arguments

#### Pregunta 3

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se puede obtener el `ProcessHandle` correspondiente al proceso padre del proceso representado por un objeto `ProcessHandle`?

Pregunta 3Respuesta

a.

Los procesos Java no pueden conocer a su proceso padre por razones de aislamiento y seguridad del sistema.

b.

Usando ProcessHandle.of(processHandle.ppid()).

c.

Llamando al método getParentProcess(), que devuelve un ProcessHandle directo.

d.

Llamando al método parent(), que devuelve un Optional.

#### Retroalimentación

Respuesta incorrecta.

El método parent() consulta al sistema operativo por el proceso progenitor y lo retorna en un envoltorio Optional.

La respuesta correcta es: Llamando al método parent(), que devuelve un Optional.

#### Pregunta 4

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué resultado devuelve la llamada `ProcessHandle.of(pid)` si se le proporciona un identificador de proceso (PID) que no existe en el sistema?

Pregunta 4Respuesta

a.

Lanza una excepción IllegalArgumentException.

b.

Lanza una excepción de tipo NoSuchProcessException.

c.

Un Optional vacío (Optional.empty()).

d.

Un valor null.

#### Retroalimentación

Respuesta incorrecta.

Dado que el PID no corresponde a ningún proceso activo en el sistema, el método retorna un Optional sin valor presente.

La respuesta correcta es: Un Optional vacío (Optional.empty()).

#### Pregunta 5

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

A diferencia de `commandLine()`, el método Respuesta Pregunta 5 de la interfaz `ProcessHandle.Info` extrae únicamente el nombre del ejecutable o ruta del comando sin incluir ningún argumento.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Término en inglés para referirse a la orden o comando principal.

La respuesta correcta es: command

#### Pregunta 6

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se obtiene una instancia de ProcessHandle correspondiente al propio proceso Java que se está ejecutando actualmente?

Pregunta 6Respuesta

a.

Process.getCurrentProcess()

b.

new ProcessHandle()

c.

ProcessHandle.current()

d.

ProcessHandle.of(0)

#### Retroalimentación

Respuesta incorrecta.

El método estático current() de ProcessHandle devuelve la representación del proceso Java en ejecución.

La respuesta correcta es: ProcessHandle.current()

#### Pregunta 7

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para listar todos los procesos vivos en el sistema operativo que sean visibles para la aplicación Java actual, se utiliza el método estático Respuesta Pregunta 7.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Método estático de la interfaz que solicita la totalidad de los procesos.

La respuesta correcta es: allProcesses

#### Pregunta 8

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué método de `ProcessHandle.Info` devuelve un `Optional<Instant>` que representa el instante de inicio del subproceso?

Pregunta 8Respuesta

a.

totalCpuDuration()

b.

getInstant()

c.

startInstant()

d.

startTime()

#### Retroalimentación

Respuesta incorrecta.

Retorna el objeto Instant de la API java.time asociado con el momento exacto en que arrancó el proceso.

La respuesta correcta es: startInstant()

#### Pregunta 9

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el código `Optional<String> currentUser = ProcessHandle.current().info().user();`, ¿qué representará `currentUser` si el SO no permite acceder a la información del usuario?

Pregunta 9Respuesta

a.

Devolverá una cadena vacía ("").

b.

Un Optional vacío, es decir, currentUser.isPresent() será false.

c.

Lanzará una SecurityException en tiempo de ejecución.

d.

Una cadena con el texto "".

#### Retroalimentación

Respuesta incorrecta.

Al devolver Optional, si la información no está disponible o accesible, se devuelve un contenedor sin valor presente.

La respuesta correcta es: Un Optional vacío, es decir, currentUser.isPresent() será false.

#### Pregunta 10

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se conoce el PID numérico de un proceso cualquiera del sistema y se desea obtener su manejador, se invoca el método estático Respuesta Pregunta 10 indicando dicho identificador.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Método de factoría estático común en la API de Java formado por solo dos letras.

La respuesta correcta es: of

#### Pregunta 11

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para acceder al manejador del proceso creador de un subproceso determinado, la interfaz `ProcessHandle` proporciona el método Respuesta Pregunta 11, el cual retorna un `Optional<ProcessHandle>`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Término en inglés que designa al progenitor o creador directo en una jerarquía.

La respuesta correcta es: parent

#### Pregunta 12

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué método de la interfaz Process / ProcessHandle, introducido en Java 9, devuelve un flujo de procesos que son únicamente los hijos directos del proceso en cuestión?

Pregunta 12Respuesta

a.

descendants()

b.

parent()

c.

getSubprocesses()

d.

children()

#### Retroalimentación

Respuesta incorrecta.

Este método retoma un Stream compuesto exclusivamente por los procesos creados directamente por el proceso consultado.

La respuesta correcta es: children()

#### Pregunta 13

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué método de ProcessHandle.Info debe utilizarse para obtener el tiempo acumulado de CPU consumido por un subproceso?

Pregunta 13Respuesta

a.

startInstant()

b.

user()

c.

commandLine()

d.

totalCpuDuration()

#### Retroalimentación

Respuesta incorrecta.

Este método retorna un Optional con el tiempo total de procesador acumulado por el proceso.

La respuesta correcta es: totalCpuDuration()

#### Pregunta 14

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El método `children()` de la clase `Process` devuelve un flujo de datos con la firma de tipo Respuesta Pregunta 14 que contiene exclusivamente los subprocesos generados de forma directa por dicho proceso.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Estructura funcional de Java 8+ parametrizada con la interfaz de manejo de procesos.

La respuesta correcta es: Stream<ProcessHandle>

#### Pregunta 15

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El método `commandLine()` de la clase `ProcessHandle.Info` devuelve un `Optional<String>` que representa la Respuesta Pregunta 15 completa utilizada para iniciar el subproceso.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Frase de tres palabras que describe la cadena completa introducida en la consola para ejecutar una orden.

La respuesta correcta es: línea de comandos

#### Pregunta 16

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La clase abstracta fundamental de Java que representa un proceso hijo iniciado mediante `ProcessBuilder` o `Runtime.exec()` es Respuesta Pregunta 16.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Nombre de la clase de Java cuya traducción directa al español es 'proceso'.

La respuesta correcta es: Process

#### Pregunta 17

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para consultar si un subproceso se encuentra todavía activo en el sistema operativo sin llegar a bloquear el hilo ejecutor, la clase `Process` expone el método Respuesta Pregunta 17.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es un método booleano cuyo nombre pregunta directamente si el proceso continúa con vida.

La respuesta correcta es: isAlive

#### Pregunta 18

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿A partir de qué versión de Java se introdujo la interfaz `ProcessHandle` y sus métodos asociados (`pid()`, `info()`, `children()`, etc.)?

Pregunta 18Respuesta

a.

Java 5

b.

Java 9

c.

Java 8

d.

Java 11

#### Retroalimentación

Respuesta incorrecta.

Java 9 renovó completamente la API de gestión de procesos agregando ProcessHandle y capacidades avanzadas de inspección.

La respuesta correcta es: Java 9

#### Pregunta 19

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la función principal del método `pid()` en la clase `Process` y en la interfaz `ProcessHandle`?

Pregunta 19Respuesta

a.

Devolver un objeto ProcessInformationData con las métricas de memoria del subproceso.

b.

Devolver el identificador numérico de proceso (PID) asignado por el sistema operativo de tipo long.

c.

Devolver el identificador de hilo (TID) asignado dentro de la máquina virtual de Java.

d.

Lanzar el proceso y retornar su código de inicialización nativo.

#### Retroalimentación

Respuesta incorrecta.

El método pid() permite obtener de forma estándar el identificador único entero largo que el sistema operativo asignó al proceso.

La respuesta correcta es: Devolver el identificador numérico de proceso (PID) asignado por el sistema operativo de tipo long.

#### Pregunta 20

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

A diferencia de `children()`, el método Respuesta Pregunta 20 de la clase `Process` obtiene la totalidad de la jerarquía descendente de subprocesos, abarcando hijos, nietos y sucesivos niveles.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre en inglés se refiere al conjunto completo de descendientes en un árbol genealógico.

La respuesta correcta es: descendants

#### Pregunta 21

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al consultar el código de terminación de un subproceso mediante `exitValue()`, el valor entero que indica por convención que la ejecución concluyó sin ningún error es Respuesta Pregunta 21.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

El primer número natural que representa la ausencia de errores.

La respuesta correcta es: 0

#### Pregunta 22

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el tipo de retorno del método `info().arguments()` dentro de `ProcessHandle.Info`?

Pregunta 22Respuesta

a.

Optional<String[]>

b.

String[]

c.

Optional<String>

d.

List

#### Retroalimentación

Respuesta incorrecta.

Devuelve un Optional que envuelve el arreglo de cadenas de texto correspondientes a los argumentos pasados al comando de inicio.

La respuesta correcta es: Optional<String[]>

#### Pregunta 23

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El método Respuesta Pregunta 23 de la interfaz `ProcessHandle.Info` permite consultar el tiempo total acumulado de procesamiento en la CPU consumido por el subproceso mediante un objeto `Optional<Duration>`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre describe en inglés la duración total de CPU utilizada.

La respuesta correcta es: totalCpuDuration

#### Pregunta 24

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al ejecutar `process.exitValue()` en un proceso que ha finalizado correctamente según las convenciones estándar del sistema operativo, ¿qué entero se obtiene habitualmente?

Pregunta 24Respuesta

a.

1

b.

0

c.

-1

d.

255

#### Retroalimentación

Respuesta incorrecta.

En los sistemas operativos estándar (Windows, Linux, macOS), un valor de salida de 0 indica una finalización con éxito.

La respuesta correcta es: 0

#### Pregunta 25

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para averiguar el momento exacto de inicio de la ejecución de un subproceso a través de `ProcessHandle.Info`, se debe invocar el método Respuesta Pregunta 25.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Combina la acción de iniciar con la clase del paquete `java.time` que representa un punto en la línea temporal.

La respuesta correcta es: startInstant

#### Pregunta 26

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para obtener el identificador único numérico que el sistema operativo ha asignado a una instancia de `Process` a partir de Java 9, se debe invocar el método Respuesta Pregunta 26.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Este método devuelve un valor de tipo `long` correspondiente al Process ID del sistema.

La respuesta correcta es: pid

#### Pregunta 27

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Dado que el acceso a los atributos de un subproceso varía según las restricciones de seguridad y el sistema operativo, los métodos de `ProcessHandle.Info` retornan sus datos envueltos en la clase genérica Respuesta Pregunta 27.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Contenedor introducido en Java 8 para representar explícitamente la presencia o ausencia de un valor.

La respuesta correcta es: Optional

#### Pregunta 28

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué método de `ProcessHandle.Info` devuelve la cadena de texto con la línea de comandos completa (comando y argumentos) con la que se inició el subproceso?

Pregunta 28Respuesta

a.

arguments()

b.

command()

c.

fullCommand()

d.

commandLine()

#### Retroalimentación

Respuesta incorrecta.

Este método devuelve un Optional con la representación textual completa de la instrucción invocada.

La respuesta correcta es: commandLine()

#### Pregunta 29

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué método estático de `ProcessHandle` permite obtener un flujo de todos los procesos visibles que están actualmente vivos en el sistema operativo?

Pregunta 29Respuesta

a.

ProcessHandle.allProcesses()

b.

System.getProcesses()

c.

ProcessHandle.getAll()

d.

ProcessBuilder.listProcesses()

#### Retroalimentación

Respuesta incorrecta.

Este método estático explora el sistema operativo y retorna un Stream con los procesos vivos visibles.

La respuesta correcta es: ProcessHandle.allProcesses()

#### Pregunta 30

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El método `info()` de la clase `Process` devuelve una instancia de la clase Respuesta Pregunta 30, la cual encapsula metadatos descriptivos sobre el estado y ejecución del subproceso.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Esta clase interna de información está vinculada a la interfaz de gestión de procesos del sistema introducida en Java 9.

La respuesta correcta es: ProcessHandle.Info

#### Pregunta 31

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se dispone de un objeto de tipo `Process`, se puede obtener su `ProcessHandle` asociado mediante el método de instancia Respuesta Pregunta 31.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Utiliza la preposición 'to' seguida del nombre de la interfaz objetivo.

La respuesta correcta es: toHandle

#### Pregunta 32

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para consultar la cuenta de usuario del sistema operativo bajo la cual se está ejecutando un subproceso, la interfaz `ProcessHandle.Info` expone el método Respuesta Pregunta 32.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Palabra en inglés para designar al usuario de un sistema informático.

La respuesta correcta es: user

#### Pregunta 33

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál de las siguientes combinaciones de métodos de control de procesos se encuentra disponible directamente en la interfaz `ProcessHandle`?

Pregunta 33Respuesta

a.

start(), waitFor(), destroy() y getInputStream()

b.

isAlive(), destroy(), destroyForcibly() y onExit()

c.

exec(), kill(), stop() y pause()

d.

redirectOutput(), inheritIO(), directory() y environment()

#### Retroalimentación

Respuesta incorrecta.

ProcessHandle proporciona métodos para comprobar el estado, solicitar la terminación y reaccionar asíncronamente al fin del proceso.

La respuesta correcta es: isAlive(), destroy(), destroyForcibly() y onExit()

#### Pregunta 34

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Dada una instancia `p` de la clase `Process`, ¿cuál es el método adecuado para obtener su correspondiente `ProcessHandle`?

Pregunta 34Respuesta

a.

toHandle()

b.

info().toProcessHandle()

c.

getHandle()

d.

ProcessHandle.from(p)

#### Retroalimentación

Respuesta incorrecta.

El método toHandle() convierte y adapta un objeto de la clase Process a su interfaz de control ProcessHandle.

La respuesta correcta es: toHandle()

#### Pregunta 35

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué método de `ProcessHandle.Info` debe invocarse para consultar el usuario del sistema operativo bajo el cual se ejecuta el proceso?

Pregunta 35Respuesta

a.

user()

b.

systemUser()

c.

getUserName()

d.

owner()

#### Retroalimentación

Respuesta incorrecta.

Devuelve un Optional con el nombre de cuenta del usuario propietario del proceso.

La respuesta correcta es: user()

#### Pregunta 36

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La renovada API de procesos que introdujo la interfaz `ProcessHandle` y el método `pid()` fue incorporada oficialmente en la versión Respuesta Pregunta 36 del lenguaje Java.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Versión de Java lanzada posteriormente a Java 8.

La respuesta correcta es: 9

#### Pregunta 37

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Por qué los métodos de la interfaz ProcessHandle.Info (como command(), user() o startInstant()) devuelven objetos de tipo Optional?

Pregunta 37Respuesta

a.

Porque es una exigencia de Java 9 para forzar el uso de bloques try-catch al consultar procesos.

b.

Porque la disponibilidad de la información del proceso depende del sistema operativo y de los privilegios del proceso que realiza la consulta.

c.

Porque el subproceso se ejecuta en un hilo asíncrono y la información solo está disponible si se invoca con waitFor().

d.

Porque indican si el proceso está en estado de ejecución activa o si ya ha sido destruido por la JVM.

#### Retroalimentación

Respuesta incorrecta.

La JVM abstrae la consulta al sistema operativo, donde ciertos datos pueden no estar accesibles o permitidos por restricciones de seguridad o del SO.

La respuesta correcta es: Porque la disponibilidad de la información del proceso depende del sistema operativo y de los privilegios del proceso que realiza la consulta.