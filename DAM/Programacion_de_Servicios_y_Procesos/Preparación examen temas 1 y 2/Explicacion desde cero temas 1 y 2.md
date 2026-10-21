---
asignatura: PSyP
tema: 1-2
tipo: guia
estado: completo
fecha: 2026-10-18
tags:
  - DAM/guia
  - DAM/psyp/subprocesos
  - DAM/psyp/sincronizacion
  - DAM/psyp/programa-vs-proceso
---

# Explicación desde cero — Temas 1 y 2 (PSyP)

> [!info] Asignatura
> [[DAM/Programacion_de_Servicios_y_Procesos/Indice|Programación de Servicios y Procesos]] · Temas 1 y 2 · Para cuando vas perdido y necesitas entenderlo todo desde el principio.

> [!tip] Material de examen
> - 🐣 [[Explicacion desde cero temas 1 y 2|Explicación desde cero]] ← **estás aquí**: primero entender
> - 🧠 [[Guia examen temas 1 y 2|Teoría y chuleta]]: después, consultar los detalles
> - ✅ [[Test de repaso temas 1 y 2|Test de repaso]]: practicar el examen del jueves
> - 💻 [[Practicos temas 1 y 2|Prácticos resueltos]]: practicar el examen del viernes

## Índice

- [[#0. Tus dos exámenes y cómo usar esta nota]]
- [[#Parte 1 · Tema 1 contado desde cero (examen del jueves)]]
	- [[#1.1 Programa y proceso]]
	- [[#1.2 Computación concurrente]]
	- [[#1.3 Procesos en el sistema operativo]]
	- [[#1.4 Técnicas de programación concurrente]]
	- [[#1.5 Orden de ejecución]]
	- [[#1.6 Sincronización]]
	- [[#1.7 Comunicación entre procesos]]
	- [[#1.8 Corrección de los programas concurrentes]]
	- [[#Todas las palabras de los huecos]]
	- [[#Trucos en caso de duda]]
- [[#Parte 2 · Tema 2 desde cero (examen del viernes)]]
	- [[#2.1 La idea: un programa Java que lanza otro programa]]
	- [[#2.2 Las tres tuberías]]
	- [[#2.3 Las capas de los flujos]]
	- [[#2.4 El ciclo de vida de un subproceso]]
	- [[#2.5 El programa hijo]]
- [[#Parte 3 · Método para completar una función]]
- [[#Parte 4 · Recetario de funciones típicas]]
- [[#Parte 5 · El examen del año pasado montado entero]]
- [[#Chuleta de una página]]

---

## 0. Tus dos exámenes y cómo usar esta nota

| Día | Examen | De qué es | Qué tienes que saber hacer |
| --- | --- | --- | --- |
| **Jueves 22** | Moodle, mismo formato que los cuestionarios 1-1 … 1-8 | **Tema 1** (teoría) | Elegir la opción correcta y **escribir una palabra** en los huecos |
| **Viernes 23** | En papel | **Tema 2** (Java) | Te dan el programa casi entero y **completas una función** |

Por qué esta nota va en este orden: el Tema 1 es vocabulario. Si entiendes la **idea** que hay detrás de cada palabra, el test sale casi solo. El Tema 2 es una receta que se repite siempre (lanzar un proceso, mandarle datos, leer lo que devuelve y esperar a que termine). Si entiendes la receta, cualquier función que te pidan es un trozo de ella.

> [!tip] Plan de estudio propuesto
> - **Domingo y lunes**: Parte 1 de esta nota (Tema 1). Cuando acabes cada bloque, rehaz el cuestionario de ese apartado en [[Cuestionario 1-1]] … [[Cuestionario 1-8]] tapando las respuestas.
> - **Martes**: [[#Todas las palabras de los huecos]] + [[Test de repaso temas 1 y 2]]. Las palabras que fallaste (*firmware*, *binarios*, *multiprocesamiento*, *cliente-servidor*) tienen que salirte solas.
> - **Miércoles**: Parte 2 (Tema 2) y Parte 3 (método). Copia a mano en papel el programa de la Parte 5.
> - **Jueves, después del examen**: Parte 4 (recetario). Haz cada función **en papel**, con los huecos tapados.
> - **Jueves por la noche**: [[Practicos temas 1 y 2]] y la [[#Chuleta de una página]].

---

# Parte 1 · Tema 1 contado desde cero (examen del jueves)

> [!note] Cómo leer cada bloque
> Cada apartado sigue el mismo orden: **idea → analogía → palabras de los huecos → trampas**. Los cuestionarios hechos te dan pistas de lo que pregunta el profesor: todos tus fallos fueron en las preguntas de **rellenar**, no en las de test. Por eso las palabras exactas son lo más importante.

## 1.1 Programa y proceso

**La idea.** Un **programa** es un fichero que está quieto en el disco: instrucciones y datos, sin hacer nada. Cuando lo ejecutas, el sistema operativo (SO) lo carga en memoria, le da recursos (memoria, CPU, ficheros abiertos) y le asigna un número, el **PID**. Esa cosa viva que está ejecutándose es el **proceso**. Por eso se dice que el programa es **estático** y el proceso es **dinámico**.

> [!example] Analogía: la receta y el cocinero
> - La **receta** escrita en el libro es el **programa**: no se mueve.
> - **Cocinar** siguiendo la receta, con sus fogones, ingredientes y el paso por el que vas, es el **proceso**.
> - Con una misma receta pueden cocinar **dos personas a la vez**: un programa puede dar lugar a **varios procesos**, cada uno con su PID.

**Vocabulario que rodea a programa y proceso:**

- **Software**: el conjunto de todos los programas que funcionan sobre el hardware.
- **Aplicación**: un programa pensado para resolver un problema concreto del usuario (un navegador, Word...).
- **Ejecutable**: el fichero que se puede ejecutar. En Windows se reconoce por la extensión `.exe`; en Linux y macOS, por tener activado el permiso de **ejecución** (no por la extensión).
- **Librería** (o biblioteca): código reutilizable que usan varios programas para no reescribir lo mismo.
- **Firmware**: software grabado en una memoria no volátil (la ROM de la placa base, por ejemplo), que controla directamente un circuito.

**Tipos de ejecutables según cómo se ejecuta su código:**

- **Binarios**: instrucciones que la **CPU ejecuta directamente**. Son rápidos, pero hay que recompilar para cada plataforma. El que los genera es el **compilador**, que traduce *todo* el código fuente a código máquina **antes** de ejecutarlo.
- **Interpretados**: un **intérprete** los va traduciendo **mientras se ejecutan**. Java es así: `javac` genera **bytecode** y la **JVM** lo interpreta. Por eso Java funciona en cualquier sistema.
- **Scripts**: interpretados y **sin compilar**; son texto legible (por ejemplo, un `.sh`).

**Demonios y servicios.** Son procesos que se ejecutan en **segundo plano**, sin ventana, durante mucho tiempo y esperando peticiones. En Linux se llaman **demonios**; en Windows, **servicios**. La mayoría se cargan durante el **arranque** del sistema. Ejemplo: el servicio de **impresión** (*spooler*) gestiona la cola de documentos y, si no hay trabajos, pone la impresora en **standby**.

> [!tip] Palabras que te pueden pedir en los huecos (Cuestionario 1-1)
> **ejecución** (permiso en Linux) · **intérprete** · **firmware** · **ejecutable** · **proceso** · **bytecode** · **dinámica** · **standby** · **binarios** · **aplicación** · **compilador** · **PID** · **software** · **segundo** (plano) · **servicio** · **arranque** · **impresión** · **librería** · **demonio** · **programa**

> [!warning] Trampas (fallaste estas)
> - Software grabado en memoria no volátil que controla un circuito → **firmware** (no "driver" ni "BIOS").
> - Ejecutables cuyas instrucciones procesa directamente la CPU → ejecutables **binarios**.
> - Un `.txt` **no** es un ejecutable ni un servicio.
> - En Linux un fichero es ejecutable por su **permiso**, no por su extensión.

> [!example]- 🔗 Fuente
> - [[1.1 - Programa vs. Proceso]] · [[Cuestionario 1-1]] · [[1.C - Cuestionario Apartado 1.1]]
> - Guía: [[Guia examen temas 1 y 2#A.1 · Programa vs. proceso|A.1 · Programa vs. proceso]]

---

## 1.2 Computación concurrente

**La idea.** Tu ordenador parece hacer muchas cosas a la vez (música, navegador, IDE...). Eso es la **concurrencia**: varios procesos **avanzan** durante el mismo periodo de tiempo. Hay dos formas de conseguirlo:

1. **Paralelismo**: hay varios núcleos y cada uno ejecuta un proceso **de verdad al mismo tiempo**. Necesita **2 o más núcleos**.
2. **Multiprogramación**: hay un solo núcleo y el SO va dando **turnos** muy cortos a cada proceso. Va tan rápido que parece simultáneo, pero no lo es.

Lo que **percibe el usuario** (poder hacer varias cosas a la vez) se llama **multitarea**.

> [!example] Analogía: el malabarista
> Un malabarista con 3 pelotas solo toca **una** en cada momento, pero las tres están "en el aire" a la vez. Eso es la **multiprogramación**. Tres malabaristas, cada uno con su pelota, serían el **paralelismo**.

**Cambio de contexto.** Para pasar la CPU de un proceso a otro, el SO **guarda el estado** del que sale (registros, por dónde iba) y **restaura** el del que entra. Mientras hace eso, la CPU no ejecuta nada útil del usuario, así que la multiprogramación **no acelera**: el tiempo total incluso **aumenta un poco**.

**Arquitecturas con varios procesadores:**

- **Multiprocesamiento**: varios procesadores **comparten la misma memoria**.
	- **Simétrico (SMP)**: todos los procesadores son iguales y cualquiera hace cualquier tarea.
	- **Asimétrico (AMP)**: uno es **maestro** y reparte el trabajo a los **esclavos**.
- **Procesamiento distribuido**: cada procesador tiene **su propia memoria** y se comunican **por red**, con mensajes. Un ejemplo es el **cluster**: varios PCs normales unidos por una red local (LAN).

Cuando varios procesos colaboran o compiten por recursos, hacen falta mecanismos de **comunicación** y **sincronización**.

> [!tip] Palabras que te pueden pedir en los huecos (Cuestionario 1-2)
> **contexto** (cambio de) · **multiprocesamiento** · **asimétrico** (AMP) · **paralelismo** · **simétrico** (SMP) · **sincronización** · **cluster** · **distribuido** · **multitarea** · **multiprogramación**

> [!warning] Trampas
> - Varios procesadores que **comparten memoria** → **multiprocesamiento** (fallaste esta). Si **no** la comparten → **distribuido**.
> - La multiprogramación **no reduce** el tiempo total: lo aumenta ligeramente por los cambios de contexto.
> - Hyper-Threading (SMT) **no es paralelismo puro**: un núcleo físico se presenta como varios lógicos.

> [!example]- 🔗 Fuente
> - [[1.2 - Computacion concurrente]] · [[Cuestionario 1-2]]
> - Guía: [[Guia examen temas 1 y 2#A.2 · Computación concurrente|A.2 · Computación concurrente]]

---

## 1.3 Procesos en el sistema operativo

**La idea.** El SO tiene que "llevar la cuenta" de cada proceso: dónde está en memoria, en qué estado se encuentra y a quién le toca usar la CPU.

**Memoria de un proceso.** Cada proceso cree que tiene la memoria para él solo (es memoria **virtual**). Está dividida en 4 trozos:

- **Código (texto)**: las instrucciones.
- **Datos**: las variables globales y estáticas.
- **Pila (stack)**: las llamadas a funciones y las variables locales.
- **Heap (montón)**: la memoria **dinámica**, la que se pide durante la ejecución (los `new` de Java).

Si un proceso intenta salirse de su memoria, se produce un **segmentation fault**.

**PCB (Process Control Block).** Es el "DNI" del proceso. Guarda el PID, el estado, la prioridad y lo necesario para el cambio de contexto (contador de programa, registros...).

**Estados de un proceso** (aprende el ciclo, no la lista):

```text
 Nuevo ──► Listo ◄───────────────┐
             │  ▲                │ espera completada
  asignación │  │ apropiación    │ (llegó la E/S)
             ▼  │ (se acabó el   │
        En ejecución  quantum)   │
             │      └────────► Bloqueado (esperando E/S)
             ▼   espera
         Terminado
```

- **Listo**: tiene todo **menos la CPU**.
- **Bloqueado**: está esperando algo (leer un fichero, una tecla...) y **cede la CPU por su cuenta**.
- **Apropiación (preemption)**: el SO le **quita** la CPU porque se le acabó el turno (**quantum**) o porque llega un proceso más prioritario. Pasa de *en ejecución* a *listo*.
- **Suspendido**: el SO lo saca de la RAM al disco (*swapping*) para liberar memoria. Suele elegir a uno **bloqueado**, porque total, no está haciendo nada.
- **Zombie**: ha terminado, pero su padre todavía no ha recogido su código de salida.

> [!example] Analogía: la consulta del médico
> - **Listo** = estás en la sala de espera.
> - **En ejecución** = estás dentro de la consulta.
> - **Bloqueado** = el médico te manda a hacerte un análisis y sales hasta que lleguen los resultados.
> - **Apropiación** = se acaba tu tiempo y te hacen volver a la sala para que pase otro.
> - **Planificador (scheduler)** = la recepcionista que **decide** quién pasa.
> - **Despachador (dispatcher)** = quien **te acompaña** hasta la puerta, es decir, quien hace el cambio de contexto.

**Algoritmos de planificación:**

- **FIFO/FCFS**: el primero que llega, primero que se ejecuta. Un proceso largo bloquea a los cortos.
- **Round Robin**: turnos de un quantum fijo, en rueda.
- **SJF**: primero el proceso más corto. Hay que saber (o estimar) cuánto dura cada uno.
- **Prioridades**: siempre el más prioritario. Puede provocar **inanición** en los de baja prioridad.
- **Multinivel con retroalimentación**: varias colas; los procesos **bajan de prioridad** según gastan CPU. Es el que usan **Windows y macOS**.

**El planificador a largo plazo** decide cuántos procesos nuevos entran (el grado de multiprogramación). **El de corto plazo** decide cuál de los listos pasa a la CPU.

**Comandos:** `ps aux` y `pstree` (listar) · `kill PID` (pedir terminar) · `kill -9 PID` (forzar) · `nice` y `renice` (prioridad, de **-20 = máxima** a **19 = mínima**) · en Windows, `tasklist` y `taskkill`.

> [!tip] En el Cuestionario 1-3 no había huecos
> Todo era test y sacaste 16/16. Repasa sobre todo: el **heap** guarda la memoria dinámica, la **apropiación** ocurre por agotar el quantum, y el **multinivel con retroalimentación** es el de Windows y macOS.

> [!example]- 🔗 Fuente
> - [[1.3 - Procesos en el sistema operativo]] · [[Cuestionario 1-3]]
> - Guía: [[Guia examen temas 1 y 2#A.3 · Procesos en el sistema operativo|A.3 · Procesos en el sistema operativo]]

---

## 1.4 Técnicas de programación concurrente

**La idea.** Según cómo se relacionan los procesos entre sí, hay 3 tipos:

| Tipo | ¿Qué pasa? | ¿Qué necesitan? | Ejemplo |
| --- | --- | --- | --- |
| **Independientes** | Cada uno va a lo suyo; solo comparten la CPU | Nada (ya se encarga el planificador del SO) | Spotify y el navegador |
| **Cooperantes** | Trabajan **juntos** en una tarea | **Comunicación** | `ls \| grep txt`: uno pasa datos al otro |
| **Competidores** | Quieren el **mismo recurso exclusivo** | **Sincronización** (exclusión mutua) | Dos procesos imprimiendo a la vez |

**Formas de programar:**

- **Concurrente**: el caso general.
- **Paralela**: varios núcleos con **memoria compartida** (SMP); el objetivo es **acelerar**.
- **Distribuida**: varias máquinas que se comunican **por mensajes**. En el curso **no** se estudia.

> [!example] Analogía
> - **Independientes**: dos vecinos, cada uno en su casa.
> - **Cooperantes**: una cadena de montaje, donde cada uno le pasa la pieza al siguiente.
> - **Competidores**: dos compañeros de piso que quieren usar el único baño.

Sin sincronización entre competidores aparecen **datos inconsistentes** y **condiciones de carrera**.

> [!example]- 🔗 Fuente
> - [[1.4 - Tecnicas de programacion concurrente]] · [[Cuestionario 1-4]]
> - Guía: [[Guia examen temas 1 y 2#A.4 · Técnicas de programación concurrente|A.4 · Técnicas de programación concurrente]]

---

## 1.5 Orden de ejecución

**La idea.** En un programa normal (**secuencial**) las instrucciones van **una detrás de otra, siempre igual**. Es el **orden total**: una línea recta. Con varios hilos, dentro de cada hilo se mantiene el orden, pero **entre hilos no sabes cuál va primero**. Eso es el **orden parcial**: varios caminos que se entrelazan de forma impredecible. Quien decide el orden es el **planificador**.

> [!example] Analogía: el gestor y los trabajadores
> Los trabajadores (hilos) hacen cada uno su lista de tareas en orden. El **gestor** (el planificador del SO) decide en cada momento a quién le toca trabajar. Como cada día lo decide de forma distinta, el resultado mezclado puede salir diferente.

**Condición de carrera (race condition).** Pasa cuando el resultado **depende del orden** en que se ejecutan los hilos. Provoca **comportamiento errático**: con los mismos datos de entrada, unas veces sale bien y otras mal.

**Carrera de datos (data race).** Es un caso concreto que exige **las 3 condiciones a la vez**:
1. Dos o más hilos acceden a la **misma variable**.
2. **Al menos uno escribe**.
3. Los accesos **no están sincronizados**.

> [!warning] Trampas
> - Si todos los hilos **solo leen**, **no** hay data race (falta la condición 2).
> - Que dos hilos impriman en distinto orden **no es un error**, salvo que la corrección del programa dependa de ese orden.
> - El **mutex** garantiza que **solo un hilo a la vez** entre en la sección crítica (no acelera nada).

> [!example]- 🔗 Fuente
> - [[1.5 - Orden de ejecucion]] · [[Cuestionario 1-5]]
> - Guía: [[Guia examen temas 1 y 2#A.5 · Orden de ejecución|A.5 · Orden de ejecución]]

---

## 1.6 Sincronización

**La idea.** Cuando varios hilos tocan lo mismo, hay que **poner orden**. Existen dos tipos de sincronización:

- **De acceso a datos (exclusión mutua)**: que **solo uno a la vez** toque el recurso.
- **De control**: que uno **espere** a que otro termine algo antes de seguir (por ejemplo, esperar a que haya un dato).

**Por qué `x = x + 1` falla con dos hilos.** Aunque parece una sola instrucción, la CPU la hace en 3 pasos: **cargar** x, **sumar** 1 y **guardar**. Si los dos hilos cargan x=0 antes de que ninguno guarde, los dos guardan 1. Resultado: **x = 1 en vez de 2**, porque se ha perdido un incremento.

> [!example] Analogía: el baño con una sola llave
> - **Sección crítica** = el baño, es decir, el trozo de código que toca el recurso compartido.
> - **Exclusión mutua** = la regla de que solo entra uno.
> - **Mutex** = la llave. Quien la tiene entra; los demás esperan en la puerta.
> - **Lock contention** = la cola de gente esperando la llave. Cuanto más tardes dentro, peor rendimiento.

En Java la llave se pone con `synchronized`:

```java
public class SafeCounter {

    private int x = 0;

    // Solo un hilo a la vez puede estar dentro de estos métodos (misma llave: this)
    public synchronized void increment() {
        x = x + 1;
    }

    public synchronized void decrement() {
        x = x - 1;
    }
}
```

**Visibilidad (JMM).** Cada hilo trabaja con una **copia en caché** de las variables, así que un hilo puede no ver el cambio que hizo otro. `volatile` asegura la **visibilidad**; `synchronized` asegura visibilidad **y además** exclusión mutua.

**Teorema de Bernstein.** Dos trozos de código pueden ejecutarse a la vez si **ninguno escribe lo que el otro lee o escribe**:
1. Lo que lee A ∩ lo que escribe B = vacío.
2. Lo que escribe A ∩ lo que lee B = vacío.
3. Lo que escribe A ∩ lo que escribe B = vacío.

**Productor-consumidor y monitor.** El consumidor no puede sacar datos de un buffer **vacío**, ni el productor meterlos en uno **lleno**. Si espera dentro de la sección crítica sin soltar la llave, el otro nunca puede entrar y se produce un **deadlock**. La solución es el **monitor**, que en Java es **cualquier objeto**:

- `synchronized` → exclusión mutua.
- `wait()` → me duermo **soltando la llave**.
- `notify()` despierta **a uno**; `notifyAll()` despierta **a todos**.

> [!example]- 🔗 Fuente
> - [[1.6 - Sincronizacion]] · [[Cuestionario 1-6]] · [[1.R - Preguntas del Tema 1]]
> - Guía: [[Guia examen temas 1 y 2#A.6 · Sincronización|A.6 · Sincronización]]

---

## 1.7 Comunicación entre procesos

> [!warning] Este apartado no tiene nota de teoría
> En el índice, el 1.7 está pendiente. Lo que sigue se ha **recuperado del [[Cuestionario 1-7]]**, que sí entra en el examen.

**La idea.** Comunicarse es mandar información de un proceso a otro. Siempre intervienen: un **emisor** (el que la genera y envía), un **receptor**, un **mensaje** y un **canal** (el medio por donde viaja: una red, un cable, una zona de memoria).

**El canal según la dirección:**

- **Simplex**: solo en una dirección, como la radio o la tele.
- **Half duplex**: en las dos direcciones, pero **por turnos**, como un walkie-talkie o una carretera de un solo carril.
- **Full duplex**: en las dos direcciones **a la vez**, como el teléfono.

**Síncrona o asíncrona:**

- **Síncrona**: el emisor **se queda esperando** a que el receptor lo reciba. El modelo **petición-respuesta** (cliente-servidor, microservicios) es síncrono.
- **Asíncrona**: el emisor deja el mensaje y **sigue con lo suyo** (como un WhatsApp).

**Según los roles:**

- **Simétrica**: todos pueden enviar y recibir (P2P).
- **Asimétrica o cliente-servidor**: el cliente pide y el servidor responde.

**Las dos grandes formas:**

- **Memoria compartida**: los hilos leen y escriben en la misma memoria. Es muy rápida, pero necesita sincronización explícita y solo sirve en la misma máquina.
- **Paso de mensajes**: se mandan mensajes, por ejemplo a través de un **socket** (el punto final de una conexión de red TCP/IP o UDP). Es más lento (red + serialización), pero funciona **entre máquinas distintas**.

> [!tip] Palabras que te pueden pedir en los huecos (Cuestionario 1-7)
> **memoria compartida** · **canal** · **simplex** · **full duplex** · **emisor** · **cliente-servidor** · **asíncrona** · **petición-respuesta** · **socket**

> [!warning] Trampa (fallaste esta)
> "Los clientes inician las solicitudes y el servidor escucha y responde": según el rol de los interlocutores, esa comunicación se llama **cliente-servidor**.

> [!example]- 🔗 Fuente
> - [[Cuestionario 1-7]] · [[1.2 - Computacion concurrente]]
> - Guía: [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|A.7 · Comunicación entre procesos]]

---

## 1.8 Corrección de los programas concurrentes

**La idea.** Un programa concurrente es correcto si cumple dos tipos de propiedades:

- **Seguridad**: que **no pase nada malo**. Por ejemplo, la exclusión mutua o que no haya deadlock.
- **Viveza**: que **acabe pasando lo bueno**, es decir, que el programa avance. Por ejemplo, que no haya livelock ni inanición.

**Los 4 problemas, con su analogía:**

| Problema | Qué pasa | Analogía |
| --- | --- | --- |
| **Interbloqueo (deadlock)**, el pasivo | Están **parados** para siempre, esperando cada uno al otro | Dos coches en un puente estrecho; ninguno da marcha atrás |
| **Bloqueo activo (livelock)** | Se **mueven** y cambian de estado, pero no avanzan | Dos personas en un pasillo que se apartan a la vez hacia el mismo lado, una y otra vez |
| **Inanición (starvation)** | A uno **nunca le toca** porque siempre se elige a otros | El que nunca consigue ser atendido en la barra porque siempre se cuela alguien |
| **Inversión de prioridad** | Uno de baja prioridad tiene el recurso, uno de media se cuela y el de alta se queda esperando | El becario tiene la llave del despacho y el jefe espera fuera |

**Las 4 condiciones de Coffman.** Para que haya deadlock tienen que darse **todas a la vez**:
1. **Exclusión mutua**: el recurso es de uno solo.
2. **Retención y espera**: tengo un recurso y espero otro **sin soltar el mío**.
3. **No apropiación**: nadie me puede quitar el recurso; solo lo suelto yo.
4. **Espera circular**: A espera a B, B espera a A.

Basta con romper una para evitarlo. La forma típica es pedir los recursos **siempre en el mismo orden**, que rompe la espera circular.

**Soluciones:**

- Inanición → **fairness** (justicia): tener en cuenta cuánto tiempo lleva esperando cada uno.
- Inversión de prioridad → **herencia de prioridad**: el de baja prioridad **hereda** temporalmente la prioridad alta, termina rápido y suelta el recurso.

**Mecanismos de exclusión mutua:**

- **Mutex**: una llave binaria.
- **Semáforo**: un contador. `acquire()` **resta 1**, y si el contador está a 0, **el hilo se bloquea** hasta que otro haga `release()`, que **suma 1**.
- **Monitor**: el de Java (`synchronized` + `wait`/`notify`).

> [!tip] Palabras que te pueden pedir en los huecos (Cuestionario 1-8)
> **inanición** · **no apropiación** · **inversión** (de prioridad) · **herencia** (de prioridad) · **exclusión mutua** · **interbloqueo** (pasivo) · **bloqueo activo**

> [!example]- 🔗 Fuente
> - [[1.8 - Corrección en los programas concurrentes]] · [[Cuestionario 1-8]]
> - Guía: [[Guia examen temas 1 y 2#A.8 · Corrección en los programas concurrentes|A.8 · Corrección en los programas concurrentes]]

---

## Todas las palabras de los huecos

Son las **46 respuestas reales** de las preguntas de rellenar de tus cuestionarios. Tapa la columna derecha y di cada palabra en voz alta.

| Pista (resumida del enunciado) | Palabra |
| --- | --- |
| Permiso que hace ejecutable un fichero en Linux | ejecución |
| Traduce código intermedio a máquina **durante** la ejecución | intérprete |
| Software grabado en memoria no volátil que controla circuitos ⚠️ | firmware |
| Fichero con código capaz de ejecutarse directamente | ejecutable |
| Entidad dinámica: programa en ejecución con recursos | proceso |
| Código intermedio de Java que interpreta la JVM | bytecode |
| El proceso es una entidad... | dinámica |
| Estado de reposo de la impresora sin trabajos | standby |
| Ejecutables procesados directamente por la CPU ⚠️ | binarios |
| Programa para resolver un problema del usuario | aplicación |
| Traduce **todo** el código fuente antes de ejecutar | compilador |
| Identificador numérico de un proceso | PID |
| Conjunto de programas sobre el hardware | software |
| Demonios y servicios se ejecutan en ... plano | segundo |
| Demonio en Windows | servicio |
| Los servicios se cargan durante la secuencia de ... | arranque |
| Servicio que gestiona la cola de la impresora | impresión |
| Código reutilizable por varios programas | librería |
| Proceso en segundo plano en Unix/Linux | demonio |
| Representación estática en disco | programa |
| Guardar el estado de un proceso y restaurar otro: cambio de ... | contexto |
| Varios procesadores que comparten memoria ⚠️ | multiprocesamiento |
| Multiprocesamiento con maestro y esclavos (AMP) | asimétrico |
| Ejecución simultánea **real** | paralelismo |
| Multiprocesamiento con procesadores iguales (SMP) | simétrico |
| Comunicación y ... entre procesos | sincronización |
| PCs normales unidos por una LAN | cluster |
| Sin memoria compartida, comunicación por red | distribuido |
| Percepción del usuario de hacer varias cosas a la vez | multitarea |
| Simular concurrencia por turnos | multiprogramación |
| Comunicación por un espacio de memoria común | memoria compartida |
| Soporte por donde viaja el mensaje | canal |
| Canal en una sola dirección | simplex |
| Canal bidireccional y simultáneo | full duplex |
| Quien inicia y genera la comunicación | emisor |
| Clientes piden, el servidor responde ⚠️ | cliente-servidor |
| El emisor deposita el mensaje y sigue | asíncrona |
| Síncrono con respuesta (microservicios) | petición-respuesta |
| Punto final de comunicación en red | socket |
| Privar indefinidamente de un recurso | inanición |
| Coffman: solo lo libera su dueño | no apropiación |
| Baja bloquea a alta y media se cuela: ... de prioridad | inversión |
| La baja sube temporalmente su prioridad: ... de prioridad | herencia |
| Solo una tarea a la vez en la sección crítica | exclusión mutua |
| Suspendidos esperándose mutuamente: ... pasivo | interbloqueo |
| En ejecución, en bucle de reintentos, sin progresar | bloqueo activo |

⚠️ = las que fallaste en el cuestionario.

---

## Trucos en caso de duda

> [!info] De dónde salen estos datos
> He analizado **las 128 preguntas tipo test y las 46 de hueco** de tus cuestionarios [[Cuestionario 1-1]] … [[Cuestionario 1-8]], comparando las opciones correctas con las incorrectas (los distractores). Lo que sigue no es intuición: son **patrones medidos**.

### Qué dicen los números (test)

| Patrón | Aparece en la correcta | Aparece en las incorrectas | ¿Sirve? |
| --- | --- | --- | --- |
| La correcta es la opción **más larga** | 86 de 128 (67 %) | — | ✅ Bastante, **pero** en el 1-4 solo acertaba 2 de 20 |
| **Exageraciones**: *elimina, a cero, el doble, la mitad, prohíbe* | **0 %** | 6 % | ✅✅ Si una opción exagera, táchala |
| **Otro ámbito**: *BIOS, bus PCI, garbage collector, compilador, GUI, MBR, swap, fibra óptica...* | 1 % | 9 % | ✅✅ Opción "de relleno" casi segura |
| **Absolutos**: *siempre, solo, exclusivamente, obligatoriamente, cualquier, ningún...* | 14 % | 36 % | ✅ Desconfía, salvo que el absoluto **sea la propia definición** |
| *Automáticamente, inmediatamente, espontáneamente* | 3 % | 8 % | ✅ Desconfía |
| **Matices**: *puede, suele, depende, habitualmente* | 10 % | 4 % | 🟡 Pista a favor de la opción |
| **La letra** (a/b/c/d) | a 33 · b 29 · c 32 · d 34 | — | ❌ Inútil: está repartida al azar y Moodle suele barajar las opciones |
| Preguntas **en negativo** ("¿cuál **NO** es...?") | 1 de 128 | — | ⚠️ Raras, pero en ellas los trucos **se invierten** |

> [!warning] La excepción del absoluto
> Las correctas también usan "solo" o "todos" cuando **es la definición**: *"que **únicamente** un hilo a la vez acceda a la sección crítica"* (exclusión mutua), *"**todos** los procesadores funcionan de igual manera"* (SMP), *"tiene **todos** los recursos **excepto** la CPU"* (estado listo). Si el absoluto coincide con lo que dicen los apuntes, no lo descartes.

### Método de descarte en 4 pasos

1. **Tacha lo absurdo**: opciones que hablan de otra cosa (hardware, compilador, GUI, permisos de administrador) o que exageran ("reduce la memoria a cero", "el doble de rápido").
2. **Tacha lo que contradice el concepto**: si la pregunta es sobre exclusión mutua y una opción dice "que todos escriban a la vez", es justo lo contrario.
3. **Entre las que queden, elige la más completa y precisa**: la que **define** con vocabulario de los apuntes, explica el **porqué** o retoma las palabras clave del enunciado. Suele ser también la más larga.
4. **Relee el enunciado** por si es una pregunta en negativo ("NO", "excepto", "falsa"). Si lo es, buscas justo la opción absurda.

### Cuatro ejemplos reales

> [!example]- Cuestionario 1-4 · P4: ¿Por qué es indispensable la sincronización con procesos competidores?
> - a. Para apagar los núcleos sobrantes del procesador. → ❌ **Otro ámbito** (hardware).
> - b. Para reducir **automáticamente** el uso de memoria **a cero**. → ❌ **Exageración** + automático.
> - c. Para permitir que **todos** los procesos escriban **a la vez** en la misma dirección. → ❌ **Contradice el concepto**: es lo contrario de sincronizar.
> - d. ✅ Para garantizar el acceso **mutuamente excluyente** al recurso crítico. → La única que usa vocabulario de los apuntes.

> [!example]- Cuestionario 1-6 · P7: `x = x + 1` con dos hilos sin exclusión mutua, partiendo de x = 0
> - a. x es **siempre** 0 por un reinicio de memoria. → ❌ Absoluto + inventado.
> - b. El procesador aborta **automáticamente** con un trap. → ❌ Automático + otro ámbito.
> - c. ✅ x vale 1, **perdiéndose uno de los incrementos**. → Da el **porqué**.
> - d. x vale 3 por desbordamiento. → ❌ Absurdo: con dos sumas de 1 no puedes llegar a 3.

> [!example]- Cuestionario 1-2 · P13: ¿Qué requisito es imprescindible para el paralelismo real?
> - a. Planificación por turnos sin hardware adicional. → ❌ Eso es multiprogramación, lo contrario.
> - b. Un **único** núcleo con caché L3 grande. → ❌ Contradice "paralelismo".
> - c. ✅ **Al menos dos núcleos** (multinúcleo o multiprocesador). → Definición de los apuntes.
> - d. **Exclusivamente** una tarjeta gráfica por **bus PCIe**. → ❌ Absoluto + otro ámbito.

> [!example]- Cuestionario 1-8 · P13: Recurso con exactamente 5 instancias. ¿Qué primitiva usar?
> - a. Un booleano con espera activa. → ❌ La espera activa siempre aparece como algo malo.
> - b. Un mutex binario "con 5 estados". → ❌ Contradicción: binario = 2 estados.
> - c. Un monitor sin variables de condición. → ❌ Incompleto.
> - d. ✅ Un semáforo contador **inicializado con el valor 5**. → Retoma el dato del enunciado (el 5).

### Trucos para las preguntas de hueco

Las 46 respuestas de hueco tienen estos patrones:

- **Siempre es una palabra** (o dos como mucho: *exclusión mutua*, *bloqueo activo*, *full duplex*), y sale **literal** en los apuntes. Nunca piden una frase.
- **El artículo da el género**: "**La** ___ de prioridad" → femenino (*inversión*, *herencia*) · "**El** ___ pasivo" → masculino (*interbloqueo*) · "**Un** ___ es un fichero" → *ejecutable* · "**Una** ___ (o biblioteca)" → *librería*.
- **El paréntesis es una pista**: "multiprocesamiento ___ (o **AMP**)" → **a**simétrico · "(o **SMP**)" → **s**imétrico · "(o biblioteca)" → librería.
- **Expresiones fijas**: "cambio de ___" → contexto · "segundo ___" → plano · "permiso de ___" → ejecución · "servicio de ___" → impresión.
- **La palabra que define es la del apunte, no un ejemplo**: fallaste *firmware* por poner BIOS/UEFI, y *binarios* por poner "nativos". Si dudas entre el **término general** y un **ejemplo concreto**, el hueco pide el **general**.
- Moodle **no distingue mayúsculas** y a veces acepta la palabra sin tilde, pero escríbela **con tilde** para ir sobre seguro.

> [!danger] Úsalos solo para desempatar
> Estos trucos aciertan muchas veces, **no siempre**: en el Cuestionario 1-4 la correcta era casi siempre la **más corta**. Si el profesor cambia de estilo, el truco de la longitud falla. Lo que nunca falla es el **contenido**. Los trucos son para cuando dudas entre dos opciones o te quedas en blanco, no para contestar sin leer.

---

# Parte 2 · Tema 2 desde cero (examen del viernes)

## 2.1 La idea: un programa Java que lanza otro programa

Hasta ahora tus programas Java hacían todo ellos solos. En el Tema 2, un programa Java (el **padre**) **arranca otro programa** (el **hijo** o **subproceso**), igual que cuando tú escribes `ls -la` en la terminal y la terminal arranca `ls`.

Para que te hagas una idea, esto es lo que hace el padre:

1. **Prepara** el comando que quiere ejecutar → `ProcessBuilder`.
2. Lo **arranca** → `start()`, que devuelve un objeto `Process` (el "mando a distancia" del hijo).
3. Le **manda datos** y **lee** lo que contesta → los flujos (tuberías).
4. **Espera** a que termine y mira si fue bien → `waitFor()` y el **código de salida** (`0` = bien; otro número = error).

```java
// Lo mínimo: lanzar "ls -la" y esperar a que acabe
ProcessBuilder pb = new ProcessBuilder("ls", "-la");    // 1. preparar (cada palabra va por separado)
Process process = pb.start();                           // 2. arrancar
int exitCode = process.waitFor();                       // 4. esperar y recoger el código de salida
```

> [!definition] `ProcessBuilder` y `Process`
> - **`ProcessBuilder`** es el **formulario**: lo rellenas (comando, carpeta, variables de entorno, redirecciones) **antes** de arrancar.
> - **`Process`** es el **mando a distancia** del hijo ya arrancado: con él le escribes, lo lees, lo esperas o lo matas.
> - Todo lo que se **configura** va **antes** de `start()`. Después de `start()`, cambiar el `ProcessBuilder` ya no afecta a ese hijo.

**Otra forma de lanzarlo, más antigua**, es `Runtime.getRuntime().exec(new String[]{"ls", "-la"})`. Hace lo mismo, pero sin poder configurar nada. Hoy se recomienda `ProcessBuilder`.

---

## 2.2 Las tres tuberías

Todo programa tiene 3 "canales" estándar: **stdin** (entrada, lo que se lee, como el teclado), **stdout** (salida normal, como `System.out`) y **stderr** (salida de errores, como `System.err`). Cuando el padre arranca al hijo, Java conecta esos canales del hijo con el padre mediante **tuberías**:

```text
          PADRE (tu programa Java)                       HIJO
  ┌──────────────────────────────────┐          ┌───────────────────┐
  │ process.getOutputStream()  ──────┼────────► │ stdin  (System.in) │
  │ process.getInputStream()   ◄─────┼───────── │ stdout (System.out)│
  │ process.getErrorStream()   ◄─────┼───────── │ stderr (System.err)│
  └──────────────────────────────────┘          └───────────────────┘
```

> [!warning] El truco para no liarte (pregunta clásica)
> Los nombres se leen **desde el punto de vista del padre**:
> - `getOutputStream()` = lo que **sale del padre** → entra al hijo → sirve para **escribirle**.
> - `getInputStream()` = lo que **entra al padre** → viene del hijo → sirve para **leer su respuesta**.
>
> Piénsalo así: *Output = yo (el padre) le hablo · Input = yo le escucho.*

**Redirecciones.** En vez de usar una tubería, puedes decirle al `ProcessBuilder` que conecte el canal del hijo a otro sitio (siempre **antes** de `start()`):

- `pb.redirectError(ProcessBuilder.Redirect.INHERIT)` → los errores del hijo salen **por la misma consola que el padre**. El enunciado lo dice así: "que la salida de error sea la misma que la del padre".
- `pb.redirectError(new File("errores.log"))` → los errores del hijo van **a un fichero**.
- `pb.redirectErrorStream(true)` → **mezcla** stderr con stdout, y lo lees todo con `getInputStream()`.
- `pb.inheritIO()` → hereda los tres canales.

---

## 2.3 Las capas de los flujos

Lo que más asusta del Tema 2 es esta línea:

```java
BufferedReader reader = new BufferedReader(
        new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8));
```

Son **tres capas**, como una cebolla. Cada una añade algo a la anterior:

| Capa | Qué es | Qué añade |
| --- | --- | --- |
| `process.getInputStream()` | `InputStream`: la tubería en bruto | Solo transporta **bytes** (números) |
| `new InputStreamReader(..., UTF_8)` | Traductor | Convierte bytes en **caracteres**, usando la codificación UTF-8 |
| `new BufferedReader(...)` | Lector cómodo | Te da **`readLine()`**, que lee una **línea entera** |

Para **escribir** es lo mismo, pero al revés:

```java
BufferedWriter writer = new BufferedWriter(
        new OutputStreamWriter(process.getOutputStream(), StandardCharsets.UTF_8));
writer.write("hola");   // escribe el texto
writer.newLine();       // salto de línea: así el hijo sabe que la línea ha terminado
```

> [!tip] Regla para recordarlo
> - **Leer** = `BufferedReader` + `InputStreamReader` + `getInputStream()` → todo lleva **Input/Reader**.
> - **Escribir** = `BufferedWriter` + `OutputStreamWriter` + `getOutputStream()` → todo lleva **Output/Writer**.
>
> Nunca se mezcla un *Input* con un *Writer*. Si en el examen te sale, está mal.

**`try-with-resources`.** Si escribes `try (BufferedWriter writer = ...) { ... }`, Java **cierra el flujo él solo** al salir de las llaves. En este tema es **clave**, como verás en el siguiente apartado.

---

## 2.4 El ciclo de vida de un subproceso

Este es el **orden que siempre hay que seguir**. El examen del viernes será casi seguro una de estas cajas:

```text
 ① CONFIGURAR     ProcessBuilder: comando, directory(), environment(), redirect...()
        │
 ② ARRANCAR       Process p = pb.start();         → p.pid() da su PID
        │
 ③ ESCRIBIR       BufferedWriter sobre p.getOutputStream(): write + newLine
        │
 ④ CERRAR         cerrar el writer  ← ¡si no, el hijo se queda esperando más datos para siempre!
        │
 ⑤ LEER           BufferedReader sobre p.getInputStream(): readLine() hasta null
        │
 ⑥ ESPERAR        int code = p.waitFor();         → 0 = bien · otro = error
```

> [!danger] El paso ④ es el que todo el mundo olvida
> El hijo lee "hasta que no haya más líneas". ¿Cómo sabe que no hay más? **Porque el padre cierra la tubería.** Si no la cierras, el hijo sigue esperando, no escribe su resultado, y el padre se queda esperando ese resultado: los dos bloqueados para siempre. Es un **interbloqueo**, el del Tema 1, en la vida real.

**Otros métodos de `Process` que pueden caer:**

- `waitFor(5, TimeUnit.SECONDS)` → espera como mucho 5 segundos; devuelve `true` si el hijo terminó.
- `isAlive()` → ¿sigue vivo? (no espera).
- `exitValue()` → el código de salida, pero **sin esperar**: si el hijo sigue vivo, lanza `IllegalThreadStateException`.
- `destroy()` / `destroyForcibly()` → pedirle que termine / matarlo a la fuerza.
- `pid()` → su número de proceso.

**Las excepciones.** `start()`, `write()` y `readLine()` pueden lanzar `IOException`; `waitFor()` puede lanzar `InterruptedException`. Las dos son *checked*: o pones `throws` en el método, o un `try/catch`. Si capturas `InterruptedException`, lo correcto es llamar a `Thread.currentThread().interrupt();`.

---

## 2.5 El programa hijo

El hijo es un programa Java **normal y corriente**. Lo único especial es que:

- Recibe sus **argumentos** en `String[] args` (lo que va después del nombre de la clase en el comando).
- Lee sus datos de **`System.in`** (que ahora no es el teclado, sino la tubería del padre).
- Escribe el resultado en **`System.out`** (el padre lo lee con `getInputStream()`) y los errores en **`System.err`**.
- Termina con **`System.exit(0)`** si todo fue bien y **`System.exit(1)`** si hubo un error. Ese número es el que recibe el padre con `waitFor()`.
- Puede leer **variables de entorno** con `System.getenv("NOMBRE")`, que devuelve `null` si no existe.

> [!warning] `getenv` vs. `getProperty`
> - `System.getenv("DEBUG_MODE")` → **variable de entorno** del **sistema operativo**. El padre la pone con `pb.environment().put("DEBUG_MODE", "TRUE")`.
> - `System.getProperty("java.home")` → **propiedad de la JVM**. Las típicas son `java.home` (dónde está Java), `java.class.path` (dónde están tus `.class`), `os.name` y `user.dir`.

**El bucle de lectura del hijo**, que hay que saberse de memoria:

```java
BufferedReader input = new BufferedReader(
        new InputStreamReader(System.in, StandardCharsets.UTF_8));
String line;
while ((line = input.readLine()) != null) {   // null = el padre cerró la tubería
    // procesar la línea
}
```

`(line = input.readLine()) != null` hace dos cosas a la vez: **lee** una línea y la guarda en `line`, y **comprueba** que no sea `null`. `readLine()` devuelve `null` cuando **ya no hay más datos**, es decir, cuando el padre ha cerrado (paso ④).

> [!example]- 🔗 Fuente
> - [[2.2 - Gestión de subprocesos]] · [[2.3 - Flujos de comunicación]] · [[2.4 - Finalización de subprocesos]] · [[2.5 - Información sobre procesos]]
> - Guía: [[Guia examen temas 1 y 2#B.2 · Gestión de subprocesos|B.2 · Gestión de subprocesos]] · [[Guia examen temas 1 y 2#B.3 · Flujos de comunicación entre procesos|B.3 · Flujos]] · [[Guia examen temas 1 y 2#B.4 · Finalización de subprocesos|B.4 · Finalización]]
> - Programación básica: [[Programación basica/Tema 6/Excepciones#2. Try-catch|Excepciones → 2. Try-catch]] · [[Programación basica/Tema 6/Excepciones#7. Throws|Excepciones → 7. Throws]]

---

# Parte 3 · Método para completar una función

El profesor te dará el programa con una función vacía. Sigue estos **6 pasos** antes de escribir nada:

1. **Lee la firma** (la primera línea del método): `public String readResult(Process process) throws IOException`.
	- **Qué devuelve** (`String`): tienes que acabar con un `return` de ese tipo. Si es `void`, no hace falta `return`.
	- **Qué recibe** (`Process process`): es tu material de trabajo.
	- **Qué lanza** (`throws IOException`): si aparece, **no** necesitas `try/catch` para esa excepción.
2. **Lee el comentario o el enunciado** de esa función y **subraya los verbos**: *configurar*, *enviar*, *leer*, *esperar*, *cerrar*...
3. **Sitúa la función en el ciclo** de [[#2.4 El ciclo de vida de un subproceso]]: ¿es el paso ①, el ③-④, el ⑤ o el ⑥? Cada paso tiene su "plantilla" (Parte 4).
4. **Mira cómo se usa** la función en `run()` o en `main`: qué hacen con lo que devuelve y si se llama antes o después de `start()`.
5. **Escribe la plantilla** y adáptala a los nombres del enunciado.
6. **Repasa la lista de errores típicos**:
	- [ ] ¿He configurado **antes** de `start()`?
	- [ ] ¿He usado `getOutputStream` para escribir y `getInputStream` para leer?
	- [ ] ¿He hecho `newLine()` después de cada `write()`?
	- [ ] ¿He **cerrado** el writer (con `try-with-resources` o `close()`)?
	- [ ] ¿El bucle de lectura compara con `!= null`?
	- [ ] ¿He puesto el `return` con el tipo correcto?
	- [ ] ¿Las cadenas van entre comillas dobles y cada argumento del comando va por separado?

---

# Parte 4 · Recetario de funciones típicas

Cada receta tiene el enunciado tal como lo pondría el profesor, el **código con huecos** para hacerlo en papel y la **solución plegada**. Todas son métodos de instancia de las clases `MainAnalyzer` (padre) o `CharacterCounter` (hijo) del [[Examen año pasado]], y en la Parte 5 están todas juntas.

## R1 · Construir el comando portable (`buildCommand`)

> [!question] Enunciado
> Construye el comando para lanzar `CharacterCounter` con el modo recibido. Debe ser **portable**: la ruta de `java` se obtiene de la propiedad `java.home` y el classpath de `java.class.path`.

```java
public List<String> buildCommand(String mode) {
    String javaPath = System.____(1)____("java.home")
            + File.separator + "____(2)____" + File.separator + "java";
    String classPath = System.getProperty("____(3)____");

    List<String> command = new ArrayList<>();
    command.add(javaPath);
    command.add("____(4)____");
    command.add(classPath);
    command.add("CharacterCounter");
    command.add(____(5)____);
    return command;
}
```

> [!success]- Solución R1
> **(1)** `getProperty` · **(2)** `bin` · **(3)** `java.class.path` · **(4)** `-cp` · **(5)** `mode`
>
> **Por qué:** lo que quieres ejecutar es esto: `/ruta/a/java/bin/java -cp <classpath> CharacterCounter vowels`.
> - `java.home` es la carpeta donde está instalado Java, y el ejecutable está en su subcarpeta `bin`. `File.separator` es `/` en Linux y `\` en Windows: eso lo hace **portable**.
> - `-cp` (classpath) le dice a la JVM hija **dónde están los `.class`**. Le pasas el mismo que usa el padre, así que el hijo encuentra `CharacterCounter.class`.
> - Cada trozo del comando es **un elemento distinto** de la lista. Nunca pongas `"java -cp ..."` todo en un solo `String`.

## R2 · Configurar el contador de vocales

> [!question] Enunciado
> Configura un `ProcessBuilder` para el contador de vocales de manera que su **salida de error sea la misma que la de MainAnalyzer** y el modo de depuración esté activo (`DEBUG_MODE` = `TRUE`).

```java
public ProcessBuilder configureVowelCounter() {
    ProcessBuilder pb = new ProcessBuilder(buildCommand("vowels"));
    pb.redirectError(ProcessBuilder.Redirect.____(1)____);
    pb.____(2)____().put("____(3)____", "TRUE");
    return pb;
}
```

> [!success]- Solución R2
> **(1)** `INHERIT` · **(2)** `environment` · **(3)** `DEBUG_MODE`
>
> **Por qué:**
> - "La misma salida de error que el padre" = **heredarla** → `Redirect.INHERIT`. Así los mensajes `[PID: ...]` que el hijo escribe en `System.err` aparecen en la consola del padre.
> - `environment()` devuelve un `Map` con las variables de entorno **que tendrá el hijo**. Empieza siendo una copia de las del padre; con `put` añades la tuya. El hijo la leerá con `System.getenv("DEBUG_MODE")`.
> - **No** se llama a `start()` aquí: la función solo **configura** y devuelve el `ProcessBuilder`.

## R3 · Configurar el contador de consonantes

> [!question] Enunciado
> Configura un `ProcessBuilder` para el contador de consonantes con **directorio de trabajo** `./logs`. Sus errores se redirigirán al archivo `consonant_err.log` de ese directorio.

```java
public ProcessBuilder configureConsonantCounter() {
    ProcessBuilder pb = new ProcessBuilder(buildCommand("consonants"));
    File logs = new File("./logs");
    logs.mkdirs();
    pb.____(1)____(logs);
    pb.____(2)____(new File(logs, "consonant_err.log"));
    return pb;
}
```

> [!success]- Solución R3
> **(1)** `directory` · **(2)** `redirectError`
>
> **Por qué:**
> - `directory(File)` cambia la **carpeta en la que "vive"** el hijo (su `user.dir`). Las rutas relativas que use **el hijo** se resuelven desde ahí.
> - `redirectError(File)` manda su `stderr` a un fichero (equivale a `Redirect.to(file)`).
> - `logs.mkdirs()` crea la carpeta si no existe. Si no existe, `start()` falla con una `IOException`.

> [!warning] Detalle fino para el examen
> La ruta del fichero de `redirectError` se resuelve desde la carpeta **del padre**, no desde la del hijo. Por eso se construye como `new File(logs, "consonant_err.log")`, que da `./logs/consonant_err.log` sin depender de `directory()`.
> Por la misma razón, si el classpath es relativo (por ejemplo `.`), el hijo **ya no encontraría** sus clases dentro de `./logs`. En IntelliJ el classpath ya es una ruta absoluta; en la versión completa de la Parte 5 se convierte con `new File(...).getAbsolutePath()` por seguridad.

## R4 · Enviar las líneas al hijo (`sendLines`)

> [!question] Enunciado
> Envía al proceso, cadena a cadena (cada una como una línea), la lista recibida. Al terminar, **cierra la comunicación** para que el hijo deje de procesar líneas.

```java
public void sendLines(Process process, List<String> lines) throws IOException {
    try (BufferedWriter writer = new BufferedWriter(
            new ____(1)____(process.____(2)____(), StandardCharsets.UTF_8))) {
        for (String line : ____(3)____) {
            writer.____(4)____(line);
            writer.____(5)____();
        }
    }
}
```

> [!success]- Solución R4
> **(1)** `OutputStreamWriter` · **(2)** `getOutputStream` · **(3)** `lines` · **(4)** `write` · **(5)** `newLine`
>
> **Por qué:**
> - Para **escribirle** al hijo se usa `getOutputStream()` (lo que *sale* del padre), envuelto en `OutputStreamWriter` (caracteres → bytes) y en `BufferedWriter` (escribe de forma eficiente y tiene `newLine()`).
> - `newLine()` es imprescindible: el hijo lee con `readLine()`, que espera un salto de línea para saber que la línea ha terminado.
> - El **`try (...)`** cierra el writer al salir de las llaves. Ese cierre es el "**cerrar la comunicación**" que pide el enunciado: el `readLine()` del hijo devuelve `null` y su bucle termina.
> - Sin `try-with-resources` sería igual de válido escribir `writer.close();` al final del `for`.

## R5 · Leer el resultado del hijo (`readResult`)

> [!question] Enunciado
> Lee la línea de resultado que produce el contador y devuélvela.

```java
public String readResult(Process process) throws IOException {
    try (BufferedReader reader = new BufferedReader(
            new ____(1)____(process.____(2)____(), StandardCharsets.UTF_8))) {
        return reader.____(3)____();
    }
}
```

> [!success]- Solución R5
> **(1)** `InputStreamReader` · **(2)** `getInputStream` · **(3)** `readLine`
>
> **Por qué:** para **leer** lo que el hijo escribe en su `System.out` se usa `getInputStream()` (lo que *entra* al padre). Como el hijo escribe **una sola línea** (`Total vowels: 38`), basta con un `readLine()`.
>
> **Variante: leer todas las líneas.** Si el hijo escribe varias, se usa el bucle:
> ```java
> String line;
> StringBuilder all = new StringBuilder();
> while ((line = reader.readLine()) != null) {
>     all.append(line).append("\n");
> }
> return all.toString();
> ```

## R6 · Esperar al hijo y obtener su código de salida

> [!question] Enunciado
> Espera a que el proceso finalice y devuelve su valor de salida.

```java
public int waitAndGetExitCode(Process process) throws ____(1)____ {
    return process.____(2)____();
}
```

> [!success]- Solución R6
> **(1)** `InterruptedException` · **(2)** `waitFor`
>
> **Por qué:** `waitFor()` **bloquea** el programa padre hasta que el hijo termina y **devuelve** el número que el hijo pasó a `System.exit(...)`. Lanza `InterruptedException` (si alguien interrumpe la espera), que es *checked*: o la declaras con `throws` o la capturas.
>
> **Variante con tiempo máximo:**
> ```java
> if (process.waitFor(5, TimeUnit.SECONDS)) {
>     return process.exitValue();   // ya terminó: exitValue() es seguro
> }
> process.destroy();                // tarda demasiado: lo terminamos
> return -1;
> ```

## R7 · Hijo: validar los argumentos

> [!question] Enunciado
> `CharacterCounter` debe recibir **exactamente un** argumento, que será `"vowels"` o `"consonants"`. Si no, escribe `Error: Invalid mode` en la salida de error y termina con valor 1.

```java
public boolean validateArgs(String[] args) {
    if (args.____(1)____ != 1) {
        return false;
    }
    return args[0].____(2)____("vowels") ____(3)____ args[0].equals("consonants");
}

// en run(String[] args):
if (!validateArgs(args)) {
    System.____(4)____.println("Error: Invalid mode");
    System.exit(____(5)____);
}
```

> [!success]- Solución R7
> **(1)** `length` · **(2)** `equals` · **(3)** `||` · **(4)** `err` · **(5)** `1`
>
> **Por qué:**
> - `args.length` (sin paréntesis: es un **array**, no un `String`) dice cuántos argumentos llegaron. Hay que comprobarlo **antes** de mirar `args[0]`, porque si no hay ninguno, `args[0]` lanza `ArrayIndexOutOfBoundsException`.
> - Las cadenas se comparan con **`equals`**, nunca con `==`.
> - `||`: vale si es uno **o** el otro.
> - El error va por **`System.err`**, y `System.exit(1)` hace que el padre reciba `1` en su `waitFor()`.

## R8 · Hijo: comprobar `DEBUG_MODE`

> [!question] Enunciado
> Comprueba si existe la variable de entorno `DEBUG_MODE` y si vale `TRUE`.

```java
public boolean isDebug() {
    String value = System.____(1)____("DEBUG_MODE");
    return value ____(2)____ null && value.equals("____(3)____");
}
```

> [!success]- Solución R8
> **(1)** `getenv` · **(2)** `!=` · **(3)** `TRUE`
>
> **Por qué:** `getenv` devuelve `null` si la variable **no existe** (por ejemplo, en el contador de consonantes, al que no se le puso). Si llamaras a `value.equals(...)` con `value == null`, saltaría un `NullPointerException`. Por eso primero se comprueba `!= null`: el `&&` no evalúa la segunda parte si la primera es falsa.

## R9 · Hijo: contar vocales de una línea

> [!question] Enunciado
> Devuelve el número de vocales de la línea recibida.

```java
private static final String VOWELS = "aeiouáéíóúAEIOUÁÉÍÓÚ";

public int countVowels(String line) {
    int count = 0;
    for (int i = 0; i < line.____(1)____(); i++) {
        if (VOWELS.____(2)____(line.____(3)____(i)) >= 0) {
            count++;
        }
    }
    return ____(4)____;
}
```

> [!success]- Solución R9
> **(1)** `length` · **(2)** `indexOf` · **(3)** `charAt` · **(4)** `count`
>
> **Por qué:** se recorre la cadena letra a letra con `charAt(i)`. `VOWELS.indexOf(c)` busca la letra dentro de la cadena de vocales: devuelve su posición (0, 1, 2...) si está, o **-1** si no está. Por eso `>= 0` significa "es vocal".
> **Consonantes:** misma idea, pero contando las que son letra (`Character.isLetter(c)`) y **no** están en `VOWELS` (`indexOf(c) < 0`). Hay que comprobar lo de ser letra para no contar espacios ni signos.

## R10 · Hijo: bucle principal de lectura

> [!question] Enunciado
> Lee línea a línea la entrada estándar. Por cada línea, cuenta vocales o consonantes según el modo. Si está en depuración, escribe en la salida de error `[PID: 12345] Line parsed. Found n vowels`. Devuelve el total.

```java
public int processInput() throws IOException {
    int total = 0;
    BufferedReader input = new BufferedReader(
            new InputStreamReader(System.____(1)____, StandardCharsets.UTF_8));
    String line;
    while ((line = input.readLine()) ____(2)____) {
        int count = mode.equals("vowels") ? countVowels(line) : countConsonants(line);
        total += count;
        if (debug) {
            System.err.printf("[PID: %d] Line parsed. Found %d %s%n",
                    ProcessHandle.____(3)____().____(4)____(), count, mode);
        }
    }
    return total;
}
```

> [!success]- Solución R10
> **(1)** `in` · **(2)** `!= null` · **(3)** `current` · **(4)** `pid`
>
> **Por qué:**
> - El hijo lee de **`System.in`**, que está conectado a la tubería por la que escribe el padre.
> - `!= null` → el bucle sigue hasta que el padre **cierra** (R4).
> - `ProcessHandle.current()` es "yo mismo, el proceso actual", y `.pid()` da mi PID.
> - `condicion ? a : b` es el operador ternario: si el modo es `vowels` cuenta vocales y, si no, consonantes.
> - `mode` y `debug` son **atributos** de la clase, que se rellenan en `run()` (Parte 5).

---

# Parte 5 · El examen del año pasado montado entero

Estas son todas las recetas juntas, resolviendo el [[Examen año pasado]] completo. Está **compilado y probado**: imprime los dos PIDs, las líneas de depuración del contador de vocales, `Total vowels: 38`, `Total consonants: 42` y "Ambos procesos terminaron con éxito".

> [!note] Estilo
> Es POO como en el curso: atributos, constructor y **métodos de instancia**. `main` solo crea el objeto y llama a `run()`. Lo único `static` es `main` y la constante `VOWELS`.

### `CharacterCounter.java` (hijo)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class CharacterCounter {

    private static final String VOWELS = "aeiouáéíóúAEIOUÁÉÍÓÚ";

    private String mode;        // "vowels" o "consonants"
    private boolean debug;      // true si DEBUG_MODE vale TRUE

    // Comprueba que llega exactamente un argumento válido
    public boolean validateArgs(String[] args) {
        if (args.length != 1) {
            return false;
        }
        return args[0].equals("vowels") || args[0].equals("consonants");
    }

    // Lee la variable de entorno DEBUG_MODE
    public boolean isDebug() {
        String value = System.getenv("DEBUG_MODE");
        return value != null && value.equals("TRUE");
    }

    // Cuenta las vocales de una línea
    public int countVowels(String line) {
        int count = 0;
        for (int i = 0; i < line.length(); i++) {
            if (VOWELS.indexOf(line.charAt(i)) >= 0) {
                count++;
            }
        }
        return count;
    }

    // Cuenta las consonantes: letras que NO son vocales
    public int countConsonants(String line) {
        int count = 0;
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (Character.isLetter(c) && VOWELS.indexOf(c) < 0) {
                count++;
            }
        }
        return count;
    }

    // Bucle principal: lee de stdin hasta que el padre cierre la tubería
    public int processInput() throws IOException {
        int total = 0;
        BufferedReader input = new BufferedReader(
                new InputStreamReader(System.in, StandardCharsets.UTF_8));
        String line;
        while ((line = input.readLine()) != null) {
            int count = mode.equals("vowels") ? countVowels(line) : countConsonants(line);
            total += count;
            if (debug) {
                System.err.printf("[PID: %d] Line parsed. Found %d %s%n",
                        ProcessHandle.current().pid(), count, mode);
            }
        }
        return total;
    }

    public void run(String[] args) {
        if (!validateArgs(args)) {
            System.err.println("Error: Invalid mode");
            System.exit(1);
        }
        mode = args[0];
        debug = isDebug();
        try {
            int total = processInput();
            System.out.println("Total " + mode + ": " + total);
            System.exit(0);
        } catch (IOException e) {
            System.err.println("Error de lectura: " + e.getMessage());
            System.exit(1);
        }
    }

    public static void main(String[] args) {
        new CharacterCounter().run(args);
    }
}
```

### `MainAnalyzer.java` (padre)

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class MainAnalyzer {

    private final List<String> text;

    public MainAnalyzer() {
        // Lista de cadenas que simula el texto a analizar
        text = List.of(
                "En un lugar de la Mancha",
                "de cuyo nombre no quiero acordarme",
                "no ha mucho tiempo que vivia un hidalgo");
    }

    // Construye el comando portable: java -cp <classpath> CharacterCounter <modo>
    public List<String> buildCommand(String mode) {
        String javaPath = System.getProperty("java.home")
                + File.separator + "bin" + File.separator + "java";
        // Ruta absoluta: si el hijo cambia de directorio, un classpath relativo dejaría de valer
        String classPath = new File(System.getProperty("java.class.path")).getAbsolutePath();

        List<String> command = new ArrayList<>();
        command.add(javaPath);
        command.add("-cp");
        command.add(classPath);
        command.add("CharacterCounter");
        command.add(mode);
        return command;
    }

    // Contador de vocales: stderr compartido con el padre y DEBUG_MODE=TRUE
    public ProcessBuilder configureVowelCounter() {
        ProcessBuilder pb = new ProcessBuilder(buildCommand("vowels"));
        pb.redirectError(ProcessBuilder.Redirect.INHERIT);
        pb.environment().put("DEBUG_MODE", "TRUE");
        return pb;
    }

    // Contador de consonantes: directorio ./logs y stderr a un fichero
    public ProcessBuilder configureConsonantCounter() {
        ProcessBuilder pb = new ProcessBuilder(buildCommand("consonants"));
        File logs = new File("./logs");
        logs.mkdirs();                       // si no existe, start() fallaría
        pb.directory(logs);
        pb.redirectError(new File(logs, "consonant_err.log"));
        return pb;
    }

    // Envía cada cadena como una línea y CIERRA la entrada del hijo
    public void sendLines(Process process, List<String> lines) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(
                new OutputStreamWriter(process.getOutputStream(), StandardCharsets.UTF_8))) {
            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }
        }   // aquí se cierra el flujo: el hijo recibe "fin de datos" (readLine devuelve null)
    }

    // Lee la línea de resultado que escribe el hijo en su stdout
    public String readResult(Process process) throws IOException {
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8))) {
            return reader.readLine();
        }
    }

    // Espera a que termine el hijo y devuelve su código de salida
    public int waitAndGetExitCode(Process process) throws InterruptedException {
        return process.waitFor();
    }

    public void run() {
        try {
            Process vowels = configureVowelCounter().start();
            Process consonants = configureConsonantCounter().start();

            System.out.println("PID vowel counter: " + vowels.pid());
            System.out.println("PID consonant counter: " + consonants.pid());

            sendLines(vowels, text);
            sendLines(consonants, text);

            String vowelResult = readResult(vowels);
            String consonantResult = readResult(consonants);

            int vowelExit = waitAndGetExitCode(vowels);
            int consonantExit = waitAndGetExitCode(consonants);

            System.out.println("Vowel Result: " + vowelResult);
            System.out.println("Consonant Result: " + consonantResult);
            if (vowelExit == 0 && consonantExit == 0) {
                System.out.println("Ambos procesos terminaron con éxito.");
            } else {
                System.out.println("Algún proceso falló (vowels=" + vowelExit
                        + ", consonants=" + consonantExit + ").");
            }
        } catch (IOException e) {
            System.err.println("Error de E/S: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("Se interrumpió la espera.");
        }
    }

    public static void main(String[] args) {
        new MainAnalyzer().run();
    }
}
```

> [!note]- 🧠 Por qué `run()` sigue este orden
> 1. **Arranca los dos** hijos antes de mandarles nada: así trabajan **a la vez** (concurrencia, Tema 1).
> 2. **Envía y cierra** (R4) a cada uno. Tras el cierre, cada hijo termina su bucle y escribe su `Total ...`.
> 3. **Lee** el resultado de cada uno (R5).
> 4. **Espera** (R6) y obtiene los códigos de salida. Se hace al final, cuando ya se han leído las salidas, para no dejar ninguna tubería llena sin leer.
> 5. Comprueba que **ambos** códigos sean `0`.

> [!tip] Cómo probarlo tú
> En IntelliJ: crea un proyecto, pon las dos clases en `src/` (sin paquete) y ejecuta `MainAnalyzer`. Desde la terminal: `javac *.java && java MainAnalyzer`. Si te dice que `javac` no existe, instala el JDK con `sudo pacman -S jdk-openjdk`.

---

# Chuleta de una página

**Tema 1 en 10 frases:**
1. Programa = **estático** (en disco) · proceso = **dinámico** (en ejecución, con su **PID**).
2. Paralelismo = **real** (≥2 núcleos) · multiprogramación = **turnos** · multitarea = lo que **percibe el usuario**.
3. Cambio de **contexto** = guardar uno y restaurar otro; **no acelera**.
4. Multiprocesamiento = memoria **compartida** (SMP iguales / AMP maestro-esclavo) · distribuido = memoria **propia** + red (cluster).
5. Estados: nuevo → listo ⇄ ejecución → bloqueado → listo · **apropiación** = se acabó el quantum.
6. Independientes (nada) · cooperantes (**comunicación**) · competidores (**sincronización**).
7. Data race = misma variable + **alguien escribe** + sin sincronizar.
8. Sección crítica = el baño · exclusión mutua = solo uno · mutex = la llave · monitor = `synchronized` + `wait`/`notify`.
9. Simplex (una dirección) · half duplex (por turnos) · full duplex (a la vez) · síncrona (espero) · asíncrona (sigo).
10. Seguridad = que no pase lo malo · viveza = que pase lo bueno · Coffman = exclusión mutua + retención y espera + **no apropiación** + espera circular.

**Tema 2: la receta:**

```java
ProcessBuilder pb = new ProcessBuilder(javaPath, "-cp", classPath, "Hijo", "arg");
pb.directory(new File("./carpeta"));                 // ① configurar (ANTES de start)
pb.environment().put("VAR", "VALOR");
pb.redirectError(ProcessBuilder.Redirect.INHERIT);   //    o new File("err.log")
Process p = pb.start();                              // ② arrancar · p.pid()

try (BufferedWriter w = new BufferedWriter(           // ③ escribir
        new OutputStreamWriter(p.getOutputStream(), StandardCharsets.UTF_8))) {
    w.write("línea"); w.newLine();
}                                                    // ④ cerrar (fin de datos)

try (BufferedReader r = new BufferedReader(           // ⑤ leer
        new InputStreamReader(p.getInputStream(), StandardCharsets.UTF_8))) {
    String line;
    while ((line = r.readLine()) != null) { /* ... */ }
}
int code = p.waitFor();                              // ⑥ esperar · 0 = OK
```

**Hijo:** `args.length` · `args[0].equals(...)` · `System.getenv("VAR")` (puede ser `null`) · leer `System.in` hasta `null` · resultado a `System.out` · errores a `System.err` · `System.exit(0 / 1)`.

**Propiedades:** `java.home` (dónde está Java) · `java.class.path` (dónde están los `.class`) · `os.name` · `user.dir`.

---

## Para repasar

- [ ] Explicar con mis palabras programa vs. proceso, y paralelismo vs. multiprogramación.
- [ ] Decir de memoria las 46 [[#Todas las palabras de los huecos]], sobre todo las ⚠️.
- [ ] Aplicar el método de descarte en 4 pasos de [[#Trucos en caso de duda]] a un cuestionario.
- [ ] Dibujar el ciclo de estados de un proceso.
- [ ] Explicar por qué `x = x + 1` con dos hilos puede dar 1.
- [ ] Nombrar las 4 condiciones de Coffman y los 4 problemas (deadlock, livelock, inanición, inversión).
- [ ] Dibujar las 3 tuberías y decir qué método uso para escribir y cuál para leer.
- [ ] Recitar los 6 pasos del ciclo de vida de un subproceso y explicar por qué el ④ es obligatorio.
- [ ] Hacer en papel las recetas R1–R10 sin mirar la solución.
- [ ] Escribir `MainAnalyzer` entero en papel en menos de 20 minutos.

## Guía relacionada

- 🧠 **Teoría y chuleta** (para consultar detalles) → [[Guia examen temas 1 y 2]]
- ✅ **Test de repaso** (examen del jueves) → [[Test de repaso temas 1 y 2]]
- 💻 **Prácticos resueltos** (examen del viernes) → [[Practicos temas 1 y 2]]

## Relaciones

- [[DAM/Programacion_de_Servicios_y_Procesos/Indice|Índice de PSyP]]
- [[Examen año pasado]] — enunciado del práctico resuelto en la Parte 5
- [[2.Repaso - Ejercicio filtro con subproceso]] · [[2.Respaso - Listar archivos con Runtime]] — otros ejercicios padre-hijo
- [[Programación basica/Indice|Programación básica]] — estilo de código Java del curso
