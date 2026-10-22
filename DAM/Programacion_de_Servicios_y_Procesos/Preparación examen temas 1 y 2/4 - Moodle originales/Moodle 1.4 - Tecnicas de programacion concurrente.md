# Cuestionario del apartado 1-4

##### Estado

Finalizado

##### Comenzado

domingo, 11 de octubre de 2026, 19:30

##### Completado

domingo, 11 de octubre de 2026, 19:35

##### Duración

4 minutos 8 segundos

##### Puntos

20,00/20,00

##### Calificación

**10,00** de 10,00 (**100**%)

#### Pregunta 1

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué concepto define la propiedad de que solo un proceso pueda entrar a su sección crítica a la vez?

Pregunta 1Seleccione una:

a.

Exclusión mutua.

¡Correcto! La exclusión mutua asegura que ningún otro hilo o proceso ingrese a la sección crítica mientras está ocupada.

b.

Inanición involuntaria.

c.

Prioridad dinámica estricta.

d.

Paralelismo temporal asíncrono.

#### Retroalimentación

La exclusión mutua es el principio fundamental que garantiza que ningún otro proceso pueda ejecutar su sección crítica mientras uno ya se encuentra en ella.

La respuesta correcta es: Exclusión mutua.

#### Pregunta 2

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué arquitectura de hardware caracteriza principalmente a la programación paralela en entornos SMP?

Pregunta 2Seleccione una:

a.

Nodos heterogéneos sin posibilidad de compartir bus de datos ni reloj.

b.

Un único procesador mononúcleo con memoria virtual segmentada.

c.

Múltiples núcleos de procesamiento que comparten la memoria principal.

¡Correcto! SMP consiste en sistemas con múltiples procesadores/núcleos y un espacio de memoria física compartida.

d.

Múltiples servidores independientes interconectados exclusivamente mediante switches de red.

#### Retroalimentación

Los entornos SMP (Symmetric Multiprocessing) se definen por tener múltiples núcleos o procesadores que comparten la misma memoria principal física.

La respuesta correcta es: Múltiples núcleos de procesamiento que comparten la memoria principal.

#### Pregunta 3

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué componente del sistema operativo gestiona la competencia por la CPU entre procesos independientes?

Pregunta 3Seleccione una:

a.

El compilador JIT (Just-In-Time).

b.

El gestor de sockets de red.

c.

El planificador de procesos (scheduler).

¡Correcto! El scheduler asigna los cuantos de tiempo de CPU a cada proceso de forma equitativa o por prioridades.

d.

El recolector de basura (Garbage Collector).

#### Retroalimentación

El planificador de procesos (scheduler) se encarga de repartir el tiempo de CPU entre los diferentes procesos según prioridades y políticas de reparto.

La respuesta correcta es: El planificador de procesos (scheduler).

#### Pregunta 4

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Por qué la sincronización de procesos es indispensable cuando se tienen procesos competidores?

Pregunta 4Seleccione una:

a.

Para apagar los núcleos sobrantes del procesador durante la ejecución de las tareas.

b.

Para reducir automáticamente el uso total de memoria física del sistema operativo a cero.

c.

Para permitir que todos los procesos escriban a la vez en la misma dirección de memoria.

d.

Para garantizar el acceso mutuamente excluyente al recurso crítico.

¡Correcto! La sincronización evita que dos procesos modifiquen simultáneamente el recurso común no compartible.

#### Retroalimentación

Sin sincronización, los procesos competidores podrían acceder de forma solapada a recursos no compartibles (secciones críticas), causando inconsistencia y estados corruptos.

La respuesta correcta es: Para garantizar el acceso mutuamente excluyente al recurso crítico.

#### Pregunta 5

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué estructura de datos intermedia se utiliza comúnmente para desacoplar el ritmo de ejecución entre un proceso productor y uno consumidor?

Pregunta 5Seleccione una:

a.

Un buffer compartido.

¡Correcto! El buffer almacena temporalmente los elementos permitiendo que productor y consumidor operen a velocidades variables.

b.

Un registro de instrucciones de la ALU.

c.

Un archivo de swap de paginación obligatorio.

d.

Una partición física MBR del disco duro.

#### Retroalimentación

Un buffer compartido (generalmente una cola o array circular) absorbe las diferencias de velocidad entre el emisor (productor) y el receptor (consumidor).

La respuesta correcta es: Un buffer compartido.

#### Pregunta 6

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se clasifica un servidor web que recibe peticiones HTTP y asigna cada una a un hilo de procesamiento para mantener la interfaz o escucha atenta?

Pregunta 6Seleccione una:

a.

Aplicación con programación concurrente.

¡Correcto! Representa el ejemplo clásico de programación concurrente general para gestionar múltiples tareas y entradas/salidas.

b.

Simulación científica masivamente paralela.

c.

Aplicación puramente secuencial y monolítica.

d.

Sistema embebido en tiempo real estricto (hard real-time).

#### Retroalimentación

Un servidor web multitarea gestiona múltiples tareas de atención al cliente concurrentemente (concurrencia general), garantizando responsividad y reparto de atención.

La respuesta correcta es: Aplicación con programación concurrente.

#### Pregunta 7

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué factor incrementa significativamente la complejidad de los sistemas distribuidos respecto a los de memoria compartida?

Pregunta 7Seleccione una:

a.

La necesidad de sincronizar el acceso al bus PCI de una placa base local.

b.

La imposibilidad de ejecutar procesos concurrentes en un mismo nodo.

c.

Que los programas deben compilarse forzosamente en código ensamblador.

d.

La gestión de latencias de red, heterogeneidad y fallos parciales.

¡Correcto! La red añade latencia no determinista y posibilidades de desconexión o caída parcial de nodos.

#### Retroalimentación

Los sistemas distribuidos deben lidiar con latencias de comunicación variables, heterogeneidad en los nodos y la posibilidad de fallos parciales de red o de máquinas.

La respuesta correcta es: La gestión de latencias de red, heterogeneidad y fallos parciales.

#### Pregunta 8

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En la simulación científica de dinámica de fluidos dividida en cuadrículas ejecutadas en un supercomputador SMP, ¿qué paradigma se aplica principalmente?

Pregunta 8Seleccione una:

a.

Procesamiento por lotes (batch) monofásico mononúcleo.

b.

Programación basada exclusivamente en eventos de usuario GUI.

c.

Programación paralela.

¡Correcto! Explotar múltiples núcleos de un sistema SMP para acelerar un cálculo intensivo dividiendo subtareas simultáneas es programación paralela.

d.

Programación secuencial síncrona en un hilo.

#### Retroalimentación

Se trata de programación paralela: el problema de cálculo intensivo se descompone en bloques para ejecutarse a la vez en múltiples núcleos de memoria compartida con el fin de acelerar el cálculo.

La respuesta correcta es: Programación paralela.

#### Pregunta 9

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué diferencia fundamental existe entre un sistema con memoria compartida y uno con memoria distribuida?

Pregunta 9Seleccione una:

a.

Que la memoria distribuida no permite la ejecución concurrente de código.

b.

La velocidad del reloj de los procesadores, que debe ser siempre idéntica en memoria distribuida.

c.

Que en memoria compartida no se pueden usar variables booleanas ni enteros.

d.

El acceso directo a una misma RAM física frente a memorias locales por nodo.

¡Correcto! En memoria compartida todos los procesadores acceden al mismo espacio de RAM; en distribuida, cada nodo tiene su memoria local y se requiere red.

#### Retroalimentación

En los sistemas de memoria compartida todos los procesadores leen y escriben en un espacio físico global de RAM, mientras que en memoria distribuida cada nodo posee su propia RAM privada y se comunica por red.

La respuesta correcta es: El acceso directo a una misma RAM física frente a memorias locales por nodo.

#### Pregunta 10

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el mecanismo primordial de comunicación en la programación distribuida?

Pregunta 10Seleccione una:

a.

Llamadas atómicas a registros de CPU compartidos.

b.

Intercambio de mensajes a través de una red de comunicaciones.

¡Correcto! Al no haber memoria común, los mensajes por red son el mecanismo imprescindible.

c.

Señales hardware directas en la placa base.

d.

Variables globales ubicadas en la memoria RAM compartida.

#### Retroalimentación

Dado que los nodos en un sistema distribuido tienen memorias locales independientes, la comunicación y coordinación se realiza necesariamente mediante intercambio de mensajes a través de la red.

La respuesta correcta es: Intercambio de mensajes a través de una red de comunicaciones.

#### Pregunta 11

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuándo se considera que dos o más procesos están en interacción de competencia?

Pregunta 11Seleccione una:

a.

Cuando se ejecutan en diferentes ordenadores conectados por un switch.

b.

Cuando ambos procesos pertenecen a usuarios que no tienen permisos de administrador.

c.

Cuando intentan acceder simultáneamente a un recurso no compartible.

¡Correcto! La necesidad de acceder a recursos compartidos que exigen exclusión mutua define la relación de competencia.

d.

Cuando uno lee los mensajes que el otro ha colocado en una cola intencionadamente.

#### Retroalimentación

Se produce competencia cuando varios procesos necesitan acceder a un recurso compartido que no admite uso simultáneo (requiere acceso mutuamente excluyente).

La respuesta correcta es: Cuando intentan acceder simultáneamente a un recurso no compartible.

#### Pregunta 12

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué patrón clásico de concurrencia ejemplifica la interacción de procesos cooperantes?

Pregunta 12Seleccione una:

a.

Patrón Singleton mono-hilo.

b.

Particionamiento estático sin comunicación.

c.

Patrón Productor-Consumidor.

¡Correcto! En este patrón, el productor genera elementos y el consumidor los procesa, colaborando a través de un canal intermedio.

d.

Inversión de dependencias desacoplada.

#### Retroalimentación

El patrón Productor-Consumidor es el arquetipo de procesos cooperantes: un proceso genera datos y los deposita en un buffer para que otro los consuma.

La respuesta correcta es: Patrón Productor-Consumidor.

#### Pregunta 13

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la característica principal que distingue a la programación concurrente en general de la programación paralela?

Pregunta 13Seleccione una:

a.

Únicamente se puede aplicar en sistemas monoprocesador sin memoria compartida.

b.

Requiere obligatoriamente una red de ordenadores conectados para intercambiar mensajes.

c.

Garantiza que todas las tareas se ejecuten exactamente al mismo instante de tiempo físico.

d.

Gestiona la ejecución entrelazada o simultánea de múltiples tareas para optimizar recursos o reparto de tiempo, sin requerir obligatoriamente múltiples núcleos.

¡Correcto! La concurrencia es el concepto general de estructurar un programa en tareas que pueden solaparse o entrelazarse en el tiempo.

#### Retroalimentación

La programación concurrente gestiona tareas que pueden ejecutarse de forma entrelazada o simultánea, mientras que la programación paralela busca explícitamente acelerar la ejecución mediante paralelismo real en arquitecturas multiprocesador (SMP).

La respuesta correcta es: Gestiona la ejecución entrelazada o simultánea de múltiples tareas para optimizar recursos o reparto de tiempo, sin requerir obligatoriamente múltiples núcleos.

#### Pregunta 14

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo se caracterizan los procesos independientes en un sistema multitarea?

Pregunta 14Seleccione una:

a.

Requieren tuberías (pipes) para sincronizar su inicio y fin.

b.

Modifican de forma coordinada las mismas variables globales en memoria.

c.

No comparten recursos directamente ni se comunican entre sí.

¡Correcto! Cada proceso ejecuta su flujo de forma aislada sin interacción deliberada con los demás.

d.

Comparten obligatoriamente el mismo espacio de direccionamiento virtual.

#### Retroalimentación

Los procesos independientes ejecutan tareas aisladas, sin comunicarse ni compartir recursos directamente, interfiriendo solo de manera indirecta en la contención por el hardware (CPU/memoria).

La respuesta correcta es: No comparten recursos directamente ni se comunican entre sí.

#### Pregunta 15

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la finalidad esencial de la relación entre procesos cooperantes?

Pregunta 15Seleccione una:

a.

Evitar cualquier tipo de comunicación para reducir la sobrecarga del sistema.

b.

Impedir que el sistema operativo suspenda la ejecución de sus hilos.

c.

Trabajar conjuntamente intercambiando datos para una tarea común.

¡Correcto! La cooperación busca combinar el trabajo de varios procesos para conseguir un fin común mediante comunicación.

d.

Bloquear la ejecución de otros procesos para ganar tiempo de procesador.

#### Retroalimentación

Los procesos cooperantes están diseñados para colaborar en la resolución de una tarea común mediante el intercambio de información y servicios.

La respuesta correcta es: Trabajar conjuntamente intercambiando datos para una tarea común.

#### Pregunta 16

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué problema grave ocurre cuando dos procesos quedan bloqueados indefinidamente esperando cada uno un recurso que posee el otro?

Pregunta 16Seleccione una:

a.

Fallo de página de disco (Page Fault).

b.

Fragmentación externa de memoria.

c.

Interbloqueo (Deadlock).

¡Correcto! El deadlock es el estado donde ninguno de los procesos implicados puede continuar su ejecución por la retención y espera circular.

d.

Desbordamiento de pila (Stack Overflow).

#### Retroalimentación

El interbloqueo o deadlock ocurre cuando existe una espera circular donde dos o más procesos retienen recursos y quedan esperando los que poseen los demás, impidiendo su avance.

La respuesta correcta es: Interbloqueo (Deadlock).

#### Pregunta 17

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el contexto de interacciones entre procesos, ¿por qué los procesos independientes no requieren mecanismos explícitos de sincronización de usuario?

Pregunta 17Seleccione una:

a.

Porque los procesos independientes solo funcionan en ordenadores apagados.

b.

Porque el SO aísla sus espacios de memoria y recursos.

¡Correcto! El aislamiento de memoria y recursos provisto por el sistema operativo impide que sus estados internos colisionen.

c.

Porque se ejecutan siempre a través del mismo hilo principal.

d.

Porque la JVM prohíbe la multiprogramación en sistemas operativos modernos.

#### Retroalimentación

Dado que el SO aísla el espacio de direcciones de memoria de cada proceso y gestiona sus recursos, no existe riesgo de corrupción directa de datos de aplicación entre procesos independientes.

La respuesta correcta es: Porque el SO aísla sus espacios de memoria y recursos.

#### Pregunta 18

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué riesgo directo surge si varios procesos competidores modifican una variable compartida sin sincronización?

Pregunta 18Seleccione una:

a.

Condición de carrera e inconsistencia de datos.

¡Correcto! Sin exclusión mutua, las modificaciones concurrentes provocan escrituras inconsistentes y pérdidas de actualizaciones.

b.

Reinicio instantáneo del hardware de la placa base.

c.

Aceleración espontánea del tiempo de cálculo en la CPU.

d.

Duplicación física de la memoria RAM del equipo.

#### Retroalimentación

El entrelazado incontrolado de instrucciones de lectura y escritura concurrentes genera condiciones de carrera (race conditions) e inconsistencia en los datos resultantes.

La respuesta correcta es: Condición de carrera e inconsistencia de datos.

#### Pregunta 19

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Una tubería (pipeline) en un sistema operativo Unix/Linux, donde la salida de un proceso se conecta a la entrada de otro, es un ejemplo de:

Pregunta 19Seleccione una:

a.

Sistemas distribuidos en malla sin conexión física.

b.

Procesos cooperantes.

¡Correcto! Los procesos colaboran pasándose datos ordenadamente para resolver una tarea compuesta.

c.

Procesos en competencia destructiva por el bus de direcciones.

d.

Procesos independientes sin interacción.

#### Retroalimentación

Es un ejemplo paradigmático de procesos cooperantes, ya que un proceso colabora con el siguiente pasándole el flujo de datos para completar conjuntamente una tarea.

La respuesta correcta es: Procesos cooperantes.

#### Pregunta 20

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es el objetivo primario de la programación paralela?

Pregunta 20Seleccione una:

a.

Acelerar la ejecución dividiendo tareas en subtareas simultáneas.

¡Correcto! Su meta principal es el rendimiento y la reducción del tiempo de ejecución (speedup).

b.

Permitir que un solo núcleo atienda múltiples hilos por turno de tiempo.

c.

Gestionar la interfaz de usuario para que no se congele durante operaciones de E/S.

d.

Tolerar caídas de servidores en centros de datos remotos.

#### Retroalimentación

El fin primordial de la programación paralela es reducir el tiempo total de cómputo dividiendo el problema en subtareas ejecutadas simultáneamente en múltiples núcleos.

La respuesta correcta es: Acelerar la ejecución dividiendo tareas en subtareas simultáneas.