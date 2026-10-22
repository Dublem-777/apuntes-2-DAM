# Cuestionario del apartado 2-3

##### Estado

Finalizado

##### Comenzado

miércoles, 21 de octubre de 2026, 17:50

##### Completado

miércoles, 21 de octubre de 2026, 17:50

##### Duración

10 segundos

##### Puntos

0,00/36,00

##### Calificación

**0,00** de 10,00 (**0**%)

#### Pregunta 1

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el modelo de comunicación por defecto entre un proceso padre y un subproceso hijo en Java, ¿qué método de la clase Process debe utilizar el proceso padre para leer la salida estándar (stdout) generada por el hijo?

Pregunta 1Respuesta

a.

getInputStream()

b.

getOutputStream()

c.

getErrorStream()

d.

getStandardOutput()

#### Retroalimentación

Respuesta incorrecta.

Permite obtener el flujo de entrada desde el cual el proceso padre lee lo que el subproceso escribe en su salida estándar.

La respuesta correcta es: getInputStream()

#### Pregunta 2

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿En qué momento debe realizarse la configuración de redirección de flujos (redirectInput, redirectOutput, etc.) mediante la API de ProcessBuilder?

Pregunta 2Respuesta

a.

Únicamente cuando el proceso hijo se encuentre en estado bloqueado.

b.

Inmediatamente después de llamar a start(), utilizando el objeto Process obtenido.

c.

En cualquier momento del ciclo de vida del proceso antes de llamar a waitFor().

d.

Siempre antes de invocar el método start() del ProcessBuilder.

#### Retroalimentación

Respuesta incorrecta.

La configuración de redirección modifica los parámetros con los que el sistema operativo creará el proceso, por lo que debe establecerse antes de llamar a start().

La respuesta correcta es: Siempre antes de invocar el método start() del ProcessBuilder.

#### Pregunta 3

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para descartar por completo el flujo de salida o error de un subproceso sin procesarlo ni mostrarlo, se utiliza la constante de redirección Redirect.Respuesta Pregunta 3.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es un término en inglés que indica desechar o descartar datos.

La respuesta correcta es: DISCARD

#### Pregunta 4

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué problema crítico de concurrencia (deadlock) puede ocurrir si un subproceso hijo produce abundante salida por stdout o stderr y el proceso padre no lee esos flujos mientras ejecuta process.waitFor()?

Pregunta 4Respuesta

a.

El flujo del subproceso hijo se redirige automáticamente al archivo out.txt para liberar espacio.

b.

La JVM destruye automáticamente el subproceso hijo por superar el límite de memoria del búfer.

c.

El método waitFor() lanza una IllegalThreadStateException de forma asíncrona.

d.

La tubería del sistema operativo llena su búfer limitado, lo que provoca que el subproceso hijo se bloquee al intentar escribir, impidiendo que termine.

#### Retroalimentación

Respuesta incorrecta.

Los búferes de las tuberías del sistema operativo tienen capacidad limitada; si se llenan y nadie lee, el proceso hijo se bloquea al escribir, generando un interbloqueo con el padre que espera su finalización.

La respuesta correcta es: La tubería del sistema operativo llena su búfer limitado, lo que provoca que el subproceso hijo se bloquee al intentar escribir, impidiendo que termine.

#### Pregunta 5

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué efecto tiene invocar el método redirectErrorStream(true) sobre un objeto ProcessBuilder antes de iniciar el proceso?

Pregunta 5Respuesta

a.

Descarta por completo cualquier mensaje de error generado por el subproceso.

b.

Redirige la salida estándar (stdout) directamente a la consola del padre y conserva stderr en la tubería por defecto.

c.

Combina la salida de error estándar (stderr) con la salida estándar (stdout), haciendo que getErrorStream() devuelva un flujo nulo.

d.

Lanza una excepción de entrada/salida si no se ha configurado previamente un archivo de destino.

#### Retroalimentación

Respuesta incorrecta.

Al combinar ambos flujos en la salida estándar, el flujo de error queda redireccionado a un objeto nulo y los errores se leen mediante getInputStream().

La respuesta correcta es: Combina la salida de error estándar (stderr) con la salida estándar (stdout), haciendo que getErrorStream() devuelva un flujo nulo.

#### Pregunta 6

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se desea que un subproceso comparta exactamente el mismo destino de salida o entrada que su proceso padre (como la consola), se debe utilizar la constante Redirect.Respuesta Pregunta 6.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Corresponde al verbo en inglés que significa heredar.

La respuesta correcta es: INHERIT

#### Pregunta 7

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Por qué se afirma que la comunicación mediante flujos (pipes) entre un proceso padre y un subproceso produce una "sincronización implícita"?

Pregunta 7Respuesta

a.

Porque la JVM utiliza internamente cerrojos de tipo ReentrantLock para coordinar los hilos del proceso padre y el proceso hijo.

b.

Porque la lectura y la escritura en las tuberías son operaciones bloqueantes, ajustando el ritmo de los procesos sin necesidad de mecanismos adicionales de sincronización.

c.

Porque los procesos comparten la misma región de memoria RAM gestionada por el sistema operativo.

d.

Porque el sistema operativo congela la ejecución del proceso hijo en cada salto de línea de su salida.

#### Retroalimentación

Respuesta incorrecta.

El carácter bloqueante de las tuberías sincroniza de forma natural al emisor y al receptor, ralentizando o pausando la ejecución según la disponibilidad de datos o espacio en búfer.

La respuesta correcta es: Porque la lectura y la escritura en las tuberías son operaciones bloqueantes, ajustando el ritmo de los procesos sin necesidad de mecanismos adicionales de sincronización.

#### Pregunta 8

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En la clase ProcessBuilder, invocar el método inheritIO() equivale exactamente a ejecutar de forma secuencial ¿qué combinación de métodos?

Pregunta 8Respuesta

a.

redirectInput(Redirect.PIPE), redirectOutput(Redirect.PIPE) y redirectError(Redirect.PIPE)

b.

redirectInput(Redirect.DISCARD), redirectOutput(Redirect.DISCARD) y redirectError(Redirect.DISCARD)

c.

redirectInput(Redirect.INHERIT), redirectOutput(Redirect.INHERIT) y redirectError(Redirect.INHERIT)

d.

redirectErrorStream(true) seguido de redirectOutput(Redirect.INHERIT)

#### Retroalimentación

Respuesta incorrecta.

inheritIO() es un método de conveniencia que aplica la redirección Redirect.INHERIT a la entrada, salida y salida de error del subproceso de forma consecutiva.

La respuesta correcta es: redirectInput(Redirect.INHERIT), redirectOutput(Redirect.INHERIT) y redirectError(Redirect.INHERIT)

#### Pregunta 9

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si en un ProcessBuilder se configuran conjuntamente redirectErrorStream(true) y redirectOutput(new File("salida.txt")), ¿a dónde se enviará la salida de error estándar (stderr) del subproceso?

Pregunta 9Respuesta

a.

Se descartará por completo al no haber configurado un archivo explícito con redirectError.

b.

Lanza una excepción al iniciar el proceso por conflicto de redirecciones.

c.

A la consola del proceso padre mediante la tubería predeterminada.

d.

Al archivo salida.txt, combinada con la salida estándar.

#### Retroalimentación

Respuesta incorrecta.

Como redirectErrorStream(true) fusiona stderr con stdout, cualquier redirección sobre stdout (como un archivo) aplicará también a los mensajes de error.

La respuesta correcta es: Al archivo salida.txt, combinada con la salida estándar.

#### Pregunta 10

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la diferencia fundamental entre utilizar ProcessBuilder.Redirect.to(file) y ProcessBuilder.Redirect.appendTo(file) para redirigir la salida de un proceso?

Pregunta 10Respuesta

a.

appendTo(file) permite escritura concurrente de múltiples procesos, mientras que to(file) bloquea el archivo de forma exclusiva.

b.

to(file) sobrescribe el contenido del fichero si existe, mientras que appendTo(file) escribe al final del fichero preservando el contenido previo.

c.

to(file) redirige únicamente la salida estándar, mientras que appendTo(file) redirige automáticamente la salida de error.

d.

to(file) crea un archivo temporal en la carpeta del sistema, mientras que appendTo(file) requiere que el archivo ya exista.

#### Retroalimentación

Respuesta incorrecta.

to(file) truncará y sobrescribirá el fichero indicado, mientras que appendTo(file) añadirá los datos al final de este.

La respuesta correcta es: to(file) sobrescribe el contenido del fichero si existe, mientras que appendTo(file) escribe al final del fichero preservando el contenido previo.

#### Pregunta 11

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En sistemas Windows, la consola de comandos históricamente utiliza la página de códigos Respuesta Pregunta 11, por lo que el proceso padre debe especificarla explícitamente para evitar la aparición de caracteres corruptos (mojibake).

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es la denominación habitual de la página de códigos del símbolo del sistema en entorns occidentales.

La respuesta correcta es: CP850

#### Pregunta 12

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El valor por defecto para las redirecciones de entrada y salida en ProcessBuilder, donde el destinatario del flujo es el propio proceso padre a través de una tubería, corresponde a Redirect.Respuesta Pregunta 12.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es el término en inglés utilizado para denominar a las tuberías de comunicación de datos.

La respuesta correcta es: PIPE

#### Pregunta 13

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando el proceso padre necesita enviar datos hacia la entrada estándar (stdin) de un subproceso hijo, debe escribir en el flujo devuelto por el método Respuesta Pregunta 13.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

El proceso padre envía información escribiendo en un flujo de salida hacia el hijo.

La respuesta correcta es: getOutputStream

#### Pregunta 14

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Complete el espacio en blanco con el término adecuado: Cuando un proceso padre realiza una operación de lectura sobre la salida del subproceso y el búfer está vacío, el proceso padre queda ______ hasta que el subproceso escriba datos o cierre el flujo.

Pregunta 14Respuesta

a.

redirigido

b.

destruido

c.

desvinculado (detached)

d.

bloqueado

#### Retroalimentación

Respuesta incorrecta.

El proceso padre permanece en estado bloqueado en la llamada de lectura hasta que el subproceso genere datos o se cierre la tubería.

La respuesta correcta es: bloqueado

#### Pregunta 15

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El método de la clase ProcessBuilder que equivale a invocar secuencialmente la redirección a Redirect.INHERIT para la entrada, la salida y el error estándar es Respuesta Pregunta 15.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Suma la acción de heredar con las siglas habituales para la entrada/salida.

La respuesta correcta es: inheritIO

#### Pregunta 16

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

A partir de Java 17, ¿qué nuevos métodos convenientes se incorporaron a la clase Process para simplificar la lectura/escritura directa de flujos sin instanciar manualmente un InputStreamReader o OutputStreamWriter?

Pregunta 16Respuesta

a.

readInput(), writeOutput() y readError()

b.

inputReader(), outputWriter() y errorReader()

c.

openInputStream(), openOutputStream() y openErrorStream()

d.

getReader(), getWriter() y getErrReader()

#### Retroalimentación

Respuesta incorrecta.

En Java 17 se agregaron estos métodos directos a Process para retornar directamente instancias de BufferedReader y BufferedWriter.

La respuesta correcta es: inputReader(), outputWriter() y errorReader()

#### Pregunta 17

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El método ProcessBuilder.startPipeline recibe una lista de objetos ProcessBuilder y devuelve un objeto de tipo List<Respuesta Pregunta 17>.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Representa la clase fundamental que encapsula a cada proceso en ejecución.

La respuesta correcta es: Process

#### Pregunta 18

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

A partir de Java 17, el método de la clase Process que permite obtener directamente un BufferedReader configurado para la salida de error del subproceso es Respuesta Pregunta 18.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Combina la palabra 'error' con la clase 'Reader' correspondiente.

La respuesta correcta es: errorReader

#### Pregunta 19

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al ejecutar un subproceso en Windows y leer su salida estándar sin especificar una codificación, suele producirse el fenómeno conocido como mojibake (caracteres basura). ¿A qué se debe esto principalmente según la fuente?

Pregunta 19Respuesta

a.

A que la clase InputStreamReader solo admite codificaciones Unicode de 16 bits en plataformas Windows.

b.

A que la JVM en Windows desactiva la conversión automática de caracteres en la entrada estándar.

c.

A que los subprocesos de Windows no soportan flujos basados en tuberías (pipes).

d.

A que la consola de comandos de Windows históricamente utiliza la página de códigos CP850 mientras que Java intenta decodificar usando la codificación por defecto de la JVM.

#### Retroalimentación

Respuesta incorrecta.

Ocurre porque la consola de Windows utiliza CP850 mientras que la JVM suele interpretar los bytes entrantes mediante UTF-8 o Windows-1252.

La respuesta correcta es: A que la consola de comandos de Windows históricamente utiliza la página de códigos CP850 mientras que Java intenta decodificar usando la codificación por defecto de la JVM.

#### Pregunta 20

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para iniciar una cadena de subprocesos enlazados donde la salida de uno se conecta automáticamente a la entrada del siguiente, se utiliza el método estático Respuesta Pregunta 20 de la clase ProcessBuilder.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Une la palabra de inicio en inglés con el término para una tubería en cadena.

La respuesta correcta es: startPipeline

#### Pregunta 21

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Con respecto a los extremos de una tubería o pipeline creada con ProcessBuilder.startPipeline(), ¿cuál es la configuración por defecto para el primer y el último proceso?

Pregunta 21Respuesta

a.

La stdin del primer proceso y la stdout del último proceso se configuran automáticamente como Redirect.INHERIT.

b.

Ambos extremos se configuran como Redirect.DISCARD para evitar fuga de recursos.

c.

La stdin del primer proceso y la stdout del último proceso son por defecto Redirect.PIPE, lo que permite que el proceso padre interactúe con ellos.

d.

El primer proceso debe leer obligatoriamente de un archivo con Redirect.from() y el último escribir con Redirect.to().

#### Retroalimentación

Respuesta incorrecta.

Al mantener Redirect.PIPE en los extremos, se permite que el proceso padre envíe datos al inicio de la tubería y lea la salida del proceso final.

La respuesta correcta es: La stdin del primer proceso y la stdout del último proceso son por defecto Redirect.PIPE, lo que permite que el proceso padre interactúe con ellos.

#### Pregunta 22

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para que el proceso padre lea la salida estándar (stdout) generada por un subproceso hijo, debe obtener el flujo mediante el método Respuesta Pregunta 22 de la clase Process.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

A pesar de que el proceso hijo escribe en su salida, desde la perspectiva del padre se debe utilizar un flujo de entrada.

La respuesta correcta es: getInputStream

#### Pregunta 23

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se desea que un subproceso hijo comparta los mismos destinos de entrada, salida y error que el proceso padre (como la consola del sistema), ¿cuál es el valor constante de ProcessBuilder.Redirect correspondiente?

Pregunta 23Respuesta

a.

Redirect.PARENT

b.

Redirect.INHERIT

c.

Redirect.PIPE

d.

Redirect.DISCARD

#### Retroalimentación

Respuesta incorrecta.

Redirect.INHERIT establece que el subproceso compartirá los mismos flujos de E/S que tiene asignados el proceso padre.

La respuesta correcta es: Redirect.INHERIT

#### Pregunta 24

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué tipo de objeto devuelve el método estático ProcessBuilder.startPipeline(List builders)?

Pregunta 24Respuesta

a.

Un objeto ProcessPipeline que expone métodos para pausar o reanudar el flujo.

b.

Un objeto único de tipo Process que representa la tubería completa consolidada.

c.

Un array de enteros con los PID de los procesos creados en el sistema operativo.

d.

Un objeto de tipo List, que contiene una instancia de Process por cada ProcessBuilder de la lista, en el mismo orden.

#### Retroalimentación

Respuesta incorrecta.

startPipeline() inicia cada proceso ordenadamente y retorna la lista completa de instancias Process correspondientes a la secuencia.

La respuesta correcta es: Un objeto de tipo List, que contiene una instancia de Process por cada ProcessBuilder de la lista, en el mismo orden.

#### Pregunta 25

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué interfaz debe implementar una clase para que sus instancias puedan ser gestionadas y cerradas automáticamente dentro de una estructura try-with-resources?

Pregunta 25Respuesta

a.

CloseableStream

b.

Flushable

c.

AutoCloseable

d.

ProcessResource

#### Retroalimentación

Respuesta incorrecta.

Las clases que implementan AutoCloseable garantizan la invocación automática de su método close() al salir del bloque try-with-resources.

La respuesta correcta es: AutoCloseable

#### Pregunta 26

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se requiere redirigir la salida de un subproceso a un archivo escribiendo al final sin sobrescribir el contenido preexistente, se debe utilizar el método estático Redirect.Respuesta Pregunta 26.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es un método factoría cuyo nombre en inglés significa adjuntar o añadir al final.

La respuesta correcta es: appendTo

#### Pregunta 27

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para combinar la salida de error estándar (stderr) con la salida estándar (stdout) en un único flujo leíble a través de getInputStream(), se debe invocar el método Respuesta Pregunta 27 pasando el argumento true.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre alude a la redirección del flujo o canal de errores.

La respuesta correcta es: redirectErrorStream

#### Pregunta 28

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En un pipeline de subprocesos creado mediante ProcessBuilder.startPipeline(processBuilderList) (introducido en Java 9), ¿cómo están configurados y restringidos los flujos intermedios entre los procesos de la lista?

Pregunta 28Respuesta

a.

Están configurados como Redirect.INHERIT por defecto y pueden redirigirse libremente a archivos temporales.

b.

Son redirigidos automáticamente a Redirect.DISCARD para optimizar el rendimiento.

c.

Deben ser configurados manualmente por el desarrollador mediante redirectOutput(Redirect.to(pipe)) antes de llamar a startPipeline().

d.

Están implícitamente configurados como Redirect.PIPE y no pueden ser redirigidos.

#### Retroalimentación

Respuesta incorrecta.

En un pipeline, la salida estándar de cada proceso se conecta a la entrada del siguiente mediante tuberías fijadas como Redirect.PIPE, prohibiendo su redirección explícita.

La respuesta correcta es: Están implícitamente configurados como Redirect.PIPE y no pueden ser redirigidos.

#### Pregunta 29

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La estructura de control introducida en Java 7 que asegura el cierre automático de los flujos de E/S al finalizar el bloque de ejecución se denomina Respuesta Pregunta 29.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre combina la palabra clave para la gestión de excepciones con el término que designa a los recursos asignados.

La respuesta correcta es: try-with-resources

#### Pregunta 30

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para que un subproceso tome su entrada estándar directamente desde un archivo en el disco, se debe invocar el método redirectInput pasándole el resultado del método factoría Redirect.Respuesta Pregunta 30.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Preposición en inglés que indica la procedencia u origen de los datos.

La respuesta correcta es: from

#### Pregunta 31

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando el proceso padre intenta leer datos del flujo de salida de un subproceso y el búfer está vacío, la ejecución del proceso padre queda en estado Respuesta Pregunta 31 hasta que haya datos disponibles.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Indica el estado de suspensión en el que la ejecución no progresa hasta recibir eventos o datos.

La respuesta correcta es: bloqueado

#### Pregunta 32

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué sucede cuando el proceso padre intenta leer datos del InputStream de un subproceso hijo mediante una operación de lectura y el búfer de comunicación de la tubería está vacío?

Pregunta 32Respuesta

a.

La operación se bloquea hasta que el subproceso escriba datos en su salida estándar o cierre el flujo.

b.

El método devuelve inmediatamente el valor -1 notificando la ausencia temporal de datos.

c.

Se lanza inmediatamente una excepción de tipo IOException indicando que el búfer está vacío.

d.

Se interrumpe el subproceso hijo para forzar la generación de datos.

#### Retroalimentación

Respuesta incorrecta.

Las operaciones de lectura sobre tuberías son bloqueantes y detienen la ejecución del padre hasta que haya datos disponibles o finalice el flujo.

La respuesta correcta es: La operación se bloquea hasta que el subproceso escriba datos en su salida estándar o cierre el flujo.

#### Pregunta 33

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el valor por defecto de redirección que asigna la API de ProcessBuilder a los flujos stdout, stderr y stdin de un subproceso si no se modifica la configuración?

Pregunta 33Respuesta

a.

null

b.

Redirect.PIPE

c.

Redirect.INHERIT

d.

Redirect.DISCARD

#### Retroalimentación

Respuesta incorrecta.

Redirect.PIPE es el valor predeterminado que establece tuberías de comunicación entre el proceso padre y el subproceso.

La respuesta correcta es: Redirect.PIPE

#### Pregunta 34

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si el proceso padre necesita enviar datos a la entrada estándar (stdin) del subproceso hijo, ¿a través de qué método del objeto Process debe obtener el flujo correspondiente?

Pregunta 34Respuesta

a.

setInputWriter()

b.

getInputStream()

c.

getOutputStream()

d.

getErrorStream()

#### Retroalimentación

Respuesta incorrecta.

El proceso padre escribe en este flujo de salida para enviar información que el subproceso recibirá a través de su entrada estándar.

La respuesta correcta es: getOutputStream()

#### Pregunta 35

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para que un recurso de E/S pueda ser utilizado dentro de un bloque try-with-resources y cerrarse automáticamente, debe implementar la interfaz Respuesta Pregunta 35.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

El nombre de esta interfaz estándar hace referencia explícita al cierre automático.

La respuesta correcta es: AutoCloseable

#### Pregunta 36

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

A partir de Java 17, el método de la clase Process que devuelve directamente un BufferedReader para leer la salida estándar del subproceso es Respuesta Pregunta 36.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Su nombre combina el término de entrada de datos con la clase Reader correspondiente.

La respuesta correcta es: inputReader