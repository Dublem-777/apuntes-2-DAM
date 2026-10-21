---
asignatura: PSyP
tema: 1
tipo: cuestionario
estado: completo
fecha: 2026-10-20
tags:
  - DAM/cuestionario
  - DAM/psyp/programacion-concurrente
  - DAM/psyp/sincronizacion
---

# Simulacro de examen · Tema 1 (50 preguntas)

> [!info] Alcance
> **50 preguntas** escogidas de los 8 [[Simulacros tipo test tema 1|simulacros por apartado]] para hacer un examen completo del Tema 1: repartidas según el peso de cada apartado (1.1: 8 · 1.2: 6 · 1.3: 7 · 1.4: 5 · 1.5: 6 · 1.6: 8 · 1.7: 4 · 1.8: 6), sin conceptos repetidos y con las 4 preguntas ⚠️ que fallaste en Moodle. El orden de las preguntas está mezclado y **las opciones están barajadas**, así que la letra no coincide con la de Moodle.

> [!tip] Cómo hacer el simulacro
> 1. Pon un cronómetro de **25 minutos** (unos 30 s por pregunta).
> 2. Apunta tus respuestas en un papel **sin abrir** ningún desplegable de **Respuesta**.
> 3. Corrige con la [[#Hoja de respuestas]] y abre solo las respuestas de las preguntas que hayas fallado.
> 4. Cada respuesta indica de qué simulacro sale la pregunta: repasa ese apartado si fallas varias del mismo.

> [!warning] Patrones detectados en los cuestionarios Moodle
> Análisis de las 128 preguntas con opciones de los 8 cuestionarios:
>
> | Patrón | Resultado | Por azar |
> | --- | --- | --- |
> | Letra de la respuesta correcta | a 33 · b 29 · c 32 · d 34, sin rachas → **no hay patrón** | — |
> | La correcta es la opción **más larga** | **86 de 128 (67 %)** | 25 % |
> | Palabras absolutas (*siempre, exclusivamente, obligatoriamente, únicamente, automáticamente…*) | en el **33 % de las incorrectas** y solo en el 6 % de las correctas | — |
> | La correcta repite palabras del enunciado | 95 de 128 (74 %) | ~25 % |
>
> **Estrategia de descarte:** quita las opciones absurdas y las que llevan palabras absolutas; si dudas entre dos, la más larga y matizada suele ser la buena. En este simulacro las letras están barajadas, pero el patrón de la opción más larga sigue ahí, porque el texto de las opciones no se ha cambiado.
>
> Ojo: el examen del año pasado ([[Examen año pasado]]) fue **práctico, del Tema 2**. Estos trucos solo sirven si el test sale del mismo banco de Moodle; no sustituyen a saberse la teoría.

> [!tip] Material de preparación
> - [[Guia examen temas 1 y 2|🧠 Teoría y chuleta]]
> - [[Test de repaso temas 1 y 2|✅ Test de repaso]]
> - [[Simulacros tipo test tema 1|⏱️ Simulacros por apartado]]
> - [[Simulacro examen tema 1 (50 preguntas)|📝 Simulacro de examen]]
> - [[Practicos temas 1 y 2|💻 Prácticos resueltos]]

## Preguntas (auto-test)

> [!question] P1 · `wait()`/`notify()` sin el cerrojo
> En Java, ¿qué ocurre si un hilo intenta invocar el método `wait()` o `notify()` sobre un objeto sin haber obtenido previamente su bloqueo mediante un bloque o método `synchronized`?
> - a. Se produce una excepción de tipo `IllegalMonitorStateException` en tiempo de ejecución.
> - b. El código no compila generando un error de tipado estático.
> - c. El hilo entra en un estado zombi no recuperable por el sistema operativo.
> - d. El objeto adquiere automáticamente el cerrojo de forma implícita sin advertencias.

> [!success]- Respuesta
>
> - a. ✅ Se produce una excepción de tipo `IllegalMonitorStateException` en tiempo de ejecución.
>
> *Por qué:* lanza **`IllegalMonitorStateException`** en **tiempo de ejecución**. Compila sin problemas, no coge el cerrojo implícitamente y no hay estados "zombi" de hilos. [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P13

> [!question] P2 · Concurrente vs. paralela
> ¿Cuál es la característica principal que distingue a la programación concurrente en general de la programación paralela?
> - a. Garantiza que todas las tareas se ejecuten exactamente al mismo instante de tiempo físico.
> - b. Únicamente se puede aplicar en sistemas monoprocesador sin memoria compartida.
> - c. Gestiona la ejecución entrelazada o simultánea de múltiples tareas para optimizar recursos o reparto de tiempo, sin requerir obligatoriamente múltiples núcleos.
> - d. Requiere obligatoriamente una red de ordenadores conectados para intercambiar mensajes.

> [!success]- Respuesta
>
> - c. ✅ Gestiona la ejecución entrelazada o simultánea de múltiples tareas para optimizar recursos o reparto de tiempo, sin requerir obligatoriamente múltiples núcleos.
>
> *Por qué:* la concurrente gestiona tareas **entrelazadas o simultáneas** para repartir recursos o tiempo, **sin exigir varios núcleos**. No se limita a monoprocesador, no exige red y no garantiza simultaneidad física. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 4 · 1.4 · Técnicas de programación concurrente|Simulacro 4]] · P13

> [!question] P3 · Tres condiciones de la data race
> ¿Cuáles son las **tres condiciones simultáneas** que deben cumplirse para que exista una **carrera de datos** (_data race_)?
> - a. Dos o más hilos acceden a la misma variable compartida, al menos uno realiza una escritura y los accesos no están sincronizados.
> - b. Un hilo escribe en una variable local, otro escribe en memoria secundaria y ambos usan exclusión mutua.
> - c. Tres procesos compiten por el mismo descriptor de fichero en modo solo lectura de forma sincronizada.
> - d. Dos hilos ejecutan la misma función, ambos leen la misma variable y no usan semáforos.

> [!success]- Respuesta
>
> - a. ✅ Dos o más hilos acceden a la misma variable compartida, al menos uno realiza una escritura y los accesos no están sincronizados.
>
> *Por qué:* **misma variable compartida + al menos una escritura + accesos sin sincronizar**. Las demás opciones fallan en alguna: solo lecturas, uso de exclusión mutua o acceso sincronizado. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 5 · 1.5 · Orden de ejecución|Simulacro 5]] · P12

> [!question] P4 · Procesos independientes sin sincronización
> En el contexto de interacciones entre procesos, ¿por qué los procesos independientes no requieren mecanismos explícitos de sincronización de usuario?
> - a. Porque los procesos independientes solo funcionan en ordenadores apagados.
> - b. Porque se ejecutan siempre a través del mismo hilo principal.
> - c. Porque el SO aísla sus espacios de memoria y recursos.
> - d. Porque la JVM prohíbe la multiprogramación en sistemas operativos modernos.

> [!success]- Respuesta
>
> - c. ✅ Porque el SO aísla sus espacios de memoria y recursos.
>
> *Por qué:* el **SO aísla su memoria y sus recursos**, así que no pueden corromperse los datos entre ellos. No usan el mismo hilo y la JVM no prohíbe la multiprogramación. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 4 · 1.4 · Técnicas de programación concurrente|Simulacro 4]] · P17

> [!question] P5 · Interacción de competencia
> ¿Cuándo se considera que dos o más procesos están en interacción de competencia?
> - a. Cuando se ejecutan en diferentes ordenadores conectados por un switch.
> - b. Cuando ambos procesos pertenecen a usuarios que no tienen permisos de administrador.
> - c. Cuando intentan acceder simultáneamente a un recurso no compartible.
> - d. Cuando uno lee los mensajes que el otro ha colocado en una cola intencionadamente.

> [!success]- Respuesta
>
> - c. ✅ Cuando intentan acceder simultáneamente a un recurso no compartible.
>
> *Por qué:* compiten cuando quieren acceder **a la vez a un recurso no compartible**. Estar en distintos ordenadores o sin permisos no tiene que ver, y leer mensajes de una cola es cooperación. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 4 · 1.4 · Técnicas de programación concurrente|Simulacro 4]] · P11

> [!question] P6 · SMP vs. distribuido
> ¿Cuál es la diferencia clave fundamental entre el **multiprocesamiento (SMP)** y el **procesamiento distribuido**?
> - a. La utilización exclusiva de sistemas operativos tipo Unix en arquitecturas SMP.
> - b. La existencia o no de una memoria principal común compartida por todos los procesadores.
> - c. Que los sistemas SMP no son capaces de ejecutar hilos de forma concurrente.
> - d. La presencia obligatoria de una red cableada de fibra óptica para que funcione el bus local.

> [!success]- Respuesta
>
> - b. ✅ La existencia o no de una memoria principal común compartida por todos los procesadores.
>
> *Por qué:* la diferencia clave es si hay **memoria principal común** (SMP) o si cada nodo tiene la suya (distribuido). Ambos ejecutan hilos y ninguno exige fibra óptica o Unix. [[1.2 - Computacion concurrente#4.2 Procesamiento distribuido|Ver 1.2 · Procesamiento distribuido]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 2 · 1.2 · Computación concurrente|Simulacro 2]] · P15

> [!question] P7 · Segmento de memoria dinámica
> ¿Qué segmento de la memoria de un proceso se utiliza para almacenar la memoria dinámica asignada durante el tiempo de ejecución?
> - a. Código (Texto).
> - b. Heap (Montón).
> - c. Pila (Stack).
> - d. Datos (Data).

> [!success]- Respuesta
>
> - b. ✅ Heap (Montón).
>
> *Por qué:* el **heap** guarda la memoria dinámica pedida en ejecución (`new`, `malloc`). El código guarda instrucciones; los datos, variables globales y estáticas; la pila, llamadas y variables locales. [[1.3 - Procesos en el sistema operativo#1.1 El cargador de procesos|Ver 1.3 · El cargador]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P3

> [!question] P8 · Comunicación síncrona bloqueante
> ¿Cómo afecta el carácter bloqueante de la comunicación síncrona al comportamiento y rendimiento de un programa concurrente?
> - a. Maximiza el paralelismo del sistema al permitir que el emisor ejecute instrucciones en segundo plano sin detener su flujo de control.
> - b. Aumenta la eficiencia de red al comprimir automáticamente los datos antes de enviarlos de forma asíncrona.
> - c. Garantiza la eliminación total de deadlocks al forzar la recepción inmediata de cualquier mensaje.
> - d. Reduce el paralelismo potencial y puede introducir bloqueos, ya que el emisor debe suspender su ejecución hasta que el receptor recibe y/o procesa el mensaje.

> [!success]- Respuesta
>
> - d. ✅ Reduce el paralelismo potencial y puede introducir bloqueos, ya que el emisor debe suspender su ejecución hasta que el receptor recibe y/o procesa el mensaje.
>
> *Por qué:* el emisor **se queda parado** hasta que el receptor recibe o procesa: **menos paralelismo y riesgo de bloqueos**. No maximiza el paralelismo (eso es la asíncrona), no elimina deadlocks ni comprime datos. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 7 · 1.7 · Comunicación entre procesos|Simulacro 7]] · P14

> [!question] P9 · `cuenta++` da 1 en vez de 2
> Dos hilos incrementan en 1 una variable global compartida `cuenta = 0` mediante la instrucción `cuenta++` sin sincronización. ¿Por qué el valor final puede ser 1 en lugar de 2?
> - a. Porque la operación consta de lectura, modificación y escritura; si sus secuencias se intercalan, ambos hilos pueden leer el valor original y sobreescribirse mutuamente.
> - b. Porque el planificador cancela de inmediato uno de los hilos si detecta operaciones aritméticas.
> - c. Porque los operadores de incremento unitario están prohibidos por el estándar en programas concurrentes.
> - d. Porque la memoria RAM borra automáticamente las variables cuando dos hilos intentan acceder al mismo ciclo de reloj.

> [!success]- Respuesta
>
> - a. ✅ Porque la operación consta de lectura, modificación y escritura; si sus secuencias se intercalan, ambos hilos pueden leer el valor original y sobreescribirse mutuamente.
>
> *Por qué:* `cuenta++` es **leer, sumar y escribir**; si los dos hilos leen 0 antes de que el otro escriba, ambos escriben 1 y se pierde un incremento. No está prohibido, la RAM no borra nada y el planificador no cancela hilos. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 5 · 1.5 · Orden de ejecución|Simulacro 5]] · P18

> [!question] P10 · Programa desde el punto de vista del SO
> Desde la perspectiva técnica de un sistema operativo, ¿qué representa exactamente un **programa**?
> - a. Una instancia activa con asignación dinámica de memoria y registros de CPU.
> - b. Un hilo de ejecución en segundo plano que carece de interfaz gráfica.
> - c. Un archivo de texto plano con código fuente editable por el usuario.
> - d. La representación estática en disco de una aplicación, que contiene código y datos asociados.

> [!success]- Respuesta
>
> - d. ✅ La representación estática en disco de una aplicación, que contiene código y datos asociados.
>
> *Por qué:* para el SO, un **programa** es la representación **estática en disco** con código y datos. Una instancia activa con memoria y registros es un proceso; el código fuente editable aún no es el programa ejecutable, y un hilo en segundo plano es otra cosa. [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P25

> [!question] P11 · Orden total
> ¿Qué característica define al concepto de **orden total** en la ejecución de un programa?
> - a. El planificador del sistema operativo asigna dinámicamente el orden exacto según la carga de la CPU.
> - b. Es un orden en el que intervienen mecanismos de exclusión mutua para forzar la sincronización.
> - c. Las instrucciones se ejecutan siguiendo una secuencia única, predecible y completamente determinada por el código y sus entradas.
> - d. El orden dentro de cada hilo es conocido, pero no la intercalación entre diferentes hilos concurrentes.

> [!success]- Respuesta
>
> - c. ✅ Las instrucciones se ejecutan siguiendo una secuencia única, predecible y completamente determinada por el código y sus entradas.
>
> *Por qué:* orden total = **secuencia única y predecible**, fijada por el código y las entradas. Conocer el orden dentro de cada hilo pero no la intercalación es orden parcial; depender del planificador es justo lo que el orden total excluye. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 5 · 1.5 · Orden de ejecución|Simulacro 5]] · P6

> [!question] P12 · De Listo a En ejecución
> La transición de un proceso desde el estado "Listo" al estado "En ejecución" recibe el nombre de:
> - a. Espera completada (event completion).
> - b. Reactivación (resume).
> - c. Asignación (dispatching).
> - d. Apropiación (preemption).

> [!success]- Respuesta
>
> - c. ✅ Asignación (dispatching).
>
> *Por qué:* pasar de *Listo* a *En ejecución* es la **asignación** (*dispatching*). La apropiación es la transición inversa; la reactivación viene de suspendido; la espera completada saca de *Bloqueado*. [[1.3 - Procesos en el sistema operativo#2.2 Las transiciones|Ver 1.3 · Las transiciones]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P11

> [!question] P13 · Ejecutables binarios ⚠️
> Los ejecutables formados por un conjunto de instrucciones que son procesadas directamente por la CPU sin un software intermediario se denominan ejecutables ______.

> [!success]- Respuesta
>
> - **binarios** (o binario)
>
> *Por qué:* los ejecutables **binarios** contienen instrucciones que la CPU procesa directamente, sin intérprete. Son los que genera un compilador nativo (C, C++). [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P13
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P14 · 5 instancias idénticas
> Un sistema concurrente debe gestionar el acceso a un recurso compartido del cual existen exactamente 5 instancias idénticas disponibles simultáneamente. ¿Qué primitiva de sincronización es la más adecuada para controlar este acceso?
> - a. Un semáforo general o contador, inicializado con el valor 5.
> - b. Un monitor sin variables de condición.
> - c. Una variable booleana consultada mediante un bucle de espera activa.
> - d. Un mutex binario, configurado para alternar entre 5 estados de desbloqueo.

> [!success]- Respuesta
>
> - a. ✅ Un semáforo general o contador, inicializado con el valor 5.
>
> *Por qué:* un **semáforo contador iniciado a 5** controla exactamente 5 accesos simultáneos. Un mutex es binario y la espera activa sobre un booleano gasta CPU y no cuenta instancias. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Mecanismos de exclusión mutua|Guía · Mecanismos de exclusión mutua]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 8 · 1.8 · Corrección en los programas concurrentes|Simulacro 8]] · P13

> [!question] P15 · Proceso zombi
> En sistemas Unix/Linux, ¿qué es un proceso en estado "zombi" (zombie)?
> - a. Un proceso que se ha bloqueado de forma irrecuperable por un fallo de hardware.
> - b. Un proceso que ha finalizado su ejecución pero aún mantiene una entrada en la tabla de procesos hasta que el padre recoja su código de retorno.
> - c. Un proceso trasladado a disco durante una sobrecarga de memoria RAM.
> - d. Un proceso en bucle infinito que consume el 100% de la CPU.

> [!success]- Respuesta
>
> - b. ✅ Un proceso que ha finalizado su ejecución pero aún mantiene una entrada en la tabla de procesos hasta que el padre recoja su código de retorno.
>
> *Por qué:* un **zombi** ha terminado pero conserva su entrada en la tabla de procesos hasta que el padre recoge el código de retorno. No está colgado, ni en bucle, ni en disco (eso sería suspendido). [[1.3 - Procesos en el sistema operativo#2.1 Los estados|Ver 1.3 · Los estados]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P5

> [!question] P16 · Tres ventanas de Chrome
> Si un usuario abre tres ventanas independientes de Google Chrome para navegar por diferentes páginas web, ¿qué ocurre en el sistema operativo?
> - a. El ejecutable se transforma temporalmente en un servicio del sistema operativo.
> - b. Se crean tres copias idénticas del fichero ejecutable en el disco duro con nombres distintos.
> - c. Se ejecutan múltiples procesos independientes en memoria asociados al mismo programa estático en disco.
> - d. El sistema operativo fusiona las tres ventanas en un único hilo indivisible.

> [!success]- Respuesta
>
> - c. ✅ Se ejecutan múltiples procesos independientes en memoria asociados al mismo programa estático en disco.
>
> *Por qué:* hay **un solo programa** en disco y **varios procesos** independientes en memoria, cada uno con su PID y su contexto. No se copia el ejecutable ni se convierte en servicio, y los procesos no se "fusionan" en un hilo. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P15

> [!question] P17 · Romper hold and wait
> Se desea prevenir la aparición de deadlocks eliminando la condición de Coffman conocida como 'retención y espera' (Hold and Wait). ¿Qué estrategia de diseño permite romper esta condición?
> - a. Permitir que el sistema operativo expropie o quite forzosamente recursos a cualquier proceso bloqueado.
> - b. Obligar a que cada proceso solicite y obtenga todos los recursos que necesita de una sola vez antes de iniciar su ejecución.
> - c. Establecer una jerarquía global u ordenamiento numérico estricto en la adquisición de recursos.
> - d. Garantizar que todos los recursos compartidos sean leídos de forma asíncrona sin exclusión mutua.

> [!success]- Respuesta
>
> - b. ✅ Obligar a que cada proceso solicite y obtenga todos los recursos que necesita de una sola vez antes de iniciar su ejecución.
>
> *Por qué:* **pedir todos los recursos de una vez** antes de empezar: así nunca se retiene uno mientras se espera otro. Que el SO quite recursos rompe la no apropiación; el orden global rompe la espera circular. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 8 · 1.8 · Corrección en los programas concurrentes|Simulacro 8]] · P19

> [!question] P18 · Dispatcher
> ¿Cuál es el cometido del módulo despachador (dispatcher)?
> - a. Materializar la decisión del scheduler ejecutando físicamente el cambio de contexto entre procesos.
> - b. Crear la memoria virtual en el disco de intercambio (swap).
> - c. Asignar los identificadores PID a los programas que inician.
> - d. Elegir el algoritmo teórico de ordenación de colas (FIFO, RR, SJF).

> [!success]- Respuesta
>
> - a. ✅ Materializar la decisión del scheduler ejecutando físicamente el cambio de contexto entre procesos.
>
> *Por qué:* el **dispatcher** ejecuta la decisión del scheduler: hace físicamente el **cambio de contexto**. Elegir el algoritmo es cosa del scheduler; crear la swap o asignar PID son tareas de otros componentes. [[1.3 - Procesos en el sistema operativo#3.2 El dispatcher|Ver 1.3 · El dispatcher]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P9

> [!question] P19 · SMP
> En un sistema de multiprocesamiento simétrico (**SMP**):
> - a. Cada procesador tiene su propia memoria física aislada y se comunican únicamente mediante WAN.
> - b. Todos los procesadores funcionan de igual manera, ninguno está diferenciado y cualquiera puede realizar cualquier tarea.
> - c. Existe un procesador maestro que gestiona el SO y distribuye obligatoriamente tareas a los esclavos.
> - d. Las tareas del núcleo del sistema operativo no pueden repartirse entre los procesadores.

> [!success]- Respuesta
>
> - b. ✅ Todos los procesadores funcionan de igual manera, ninguno está diferenciado y cualquiera puede realizar cualquier tarea.
>
> *Por qué:* en **SMP** todos los procesadores son iguales y cualquiera puede hacer cualquier tarea, incluidas las del SO. El maestro que reparte tareas es AMP; la memoria aislada con comunicación por red es procesamiento distribuido. [[1.2 - Computacion concurrente#4.1 Multiprocesamiento|Ver 1.2 · Multiprocesamiento]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 2 · 1.2 · Computación concurrente|Simulacro 2]] · P5

> [!question] P20 · Multiprogramación en un mononúcleo
> ¿En qué consiste la técnica de **multiprogramación** en un sistema mononúcleo?
> - a. En esperar a que cada proceso finalice por completo antes de admitir uno nuevo en la cola.
> - b. En ejecutar instrucciones verdaderamente al mismo instante físico duplicando la ALU.
> - c. En prescindir de cualquier cambio de contexto para reducir la latencia de memoria.
> - d. En asignar por turnos el procesador durante cortos periodos de tiempo a cada proceso mediante planificación.

> [!success]- Respuesta
>
> - d. ✅ En asignar por turnos el procesador durante cortos periodos de tiempo a cada proceso mediante planificación.
>
> *Por qué:* la multiprogramación **reparte el procesador por turnos** cortos entre procesos gracias al planificador. No ejecuta a la vez de verdad (eso sería paralelismo), no elimina el cambio de contexto (lo necesita) y no espera a que cada proceso acabe (eso es ejecución por lotes secuencial). [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 2 · 1.2 · Computación concurrente|Simulacro 2]] · P2

> [!question] P21 · Requisito del paralelismo real
> ¿Qué requisito hardware es imprescindible para que exista **paralelismo real**?
> - a. Disponer de un único núcleo con una memoria caché L3 de gran tamaño.
> - b. Contar exclusivamente con una tarjeta gráfica externa comunicada mediante bus PCIe.
> - c. Disponer de al menos dos núcleos de procesamiento (multinúcleo o multiprocesador).
> - d. Tener implementado un algoritmo de planificación por turnos sin soporte de hardware adicional.

> [!success]- Respuesta
>
> - c. ✅ Disponer de al menos dos núcleos de procesamiento (multinúcleo o multiprocesador).
>
> *Por qué:* para que haya paralelismo real hacen falta **al menos dos núcleos**. Con uno solo, por grande que sea su caché o por bueno que sea el planificador, solo hay multiprogramación. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 2 · 1.2 · Computación concurrente|Simulacro 2]] · P13

> [!question] P22 · Tareas A, B y C sin solución
> Considere tres tareas: Tarea A (alta prioridad), Tarea B (media prioridad) y Tarea C (baja prioridad). Tarea C retiene un cerrojo que Tarea A necesita, por lo que Tarea A se bloquea. Luego, Tarea B pasa a estar lista para ejecutarse. Si NO se aplica ningún mecanismo de solución, ¿qué sucede a continuación?
> - a. El sistema operativo aborta Tarea B por intentar acceder a una sección crítica ajena.
> - b. Tarea B se ejecuta desplazando a Tarea C; Tarea A queda indirectamente bloqueada por Tarea B hasta que B y C terminen.
> - c. Tarea C eleva automáticamente su prioridad por encima de B sin requerir ningún algoritmo especial.
> - d. Tarea A desaloja inmediatamente a Tarea B y fuerza a Tarea C a liberar el recurso.

> [!success]- Respuesta
>
> - b. ✅ Tarea B se ejecuta desplazando a Tarea C; Tarea A queda indirectamente bloqueada por Tarea B hasta que B y C terminen.
>
> *Por qué:* B (media) desaloja a C (baja), que no puede soltar el cerrojo; A (alta) queda **bloqueada indirectamente por B**. Sin herencia de prioridad, C no sube sola y el SO no aborta a B. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inversión de prioridad|Guía · Inversión de prioridad]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 8 · 1.8 · Corrección en los programas concurrentes|Simulacro 8]] · P9

> [!question] P23 · Impacto del cambio de contexto
> ¿Qué impacto tiene el **cambio de contexto** sobre el tiempo global de ejecución en la multiprogramación?
> - a. Introduce una sobrecarga que no reduce el tiempo global de ejecución, sino que lo incrementa ligeramente.
> - b. Elimina completamente las latencias provocadas por las operaciones de E/S.
> - c. Reduce a la mitad el tiempo global necesario para completar todos los procesos concurrentes.
> - d. Garantiza una aceleración lineal de procesamiento idéntica a la del paralelismo puro.

> [!success]- Respuesta
>
> - a. ✅ Introduce una sobrecarga que no reduce el tiempo global de ejecución, sino que lo incrementa ligeramente.
>
> *Por qué:* el cambio de contexto es **sobrecarga**: mientras se guarda y restaura el estado no se ejecuta código útil, así que el tiempo global **aumenta ligeramente**. La multiprogramación no acelera como el paralelismo ni elimina las esperas de E/S. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 2 · 1.2 · Computación concurrente|Simulacro 2]] · P4

> [!question] P24 · Tubería Unix
> Una tubería (pipeline) en un sistema operativo Unix/Linux, donde la salida de un proceso se conecta a la entrada de otro, es un ejemplo de:
> - a. Procesos cooperantes.
> - b. Procesos en competencia destructiva por el bus de direcciones.
> - c. Sistemas distribuidos en malla sin conexión física.
> - d. Procesos independientes sin interacción.

> [!success]- Respuesta
>
> - a. ✅ Procesos cooperantes.
>
> *Por qué:* en `ls | grep` la salida de uno es la entrada del otro: **procesos cooperantes**. No son independientes (se pasan datos) ni compiten. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 4 · 1.4 · Técnicas de programación concurrente|Simulacro 4]] · P19

> [!question] P25 · Qué garantiza `volatile`
> ¿Qué efecto garantiza el uso de la palabra clave `volatile` sobre un campo en Java?
> - a. Convierte el tipo de dato en inmutable de sólo lectura durante la ejecución.
> - b. Garantiza atomicidad completa en operaciones compuestas como `count++`.
> - c. Garantiza que las lecturas y escrituras se realicen directamente sobre la memoria principal, asegurando visibilidad inmediata.
> - d. Bloquea el objeto impidiendo que cualquier otro hilo lea la variable hasta que finalice el método.

> [!success]- Respuesta
>
> - c. ✅ Garantiza que las lecturas y escrituras se realicen directamente sobre la memoria principal, asegurando visibilidad inmediata.
>
> *Por qué:* `volatile` garantiza **visibilidad**: lecturas y escrituras van a memoria principal. **No** da atomicidad a `count++`, no bloquea el objeto (eso es `synchronized`) ni lo hace inmutable (`final`). [[1.6 - Sincronizacion#4. El problema de la visibilidad de datos|Ver 1.6 · Visibilidad de datos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P8

> [!question] P26 · Servidor web con un hilo por petición
> ¿Cómo se clasifica un servidor web que recibe peticiones HTTP y asigna cada una a un hilo de procesamiento para mantener la interfaz o escucha atenta?
> - a. Aplicación con programación concurrente.
> - b. Aplicación puramente secuencial y monolítica.
> - c. Simulación científica masivamente paralela.
> - d. Sistema embebido en tiempo real estricto (hard real-time).

> [!success]- Respuesta
>
> - a. ✅ Aplicación con programación concurrente.
>
> *Por qué:* es el ejemplo clásico de **programación concurrente** general: atender muchas peticiones y E/S manteniendo la respuesta. No busca acelerar un cálculo (paralela), no es secuencial y no es tiempo real estricto. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 4 · 1.4 · Técnicas de programación concurrente|Simulacro 4]] · P6

> [!question] P27 · `while(running)` sin `volatile`
> Un hilo _A_ actualiza una variable `boolean running = true` a `false`. Si la variable no es `volatile` ni se usa sincronización, ¿qué anomalía clásica puede manifestar el hilo _B_ que ejecuta `while(running) { }`?
> - a. La máquina virtual detendrá forzosamente ambos hilos por desbordamiento de pila (_StackOverflowError_).
> - b. El hilo _B_ puede seguir leyendo el valor `true` de su caché local y quedar atrapado indefinidamente en el bucle.
> - c. El hilo _B_ provocará inmediatamente un error de tipo `NullPointerException`.
> - d. El hilo _A_ se quedará suspendido automáticamente a la espera de que _B_ termine.

> [!success]- Respuesta
>
> - b. ✅ El hilo _B_ puede seguir leyendo el valor `true` de su caché local y quedar atrapado indefinidamente en el bucle.
>
> *Por qué:* B puede seguir viendo `true` en su caché (o el JIT puede optimizar la lectura) y **quedarse en el bucle para siempre**. No hay `StackOverflowError`, `NullPointerException` ni suspensión automática de A. [[1.6 - Sincronizacion#4. El problema de la visibilidad de datos|Ver 1.6 · Visibilidad de datos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P6

> [!question] P28 · `BlockingQueue`
> Si una aplicación Java utiliza la clase `BlockingQueue` para enviar y recibir datos entre hilos dentro de un mismo proceso, ¿qué mecanismo técnico de comunicación se está utilizando?
> - a. Paso de mensajes mediante un buffer de memoria compartido en la memoria principal del proceso.
> - b. Invocación remota asimétrica desacoplada de la pila de ejecución de la JVM.
> - c. Comunicaciones mediante sockets de red sobre la interfaz de red loopback.
> - d. Comunicación símplex no bloqueante respaldada por archivos en disco duro.

> [!success]- Respuesta
>
> - a. ✅ Paso de mensajes mediante un buffer de memoria compartido en la memoria principal del proceso.
>
> *Por qué:* es **paso de mensajes con un buffer en memoria compartida** del proceso (cola FIFO entre hilos). No hay sockets, ni ficheros en disco, ni invocación remota. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 7 · 1.7 · Comunicación entre procesos|Simulacro 7]] · P16

> [!question] P29 · Ejecutables binarios: portabilidad
> ¿Cuál es una característica intrínseca fundamental de los **ejecutables binarios** compilados de forma nativa?
> - a. Son multiplataforma por naturaleza y se ejecutan en cualquier CPU sin necesidad de adaptación previa.
> - b. Requieren obligatoriamente la presencia de un entorno virtual como la JVM para ser procesados.
> - c. Contienen texto legible en lenguaje ensamblador que el sistema operativo traduce línea a línea.
> - d. Están vinculados a una arquitectura de procesador específica y requieren recompilación para ejecutarse en arquitecturas incompatibles.

> [!success]- Respuesta
>
> - d. ✅ Están vinculados a una arquitectura de procesador específica y requieren recompilación para ejecutarse en arquitecturas incompatibles.
>
> *Por qué:* el código máquina depende del juego de instrucciones (x86_64, ARM…), así que el binario **solo funciona en su arquitectura** y hay que recompilarlo para otra. No es texto ensamblador, no es multiplataforma y no necesita JVM (eso son los interpretados). [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P19

> [!question] P30 · Timeout y liberar cerrojos
> Un algoritmo de gestión de recursos asigna un tiempo máximo de espera a las solicitudes de cerrojos. Si una tarea no obtiene el recurso en ese tiempo, suelta los cerrojos que ya tenía y reintenta más tarde. ¿Qué condición de Coffman está atacando directamente para evitar deadlocks?
> - a. Exclusión mutua.
> - b. No apropiación.
> - c. Inversión de prioridad.
> - d. Retención y espera (Hold and Wait).

> [!success]- Respuesta
>
> - d. ✅ Retención y espera (Hold and Wait).
>
> *Por qué:* al soltar lo que tenía si no consigue el resto, la tarea deja de **retener mientras espera**: rompe *hold and wait*. No toca la exclusión mutua; la no apropiación se rompería si el **sistema** le quitara los recursos; la inversión de prioridad no es una condición de Coffman. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 8 · 1.8 · Corrección en los programas concurrentes|Simulacro 8]] · P12

> [!question] P31 · Memoria común compartida ⚠️
> La arquitectura de sistemas paralelos donde múltiples núcleos o procesadores comparten una memoria principal común se denomina ______.

> [!success]- Respuesta
>
> - **multiprocesamiento**
>
> *Por qué:* varios núcleos o procesadores **compartiendo memoria principal** = **multiprocesamiento**. Si cada uno tiene su memoria local, es procesamiento distribuido. [[1.2 - Computacion concurrente#4.1 Multiprocesamiento|Ver 1.2 · Multiprocesamiento]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 2 · 1.2 · Computación concurrente|Simulacro 2]] · P3
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P32 · Dos hilos al 100 % sin avanzar
> Al analizar una aplicación concurrente, se detecta que dos hilos están consumiendo el 100% del procesador cambiando constantemente el valor de sus variables, pero sin lograr avanzar en el procesamiento de sus datos. ¿Qué problema presenta la aplicación?
> - a. Interbloqueo activo (livelock).
> - b. Interbloqueo pasivo (deadlock).
> - c. Violación del principio de exclusión mutua.
> - d. Inversión de prioridad no gestionada.

> [!success]- Respuesta
>
> - a. ✅ Interbloqueo activo (livelock).
>
> *Por qué:* activos, cambiando de estado y sin progreso: **livelock**. En un deadlock los hilos estarían **suspendidos**, sin gastar CPU. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Livelock (interbloqueo activo)|Guía · Livelock]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 8 · 1.8 · Corrección en los programas concurrentes|Simulacro 8]] · P20

> [!question] P33 · Papel del intérprete o máquina virtual
> En el contexto de los lenguajes interpretados o basados en bytecode (como Java o Python), ¿cuál es el papel principal del **intérprete o máquina virtual**?
> - a. Compilar de forma permanente el código a un fichero `.exe` en el disco duro antes de cada inicio.
> - b. Sustituir al sistema operativo administrando los controladores físicos de la placa base.
> - c. Tomar los códigos de operación intermedios y traducirlos al lenguaje máquina que el procesador físico ejecuta.
> - d. Eliminar los errores lógicos del algoritmo del programador en tiempo de compilación.

> [!success]- Respuesta
>
> - c. ✅ Tomar los códigos de operación intermedios y traducirlos al lenguaje máquina que el procesador físico ejecuta.
>
> *Por qué:* traduce los **códigos intermedios** (bytecode, script) a instrucciones máquina que ejecuta la CPU. No sustituye al SO, no genera un `.exe` permanente y no corrige errores lógicos del programador. [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P32

> [!question] P34 · Firmware ⚠️
> Dentro de los programas para la gestión del hardware, el software básico grabado en memorias no volátiles que controla directamente los circuitos de un periférico o placa base se conoce como ______.

> [!success]- Respuesta
>
> - **firmware**
>
> *Por qué:* el **firmware** es el software básico grabado en memoria no volátil que controla directamente el hardware (BIOS/UEFI, controladora de un periférico). No confundir con el *driver*, que se carga desde el SO. [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P4
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P35 · Planificador a largo plazo
> ¿Cuál es la función principal del planificador a largo plazo en un sistema operativo?
> - a. Restaurar los registros del procesador y cambiar el contador de programa.
> - b. Alternar procesos en la CPU en intervalos de milisegundos mediante quantum.
> - c. Seleccionar qué nuevos procesos pasan a la cola de preparados, controlando el grado de multiprogramación.
> - d. Gestionar el envío de señales interproceso como SIGKILL.

> [!success]- Respuesta
>
> - c. ✅ Seleccionar qué nuevos procesos pasan a la cola de preparados, controlando el grado de multiprogramación.
>
> *Por qué:* decide **qué procesos nuevos entran** en la cola de listos y controla el **grado de multiprogramación**. Alternar procesos cada pocos milisegundos lo hace el planificador a corto plazo; restaurar registros, el dispatcher. [[1.3 - Procesos en el sistema operativo#3. Planificación de procesos|Ver 1.3 · Planificación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P2

> [!question] P36 · Orden parcial
> ¿Qué se entiende por **orden parcial** en programación concurrente?
> - a. Se conoce el orden de ejecución dentro de cada proceso o hilo, pero no el orden en el que se intercalan entre sí.
> - b. Las instrucciones dentro de cada hilo se ejecutan en orden aleatorio según las interrupciones hardware.
> - c. Solo se ejecutan una parte de los hilos creados debido a limitaciones de memoria.
> - d. El programador fija estáticamente en tiempo de compilación el entrelazado de los hilos.

> [!success]- Respuesta
>
> - a. ✅ Se conoce el orden de ejecución dentro de cada proceso o hilo, pero no el orden en el que se intercalan entre sí.
>
> *Por qué:* orden parcial = **se conoce el orden dentro de cada hilo, pero no cómo se intercalan**. No es aleatorio dentro del hilo, ni significa que se ejecuten solo algunos, ni lo fija el programador al compilar. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 5 · 1.5 · Orden de ejecución|Simulacro 5]] · P11

> [!question] P37 · ¿Indeterminismo = programa incorrecto?
> ¿El comportamiento indeterminista (posibles diferentes secuencias de ejecución ante las mismas entradas) implica necesariamente que un programa concurrente sea incorrecto?
> - a. No, siempre y cuando el sistema operativo desactive la multitarea apropiativa.
> - b. No, que existan diferentes caminos de ejecución no significa por sí solo que el programa sea incorrecto, siempre que todos conduzcan a un resultado válido.
> - c. Sí, por definición cualquier programa que no presente orden total se considera defectuoso.
> - d. Sí, porque el estándar POSIX exige determinismo estricto en el resultado y en el tiempo de ejecución.

> [!success]- Respuesta
>
> - b. ✅ No, que existan diferentes caminos de ejecución no significa por sí solo que el programa sea incorrecto, siempre que todos conduzcan a un resultado válido.
>
> *Por qué:* no: puede haber **varios caminos de ejecución y ser correcto** si todos llevan a un resultado válido (por ejemplo, otro orden de impresión). POSIX no exige determinismo y desactivar la multitarea no es la condición. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 5 · 1.5 · Orden de ejecución|Simulacro 5]] · P19

> [!question] P38 · Walkie-talkie
> Un sistema de comunicación mediante walkie-talkies o una vía estrecha de un solo carril con tráfico en ambos sentidos representan analogías de ¿qué tipo de canal según su capacidad?
> - a. Símplex, puesto que la información fluye estrictamente en una única dirección sin posibilidad de retorno o respuesta.
> - b. Full duplex, dado que permite la interacción de dos partes de forma totalmente simultánea y sin esperas.
> - c. Half duplex, ya que la comunicación es bidireccional pero alternante en el tiempo, impidiendo la transmisión simultánea.
> - d. Invocación remota, debido a que requiere un protocolo de red cliente-servidor estrictamente síncrono.

> [!success]- Respuesta
>
> - c. ✅ Half duplex, ya que la comunicación es bidireccional pero alternante en el tiempo, impidiendo la transmisión simultánea.
>
> *Por qué:* **half duplex**: los dos sentidos, pero **no a la vez**. Full duplex sería simultáneo (teléfono); símplex, un único sentido (radio, cine). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 7 · 1.7 · Comunicación entre procesos|Simulacro 7]] · P4

> [!question] P39 · Pipeline: B depende de A
> En un sistema de procesamiento por etapas (_pipeline_), la tarea _B_ requiere como entrada indispensable los datos procesados previamente por la tarea _A_. ¿Qué tipo de sincronización se requiere principalmente?
> - a. Sincronización de control.
> - b. Exclusión mutua pura sin dependencias.
> - c. No se requiere sincronización si las tareas corren en hilos separados.
> - d. Sincronización de memoria caché local.

> [!success]- Respuesta
>
> - a. ✅ Sincronización de control.
>
> *Por qué:* si B necesita los resultados de A hay que coordinar el **orden**: **sincronización de control**. La exclusión mutua protege datos, no impone precedencias. [[1.6 - Sincronizacion#1. Sincronización de tareas|Ver 1.6 · Sincronización de tareas]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P11

> [!question] P40 · Solo lecturas concurrentes
> Si múltiples hilos acceden a una misma variable compartida de forma simultánea y sin ningún mecanismo de sincronización, pero **todos ellos realizan exclusivamente operaciones de lectura**, ¿se produce una carrera de datos?
> - a. Sí, la falta de sincronización siempre desencadena una carrera de datos sin importar la operación.
> - b. Solo si hay más de 4 hilos concurrentes involucrados.
> - c. Sí, porque los registros de la CPU pueden desbordarse al leer a la vez.
> - d. No, porque es requisito indispensable que al menos uno de los accesos sea de modificación/escritura.

> [!success]- Respuesta
>
> - d. ✅ No, porque es requisito indispensable que al menos uno de los accesos sea de modificación/escritura.
>
> *Por qué:* para que haya *data race* hace falta que **al menos un acceso sea de escritura**. Si todos leen, no hay carrera, aunque no haya sincronización ni importe el número de hilos. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 5 · 1.5 · Orden de ejecución|Simulacro 5]] · P2

> [!question] P41 · Consumidor espera sin soltar el cerrojo
> En el problema del Productor-Consumidor con buffer limitado, ¿qué sucede si el consumidor comprueba que el buffer está vacío y se queda esperando dentro de la sección crítica sin liberar el cerrojo?
> - a. El sistema operativo expulsa automáticamente al consumidor para permitir el paso al productor.
> - b. El buffer amplía dinámicamente su capacidad para resolver la condición.
> - c. El consumidor consumirá elementos nulos sin generar consecuencias adversas.
> - d. Se produce un interbloqueo (_deadlock_), pues el productor no puede entrar a insertar elementos para que se cumpla la condición.

> [!success]- Respuesta
>
> - d. ✅ Se produce un interbloqueo (_deadlock_), pues el productor no puede entrar a insertar elementos para que se cumpla la condición.
>
> *Por qué:* si el consumidor espera **con el cerrojo cogido**, el productor no puede entrar a añadir elementos: **deadlock**. El buffer no crece solo y el SO no expulsa al consumidor para dejar pasar al productor. [[1.6 - Sincronizacion#5. Condición de sincronización|Ver 1.6 · Condición de sincronización]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P10

> [!question] P42 · Bernstein: E(S1) ∩ L(S2) = {c}
> Sean dos conjuntos de instrucciones _S1_ y _S2_ con los siguientes conjuntos de lectura y escritura:
> _L(S1) = {a, b}_, _E(S1) = {c}_
> _L(S2) = {c, d}_, _E(S2) = {e}_
> ¿Qué condición del Teorema de Bernstein se viola impidiendo su ejecución concurrente sin sincronización?
> - a. La condición de independencia de salida (_E(S1) ∩ E(S2) = ∅_).
> - b. Se cumplen todas las condiciones y pueden ejecutarse en paralelo de forma segura.
> - c. La condición simétrica de lectura (_L(S1) ∩ E(S2) = ∅_).
> - d. La condición de independencia de flujo de datos (_E(S1) ∩ L(S2) = ∅_).

> [!success]- Respuesta
>
> - d. ✅ La condición de independencia de flujo de datos (_E(S1) ∩ L(S2) = ∅_).
>
> *Por qué:* `S1` escribe `c` y `S2` lo lee: **independencia de flujo de datos** violada (`S2` depende de `S1`). E(S1) ∩ E(S2) = ∅ y L(S1) ∩ E(S2) = ∅, así que esas sí se cumplen. [[1.6 - Sincronizacion#2.3 Independencia de flujo de datos|Ver 1.6 · Independencia de flujo de datos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P17

> [!question] P43 · Bernstein: L(P1) ∩ E(P2) ≠ ∅
> Si dos procesos _P1_ y _P2_ cumplen que _L(P1) ∩ E(P2) ≠ ∅_, ¿cuál es la consecuencia directa según el Teorema de Bernstein?
> - a. Se garantiza la ausencia total de condiciones de carrera.
> - b. Ambos procesos pueden ejecutarse concurrentemente sin ningún tipo de sincronización.
> - c. Se produce una violación estricta de la independencia de salida.
> - d. Se viola la independencia de entrada, exigiendo sincronización de acceso para evitar que _P1_ lea datos mientras _P2_ los modifica.

> [!success]- Respuesta
>
> - d. ✅ Se viola la independencia de entrada, exigiendo sincronización de acceso para evitar que _P1_ lea datos mientras _P2_ los modifica.
>
> *Por qué:* lo que lee uno lo escribe el otro: se viola la **independencia de entrada** y hay que sincronizar. No es la de salida (sería E ∩ E) y desde luego no garantiza ausencia de carreras. [[1.6 - Sincronizacion#2.1 Independencia de entrada|Ver 1.6 · Independencia de entrada]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P16

> [!question] P44 · Transición por apropiación
> ¿Qué suceso provoca la transición por "Apropiación" o interrupción (preemption) de "En ejecución" a "Listo"?
> - a. La falta de espacio físico en la memoria RAM del equipo.
> - b. La expiración del quantum de tiempo asignado o la llegada de un proceso de mayor prioridad.
> - c. La terminación controlada del programa mediante una llamada al sistema exit.
> - d. La petición explícita de lectura o escritura en un disco.

> [!success]- Respuesta
>
> - b. ✅ La expiración del quantum de tiempo asignado o la llegada de un proceso de mayor prioridad.
>
> *Por qué:* pasa de *En ejecución* a *Listo* cuando **expira el quantum** o llega un proceso de **más prioridad**. Pedir E/S lleva a *Bloqueado*, `exit` lleva a *Terminado* y la falta de RAM provoca suspensión. [[1.3 - Procesos en el sistema operativo#2.2 Las transiciones|Ver 1.3 · Las transiciones]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P1

> [!question] P45 · Servicio del SO vs. servicio de aplicación
> ¿Qué distingue a un **servicio del sistema operativo** de un **servicio de aplicación** instalado por el usuario?
> - a. Los servicios de aplicación requieren obligatoriamente una pantalla táctil para funcionar.
> - b. Los del sistema gestionan recursos esenciales del SO (red, autenticación, audio), mientras que los de aplicación cubren requerimientos de software instalado (servidor web, base de datos).
> - c. Los servicios del sistema se ejecutan en la CPU, mientras que los de aplicación se ejecutan exclusivamente en la memoria swap.
> - d. Los servicios del sistema se eliminan del disco tras el primer inicio de sesión.

> [!success]- Respuesta
>
> - b. ✅ Los del sistema gestionan recursos esenciales del SO (red, autenticación, audio), mientras que los de aplicación cubren requerimientos de software instalado (servidor web, base de datos).
>
> *Por qué:* los **del sistema** gestionan recursos esenciales del SO (red, audio, autenticación); los **de aplicación** dan soporte a software instalado (servidor web, base de datos). Ninguno se borra tras el login, ni necesita pantalla táctil, ni corre "en la swap". [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P38

> [!question] P46 · Cliente-servidor ⚠️
> En un sistema donde los clientes inician las solicitudes y el servidor escucha y responde proporcionando servicios, se utiliza un tipo de comunicación según el rol de los interlocutores denominada ______.

> [!success]- Respuesta
>
> - **cliente-servidor**
>
> *Por qué:* los clientes piden y el servidor responde: comunicación **asimétrica** o **cliente-servidor**. En Moodle se aceptó `cliente-servidor`; "asimétrica" es el nombre de la categoría. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 7 · 1.7 · Comunicación entre procesos|Simulacro 7]] · P13
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P47 · Seguridad vs. viveza
> En el contexto de los programas concurrentes, ¿cuál es la diferencia fundamental en la naturaleza de lo que garantizan las propiedades de seguridad frente a las propiedades de viveza?
> - a. Las propiedades de seguridad dependen de las políticas del planificador del sistema operativo, mientras que las de viveza dependen exclusivamente de cerrojos binarios.
> - b. Las propiedades de seguridad especifican 'lo que no debe ocurrir' para evitar estados incorrectos, mientras que las de viveza especifican 'lo que debe ocurrir' para garantizar el progreso.
> - c. Las propiedades de seguridad garantizan la velocidad de ejecución, mientras que las de viveza previenen condiciones de carrera en variables globales.
> - d. Las propiedades de seguridad aplican únicamente a sistemas distribuidos, mientras que las de viveza aplican a la programación multihilo local.

> [!success]- Respuesta
>
> - b. ✅ Las propiedades de seguridad especifican 'lo que no debe ocurrir' para evitar estados incorrectos, mientras que las de viveza especifican 'lo que debe ocurrir' para garantizar el progreso.
>
> *Por qué:* seguridad = **lo que no debe pasar** (estados incorrectos); viveza = **lo que debe pasar** (progreso). No van de velocidad, ni se reparten entre local y distribuido. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#A.8 · Corrección en los programas concurrentes|Guía · A.8 Corrección]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 8 · 1.8 · Corrección en los programas concurrentes|Simulacro 8]] · P14

> [!question] P48 · `wait()` dentro de `synchronized`
> En Java, ¿cuál es el comportamiento específico de la invocación al método `wait()` dentro de un bloque sincronizado?
> - a. Pone al hilo en espera activa (_busy waiting_) consumiendo CPU mientras retiene el cerrojo.
> - b. Suspende al hilo pero mantiene el bloqueo exclusivo del objeto impidiendo todo acceso exterior.
> - c. Termina definitivamente la ejecución del hilo y destruye su pila de ejecución.
> - d. Suspende el hilo actual y libera de manera atómica el cerrojo del monitor, permitiendo la entrada a otros hilos.

> [!success]- Respuesta
>
> - d. ✅ Suspende el hilo actual y libera de manera atómica el cerrojo del monitor, permitiendo la entrada a otros hilos.
>
> *Por qué:* `wait()` **suspende el hilo y libera el cerrojo** de forma atómica para que otros puedan cambiar la condición. No termina el hilo, no hace espera activa y no conserva el bloqueo (eso causaría deadlock). [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 6 · 1.6 · Sincronización|Simulacro 6]] · P1

> [!question] P49 · Round Robin: expira el quantum
> En el algoritmo de planificación Round Robin (RR), ¿qué sucede si un proceso no ha terminado su tarea cuando expira su quantum asignado?
> - a. Pasa directamente al estado bloqueado hasta que vuelva a haber tiempo libre.
> - b. Es expulsado de la CPU y se coloca al final de la cola de listos de forma cíclica.
> - c. Se le degrada su prioridad al nivel más bajo y se suspende en disco.
> - d. Continúa ejecutándose indefinidamente hasta que haga una llamada a E/S.

> [!success]- Respuesta
>
> - b. ✅ Es expulsado de la CPU y se coloca al final de la cola de listos de forma cíclica.
>
> *Por qué:* en RR, si el quantum se acaba el proceso es **expulsado y va al final de la cola de listos** (cíclico). No se bloquea (no espera ningún evento), no baja de prioridad (eso es multinivel) y no sigue indefinidamente. [[1.3 - Procesos en el sistema operativo#3.1 Algoritmos de planificación|Ver 1.3 · Algoritmos de planificación]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 3 · 1.3 · Procesos en el sistema operativo|Simulacro 3]] · P13

> [!question] P50 · Ejecutable en Linux/macOS
> En sistemas basados en GNU/Linux o macOS, ¿cómo determina principalmente el sistema operativo que un fichero es un ejecutable?
> - a. Por la presencia estricta y obligatoria de la extensión `.exe` o `.com` al final del nombre.
> - b. Por estar alojado exclusivamente en el directorio `/boot` del disco raíz.
> - c. Por su tamaño en bytes, que debe ser múltiplo exacto del tamaño de página de memoria.
> - d. Mediante la activación de los permisos de ejecución (+x) en los metadatos del fichero, independientemente de su extensión.

> [!success]- Respuesta
>
> - d. ✅ Mediante la activación de los permisos de ejecución (+x) en los metadatos del fichero, independientemente de su extensión.
>
> *Por qué:* lo decide el **bit de ejecución** (`+x`) de los metadatos del fichero, sin importar la extensión. La extensión `.exe` es cosa de Windows; el tamaño o estar en `/boot` no influyen. [[1.1 - Programa vs. Proceso#2. Ejecutable|Ver 1.1 · Ejecutable]]
>
> *Origen:* [[Simulacros tipo test tema 1#Simulacro 1 · 1.1 · Programa vs. proceso|Simulacro 1]] · P40

---

## Hoja de respuestas

> [!abstract]- 📝 Soluciones (ábrelo solo para corregir)
> P1 **a** · P2 **c** · P3 **a** · P4 **c** · P5 **c**  
> P6 **b** · P7 **b** · P8 **d** · P9 **a** · P10 **d**  
> P11 **c** · P12 **c** · P13 *binarios* · P14 **a** · P15 **b**  
> P16 **c** · P17 **b** · P18 **a** · P19 **b** · P20 **d**  
> P21 **c** · P22 **b** · P23 **a** · P24 **a** · P25 **c**  
> P26 **a** · P27 **b** · P28 **a** · P29 **d** · P30 **d**  
> P31 *multiprocesamiento* · P32 **a** · P33 **c** · P34 *firmware* · P35 **c**  
> P36 **a** · P37 **b** · P38 **c** · P39 **a** · P40 **d**  
> P41 **d** · P42 **d** · P43 **d** · P44 **b** · P45 **b**  
> P46 *cliente-servidor* · P47 **b** · P48 **d** · P49 **b** · P50 **d**  

> [!tip] Nota
> Cada acierto vale 0,2 puntos: 40 aciertos son un 8. Si sacas menos de 35, repite los simulacros por apartado de los temas en que más fallas.

## Esquema de repaso

- **Descarte:** fuera las opciones absurdas y las que llevan palabras absolutas → entre las que quedan, la más matizada.
- **Trampas que más se repiten:** concurrencia ≠ paralelismo · el cambio de contexto **no** acelera · `volatile` = visibilidad, **no** atomicidad · `wait()` **libera** el cerrojo · deadlock (suspendidos) ≠ livelock (activos) · el timeout rompe *hold and wait*, no la no apropiación.

## Relaciones

- [[Simulacros tipo test tema 1]] — las 174 preguntas por apartado, de donde sale esta selección
- [[Guia examen temas 1 y 2]] — teoría y chuleta
- [[Examen año pasado]] — formato del examen anterior (práctico, Tema 2)

## Para repasar

- [ ] Hacer el simulacro en 25 minutos sin abrir las respuestas.
- [ ] Repasar en el apunte enlazado cada pregunta fallada.
- [ ] Repetir el simulacro unos días después y comparar la nota.

## Guía relacionada

- [[Guia examen temas 1 y 2|🧠 Guía de teoría y chuleta]]
- [[Test de repaso temas 1 y 2|✅ Test de repaso temas 1 y 2]]
- [[Practicos temas 1 y 2|💻 Prácticos temas 1 y 2]]
