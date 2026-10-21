# Cuestionario del apartado 1-8

##### Estado

Finalizado

##### Comenzado

domingo, 11 de octubre de 2026, 19:50

##### Completado

domingo, 11 de octubre de 2026, 19:55

##### Duración

4 minutos 49 segundos

##### Puntos

20,00/20,00

##### Calificación

**10,00** de 10,00 (**100**%)

#### Pregunta 1

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La Respuesta Pregunta 1 es la propiedad de viveza que se vulnera cuando a un proceso o hilo se le priva indefinidamente del acceso a un recurso necesario porque el planificador o sistema se lo concede sistemáticamente a otros.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Condición en la que un proceso 'muere de hambre' por falta de acceso a recursos.

La respuesta correcta es: inanición

#### Pregunta 2

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La condición de Coffman denominada Respuesta Pregunta 2 establece que un recurso adquirido por un proceso solo puede ser liberado voluntariamente por él mismo una vez finalizada su tarea, sin que el sistema operativo pueda forzar su liberación.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Traducción del término en inglés 'No Preemption'.

La respuesta correcta es: no apropiación

#### Pregunta 3

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un semáforo contador se inicializa en 0. Si un hilo ejecuta la operación atómica `acquire()` sobre dicho semáforo, ¿cuál será el comportamiento del sistema?

Pregunta 3Respuesta

a.

El hilo detecta que el contador es 0, se bloquea y pasa a estado de espera hasta que otro hilo invoque `release()`.

b.

Se genera de inmediato un error de ejecución del tipo `IllegalThreadStateException`.

c.

El hilo decrementa automáticamente el valor del semáforo a -1 y continúa su ejecución de inmediato.

d.

El semáforo se reinicia a su valor máximo permitido y despierta a todos los hilos del proceso.

#### Retroalimentación

Respuesta correcta

Al valer 0 el semáforo, `acquire()` no puede decrementar la variable y suspende al hilo solicitante hasta que haya unidades disponibles.

La respuesta correcta es: El hilo detecta que el contador es 0, se bloquea y pasa a estado de espera hasta que otro hilo invoque `release()`.

#### Pregunta 4

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La Respuesta Pregunta 4 de prioridad ocurre cuando una tarea de baja prioridad bloquea un recurso necesitado por una tarea de alta prioridad, y a su vez una tarea de prioridad media desaloja a la de baja prioridad, retrasando a la de alta prioridad.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Fenómeno donde el orden de atención de prioridades queda 'al revés'.

La respuesta correcta es: inversión

#### Pregunta 5

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En un sistema de planificación por prioridades estáticas sin mecanismos de equidad, ¿qué situación conduce directamente a la inanición de una tarea de baja prioridad?

Pregunta 5Respuesta

a.

La adquisición de un monitor por parte de una tarea que completa su método y sale inmediatamente.

b.

La creación de una dependencia de recursos en orden estricto descendente.

c.

El uso de la herencia de prioridad entre tareas de baja y alta prioridad.

d.

La presencia constante y continuada de tareas de mayor prioridad listas para ejecutarse.

#### Retroalimentación

Respuesta correcta

Al haber siempre tareas de mayor prioridad listas, el planificador nunca concede el tiempo de CPU a la tarea de baja prioridad, dejándola en inanición.

La respuesta correcta es: La presencia constante y continuada de tareas de mayor prioridad listas para ejecutarse.

#### Pregunta 6

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el lenguaje Java, ¿cómo se implementa el concepto de monitor para garantizar tanto la exclusión mutua implícita como la sincronización condicional?

Pregunta 6Respuesta

a.

Declarando todas las variables compartidas como `volatile` sin requerir métodos bloqueantes.

b.

A través de la interfaz `Runnable` acoplada con bucles de espera activa sobre números enteros.

c.

Utilizando exclusivamente la clase `Thread` y modificando su prioridad de forma dinámica.

d.

Mediante la palabra clave `synchronized` para la exclusión mutua, combinada con los métodos `wait()`, `notify()` y `notifyAll()`.

#### Retroalimentación

Respuesta correcta

En Java, los bloques o métodos `synchronized` actúan como monitores implícitos, y la sincronización condicional se gestiona con `wait()` y las notificaciones.

La respuesta correcta es: Mediante la palabra clave `synchronized` para la exclusión mutua, combinada con los métodos `wait()`, `notify()` y `notifyAll()`.

#### Pregunta 7

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Para evitar la condición de Coffman de 'espera circular' en la gestión de múltiples recursos compartidos, ¿cuál es la técnica de prevención más habitual?

Pregunta 7Respuesta

a.

Asignar siempre prioridades dinámicas basadas únicamente en la velocidad de la CPU.

b.

Eliminar la exclusión mutua de todos los dispositivos de hardware del sistema.

c.

Permitir que los procesos mantengan bloqueados los recursos indefinidamente mediante un bucle activo.

d.

Establecer un orden jerárquico o numérico consistente para la adquisición de recursos en todas las tareas.

#### Retroalimentación

Respuesta correcta

Si se impone un orden estricto de adquisición (por ejemplo, adquirir siempre el recurso A antes que el B), se imposibilita la formación de ciclos de dependencias.

La respuesta correcta es: Establecer un orden jerárquico o numérico consistente para la adquisición de recursos en todas las tareas.

#### Pregunta 8

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿De qué manera el concepto de 'fairness' (justicia o equidad) contribuye a evitar el problema de la inanición en los algoritmos de sincronización y planificación?

Pregunta 8Respuesta

a.

Elimina por completo el uso de cerrojos de exclusión mutua en variables compartidas.

b.

Otorga siempre preferencia absoluta a las tareas de mayor prioridad para maximizar el rendimiento.

c.

Garantiza que se tenga en cuenta la antigüedad de las solicitudes para otorgar el recurso a todos los procesos eventualmente.

d.

fuerza a todos los hilos a ejecutarse en un orden estrictamente al azar.

#### Retroalimentación

Respuesta correcta

La equidad o 'fairness' asegura que ningún hilo sea postergado indefinidamente al considerar el orden o tiempo de espera de sus peticiones.

La respuesta correcta es: Garantiza que se tenga en cuenta la antigüedad de las solicitudes para otorgar el recurso a todos los procesos eventualmente.

#### Pregunta 9

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Considere tres tareas: Tarea A (alta prioridad), Tarea B (media prioridad) y Tarea C (baja prioridad). Tarea C retiene un cerrojo que Tarea A necesita, por lo que Tarea A se bloquea. Luego, Tarea B pasa a estar lista para ejecutarse. Si NO se aplica ningún mecanismo de solución, ¿qué sucede a continuación?

Pregunta 9Respuesta

a.

Tarea B se ejecuta desplazando a Tarea C; Tarea A queda indirectamente bloqueada por Tarea B hasta que B y C terminen.

b.

Tarea A desaloja inmediatamente a Tarea B y fuerza a Tarea C a liberar el recurso.

c.

Tarea C eleva automáticamente su prioridad por encima de B sin requerir ningún algoritmo especial.

d.

El sistema operativo aborta Tarea B por intentar acceder a una sección crítica ajena.

#### Retroalimentación

Respuesta correcta

Dado que Tarea B tiene mayor prioridad que Tarea C, el planificador ejecuta B. C no puede liberar el recurso y A (alta prioridad) se ve obligada a esperar indirectamente por B (media prioridad).

La respuesta correcta es: Tarea B se ejecuta desplazando a Tarea C; Tarea A queda indirectamente bloqueada por Tarea B hasta que B y C terminen.

#### Pregunta 10

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La Respuesta Pregunta 10 de prioridad es un mecanismo mediante el cual un hilo de baja prioridad sube temporalmente su nivel de prioridad para coincidir con la de un hilo de alta prioridad que está esperando por un recurso que el primero retiene.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Transferencia o adopción temporal de un nivel de prioridad superior.

La respuesta correcta es: herencia

#### Pregunta 11

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

La Respuesta Pregunta 11 es la propiedad de seguridad fundamental que garantiza que el acceso a recursos compartidos o secciones críticas sea realizado por una sola tarea a la vez para evitar condiciones de carrera.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Es el mecanismo binario que impide la entrada simultánea a una sección crítica.

La respuesta correcta es: exclusión mutua

#### Pregunta 12

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un algoritmo de gestión de recursos asigna un tiempo máximo de espera a las solicitudes de cerrojos. Si una tarea no obtiene el recurso en ese tiempo, suelta los cerrojos que ya tenía y reintenta más tarde. ¿Qué condición de Coffman está atacando directamente para evitar deadlocks?

Pregunta 12Respuesta

a.

Exclusión mutua.

b.

Retención y espera (Hold and Wait).

c.

Inversión de prioridad.

d.

No apropiación.

#### Retroalimentación

Respuesta correcta

Al liberar los recursos previamente adquiridos en caso de fallo o expiración de tiempo, la tarea deja de 'retener mientras espera', rompiendo la condición.

La respuesta correcta es: Retención y espera (Hold and Wait).

#### Pregunta 13

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un sistema concurrente debe gestionar el acceso a un recurso compartido del cual existen exactamente 5 instancias idénticas disponibles simultáneamente. ¿Qué primitiva de sincronización es la más adecuada para controlar este acceso?

Pregunta 13Respuesta

a.

Una variable booleana consultada mediante un bucle de espera activa.

b.

Un mutex binario, configurado para alternar entre 5 estados de desbloqueo.

c.

Un monitor sin variables de condición.

d.

Un semáforo general o contador, inicializado con el valor 5.

#### Retroalimentación

Respuesta correcta

Un semáforo general permite controlar el acceso a un número específico de instancias simultáneas de un recurso mediante decrementos e incrementos atómicos de su valor entero.

La respuesta correcta es: Un semáforo general o contador, inicializado con el valor 5.

#### Pregunta 14

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el contexto de los programas concurrentes, ¿cuál es la diferencia fundamental en la naturaleza de lo que garantizan las propiedades de seguridad frente a las propiedades de viveza?

Pregunta 14Respuesta

a.

Las propiedades de seguridad especifican 'lo que no debe ocurrir' para evitar estados incorrectos, mientras que las de viveza especifican 'lo que debe ocurrir' para garantizar el progreso.

b.

Las propiedades de seguridad dependen de las políticas del planificador del sistema operativo, mientras que las de viveza dependen exclusivamente de cerrojos binarios.

c.

Las propiedades de seguridad aplican únicamente a sistemas distribuidos, mientras que las de viveza aplican a la programación multihilo local.

d.

Las propiedades de seguridad garantizan la velocidad de ejecución, mientras que las de viveza previenen condiciones de carrera en variables globales.

#### Retroalimentación

Respuesta correcta

Las propiedades de seguridad previenen estados inconsistentes o indeseables (como condiciones de carrera), mientras que las de viveza aseguran que el programa avance hacia la consecución de sus objetivos sin quedarse estancado.

La respuesta correcta es: Las propiedades de seguridad especifican 'lo que no debe ocurrir' para evitar estados incorrectos, mientras que las de viveza especifican 'lo que debe ocurrir' para garantizar el progreso.

#### Pregunta 15

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El Respuesta Pregunta 15 pasivo es una situación en la que dos o más procesos se encuentran suspendidos indefinidamente esperando mutuamente la liberación de recursos retenidos por los demás.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

También se conoce históricamente como el 'abrazo mortal'.

La respuesta correcta es: interbloqueo

#### Pregunta 16

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El Respuesta Pregunta 16 es una situación de falta de viveza en la que varios procesos se encuentran en ejecución activa y cambiando de estado en un bucle continuo de reintentos, pero sin realizar ningún progreso efectivo.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Se contrapone al interbloqueo pasivo.

La respuesta correcta es: bloqueo activo

#### Pregunta 17

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando un hilo se encuentra dentro de una sección crítica protegida por exclusión mutua y necesita esperar a que se cumpla una condición de sincronización, ¿por qué debe liberar el mecanismo de exclusión mutua mientras espera?

Pregunta 17Respuesta

a.

Para que el planificador de la máquina virtual aumente inmediatamente la prioridad de la tarea en espera.

b.

Para evitar un interbloqueo pasivo (deadlock), permitiendo que otros hilos accedan al recurso y puedan hacer cumplir la condición requerida.

c.

Para evitar que el semáforo contador tome valores negativos no permitidos.

d.

Para transformar la comunicación síncrona en un canal símplex de mayor velocidad.

#### Retroalimentación

Respuesta correcta

Si el hilo retuviera la exclusión mutua mientras espera, impediría que el hilo responsable de modificar y cumplir la condición pueda entrar a la sección crítica.

La respuesta correcta es: Para evitar un interbloqueo pasivo (deadlock), permitiendo que otros hilos accedan al recurso y puedan hacer cumplir la condición requerida.

#### Pregunta 18

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿De qué manera la 'herencia de prioridad' resuelve el problema de la inversión de prioridad?

Pregunta 18Respuesta

a.

Asigna el recurso solicitado a la tarea de mayor prioridad eliminando el progreso realizado por la de baja prioridad.

b.

Disminuye la prioridad de la tarea de prioridad media a cero hasta que la tarea de alta prioridad finalice.

c.

Obliga a la tarea de alta prioridad a ejecutar su sección crítica sin adquirir el cerrojo de exclusión mutua.

d.

Hace que la tarea de baja prioridad que retiene el recurso herede temporalmente la prioridad de la tarea de alta prioridad que está bloqueada.

#### Retroalimentación

Respuesta correcta

Al elevar temporalmente la prioridad de C al nivel de A, C no puede ser interrumpida por tareas de prioridad media (como B), liberando el recurso lo antes posible.

La respuesta correcta es: Hace que la tarea de baja prioridad que retiene el recurso herede temporalmente la prioridad de la tarea de alta prioridad que está bloqueada.

#### Pregunta 19

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Se desea prevenir la aparición de deadlocks eliminando la condición de Coffman conocida como 'retención y espera' (Hold and Wait). ¿Qué estrategia de diseño permite romper esta condición?

Pregunta 19Respuesta

a.

Obligar a que cada proceso solicite y obtenga todos los recursos que necesita de una sola vez antes de iniciar su ejecución.

b.

Permitir que el sistema operativo expropie o quite forzosamente recursos a cualquier proceso bloqueado.

c.

Garantizar que todos los recursos compartidos sean leídos de forma asíncrona sin exclusión mutua.

d.

Establecer una jerarquía global u ordenamiento numérico estricto en la adquisición de recursos.

#### Retroalimentación

Respuesta correcta

Si un proceso obtiene todos los recursos simultáneamente antes de comenzar, nunca retendrá recursos mientras espera otros adicionales, rompiendo 'Hold and Wait'.

La respuesta correcta es: Obligar a que cada proceso solicite y obtenga todos los recursos que necesita de una sola vez antes de iniciar su ejecución.

#### Pregunta 20

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al analizar una aplicación concurrente, se detecta que dos hilos están consumiendo el 100% del procesador cambiando constantemente el valor de sus variables, pero sin lograr avanzar en el procesamiento de sus datos. ¿Qué problema presenta la aplicación?

Pregunta 20Respuesta

a.

Violación del principio de exclusión mutua.

b.

Interbloqueo pasivo (deadlock).

c.

Inversión de prioridad no gestionada.

d.

Interbloqueo activo (livelock).

#### Retroalimentación

Respuesta correcta

En el livelock, los hilos permanecen activos y ejecutando código (cambiando de estado en bucles de reintento), pero son incapaces de realizar progreso efectivo hacia su meta.

La respuesta correcta es: Interbloqueo activo (livelock).