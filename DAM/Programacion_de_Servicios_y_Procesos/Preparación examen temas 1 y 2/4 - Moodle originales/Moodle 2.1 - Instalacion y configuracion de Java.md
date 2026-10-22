# Cuestionario del apartado 2-1

##### Estado

Finalizado

##### Comenzado

miércoles, 14 de octubre de 2026, 18:48

##### Completado

miércoles, 21 de octubre de 2026, 17:47

##### Duración

6 días 22 horas

##### Puntos

-1,00/12,00

##### Calificación

**-0,83** de 10,00 (**-8,33**%)

#### Pregunta 1

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Dado el siguiente código fuente ejecutado mediante el comando `java MyProgram Baldomero cincuenta`:

`   public class MyProgram {     public static void main(String[] args) {       if (args.length == 2) {         try {           String name = args[0];           int age = Integer.parseInt(args[1]);           System.out.println("Hi " + name + ", you're " + age + " years old.");         } catch (NumberFormatException e) {           System.out.println("Second argument must be an integer.");         }       } else {         System.out.println("Program needs 2 arguments: a name and an age.");       }     }   }`

¿Cuál será la salida impresa en la consola?

Pregunta 1Respuesta

a.

Hi Baldomero, you're cincuenta years old.

b.

Program needs 2 arguments: a name and an age.

c.

Second argument must be an integer.

d.

Se interrumpe la ejecución abruptamente mostrando la traza de la excepción `ArrayIndexOutOfBoundsException`.

#### Retroalimentación

Respuesta incorrecta.

El valor 'cincuenta' se recibe en `args[1]` como String, y al intentar convertirlo con `Integer.parseInt` se produce un `NumberFormatException`, ejecutando el bloque catch correspondiente.

La respuesta correcta es: Second argument must be an integer.

#### Pregunta 2

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La funcionalidad introducida en Java 11 denominada ejecución de archivo único (_single-file execution_) permite ejecutar un fichero fuente directamente con el comando `java` realizando la compilación en `Respuesta Pregunta 2`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Indica el medio de almacenamiento volátil donde se realiza la compilación sin escribir archivos en disco.

La respuesta correcta es: memoria

#### Pregunta 3

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando se ejecuta una cadena de órdenes en un pipeline como `java Programa1 | java Programa2`, por defecto en Bash el código de salida devuelto al finalizar la tubería corresponde al código de salida del Respuesta Pregunta 3 comando.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Considera cuál de los programas en la cadena de comandos determina el resultado final reportado al interprete.

La respuesta correcta es: último

#### Pregunta 4

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para concatenar la salida de un programa al contenido existente de un archivo de texto sin sobrescribirlo desde la línea de comandos, se utiliza el operador de redirección `Respuesta Pregunta 4`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Diferencia el operador que sobrescribe un archivo del que añade texto al final de este.

La respuesta correcta es: >>

#### Pregunta 5

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En sistemas operativos Windows y UNIX, para redirigir la entrada estándar `System.in` de un programa Java para que lea los datos desde un archivo en lugar del teclado, se utiliza el operador `Respuesta Pregunta 5`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Identifica el símbolo matemático de desigualdad utilizado para apuntar un archivo hacia la entrada del programa.

La respuesta correcta es: <

#### Pregunta 6

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para permitir la ejecución global de los comandos de desarrollo de Java (`javac`, `java`, `jar`) desde cualquier directorio en la terminal, se debe añadir la ruta del directorio binario del JDK a la variable de entorno `Respuesta Pregunta 6`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Nombra la variable de entorno global del sistema operativo utilizada para la localización de ejecutables.

La respuesta correcta es: PATH

#### Pregunta 7

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Durante la preparación manual del archivo `META-INF/MANIFEST.MF` para crear un JAR ejecutable con la orden `jar cfm`, un desarrollador olvida incluir un salto de línea al final de la línea `Main-Class: MiClasePrincipal`. ¿Qué consecuencia tiene esto al intentar ejecutar el archivo mediante `java -jar app.jar`?

Pregunta 7Respuesta

a.

La JVM no interpretará correctamente la directiva del manifiesto y fallará al intentar localizar la clase principal.

b.

El programa se ejecutará correctamente, pero cualquier argumento pasado por línea de comandos será ignorado silenciosamente.

c.

La JVM añade automáticamente el salto de línea que falta durante la lectura del manifiesto en memoria.

d.

La herramienta `jar` mostrará un error de sintaxis durante el empaquetado y abortará la creación del archivo.

#### Retroalimentación

Respuesta incorrecta.

La especificación del manifiesto de Java requiere estrictamente un salto de línea al final de cada línea para que la JVM pueda procesar y reconocer correctamente cabeceras como `Main-Class`.

La respuesta correcta es: La JVM no interpretará correctamente la directiva del manifiesto y fallará al intentar localizar la clase principal.

#### Pregunta 8

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Se requiere ejecutar dos programas en una tubería (`java Programa1 | java Programa2`), pero se necesita que las salidas de error de ambos programas se guarden en archivos independientes (`error1.log` y `error2.log`) sin interrumpir el flujo entre ellos. ¿Cuál es la sintaxis correcta en la línea de comandos?

Pregunta 8Respuesta

a.

`java Programa1 2>&1 | java Programa2 > error1.log > error2.log`

b.

`java -err error1.log Programa1 | java -err error2.log Programa2`

c.

`java Programa1 2> error1.log | java Programa2 2> error2.log`

d.

`java Programa1 | java Programa2 2> error1.log 2> error2.log`

#### Retroalimentación

Respuesta incorrecta.

Esta sintaxis redirige individualmente la salida de error (`2>`) de cada proceso a su respectivo archivo de log, manteniendo la tubería (`|`) enfocada en conectar los flujos de salida estándar.

La respuesta correcta es: `java Programa1 2> error1.log | java Programa2 2> error2.log`

#### Pregunta 9

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En un programa Java, los argumentos pasados por línea de comandos al invocar `java MiPrograma arg1 arg2` se reciben en el método `main` como un arreglo de cadenas, donde la cadena correspondiente a `arg1` se almacena en el índice `Respuesta Pregunta 9`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Indica la primera posición del arreglo `args` recibida en el método `main`.

La respuesta correcta es: 0

#### Pregunta 10

Sin contestar

Se puntúa como 0 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En sistemas UNIX y Windows, la redirección de la salida de error estándar a un archivo de texto reemplazando su contenido previo se realiza mediante el operador `Respuesta Pregunta 10`.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Piensa en el número de descriptor de archivo asignado a la salida de error estándar junto con el operador de sobrescritura.

La respuesta correcta es: 2>

#### Pregunta 11

Incorrecta

Se puntúa -0,50 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Se ejecuta el comando `java Programa1 | java Programa2` en una terminal de Bash. `Programa1` escribe mensajes de procesamiento regular en `System.out` y alertas de depuración en `System.err`. ¿Cómo gestiona la tubería (pipe) los flujos transmitidos por `Programa1`?

Pregunta 11Respuesta

a.

Ambos flujos `System.out` y `System.err` se combinan automáticamente y se envían a la entrada estándar de `Programa2`.

b.

`System.err` provoca la interrupción inmediata de la tubería antes de que `Programa2` pueda procesar cualquier dato de `System.out`.

c.

`System.err` se redirige automáticamente a un archivo temporal de registro gestionado por el sistema operativo.

d.

`System.out` se redirige a la entrada estándar (`System.in`) de `Programa2`, mientras que `System.err` no se canaliza y se imprime directamente en la consola.

#### Retroalimentación

Respuesta incorrecta.

Por diseño en los sistemas operativos, el pipe (`|`) únicamente canaliza la salida estándar (`stdout`), permitiendo que la salida de error (`stderr`) fluya a la consola para no contaminar los datos.

La respuesta correcta es: `System.out` se redirige a la entrada estándar (`System.in`) de `Programa2`, mientras que `System.err` no se canaliza y se imprime directamente en la consola.

#### Pregunta 12

Incorrecta

Se puntúa -0,50 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1792484846/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En la ejecución del pipeline `java Programa1 | java Programa2`, `Programa1` escribe datos en su salida estándar a una velocidad sustancialmente mayor de la que `Programa2` puede leerlos desde su entrada estándar. ¿Qué mecanismo aplica el sistema operativo para gestionar este desequilibrio?

Pregunta 12Respuesta

a.

`Programa2` almacena indefinidamente la salida excedente en la memoria de intercambio (SWAP) del sistema sin pausar a `Programa1`.

b.

`Programa1` descarta silenciosamente los nuevos datos emitidos por `System.out` hasta que `Programa2` reduzca su carga de procesamiento.

c.

`Programa1` se bloquea temporalmente cuando la tubería alcanza su capacidad máxima hasta que `Programa2` consuma datos y libere espacio.

d.

El sistema operativo aborta el proceso de `Programa1` generando una excepción de desbordamiento de búfer (_buffer overflow_).

#### Retroalimentación

Respuesta incorrecta.

El sistema operativo gestiona el búfer de la tubería; si el búfer se llena por una velocidad asimétrica de producción, el proceso emisor se bloquea temporalmente hasta que haya espacio disponible.

La respuesta correcta es: `Programa1` se bloquea temporalmente cuando la tubería alcanza su capacidad máxima hasta que `Programa2` consuma datos y libere espacio.