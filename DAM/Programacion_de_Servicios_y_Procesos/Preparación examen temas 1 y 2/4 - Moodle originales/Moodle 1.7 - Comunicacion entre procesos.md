# Cuestionario del apartado 1-7

##### Estado

Finalizado

##### Comenzado

domingo, 11 de octubre de 2026, 19:44

##### Completado

domingo, 11 de octubre de 2026, 19:49

##### Duración

4 minutos 51 segundos

##### Puntos

18,00/19,00

##### Calificación

**9,47** de 10,00 (**94,74**%)

#### Pregunta 1

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En el modelo de comunicación a través de Respuesta Pregunta 1, las tareas concurrentes comparten un espacio de memoria principal común, lo que requiere mecanismos de sincronización explícitos para evitar condiciones de carrera.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Identifica el paradigma típico de la programación multihilo en un mismo proceso donde los datos residen en un espacio común.

La respuesta correcta es: memoria compartida

#### Pregunta 2

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Qué compromiso (trade-off) en términos de rendimiento y complejidad presenta el paso de mensajes mediante sockets de red frente al acceso a memoria compartida?

Pregunta 2Respuesta

a.

Los sockets ofrecen menor latencia que la memoria compartida, pero aumentan el peligro de condiciones de carrera directas sobre las variables del hilo remoto.

b.

Los sockets eliminan la sobrecarga de serialización a costa de requerir una región de memoria física directamente accesible por todos los ordenadores.

c.

Los sockets permiten la comunicación entre máquinas distribuidas, pero introducen mayor latencia y sobrecarga debido a la serialización de mensajes y la transmisión por red.

d.

La memoria compartida genera mayor latencia en comunicaciones locales, pero simplifica la transmisión de mensajes entre nodos físicamente separados.

#### Retroalimentación

Respuesta correcta

El paso de mensajes por red desacopla el espacio de memoria física, permitiendo la distribución geográfica, a costa de asumir el coste temporal de formatear y transmitir los datos por la red.

La respuesta correcta es: Los sockets permiten la comunicación entre máquinas distribuidas, pero introducen mayor latencia y sobrecarga debido a la serialización de mensajes y la transmisión por red.

#### Pregunta 3

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El soporte físico o lógico (como una red, un cable o una región de memoria) a través del cual se transmite un mensaje del emisor al receptor se denomina Respuesta Pregunta 3.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Es uno de los cuatro componentes básicos de la comunicación, junto al mensaje, el emisor y el receptor.

La respuesta correcta es: canal

#### Pregunta 4

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un sistema de comunicación mediante walkie-talkies o una vía estrecha de un solo carril con tráfico en ambos sentidos representan analogías de ¿qué tipo de canal según su capacidad?

Pregunta 4Respuesta

a.

Half duplex, ya que la comunicación es bidireccional pero alternante en el tiempo, impidiendo la transmisión simultánea.

b.

Full duplex, dado que permite la interacción de dos partes de forma totalmente simultánea y sin esperas.

c.

Símplex, puesto que la información fluye estrictamente en una única dirección sin posibilidad de retorno o respuesta.

d.

Invocación remota, debido a que requiere un protocolo de red cliente-servidor estrictamente síncrono.

#### Retroalimentación

Respuesta correcta

En un canal half duplex o semidúplex la información puede viajar en ambos sentidos, pero sólo un participante puede transmitir en un instante dado.

La respuesta correcta es: Half duplex, ya que la comunicación es bidireccional pero alternante en el tiempo, impidiendo la transmisión simultánea.

#### Pregunta 5

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Un canal de comunicación en el que la información fluye estrictamente en una única dirección, actuando una entidad únicamente como emisor y la otra únicamente como receptor, se denomina Respuesta Pregunta 5.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Recuerda el ejemplo de la radiodifusión o la proyección de una película en el cine.

La respuesta correcta es: simplex

#### Pregunta 6

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En la clasificación según la capacidad del canal, un canal de comunicación de tipo Respuesta Pregunta 6 permite la transmisión bidireccional y simultánea de información entre el emisor y el receptor.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Piensa en la analogía de una avenida de doble sentido con carriles separados o una conversación telefónica.

La respuesta correcta es: full duplex

#### Pregunta 7

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Al diseñar un sistema complejo, los arquitectos deciden usar memoria compartida para coordinar hilos internos y paso de mensajes para la interacción entre servidores. ¿Por qué es adecuada esta decisión según el texto?

Pregunta 7Respuesta

a.

Porque la memoria compartida es la única opción válida en sistemas distribuidos y el paso de mensajes se limita exclusivamente a hilos de un mismo hilo.

b.

Porque evita el uso de cerrojos o mutexes en la memoria local e impone canales full duplex síncronos en las máquinas remotas.

c.

Porque el paso de mensajes por red elimina la necesidad de serializar datos, mientras que la memoria compartida gestiona automáticamente la red local.

d.

Aprovecha el alto rendimiento y baja latencia de la memoria compartida a nivel local y utiliza el paso de mensajes para superar la ausencia de memoria física común entre servidores.

#### Retroalimentación

Respuesta correcta

El texto explica que en sistemas complejos se combinan ambos modelos para optimizar el rendimiento intraproceso e independizar la comunicación intermáquina.

La respuesta correcta es: Aprovecha el alto rendimiento y baja latencia de la memoria compartida a nivel local y utiliza el paso de mensajes para superar la ausencia de memoria física común entre servidores.

#### Pregunta 8

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En una red peer-to-peer (P2P), donde todos los nodos pueden actuar tanto solicitando como ofreciendo información sin una jerarquía predefinida, se manifiesta una comunicación de tipo:

Pregunta 8Respuesta

a.

Simétrica (o entre pares).

b.

Asimétrica (o cliente-servidor).

c.

Invocación remota exclusivamente local.

d.

Símplex no bloqueante.

#### Retroalimentación

Respuesta correcta

La comunicación simétrica se caracteriza por la igualdad de roles entre los interlocutores, pudiendo todos actuar como emisores y receptores.

La respuesta correcta es: Simétrica (o entre pares).

#### Pregunta 9

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿En qué se diferencian los modelos de comunicación simétrica y asimétrica según el comportamiento o rol de los interlocutores?

Pregunta 9Respuesta

a.

En la comunicación simétrica el canal es siempre half duplex, mientras que en la asimétrica debe ser obligatoriamente símplex.

b.

La comunicación asimétrica solo se puede implementar mediante memoria compartida, mientras que la simétrica requiere sockets de red.

c.

En la comunicación simétrica todos los procesos tienen el mismo rol y pueden ser emisores o receptores, mientras que en la asimétrica existen roles diferenciados de cliente y servidor.

d.

La comunicación simétrica requiere que un proceso maestro gestione la cola de mensajes, mientras que la asimétrica no utiliza servidores.

#### Retroalimentación

Respuesta correcta

En el modelo simétrico (peer-to-peer) no hay jerarquía funcional predefinida, a diferencia del modelo asimétrico donde el cliente solicita y el servidor atiende.

La respuesta correcta es: En la comunicación simétrica todos los procesos tienen el mismo rol y pueden ser emisores o receptores, mientras que en la asimétrica existen roles diferenciados de cliente y servidor.

#### Pregunta 10

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál de las siguientes afirmaciones describe una ventaja del paso de mensajes en relación con la simplificación de la programación concurrente?

Pregunta 10Respuesta

a.

Permite modificar libremente las variables del espacio de memoria privado de otro proceso sin causar condiciones de carrera.

b.

Garantiza que la latencia de transmisión a través de la red sea inferior a los accesos a la memoria búfer de la CPU.

c.

Elimina totalmente la necesidad de coordinar la lógica de negocio o la secuencia de ejecución entre las tareas.

d.

La sincronización suele estar implícita en las operaciones de envío y recepción, reduciendo la necesidad de utilizar mecanismos de sincronización explícitos a nivel de memoria.

#### Retroalimentación

Respuesta correcta

Al realizar envíos y recepciones, las primitivas gestionan internamente el acoplamiento y transferencia de datos, lo que disminuye el riesgo de errores de memoria compartida.

La respuesta correcta es: La sincronización suele estar implícita en las operaciones de envío y recepción, reduciendo la necesidad de utilizar mecanismos de sincronización explícitos a nivel de memoria.

#### Pregunta 11

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Cuando se implementa el paso de mensajes utilizando un buffer de memoria compartido (como una cola de mensajes en memoria principal), ¿por qué sigue siendo necesario utilizar mecanismos de sincronización explícitos?

Pregunta 11Respuesta

a.

Porque el sistema operativo obliga a empaquetar los mensajes en tramas de red TCP/IP antes de depositar los datos en el buffer de la memoria RAM.

b.

Porque las operaciones de encolado y desencolado sobre la estructura de datos compartida en memoria deben protegerse con exclusión mutua para evitar condiciones de carrera.

c.

Porque el hardware de la memoria RAM prohíbe la lectura concurrente por múltiples hilos a menos que se destruya la cola.

d.

Porque los buffers de memoria solo aceptan canales de tipo símplex unidireccional sin capacidad de almacenamiento temporal.

#### Retroalimentación

Respuesta correcta

Al utilizar una estructura de datos compartida en memoria como buffer intermedio, las modificaciones concurrentes al encolar o desencolar mensajes pueden corromper la estructura si no se aplican primitivas de sincronización.

La respuesta correcta es: Porque las operaciones de encolado y desencolado sobre la estructura de datos compartida en memoria deben protegerse con exclusión mutua para evitar condiciones de carrera.

#### Pregunta 12

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En los elementos básicos que intervienen en cualquier proceso de comunicación concurrente, la entidad que inicia la comunicación y genera la información se denomina Respuesta Pregunta 12.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Es la entidad origen de la información en el esquema fundamental de comunicación.

La respuesta correcta es: emisor

#### Pregunta 13

Incorrecta

Se puntúa 0,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En un sistema donde los clientes inician las solicitudes y el servidor escucha y responde proporcionando servicios, se utiliza un tipo de comunicación según el rol de los interlocutores denominada Respuesta Pregunta 13.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

Contrasta este modelo jerárquico y funcional con las redes entre pares (P2P).

La respuesta correcta es: cliente-servidor

#### Pregunta 14

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cómo afecta el carácter bloqueante de la comunicación síncrona al comportamiento y rendimiento de un programa concurrente?

Pregunta 14Respuesta

a.

Maximiza el paralelismo del sistema al permitir que el emisor ejecute instrucciones en segundo plano sin detener su flujo de control.

b.

Garantiza la eliminación total de deadlocks al forzar la recepción inmediata de cualquier mensaje.

c.

Aumenta la eficiencia de red al comprimir automáticamente los datos antes de enviarlos de forma asíncrona.

d.

Reduce el paralelismo potencial y puede introducir bloqueos, ya que el emisor debe suspender su ejecución hasta que el receptor recibe y/o procesa el mensaje.

#### Retroalimentación

Respuesta correcta

La sincronía acopla temporalmente al emisor y al receptor, forzando tiempos de espera que impiden al emisor seguir ejecutando otras tareas de forma paralela.

La respuesta correcta es: Reduce el paralelismo potencial y puede introducir bloqueos, ya que el emisor debe suspender su ejecución hasta que el receptor recibe y/o procesa el mensaje.

#### Pregunta 15

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

¿Cuál es la diferencia fundamental en cuanto a la gestión de la sincronización entre el modelo de comunicación por memoria compartida y el modelo por paso de mensajes?

Pregunta 15Respuesta

a.

La memoria compartida elimina automáticamente los problemas de visibilidad de datos, mientras que el paso de mensajes exige el uso explícito de monitores en cada tarea transmisora.

b.

En la memoria compartida la sincronización de acceso a los datos debe ser explícita para evitar condiciones de carrera, mientras que en el paso de mensajes la sincronización suele ser implícita en las operaciones de envío y recepción.

c.

En el paso de mensajes es imprescindible implementar exclusión mutua mediante cerrojos de red, mientras que la memoria compartida no requiere sincronización alguna por ejecutarse dentro del mismo proceso.

d.

En el paso de mensajes el emisor queda bloqueado obligatoriamente en memoria física hasta que el receptor borre la variable compartida.

#### Retroalimentación

Respuesta correcta

El acceso a regiones de memoria compartida exige el uso explícito de primitivas de exclusión mutua para coordinar a los hilos, a diferencia de las primitivas de mensajes donde el propio intercambio coordina implícitamente la entrega.

La respuesta correcta es: En la memoria compartida la sincronización de acceso a los datos debe ser explícita para evitar condiciones de carrera, mientras que en el paso de mensajes la sincronización suele ser implícita en las operaciones de envío y recepción.

#### Pregunta 16

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Si una aplicación Java utiliza la clase `BlockingQueue` para enviar y recibir datos entre hilos dentro de un mismo proceso, ¿qué mecanismo técnico de comunicación se está utilizando?

Pregunta 16Respuesta

a.

Invocación remota asimétrica desacoplada de la pila de ejecución de la JVM.

b.

Paso de mensajes mediante un buffer de memoria compartido en la memoria principal del proceso.

c.

Comunicaciones mediante sockets de red sobre la interfaz de red loopback.

d.

Comunicación símplex no bloqueante respaldada por archivos en disco duro.

#### Retroalimentación

Respuesta correcta

`BlockingQueue` es una estructura de datos compartida en la memoria RAM que actúa como una cola FIFO para el paso de mensajes entre hilos concurrentes.

La respuesta correcta es: Paso de mensajes mediante un buffer de memoria compartido en la memoria principal del proceso.

#### Pregunta 17

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

En la comunicación Respuesta Pregunta 17, el proceso emisor deposita el mensaje y continúa inmediatamente con su ejecución sin suspenderse ni esperar a que el receptor procese la información.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Piensa en la analogía de depositar una carta en el buzón de correo postal o enviar un email.

La respuesta correcta es: asíncrona

#### Pregunta 18

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

El modelo de comunicación síncrono con respuesta utilizado en arquitecturas cliente-servidor y microservicios, donde el emisor se bloquea a la espera de un resultado tras enviar una petición, se conoce como Respuesta Pregunta 18.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Piensa en el mecanismo RPC (Remote Procedure Call) o en la petición que hace un cliente a un servicio web.

La respuesta correcta es: petición-respuesta

#### Pregunta 19

Correcta

Se puntúa 1,00 sobre 1,00

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/theme/image.php/centros/core/1791465588/i/unflagged)Marcar pregunta

#### Enunciado de la pregunta

Mecanismo fundamental de comunicación en red que actúa como punto final para el intercambio de datos entre procesos en máquinas distintas a través de protocolos como TCP/IP o UDP: Respuesta Pregunta 19.

_(Nota: Esta pregunta no diferencia entre mayúsculas y minúsculas)._

#### Retroalimentación

¡Correcto!

Es el punto final lógico de comunicación en red utilizado en arquitecturas cliente-servidor o de microservicios.

La respuesta correcta es: socket