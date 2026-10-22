# Cuestionario del apartado 2-2

##### Estado

Finalizado

##### Comenzado

miércoles, 14 de octubre de 2026, 18:53

##### Completado

miércoles, 21 de octubre de 2026, 17:50

##### Duración

6 días 22 horas

##### Puntos

0,00/36,00

##### Calificación

**0,00** de 10,00 (**0**%)

#### Pregunta 1

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se invoca el método `pbuilder.command(...)` para modificar la orden de ejecución después de haber llamado a `pbuilder.start()`, ¿qué ocurre con el subproceso recién creado?

Pregunta 1Respuesta

a.

Se envía una señal de cancelación inmediata para detener el subproceso actual antes de modificar la orden.

b.

El subproceso ya iniciado no se ve afectado, pero la nueva configuración se aplicará a futuras llamadas a `start()`.

c.

Se lanza inmediatamente una excepción `IllegalStateException` porque el `ProcessBuilder` queda bloqueado tras la ejecución.

d.

El subproceso ya iniciado se reconfigura y reinicia automáticamente con la nueva lista de comandos.

#### Retroalimentación

Respuesta incorrecta.

`command()` modifica el estado interno del objeto `ProcessBuilder`, de modo que no altera la instancia `Process` en ejecución pero sí afectará a los procesos lanzados posteriormente.

La respuesta correcta es: El subproceso ya iniciado no se ve afectado, pero la nueva configuración se aplicará a futuras llamadas a `start()`.

#### Pregunta 2

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la diferencia fundamental entre el mapa devuelto por `System.getenv()` y el devuelto por `ProcessBuilder.environment()`?

Pregunta 2Respuesta

a.

El mapa de `System.getenv()` permite modificar variables del sistema operativo globalmente, mientras que el de `ProcessBuilder` solo afecta al proceso padre.

b.

El mapa de `System.getenv()` es de solo lectura, mientras que el de `ProcessBuilder.environment()` es modificable y permite ajustar las variables para el subproceso.

c.

Ambos mapas son de solo lectura, exigiendo el uso de parámetros de línea de comandos para pasar variables al subproceso.

d.

`ProcessBuilder.environment()` devuelve un mapa vacío por defecto que debe poblarse desde cero, a diferencia de `System.getenv()`.

#### Retroalimentación

Respuesta incorrecta.

El mapa devuelto por `System.getenv()` no permite escrituras, mientras que `ProcessBuilder.environment()` devuelve un mapa mutable prepoblado con las variables del padre que se pueden modificar antes de llamar a `start()`.

La respuesta correcta es: El mapa de `System.getenv()` es de solo lectura, mientras que el de `ProcessBuilder.environment()` es modificable y permite ajustar las variables para el subproceso.

#### Pregunta 3

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si se requiere consultar o modificar la lista de tokens que componen la orden de un `ProcessBuilder` con posterioridad a su instanciación, se debe invocar su método `Respuesta Pregunta 3()`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Método de `ProcessBuilder` que devuelve la lista mutable con los componentes de la orden a ejecutar.

La respuesta correcta es: command

#### Pregunta 4

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el directorio de trabajo predeterminado (_working directory_) de un subproceso creado con `ProcessBuilder` si no se modifica expresamente mediante `directory(File)`?

Pregunta 4Respuesta

a.

La carpeta temporal del sistema definida en la variable de entorno `TEMP` o `/tmp`.

b.

La ubicación exacta del ejecutable `java` dentro del sistema de archivos.

c.

El directorio raíz del sistema operativo (`C:\` en Windows o `/` en Unix).

d.

El directorio indicado por la propiedad del sistema `user.dir` del proceso padre.

#### Retroalimentación

Respuesta incorrecta.

Si no se especifica un directorio de trabajo distinto, el subproceso hereda el directorio de trabajo actual del proceso padre provisto por `user.dir`.

La respuesta correcta es: El directorio indicado por la propiedad del sistema `user.dir` del proceso padre.

#### Pregunta 5

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Antes de invocar métodos de acción sobre un objeto `Desktop` (como `desktop.browse(uri)` o `desktop.open(file)`), ¿qué dos comprobaciones de compatibilidad se deben realizar?

Pregunta 5Respuesta

a.

Comprobar que `System.getenv("DESKTOP") != null` y verificar los permisos de administrador del usuario.

b.

Verificar si la propiedad `os.name` contiene "win" y comprobar el espacio en memoria mediante `Runtime.getRuntime().freeMemory()`.

c.

Verificar `Desktop.isDesktopSupported()` y posteriormente `desktop.isSupported(Desktop.Action)`.

d.

Validar que el archivo exista mediante `file.exists()` y comprobar que la versión de Java sea superior a 18.

#### Retroalimentación

Respuesta incorrecta.

Se debe confirmar primero si el entorno admite la API `Desktop` (no _headless_) y luego si la plataforma admite la acción específica (`BROWSE`, `OPEN`, etc.) a través del enum `Desktop.Action`.

La respuesta correcta es: Verificar `Desktop.isDesktopSupported()` y posteriormente `desktop.isSupported(Desktop.Action)`.

#### Pregunta 6

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para verificar si el sistema operativo específico en el que se ejecuta la aplicación puede realizar una acción concreta (como imprimir o editar) con la clase `Desktop`, se utiliza el método `isSupported()`, pasándole una constante del enumerado `Desktop.Respuesta Pregunta 6`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Nombre de la enumeración interna de `Desktop` traducida al español como 'Acción'.

La respuesta correcta es: Action

#### Pregunta 7

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La clase `ProcessBuilder`, recomendada desde Java 5 para la creación de subprocesos, pertenece al patrón de diseño de construcción de objetos y requiere el uso del método `Respuesta Pregunta 7` para iniciar la ejecución del subproceso configurado.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Nombre del método de la clase `ProcessBuilder` que activa y pone en marcha el subproceso.

La respuesta correcta es: start

#### Pregunta 8

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al instanciar un objeto `ProcessBuilder` para ejecutar `cmd /c dir /o`, ¿cuál es un error común al pasar los comandos como argumento?

Pregunta 8Respuesta

a.

Utilizar barras diagonales `/` para los modificadores `/c` y `/o` en lugar de barras invertidas `\`.

b.

Pasar la cadena completa `"cmd /c dir /o"` como un único argumento en el constructor.

c.

Utilizar una lista de cadenas `List<String>` en lugar de un array varargs.

d.

No incluir la extensión `.exe` explícitamente en el primer elemento `"cmd.exe"`.

#### Retroalimentación

Respuesta incorrecta.

Pasar una sola cadena con espacios provoca que `ProcessBuilder` busque un ejecutable cuya ruta coincida literalmente con todo el texto, fallando salvo que se separen los tokens o se use `split("\\s")`.

La respuesta correcta es: Pasar la cadena completa `"cmd /c dir /o"` como un único argumento en el constructor.

#### Pregunta 9

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La clase `System` invoca internamente al método `Runtime.getRuntime().Respuesta Pregunta 9(status)` cuando se desea finalizar formalmente la ejecución de la máquina virtual de Java.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es el nombre del método de la clase `Runtime` encargado de detener la JVM recibiendo un entero como estado.

La respuesta correcta es: exit

#### Pregunta 10

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para establecer el directorio de trabajo inicial de un proceso a través de `ProcessBuilder`, se emplea el método `directory()`, el cual recibe un objeto de tipo `Respuesta Pregunta 10`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Nombre de la clase principal del paquete `java.io` utilizada para hacer referencia a archivos y rutas.

La respuesta correcta es: File

#### Pregunta 11

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si una aplicación Java finaliza debido a una excepción no capturada (uncaught exception) sin invocar explícitamente `System.exit()`, ¿qué valor de terminación (_exit value_) recibe el sistema operativo?

Pregunta 11Respuesta

a.

Devuelve siempre -1, indicando un fallo genérico de ejecución en la JVM.

b.

El valor 255, que representa el código de error estándar por defecto en Java.

c.

Siempre se devuelve 0 porque el proceso principal concluyó su ciclo de ejecución.

d.

Un valor distinto de 0 determinado por la Máquina Virtual de Java (JVM).

#### Retroalimentación

Respuesta incorrecta.

Ante una excepción no controlada que aborta la ejecución, la propia JVM asigna y retorna un código de salida distinto de cero para señalar el fallo al sistema operativo.

La respuesta correcta es: Un valor distinto de 0 determinado por la Máquina Virtual de Java (JVM).

#### Pregunta 12

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué métodos de la clase `java.lang.Runtime` permiten inspeccionar la memoria del entorno de ejecución en bytes?

Pregunta 12Respuesta

a.

`getUsedMemory()`, `getAvailableMemory()` y `getHeapSize()`.

b.

`systemMemory()`, `allocatedMemory()` y `peakMemory()`.

c.

`freeMemory()`, `totalMemory()` y `maxMemory()`.

d.

`ramFree()`, `ramTotal()` y `ramLimit()`.

#### Retroalimentación

Respuesta incorrecta.

La clase `Runtime` expone `freeMemory()` (memoria libre), `totalMemory()` (memoria total reservada) y `maxMemory()` (máxima memoria que la JVM intentará usar).

La respuesta correcta es: `freeMemory()`, `totalMemory()` y `maxMemory()`.

#### Pregunta 13

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al lanzar un comando interno de la consola de Windows (como `dir` o `ipconfig`) desde Java con `ProcessBuilder`, ¿por qué se requiere invocar `cmd.exe /c`?

Pregunta 13Respuesta

a.

Porque el argumento `/c` mantiene abierta la consola para poder leer la salida estándar desde Java.

b.

Porque los comandos internos no son archivos ejecutables independientes, sino funciones pertenecientes al intérprete de comandos.

c.

Porque `ProcessBuilder` solo reconoce archivos con extensión `.exe` si no se especifica un intérprete intermediario.

d.

Porque Windows prohíbe la ejecución directa de cualquier binario sin privilegios elevados provistos por `cmd.exe`.

#### Retroalimentación

Respuesta incorrecta.

Instrucciones como `dir` o `echo` están integradas dentro del propio `cmd.exe` y requieren que el intérprete las procese para poder ejecutarse.

La respuesta correcta es: Porque los comandos internos no son archivos ejecutables independientes, sino funciones pertenecientes al intérprete de comandos.

#### Pregunta 14

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando un proceso termina su ejecución con un estado de error, devuelve al sistema operativo un valor de terminación (exit value) representado por un número entre 1 y Respuesta Pregunta 14 .

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Piensa en el valor máximo que puede tomar el código numérico de error en el rango estándar de un byte.

La respuesta correcta es: 255

#### Pregunta 15

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué efecto importante tiene utilizar la instrucción `start` mediante `cmd.exe /c start notepad.exe` al crear un subproceso desde Java?

Pregunta 15Respuesta

a.

Genera una excepción `SecurityException` inmediata salvo que el usuario ejecute Java con privilegios de administrador.

b.

Obliga a Java a bloquear el hilo principal hasta que la ventana de la aplicación lanzada se cierre.

c.

El nuevo proceso se ejecuta de forma desvinculada (_detached_), por lo que Java no podrá leer su salida ni lo cerrará al terminar el programa padre.

d.

Permite capturar la salida de error estándar (`stderr`), pero bloquea la lectura de la salida estándar (`stdout`).

#### Retroalimentación

Respuesta incorrecta.

El comando `start` crea un proceso completamente independiente (_detached_), lo que impide al proceso padre capturar `stdout`/`stderr` o controlar su ciclo de vida.

La respuesta correcta es: El nuevo proceso se ejecuta de forma desvinculada (_detached_), por lo que Java no podrá leer su salida ni lo cerrará al terminar el programa padre.

#### Pregunta 16

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En un literal de cadena en Java, ¿cómo se deben escribir las rutas de archivos para Windows si no se utiliza la constante `File.separator`?

Pregunta 16Respuesta

a.

Anteponiendo el carácter `$` a la ruta completa.

b.

Escribiendo la barra invertida dos veces (`\\`) para escapar el carácter de escape de Java.

c.

Reemplazando las barras invertidas por signos de porcentaje (`%`).

d.

Encerrando la cadena entre comillas simples adicionales.

#### Retroalimentación

Respuesta incorrecta.

En las cadenas literales de Java, el carácter `\` actúa como escape, por lo que es necesario escribir `\\` para representar una barra invertida literal en una ruta de Windows.

La respuesta correcta es: Escribiendo la barra invertida dos veces (`\\`) para escapar el carácter de escape de Java.

#### Pregunta 17

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para personalizar o añadir variables de entorno a un subproceso antes de iniciarlo con `ProcessBuilder`, se utiliza el método `Respuesta Pregunta 17()`, el cual devuelve un `Map<String, String>` modificable.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Término en inglés traducido como 'entorno' que nombra al método de configuración de variables en `ProcessBuilder`.

La respuesta correcta es: environment

#### Pregunta 18

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En sistemas Linux o macOS, ¿cuál de las siguientes ejecuciones requiere obligatoriamente invocar un shell (como `sh -c`) en lugar de llamar directamente al ejecutable?

Pregunta 18Respuesta

a.

El lanzamiento de cualquier script ejecutable `.sh` que contenga un _shebang_ válido y permisos de ejecución.

b.

La ejecución de un archivo JAR utilizando la orden binaria `java -jar app.jar`.

c.

La invocación del comando `ls -la /home/user` pasando sus argumentos como elementos del array.

d.

Una orden que incluye tuberías (`|`), redirecciones (`>`) o comandos internos del shell como `cd`.

#### Retroalimentación

Respuesta incorrecta.

Las tuberías, redirecciones y comandos propios de la sintaxis del shell requieren la interpretación de un intérprete de comandos mediante la opción `-c`.

La respuesta correcta es: Una orden que incluye tuberías (`|`), redirecciones (`>`) o comandos internos del shell como `cd`.

#### Pregunta 19

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué excepción se lanza al invocar `processBuilder.start()` si la orden o programa ejecutable especificado no existe o no se encuentra en la ruta?

Pregunta 19Respuesta

a.

Una excepción de tipo `java.lang.ClassNotFoundException`.

b.

Una excepción de tipo `java.lang.IllegalArgumentException`.

c.

Una excepción de tipo `java.lang.NullPointerException`.

d.

An excepción de tipo `java.io.IOException`.

#### Retroalimentación

Respuesta incorrecta.

El fallo del sistema al intentar localizar u obtener acceso al archivo ejecutable durante la creación del proceso se clasifica y notifica como un error de Entrada/Salida (`IOException`).

La respuesta correcta es: An excepción de tipo `java.io.IOException`.

#### Pregunta 20

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para abrir una página o sitio web en el navegador predeterminado mediante la clase `Desktop`, se debe invocar el método `browse()` pasando un objeto de tipo `Respuesta Pregunta 20`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Siglas de tres letras en mayúsculas que identifican a un Identificador Uniforme de Recursos.

La respuesta correcta es: URI

#### Pregunta 21

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el canal predeterminado de salida de diagnóstico de la clase `Desktop` en caso de fallo durante el lanzamiento de una acción?

Pregunta 21Respuesta

a.

Captura silenciosamente las excepciones del sistema y las canaliza hacia la salida estándar `System.out`.

b.

Escribe los registros de error en un archivo temporal de registro ubicado en `user.dir`.

c.

Redirige automáticamente todos sus mensajes de error al flujo `System.err` del proceso Java.

d.

`Desktop` no gestiona flujos de entrada/salida de subprocesos, sino que reporta los errores lanzando excepciones comprobadas como `IOException` o `URISyntaxException`.

#### Retroalimentación

Respuesta incorrecta.

A diferencia de `ProcessBuilder`, `Desktop` interactúa con el escritorio del SO y no canaliza flujos de E/S, sino que notifica los errores directamente mediante excepciones comprobadas de Java.

La respuesta correcta es: `Desktop` no gestiona flujos de entrada/salida de subprocesos, sino que reporta los errores lanzando excepciones comprobadas como `IOException` o `URISyntaxException`.

#### Pregunta 22

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para consultar todas las variables de entorno del sistema desde Java de manera global, se utiliza el método `System.getenv()`, el cual retorna un objeto de tipo `Map<String, String>` que es de Respuesta Pregunta 22 .

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Reflexiona sobre la restricción de modificación que posee el mapa global devuelto por el sistema operativo.

La respuesta correcta es: solo lectura

#### Pregunta 23

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para comprobar de forma robusta si el programa se está ejecutando en un sistema operativo Windows mediante propiedades del sistema, ¿cuál es el procedimiento recomendado?

Pregunta 23Respuesta

a.

Leer `System.getenv("OS")` y comprobar si la cadena es exactamente igual a `"Windows_NT"`.

b.

Verificar únicamente si el separador de archivos `File.separator` es equivalente al carácter `/`.

c.

Obtener `System.getProperty("os.name")`, pasar la cadena a minúsculas y verificar si contiene `"win"`.

d.

Consultar `System.getProperty("os.version")` y comprobar si devuelve un número superior o igual a 10.

#### Retroalimentación

Respuesta incorrecta.

Puesto que `os.name` puede devolver valores como "Windows 11" o "Windows 10", convertir a minúsculas y buscar la subcadena "win" es el método portable estándar.

La respuesta correcta es: Obtener `System.getProperty("os.name")`, pasar la cadena a minúsculas y verificar si contiene `"win"`.

#### Pregunta 24

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué diferencia principal existe entre el uso de la clase `java.awt.Desktop` y la clase `ProcessBuilder` para abrir una aplicación o archivo?

Pregunta 24Respuesta

a.

`Desktop` permite ejecutar comandos de consola con tuberías y redirecciones, mientras que `ProcessBuilder` no puede gestionarlos.

b.

`ProcessBuilder` no puede lanzar archivos ejecutables `.exe`, requiriendo obligatoriamente el uso de `Desktop.getDesktop().open()`.

c.

`ProcessBuilder` solo funciona en entornos con interfaz gráfica, mientras que `Desktop` está diseñado para servidores en modo consola (_headless_).

d.

`Desktop` delega la acción a la aplicación predeterminada del sistema operativo sin ofrecer un objeto `Process` para controlar el subproceso.

#### Retroalimentación

Respuesta incorrecta.

A diferencia de `ProcessBuilder`, la clase `Desktop` no devuelve una instancia de `Process`, impidiendo la lectura directa de la salida o el control explícito sobre el proceso abierto.

La respuesta correcta es: `Desktop` delega la acción a la aplicación predeterminada del sistema operativo sin ofrecer un objeto `Process` para controlar el subproceso.

#### Pregunta 25

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se distinguen conceptualmente una **Variable de Entorno** y una **Propiedad del Sistema** en Java?

Pregunta 25Respuesta

a.

Las propiedades del sistema se leen con `System.getenv()`, mientras que las variables de entorno se leen con `System.getProperty()`.

b.

La variable de entorno tiene ámbito global al Sistema Operativo, mientras que la propiedad del sistema es local a una instancia de la JVM.

c.

La variable de entorno se define en la línea de comandos con `-D`, mientras que la propiedad del sistema se define en el SO.

d.

Las variables de entorno son específicas del proceso Java, mientras que las propiedades del sistema son compartidas por todas las aplicaciones de la máquina.

#### Retroalimentación

Respuesta incorrecta.

Las variables de entorno se definen fuera de Java a nivel de SO y son accesibles por cualquier proceso, mientras que las propiedades del sistema son locales a la máquina virtual concreta que las ejecuta.

La respuesta correcta es: La variable de entorno tiene ámbito global al Sistema Operativo, mientras que la propiedad del sistema es local a una instancia de la JVM.

#### Pregunta 26

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para acceder al separador de directorios específico del sistema operativo subyacente mediante la consulta de propiedades de la JVM, se utiliza la clave de propiedad `Respuesta Pregunta 26`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Identifica el nombre de la propiedad en inglés que une las palabras 'file' y 'separator' mediante un punto.

La respuesta correcta es: file.separator

#### Pregunta 27

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para conocer la ruta del ejecutable `java` de la máquina virtual que está ejecutando el programa principal, se puede consultar la propiedad del sistema denominada `Respuesta Pregunta 27`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Clave de propiedad del sistema enviada a `System.getProperty` que combina 'java' y 'home' mediante un punto.

La respuesta correcta es: java.home

#### Pregunta 28

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al ejecutar un comando en Windows con `cmd.exe`, se debe incluir el argumento `Respuesta Pregunta 28` para indicarle al intérprete de comandos que ejecute la orden especificada y luego se cierre automáticamente.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es una bandera compuesta por una barra diagonal y una única letra minúscula.

La respuesta correcta es: /c

#### Pregunta 29

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En los sistemas basados en UNIX (Linux o macOS), si se desea ejecutar un comando que incluye una tubería (`|`) o redirección de salida (`>`), se debe invocar al shell utilizando el parámetro `Respuesta Pregunta 29` seguido de la orden.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Consiste en un guion precediendo a una única letra que le indica al shell que interprete la cadena adjunta.

La respuesta correcta es: -c

#### Pregunta 30

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para ejecutar una clase Java como subproceso utilizando `ProcessBuilder` de forma portable sin escribir rutas fijas (_hardcodeadas_), ¿qué propiedades del sistema se deben consultar para obtener el ejecutable `java` y el _classpath_?

Pregunta 30Respuesta

a.

`java.version` para localizar el binario de ejecución y `user.home` para determinar la ruta del _classpath_.

b.

`file.separator` para el ejecutable y `line.separator` para la cadena del _classpath_.

c.

`java.home` para construir la ruta al ejecutable `java` y `java.class.path` para obtener el _classpath_.

d.

`user.dir` para ubicar el ejecutable `java` y `os.name` para reconstruir el _classpath_.

#### Retroalimentación

Respuesta incorrecta.

`java.home` devuelve la ubicación del entorno de ejecución activo para localizar `bin/java`, mientras que `java.class.path` proporciona las rutas de clases compiladas y librerías del proceso actual.

La respuesta correcta es: `java.home` para construir la ruta al ejecutable `java` y `java.class.path` para obtener el _classpath_.

#### Pregunta 31

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El comando interno de Windows `Respuesta Pregunta 31` permite ejecutar un programa o proceso de forma totalmente desvinculada (detached) de la aplicación Java principal, impidiendo leer su salida estándar o controlar su finalización.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Es el comando de `cmd.exe` cuyo significado en español es 'iniciar' o 'comenzar'.

La respuesta correcta es: start

#### Pregunta 32

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué ocurre si se llama al método `start()` de un mismo objeto `ProcessBuilder` en múltiples ocasiones?

Pregunta 32Respuesta

a.

Se crea un nuevo proceso independiente en cada llamada a `start()`, todos ellos compartiendo los mismos atributos de configuración.

b.

Las llamadas posteriores son ignoradas y devuelven la referencia al primer objeto `Process` creado.

c.

Se lanza una excepción `IllegalThreadStateException` porque `ProcessBuilder` es de un solo uso.

d.

El subproceso anterior se detiene forzosamente antes de iniciar la nueva ejecución.

#### Retroalimentación

Respuesta incorrecta.

A diferencia de la clase `Process`, el objeto `ProcessBuilder` es reusable y cada llamada a `start()` inicia un nuevo subproceso con los parámetros configurados.

La respuesta correcta es: Se crea un nuevo proceso independiente en cada llamada a `start()`, todos ellos compartiendo los mismos atributos de configuración.

#### Pregunta 33

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cada elemento o token pasado como parámetro al constructor de `ProcessBuilder` representa un argumento de la orden y no debe contener ningún Respuesta Pregunta 33 en blanco.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Indica el tipo de carácter delimitador invisible que debe separarse en tokens distintos al construir la orden.

La respuesta correcta es: espacio

#### Pregunta 34

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el comportamiento de `System.exit(int status)` respecto a la clase `Runtime`?

Pregunta 34Respuesta

a.

Internamente invoca de forma directa a `Runtime.getRuntime().exit(status)`.

b.

Crea un hilo en segundo plano que espera a que todos los subprocesos finalicen antes de llamar a `Runtime`.

c.

Lanza una excepción de tipo `SecurityException` si el parámetro `status` es distinto de cero.

d.

Invalida la instancia _singleton_ de `Runtime` obligando a su recreación antes de detener el proceso.

#### Retroalimentación

Respuesta incorrecta.

`System.exit()` actúa como una fachada estática que llama internamente al método `exit()` de la instancia _singleton_ de `Runtime`.

La respuesta correcta es: Internamente invoca de forma directa a `Runtime.getRuntime().exit(status)`.

#### Pregunta 35

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Respecto a la creación de procesos con la clase `Runtime`, ¿qué afirmación sobre el método `exec(String command)` es correcta según la documentación de Java?

Pregunta 35Respuesta

a.

Fue eliminado por completo en Java 17 y sustituido obligatoriamente por la clase `Desktop`.

b.

Permite modificar el directorio de trabajo del subproceso directamente a través de un único argumento de cadena.

c.

Está marcado como obsoleto (_deprecated_) desde la versión 18 de Java, recomendándose el uso de `exec(String[])` o `ProcessBuilder`.

d.

Analiza automáticamente los espacios en blanco dentro de cadenas entrecomilladas sin riesgo de error sintáctico.

#### Retroalimentación

Respuesta incorrecta.

El método `exec(String)` fue marcado como obsoleto debido a sus deficiencias en el manejo y tokenización de argumentos con espacios.

La respuesta correcta es: Está marcado como obsoleto (_deprecated_) desde la versión 18 de Java, recomendándose el uso de `exec(String[])` o `ProcessBuilder`.

#### Pregunta 36

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para recomendar la portabilidad de rutas en código Java al escribir literales en Windows sin depender del carácter de escape, se utiliza la constante estática `File.Respuesta Pregunta 36`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Nombre del atributo estático de la clase `File` que representa el separador de directorios.

La respuesta correcta es: separator