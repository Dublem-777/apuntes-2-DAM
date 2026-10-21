# Cuestionario del apartado 1-6

##### Estado

Finalizado

##### Comenzado

domingo, 11 de octubre de 2026, 19:40

##### Completado

domingo, 11 de octubre de 2026, 19:44

##### Duración

4 minutos 16 segundos

##### Puntos

20,00/20,00

##### Calificación

**10,00** de 10,00 (**100**%)

#### Pregunta 1

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En Java, ¿cuál es el comportamiento específico de la invocación al método `wait()` dentro de un bloque sincronizado?

Pregunta 1Seleccione una:

a.

Suspende el hilo actual y libera de manera atómica el cerrojo del monitor, permitiendo la entrada a otros hilos.

¡Correcto! Al liberar el bloqueo, otros hilos pueden interactuar con el recurso para modificar la condición esperada.

b.

Termina definitivamente la ejecución del hilo y destruye su pila de ejecución.

c.

Pone al hilo en espera activa (_busy waiting_) consumiendo CPU mientras retiene el cerrojo.

d.

Suspende al hilo pero mantiene el bloqueo exclusivo del objeto impidiendo todo acceso exterior.

#### Retroalimentación

La respuesta correcta es: Suspende el hilo actual y libera de manera atómica el cerrojo del monitor, permitiendo la entrada a otros hilos.

#### Pregunta 2

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué es un **monitor** en el contexto del diseño de sistemas concurrentes?

Pregunta 2Seleccione una:

a.

Una herramienta gráfica externa que supervisa el uso de procesador y memoria de la JVM.

b.

Un hilo del sistema encargado de terminar procesos que causan condiciones de carrera.

c.

Un cerrojo de bajo nivel que solo permite sincronización de control sin admitir datos compartidos.

d.

Una abstracción de alto nivel que encapsula un recurso integrando exclusión mutua y sincronización condicional (espera y notificación).

¡Correcto! Facilita la programación estructurada de la concurrencia protegiendo recursos de forma modular.

#### Retroalimentación

La respuesta correcta es: Una abstracción de alto nivel que encapsula un recurso integrando exclusión mutua y sincronización condicional (espera y notificación).

#### Pregunta 3

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el contexto del modelo de memoria de Java (JMM), ¿por qué se produce fundamentalmente el problema de la visibilidad de datos entre hilos?

Pregunta 3Seleccione una:

a.

Porque la memoria RAM física prohíbe que dos hilos compartan la misma dirección de memoria virtual.

b.

Porque los hilos operan sobre copias locales en sus cachés de trabajo y no hay garantía inmediata de propagación a la memoria principal.

¡Correcto! Sin sincronización, el JMM no garantiza cuándo se propagan las escrituras locales a la memoria principal.

c.

Porque el compilador de Java convierte automáticamente todas las variables en constantes inmutables.

d.

Porque el recolector de basura (Garbage Collector) elimina periódicamente las variables no sincronizadas.

#### Retroalimentación

La respuesta correcta es: Porque los hilos operan sobre copias locales en sus cachés de trabajo y no hay garantía inmediata de propagación a la memoria principal.

#### Pregunta 4

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la diferencia fundamental entre los métodos `notify()` y `notifyAll()` en el modelo de monitores de Java?

Pregunta 4Seleccione una:

a.

`notify()` despierta de forma arbitraria a un único hilo en espera, mientras que `notifyAll()` despierta a todos los hilos que esperan sobre dicho monitor.

¡Correcto! Con `notifyAll()` todos los hilos despiertos compiten por readquirir el cerrojo.

b.

`notify()` solo sirve para hilos prioritarios y `notifyAll()` para hilos demonio (_daemon_).

c.

`notifyAll()` reinicia la JVM y `notify()` reinicia únicamente el hilo en ejecución.

d.

`notify()` libera el bloqueo de inmediato, mientras que `notifyAll()` retiene el bloqueo permanentemente.

#### Retroalimentación

La respuesta correcta es: `notify()` despierta de forma arbitraria a un único hilo en espera, mientras que `notifyAll()` despierta a todos los hilos que esperan sobre dicho monitor.

#### Pregunta 5

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál de las siguientes medidas es una técnica efectiva para reducir la contención por bloqueo en aplicaciones concurrentes?

Pregunta 5Seleccione una:

a.

Reducir el tamaño y la duración del código dentro de la sección crítica.

¡Correcto! Al estar menos tiempo retenido el cerrojo, disminuye el tiempo de espera de los demás hilos.

b.

Aumentar el número de hilos que compiten simultáneamente por el mismo cerrojo.

c.

Incluir llamadas de E/S bloqueantes (como acceso a disco o red) dentro de la sección crítica.

d.

Reemplazar todos los cerrojos por bucles de espera activa (_busy waiting_).

#### Retroalimentación

La respuesta correcta es: Reducir el tamaño y la duración del código dentro de la sección crítica.

#### Pregunta 6

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un hilo _A_ actualiza una variable `boolean running = true` a `false`. Si la variable no es `volatile` ni se usa sincronización, ¿qué anomalía clásica puede manifestar el hilo _B_ que ejecuta `while(running) { }`?

Pregunta 6Seleccione una:

a.

El hilo _B_ puede seguir leyendo el valor `true` de su caché local y quedar atrapado indefinidamente en el bucle.

¡Correcto! Debido a la falta de visibilidad y a optimizaciones del JIT, el hilo _B_ puede no percibir jamás el cambio.

b.

La máquina virtual detendrá forzosamente ambos hilos por desbordamiento de pila (_StackOverflowError_).

c.

El hilo _B_ provocará inmediatamente un error de tipo `NullPointerException`.

d.

El hilo _A_ se quedará suspendido automáticamente a la espera de que _B_ termine.

#### Retroalimentación

La respuesta correcta es: El hilo _B_ puede seguir leyendo el valor `true` de su caché local y quedar atrapado indefinidamente en el bucle.

#### Pregunta 7

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

A nivel de código máquina, la instrucción `x = x + 1` se descompone en `LOAD X R1`, `ADD R1 1` y `STORE R1 X`. Si dos hilos la ejecutan en paralelo sin exclusión mutua partiendo de _x = 0_, ¿cuál es un resultado erróneo posible por entrelazamiento?

Pregunta 7Seleccione una:

a.

El valor final de _x_ es siempre 0 debido a un reinicio de memoria.

b.

El hardware del procesador aborta automáticamente la ejecución lanzando un trap.

c.

El valor final de _x_ es 1, perdiéndose uno de los dos incrementos.

¡Correcto! Ambos hilos cargan 0, calculan 1 y ambos escriben 1 de vuelta en memoria.

d.

El valor final de _x_ será 3 por desbordamiento de registro.

#### Retroalimentación

La respuesta correcta es: El valor final de _x_ es 1, perdiéndose uno de los dos incrementos.

#### Pregunta 8

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué efecto garantiza el uso de la palabra clave `volatile` sobre un campo en Java?

Pregunta 8Seleccione una:

a.

Bloquea el objeto impidiendo que cualquier otro hilo lea la variable hasta que finalice el método.

b.

Convierte el tipo de dato en inmutable de sólo lectura durante la ejecución.

c.

Garantiza atomicidad completa en operaciones compuestas como `count++`.

d.

Garantiza que las lecturas y escrituras se realicen directamente sobre la memoria principal, asegurando visibilidad inmediata.

¡Correcto! Establece barreras de memoria para sincronizar la visibilidad de los datos compartidos entre hilos.

#### Retroalimentación

La respuesta correcta es: Garantiza que las lecturas y escrituras se realicen directamente sobre la memoria principal, asegurando visibilidad inmediata.

#### Pregunta 9

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un sistema cuenta con una variable compartida _x_. El hilo _T1_ ejecuta la instrucción `x = x + 5` y el hilo _T2_ ejecuta `x = x * 2`. ¿Por qué se requiere sincronización de acceso a datos en este escenario?

Pregunta 9Seleccione una:

a.

Porque las operaciones aritméticas simples no pueden ejecutarse en CPUs multinúcleo.

b.

Para evitar lecturas o escrituras entrelazadas no atómicas sobre _x_.

¡Correcto! Ambas operaciones leen y escriben en la misma variable sin atomicidad.

c.

Porque el sistema operativo suspende automáticamente los procesos que usan multiplicaciones concurrentes.

d.

Únicamente para forzar que _T1_ se ejecute siempre antes que _T2_.

#### Retroalimentación

La respuesta correcta es: Para evitar lecturas o escrituras entrelazadas no atómicas sobre _x_.

#### Pregunta 10

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el problema del Productor-Consumidor con buffer limitado, ¿qué sucede si el consumidor comprueba que el buffer está vacío y se queda esperando dentro de la sección crítica sin liberar el cerrojo?

Pregunta 10Seleccione una:

a.

El buffer amplía dinámicamente su capacidad para resolver la condición.

b.

El consumidor consumirá elementos nulos sin generar consecuencias adversas.

c.

Se produce un interbloqueo (_deadlock_), pues el productor no puede entrar a insertar elementos para que se cumpla la condición.

¡Correcto! El consumidor retiene el cerrojo del buffer, impidiendo que el productor añada datos.

d.

El sistema operativo expulsa automáticamente al consumidor para permitir el paso al productor.

#### Retroalimentación

La respuesta correcta es: Se produce un interbloqueo (_deadlock_), pues el productor no puede entrar a insertar elementos para que se cumpla la condición.

#### Pregunta 11

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En un sistema de procesamiento por etapas (_pipeline_), la tarea _B_ requiere como entrada indispensable los datos procesados previamente por la tarea _A_. ¿Qué tipo de sincronización se requiere principalmente?

Pregunta 11Seleccione una:

a.

Sincronización de memoria caché local.

b.

No se requiere sincronización si las tareas corren en hilos separados.

c.

Exclusión mutua pura sin dependencias.

d.

Sincronización de control.

¡Correcto! Se coordina el orden de ejecución y la secuencia temporal entre tareas dependientes.

#### Retroalimentación

La respuesta correcta es: Sincronización de control.

#### Pregunta 12

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Dos bloques de código en hilos distintos modifican la misma variable compartida _y_: uno realiza `y = y + 1` y el otro `y = y - 1`. ¿Cómo se definen estas regiones en relación al concepto de sección crítica?

Pregunta 12Seleccione una:

a.

Constituyen dos secciones críticas completamente independientes gestionadas por distintos mutexes.

b.

No se consideran regiones críticas porque una suma y la otra resta, cancelándose el efecto.

c.

Son dos regiones críticas que pertenecen a la misma sección crítica asociada al recurso compartido _y_.

¡Correcto! La sección crítica se define alrededor del recurso que necesita protección.

d.

Solo el incremento es una región crítica; el decremento es una operación no bloqueante.

#### Retroalimentación

La respuesta correcta es: Son dos regiones críticas que pertenecen a la misma sección crítica asociada al recurso compartido _y_.

#### Pregunta 13

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En Java, ¿qué ocurre si un hilo intenta invocar el método `wait()` o `notify()` sobre un objeto sin haber obtenido previamente su bloqueo mediante un bloque o método `synchronized`?

Pregunta 13Seleccione una:

a.

El objeto adquiere automáticamente el cerrojo de forma implícita sin advertencias.

b.

El hilo entra en un estado zombi no recuperable por el sistema operativo.

c.

El código no compila generando un error de tipado estático.

d.

Se produce una excepción de tipo `IllegalMonitorStateException` en tiempo de ejecución.

¡Correcto! Para interactuar con los métodos de monitor de un objeto en Java es imprescindible ser el propietario del cerrojo.

#### Retroalimentación

La respuesta correcta es: Se produce una excepción de tipo `IllegalMonitorStateException` en tiempo de ejecución.

#### Pregunta 14

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Por qué el mecanismo de suspensión y notificación es más eficiente que el bucle de espera activa (_busy waiting_ / spinlock) al esperar una condición de sincronización prolongada?

Pregunta 14Seleccione una:

a.

Porque el hilo suspendido cede el procesador, evitando el consumo inútil de ciclos de CPU mientras espera la condición.

¡Correcto! El hilo pasa a estado bloqueado y no gasta tiempo de computación.

b.

Porque la espera activa satura la memoria secundaria liberando excesiva CPU.

c.

Porque el compilador prohíbe la inclusión de bucles condicionales dentro de programas concurrentes.

d.

Porque la suspensión garantiza que el hilo se ejecute siempre con la máxima prioridad del planificador.

#### Retroalimentación

La respuesta correcta es: Porque el hilo suspendido cede el procesador, evitando el consumo inútil de ciclos de CPU mientras espera la condición.

#### Pregunta 15

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Considere dos procesos _PA_ y _PB_ que modifican un mismo archivo compartido de registro. Si _E(PA) = {log.txt}_ y _E(PB) = {log.txt}_, ¿qué condición de Bernstein no se cumple?

Pregunta 15Seleccione una:

a.

Independencia de flujo de instrucciones.

b.

Independencia de entrada exclusiva.

c.

Independencia de salida (_E(PA) ∩ E(PB) = ∅_).

¡Correcto! Ambos escriben sobre el mismo recurso, pudiendo sobrescribir sus salidas.

d.

Se cumplen todas las condiciones si el archivo se abre en modo append.

#### Retroalimentación

La respuesta correcta es: Independencia de salida (_E(PA) ∩ E(PB) = ∅_).

#### Pregunta 16

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si dos procesos _P1_ y _P2_ cumplen que _L(P1) ∩ E(P2) ≠ ∅_, ¿cuál es la consecuencia directa según el Teorema de Bernstein?

Pregunta 16Seleccione una:

a.

Se viola la independencia de entrada, exigiendo sincronización de acceso para evitar que _P1_ lea datos mientras _P2_ los modifica.

¡Correcto! Existe un solapamiento entre la lectura de uno y la escritura del otro.

b.

Ambos procesos pueden ejecutarse concurrentemente sin ningún tipo de sincronización.

c.

Se produce una violación estricta de la independencia de salida.

d.

Se garantiza la ausencia total de condiciones de carrera.

#### Retroalimentación

La respuesta correcta es: Se viola la independencia de entrada, exigiendo sincronización de acceso para evitar que _P1_ lea datos mientras _P2_ los modifica.

#### Pregunta 17

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Sean dos conjuntos de instrucciones _S1_ y _S2_ con los siguientes conjuntos de lectura y escritura:  
_L(S1) = {a, b}_, _E(S1) = {c}_  
_L(S2) = {c, d}_, _E(S2) = {e}_  
¿Qué condición del Teorema de Bernstein se viola impidiendo su ejecución concurrente sin sincronización?

Pregunta 17Seleccione una:

a.

Se cumplen todas las condiciones y pueden ejecutarse en paralelo de forma segura.

b.

La condición de independencia de salida (_E(S1) ∩ E(S2) = ∅_).

c.

La condición simétrica de lectura (_L(S1) ∩ E(S2) = ∅_).

d.

La condición de independencia de flujo de datos (_E(S1) ∩ L(S2) = ∅_).

¡Correcto! _E(S1) ∩ L(S2) = {c} ≠ ∅_, por lo que _S2_ depende de los datos producidos por _S1_.

#### Retroalimentación

La respuesta correcta es: La condición de independencia de flujo de datos (_E(S1) ∩ L(S2) = ∅_).

#### Pregunta 18

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si dos procesos _S1_ y _S2_ tienen los siguientes conjuntos de variables:  
_L(S1) = {x}_, _E(S1) = {y}_  
_L(S2) = {z}_, _E(S2) = {w}_  
¿Qué se concluye según el Teorema de Bernstein?

Pregunta 18Seleccione una:

a.

Se produce una condición de carrera sobre el bus de memoria impidiendo el paralelismo real.

b.

Requieren obligatoriamente un mutex para proteger la variable _y_ del proceso _S2_.

c.

No pueden ejecutarse en paralelo porque sus conjuntos no comparten memoria de sincronización.

d.

Se cumplen simultáneamente las tres condiciones de independencia y pueden ejecutarse en paralelo de forma segura sin sincronización adicional.

¡Correcto! Todas las intersecciones entre conjuntos de lectura y escritura son vacías.

#### Retroalimentación

La respuesta correcta es: Se cumplen simultáneamente las tres condiciones de independencia y pueden ejecutarse en paralelo de forma segura sin sincronización adicional.

#### Pregunta 19

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué es la contención por bloqueo (_lock contention_) y qué impacto produce en un sistema concurrente?

Pregunta 19Seleccione una:

a.

Es la competencia de varios hilos por un mismo bloqueo, que degrada el rendimiento al suspender o bloquear hilos en espera.

¡Correcto! Los hilos bloqueados no pueden realizar trabajo útil mientras esperan la liberación del recurso.

b.

Es la corrupción irrecuperable de la tabla de hilos en el kernel del sistema operativo.

c.

Es una técnica de optimización que acelera la ejecución concurrente eliminando los cerrojos.

d.

Es un fallo del hardware en el que dos hilos acceden al mismo registro físico simultáneamente.

#### Retroalimentación

La respuesta correcta es: Es la competencia de varios hilos por un mismo bloqueo, que degrada el rendimiento al suspender o bloquear hilos en espera.

#### Pregunta 20

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué condición de sincronización debe verificarse y cumplirse para que un hilo productor pueda depositar de forma segura un nuevo elemento en un buffer acotado de capacidad _N_?

Pregunta 20Seleccione una:

a.

Que el hilo consumidor se encuentre activo en la CPU en ese instante.

b.

Que el buffer esté completamente vacío (número de elementos = 0).

c.

Que el buffer no esté lleno (número de elementos < _N_).

¡Correcto! Si está lleno, debe suspenderse hasta que el consumidor extraiga al menos un elemento.

d.

Que no existan hilos consumidores registrados en la aplicación.

#### Retroalimentación

La respuesta correcta es: Que el buffer no esté lleno (número de elementos < _N_).