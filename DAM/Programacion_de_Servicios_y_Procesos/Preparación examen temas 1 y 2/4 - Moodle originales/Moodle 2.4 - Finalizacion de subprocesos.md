# Cuestionario del apartado 2-4

##### Estado

Finalizado

##### Comenzado

miércoles, 21 de octubre de 2026, 17:51

##### Completado

miércoles, 21 de octubre de 2026, 17:51

##### Duración

9 segundos

##### Puntos

0,00/28,00

##### Calificación

**0,00** de 10,00 (**0**%)

#### Pregunta 1

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se denomina al subproceso que continúa ejecutándose cuando su proceso padre finaliza de forma inesperada sin haberlo destruido explícitamente?

Pregunta 1Respuesta

a.

Proceso huérfano.

b.

Proceso zombi.

c.

Subproceso bloqueado (deadlocked).

d.

Proceso desvinculado (detached).

#### Retroalimentación

Respuesta incorrecta.

Se le llama proceso huérfano porque su proceso creador ha terminado y él continúa vivo en el sistema consumiendo recursos.

La respuesta correcta es: Proceso huérfano.

#### Pregunta 2

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué excepción se produce cuando el proceso padre intenta seguir leyendo de process.getInputStream() después de que la tubería ha sido cerrada debido a la destrucción del subproceso?

Pregunta 2Respuesta

a.

InterruptedException.

b.

IllegalThreadStateException.

c.

NullPointerException.

d.

IOException con el mensaje 'Stream closed'.

#### Retroalimentación

Respuesta incorrecta.

Al cerrarse la tubería por la terminación del subproceso, la lectura subsiguiente sobre el flujo lanza una IOException indicando que la corriente está cerrada.

La respuesta correcta es: IOException con el mensaje 'Stream closed'.

#### Pregunta 3

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La acumulación ilimitada de datos producidos por la salida estándar de un subproceso sin que el proceso padre los consuma provoca el llenado de los búferes del sistema operativo, generando una situación de interbloqueo conocida como Respuesta Pregunta 3.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Representa el término en inglés para el bloqueo mutuo entre dos o más procesos en espera de recursos.

La respuesta correcta es: deadlock

#### Pregunta 4

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué comportamiento tiene el método waitFor() sin parámetros cuando se invoca sobre una instancia de Process?

Pregunta 4Respuesta

a.

Bloquea el proceso padre hasta que el subproceso hijo finaliza y devuelve su valor de terminación (exit value).

b.

Detiene de manera forzada la ejecución del subproceso y devuelve un código de error del sistema.

c.

Espera durante un máximo de 10 segundos por defecto y lanza una excepción si el subproceso continúa activo.

d.

Devuelve inmediatamente un booleano indicando si el proceso terminó sin bloquear al proceso padre.

#### Retroalimentación

Respuesta incorrecta.

El método waitFor() suspende el hilo actual del padre hasta que el subproceso termina, retornando el código numérico de salida de dicho subproceso.

La respuesta correcta es: Bloquea el proceso padre hasta que el subproceso hijo finaliza y devuelve su valor de terminación (exit value).

#### Pregunta 5

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si el método waitFor(5, TimeUnit.SECONDS) devuelve true, ¿cuál es la forma segura y no bloqueante de obtener el código de terminación del subproceso?

Pregunta 5Respuesta

a.

Volviendo a llamar a waitFor() sin parámetros para forzar la devolución del entero.

b.

Leyendo la primera línea de datos devuelta por process.getInputStream().

c.

Invocando al método exitValue() del objeto Process.

d.

Consultando el método pid() del subproceso.

#### Retroalimentación

Respuesta incorrecta.

Dado que el valor devuelto fue true, el subproceso ha finalizado formalmente, por lo que exitValue() devolverá el código sin lanzar excepciones.

La respuesta correcta es: Invocando al método exitValue() del objeto Process.

#### Pregunta 6

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para verificar si la plataforma o sistema operativo actual admite una terminación normal antes de invocar el método `destroy()`, la API de `Process` dispone del método Respuesta Pregunta 6.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre en inglés consulta literalmente si el sistema soporta la terminación normal.

La respuesta correcta es: supportsNormalTermination

#### Pregunta 7

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En una estrategia de espera activa con isAlive(), ¿por qué se incluye una llamada a Thread.sleep() dentro del bucle de consulta?

Pregunta 7Respuesta

a.

Para evitar que el método isAlive() lance una excepción IllegalThreadStateException.

b.

Para pausar el hilo actual y evitar sobrecargar la CPU con consultas continuas en un bucle denso.

c.

Para limpiar la marca de interrupción del hilo del proceso padre de forma automática.

d.

Para obligar al subproceso hijo a terminar su ejecución más rápidamente.

#### Retroalimentación

Respuesta incorrecta.

Introducir pequeñas pausas (ej. 50 ms) evita que el bucle de espera activa consuma el 100% de la capacidad del núcleo de CPU.

La respuesta correcta es: Para pausar el hilo actual y evitar sobrecargar la CPU con consultas continuas en un bucle denso.

#### Pregunta 8

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando se requiere forzar la terminación inmediata de un subproceso sin permitirle realizar ninguna tarea de limpieza, el método `destroyForcibly()` envía la señal Respuesta Pregunta 8 en sistemas Unix/Linux.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es la señal ininterrumpible utilizada por el kernel para matar un proceso de forma fulminante.

La respuesta correcta es: SIGKILL

#### Pregunta 9

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En sistemas de tipo Unix/Linux, la terminación suave de un subproceso iniciada con el método `destroy()` de la clase `Process` se traduce internamente en el envío de la señal Respuesta Pregunta 9 al proceso hijo.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es la señal estándar enviada en entornos POSIX para solicitar una terminación ordenada a un proceso.

La respuesta correcta es: SIGTERM

#### Pregunta 10

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué excepción comprobada (checked exception) debe gestionarse obligatoriamente al llamar al método waitFor() debido a su naturaleza bloqueante?

Pregunta 10Respuesta

a.

IllegalThreadStateException.

b.

InterruptedException.

c.

TimeoutException.

d.

IOException.

#### Retroalimentación

Respuesta incorrecta.

Como waitFor() bloquea el hilo actual, la firma del método declara InterruptedException en caso de que el hilo padre sea interrumpido durante la espera.

La respuesta correcta es: InterruptedException.

#### Pregunta 11

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si el proceso padre invoca el método `exitValue()` antes de que el subproceso haya terminado completamente su ejecución, la JVM lanzará la excepción de tipo Respuesta Pregunta 11.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Esta excepción indica que el hilo o subproceso no se encuentra en el estado adecuado para la operación solicitada.

La respuesta correcta es: IllegalThreadStateException

#### Pregunta 12

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al leer la salida de una consola de comandos en Windows (`cmd.exe`), la decodificación incorrecta de caracteres debido a la página de códigos histórica Respuesta Pregunta 12 puede causar distorsiones conocidas como mojibake.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es la denominación dada a la página de códigos predeterminada del sistema MS-DOS/Windows en regiones occidentales.

La respuesta correcta es: CP850

#### Pregunta 13

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué tipo de objeto devuelve el método onExit() de la clase Process para permitir la ejecución asíncrona tras la terminación de un subproceso?

Pregunta 13Respuesta

a.

Un objeto de tipo CompletableFuture.

b.

Un objeto de tipo Thread en estado RUNNABLE.

c.

Un objeto InputStream con el flujo de salida del subproceso.

d.

Una instancia de Optional.

#### Retroalimentación

Respuesta incorrecta.

onExit() devuelve un CompletableFuture que se marca como completado cuando el subproceso hijo finaliza.

La respuesta correcta es: Un objeto de tipo CompletableFuture.

#### Pregunta 14

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se resuelve de forma estándar en Java el riesgo de interbloqueo (deadlock) por llenado de los búferes de entrada/salida de un subproceso?

Pregunta 14Respuesta

a.

Creando en el padre hilos dedicados para leer de forma asíncrona la salida estándar y la salida de error del subproceso.

b.

Llamando únicamente a exitValue() dentro de un bucle infinito sin pausas.

c.

Reduciendo el tiempo de espera en el método waitFor() a menos de un segundo.

d.

Invocando al método destroyForcibly() inmediatamente después de llamar a start().

#### Retroalimentación

Respuesta incorrecta.

Asignar la lectura de stdout y stderr a hilos secundarios mantiene vacíos los búferes de las tuberías y evita que el hijo se bloquee.

La respuesta correcta es: Creando en el padre hilos dedicados para leer de forma asíncrona la salida estándar y la salida de error del subproceso.

#### Pregunta 15

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se llama al método cancel() sobre el CompletableFuture retornado por onExit(), ¿qué impacto tiene dicha acción sobre el subproceso hijo?

Pregunta 15Respuesta

a.

Provoca la llamada automática e inmediata a destroyForcibly() sobre el subproceso.

b.

Detiene la lectura de los búferes de entrada y salida, bloqueando al subproceso.

c.

Envía una señal SIGTERM al subproceso para solicitar su cierre elegante.

d.

No tiene ningún efecto sobre la ejecución del subproceso en el sistema operativo.

#### Retroalimentación

Respuesta incorrecta.

Cancelar el CompletableFuture en Java solo afecta a la tarea asíncrona en el proceso padre, pero no destruye ni detiene al subproceso nativo.

La respuesta correcta es: No tiene ningún efecto sobre la ejecución del subproceso en el sistema operativo.

#### Pregunta 16

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al invocar la versión sobrecargada waitFor(long timeout, TimeUnit unit), ¿qué valor retorna si expira el tiempo especificado y el subproceso sigue ejecutándose?

Pregunta 16Respuesta

a.

Retorna true y fuerza la terminación inmediata del subproceso.

b.

Lanza una excepción de tipo TimeoutException deteniendo la ejecución del proceso padre.

c.

Devuelve el valor de terminación predeterminado -1.

d.

Retorna false para indicar que el tiempo expiró sin que el subproceso hubiera finalizado.

#### Retroalimentación

Respuesta incorrecta.

La sobrecarga temporizada devuelve false si el tiempo límite se cumple y el proceso continúa con vida.

La respuesta correcta es: Retorna false para indicar que el tiempo expiró sin que el subproceso hubiera finalizado.

#### Pregunta 17

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué sucede si se invoca el método exitValue() en un objeto Process cuya ejecución aún no ha terminado?

Pregunta 17Respuesta

a.

Bloquea el hilo del proceso padre hasta que el subproceso finalice y retorne su código.

b.

Devuelve un valor genérico -1 para indicar que el proceso continúa ejecutándose.

c.

Devuelve null indicando que el valor de salida no está disponible todavía.

d.

Se lanza una excepción de tipo IllegalThreadStateException.

#### Retroalimentación

Respuesta incorrecta.

exitValue() es un método no bloqueante y la JVM lanza IllegalThreadStateException si el subproceso aún está en ejecución cuando se le consulta.

La respuesta correcta es: Se lanza una excepción de tipo IllegalThreadStateException.

#### Pregunta 18

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la causa principal de un interbloqueo (deadlock) cuando un subproceso genera un gran volumen de salida y el proceso padre ejecuta process.waitFor()?

Pregunta 18Respuesta

a.

El llenado de los búferes de capacidad limitada en las tuberías (pipes), lo que bloquea al hijo al escribir y al padre al esperar que el hijo termine.

b.

La falta de llamadas obligatorias al método destroy() antes de la llamada a waitFor().

c.

La señal SIGTERM enviada por el sistema operativo, que congela la ejecución del proceso padre.

d.

La ejecución simultánea del método exitValue() en otro hilo del proceso padre.

#### Retroalimentación

Respuesta incorrecta.

Las tuberías de stdout y stderr tienen capacidad reducida (pocos KB). Si el hijo la llena y nadie lee, se bloquea escribiendo, mientras que el padre se bloquea esperando su fin.

La respuesta correcta es: El llenado de los búferes de capacidad limitada en las tuberías (pipes), lo que bloquea al hijo al escribir y al padre al esperar que el hijo termine.

#### Pregunta 19

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuáles son las tres formas principales explicadas en la documentación para determinar desde el proceso padre si un subproceso ha finalizado su ejecución?

Pregunta 19Respuesta

a.

Bloqueo con getInputStream(), lectura de exitCode() y reinicio con start().

b.

Monitoreo con ProcessHandle.allProcesses(), pausa con Thread.sleep(), y terminación en cascada con System.exit().

c.

Espera bloqueante con waitFor(), consulta no bloqueante o espera activa con isAlive()/exitValue(), y notificación asíncrona con onExit().

d.

Redirección con inheritIO(), consulta con pid(), y destrucción mediante destroy().

#### Retroalimentación

Respuesta incorrecta.

Estas tres opciones representan los enfoques síncrono/bloqueante, sondeo periódico y reactivo/asíncrono descritos para gestionar el fin de un subproceso.

La respuesta correcta es: Espera bloqueante con waitFor(), consulta no bloqueante o espera activa con isAlive()/exitValue(), y notificación asíncrona con onExit().

#### Pregunta 20

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si al invocar waitFor() en el proceso padre, el subproceso hijo ya había finalizado previamente su ejecución, ¿cuál es el comportamiento del método?

Pregunta 20Respuesta

a.

Retorna inmediatamente devolviendo el valor de terminación del subproceso.

b.

Queda bloqueado indefinidamente a la espera de un evento de reinicio.

c.

Lanza una excepción IllegalThreadStateException por intentar esperar a un proceso inexistente.

d.

Devuelve el valor -1 indicando que la consulta fue extemporánea.

#### Retroalimentación

Respuesta incorrecta.

Si el subproceso ya ha muerto cuando se invoca waitFor(), el método no se bloquea y retorna al instante el código de salida.

La respuesta correcta es: Retorna inmediatamente devolviendo el valor de terminación del subproceso.

#### Pregunta 21

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La creación de una cadena de subprocesos enlazados donde la salida estándar de cada uno se conecta automáticamente a la entrada del siguiente se realiza mediante el método estático Respuesta Pregunta 21 de `ProcessBuilder`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre alude a la acción de iniciar una canalización o tubería de procesos.

La respuesta correcta es: startPipeline

#### Pregunta 22

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para descartar por completo el flujo de salida o error de un subproceso sin enviarlo al proceso padre ni a la consola, se utiliza el valor de redirección `ProcessBuilder.Redirect.Respuesta Pregunta 22`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es la constante de enumeración que significa desechar o descartar datos.

La respuesta correcta es: DISCARD

#### Pregunta 23

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para encadenar la ejecución asíncrona de una acción inmediatamente después de que un subproceso finalice sin bloquear el hilo actual, se utiliza el método Respuesta Pregunta 23 de la clase `Process`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Retorna un futuro completable que se activa justo al finalizar el subproceso.

La respuesta correcta es: onExit

#### Pregunta 24

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Por qué cuando un proceso padre en Java termina, el subproceso hijo puede continuar ejecutándose en el sistema operativo?

Pregunta 24Respuesta

a.

Porque la JVM no impone automáticamente una terminación en cascada y el sistema operativo trata al hijo como un proceso independiente.

b.

Porque Java convierte automáticamente todos los subprocesos en hilos demonio de la JVM.

c.

Porque los subprocesos creados por Java se ejecutan siempre dentro del espacio de memoria de la propia JVM.

d.

Porque el subproceso hijo hereda automáticamente el PID del proceso padre evitando ser cerrado.

#### Retroalimentación

Respuesta incorrecta.

La JVM no gestiona de forma nativa el ciclo de vida en cascada de los subprocesos, por lo que el SO mantiene vivo al hijo si el padre finaliza.

La respuesta correcta es: Porque la JVM no impone automáticamente una terminación en cascada y el sistema operativo trata al hijo como un proceso independiente.

#### Pregunta 25

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En sistemas Unix/Linux, ¿a qué señal del sistema operativo se traduce habitualmente una llamada al método destroy() de Process para lograr una terminación normal?

Pregunta 25Respuesta

a.

A la señal de suspensión de proceso SIGSTOP.

b.

A la señal de terminación suave SIGTERM.

c.

A la señal de terminación abrupta SIGKILL.

d.

A la señal de interrupción de teclado SIGINT.

#### Retroalimentación

Respuesta incorrecta.

destroy() envía la señal SIGTERM en sistemas Unix/Linux, lo que notifica al proceso para que pueda realizar la limpieza de sus recursos antes de salir.

La respuesta correcta es: A la señal de terminación suave SIGTERM.

#### Pregunta 26

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué señal envía el sistema operativo Unix/Linux cuando se invoca el método destroyForcibly() sobre un subproceso?

Pregunta 26Respuesta

a.

La señal de cierre de tubería SIGPIPE.

b.

La señal de terminación abrupta e inmediata SIGKILL.

c.

La señal de terminación suave SIGTERM.

d.

La señal de notificación de hijo finalizado SIGCHLD.

#### Retroalimentación

Respuesta incorrecta.

destroyForcibly() fuerza la detención inmediata del proceso en Unix/Linux enviando una señal SIGKILL que no puede ser ignorada.

La respuesta correcta es: La señal de terminación abrupta e inmediata SIGKILL.

#### Pregunta 27

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la secuencia de pasos recomendada (patrón por etapas) para finalizar explícitamente un subproceso desde el proceso padre?

Pregunta 27Respuesta

a.

Cancelar el CompletableFuture de onExit(), llamar a destroy() y finalizar el proceso con Thread.sleep().

b.

Llamar directamente a destroyForcibly(), cerrar los pipes con close() y verificar el estado con exitValue().

c.

Intentar primero destroy(), esperar un tiempo razonable con waitFor(timeout, unit) y, si no finaliza, llamar a destroyForcibly().

d.

Invocar isAlive(), llamar a System.exit(0) en el padre y esperar a que el sistema operativo los cierre en cascada.

#### Retroalimentación

Respuesta incorrecta.

Este patrón prioriza dar tiempo al subproceso para realizar un cierre ordenado antes de forzar su terminación abrupta.

La respuesta correcta es: Intentar primero destroy(), esperar un tiempo razonable con waitFor(timeout, unit) y, si no finaliza, llamar a destroyForcibly().

#### Pregunta 28

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Para qué sirve el método supportsNormalTermination() introducido en Java 9 dentro de la clase Process?

Pregunta 28Respuesta

a.

Para comprobar si un proceso finalizó con un valor de salida igual a 0.

b.

Para verificar si la plataforma o sistema operativo admite la terminación suave o elegante mediante destroy().

c.

Para indicar si el subproceso permite leer de su entrada estándar sin causar bloqueos.

d.

Para determinar si un proceso fue terminado obligatoriamente mediante una señal SIGKILL.

#### Retroalimentación

Respuesta incorrecta.

Permite saber si destroy() intentará una terminación ordenada (SIGTERM) o si la plataforma no lo distingue y funcionará directamente como forzada.

La respuesta correcta es: Para verificar si la plataforma o sistema operativo admite la terminación suave o elegante mediante destroy().