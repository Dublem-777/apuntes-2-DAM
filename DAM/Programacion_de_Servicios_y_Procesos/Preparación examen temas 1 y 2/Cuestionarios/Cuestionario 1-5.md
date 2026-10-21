# Cuestionario del apartado 1-5

##### Estado

Finalizado

##### Comenzado

domingo, 11 de octubre de 2026, 19:35

##### Completado

domingo, 11 de octubre de 2026, 19:39

##### Duración

4 minutos 7 segundos

##### Puntos

19,00/19,00

##### Calificación

**10,00** de 10,00 (**100**%)

#### Pregunta 1

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué metáfora geométrica describe mejor la diferencia entre la ejecución secuencial y la concurrente según los fundamentos teóricos?

Pregunta 1Seleccione una:

a.

La ejecución secuencial es un árbol ramificado; la concurrente un bucle circular cerrado.

b.

La ejecución secuencial carece de dirección; la concurrente sigue una trayectoria elíptica estricta.

c.

Ambas se representan siempre mediante una única recta continua sin ninguna bifurcación.

d.

La ejecución secuencial es una línea recta única; la concurrente son múltiples caminos que se entrelazan de forma impredecible.

¡Correcto!

#### Retroalimentación

El orden total se asemeja a una línea recta única; el orden parcial a múltiples caminos que avanzan y se entrelazan de forma variable e impredecible.

La respuesta correcta es: La ejecución secuencial es una línea recta única; la concurrente son múltiples caminos que se entrelazan de forma impredecible.

#### Pregunta 2

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si múltiples hilos acceden a una misma variable compartida de forma simultánea y sin ningún mecanismo de sincronización, pero **todos ellos realizan exclusivamente operaciones de lectura**, ¿se produce una carrera de datos?

Pregunta 2Seleccione una:

a.

Sí, la falta de sincronización siempre desencadena una carrera de datos sin importar la operación.

b.

Solo si hay más de 4 hilos concurrentes involucrados.

c.

No, porque es requisito indispensable que al menos uno de los accesos sea de modificación/escritura.

¡Correcto!

d.

Sí, porque los registros de la CPU pueden desbordarse al leer a la vez.

#### Retroalimentación

No, porque para que exista data race es imprescindible que al menos uno de los accesos concurrentes sea de escritura.

La respuesta correcta es: No, porque es requisito indispensable que al menos uno de los accesos sea de modificación/escritura.

#### Pregunta 3

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En la analogía del "gestor y los trabajadores", ¿qué elemento del sistema representa al gestor que decide en cada momento a quién le toca trabajar?

Pregunta 3Seleccione una:

a.

El planificador del sistema operativo (_scheduler_).

¡Correcto!

b.

El compilador de C o Java durante la fase de optimización.

c.

El recolector de basura (_garbage collector_).

d.

El bus de control de la placa base.

#### Retroalimentación

El planificador (scheduler) del sistema operativo es el encargado de asignar la CPU a los diferentes hilos o procesos en ejecución.

La respuesta correcta es: El planificador del sistema operativo (_scheduler_).

#### Pregunta 4

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Se dice que un programa concurrente presenta **comportamiento errático** cuando:

Pregunta 4Seleccione una:

a.

Termina inmediatamente la ejecución al intentar abrir un fichero inexistente.

b.

Ante las mismas entradas, arroja resultados correctos en unas ejecuciones y resultados erróneos o fallos en otras.

¡Correcto!

c.

Produce siempre exactamente la misma salida incorrecta en todas las ejecuciones sin variación.

d.

Genera errores de sintaxis en tiempo de compilación cada vez que se modifica el código fuente.

#### Retroalimentación

Un comportamiento errático implica que ante los mismos datos de entrada, el programa produce resultados correctos en algunas ocasiones y erróneos o fallos en otras debido al entrelazado de hilos.

La respuesta correcta es: Ante las mismas entradas, arroja resultados correctos en unas ejecuciones y resultados erróneos o fallos en otras.

#### Pregunta 5

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué propiedad garantiza el uso de un mecanismo de **exclusión mutua** (_mutex_) sobre una región crítica que accede a una variable compartida?

Pregunta 5Seleccione una:

a.

Que ningún hilo pueda volver a leer la variable una vez que haya sido modificada.

b.

Que el programa se ejecute el doble de rápido al repartir las escrituras en varios hilos a la vez.

c.

Que todas las variables del programa pasen a ubicarse en el almacenamiento secundario.

d.

Que únicamente un hilo a la vez pueda acceder a la sección crítica y manipular el dato compartido.

¡Correcto!

#### Retroalimentación

Garantiza que en un instante de tiempo dado, solo un hilo puede encontrarse ejecutando la región crítica protegida, evitando que coincidan escrituras no controladas.

La respuesta correcta es: Que únicamente un hilo a la vez pueda acceder a la sección crítica y manipular el dato compartido.

#### Pregunta 6

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué característica define al concepto de **orden total** en la ejecución de un programa?

Pregunta 6Respuesta

a.

Es un orden en el que intervienen mecanismos de exclusión mutua para forzar la sincronización.

b.

Las instrucciones se ejecutan siguiendo una secuencia única, predecible y completamente determinada por el código y sus entradas.

¡Correcto!

c.

El orden dentro de cada hilo es conocido, pero no la intercalación entre diferentes hilos concurrentes.

d.

El planificador del sistema operativo asigna dinámicamente el orden exacto según la carga de la CPU.

#### Retroalimentación

En un programa secuencial el orden de ejecución es total y determinista: las instrucciones siguen un camino único y predecible predeterminado por el código y las entradas.

La respuesta correcta es: Las instrucciones se ejecutan siguiendo una secuencia única, predecible y completamente determinada por el código y sus entradas.

#### Pregunta 7

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la relación conceptual entre una **condición de carrera** (_race condition_) y una **carrera de datos** (_data race_)?

Pregunta 7Seleccione una:

a.

La carrera de datos es un caso específico de condición de carrera, circunscrito concretamente al acceso concurrente no sincronizado y escritura en memoria compartida.

¡Correcto!

b.

La condición de carrera solo afecta a variables locales, y la carrera de datos a sockets de red.

c.

Son conceptos sinónimos e idénticos en todos los niveles de abstracción del software.

d.

La carrera de datos ocurre solo en programas secuenciales, mientras que la condición de carrera en distribuidos.

#### Retroalimentación

Una data race es un caso específico y concreto de race condition centrado en accesos concurrentes no sincronizados a variables compartidas en memoria donde al menos uno escribe.

La respuesta correcta es: La carrera de datos es un caso específico de condición de carrera, circunscrito concretamente al acceso concurrente no sincronizado y escritura en memoria compartida.

#### Pregunta 8

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Puede ocurrir una condición de carrera en un programa estrictamente **secuencial** mono-hilo sin interrupciones asíncronas?

Pregunta 8Seleccione una:

a.

Sí, debido a que la memoria RAM siempre tiene fluctuaciones en el voltaje.

b.

Sí, si el programa contiene bucles anidados con más de tres variables enteras.

c.

No, porque las instrucciones siguen un orden total totalmente determinado por el código y los datos de entrada.

¡Correcto!

d.

Solo si se utilizan punteros a funciones en lugar de llamadas directas.

#### Retroalimentación

No, porque en un programa secuencial rige el orden total: el camino de ejecución es único, estrictamente determinista y no existe intercalación de flujos de control concurrentes.

La respuesta correcta es: No, porque las instrucciones siguen un orden total totalmente determinado por el código y los datos de entrada.

#### Pregunta 9

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para que un programa concurrente sea robusto frente al orden parcial de ejecución, ¿en qué principio debe basarse su diseño?

Pregunta 9Seleccione una:

a.

En asumir que el sistema operativo siempre otorgará el mismo intervalo de tiempo (*quantum*) a cada hilo de forma fija.

b.

En introducir pausas artificiales fijas (como `sleep`) para intentar predecir cuál terminará antes.

c.

En ejecutar todos los hilos siempre en modo núcleo deshabilitando las interrupciones externas.

d.

En garantizar la corrección del resultado con independencia del orden o velocidad de intercalación con que el procesador ejecute los hilos.

¡Correcto!

#### Retroalimentación

Debe ser robusto e independiente del timing o secuencia de intercalación concreta que determine el planificador en cada ejecución.

La respuesta correcta es: En garantizar la corrección del resultado con independencia del orden o velocidad de intercalación con que el procesador ejecute los hilos.

#### Pregunta 10

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Dentro de los límites de un **hilo individual** en un sistema concurrente, ¿cómo se ejecutan sus propias instrucciones?

Pregunta 10Seleccione una:

a.

En orden parcial dentro de su propia pila de llamadas locales.

b.

De forma caótica, alterando el orden interno de las sentencias del programador al azar.

c.

De forma secuencial, manteniendo su orden interno de ejecución.

¡Correcto!

d.

En orden inverso a como fueron declaradas en la función principal.

#### Retroalimentación

Dentro de cada hilo individual se mantiene una ejecución secuencial de sus instrucciones; lo que es impredecible es cómo se intercala con otros hilos.

La respuesta correcta es: De forma secuencial, manteniendo su orden interno de ejecución.

#### Pregunta 11

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué se entiende por **orden parcial** en programación concurrente?

Pregunta 11Seleccione una:

a.

Las instrucciones dentro de cada hilo se ejecutan en orden aleatorio según las interrupciones hardware.

b.

Solo se ejecutan una parte de los hilos creados debido a limitaciones de memoria.

c.

El programador fija estáticamente en tiempo de compilación el entrelazado de los hilos.

d.

Se conoce el orden de ejecución dentro de cada proceso o hilo, pero no el orden en el que se intercalan entre sí.

¡Correcto!

#### Retroalimentación

Se conoce el orden secuencial de instrucciones dentro de cada hilo/proceso, pero la forma exacta en que se intercalan unos con otros no se puede predecir de antemano.

La respuesta correcta es: Se conoce el orden de ejecución dentro de cada proceso o hilo, pero no el orden en el que se intercalan entre sí.

#### Pregunta 12

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuáles son las **tres condiciones simultáneas** que deben cumplirse para que exista una **carrera de datos** (_data race_)?

Pregunta 12Seleccione una:

a.

Dos hilos ejecutan la misma función, ambos leen la misma variable y no usan semáforos.

b.

Un hilo escribe en una variable local, otro escribe en memoria secundaria y ambos usan exclusión mutua.

c.

Tres procesos compiten por el mismo descriptor de fichero en modo solo lectura de forma sincronizada.

d.

Dos o más hilos acceden a la misma variable compartida, al menos uno realiza una escritura y los accesos no están sincronizados.

¡Correcto!

#### Retroalimentación

1. Dos o más hilos acceden a la misma variable compartida. 2. Al menos un acceso es de escritura. 3. Los accesos no están debidamente sincronizados.

La respuesta correcta es: Dos o más hilos acceden a la misma variable compartida, al menos uno realiza una escritura y los accesos no están sincronizados.

#### Pregunta 13

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuándo se produce una **condición de carrera** (_race condition_)?

Pregunta 13Seleccione una:

a.

Cuando la corrección del programa depende críticamente de una secuencia o _timing_ de intercalación concreto de sus hilos.

¡Correcto!

b.

Cuando un hilo consume el 100% de la CPU impidiendo que los demás comiencen su ejecución.

c.

Cuando un proceso padre finaliza antes que sus hijos generando procesos zombies.

d.

Siempre que dos hilos acceden en modo solo lectura a una constante global.

#### Retroalimentación

Ocurre cuando la corrección del programa depende de que los hilos se ejecuten en una secuencia o timing de intercalación específico.

La respuesta correcta es: Cuando la corrección del programa depende críticamente de una secuencia o _timing_ de intercalación concreto de sus hilos.

#### Pregunta 14

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la finalidad principal de utilizar **mecanismos de sincronización** (como exclusión mutua o semáforos) en programación concurrente?

Pregunta 14Seleccione una:

a.

Eliminar por completo la necesidad de tener un planificador de procesos en el sistema operativo.

b.

Obligar a la CPU a ejecutar todos los hilos siempre a la velocidad máxima del reloj.

c.

Controlar y proteger el acceso a variables y recursos compartidos para garantizar la consistencia y corrección frente al entrelazado de hilos.

¡Correcto!

d.

Evitar que los programas concurrentes hagan uso de memoria RAM compartida.

#### Retroalimentación

Garantizan el acceso ordenado y exclusivo a recursos compartidos, evitando carreras de datos y asegurando la corrección del programa frente al orden parcial de ejecución.

La respuesta correcta es: Controlar y proteger el acceso a variables y recursos compartidos para garantizar la consistencia y corrección frente al entrelazado de hilos.

#### Pregunta 15

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿De cuáles de los siguientes factores depende la secuencia exacta en que se intercalan los hilos concurrentes?

Pregunta 15Seleccione una:

a.

De la velocidad fija del bus de datos, siendo idéntica en cada ejecución con los mismos datos.

b.

Únicamente del compilador al generar el código binario durante el enlazado.

c.

De decisiones del planificador del sistema operativo, la carga del sistema, interrupciones y eventos asíncronos.

¡Correcto!

d.

Exclusivamente del orden en que el código fuente declara las variables compartidas.

#### Retroalimentación

Depende de factores externos al código como las decisiones del planificador del sistema operativo, la carga del sistema, interrupciones hardware y eventos asíncronos.

La respuesta correcta es: De decisiones del planificador del sistema operativo, la carga del sistema, interrupciones y eventos asíncronos.

#### Pregunta 16

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál de las siguientes **NO** es una consecuencia típica provocada por condiciones de carrera?

Pregunta 16Seleccione una:

a.

Comportamiento errático e impredecible en distintas ejecuciones con idénticos datos de entrada.

b.

Corrupción de memoria o resultados inconsistentes e incorrectos.

c.

Aparición de vulnerabilidades de seguridad susceptibles de ser explotadas por atacantes.

d.

Optimización determinista en el tiempo de procesamiento de cada instrucción.

¡Correcto! Esta no es una consecuencia, es un enunciado falso.

#### Retroalimentación

Las condiciones de carrera no aceleran de forma determinista la ejecución de los algoritmos; al contrario, provocan corrupción de datos, fallos intermitentes y agujeros de seguridad.

La respuesta correcta es: Optimización determinista en el tiempo de procesamiento de cada instrucción.

#### Pregunta 17

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Por qué las condiciones de carrera son consideradas uno de los errores más difíciles de depurar en el software?

Pregunta 17Seleccione una:

a.

Porque pueden presentarse de forma esporádica e intermitente bajo cargas específicas, haciendo difícil reproducir el error.

¡Correcto!

b.

Porque las condiciones de carrera solo se manifiestan en sistemas con un único núcleo de procesador.

c.

Porque siempre provocan un cuelgue inmediato del núcleo del sistema operativo en el primer milisegundo.

d.

Porque el compilador impide generar el ejecutable si detecta hilos en el código.

#### Retroalimentación

Porque son intermitentes: pueden manifestarse solo de manera esporádica o bajo ciertas condiciones de carga, pasando inadvertidas en pruebas normales.

La respuesta correcta es: Porque pueden presentarse de forma esporádica e intermitente bajo cargas específicas, haciendo difícil reproducir el error.

#### Pregunta 18

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Dos hilos incrementan en 1 una variable global compartida `cuenta = 0` mediante la instrucción `cuenta++` sin sincronización. ¿Por qué el valor final puede ser 1 en lugar de 2?

Pregunta 18Seleccione una:

a.

Porque los operadores de incremento unitario están prohibidos por el estándar en programas concurrentes.

b.

Porque la memoria RAM borra automáticamente las variables cuando dos hilos intentan acceder al mismo ciclo de reloj.

c.

Porque la operación consta de lectura, modificación y escritura; si sus secuencias se intercalan, ambos hilos pueden leer el valor original y sobreescribirse mutuamente.

¡Correcto!

d.

Porque el planificador cancela de inmediato uno de los hilos si detecta operaciones aritméticas.

#### Retroalimentación

La operación cuenta++ se descompone en leer, modificar y escribir. Si ambos hilos leen el valor 0 antes de que el otro escriba, ambos calcularán 1 y sobreescribirán el resultado, perdiéndose un incremento (carrera de datos).

La respuesta correcta es: Porque la operación consta de lectura, modificación y escritura; si sus secuencias se intercalan, ambos hilos pueden leer el valor original y sobreescribirse mutuamente.

#### Pregunta 19

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿El comportamiento indeterminista (posibles diferentes secuencias de ejecución ante las mismas entradas) implica necesariamente que un programa concurrente sea incorrecto?

Pregunta 19Seleccione una:

a.

Sí, porque el estándar POSIX exige determinismo estricto en el resultado y en el tiempo de ejecución.

b.

Sí, por definición cualquier programa que no presente orden total se considera defectuoso.

c.

No, que existan diferentes caminos de ejecución no significa por sí solo que el programa sea incorrecto, siempre que todos conduzcan a un resultado válido.

¡Correcto!

d.

No, siempre y cuando el sistema operativo desactive la multitarea apropiativa.

#### Retroalimentación

No necesariamente. Un programa concurrente puede tener múltiples caminos de entrelazado y seguir siendo correcto si todos ellos producen resultados válidos y consistentes.

La respuesta correcta es: No, que existan diferentes caminos de ejecución no significa por sí solo que el programa sea incorrecto, siempre que todos conduzcan a un resultado válido.