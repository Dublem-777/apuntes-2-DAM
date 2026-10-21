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

# Simulacros tipo test · Tema 1

> [!info] Alcance
> **174 preguntas** repartidas en **8 simulacros**, uno por apartado del Tema 1 (1.1 – 1.8). Son las preguntas de los cuestionarios Moodle (carpeta `Cuestionarios/`) pasadas al formato del [[Test de repaso temas 1 y 2|test de repaso]]: cada respuesta está plegada, razona por qué fallan las demás opciones y enlaza al apunte. Las preguntas marcadas con ⚠️ son las que fallaste en Moodle.

> [!tip] Cómo hacer un simulacro
> 1. Elige un simulacro y pon un cronómetro (unos **30 s por pregunta**).
> 2. Apunta tus respuestas en un papel **sin abrir** ningún desplegable de **Respuesta**.
> 3. Al terminar, corrige con la **Hoja de respuestas** plegada al final del simulacro.
> 4. Abre solo la respuesta de las preguntas falladas, lee el *Por qué* y sigue el enlace al apunte.
> 5. Anota el resultado en [[#Registro de resultados]] y repite los simulacros con peor nota.

> [!tip] Material de preparación
> - [[Guia examen temas 1 y 2|🧠 Teoría y chuleta]]
> - [[Test de repaso temas 1 y 2|✅ Test de repaso]]
> - [[Simulacros tipo test tema 1|⏱️ Simulacros tipo test]]
> - [[Practicos temas 1 y 2|💻 Prácticos resueltos]]

## Índice de simulacros

- [[#Simulacro 1 · 1.1 · Programa vs. proceso]] — 40 preguntas
- [[#Simulacro 2 · 1.2 · Computación concurrente]] — 20 preguntas
- [[#Simulacro 3 · 1.3 · Procesos en el sistema operativo]] — 16 preguntas
- [[#Simulacro 4 · 1.4 · Técnicas de programación concurrente]] — 20 preguntas
- [[#Simulacro 5 · 1.5 · Orden de ejecución]] — 19 preguntas
- [[#Simulacro 6 · 1.6 · Sincronización]] — 20 preguntas
- [[#Simulacro 7 · 1.7 · Comunicación entre procesos]] — 19 preguntas
- [[#Simulacro 8 · 1.8 · Corrección en los programas concurrentes]] — 20 preguntas
- [[#Registro de resultados]]

## Preguntas (auto-test)

### Simulacro 1 · 1.1 · Programa vs. proceso

> [!abstract] Simulacro 1
> **40 preguntas** · ⏱️ ~20 min · Fuente: [[Cuestionario 1-1]] · [[1.1 - Programa vs. Proceso|Apuntes del 1.1]] · Tu nota en Moodle: **38/40**

> [!question] P1 · Servicio o demonio de aplicación
> ¿Cuál de las siguientes opciones constituye un ejemplo típico de **servicio o demonio de aplicación**?
> - a. Un archivo de texto con extensión `.txt` almacenado en el escritorio.
> - b. Un servidor de bases de datos como MySQL o PostgreSQL atendiendo peticiones en segundo plano.
> - c. El videojuego Pac-Man en ejecución con gráficos a pantalla completa.
> - d. El menú de inicio de sesión visual del sistema operativo.

> [!success]- Respuesta
>
> - b. ✅ Un servidor de bases de datos como MySQL o PostgreSQL atendiendo peticiones en segundo plano.
>
> *Por qué:* los servidores de bases de datos o web (MySQL, PostgreSQL, Apache) son **servicios de aplicación** que corren en segundo plano dando soporte a otras aplicaciones. Un `.txt` no es ni siquiera un programa; Pac-Man y el menú de inicio de sesión son interactivos y en primer plano. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P2 · Permiso de ejecución en Unix
> En los sistemas basados en GNU/Linux o macOS, un fichero se reconoce como ejecutable si tiene activado en sus metadatos el permiso de ______.

> [!success]- Respuesta
>
> - **ejecución** (o ejecucion)
>
> *Por qué:* en GNU/Linux y macOS un fichero es ejecutable por su **permiso de ejecución** (`+x`), no por la extensión como en Windows (`.exe`). [[1.1 - Programa vs. Proceso#2. Ejecutable|Ver 1.1 · Ejecutable]]

> [!question] P3 · Intérprete
> El programa encargado de tomar el código intermedio (o script) y traducir sus instrucciones al lenguaje máquina durante el tiempo de ejecución se conoce como ______.

> [!success]- Respuesta
>
> - **intérprete** (o interprete)
>
> *Por qué:* el **intérprete** (o la máquina virtual) traduce el código intermedio o el script a lenguaje máquina **en tiempo de ejecución**; el compilador, en cambio, lo hace todo **antes**. [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]

> [!question] P4 · Firmware ⚠️
> Dentro de los programas para la gestión del hardware, el software básico grabado en memorias no volátiles que controla directamente los circuitos de un periférico o placa base se conoce como ______.

> [!success]- Respuesta
>
> - **firmware**
>
> *Por qué:* el **firmware** es el software básico grabado en memoria no volátil que controla directamente el hardware (BIOS/UEFI, controladora de un periférico). No confundir con el *driver*, que se carga desde el SO. [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P5 · Fichero ejecutable
> Un ______ es un fichero que contiene el código binario o interpretado capaz de ser ejecutado de forma directa por un ordenador o por una máquina virtual.

> [!success]- Respuesta
>
> - **ejecutable** (o fichero ejecutable)
>
> *Por qué:* un **ejecutable** contiene código binario (lo ejecuta la CPU) o interpretado (lo ejecuta una máquina virtual o un intérprete). [[1.1 - Programa vs. Proceso#2. Ejecutable|Ver 1.1 · Ejecutable]]

> [!question] P6 · Proceso
> En sistemas operativos, la entidad dinámica que representa un programa en ejecución con recursos asignados recibe el nombre de ______.

> [!success]- Respuesta
>
> - **proceso**
>
> *Por qué:* el **proceso** es la entidad dinámica: un programa en ejecución con recursos asignados (memoria, PID, contexto). [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P7 · Delegar la impresión en un servicio
> ¿Qué ventaja clave proporciona a las aplicaciones de usuario (como procesadores de texto) delegar la impresión en un servicio del sistema operativo?
> - a. Garantiza que el documento se guarde automáticamente en formato ejecutable nativo.
> - b. Fuerza a la aplicación a cerrarse inmediatamente para liberar toda su memoria RAM.
> - c. Evita que la aplicación tenga que gestionar la comunicación a bajo nivel y la memoria limitada de la impresora física.
> - d. Permite que el texto se traduzca de forma automática a código ensamblador.

> [!success]- Respuesta
>
> - c. ✅ Evita que la aplicación tenga que gestionar la comunicación a bajo nivel y la memoria limitada de la impresora física.
>
> *Por qué:* la aplicación entrega el documento al servicio de impresión y sigue trabajando: **no tiene que gestionar el protocolo de bajo nivel ni la memoria limitada de la impresora**. Las demás opciones no tienen relación con la impresión (formato ejecutable, cerrar la app, traducir a ensamblador). [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P8 · Spooler sin trabajos pendientes
> ¿Qué sucede con el **servicio de impresión (spooler)** cuando no existen trabajos pendientes en su cola?
> - a. Genera impresiones de prueba continuas para verificar que el hardware no se desconecte.
> - b. Queda a la espera de peticiones entrantes y puede ordenar a la impresora pasar a estado standby.
> - c. Se destruye permanentemente del disco duro para liberar espacio de almacenamiento.
> - d. Ocupa el 100% de los ciclos de CPU en un bucle activo indefinido.

> [!success]- Respuesta
>
> - b. ✅ Queda a la espera de peticiones entrantes y puede ordenar a la impresora pasar a estado standby.
>
> *Por qué:* sin trabajos el servicio **queda a la espera** (bloqueado, sin gastar CPU) y puede poner la impresora en *standby*. Un servicio nunca ocupa el 100 % de CPU en espera activa ni se borra del disco, y tampoco imprime pruebas sin que se lo pidan. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P9 · Bytecode
> El código intermedio que genera el compilador de Java y que es interpretado posteriormente por la Máquina Virtual Java (JVM) se denomina ______.

> [!success]- Respuesta
>
> - **bytecode**
>
> *Por qué:* `javac` genera **bytecode** (`.class`), que la JVM interpreta (o compila JIT) en tiempo de ejecución. [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]

> [!question] P10 · Definición de software
> ¿Cómo se define de manera general el concepto de **software** en el ámbito informático?
> - a. Cualquier fichero almacenado de forma permanente en un disco de estado sólido.
> - b. Únicamente el sistema operativo principal que administra la memoria RAM.
> - c. La circuitería física encargada de procesar las señales binarias.
> - d. El conjunto de programas informáticos que se ejecutan sobre el hardware del equipo.

> [!success]- Respuesta
>
> - d. ✅ El conjunto de programas informáticos que se ejecutan sobre el hardware del equipo.
>
> *Por qué:* el **software** es el conjunto de programas que se ejecutan sobre el hardware. No es "cualquier fichero" (un `.txt` no es software ejecutable), ni solo el SO, ni la circuitería (eso es el hardware). [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]

> [!question] P11 · Proceso: entidad…
> En contraposición a la naturaleza pasiva y estática de un programa, el proceso se caracteriza por ser una entidad ______.

> [!success]- Respuesta
>
> - **dinámica** (o dinamica / activa)
>
> *Por qué:* el programa es **estático y pasivo**; el proceso es **dinámico y activo**. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P12 · Estado de reposo de la impresora
> Cuando en la cola de impresión no existen trabajos pendientes, el servicio de impresión puede ordenar a la impresora pasar al estado de reposo o ______.

> [!success]- Respuesta
>
> - **standby** (o reposo / espera)
>
> *Por qué:* con la cola vacía el servicio puede ordenar a la impresora pasar a **standby** (reposo). [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P13 · Ejecutables binarios ⚠️
> Los ejecutables formados por un conjunto de instrucciones que son procesadas directamente por la CPU sin un software intermediario se denominan ejecutables ______.

> [!success]- Respuesta
>
> - **binarios** (o binario)
>
> *Por qué:* los ejecutables **binarios** contienen instrucciones que la CPU procesa directamente, sin intérprete. Son los que genera un compilador nativo (C, C++). [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P14 · Aplicación
> Una ______ es un tipo de programa informático diseñado como herramienta para resolver de manera automática un problema específico del usuario.

> [!success]- Respuesta
>
> - **aplicación** (o aplicacion)
>
> *Por qué:* una **aplicación** es un programa orientado a resolver un problema concreto del usuario final (procesador de textos, navegador…). [[1.1 - Programa vs. Proceso#1.2 Aplicación|Ver 1.1 · Aplicación]]

> [!question] P15 · Tres ventanas de Chrome
> Si un usuario abre tres ventanas independientes de Google Chrome para navegar por diferentes páginas web, ¿qué ocurre en el sistema operativo?
> - a. Se ejecutan múltiples procesos independientes en memoria asociados al mismo programa estático en disco.
> - b. El sistema operativo fusiona las tres ventanas en un único hilo indivisible.
> - c. Se crean tres copias idénticas del fichero ejecutable en el disco duro con nombres distintos.
> - d. El ejecutable se transforma temporalmente en un servicio del sistema operativo.

> [!success]- Respuesta
>
> - a. ✅ Se ejecutan múltiples procesos independientes en memoria asociados al mismo programa estático en disco.
>
> *Por qué:* hay **un solo programa** en disco y **varios procesos** independientes en memoria, cada uno con su PID y su contexto. No se copia el ejecutable ni se convierte en servicio, y los procesos no se "fusionan" en un hilo. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P16 · Compilador
> La herramienta de traducción que toma el código fuente y lo traduce por completo a código máquina nativo antes de su ejecución se denomina ______.

> [!success]- Respuesta
>
> - **compilador**
>
> *Por qué:* el **compilador** traduce todo el código fuente a código máquina **antes** de ejecutarlo; el intérprete lo hace durante la ejecución. [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]

> [!question] P17 · PID
> El identificador numérico único que el sistema operativo asigna a cada proceso en ejecución para su control y seguimiento se conoce por las siglas ______.

> [!success]- Respuesta
>
> - **PID** (Process Identifier)
>
> *Por qué:* el **PID** (*Process Identifier*) es el número único con el que el SO identifica y controla cada proceso. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P18 · Software
> En general, conocemos como ______ al conjunto de programas informáticos que se ejecutan sobre el hardware del equipo.

> [!success]- Respuesta
>
> - **software**
>
> *Por qué:* **software** = conjunto de programas que se ejecutan sobre el hardware. [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]

> [!question] P19 · Ejecutables binarios: portabilidad
> ¿Cuál es una característica intrínseca fundamental de los **ejecutables binarios** compilados de forma nativa?
> - a. Contienen texto legible en lenguaje ensamblador que el sistema operativo traduce línea a línea.
> - b. Son multiplataforma por naturaleza y se ejecutan en cualquier CPU sin necesidad de adaptación previa.
> - c. Están vinculados a una arquitectura de procesador específica y requieren recompilación para ejecutarse en arquitecturas incompatibles.
> - d. Requieren obligatoriamente la presencia de un entorno virtual como la JVM para ser procesados.

> [!success]- Respuesta
>
> - c. ✅ Están vinculados a una arquitectura de procesador específica y requieren recompilación para ejecutarse en arquitecturas incompatibles.
>
> *Por qué:* el código máquina depende del juego de instrucciones (x86_64, ARM…), así que el binario **solo funciona en su arquitectura** y hay que recompilarlo para otra. No es texto ensamblador, no es multiplataforma y no necesita JVM (eso son los interpretados). [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]

> [!question] P20 · Qué es un fichero ejecutable
> ¿Qué define de forma precisa a un **fichero ejecutable**?
> - a. Cualquier documento protegido contra escritura dentro del sistema de ficheros.
> - b. Un fichero con código binario o interpretado capaz de ser ejecutado por el procesador o por una máquina virtual.
> - c. Un bloque de memoria RAM asignado a la pila de llamadas del sistema operativo.
> - d. Un archivo de texto estructurado con directivas de configuración que lee el kernel.

> [!success]- Respuesta
>
> - b. ✅ Un fichero con código binario o interpretado capaz de ser ejecutado por el procesador o por una máquina virtual.
>
> *Por qué:* ejecutable = código **binario** (CPU) o **interpretado** (máquina virtual). Estar protegido contra escritura, ser un bloque de RAM o un fichero de configuración no lo hace ejecutable. [[1.1 - Programa vs. Proceso#2. Ejecutable|Ver 1.1 · Ejecutable]]

> [!question] P21 · Demonios: segundo plano
> Los demonios y servicios trabajan de forma invisible para el usuario final porque se ejecutan en ______ plano.

> [!success]- Respuesta
>
> - **segundo** (o segundo plano / background)
>
> *Por qué:* demonios y servicios se ejecutan en **segundo plano** (*background*), sin interfaz con el usuario. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P22 · Demonio en Windows
> En los sistemas operativos Windows, el término equivalente a demonio que describe un proceso en segundo plano de larga duración es ______.

> [!success]- Respuesta
>
> - **servicio**
>
> *Por qué:* en Windows se llaman **servicios**; en Unix/Linux, **demonios** (*daemons*). [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P23 · Gestión de demonios sin GUI
> Si los demonios y servicios no disponen de interfaz gráfica directa, ¿cómo suele gestionarse su configuración o estado?
> - a. Modificando físicamente los microchips de la memoria ROM.
> - b. Únicamente apagando y encendiendo el interruptor eléctrico del equipo.
> - c. No es posible gestionarlos una vez iniciados; son completamente inmutables hasta reinstalar el sistema.
> - d. A través de herramientas de administración del sistema operativo o mediante otras aplicaciones cliente intermediarias.

> [!success]- Respuesta
>
> - d. ✅ A través de herramientas de administración del sistema operativo o mediante otras aplicaciones cliente intermediarias.
>
> *Por qué:* se configuran con **herramientas de administración del SO** (`systemctl`, consola de servicios) o con aplicaciones cliente que hacen de intermediarias. Sí se pueden gestionar en caliente; no hace falta tocar la ROM ni apagar el equipo. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P24 · Carga de servicios esenciales
> La gran mayoría de servicios y demonios esenciales del sistema operativo se configuran para ser cargados automáticamente durante la secuencia de ______ del sistema.

> [!success]- Respuesta
>
> - **arranque** (o inicio / boot)
>
> *Por qué:* la mayoría de servicios esenciales se cargan durante el **arranque** (*boot*) del sistema. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P25 · Programa desde el punto de vista del SO
> Desde la perspectiva técnica de un sistema operativo, ¿qué representa exactamente un **programa**?
> - a. La representación estática en disco de una aplicación, que contiene código y datos asociados.
> - b. Una instancia activa con asignación dinámica de memoria y registros de CPU.
> - c. Un archivo de texto plano con código fuente editable por el usuario.
> - d. Un hilo de ejecución en segundo plano que carece de interfaz gráfica.

> [!success]- Respuesta
>
> - a. ✅ La representación estática en disco de una aplicación, que contiene código y datos asociados.
>
> *Por qué:* para el SO, un **programa** es la representación **estática en disco** con código y datos. Una instancia activa con memoria y registros es un proceso; el código fuente editable aún no es el programa ejecutable, y un hilo en segundo plano es otra cosa. [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]

> [!question] P26 · Servicio que gestiona la cola de impresión
> El servicio del sistema operativo que gestiona la cola de documentos y dosifica los datos hacia la impresora física se denomina servicio de ______.

> [!success]- Respuesta
>
> - **impresión** (o impresion / spooler)
>
> *Por qué:* el **servicio de impresión** (*spooler*) recibe los trabajos, los encola y dosifica los datos a la impresora. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P27 · Analogía del libro de cocina
> En la clásica analogía pedagógica del libro de cocina empleada para explicar la concurrencia, ¿qué elemento corresponde al **programa** y cuál al **proceso**?
> - a. La receta escrita es el programa (estático); el cocinero preparando activamente la receta es el proceso (dinámico).
> - b. El restaurante completo es el proceso y el cliente sentado es el programa.
> - c. El libro de recetas es el proceso y los ingredientes almacenados son el programa.
> - d. El cocinero es el programa y la sartén es el proceso.

> [!success]- Respuesta
>
> - a. ✅ La receta escrita es el programa (estático); el cocinero preparando activamente la receta es el proceso (dinámico).
>
> *Por qué:* la **receta** (instrucciones escritas, estáticas) es el programa; el **cocinero preparándola** con los ingredientes es el proceso. El resto de opciones asignan papeles que no encajan con estático/dinámico. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P28 · Librería o biblioteca
> Una ______ (o biblioteca) contiene código ejecutable modular y reutilizable por múltiples programas para evitar reescribir funciones comunes.

> [!success]- Respuesta
>
> - **librería** (o libreria / biblioteca)
>
> *Por qué:* una **librería** contiene código reutilizable por varios programas (`.dll`, `.so`, `.jar`). [[1.1 - Programa vs. Proceso#2.3 Librerías|Ver 1.1 · Librerías]]

> [!question] P29 · Qué es un demonio o servicio
> ¿Qué caracteriza esencialmente a un **demonio** (en entornos UNIX) o **servicio** (en Windows)?
> - a. Un programa malicioso cuyo único objetivo es sobrecargar los núcleos de la CPU.
> - b. Un proceso que se ejecuta continuamente en segundo plano, en espera de peticiones o eventos, sin interactuar directamente con el usuario.
> - c. Una ventana interactiva en primer plano diseñada para recibir eventos de ratón y teclado.
> - d. Un script que solo puede ejecutarse de forma puntual antes del inicio de sesión del usuario.

> [!success]- Respuesta
>
> - b. ✅ Un proceso que se ejecuta continuamente en segundo plano, en espera de peticiones o eventos, sin interactuar directamente con el usuario.
>
> *Por qué:* proceso **de larga duración, en segundo plano**, que espera peticiones o eventos sin interactuar con el usuario. No es malware, no tiene ventana interactiva y no se limita a ejecutarse una vez antes del login. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P30 · Definición de proceso
> ¿Cómo define la teoría de sistemas operativos a un **proceso**?
> - a. Una entidad dinámica que representa en el sistema operativo la ejecución activa de un programa.
> - b. El código estático almacenado de forma permanente en un sector de disco.
> - c. Un dispositivo de hardware dedicado exclusivamente al cálculo concurrente.
> - d. El documento de texto que contiene las directivas del compilador.

> [!success]- Respuesta
>
> - a. ✅ Una entidad dinámica que representa en el sistema operativo la ejecución activa de un programa.
>
> *Por qué:* proceso = **entidad dinámica** que representa la ejecución de un programa. El código estático en disco es el programa; ni un dispositivo hardware ni las directivas del compilador son procesos. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P31 · Demonio en Unix
> En entornos UNIX y Linux, un tipo de proceso que se ejecuta continuamente en segundo plano a la espera de eventos sin interactuar de forma directa con el usuario se denomina ______.

> [!success]- Respuesta
>
> - **demonio** (o daemon / servicio)
>
> *Por qué:* en Unix/Linux, el proceso en segundo plano que espera eventos es un **demonio** (*daemon*). [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P32 · Papel del intérprete o máquina virtual
> En el contexto de los lenguajes interpretados o basados en bytecode (como Java o Python), ¿cuál es el papel principal del **intérprete o máquina virtual**?
> - a. Sustituir al sistema operativo administrando los controladores físicos de la placa base.
> - b. Compilar de forma permanente el código a un fichero `.exe` en el disco duro antes de cada inicio.
> - c. Eliminar los errores lógicos del algoritmo del programador en tiempo de compilación.
> - d. Tomar los códigos de operación intermedios y traducirlos al lenguaje máquina que el procesador físico ejecuta.

> [!success]- Respuesta
>
> - d. ✅ Tomar los códigos de operación intermedios y traducirlos al lenguaje máquina que el procesador físico ejecuta.
>
> *Por qué:* traduce los **códigos intermedios** (bytecode, script) a instrucciones máquina que ejecuta la CPU. No sustituye al SO, no genera un `.exe` permanente y no corrige errores lógicos del programador. [[1.1 - Programa vs. Proceso#2.1 Clasificación según el tipo de código|Ver 1.1 · Tipos de código]]

> [!question] P33 · Cuándo arrancan los demonios
> ¿Cuándo suelen iniciarse y activarse con mayor frecuencia los demonios y servicios esenciales del sistema operativo?
> - a. Únicamente cuando el usuario final hace doble clic sobre un icono en el escritorio.
> - b. Automáticamente durante la secuencia de arranque o inicio del sistema operativo.
> - c. Solo cuando el disco duro alcanza el 100% de su capacidad disponible.
> - d. Exclusivamente al momento de apagar el equipo antes de cortar la energía.

> [!success]- Respuesta
>
> - b. ✅ Automáticamente durante la secuencia de arranque o inicio del sistema operativo.
>
> *Por qué:* los servicios esenciales se inician **automáticamente en el arranque** del sistema, no al hacer doble clic, ni al llenarse el disco, ni al apagar. [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P34 · Programa
> Desde la perspectiva del sistema operativo, llamamos ______ a la representación estática en disco de una aplicación, que contiene tanto el código como los datos que maneja.

> [!success]- Respuesta
>
> - **programa**
>
> *Por qué:* el **programa** es la representación estática y pasiva en disco (código + datos). [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]

> [!question] P35 · Programa vs. proceso
> Considerando la dicotomía entre programa y proceso, ¿cuál de las siguientes afirmaciones es correcta?
> - a. Ambos son entidades estáticas que únicamente difieren en su extensión de archivo.
> - b. Ambos son entidades dinámicas creadas durante el arranque de la BIOS.
> - c. El programa es una entidad estática y pasiva, mientras que el proceso es una entidad dinámica y activa.
> - d. El proceso es estático en disco y el programa es dinámico en el procesador.

> [!success]- Respuesta
>
> - c. ✅ El programa es una entidad estática y pasiva, mientras que el proceso es una entidad dinámica y activa.
>
> *Por qué:* **programa estático y pasivo / proceso dinámico y activo**. Las demás opciones o los igualan (los dos estáticos o los dos dinámicos) o invierten los papeles. [[1.1 - Programa vs. Proceso#3. Proceso|Ver 1.1 · Proceso]]

> [!question] P36 · Programa vs. aplicación
> ¿Cuál es la diferencia conceptual primordial entre un **programa** y una **aplicación**?
> - a. La aplicación es un tipo de programa enfocado específicamente en resolver un problema o necesidad del usuario final.
> - b. Las aplicaciones residen solo en memoria RAM, mientras que los programas habitan únicamente en la CPU.
> - c. El programa siempre se compila a binario nativo, mientras que la aplicación siempre es interpretada.
> - d. Un programa incluye exclusivamente código del kernel; todo lo demás se cataloga como aplicación.

> [!success]- Respuesta
>
> - a. ✅ La aplicación es un tipo de programa enfocado específicamente en resolver un problema o necesidad del usuario final.
>
> *Por qué:* toda aplicación es un programa, pero **orientado al usuario final** para resolver una necesidad concreta. No se diferencian por RAM/CPU, por compilado/interpretado ni por ser código del kernel. [[1.1 - Programa vs. Proceso#1.2 Aplicación|Ver 1.1 · Aplicación]]

> [!question] P37 · Programas de gestión del hardware
> ¿Cuál de las siguientes opciones pertenece a la categoría de **programas para la gestión del hardware**?
> - a. Procesador de textos LibreOffice Writer.
> - b. Navegador web Mozilla Firefox.
> - c. Controlador de dispositivo (driver) de una tarjeta de red.
> - d. Reproductor multimedia VLC.

> [!success]- Respuesta
>
> - c. ✅ Controlador de dispositivo (driver) de una tarjeta de red.
>
> *Por qué:* un **driver** (controlador de dispositivo) gestiona directamente el hardware. LibreOffice, Firefox y VLC son aplicaciones de usuario. [[1.1 - Programa vs. Proceso#1.1 Programa|Ver 1.1 · Programa]]

> [!question] P38 · Servicio del SO vs. servicio de aplicación
> ¿Qué distingue a un **servicio del sistema operativo** de un **servicio de aplicación** instalado por el usuario?
> - a. Los servicios del sistema se eliminan del disco tras el primer inicio de sesión.
> - b. Los del sistema gestionan recursos esenciales del SO (red, autenticación, audio), mientras que los de aplicación cubren requerimientos de software instalado (servidor web, base de datos).
> - c. Los servicios de aplicación requieren obligatoriamente una pantalla táctil para funcionar.
> - d. Los servicios del sistema se ejecutan en la CPU, mientras que los de aplicación se ejecutan exclusivamente en la memoria swap.

> [!success]- Respuesta
>
> - b. ✅ Los del sistema gestionan recursos esenciales del SO (red, autenticación, audio), mientras que los de aplicación cubren requerimientos de software instalado (servidor web, base de datos).
>
> *Por qué:* los **del sistema** gestionan recursos esenciales del SO (red, audio, autenticación); los **de aplicación** dan soporte a software instalado (servidor web, base de datos). Ninguno se borra tras el login, ni necesita pantalla táctil, ni corre "en la swap". [[1.1 - Programa vs. Proceso#4. Demonios y servicios|Ver 1.1 · Demonios y servicios]]

> [!question] P39 · Ventaja de las librerías
> ¿Cuál es la ventaja principal de utilizar **librerías o bibliotecas** en el desarrollo de software?
> - a. Convierten automáticamente cualquier ejecutable binario en código interpretado.
> - b. Impiden que los procesos sean interrumpidos por el planificador del sistema operativo.
> - c. Permiten que un programa se ejecute sin necesidad de consumir memoria RAM.
> - d. Promueven la modularidad y reutilización de código de uso común entre múltiples programas.

> [!success]- Respuesta
>
> - d. ✅ Promueven la modularidad y reutilización de código de uso común entre múltiples programas.
>
> *Por qué:* fomentan la **modularidad y la reutilización** del código común entre programas. No convierten binarios en interpretados, no evitan el planificador ni permiten ejecutar sin RAM. [[1.1 - Programa vs. Proceso#2.3 Librerías|Ver 1.1 · Librerías]]

> [!question] P40 · Ejecutable en Linux/macOS
> En sistemas basados en GNU/Linux o macOS, ¿cómo determina principalmente el sistema operativo que un fichero es un ejecutable?
> - a. Por la presencia estricta y obligatoria de la extensión `.exe` o `.com` al final del nombre.
> - b. Mediante la activación de los permisos de ejecución (+x) en los metadatos del fichero, independientemente de su extensión.
> - c. Por su tamaño en bytes, que debe ser múltiplo exacto del tamaño de página de memoria.
> - d. Por estar alojado exclusivamente en el directorio `/boot` del disco raíz.

> [!success]- Respuesta
>
> - b. ✅ Mediante la activación de los permisos de ejecución (+x) en los metadatos del fichero, independientemente de su extensión.
>
> *Por qué:* lo decide el **bit de ejecución** (`+x`) de los metadatos del fichero, sin importar la extensión. La extensión `.exe` es cosa de Windows; el tamaño o estar en `/boot` no influyen. [[1.1 - Programa vs. Proceso#2. Ejecutable|Ver 1.1 · Ejecutable]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 1
> P1 **b** · P2 *ejecución* · P3 *intérprete* · P4 *firmware* · P5 *ejecutable*  
> P6 *proceso* · P7 **c** · P8 **b** · P9 *bytecode* · P10 **d**  
> P11 *dinámica* · P12 *standby* · P13 *binarios* · P14 *aplicación* · P15 **a**  
> P16 *compilador* · P17 *PID* · P18 *software* · P19 **c** · P20 **b**  
> P21 *segundo* · P22 *servicio* · P23 **d** · P24 *arranque* · P25 **a**  
> P26 *impresión* · P27 **a** · P28 *librería* · P29 **b** · P30 **a**  
> P31 *demonio* · P32 **d** · P33 **b** · P34 *programa* · P35 **c**  
> P36 **a** · P37 **c** · P38 **b** · P39 **d** · P40 **b**  

---

### Simulacro 2 · 1.2 · Computación concurrente

> [!abstract] Simulacro 2
> **20 preguntas** · ⏱️ ~10 min · Fuente: [[Cuestionario 1-2]] · [[1.2 - Computacion concurrente|Apuntes del 1.2]] · Tu nota en Moodle: **19/20**

> [!question] P1 · Cambio de contexto
> El conjunto de operaciones necesarias para guardar el estado del proceso actual y restaurar el estado de otro proceso listo para ejecutarse se conoce como cambio de ______.

> [!success]- Respuesta
>
> - **contexto**
>
> *Por qué:* guardar el estado del proceso actual y cargar el del siguiente es el **cambio de contexto**. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]

> [!question] P2 · Multiprogramación en un mononúcleo
> ¿En qué consiste la técnica de **multiprogramación** en un sistema mononúcleo?
> - a. En prescindir de cualquier cambio de contexto para reducir la latencia de memoria.
> - b. En ejecutar instrucciones verdaderamente al mismo instante físico duplicando la ALU.
> - c. En asignar por turnos el procesador durante cortos periodos de tiempo a cada proceso mediante planificación.
> - d. En esperar a que cada proceso finalice por completo antes de admitir uno nuevo en la cola.

> [!success]- Respuesta
>
> - c. ✅ En asignar por turnos el procesador durante cortos periodos de tiempo a cada proceso mediante planificación.
>
> *Por qué:* la multiprogramación **reparte el procesador por turnos** cortos entre procesos gracias al planificador. No ejecuta a la vez de verdad (eso sería paralelismo), no elimina el cambio de contexto (lo necesita) y no espera a que cada proceso acabe (eso es ejecución por lotes secuencial). [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]

> [!question] P3 · Memoria común compartida ⚠️
> La arquitectura de sistemas paralelos donde múltiples núcleos o procesadores comparten una memoria principal común se denomina ______.

> [!success]- Respuesta
>
> - **multiprocesamiento**
>
> *Por qué:* varios núcleos o procesadores **compartiendo memoria principal** = **multiprocesamiento**. Si cada uno tiene su memoria local, es procesamiento distribuido. [[1.2 - Computacion concurrente#4.1 Multiprocesamiento|Ver 1.2 · Multiprocesamiento]]
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P4 · Impacto del cambio de contexto
> ¿Qué impacto tiene el **cambio de contexto** sobre el tiempo global de ejecución en la multiprogramación?
> - a. Reduce a la mitad el tiempo global necesario para completar todos los procesos concurrentes.
> - b. Introduce una sobrecarga que no reduce el tiempo global de ejecución, sino que lo incrementa ligeramente.
> - c. Elimina completamente las latencias provocadas por las operaciones de E/S.
> - d. Garantiza una aceleración lineal de procesamiento idéntica a la del paralelismo puro.

> [!success]- Respuesta
>
> - b. ✅ Introduce una sobrecarga que no reduce el tiempo global de ejecución, sino que lo incrementa ligeramente.
>
> *Por qué:* el cambio de contexto es **sobrecarga**: mientras se guarda y restaura el estado no se ejecuta código útil, así que el tiempo global **aumenta ligeramente**. La multiprogramación no acelera como el paralelismo ni elimina las esperas de E/S. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]

> [!question] P5 · SMP
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

> [!question] P6 · AMP
> En el multiprocesamiento ______ (o AMP), un procesador maestro controla al resto de procesadores subordinados o esclavos.

> [!success]- Respuesta
>
> - **asimétrico** / asimetrico
>
> *Por qué:* en el multiprocesamiento **asimétrico** (AMP, *master-slave*) un procesador maestro controla a los esclavos. [[1.2 - Computacion concurrente#4.1 Multiprocesamiento|Ver 1.2 · Multiprocesamiento]]

> [!question] P7 · Sin reloj global
> ¿Qué consecuencia directa tiene la **inexistencia de un reloj global** en los sistemas distribuidos?
> - a. Que la comunicación debe realizarse obligatoriamente mediante un bus de memoria física común.
> - b. Que la caída de un nodo cualquiera detiene de forma obligatoria todo el entorno distribuido.
> - c. Que todos los procesos deben ejecutarse necesariamente al mismo microsegundo exacto.
> - d. La sincronización entre procesos debe realizarse mediante el paso o intercambio de mensajes.

> [!success]- Respuesta
>
> - d. ✅ La sincronización entre procesos debe realizarse mediante el paso o intercambio de mensajes.
>
> *Por qué:* sin reloj común no se puede coordinar por tiempo, así que la sincronización se hace **intercambiando mensajes**. No hay bus de memoria común (eso es SMP), la caída de un nodo no tumba todo el sistema y nadie puede ejecutar "al mismo microsegundo". [[1.2 - Computacion concurrente#4.2 Procesamiento distribuido|Ver 1.2 · Procesamiento distribuido]]

> [!question] P8 · Computación concurrente
> ¿Qué define a la **computación concurrente** según el material de estudio?
> - a. Múltiples procesos parecen progresar al mismo tiempo compartiendo recursos, aunque no necesariamente se ejecuten simultáneamente en un instante dado.
> - b. La necesidad obligatoria de disponer de procesadores distribuidos geográficamente en red.
> - c. El uso exclusivo de procesamiento en la nube sin intervención del sistema operativo local.
> - d. La ejecución estrictamente secuencial de tareas donde una debe finalizar antes de que empiece la siguiente.

> [!success]- Respuesta
>
> - a. ✅ Múltiples procesos parecen progresar al mismo tiempo compartiendo recursos, aunque no necesariamente se ejecuten simultáneamente en un instante dado.
>
> *Por qué:* concurrencia = varios procesos **parecen** progresar a la vez compartiendo recursos, aunque no se ejecuten necesariamente en el mismo instante. No exige red ni nube, y es justo lo contrario de la ejecución estrictamente secuencial. [[1.2 - Computacion concurrente#1. Computación concurrente y multitarea|Ver 1.2 · Concurrencia y multitarea]]

> [!question] P9 · AMP (master-slave)
> ¿Qué característica define al multiprocesamiento asimétrico (**AMP** o _master-slave_)?
> - a. Requiere necesariamente que los procesadores se encuentren distribuidos en ciudades diferentes.
> - b. Un procesador maestro controla al resto (esclavos), gestionando el sistema operativo y repartiendo las tareas.
> - c. No existe ningún procesador jerarquizado y todos ejecutan las rutinas del SO al mismo nivel.
> - d. Prescinde por completo del uso de planificadores de CPU en todos los niveles.

> [!success]- Respuesta
>
> - b. ✅ Un procesador maestro controla al resto (esclavos), gestionando el sistema operativo y repartiendo las tareas.
>
> *Por qué:* en AMP un **maestro** gestiona el SO y reparte el trabajo a los esclavos. "Todos al mismo nivel" describe SMP; la distancia geográfica describe sistemas distribuidos. [[1.2 - Computacion concurrente#4.1 Multiprocesamiento|Ver 1.2 · Multiprocesamiento]]

> [!question] P10 · Paralelismo
> La ejecución simultánea y real (al mismo tiempo) de diferentes tareas o partes de un programa en múltiples unidades de procesamiento se denomina ______.

> [!success]- Respuesta
>
> - **paralelismo**
>
> *Por qué:* ejecución **simultánea real** en varias unidades de procesamiento = **paralelismo**. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]

> [!question] P11 · SMP: simétrico
> El multiprocesamiento ______ (o SMP) se caracteriza porque todos los procesadores funcionan de igual manera y ninguno está diferenciado del resto.

> [!success]- Respuesta
>
> - **simétrico** / simetrico
>
> *Por qué:* multiprocesamiento **simétrico** (SMP): todos los procesadores son iguales. [[1.2 - Computacion concurrente#4.1 Multiprocesamiento|Ver 1.2 · Multiprocesamiento]]

> [!question] P12 · Cluster
> ¿Cómo se define habitualmente un **cluster** dentro de las arquitecturas de procesamiento distribuido?
> - a. Un circuito de supercomputación diseñado a medida con interconexión tipo hipercubo.
> - b. Múltiples unidades de ejecución dentro de un mismo chip compartiendo registros físicos.
> - c. Ordenadores convencionales interconectados mediante una red de área local (LAN) convencional.
> - d. Dispositivos móviles heterogéneos y aislados sincronizados mediante un reloj global unificado.

> [!success]- Respuesta
>
> - c. ✅ Ordenadores convencionales interconectados mediante una red de área local (LAN) convencional.
>
> *Por qué:* un **cluster** son ordenadores convencionales unidos por una **LAN convencional** (Ethernet, InfiniBand). La interconexión en hipercubo a medida es un MPP; varias unidades en un chip, un multinúcleo. [[1.2 - Computacion concurrente#4.2 Procesamiento distribuido|Ver 1.2 · Procesamiento distribuido]]

> [!question] P13 · Requisito del paralelismo real
> ¿Qué requisito hardware es imprescindible para que exista **paralelismo real**?
> - a. Tener implementado un algoritmo de planificación por turnos sin soporte de hardware adicional.
> - b. Disponer de un único núcleo con una memoria caché L3 de gran tamaño.
> - c. Disponer de al menos dos núcleos de procesamiento (multinúcleo o multiprocesador).
> - d. Contar exclusivamente con una tarjeta gráfica externa comunicada mediante bus PCIe.

> [!success]- Respuesta
>
> - c. ✅ Disponer de al menos dos núcleos de procesamiento (multinúcleo o multiprocesador).
>
> *Por qué:* para que haya paralelismo real hacen falta **al menos dos núcleos**. Con uno solo, por grande que sea su caché o por bueno que sea el planificador, solo hay multiprogramación. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]

> [!question] P14 · SMT / Hyper-Threading
> ¿Cómo funciona la tecnología **SMT (Simultaneous Multithreading)** o _Hyper-Threading_?
> - a. Sustituye la memoria caché interna por memoria no volátil distribuida en la placa base.
> - b. Presenta un núcleo físico como varios núcleos lógicos compartiendo recursos de ejecución pero con distintos registros.
> - c. Duplica físicamente todos los componentes del núcleo (incluyendo todas las unidades de cálculo y cachés L1).
> - d. Transforma una máquina aislada en un cluster conectado mediante protocolos TCP/IP.

> [!success]- Respuesta
>
> - b. ✅ Presenta un núcleo físico como varios núcleos lógicos compartiendo recursos de ejecución pero con distintos registros.
>
> *Por qué:* SMT presenta **un núcleo físico como varios lógicos**, que comparten las unidades de ejecución y tienen registros propios. No duplica el núcleo entero (eso serían dos núcleos físicos). [[1.2 - Computacion concurrente#2.1 Núcleos, hilos lógicos y SMT|Ver 1.2 · Núcleos y SMT]]

> [!question] P15 · SMP vs. distribuido
> ¿Cuál es la diferencia clave fundamental entre el **multiprocesamiento (SMP)** y el **procesamiento distribuido**?
> - a. Que los sistemas SMP no son capaces de ejecutar hilos de forma concurrente.
> - b. La existencia o no de una memoria principal común compartida por todos los procesadores.
> - c. La presencia obligatoria de una red cableada de fibra óptica para que funcione el bus local.
> - d. La utilización exclusiva de sistemas operativos tipo Unix en arquitecturas SMP.

> [!success]- Respuesta
>
> - b. ✅ La existencia o no de una memoria principal común compartida por todos los procesadores.
>
> *Por qué:* la diferencia clave es si hay **memoria principal común** (SMP) o si cada nodo tiene la suya (distribuido). Ambos ejecutan hilos y ninguno exige fibra óptica o Unix. [[1.2 - Computacion concurrente#4.2 Procesamiento distribuido|Ver 1.2 · Procesamiento distribuido]]

> [!question] P16 · Coordinar procesos concurrentes
> Para coordinar la colaboración y competencia por recursos entre procesos concurrentes, se introducen mecanismos de comunicación y ______.

> [!success]- Respuesta
>
> - **sincronización** / sincronizacion
>
> *Por qué:* para colaborar y competir por recursos hacen falta mecanismos de **comunicación y sincronización**. [[1.2 - Computacion concurrente#3. Mecanismos de comunicación y sincronización|Ver 1.2 · Comunicación y sincronización]]

> [!question] P17 · Cluster (definición)
> Un conjunto de ordenadores convencionales interconectados mediante una red de área local (LAN) convencional para trabajar conjuntamente se conoce como ______.

> [!success]- Respuesta
>
> - **cluster** / clúster
>
> *Por qué:* ordenadores convencionales unidos por una LAN = **cluster**. [[1.2 - Computacion concurrente#4.2 Procesamiento distribuido|Ver 1.2 · Procesamiento distribuido]]

> [!question] P18 · Procesamiento distribuido
> El procesamiento ______ es aquel en el que los procesadores no comparten memoria principal, teniendo cada uno su propia memoria local y comunicándose mediante una red.

> [!success]- Respuesta
>
> - **distribuido** / distribuído
>
> *Por qué:* sin memoria común, con memoria local en cada nodo y comunicación por red = **distribuido**. [[1.2 - Computacion concurrente#4.2 Procesamiento distribuido|Ver 1.2 · Procesamiento distribuido]]

> [!question] P19 · Multitarea
> Desde el punto de vista del usuario, la percepción de la computación concurrente que le permite realizar múltiples tareas de forma aparentemente simultánea se denomina ______.

> [!success]- Respuesta
>
> - **multitarea**
>
> *Por qué:* la percepción del usuario de que puede hacer varias cosas a la vez se llama **multitarea**. [[1.2 - Computacion concurrente#1. Computación concurrente y multitarea|Ver 1.2 · Concurrencia y multitarea]]

> [!question] P20 · Multiprogramación
> La técnica que simula la ejecución concurrente alternando por turnos el uso del procesador entre varios procesos se denomina ______.

> [!success]- Respuesta
>
> - **multiprogramación** / multiprogramacion
>
> *Por qué:* alternar el procesador por turnos entre procesos para simular concurrencia = **multiprogramación**. [[1.2 - Computacion concurrente#2. Paralelismo y multiprogramación|Ver 1.2 · Paralelismo y multiprogramación]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 2
> P1 *contexto* · P2 **c** · P3 *multiprocesamiento* · P4 **b** · P5 **b**  
> P6 *asimétrico* · P7 **d** · P8 **a** · P9 **b** · P10 *paralelismo*  
> P11 *simétrico* · P12 **c** · P13 **c** · P14 **b** · P15 **b**  
> P16 *sincronización* · P17 *cluster* · P18 *distribuido* · P19 *multitarea* · P20 *multiprogramación*  

---

### Simulacro 3 · 1.3 · Procesos en el sistema operativo

> [!abstract] Simulacro 3
> **16 preguntas** · ⏱️ ~8 min · Fuente: [[Cuestionario 1-3]] · [[1.3 - Procesos en el sistema operativo|Apuntes del 1.3]] · Tu nota en Moodle: **16/16**

> [!question] P1 · Transición por apropiación
> ¿Qué suceso provoca la transición por "Apropiación" o interrupción (preemption) de "En ejecución" a "Listo"?
> - a. La petición explícita de lectura o escritura en un disco.
> - b. La terminación controlada del programa mediante una llamada al sistema exit.
> - c. La falta de espacio físico en la memoria RAM del equipo.
> - d. La expiración del quantum de tiempo asignado o la llegada de un proceso de mayor prioridad.

> [!success]- Respuesta
>
> - d. ✅ La expiración del quantum de tiempo asignado o la llegada de un proceso de mayor prioridad.
>
> *Por qué:* pasa de *En ejecución* a *Listo* cuando **expira el quantum** o llega un proceso de **más prioridad**. Pedir E/S lleva a *Bloqueado*, `exit` lleva a *Terminado* y la falta de RAM provoca suspensión. [[1.3 - Procesos en el sistema operativo#2.2 Las transiciones|Ver 1.3 · Las transiciones]]

> [!question] P2 · Planificador a largo plazo
> ¿Cuál es la función principal del planificador a largo plazo en un sistema operativo?
> - a. Alternar procesos en la CPU en intervalos de milisegundos mediante quantum.
> - b. Seleccionar qué nuevos procesos pasan a la cola de preparados, controlando el grado de multiprogramación.
> - c. Gestionar el envío de señales interproceso como SIGKILL.
> - d. Restaurar los registros del procesador y cambiar el contador de programa.

> [!success]- Respuesta
>
> - b. ✅ Seleccionar qué nuevos procesos pasan a la cola de preparados, controlando el grado de multiprogramación.
>
> *Por qué:* decide **qué procesos nuevos entran** en la cola de listos y controla el **grado de multiprogramación**. Alternar procesos cada pocos milisegundos lo hace el planificador a corto plazo; restaurar registros, el dispatcher. [[1.3 - Procesos en el sistema operativo#3. Planificación de procesos|Ver 1.3 · Planificación]]

> [!question] P3 · Segmento de memoria dinámica
> ¿Qué segmento de la memoria de un proceso se utiliza para almacenar la memoria dinámica asignada durante el tiempo de ejecución?
> - a. Heap (Montón).
> - b. Código (Texto).
> - c. Datos (Data).
> - d. Pila (Stack).

> [!success]- Respuesta
>
> - a. ✅ Heap (Montón).
>
> *Por qué:* el **heap** guarda la memoria dinámica pedida en ejecución (`new`, `malloc`). El código guarda instrucciones; los datos, variables globales y estáticas; la pila, llamadas y variables locales. [[1.3 - Procesos en el sistema operativo#1.1 El cargador de procesos|Ver 1.3 · El cargador]]

> [!question] P4 · Planificación de Windows y macOS
> ¿Qué esquema de planificación utilizan sistemas operativos como Windows y macOS donde los procesos entran con máxima prioridad y se degradan conforme consumen CPU?
> - a. First-In First-Out estricto (FIFO).
> - b. Shortest Job First no apropiativo.
> - c. Planificación por colas multinivel con retroalimentación.
> - d. Planificación por cuotas estáticas sin desalojo.

> [!success]- Respuesta
>
> - c. ✅ Planificación por colas multinivel con retroalimentación.
>
> *Por qué:* usan **colas multinivel con retroalimentación**: los procesos entran con máxima prioridad y bajan de cola según consumen CPU. FIFO y SJF no degradan prioridades y las cuotas estáticas no expulsan. [[1.3 - Procesos en el sistema operativo#3.1 Algoritmos de planificación|Ver 1.3 · Algoritmos de planificación]]

> [!question] P5 · Proceso zombi
> En sistemas Unix/Linux, ¿qué es un proceso en estado "zombi" (zombie)?
> - a. Un proceso que ha finalizado su ejecución pero aún mantiene una entrada en la tabla de procesos hasta que el padre recoja su código de retorno.
> - b. Un proceso que se ha bloqueado de forma irrecuperable por un fallo de hardware.
> - c. Un proceso en bucle infinito que consume el 100% de la CPU.
> - d. Un proceso trasladado a disco durante una sobrecarga de memoria RAM.

> [!success]- Respuesta
>
> - a. ✅ Un proceso que ha finalizado su ejecución pero aún mantiene una entrada en la tabla de procesos hasta que el padre recoja su código de retorno.
>
> *Por qué:* un **zombi** ha terminado pero conserva su entrada en la tabla de procesos hasta que el padre recoge el código de retorno. No está colgado, ni en bucle, ni en disco (eso sería suspendido). [[1.3 - Procesos en el sistema operativo#2.1 Los estados|Ver 1.3 · Los estados]]

> [!question] P6 · Espacio de direcciones virtual
> Respecto al espacio de direcciones de memoria virtual de un proceso, ¿cuál de las siguientes afirmaciones es correcta?
> - a. El proceso percibe un espacio contiguo y exclusivo, aunque físicamente la RAM pueda estar fragmentada.
> - b. Permite que dos procesos compartan libremente variables locales sin intervención del kernel.
> - c. Es creado directamente por el planificador de la CPU en lugar del cargador del SO.
> - d. El proceso accede directamente y sin traducción a los bancos físicos contiguos de la memoria RAM.

> [!success]- Respuesta
>
> - a. ✅ El proceso percibe un espacio contiguo y exclusivo, aunque físicamente la RAM pueda estar fragmentada.
>
> *Por qué:* cada proceso ve un **espacio contiguo y exclusivo**, aunque en la RAM física esté fragmentado. El acceso pasa por traducción, no permite compartir variables locales con otros procesos y lo crea el cargador, no el planificador. [[1.3 - Procesos en el sistema operativo#1.1 El cargador de procesos|Ver 1.3 · El cargador]]

> [!question] P7 · Latencia del cambio de contexto
> Se define como 'latencia del cambio de contexto' o dispatch latency al tiempo en el que:
> - a. El disco tarda en transferir un bloque de memoria a la memoria principal RAM.
> - b. La CPU no ejecuta instrucciones útiles de procesos de usuario, sino labores de gestión del sistema operativo.
> - c. Tarda un periférico de entrada/salida en responder a una interrupción de hardware.
> - d. Un proceso pasa esperando en cola de listos antes de recibir su primer quantum.

> [!success]- Respuesta
>
> - b. ✅ La CPU no ejecuta instrucciones útiles de procesos de usuario, sino labores de gestión del sistema operativo.
>
> *Por qué:* es el tiempo en que la CPU **no ejecuta instrucciones útiles** de usuario porque está gestionando el cambio. No es el tiempo de disco, de un periférico ni de espera en la cola de listos. [[1.3 - Procesos en el sistema operativo#3.2 El dispatcher|Ver 1.3 · El dispatcher]]

> [!question] P8 · Acceso fuera del espacio de direcciones
> Si un proceso intenta acceder a una dirección fuera de su espacio de direcciones de memoria virtual asignado, ¿qué ocurre en un sistema Unix/Linux?
> - a. El proceso entra inmediatamente en estado zombie.
> - b. El sistema operativo expande automáticamente el segmento Heap sin avisar.
> - c. Se le asigna automáticamente un nuevo quantum de tiempo en la CPU.
> - d. Se genera un fallo de segmentación (segmentation fault) o excepción de protección.

> [!success]- Respuesta
>
> - d. ✅ Se genera un fallo de segmentación (segmentation fault) o excepción de protección.
>
> *Por qué:* el SO detecta la violación y lanza un **segmentation fault** (excepción de protección). No lo convierte en zombi, no le amplía el heap ni le da otro quantum. [[1.3 - Procesos en el sistema operativo#1.2 El PCB (Process Control Block)|Ver 1.3 · El PCB]]

> [!question] P9 · Dispatcher
> ¿Cuál es el cometido del módulo despachador (dispatcher)?
> - a. Elegir el algoritmo teórico de ordenación de colas (FIFO, RR, SJF).
> - b. Materializar la decisión del scheduler ejecutando físicamente el cambio de contexto entre procesos.
> - c. Crear la memoria virtual en el disco de intercambio (swap).
> - d. Asignar los identificadores PID a los programas que inician.

> [!success]- Respuesta
>
> - b. ✅ Materializar la decisión del scheduler ejecutando físicamente el cambio de contexto entre procesos.
>
> *Por qué:* el **dispatcher** ejecuta la decisión del scheduler: hace físicamente el **cambio de contexto**. Elegir el algoritmo es cosa del scheduler; crear la swap o asignar PID son tareas de otros componentes. [[1.3 - Procesos en el sistema operativo#3.2 El dispatcher|Ver 1.3 · El dispatcher]]

> [!question] P10 · Hilo
> ¿Cómo se define un hilo (thread) dentro del contexto de los sistemas operativos?
> - a. Es el identificador numérico único asignado a un ejecutable en disco.
> - b. Es un programa completo cargado en su propio espacio virtual independiente.
> - c. Es una estructura del núcleo encargada exclusivamente del swapping a disco.
> - d. Es la unidad mínima de ejecución dentro de un proceso.

> [!success]- Respuesta
>
> - d. ✅ Es la unidad mínima de ejecución dentro de un proceso.
>
> *Por qué:* un **hilo** es la **unidad mínima de ejecución dentro de un proceso**. El identificador es el PID; un programa con su propio espacio virtual es un proceso. [[1.3 - Procesos en el sistema operativo#1. Gestión de procesos en multiprogramación|Ver 1.3 · Gestión de procesos]]

> [!question] P11 · De Listo a En ejecución
> La transición de un proceso desde el estado "Listo" al estado "En ejecución" recibe el nombre de:
> - a. Espera completada (event completion).
> - b. Apropiación (preemption).
> - c. Reactivación (resume).
> - d. Asignación (dispatching).

> [!success]- Respuesta
>
> - d. ✅ Asignación (dispatching).
>
> *Por qué:* pasar de *Listo* a *En ejecución* es la **asignación** (*dispatching*). La apropiación es la transición inversa; la reactivación viene de suspendido; la espera completada saca de *Bloqueado*. [[1.3 - Procesos en el sistema operativo#2.2 Las transiciones|Ver 1.3 · Las transiciones]]

> [!question] P12 · PCB: siguiente instrucción
> ¿Qué elemento del Bloque de Control de Proceso (PCB) contiene la dirección de memoria de la siguiente instrucción a ejecutar?
> - a. Contador del programa (Program Counter - PC).
> - b. Identificador del proceso (PID).
> - c. Puntero de pila (Stack Pointer).
> - d. Registro de estado o flags.

> [!success]- Respuesta
>
> - a. ✅ Contador del programa (Program Counter - PC).
>
> *Por qué:* el **contador de programa** (PC) guarda la dirección de la siguiente instrucción. El PID identifica, el puntero de pila apunta a la pila y los flags guardan el estado de la última operación. [[1.3 - Procesos en el sistema operativo#1.2 El PCB (Process Control Block)|Ver 1.3 · El PCB]]

> [!question] P13 · Round Robin: expira el quantum
> En el algoritmo de planificación Round Robin (RR), ¿qué sucede si un proceso no ha terminado su tarea cuando expira su quantum asignado?
> - a. Pasa directamente al estado bloqueado hasta que vuelva a haber tiempo libre.
> - b. Se le degrada su prioridad al nivel más bajo y se suspende en disco.
> - c. Es expulsado de la CPU y se coloca al final de la cola de listos de forma cíclica.
> - d. Continúa ejecutándose indefinidamente hasta que haga una llamada a E/S.

> [!success]- Respuesta
>
> - c. ✅ Es expulsado de la CPU y se coloca al final de la cola de listos de forma cíclica.
>
> *Por qué:* en RR, si el quantum se acaba el proceso es **expulsado y va al final de la cola de listos** (cíclico). No se bloquea (no espera ningún evento), no baja de prioridad (eso es multinivel) y no sigue indefinidamente. [[1.3 - Procesos en el sistema operativo#3.1 Algoritmos de planificación|Ver 1.3 · Algoritmos de planificación]]

> [!question] P14 · Estado Listo
> ¿Qué caracteriza a un proceso que se encuentra en el estado "Listo" (ready)?
> - a. Está esperando a que concluya una operación de entrada/salida (E/S).
> - b. Tiene todos los recursos necesarios asignados excepto la CPU y espera su turno en cola.
> - c. Se encuentra ejecutando instrucciones activamente en un núcleo del procesador.
> - d. Ha sido expulsado completamente a memoria secundaria (disco).

> [!success]- Respuesta
>
> - b. ✅ Tiene todos los recursos necesarios asignados excepto la CPU y espera su turno en cola.
>
> *Por qué:* en **Listo** el proceso tiene todo lo que necesita **menos la CPU** y espera su turno. Esperar E/S es *Bloqueado*; ejecutar es *En ejecución*; estar en disco es *Suspendido*. [[1.3 - Procesos en el sistema operativo#2.1 Los estados|Ver 1.3 · Los estados]]

> [!question] P15 · Suspender bloqueados antes que listos
> ¿Por qué el sistema operativo suele preferir suspender procesos bloqueados antes que procesos listos?
> - a. Porque los procesos bloqueados no tienen PCB asignado en la tabla de procesos.
> - b. Porque al estar esperando un evento no compiten por la CPU, liberando memoria sin mermar el rendimiento inmediato.
> - c. Porque los procesos suspendidos listos causan bloqueos mutuos irreversibles.
> - d. Porque los procesos listos ocupan un tamaño fijo que el disco no puede albergar.

> [!success]- Respuesta
>
> - b. ✅ Porque al estar esperando un evento no compiten por la CPU, liberando memoria sin mermar el rendimiento inmediato.
>
> *Por qué:* un proceso bloqueado **no compite por la CPU** mientras espera, así que mandarlo a disco libera RAM sin afectar al rendimiento inmediato. Los bloqueados sí tienen PCB, y las otras razones son inventadas. [[1.3 - Procesos en el sistema operativo#2.2 Las transiciones|Ver 1.3 · Las transiciones]]

> [!question] P16 · Contenido de la pila
> En la estructura de memoria de un proceso, la pila (Stack) contiene principalmente:
> - a. Llamadas a funciones y variables locales.
> - b. Variables globales y datos estáticos.
> - c. Instrucciones binarias del programa.
> - d. Memoria solicitada dinámicamente con malloc o new.

> [!success]- Respuesta
>
> - a. ✅ Llamadas a funciones y variables locales.
>
> *Por qué:* la **pila** guarda **llamadas a funciones y variables locales**. Las globales van en *datos*; las instrucciones, en *código*; la memoria de `new`/`malloc`, en el *heap*. [[1.3 - Procesos en el sistema operativo#1.1 El cargador de procesos|Ver 1.3 · El cargador]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 3
> P1 **d** · P2 **b** · P3 **a** · P4 **c** · P5 **a**  
> P6 **a** · P7 **b** · P8 **d** · P9 **b** · P10 **d**  
> P11 **d** · P12 **a** · P13 **c** · P14 **b** · P15 **b**  
> P16 **a**  

---

### Simulacro 4 · 1.4 · Técnicas de programación concurrente

> [!abstract] Simulacro 4
> **20 preguntas** · ⏱️ ~10 min · Fuente: [[Cuestionario 1-4]] · [[1.4 - Tecnicas de programacion concurrente|Apuntes del 1.4]] · Tu nota en Moodle: **20/20**

> [!question] P1 · Solo uno en la sección crítica
> ¿Qué concepto define la propiedad de que solo un proceso pueda entrar a su sección crítica a la vez?
> - a. Exclusión mutua.
> - b. Inanición involuntaria.
> - c. Prioridad dinámica estricta.
> - d. Paralelismo temporal asíncrono.

> [!success]- Respuesta
>
> - a. ✅ Exclusión mutua.
>
> *Por qué:* la **exclusión mutua** garantiza que solo un proceso esté en la sección crítica a la vez. La inanición es un problema, no una propiedad buscada, y las otras dos opciones no son conceptos del temario. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P2 · Hardware de la programación paralela
> ¿Qué arquitectura de hardware caracteriza principalmente a la programación paralela en entornos SMP?
> - a. Nodos heterogéneos sin posibilidad de compartir bus de datos ni reloj.
> - b. Un único procesador mononúcleo con memoria virtual segmentada.
> - c. Múltiples núcleos de procesamiento que comparten la memoria principal.
> - d. Múltiples servidores independientes interconectados exclusivamente mediante switches de red.

> [!success]- Respuesta
>
> - c. ✅ Múltiples núcleos de procesamiento que comparten la memoria principal.
>
> *Por qué:* SMP = **varios núcleos que comparten la memoria principal**. Los nodos que se comunican por red son sistemas distribuidos; un mononúcleo no permite paralelismo. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P3 · Competencia por la CPU
> ¿Qué componente del sistema operativo gestiona la competencia por la CPU entre procesos independientes?
> - a. El compilador JIT (Just-In-Time).
> - b. El gestor de sockets de red.
> - c. El planificador de procesos (scheduler).
> - d. El recolector de basura (Garbage Collector).

> [!success]- Respuesta
>
> - c. ✅ El planificador de procesos (scheduler).
>
> *Por qué:* el **planificador** (*scheduler*) reparte la CPU entre procesos independientes. El JIT compila, el gestor de sockets comunica y el GC libera memoria. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P4 · Por qué sincronizar procesos competidores
> ¿Por qué la sincronización de procesos es indispensable cuando se tienen procesos competidores?
> - a. Para apagar los núcleos sobrantes del procesador durante la ejecución de las tareas.
> - b. Para reducir automáticamente el uso total de memoria física del sistema operativo a cero.
> - c. Para permitir que todos los procesos escriban a la vez en la misma dirección de memoria.
> - d. Para garantizar el acceso mutuamente excluyente al recurso crítico.

> [!success]- Respuesta
>
> - d. ✅ Para garantizar el acceso mutuamente excluyente al recurso crítico.
>
> *Por qué:* compiten por un **recurso no compartible**, así que hay que garantizar acceso **mutuamente excluyente**. Que todos escriban a la vez en la misma dirección es justo lo que se quiere evitar. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P5 · Desacoplar productor y consumidor
> ¿Qué estructura de datos intermedia se utiliza comúnmente para desacoplar el ritmo de ejecución entre un proceso productor y uno consumidor?
> - a. Un buffer compartido.
> - b. Un registro de instrucciones de la ALU.
> - c. Un archivo de swap de paginación obligatorio.
> - d. Una partición física MBR del disco duro.

> [!success]- Respuesta
>
> - a. ✅ Un buffer compartido.
>
> *Por qué:* un **buffer compartido** absorbe las diferencias de velocidad entre productor y consumidor. Registros de la ALU, swap o MBR no tienen nada que ver. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P6 · Servidor web con un hilo por petición
> ¿Cómo se clasifica un servidor web que recibe peticiones HTTP y asigna cada una a un hilo de procesamiento para mantener la interfaz o escucha atenta?
> - a. Aplicación con programación concurrente.
> - b. Simulación científica masivamente paralela.
> - c. Aplicación puramente secuencial y monolítica.
> - d. Sistema embebido en tiempo real estricto (hard real-time).

> [!success]- Respuesta
>
> - a. ✅ Aplicación con programación concurrente.
>
> *Por qué:* es el ejemplo clásico de **programación concurrente** general: atender muchas peticiones y E/S manteniendo la respuesta. No busca acelerar un cálculo (paralela), no es secuencial y no es tiempo real estricto. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P7 · Complejidad de los sistemas distribuidos
> ¿Qué factor incrementa significativamente la complejidad de los sistemas distribuidos respecto a los de memoria compartida?
> - a. La necesidad de sincronizar el acceso al bus PCI de una placa base local.
> - b. La imposibilidad de ejecutar procesos concurrentes en un mismo nodo.
> - c. Que los programas deben compilarse forzosamente en código ensamblador.
> - d. La gestión de latencias de red, heterogeneidad y fallos parciales.

> [!success]- Respuesta
>
> - d. ✅ La gestión de latencias de red, heterogeneidad y fallos parciales.
>
> *Por qué:* la red añade **latencias, heterogeneidad y fallos parciales**. El bus PCI es local, sí se puede ejecutar concurrencia en un nodo y no hace falta compilar en ensamblador. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P8 · Simulación de fluidos en SMP
> En la simulación científica de dinámica de fluidos dividida en cuadrículas ejecutadas en un supercomputador SMP, ¿qué paradigma se aplica principalmente?
> - a. Procesamiento por lotes (batch) monofásico mononúcleo.
> - b. Programación basada exclusivamente en eventos de usuario GUI.
> - c. Programación paralela.
> - d. Programación secuencial síncrona en un hilo.

> [!success]- Respuesta
>
> - c. ✅ Programación paralela.
>
> *Por qué:* dividir un cálculo intensivo en partes que corren a la vez en varios núcleos con memoria compartida = **programación paralela**. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P9 · Memoria compartida vs. distribuida
> ¿Qué diferencia fundamental existe entre un sistema con memoria compartida y uno con memoria distribuida?
> - a. Que la memoria distribuida no permite la ejecución concurrente de código.
> - b. La velocidad del reloj de los procesadores, que debe ser siempre idéntica en memoria distribuida.
> - c. Que en memoria compartida no se pueden usar variables booleanas ni enteros.
> - d. El acceso directo a una misma RAM física frente a memorias locales por nodo.

> [!success]- Respuesta
>
> - d. ✅ El acceso directo a una misma RAM física frente a memorias locales por nodo.
>
> *Por qué:* compartida: **todos acceden a la misma RAM**; distribuida: **cada nodo tiene su memoria local** y se comunica por red. Ambas permiten concurrencia, usan cualquier tipo de dato y no exigen relojes iguales. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P10 · Comunicación en programación distribuida
> ¿Cuál es el mecanismo primordial de comunicación en la programación distribuida?
> - a. Llamadas atómicas a registros de CPU compartidos.
> - b. Intercambio de mensajes a través de una red de comunicaciones.
> - c. Señales hardware directas en la placa base.
> - d. Variables globales ubicadas en la memoria RAM compartida.

> [!success]- Respuesta
>
> - b. ✅ Intercambio de mensajes a través de una red de comunicaciones.
>
> *Por qué:* sin memoria común, el mecanismo es el **paso de mensajes por red**. Registros o variables globales compartidas exigen memoria común. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P11 · Interacción de competencia
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

> [!question] P12 · Patrón de procesos cooperantes
> ¿Qué patrón clásico de concurrencia ejemplifica la interacción de procesos cooperantes?
> - a. Patrón Singleton mono-hilo.
> - b. Particionamiento estático sin comunicación.
> - c. Patrón Productor-Consumidor.
> - d. Inversión de dependencias desacoplada.

> [!success]- Respuesta
>
> - c. ✅ Patrón Productor-Consumidor.
>
> *Por qué:* el **productor-consumidor** es el ejemplo típico de cooperación a través de un buffer. Los demás son patrones de diseño ajenos a la concurrencia. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P13 · Concurrente vs. paralela
> ¿Cuál es la característica principal que distingue a la programación concurrente en general de la programación paralela?
> - a. Únicamente se puede aplicar en sistemas monoprocesador sin memoria compartida.
> - b. Requiere obligatoriamente una red de ordenadores conectados para intercambiar mensajes.
> - c. Garantiza que todas las tareas se ejecuten exactamente al mismo instante de tiempo físico.
> - d. Gestiona la ejecución entrelazada o simultánea de múltiples tareas para optimizar recursos o reparto de tiempo, sin requerir obligatoriamente múltiples núcleos.

> [!success]- Respuesta
>
> - d. ✅ Gestiona la ejecución entrelazada o simultánea de múltiples tareas para optimizar recursos o reparto de tiempo, sin requerir obligatoriamente múltiples núcleos.
>
> *Por qué:* la concurrente gestiona tareas **entrelazadas o simultáneas** para repartir recursos o tiempo, **sin exigir varios núcleos**. No se limita a monoprocesador, no exige red y no garantiza simultaneidad física. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!question] P14 · Procesos independientes
> ¿Cómo se caracterizan los procesos independientes en un sistema multitarea?
> - a. Requieren tuberías (pipes) para sincronizar su inicio y fin.
> - b. Modifican de forma coordinada las mismas variables globales en memoria.
> - c. No comparten recursos directamente ni se comunican entre sí.
> - d. Comparten obligatoriamente el mismo espacio de direccionamiento virtual.

> [!success]- Respuesta
>
> - c. ✅ No comparten recursos directamente ni se comunican entre sí.
>
> *Por qué:* los independientes **no comparten recursos ni se comunican**; solo compiten indirectamente por CPU y memoria. Pipes, variables globales o espacio de direcciones compartido serían cooperación. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P15 · Finalidad de los procesos cooperantes
> ¿Cuál es la finalidad esencial de la relación entre procesos cooperantes?
> - a. Evitar cualquier tipo de comunicación para reducir la sobrecarga del sistema.
> - b. Impedir que el sistema operativo suspenda la ejecución de sus hilos.
> - c. Trabajar conjuntamente intercambiando datos para una tarea común.
> - d. Bloquear la ejecución de otros procesos para ganar tiempo de procesador.

> [!success]- Respuesta
>
> - c. ✅ Trabajar conjuntamente intercambiando datos para una tarea común.
>
> *Por qué:* cooperan para **trabajar juntos en una tarea común intercambiando datos**. Evitar la comunicación es lo contrario; bloquear a otros, competencia. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P16 · Bloqueo mutuo indefinido
> ¿Qué problema grave ocurre cuando dos procesos quedan bloqueados indefinidamente esperando cada uno un recurso que posee el otro?
> - a. Fallo de página de disco (Page Fault).
> - b. Fragmentación externa de memoria.
> - c. Interbloqueo (Deadlock).
> - d. Desbordamiento de pila (Stack Overflow).

> [!success]- Respuesta
>
> - c. ✅ Interbloqueo (Deadlock).
>
> *Por qué:* cada uno espera un recurso que tiene el otro = **interbloqueo** (*deadlock*). Page fault, fragmentación y stack overflow son problemas de memoria. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P17 · Procesos independientes sin sincronización
> En el contexto de interacciones entre procesos, ¿por qué los procesos independientes no requieren mecanismos explícitos de sincronización de usuario?
> - a. Porque los procesos independientes solo funcionan en ordenadores apagados.
> - b. Porque el SO aísla sus espacios de memoria y recursos.
> - c. Porque se ejecutan siempre a través del mismo hilo principal.
> - d. Porque la JVM prohíbe la multiprogramación en sistemas operativos modernos.

> [!success]- Respuesta
>
> - b. ✅ Porque el SO aísla sus espacios de memoria y recursos.
>
> *Por qué:* el **SO aísla su memoria y sus recursos**, así que no pueden corromperse los datos entre ellos. No usan el mismo hilo y la JVM no prohíbe la multiprogramación. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P18 · Variable compartida sin sincronizar
> ¿Qué riesgo directo surge si varios procesos competidores modifican una variable compartida sin sincronización?
> - a. Condición de carrera e inconsistencia de datos.
> - b. Reinicio instantáneo del hardware de la placa base.
> - c. Aceleración espontánea del tiempo de cálculo en la CPU.
> - d. Duplicación física de la memoria RAM del equipo.

> [!success]- Respuesta
>
> - a. ✅ Condición de carrera e inconsistencia de datos.
>
> *Por qué:* el entrelazado sin control provoca **condición de carrera e inconsistencia de datos**. No acelera nada, no reinicia el hardware ni duplica la RAM. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P19 · Tubería Unix
> Una tubería (pipeline) en un sistema operativo Unix/Linux, donde la salida de un proceso se conecta a la entrada de otro, es un ejemplo de:
> - a. Sistemas distribuidos en malla sin conexión física.
> - b. Procesos cooperantes.
> - c. Procesos en competencia destructiva por el bus de direcciones.
> - d. Procesos independientes sin interacción.

> [!success]- Respuesta
>
> - b. ✅ Procesos cooperantes.
>
> *Por qué:* en `ls | grep` la salida de uno es la entrada del otro: **procesos cooperantes**. No son independientes (se pasan datos) ni compiten. [[1.4 - Tecnicas de programacion concurrente#2. Interacción entre procesos concurrentes|Ver 1.4 · Interacción entre procesos]]

> [!question] P20 · Objetivo de la programación paralela
> ¿Cuál es el objetivo primario de la programación paralela?
> - a. Acelerar la ejecución dividiendo tareas en subtareas simultáneas.
> - b. Permitir que un solo núcleo atienda múltiples hilos por turno de tiempo.
> - c. Gestionar la interfaz de usuario para que no se congele durante operaciones de E/S.
> - d. Tolerar caídas de servidores en centros de datos remotos.

> [!success]- Respuesta
>
> - a. ✅ Acelerar la ejecución dividiendo tareas en subtareas simultáneas.
>
> *Por qué:* su meta es el **rendimiento**: acelerar dividiendo el trabajo en subtareas simultáneas. Repartir un núcleo por turnos o mantener la GUI fluida es concurrencia general; tolerar caídas remotas es cosa de sistemas distribuidos. [[1.4 - Tecnicas de programacion concurrente#1. Técnicas de programación relacionadas con la computación concurrente|Ver 1.4 · Técnicas de programación]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 4
> P1 **a** · P2 **c** · P3 **c** · P4 **d** · P5 **a**  
> P6 **a** · P7 **d** · P8 **c** · P9 **d** · P10 **b**  
> P11 **c** · P12 **c** · P13 **d** · P14 **c** · P15 **c**  
> P16 **c** · P17 **b** · P18 **a** · P19 **b** · P20 **a**  

---

### Simulacro 5 · 1.5 · Orden de ejecución

> [!abstract] Simulacro 5
> **19 preguntas** · ⏱️ ~10 min · Fuente: [[Cuestionario 1-5]] · [[1.5 - Orden de ejecucion|Apuntes del 1.5]] · Tu nota en Moodle: **19/19**

> [!question] P1 · Metáfora secuencial vs. concurrente
> ¿Qué metáfora geométrica describe mejor la diferencia entre la ejecución secuencial y la concurrente según los fundamentos teóricos?
> - a. La ejecución secuencial es un árbol ramificado; la concurrente un bucle circular cerrado.
> - b. La ejecución secuencial carece de dirección; la concurrente sigue una trayectoria elíptica estricta.
> - c. Ambas se representan siempre mediante una única recta continua sin ninguna bifurcación.
> - d. La ejecución secuencial es una línea recta única; la concurrente son múltiples caminos que se entrelazan de forma impredecible.

> [!success]- Respuesta
>
> - d. ✅ La ejecución secuencial es una línea recta única; la concurrente son múltiples caminos que se entrelazan de forma impredecible.
>
> *Por qué:* secuencial = **una línea recta**; concurrente = **varios caminos que se entrelazan** de forma impredecible. Las otras metáforas no recogen el entrelazado. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P2 · Solo lecturas concurrentes
> Si múltiples hilos acceden a una misma variable compartida de forma simultánea y sin ningún mecanismo de sincronización, pero **todos ellos realizan exclusivamente operaciones de lectura**, ¿se produce una carrera de datos?
> - a. Sí, la falta de sincronización siempre desencadena una carrera de datos sin importar la operación.
> - b. Solo si hay más de 4 hilos concurrentes involucrados.
> - c. No, porque es requisito indispensable que al menos uno de los accesos sea de modificación/escritura.
> - d. Sí, porque los registros de la CPU pueden desbordarse al leer a la vez.

> [!success]- Respuesta
>
> - c. ✅ No, porque es requisito indispensable que al menos uno de los accesos sea de modificación/escritura.
>
> *Por qué:* para que haya *data race* hace falta que **al menos un acceso sea de escritura**. Si todos leen, no hay carrera, aunque no haya sincronización ni importe el número de hilos. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]

> [!question] P3 · Analogía del gestor
> En la analogía del "gestor y los trabajadores", ¿qué elemento del sistema representa al gestor que decide en cada momento a quién le toca trabajar?
> - a. El planificador del sistema operativo (_scheduler_).
> - b. El compilador de C o Java durante la fase de optimización.
> - c. El recolector de basura (_garbage collector_).
> - d. El bus de control de la placa base.

> [!success]- Respuesta
>
> - a. ✅ El planificador del sistema operativo (_scheduler_).
>
> *Por qué:* el "gestor" que decide a quién le toca es el **planificador del SO**. El compilador, el GC y el bus no reparten turnos de CPU. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P4 · Comportamiento errático
> Se dice que un programa concurrente presenta **comportamiento errático** cuando:
> - a. Termina inmediatamente la ejecución al intentar abrir un fichero inexistente.
> - b. Ante las mismas entradas, arroja resultados correctos en unas ejecuciones y resultados erróneos o fallos en otras.
> - c. Produce siempre exactamente la misma salida incorrecta en todas las ejecuciones sin variación.
> - d. Genera errores de sintaxis en tiempo de compilación cada vez que se modifica el código fuente.

> [!success]- Respuesta
>
> - b. ✅ Ante las mismas entradas, arroja resultados correctos en unas ejecuciones y resultados erróneos o fallos en otras.
>
> *Por qué:* errático = **con las mismas entradas, unas veces acierta y otras falla**. Si falla siempre igual es un error determinista; los errores de sintaxis o de fichero inexistente no tienen que ver con la concurrencia. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!question] P5 · Qué garantiza un mutex
> ¿Qué propiedad garantiza el uso de un mecanismo de **exclusión mutua** (_mutex_) sobre una región crítica que accede a una variable compartida?
> - a. Que ningún hilo pueda volver a leer la variable una vez que haya sido modificada.
> - b. Que el programa se ejecute el doble de rápido al repartir las escrituras en varios hilos a la vez.
> - c. Que todas las variables del programa pasen a ubicarse en el almacenamiento secundario.
> - d. Que únicamente un hilo a la vez pueda acceder a la sección crítica y manipular el dato compartido.

> [!success]- Respuesta
>
> - d. ✅ Que únicamente un hilo a la vez pueda acceder a la sección crítica y manipular el dato compartido.
>
> *Por qué:* el mutex asegura que **solo un hilo a la vez** ejecute la región crítica. No impide leer después, no acelera (serializa) ni mueve variables a disco. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]

> [!question] P6 · Orden total
> ¿Qué característica define al concepto de **orden total** en la ejecución de un programa?
> - a. Es un orden en el que intervienen mecanismos de exclusión mutua para forzar la sincronización.
> - b. Las instrucciones se ejecutan siguiendo una secuencia única, predecible y completamente determinada por el código y sus entradas.
> - c. El orden dentro de cada hilo es conocido, pero no la intercalación entre diferentes hilos concurrentes.
> - d. El planificador del sistema operativo asigna dinámicamente el orden exacto según la carga de la CPU.

> [!success]- Respuesta
>
> - b. ✅ Las instrucciones se ejecutan siguiendo una secuencia única, predecible y completamente determinada por el código y sus entradas.
>
> *Por qué:* orden total = **secuencia única y predecible**, fijada por el código y las entradas. Conocer el orden dentro de cada hilo pero no la intercalación es orden parcial; depender del planificador es justo lo que el orden total excluye. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P7 · Race condition vs. data race
> ¿Cuál es la relación conceptual entre una **condición de carrera** (_race condition_) y una **carrera de datos** (_data race_)?
> - a. La carrera de datos es un caso específico de condición de carrera, circunscrito concretamente al acceso concurrente no sincronizado y escritura en memoria compartida.
> - b. La condición de carrera solo afecta a variables locales, y la carrera de datos a sockets de red.
> - c. Son conceptos sinónimos e idénticos en todos los niveles de abstracción del software.
> - d. La carrera de datos ocurre solo en programas secuenciales, mientras que la condición de carrera en distribuidos.

> [!success]- Respuesta
>
> - a. ✅ La carrera de datos es un caso específico de condición de carrera, circunscrito concretamente al acceso concurrente no sincronizado y escritura en memoria compartida.
>
> *Por qué:* la *data race* es un **caso concreto** de *race condition*: accesos no sincronizados a memoria compartida con al menos una escritura. No son sinónimos y ninguno se limita a variables locales o a sockets. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]

> [!question] P8 · ¿Carrera en un programa secuencial?
> ¿Puede ocurrir una condición de carrera en un programa estrictamente **secuencial** mono-hilo sin interrupciones asíncronas?
> - a. Sí, debido a que la memoria RAM siempre tiene fluctuaciones en el voltaje.
> - b. Sí, si el programa contiene bucles anidados con más de tres variables enteras.
> - c. No, porque las instrucciones siguen un orden total totalmente determinado por el código y los datos de entrada.
> - d. Solo si se utilizan punteros a funciones en lugar de llamadas directas.

> [!success]- Respuesta
>
> - c. ✅ No, porque las instrucciones siguen un orden total totalmente determinado por el código y los datos de entrada.
>
> *Por qué:* no: un programa secuencial tiene **orden total**, un único camino determinista sin intercalación. Voltaje, bucles o punteros no generan carreras. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P9 · Diseño robusto frente al orden parcial
> Para que un programa concurrente sea robusto frente al orden parcial de ejecución, ¿en qué principio debe basarse su diseño?
> - a. En asumir que el sistema operativo siempre otorgará el mismo intervalo de tiempo (*quantum*) a cada hilo de forma fija.
> - b. En introducir pausas artificiales fijas (como `sleep`) para intentar predecir cuál terminará antes.
> - c. En ejecutar todos los hilos siempre en modo núcleo deshabilitando las interrupciones externas.
> - d. En garantizar la corrección del resultado con independencia del orden o velocidad de intercalación con que el procesador ejecute los hilos.

> [!success]- Respuesta
>
> - d. ✅ En garantizar la corrección del resultado con independencia del orden o velocidad de intercalación con que el procesador ejecute los hilos.
>
> *Por qué:* el programa debe ser **correcto con cualquier orden o velocidad de intercalación**. Suponer quantums fijos o meter `sleep` para "adivinar" el orden es la causa típica de errores, y desactivar interrupciones no es una solución de diseño. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!question] P10 · Instrucciones dentro de un hilo
> Dentro de los límites de un **hilo individual** en un sistema concurrente, ¿cómo se ejecutan sus propias instrucciones?
> - a. En orden parcial dentro de su propia pila de llamadas locales.
> - b. De forma caótica, alterando el orden interno de las sentencias del programador al azar.
> - c. De forma secuencial, manteniendo su orden interno de ejecución.
> - d. En orden inverso a como fueron declaradas en la función principal.

> [!success]- Respuesta
>
> - c. ✅ De forma secuencial, manteniendo su orden interno de ejecución.
>
> *Por qué:* dentro de cada hilo la ejecución es **secuencial**; lo impredecible es cómo se intercalan los hilos entre sí. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P11 · Orden parcial
> ¿Qué se entiende por **orden parcial** en programación concurrente?
> - a. Las instrucciones dentro de cada hilo se ejecutan en orden aleatorio según las interrupciones hardware.
> - b. Solo se ejecutan una parte de los hilos creados debido a limitaciones de memoria.
> - c. El programador fija estáticamente en tiempo de compilación el entrelazado de los hilos.
> - d. Se conoce el orden de ejecución dentro de cada proceso o hilo, pero no el orden en el que se intercalan entre sí.

> [!success]- Respuesta
>
> - d. ✅ Se conoce el orden de ejecución dentro de cada proceso o hilo, pero no el orden en el que se intercalan entre sí.
>
> *Por qué:* orden parcial = **se conoce el orden dentro de cada hilo, pero no cómo se intercalan**. No es aleatorio dentro del hilo, ni significa que se ejecuten solo algunos, ni lo fija el programador al compilar. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P12 · Tres condiciones de la data race
> ¿Cuáles son las **tres condiciones simultáneas** que deben cumplirse para que exista una **carrera de datos** (_data race_)?
> - a. Dos hilos ejecutan la misma función, ambos leen la misma variable y no usan semáforos.
> - b. Un hilo escribe en una variable local, otro escribe en memoria secundaria y ambos usan exclusión mutua.
> - c. Tres procesos compiten por el mismo descriptor de fichero en modo solo lectura de forma sincronizada.
> - d. Dos o más hilos acceden a la misma variable compartida, al menos uno realiza una escritura y los accesos no están sincronizados.

> [!success]- Respuesta
>
> - d. ✅ Dos o más hilos acceden a la misma variable compartida, al menos uno realiza una escritura y los accesos no están sincronizados.
>
> *Por qué:* **misma variable compartida + al menos una escritura + accesos sin sincronizar**. Las demás opciones fallan en alguna: solo lecturas, uso de exclusión mutua o acceso sincronizado. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]

> [!question] P13 · Cuándo hay race condition
> ¿Cuándo se produce una **condición de carrera** (_race condition_)?
> - a. Cuando la corrección del programa depende críticamente de una secuencia o _timing_ de intercalación concreto de sus hilos.
> - b. Cuando un hilo consume el 100% de la CPU impidiendo que los demás comiencen su ejecución.
> - c. Cuando un proceso padre finaliza antes que sus hijos generando procesos zombies.
> - d. Siempre que dos hilos acceden en modo solo lectura a una constante global.

> [!success]- Respuesta
>
> - a. ✅ Cuando la corrección del programa depende críticamente de una secuencia o _timing_ de intercalación concreto de sus hilos.
>
> *Por qué:* cuando **la corrección depende del orden o del *timing*** de intercalación. Acaparar la CPU es inanición; los zombis son otro tema; leer una constante es seguro. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!question] P14 · Para qué sincronizar
> ¿Cuál es la finalidad principal de utilizar **mecanismos de sincronización** (como exclusión mutua o semáforos) en programación concurrente?
> - a. Eliminar por completo la necesidad de tener un planificador de procesos en el sistema operativo.
> - b. Obligar a la CPU a ejecutar todos los hilos siempre a la velocidad máxima del reloj.
> - c. Controlar y proteger el acceso a variables y recursos compartidos para garantizar la consistencia y corrección frente al entrelazado de hilos.
> - d. Evitar que los programas concurrentes hagan uso de memoria RAM compartida.

> [!success]- Respuesta
>
> - c. ✅ Controlar y proteger el acceso a variables y recursos compartidos para garantizar la consistencia y corrección frente al entrelazado de hilos.
>
> *Por qué:* para **proteger el acceso a recursos compartidos** y que el resultado sea correcto con cualquier intercalación. No elimina el planificador, no fuerza la velocidad de la CPU ni prohíbe la memoria compartida. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!question] P15 · De qué depende la intercalación
> ¿De cuáles de los siguientes factores depende la secuencia exacta en que se intercalan los hilos concurrentes?
> - a. De la velocidad fija del bus de datos, siendo idéntica en cada ejecución con los mismos datos.
> - b. Únicamente del compilador al generar el código binario durante el enlazado.
> - c. De decisiones del planificador del sistema operativo, la carga del sistema, interrupciones y eventos asíncronos.
> - d. Exclusivamente del orden en que el código fuente declara las variables compartidas.

> [!success]- Respuesta
>
> - c. ✅ De decisiones del planificador del sistema operativo, la carga del sistema, interrupciones y eventos asíncronos.
>
> *Por qué:* depende de **factores externos al código**: planificador, carga del sistema, interrupciones y eventos asíncronos. Por eso no es la misma en cada ejecución ni la fija el compilador. [[1.5 - Orden de ejecucion#1. Orden total vs. orden parcial|Ver 1.5 · Orden total vs. parcial]]

> [!question] P16 · NO es consecuencia de una race condition
> ¿Cuál de las siguientes **NO** es una consecuencia típica provocada por condiciones de carrera?
> - a. Comportamiento errático e impredecible en distintas ejecuciones con idénticos datos de entrada.
> - b. Corrupción de memoria o resultados inconsistentes e incorrectos.
> - c. Aparición de vulnerabilidades de seguridad susceptibles de ser explotadas por atacantes.
> - d. Optimización determinista en el tiempo de procesamiento de cada instrucción.

> [!success]- Respuesta
>
> - d. ✅ Optimización determinista en el tiempo de procesamiento de cada instrucción.
>
> *Por qué:* las carreras **no** dan ninguna "optimización determinista": provocan comportamiento errático, corrupción de datos y vulnerabilidades (las otras tres opciones sí son consecuencias). [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!question] P17 · Por qué cuesta depurar las carreras
> ¿Por qué las condiciones de carrera son consideradas uno de los errores más difíciles de depurar en el software?
> - a. Porque pueden presentarse de forma esporádica e intermitente bajo cargas específicas, haciendo difícil reproducir el error.
> - b. Porque las condiciones de carrera solo se manifiestan en sistemas con un único núcleo de procesador.
> - c. Porque siempre provocan un cuelgue inmediato del núcleo del sistema operativo en el primer milisegundo.
> - d. Porque el compilador impide generar el ejecutable si detecta hilos en el código.

> [!success]- Respuesta
>
> - a. ✅ Porque pueden presentarse de forma esporádica e intermitente bajo cargas específicas, haciendo difícil reproducir el error.
>
> *Por qué:* son **intermitentes**: aparecen solo a veces o con cierta carga y son difíciles de reproducir. Se dan también en multinúcleo, no siempre cuelgan el sistema y el compilador no las detecta. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!question] P18 · `cuenta++` da 1 en vez de 2
> Dos hilos incrementan en 1 una variable global compartida `cuenta = 0` mediante la instrucción `cuenta++` sin sincronización. ¿Por qué el valor final puede ser 1 en lugar de 2?
> - a. Porque los operadores de incremento unitario están prohibidos por el estándar en programas concurrentes.
> - b. Porque la memoria RAM borra automáticamente las variables cuando dos hilos intentan acceder al mismo ciclo de reloj.
> - c. Porque la operación consta de lectura, modificación y escritura; si sus secuencias se intercalan, ambos hilos pueden leer el valor original y sobreescribirse mutuamente.
> - d. Porque el planificador cancela de inmediato uno de los hilos si detecta operaciones aritméticas.

> [!success]- Respuesta
>
> - c. ✅ Porque la operación consta de lectura, modificación y escritura; si sus secuencias se intercalan, ambos hilos pueden leer el valor original y sobreescribirse mutuamente.
>
> *Por qué:* `cuenta++` es **leer, sumar y escribir**; si los dos hilos leen 0 antes de que el otro escriba, ambos escriben 1 y se pierde un incremento. No está prohibido, la RAM no borra nada y el planificador no cancela hilos. [[1.5 - Orden de ejecucion#3. Carrera de datos (data race)|Ver 1.5 · Carrera de datos]]

> [!question] P19 · ¿Indeterminismo = programa incorrecto?
> ¿El comportamiento indeterminista (posibles diferentes secuencias de ejecución ante las mismas entradas) implica necesariamente que un programa concurrente sea incorrecto?
> - a. Sí, porque el estándar POSIX exige determinismo estricto en el resultado y en el tiempo de ejecución.
> - b. Sí, por definición cualquier programa que no presente orden total se considera defectuoso.
> - c. No, que existan diferentes caminos de ejecución no significa por sí solo que el programa sea incorrecto, siempre que todos conduzcan a un resultado válido.
> - d. No, siempre y cuando el sistema operativo desactive la multitarea apropiativa.

> [!success]- Respuesta
>
> - c. ✅ No, que existan diferentes caminos de ejecución no significa por sí solo que el programa sea incorrecto, siempre que todos conduzcan a un resultado válido.
>
> *Por qué:* no: puede haber **varios caminos de ejecución y ser correcto** si todos llevan a un resultado válido (por ejemplo, otro orden de impresión). POSIX no exige determinismo y desactivar la multitarea no es la condición. [[1.5 - Orden de ejecucion#2. Condición de carrera (race condition)|Ver 1.5 · Condición de carrera]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 5
> P1 **d** · P2 **c** · P3 **a** · P4 **b** · P5 **d**  
> P6 **b** · P7 **a** · P8 **c** · P9 **d** · P10 **c**  
> P11 **d** · P12 **d** · P13 **a** · P14 **c** · P15 **c**  
> P16 **d** · P17 **a** · P18 **c** · P19 **c**  

---

### Simulacro 6 · 1.6 · Sincronización

> [!abstract] Simulacro 6
> **20 preguntas** · ⏱️ ~10 min · Fuente: [[Cuestionario 1-6]] · [[1.6 - Sincronizacion|Apuntes del 1.6]] · Tu nota en Moodle: **20/20**

> [!question] P1 · `wait()` dentro de `synchronized`
> En Java, ¿cuál es el comportamiento específico de la invocación al método `wait()` dentro de un bloque sincronizado?
> - a. Suspende el hilo actual y libera de manera atómica el cerrojo del monitor, permitiendo la entrada a otros hilos.
> - b. Termina definitivamente la ejecución del hilo y destruye su pila de ejecución.
> - c. Pone al hilo en espera activa (_busy waiting_) consumiendo CPU mientras retiene el cerrojo.
> - d. Suspende al hilo pero mantiene el bloqueo exclusivo del objeto impidiendo todo acceso exterior.

> [!success]- Respuesta
>
> - a. ✅ Suspende el hilo actual y libera de manera atómica el cerrojo del monitor, permitiendo la entrada a otros hilos.
>
> *Por qué:* `wait()` **suspende el hilo y libera el cerrojo** de forma atómica para que otros puedan cambiar la condición. No termina el hilo, no hace espera activa y no conserva el bloqueo (eso causaría deadlock). [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]

> [!question] P2 · Qué es un monitor
> ¿Qué es un **monitor** en el contexto del diseño de sistemas concurrentes?
> - a. Una herramienta gráfica externa que supervisa el uso de procesador y memoria de la JVM.
> - b. Un hilo del sistema encargado de terminar procesos que causan condiciones de carrera.
> - c. Un cerrojo de bajo nivel que solo permite sincronización de control sin admitir datos compartidos.
> - d. Una abstracción de alto nivel que encapsula un recurso integrando exclusión mutua y sincronización condicional (espera y notificación).

> [!success]- Respuesta
>
> - d. ✅ Una abstracción de alto nivel que encapsula un recurso integrando exclusión mutua y sincronización condicional (espera y notificación).
>
> *Por qué:* abstracción de alto nivel que **encapsula un recurso con exclusión mutua y sincronización condicional** (espera y notificación). No es una herramienta gráfica ni un hilo que mata procesos, y sí admite datos compartidos. [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]

> [!question] P3 · Origen del problema de visibilidad
> En el contexto del modelo de memoria de Java (JMM), ¿por qué se produce fundamentalmente el problema de la visibilidad de datos entre hilos?
> - a. Porque la memoria RAM física prohíbe que dos hilos compartan la misma dirección de memoria virtual.
> - b. Porque los hilos operan sobre copias locales en sus cachés de trabajo y no hay garantía inmediata de propagación a la memoria principal.
> - c. Porque el compilador de Java convierte automáticamente todas las variables en constantes inmutables.
> - d. Porque el recolector de basura (Garbage Collector) elimina periódicamente las variables no sincronizadas.

> [!success]- Respuesta
>
> - b. ✅ Porque los hilos operan sobre copias locales en sus cachés de trabajo y no hay garantía inmediata de propagación a la memoria principal.
>
> *Por qué:* cada hilo trabaja con **copias en su caché** y el JMM no garantiza cuándo se propagan a memoria principal. La RAM no lo prohíbe, el compilador no convierte variables en constantes y el GC no borra variables "no sincronizadas". [[1.6 - Sincronizacion#4. El problema de la visibilidad de datos|Ver 1.6 · Visibilidad de datos]]

> [!question] P4 · `notify()` vs. `notifyAll()`
> ¿Cuál es la diferencia fundamental entre los métodos `notify()` y `notifyAll()` en el modelo de monitores de Java?
> - a. `notify()` despierta de forma arbitraria a un único hilo en espera, mientras que `notifyAll()` despierta a todos los hilos que esperan sobre dicho monitor.
> - b. `notify()` solo sirve para hilos prioritarios y `notifyAll()` para hilos demonio (_daemon_).
> - c. `notifyAll()` reinicia la JVM y `notify()` reinicia únicamente el hilo en ejecución.
> - d. `notify()` libera el bloqueo de inmediato, mientras que `notifyAll()` retiene el bloqueo permanentemente.

> [!success]- Respuesta
>
> - a. ✅ `notify()` despierta de forma arbitraria a un único hilo en espera, mientras que `notifyAll()` despierta a todos los hilos que esperan sobre dicho monitor.
>
> *Por qué:* `notify()` despierta a **un** hilo cualquiera; `notifyAll()`, a **todos** (que luego compiten por el cerrojo). No dependen de la prioridad, no reinician nada y ninguno libera ni retiene el cerrojo "permanentemente". [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]

> [!question] P5 · Reducir la contención
> ¿Cuál de las siguientes medidas es una técnica efectiva para reducir la contención por bloqueo en aplicaciones concurrentes?
> - a. Reducir el tamaño y la duración del código dentro de la sección crítica.
> - b. Aumentar el número de hilos que compiten simultáneamente por el mismo cerrojo.
> - c. Incluir llamadas de E/S bloqueantes (como acceso a disco o red) dentro de la sección crítica.
> - d. Reemplazar todos los cerrojos por bucles de espera activa (_busy waiting_).

> [!success]- Respuesta
>
> - a. ✅ Reducir el tamaño y la duración del código dentro de la sección crítica.
>
> *Por qué:* **secciones críticas cortas**: si el cerrojo se retiene menos tiempo, los demás esperan menos. Más hilos, E/S dentro de la sección crítica o espera activa la empeoran. [[1.6 - Sincronizacion#3.3 Exclusión mutua y mutex|Ver 1.6 · Exclusión mutua y mutex]]

> [!question] P6 · `while(running)` sin `volatile`
> Un hilo _A_ actualiza una variable `boolean running = true` a `false`. Si la variable no es `volatile` ni se usa sincronización, ¿qué anomalía clásica puede manifestar el hilo _B_ que ejecuta `while(running) { }`?
> - a. El hilo _B_ puede seguir leyendo el valor `true` de su caché local y quedar atrapado indefinidamente en el bucle.
> - b. La máquina virtual detendrá forzosamente ambos hilos por desbordamiento de pila (_StackOverflowError_).
> - c. El hilo _B_ provocará inmediatamente un error de tipo `NullPointerException`.
> - d. El hilo _A_ se quedará suspendido automáticamente a la espera de que _B_ termine.

> [!success]- Respuesta
>
> - a. ✅ El hilo _B_ puede seguir leyendo el valor `true` de su caché local y quedar atrapado indefinidamente en el bucle.
>
> *Por qué:* B puede seguir viendo `true` en su caché (o el JIT puede optimizar la lectura) y **quedarse en el bucle para siempre**. No hay `StackOverflowError`, `NullPointerException` ni suspensión automática de A. [[1.6 - Sincronizacion#4. El problema de la visibilidad de datos|Ver 1.6 · Visibilidad de datos]]

> [!question] P7 · `x = x + 1` en paralelo
> A nivel de código máquina, la instrucción `x = x + 1` se descompone en `LOAD X R1`, `ADD R1 1` y `STORE R1 X`. Si dos hilos la ejecutan en paralelo sin exclusión mutua partiendo de _x = 0_, ¿cuál es un resultado erróneo posible por entrelazamiento?
> - a. El valor final de _x_ es siempre 0 debido a un reinicio de memoria.
> - b. El hardware del procesador aborta automáticamente la ejecución lanzando un trap.
> - c. El valor final de _x_ es 1, perdiéndose uno de los dos incrementos.
> - d. El valor final de _x_ será 3 por desbordamiento de registro.

> [!success]- Respuesta
>
> - c. ✅ El valor final de _x_ es 1, perdiéndose uno de los dos incrementos.
>
> *Por qué:* ambos hacen `LOAD` de 0, suman 1 y hacen `STORE` de 1: **x = 1, se pierde un incremento**. El hardware no aborta, no da 0 por "reinicio" ni 3 por desbordamiento. [[1.6 - Sincronizacion#3.1 Por qué fallan las condiciones 1ª y 2ª: escrituras no atómicas|Ver 1.6 · Escrituras no atómicas]]

> [!question] P8 · Qué garantiza `volatile`
> ¿Qué efecto garantiza el uso de la palabra clave `volatile` sobre un campo en Java?
> - a. Bloquea el objeto impidiendo que cualquier otro hilo lea la variable hasta que finalice el método.
> - b. Convierte el tipo de dato en inmutable de sólo lectura durante la ejecución.
> - c. Garantiza atomicidad completa en operaciones compuestas como `count++`.
> - d. Garantiza que las lecturas y escrituras se realicen directamente sobre la memoria principal, asegurando visibilidad inmediata.

> [!success]- Respuesta
>
> - d. ✅ Garantiza que las lecturas y escrituras se realicen directamente sobre la memoria principal, asegurando visibilidad inmediata.
>
> *Por qué:* `volatile` garantiza **visibilidad**: lecturas y escrituras van a memoria principal. **No** da atomicidad a `count++`, no bloquea el objeto (eso es `synchronized`) ni lo hace inmutable (`final`). [[1.6 - Sincronizacion#4. El problema de la visibilidad de datos|Ver 1.6 · Visibilidad de datos]]

> [!question] P9 · `x + 5` y `x * 2` concurrentes
> Un sistema cuenta con una variable compartida _x_. El hilo _T1_ ejecuta la instrucción `x = x + 5` y el hilo _T2_ ejecuta `x = x * 2`. ¿Por qué se requiere sincronización de acceso a datos en este escenario?
> - a. Porque las operaciones aritméticas simples no pueden ejecutarse en CPUs multinúcleo.
> - b. Para evitar lecturas o escrituras entrelazadas no atómicas sobre _x_.
> - c. Porque el sistema operativo suspende automáticamente los procesos que usan multiplicaciones concurrentes.
> - d. Únicamente para forzar que _T1_ se ejecute siempre antes que _T2_.

> [!success]- Respuesta
>
> - b. ✅ Para evitar lecturas o escrituras entrelazadas no atómicas sobre _x_.
>
> *Por qué:* las dos operaciones leen y escriben la misma `x` **sin atomicidad**, así que sus pasos se pueden entrelazar. El problema no es forzar un orden concreto (eso sería sincronización de control) y las CPUs multinúcleo sí calculan. [[1.6 - Sincronizacion#3.1 Por qué fallan las condiciones 1ª y 2ª: escrituras no atómicas|Ver 1.6 · Escrituras no atómicas]]

> [!question] P10 · Consumidor espera sin soltar el cerrojo
> En el problema del Productor-Consumidor con buffer limitado, ¿qué sucede si el consumidor comprueba que el buffer está vacío y se queda esperando dentro de la sección crítica sin liberar el cerrojo?
> - a. El buffer amplía dinámicamente su capacidad para resolver la condición.
> - b. El consumidor consumirá elementos nulos sin generar consecuencias adversas.
> - c. Se produce un interbloqueo (_deadlock_), pues el productor no puede entrar a insertar elementos para que se cumpla la condición.
> - d. El sistema operativo expulsa automáticamente al consumidor para permitir el paso al productor.

> [!success]- Respuesta
>
> - c. ✅ Se produce un interbloqueo (_deadlock_), pues el productor no puede entrar a insertar elementos para que se cumpla la condición.
>
> *Por qué:* si el consumidor espera **con el cerrojo cogido**, el productor no puede entrar a añadir elementos: **deadlock**. El buffer no crece solo y el SO no expulsa al consumidor para dejar pasar al productor. [[1.6 - Sincronizacion#5. Condición de sincronización|Ver 1.6 · Condición de sincronización]]

> [!question] P11 · Pipeline: B depende de A
> En un sistema de procesamiento por etapas (_pipeline_), la tarea _B_ requiere como entrada indispensable los datos procesados previamente por la tarea _A_. ¿Qué tipo de sincronización se requiere principalmente?
> - a. Sincronización de memoria caché local.
> - b. No se requiere sincronización si las tareas corren en hilos separados.
> - c. Exclusión mutua pura sin dependencias.
> - d. Sincronización de control.

> [!success]- Respuesta
>
> - d. ✅ Sincronización de control.
>
> *Por qué:* si B necesita los resultados de A hay que coordinar el **orden**: **sincronización de control**. La exclusión mutua protege datos, no impone precedencias. [[1.6 - Sincronizacion#1. Sincronización de tareas|Ver 1.6 · Sincronización de tareas]]

> [!question] P12 · `y + 1` e `y - 1`: secciones críticas
> Dos bloques de código en hilos distintos modifican la misma variable compartida _y_: uno realiza `y = y + 1` y el otro `y = y - 1`. ¿Cómo se definen estas regiones en relación al concepto de sección crítica?
> - a. Constituyen dos secciones críticas completamente independientes gestionadas por distintos mutexes.
> - b. No se consideran regiones críticas porque una suma y la otra resta, cancelándose el efecto.
> - c. Son dos regiones críticas que pertenecen a la misma sección crítica asociada al recurso compartido _y_.
> - d. Solo el incremento es una región crítica; el decremento es una operación no bloqueante.

> [!success]- Respuesta
>
> - c. ✅ Son dos regiones críticas que pertenecen a la misma sección crítica asociada al recurso compartido _y_.
>
> *Por qué:* son **dos regiones críticas de la misma sección crítica**, la del recurso `y`. Se protegen con el mismo mutex; que se compensen en teoría no evita la carrera. [[1.6 - Sincronizacion#3.2 Sección crítica|Ver 1.6 · Sección crítica]]

> [!question] P13 · `wait()`/`notify()` sin el cerrojo
> En Java, ¿qué ocurre si un hilo intenta invocar el método `wait()` o `notify()` sobre un objeto sin haber obtenido previamente su bloqueo mediante un bloque o método `synchronized`?
> - a. El objeto adquiere automáticamente el cerrojo de forma implícita sin advertencias.
> - b. El hilo entra en un estado zombi no recuperable por el sistema operativo.
> - c. El código no compila generando un error de tipado estático.
> - d. Se produce una excepción de tipo `IllegalMonitorStateException` en tiempo de ejecución.

> [!success]- Respuesta
>
> - d. ✅ Se produce una excepción de tipo `IllegalMonitorStateException` en tiempo de ejecución.
>
> *Por qué:* lanza **`IllegalMonitorStateException`** en **tiempo de ejecución**. Compila sin problemas, no coge el cerrojo implícitamente y no hay estados "zombi" de hilos. [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]

> [!question] P14 · Suspensión vs. espera activa
> ¿Por qué el mecanismo de suspensión y notificación es más eficiente que el bucle de espera activa (_busy waiting_ / spinlock) al esperar una condición de sincronización prolongada?
> - a. Porque el hilo suspendido cede el procesador, evitando el consumo inútil de ciclos de CPU mientras espera la condición.
> - b. Porque la espera activa satura la memoria secundaria liberando excesiva CPU.
> - c. Porque el compilador prohíbe la inclusión de bucles condicionales dentro de programas concurrentes.
> - d. Porque la suspensión garantiza que el hilo se ejecute siempre con la máxima prioridad del planificador.

> [!success]- Respuesta
>
> - a. ✅ Porque el hilo suspendido cede el procesador, evitando el consumo inútil de ciclos de CPU mientras espera la condición.
>
> *Por qué:* el hilo suspendido **cede la CPU** y no gasta ciclos mientras espera. La espera activa consume CPU (no memoria secundaria) y suspenderse no da más prioridad. [[1.6 - Sincronizacion#5. Condición de sincronización|Ver 1.6 · Condición de sincronización]]

> [!question] P15 · Bernstein: mismo `log.txt`
> Considere dos procesos _PA_ y _PB_ que modifican un mismo archivo compartido de registro. Si _E(PA) = {log.txt}_ y _E(PB) = {log.txt}_, ¿qué condición de Bernstein no se cumple?
> - a. Independencia de flujo de instrucciones.
> - b. Independencia de entrada exclusiva.
> - c. Independencia de salida (_E(PA) ∩ E(PB) = ∅_).
> - d. Se cumplen todas las condiciones si el archivo se abre en modo append.

> [!success]- Respuesta
>
> - c. ✅ Independencia de salida (_E(PA) ∩ E(PB) = ∅_).
>
> *Por qué:* ambos escriben en el mismo recurso: E(PA) ∩ E(PB) ≠ ∅ → falla la **independencia de salida**. Abrir en modo *append* no anula la condición teórica. [[1.6 - Sincronizacion#2.2 Independencia de salida|Ver 1.6 · Independencia de salida]]

> [!question] P16 · Bernstein: L(P1) ∩ E(P2) ≠ ∅
> Si dos procesos _P1_ y _P2_ cumplen que _L(P1) ∩ E(P2) ≠ ∅_, ¿cuál es la consecuencia directa según el Teorema de Bernstein?
> - a. Se viola la independencia de entrada, exigiendo sincronización de acceso para evitar que _P1_ lea datos mientras _P2_ los modifica.
> - b. Ambos procesos pueden ejecutarse concurrentemente sin ningún tipo de sincronización.
> - c. Se produce una violación estricta de la independencia de salida.
> - d. Se garantiza la ausencia total de condiciones de carrera.

> [!success]- Respuesta
>
> - a. ✅ Se viola la independencia de entrada, exigiendo sincronización de acceso para evitar que _P1_ lea datos mientras _P2_ los modifica.
>
> *Por qué:* lo que lee uno lo escribe el otro: se viola la **independencia de entrada** y hay que sincronizar. No es la de salida (sería E ∩ E) y desde luego no garantiza ausencia de carreras. [[1.6 - Sincronizacion#2.1 Independencia de entrada|Ver 1.6 · Independencia de entrada]]

> [!question] P17 · Bernstein: E(S1) ∩ L(S2) = {c}
> Sean dos conjuntos de instrucciones _S1_ y _S2_ con los siguientes conjuntos de lectura y escritura:
> _L(S1) = {a, b}_, _E(S1) = {c}_
> _L(S2) = {c, d}_, _E(S2) = {e}_
> ¿Qué condición del Teorema de Bernstein se viola impidiendo su ejecución concurrente sin sincronización?
> - a. Se cumplen todas las condiciones y pueden ejecutarse en paralelo de forma segura.
> - b. La condición de independencia de salida (_E(S1) ∩ E(S2) = ∅_).
> - c. La condición simétrica de lectura (_L(S1) ∩ E(S2) = ∅_).
> - d. La condición de independencia de flujo de datos (_E(S1) ∩ L(S2) = ∅_).

> [!success]- Respuesta
>
> - d. ✅ La condición de independencia de flujo de datos (_E(S1) ∩ L(S2) = ∅_).
>
> *Por qué:* `S1` escribe `c` y `S2` lo lee: **independencia de flujo de datos** violada (`S2` depende de `S1`). E(S1) ∩ E(S2) = ∅ y L(S1) ∩ E(S2) = ∅, así que esas sí se cumplen. [[1.6 - Sincronizacion#2.3 Independencia de flujo de datos|Ver 1.6 · Independencia de flujo de datos]]

> [!question] P18 · Bernstein: todo disjunto
> Si dos procesos _S1_ y _S2_ tienen los siguientes conjuntos de variables:
> _L(S1) = {x}_, _E(S1) = {y}_
> _L(S2) = {z}_, _E(S2) = {w}_
> ¿Qué se concluye según el Teorema de Bernstein?
> - a. Se produce una condición de carrera sobre el bus de memoria impidiendo el paralelismo real.
> - b. Requieren obligatoriamente un mutex para proteger la variable _y_ del proceso _S2_.
> - c. No pueden ejecutarse en paralelo porque sus conjuntos no comparten memoria de sincronización.
> - d. Se cumplen simultáneamente las tres condiciones de independencia y pueden ejecutarse en paralelo de forma segura sin sincronización adicional.

> [!success]- Respuesta
>
> - d. ✅ Se cumplen simultáneamente las tres condiciones de independencia y pueden ejecutarse en paralelo de forma segura sin sincronización adicional.
>
> *Por qué:* todas las intersecciones (L∩E, E∩L, E∩E) son vacías: **se cumplen las tres condiciones** y pueden ir en paralelo sin sincronizar. No comparten variables, así que no hace falta mutex. [[1.6 - Sincronizacion#2. Teorema de Bernstein|Ver 1.6 · Teorema de Bernstein]]

> [!question] P19 · Lock contention
> ¿Qué es la contención por bloqueo (_lock contention_) y qué impacto produce en un sistema concurrente?
> - a. Es la competencia de varios hilos por un mismo bloqueo, que degrada el rendimiento al suspender o bloquear hilos en espera.
> - b. Es la corrupción irrecuperable de la tabla de hilos en el kernel del sistema operativo.
> - c. Es una técnica de optimización que acelera la ejecución concurrente eliminando los cerrojos.
> - d. Es un fallo del hardware en el que dos hilos acceden al mismo registro físico simultáneamente.

> [!success]- Respuesta
>
> - a. ✅ Es la competencia de varios hilos por un mismo bloqueo, que degrada el rendimiento al suspender o bloquear hilos en espera.
>
> *Por qué:* varios hilos **compiten por el mismo cerrojo** y el rendimiento cae porque esperan sin trabajar. No es corrupción del kernel, ni una optimización, ni un fallo de hardware. [[1.6 - Sincronizacion#3.3 Exclusión mutua y mutex|Ver 1.6 · Exclusión mutua y mutex]]

> [!question] P20 · Condición del productor en buffer acotado
> ¿Qué condición de sincronización debe verificarse y cumplirse para que un hilo productor pueda depositar de forma segura un nuevo elemento en un buffer acotado de capacidad _N_?
> - a. Que el hilo consumidor se encuentre activo en la CPU en ese instante.
> - b. Que el buffer esté completamente vacío (número de elementos = 0).
> - c. Que el buffer no esté lleno (número de elementos < _N_).
> - d. Que no existan hilos consumidores registrados en la aplicación.

> [!success]- Respuesta
>
> - c. ✅ Que el buffer no esté lleno (número de elementos < _N_).
>
> *Por qué:* el productor puede depositar si el buffer **no está lleno** (elementos < N); si lo está, espera. No necesita que esté vacío ni que el consumidor esté en la CPU. [[1.6 - Sincronizacion#5.1 Productor-Consumidor|Ver 1.6 · Productor-Consumidor]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 6
> P1 **a** · P2 **d** · P3 **b** · P4 **a** · P5 **a**  
> P6 **a** · P7 **c** · P8 **d** · P9 **b** · P10 **c**  
> P11 **d** · P12 **c** · P13 **d** · P14 **a** · P15 **c**  
> P16 **a** · P17 **d** · P18 **d** · P19 **a** · P20 **c**  

---

### Simulacro 7 · 1.7 · Comunicación entre procesos

> [!abstract] Simulacro 7
> **19 preguntas** · ⏱️ ~10 min · Fuente: [[Cuestionario 1-7]] · [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Guía · A.7]] (el apartado 1.7 aún no tiene nota propia) · Tu nota en Moodle: **18/19**

> [!question] P1 · Memoria compartida
> En el modelo de comunicación a través de ______, las tareas concurrentes comparten un espacio de memoria principal común, lo que requiere mecanismos de sincronización explícitos para evitar condiciones de carrera.

> [!success]- Respuesta
>
> - **memoria compartida**
>
> *Por qué:* compartir un espacio de memoria común, con sincronización explícita, es el modelo de **memoria compartida** (típico del multihilo). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P2 · Sockets vs. memoria compartida
> ¿Qué compromiso (trade-off) en términos de rendimiento y complejidad presenta el paso de mensajes mediante sockets de red frente al acceso a memoria compartida?
> - a. Los sockets ofrecen menor latencia que la memoria compartida, pero aumentan el peligro de condiciones de carrera directas sobre las variables del hilo remoto.
> - b. Los sockets eliminan la sobrecarga de serialización a costa de requerir una región de memoria física directamente accesible por todos los ordenadores.
> - c. Los sockets permiten la comunicación entre máquinas distribuidas, pero introducen mayor latencia y sobrecarga debido a la serialización de mensajes y la transmisión por red.
> - d. La memoria compartida genera mayor latencia en comunicaciones locales, pero simplifica la transmisión de mensajes entre nodos físicamente separados.

> [!success]- Respuesta
>
> - c. ✅ Los sockets permiten la comunicación entre máquinas distribuidas, pero introducen mayor latencia y sobrecarga debido a la serialización de mensajes y la transmisión por red.
>
> *Por qué:* los sockets permiten **comunicar máquinas distintas**, pero añaden **latencia y sobrecarga** (serializar y transmitir). La memoria compartida es la de menor latencia en local y no sirve entre nodos separados. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P3 · Canal
> El soporte físico o lógico (como una red, un cable o una región de memoria) a través del cual se transmite un mensaje del emisor al receptor se denomina ______.

> [!success]- Respuesta
>
> - **canal**
>
> *Por qué:* el soporte por el que viaja el mensaje es el **canal**. Los cuatro elementos son emisor, receptor, mensaje y canal. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P4 · Walkie-talkie
> Un sistema de comunicación mediante walkie-talkies o una vía estrecha de un solo carril con tráfico en ambos sentidos representan analogías de ¿qué tipo de canal según su capacidad?
> - a. Half duplex, ya que la comunicación es bidireccional pero alternante en el tiempo, impidiendo la transmisión simultánea.
> - b. Full duplex, dado que permite la interacción de dos partes de forma totalmente simultánea y sin esperas.
> - c. Símplex, puesto que la información fluye estrictamente en una única dirección sin posibilidad de retorno o respuesta.
> - d. Invocación remota, debido a que requiere un protocolo de red cliente-servidor estrictamente síncrono.

> [!success]- Respuesta
>
> - a. ✅ Half duplex, ya que la comunicación es bidireccional pero alternante en el tiempo, impidiendo la transmisión simultánea.
>
> *Por qué:* **half duplex**: los dos sentidos, pero **no a la vez**. Full duplex sería simultáneo (teléfono); símplex, un único sentido (radio, cine). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P5 · Símplex
> Un canal de comunicación en el que la información fluye estrictamente en una única dirección, actuando una entidad únicamente como emisor y la otra únicamente como receptor, se denomina ______.

> [!success]- Respuesta
>
> - **simplex**
>
> *Por qué:* un solo sentido, con un emisor y un receptor fijos = **símplex** (radiodifusión). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P6 · Full duplex
> En la clasificación según la capacidad del canal, un canal de comunicación de tipo ______ permite la transmisión bidireccional y simultánea de información entre el emisor y el receptor.

> [!success]- Respuesta
>
> - **full duplex**
>
> *Por qué:* bidireccional **y simultáneo** = **full duplex** (llamada telefónica). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P7 · Modelo híbrido
> Al diseñar un sistema complejo, los arquitectos deciden usar memoria compartida para coordinar hilos internos y paso de mensajes para la interacción entre servidores. ¿Por qué es adecuada esta decisión según el texto?
> - a. Porque la memoria compartida es la única opción válida en sistemas distribuidos y el paso de mensajes se limita exclusivamente a hilos de un mismo hilo.
> - b. Porque evita el uso de cerrojos o mutexes en la memoria local e impone canales full duplex síncronos en las máquinas remotas.
> - c. Porque el paso de mensajes por red elimina la necesidad de serializar datos, mientras que la memoria compartida gestiona automáticamente la red local.
> - d. Aprovecha el alto rendimiento y baja latencia de la memoria compartida a nivel local y utiliza el paso de mensajes para superar la ausencia de memoria física común entre servidores.

> [!success]- Respuesta
>
> - d. ✅ Aprovecha el alto rendimiento y baja latencia de la memoria compartida a nivel local y utiliza el paso de mensajes para superar la ausencia de memoria física común entre servidores.
>
> *Por qué:* se aprovecha la **baja latencia de la memoria compartida en local** y se usa **paso de mensajes entre servidores**, que no comparten memoria física. Las demás opciones invierten los papeles o dicen que se elimina la serialización. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P8 · Red P2P
> En una red peer-to-peer (P2P), donde todos los nodos pueden actuar tanto solicitando como ofreciendo información sin una jerarquía predefinida, se manifiesta una comunicación de tipo:
> - a. Simétrica (o entre pares).
> - b. Asimétrica (o cliente-servidor).
> - c. Invocación remota exclusivamente local.
> - d. Símplex no bloqueante.

> [!success]- Respuesta
>
> - a. ✅ Simétrica (o entre pares).
>
> *Por qué:* todos los nodos piden y ofrecen: comunicación **simétrica** (entre pares). Cliente-servidor es la asimétrica. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P9 · Simétrica vs. asimétrica
> ¿En qué se diferencian los modelos de comunicación simétrica y asimétrica según el comportamiento o rol de los interlocutores?
> - a. En la comunicación simétrica el canal es siempre half duplex, mientras que en la asimétrica debe ser obligatoriamente símplex.
> - b. La comunicación asimétrica solo se puede implementar mediante memoria compartida, mientras que la simétrica requiere sockets de red.
> - c. En la comunicación simétrica todos los procesos tienen el mismo rol y pueden ser emisores o receptores, mientras que en la asimétrica existen roles diferenciados de cliente y servidor.
> - d. La comunicación simétrica requiere que un proceso maestro gestione la cola de mensajes, mientras que la asimétrica no utiliza servidores.

> [!success]- Respuesta
>
> - c. ✅ En la comunicación simétrica todos los procesos tienen el mismo rol y pueden ser emisores o receptores, mientras que en la asimétrica existen roles diferenciados de cliente y servidor.
>
> *Por qué:* simétrica: **todos con el mismo rol**; asimétrica: **roles cliente y servidor**. No depende del tipo de canal ni de usar memoria compartida o sockets. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P10 · Ventaja del paso de mensajes
> ¿Cuál de las siguientes afirmaciones describe una ventaja del paso de mensajes en relación con la simplificación de la programación concurrente?
> - a. Permite modificar libremente las variables del espacio de memoria privado de otro proceso sin causar condiciones de carrera.
> - b. Garantiza que la latencia de transmisión a través de la red sea inferior a los accesos a la memoria búfer de la CPU.
> - c. Elimina totalmente la necesidad de coordinar la lógica de negocio o la secuencia de ejecución entre las tareas.
> - d. La sincronización suele estar implícita en las operaciones de envío y recepción, reduciendo la necesidad de utilizar mecanismos de sincronización explícitos a nivel de memoria.

> [!success]- Respuesta
>
> - d. ✅ La sincronización suele estar implícita en las operaciones de envío y recepción, reduciendo la necesidad de utilizar mecanismos de sincronización explícitos a nivel de memoria.
>
> *Por qué:* la sincronización queda **implícita en enviar y recibir**, así que hay menos cerrojos explícitos. No permite tocar la memoria de otro proceso, no es más rápido que la caché y no elimina la coordinación lógica. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P11 · Paso de mensajes con buffer en memoria
> Cuando se implementa el paso de mensajes utilizando un buffer de memoria compartido (como una cola de mensajes en memoria principal), ¿por qué sigue siendo necesario utilizar mecanismos de sincronización explícitos?
> - a. Porque el sistema operativo obliga a empaquetar los mensajes en tramas de red TCP/IP antes de depositar los datos en el buffer de la memoria RAM.
> - b. Porque las operaciones de encolado y desencolado sobre la estructura de datos compartida en memoria deben protegerse con exclusión mutua para evitar condiciones de carrera.
> - c. Porque el hardware de la memoria RAM prohíbe la lectura concurrente por múltiples hilos a menos que se destruya la cola.
> - d. Porque los buffers de memoria solo aceptan canales de tipo símplex unidireccional sin capacidad de almacenamiento temporal.

> [!success]- Respuesta
>
> - b. ✅ Porque las operaciones de encolado y desencolado sobre la estructura de datos compartida en memoria deben protegerse con exclusión mutua para evitar condiciones de carrera.
>
> *Por qué:* la cola es una estructura de datos compartida: **encolar y desencolar necesitan exclusión mutua**. No hay tramas TCP/IP en la RAM ni restricciones de símplex. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P12 · Emisor
> En los elementos básicos que intervienen en cualquier proceso de comunicación concurrente, la entidad que inicia la comunicación y genera la información se denomina ______.

> [!success]- Respuesta
>
> - **emisor**
>
> *Por qué:* quien inicia la comunicación y genera la información es el **emisor**. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P13 · Cliente-servidor ⚠️
> En un sistema donde los clientes inician las solicitudes y el servidor escucha y responde proporcionando servicios, se utiliza un tipo de comunicación según el rol de los interlocutores denominada ______.

> [!success]- Respuesta
>
> - **cliente-servidor**
>
> *Por qué:* los clientes piden y el servidor responde: comunicación **asimétrica** o **cliente-servidor**. En Moodle se aceptó `cliente-servidor`; "asimétrica" es el nombre de la categoría. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]
>
> ⚠️ *Fallada en el cuestionario de Moodle: repásala en el apunte.*

> [!question] P14 · Comunicación síncrona bloqueante
> ¿Cómo afecta el carácter bloqueante de la comunicación síncrona al comportamiento y rendimiento de un programa concurrente?
> - a. Maximiza el paralelismo del sistema al permitir que el emisor ejecute instrucciones en segundo plano sin detener su flujo de control.
> - b. Garantiza la eliminación total de deadlocks al forzar la recepción inmediata de cualquier mensaje.
> - c. Aumenta la eficiencia de red al comprimir automáticamente los datos antes de enviarlos de forma asíncrona.
> - d. Reduce el paralelismo potencial y puede introducir bloqueos, ya que el emisor debe suspender su ejecución hasta que el receptor recibe y/o procesa el mensaje.

> [!success]- Respuesta
>
> - d. ✅ Reduce el paralelismo potencial y puede introducir bloqueos, ya que el emisor debe suspender su ejecución hasta que el receptor recibe y/o procesa el mensaje.
>
> *Por qué:* el emisor **se queda parado** hasta que el receptor recibe o procesa: **menos paralelismo y riesgo de bloqueos**. No maximiza el paralelismo (eso es la asíncrona), no elimina deadlocks ni comprime datos. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P15 · Sincronización: memoria compartida vs. mensajes
> ¿Cuál es la diferencia fundamental en cuanto a la gestión de la sincronización entre el modelo de comunicación por memoria compartida y el modelo por paso de mensajes?
> - a. La memoria compartida elimina automáticamente los problemas de visibilidad de datos, mientras que el paso de mensajes exige el uso explícito de monitores en cada tarea transmisora.
> - b. En la memoria compartida la sincronización de acceso a los datos debe ser explícita para evitar condiciones de carrera, mientras que en el paso de mensajes la sincronización suele ser implícita en las operaciones de envío y recepción.
> - c. En el paso de mensajes es imprescindible implementar exclusión mutua mediante cerrojos de red, mientras que la memoria compartida no requiere sincronización alguna por ejecutarse dentro del mismo proceso.
> - d. En el paso de mensajes el emisor queda bloqueado obligatoriamente en memoria física hasta que el receptor borre la variable compartida.

> [!success]- Respuesta
>
> - b. ✅ En la memoria compartida la sincronización de acceso a los datos debe ser explícita para evitar condiciones de carrera, mientras que en el paso de mensajes la sincronización suele ser implícita en las operaciones de envío y recepción.
>
> *Por qué:* en memoria compartida la sincronización es **explícita**; en paso de mensajes suele ser **implícita**. La memoria compartida no resuelve la visibilidad sola, y en mensajes no hacen falta "cerrojos de red". [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P16 · `BlockingQueue`
> Si una aplicación Java utiliza la clase `BlockingQueue` para enviar y recibir datos entre hilos dentro de un mismo proceso, ¿qué mecanismo técnico de comunicación se está utilizando?
> - a. Invocación remota asimétrica desacoplada de la pila de ejecución de la JVM.
> - b. Paso de mensajes mediante un buffer de memoria compartido en la memoria principal del proceso.
> - c. Comunicaciones mediante sockets de red sobre la interfaz de red loopback.
> - d. Comunicación símplex no bloqueante respaldada por archivos en disco duro.

> [!success]- Respuesta
>
> - b. ✅ Paso de mensajes mediante un buffer de memoria compartido en la memoria principal del proceso.
>
> *Por qué:* es **paso de mensajes con un buffer en memoria compartida** del proceso (cola FIFO entre hilos). No hay sockets, ni ficheros en disco, ni invocación remota. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P17 · Asíncrona
> En la comunicación ______, el proceso emisor deposita el mensaje y continúa inmediatamente con su ejecución sin suspenderse ni esperar a que el receptor procese la información.

> [!success]- Respuesta
>
> - **asíncrona**
>
> *Por qué:* el emisor deposita el mensaje y sigue: comunicación **asíncrona** (como echar una carta al buzón). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P18 · Petición-respuesta
> El modelo de comunicación síncrono con respuesta utilizado en arquitecturas cliente-servidor y microservicios, donde el emisor se bloquea a la espera de un resultado tras enviar una petición, se conoce como ______.

> [!success]- Respuesta
>
> - **petición-respuesta**
>
> *Por qué:* síncrono y con respuesta, típico de cliente-servidor y RPC: **petición-respuesta** (o invocación remota). [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!question] P19 · Socket
> Mecanismo fundamental de comunicación en red que actúa como punto final para el intercambio de datos entre procesos en máquinas distintas a través de protocolos como TCP/IP o UDP: ______.

> [!success]- Respuesta
>
> - **socket**
>
> *Por qué:* el punto final de comunicación en red (TCP/UDP) es el **socket**. [[Guia examen temas 1 y 2#A.7 · Comunicación entre procesos|Ver Guía · A.7 Comunicación entre procesos]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 7
> P1 *memoria compartida* · P2 **c** · P3 *canal* · P4 **a** · P5 *simplex*  
> P6 *full duplex* · P7 **d** · P8 **a** · P9 **c** · P10 **d**  
> P11 **b** · P12 *emisor* · P13 *cliente-servidor* · P14 **d** · P15 **b**  
> P16 **b** · P17 *asíncrona* · P18 *petición-respuesta* · P19 *socket*  

---

### Simulacro 8 · 1.8 · Corrección en los programas concurrentes

> [!abstract] Simulacro 8
> **20 preguntas** · ⏱️ ~10 min · Fuente: [[Cuestionario 1-8]] · [[1.8 - Corrección en los programas concurrentes|Apuntes del 1.8]] · Tu nota en Moodle: **20/20**

> [!question] P1 · Inanición
> La ______ es la propiedad de viveza que se vulnera cuando a un proceso o hilo se le priva indefinidamente del acceso a un recurso necesario porque el planificador o sistema se lo concede sistemáticamente a otros.

> [!success]- Respuesta
>
> - **inanición**
>
> *Por qué:* que un proceso no consiga nunca el recurso porque siempre se lo dan a otros es **inanición** (*starvation*), un fallo de viveza. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inanición (starvation)|Guía · Inanición]]

> [!question] P2 · No apropiación
> La condición de Coffman denominada ______ establece que un recurso adquirido por un proceso solo puede ser liberado voluntariamente por él mismo una vez finalizada su tarea, sin que el sistema operativo pueda forzar su liberación.

> [!success]- Respuesta
>
> - **no apropiación**
>
> *Por qué:* si solo quien tiene el recurso puede soltarlo y el SO no puede quitárselo, es la condición de **no apropiación** (*no preemption*). [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]

> [!question] P3 · `acquire()` con el semáforo a 0
> Un semáforo contador se inicializa en 0. Si un hilo ejecuta la operación atómica `acquire()` sobre dicho semáforo, ¿cuál será el comportamiento del sistema?
> - a. El hilo detecta que el contador es 0, se bloquea y pasa a estado de espera hasta que otro hilo invoque `release()`.
> - b. Se genera de inmediato un error de ejecución del tipo `IllegalThreadStateException`.
> - c. El hilo decrementa automáticamente el valor del semáforo a -1 y continúa su ejecución de inmediato.
> - d. El semáforo se reinicia a su valor máximo permitido y despierta a todos los hilos del proceso.

> [!success]- Respuesta
>
> - a. ✅ El hilo detecta que el contador es 0, se bloquea y pasa a estado de espera hasta que otro hilo invoque `release()`.
>
> *Por qué:* con 0 permisos, `acquire()` **bloquea el hilo** hasta que otro haga `release()`. No baja a −1 para seguir, no lanza excepción y no reinicia el semáforo. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Mecanismos de exclusión mutua|Guía · Mecanismos de exclusión mutua]]

> [!question] P4 · Inversión de prioridad
> La ______ de prioridad ocurre cuando una tarea de baja prioridad bloquea un recurso necesitado por una tarea de alta prioridad, y a su vez una tarea de prioridad media desaloja a la de baja prioridad, retrasando a la de alta prioridad.

> [!success]- Respuesta
>
> - **inversión**
>
> *Por qué:* una tarea baja retiene el recurso, una media la desaloja y la alta espera: **inversión** de prioridad. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inversión de prioridad|Guía · Inversión de prioridad]]

> [!question] P5 · Causa de la inanición
> En un sistema de planificación por prioridades estáticas sin mecanismos de equidad, ¿qué situación conduce directamente a la inanición de una tarea de baja prioridad?
> - a. La adquisición de un monitor por parte de una tarea que completa su método y sale inmediatamente.
> - b. La creación de una dependencia de recursos en orden estricto descendente.
> - c. El uso de la herencia de prioridad entre tareas de baja y alta prioridad.
> - d. La presencia constante y continuada de tareas de mayor prioridad listas para ejecutarse.

> [!success]- Respuesta
>
> - d. ✅ La presencia constante y continuada de tareas de mayor prioridad listas para ejecutarse.
>
> *Por qué:* si **siempre hay tareas de más prioridad listas**, la baja no recibe nunca la CPU. La herencia de prioridad o el orden de recursos son soluciones, no causas. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inanición (starvation)|Guía · Inanición]]

> [!question] P6 · Monitor en Java
> En el lenguaje Java, ¿cómo se implementa el concepto de monitor para garantizar tanto la exclusión mutua implícita como la sincronización condicional?
> - a. Declarando todas las variables compartidas como `volatile` sin requerir métodos bloqueantes.
> - b. A través de la interfaz `Runnable` acoplada con bucles de espera activa sobre números enteros.
> - c. Utilizando exclusivamente la clase `Thread` y modificando su prioridad de forma dinámica.
> - d. Mediante la palabra clave `synchronized` para la exclusión mutua, combinada con los métodos `wait()`, `notify()` y `notifyAll()`.

> [!success]- Respuesta
>
> - d. ✅ Mediante la palabra clave `synchronized` para la exclusión mutua, combinada con los métodos `wait()`, `notify()` y `notifyAll()`.
>
> *Por qué:* **`synchronized`** da la exclusión mutua y **`wait()`/`notify()`/`notifyAll()`** la sincronización condicional. `volatile` solo da visibilidad; `Runnable` y las prioridades de `Thread` no son monitores. [[1.6 - Sincronizacion#6. Monitor|Ver 1.6 · Monitor]]

> [!question] P7 · Romper la espera circular
> Para evitar la condición de Coffman de 'espera circular' en la gestión de múltiples recursos compartidos, ¿cuál es la técnica de prevención más habitual?
> - a. Asignar siempre prioridades dinámicas basadas únicamente en la velocidad de la CPU.
> - b. Eliminar la exclusión mutua de todos los dispositivos de hardware del sistema.
> - c. Permitir que los procesos mantengan bloqueados los recursos indefinidamente mediante un bucle activo.
> - d. Establecer un orden jerárquico o numérico consistente para la adquisición de recursos en todas las tareas.

> [!success]- Respuesta
>
> - d. ✅ Establecer un orden jerárquico o numérico consistente para la adquisición de recursos en todas las tareas.
>
> *Por qué:* imponer un **orden global de adquisición** (siempre A antes que B) impide los ciclos. Eliminar la exclusión mutua no es viable y retener recursos en bucle empeora el problema. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]

> [!question] P8 · Fairness contra la inanición
> ¿De qué manera el concepto de 'fairness' (justicia o equidad) contribuye a evitar el problema de la inanición en los algoritmos de sincronización y planificación?
> - a. Elimina por completo el uso de cerrojos de exclusión mutua en variables compartidas.
> - b. Otorga siempre preferencia absoluta a las tareas de mayor prioridad para maximizar el rendimiento.
> - c. Garantiza que se tenga en cuenta la antigüedad de las solicitudes para otorgar el recurso a todos los procesos eventualmente.
> - d. fuerza a todos los hilos a ejecutarse en un orden estrictamente al azar.

> [!success]- Respuesta
>
> - c. ✅ Garantiza que se tenga en cuenta la antigüedad de las solicitudes para otorgar el recurso a todos los procesos eventualmente.
>
> *Por qué:* la equidad **tiene en cuenta la antigüedad de las peticiones**, así que todos acaban recibiendo el recurso. Dar siempre preferencia a la máxima prioridad produce justo la inanición; el azar no garantiza nada. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inanición (starvation)|Guía · Inanición]]

> [!question] P9 · Tareas A, B y C sin solución
> Considere tres tareas: Tarea A (alta prioridad), Tarea B (media prioridad) y Tarea C (baja prioridad). Tarea C retiene un cerrojo que Tarea A necesita, por lo que Tarea A se bloquea. Luego, Tarea B pasa a estar lista para ejecutarse. Si NO se aplica ningún mecanismo de solución, ¿qué sucede a continuación?
> - a. Tarea B se ejecuta desplazando a Tarea C; Tarea A queda indirectamente bloqueada por Tarea B hasta que B y C terminen.
> - b. Tarea A desaloja inmediatamente a Tarea B y fuerza a Tarea C a liberar el recurso.
> - c. Tarea C eleva automáticamente su prioridad por encima de B sin requerir ningún algoritmo especial.
> - d. El sistema operativo aborta Tarea B por intentar acceder a una sección crítica ajena.

> [!success]- Respuesta
>
> - a. ✅ Tarea B se ejecuta desplazando a Tarea C; Tarea A queda indirectamente bloqueada por Tarea B hasta que B y C terminen.
>
> *Por qué:* B (media) desaloja a C (baja), que no puede soltar el cerrojo; A (alta) queda **bloqueada indirectamente por B**. Sin herencia de prioridad, C no sube sola y el SO no aborta a B. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inversión de prioridad|Guía · Inversión de prioridad]]

> [!question] P10 · Herencia de prioridad
> La ______ de prioridad es un mecanismo mediante el cual un hilo de baja prioridad sube temporalmente su nivel de prioridad para coincidir con la de un hilo de alta prioridad que está esperando por un recurso que el primero retiene.

> [!success]- Respuesta
>
> - **herencia**
>
> *Por qué:* el hilo bajo que retiene el recurso **sube temporalmente** a la prioridad del alto que espera: **herencia** de prioridad. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inversión de prioridad|Guía · Inversión de prioridad]]

> [!question] P11 · Exclusión mutua
> La ______ es la propiedad de seguridad fundamental que garantiza que el acceso a recursos compartidos o secciones críticas sea realizado por una sola tarea a la vez para evitar condiciones de carrera.

> [!success]- Respuesta
>
> - **exclusión mutua**
>
> *Por qué:* la propiedad de seguridad que deja entrar a una sola tarea en la sección crítica es la **exclusión mutua**. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Mecanismos de exclusión mutua|Guía · Mecanismos de exclusión mutua]]

> [!question] P12 · Timeout y liberar cerrojos
> Un algoritmo de gestión de recursos asigna un tiempo máximo de espera a las solicitudes de cerrojos. Si una tarea no obtiene el recurso en ese tiempo, suelta los cerrojos que ya tenía y reintenta más tarde. ¿Qué condición de Coffman está atacando directamente para evitar deadlocks?
> - a. Exclusión mutua.
> - b. Retención y espera (Hold and Wait).
> - c. Inversión de prioridad.
> - d. No apropiación.

> [!success]- Respuesta
>
> - b. ✅ Retención y espera (Hold and Wait).
>
> *Por qué:* al soltar lo que tenía si no consigue el resto, la tarea deja de **retener mientras espera**: rompe *hold and wait*. No toca la exclusión mutua; la no apropiación se rompería si el **sistema** le quitara los recursos; la inversión de prioridad no es una condición de Coffman. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]

> [!question] P13 · 5 instancias idénticas
> Un sistema concurrente debe gestionar el acceso a un recurso compartido del cual existen exactamente 5 instancias idénticas disponibles simultáneamente. ¿Qué primitiva de sincronización es la más adecuada para controlar este acceso?
> - a. Una variable booleana consultada mediante un bucle de espera activa.
> - b. Un mutex binario, configurado para alternar entre 5 estados de desbloqueo.
> - c. Un monitor sin variables de condición.
> - d. Un semáforo general o contador, inicializado con el valor 5.

> [!success]- Respuesta
>
> - d. ✅ Un semáforo general o contador, inicializado con el valor 5.
>
> *Por qué:* un **semáforo contador iniciado a 5** controla exactamente 5 accesos simultáneos. Un mutex es binario y la espera activa sobre un booleano gasta CPU y no cuenta instancias. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Mecanismos de exclusión mutua|Guía · Mecanismos de exclusión mutua]]

> [!question] P14 · Seguridad vs. viveza
> En el contexto de los programas concurrentes, ¿cuál es la diferencia fundamental en la naturaleza de lo que garantizan las propiedades de seguridad frente a las propiedades de viveza?
> - a. Las propiedades de seguridad especifican 'lo que no debe ocurrir' para evitar estados incorrectos, mientras que las de viveza especifican 'lo que debe ocurrir' para garantizar el progreso.
> - b. Las propiedades de seguridad dependen de las políticas del planificador del sistema operativo, mientras que las de viveza dependen exclusivamente de cerrojos binarios.
> - c. Las propiedades de seguridad aplican únicamente a sistemas distribuidos, mientras que las de viveza aplican a la programación multihilo local.
> - d. Las propiedades de seguridad garantizan la velocidad de ejecución, mientras que las de viveza previenen condiciones de carrera en variables globales.

> [!success]- Respuesta
>
> - a. ✅ Las propiedades de seguridad especifican 'lo que no debe ocurrir' para evitar estados incorrectos, mientras que las de viveza especifican 'lo que debe ocurrir' para garantizar el progreso.
>
> *Por qué:* seguridad = **lo que no debe pasar** (estados incorrectos); viveza = **lo que debe pasar** (progreso). No van de velocidad, ni se reparten entre local y distribuido. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#A.8 · Corrección en los programas concurrentes|Guía · A.8 Corrección]]

> [!question] P15 · Interbloqueo pasivo
> El ______ pasivo es una situación en la que dos o más procesos se encuentran suspendidos indefinidamente esperando mutuamente la liberación de recursos retenidos por los demás.

> [!success]- Respuesta
>
> - **interbloqueo**
>
> *Por qué:* procesos **suspendidos** esperando mutuamente recursos de los otros: **interbloqueo** pasivo (*deadlock*, "abrazo mortal"). [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]

> [!question] P16 · Bloqueo activo
> El ______ es una situación de falta de viveza en la que varios procesos se encuentran en ejecución activa y cambiando de estado en un bucle continuo de reintentos, pero sin realizar ningún progreso efectivo.

> [!success]- Respuesta
>
> - **bloqueo activo**
>
> *Por qué:* procesos **activos**, reintentando y cambiando de estado sin avanzar: **bloqueo activo** (*livelock*). [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Livelock (interbloqueo activo)|Guía · Livelock]]

> [!question] P17 · Soltar la exclusión mutua al esperar
> Cuando un hilo se encuentra dentro de una sección crítica protegida por exclusión mutua y necesita esperar a que se cumpla una condición de sincronización, ¿por qué debe liberar el mecanismo de exclusión mutua mientras espera?
> - a. Para que el planificador de la máquina virtual aumente inmediatamente la prioridad de la tarea en espera.
> - b. Para evitar un interbloqueo pasivo (deadlock), permitiendo que otros hilos accedan al recurso y puedan hacer cumplir la condición requerida.
> - c. Para evitar que el semáforo contador tome valores negativos no permitidos.
> - d. Para transformar la comunicación síncrona en un canal símplex de mayor velocidad.

> [!success]- Respuesta
>
> - b. ✅ Para evitar un interbloqueo pasivo (deadlock), permitiendo que otros hilos accedan al recurso y puedan hacer cumplir la condición requerida.
>
> *Por qué:* si espera con el cerrojo cogido, nadie puede entrar a cumplir la condición: **deadlock**. Soltarlo no sube la prioridad ni tiene que ver con semáforos negativos o canales símplex. [[1.6 - Sincronizacion#5. Condición de sincronización|Ver 1.6 · Condición de sincronización]]

> [!question] P18 · Cómo resuelve la herencia la inversión
> ¿De qué manera la 'herencia de prioridad' resuelve el problema de la inversión de prioridad?
> - a. Asigna el recurso solicitado a la tarea de mayor prioridad eliminando el progreso realizado por la de baja prioridad.
> - b. Disminuye la prioridad de la tarea de prioridad media a cero hasta que la tarea de alta prioridad finalice.
> - c. Obliga a la tarea de alta prioridad a ejecutar su sección crítica sin adquirir el cerrojo de exclusión mutua.
> - d. Hace que la tarea de baja prioridad que retiene el recurso herede temporalmente la prioridad de la tarea de alta prioridad que está bloqueada.

> [!success]- Respuesta
>
> - d. ✅ Hace que la tarea de baja prioridad que retiene el recurso herede temporalmente la prioridad de la tarea de alta prioridad que está bloqueada.
>
> *Por qué:* la tarea baja **hereda temporalmente la prioridad de la alta**, así que la media no puede desalojarla y suelta el recurso antes. No quita el recurso, no baja a la media a 0 ni se salta el cerrojo. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Inversión de prioridad|Guía · Inversión de prioridad]]

> [!question] P19 · Romper hold and wait
> Se desea prevenir la aparición de deadlocks eliminando la condición de Coffman conocida como 'retención y espera' (Hold and Wait). ¿Qué estrategia de diseño permite romper esta condición?
> - a. Obligar a que cada proceso solicite y obtenga todos los recursos que necesita de una sola vez antes de iniciar su ejecución.
> - b. Permitir que el sistema operativo expropie o quite forzosamente recursos a cualquier proceso bloqueado.
> - c. Garantizar que todos los recursos compartidos sean leídos de forma asíncrona sin exclusión mutua.
> - d. Establecer una jerarquía global u ordenamiento numérico estricto en la adquisición de recursos.

> [!success]- Respuesta
>
> - a. ✅ Obligar a que cada proceso solicite y obtenga todos los recursos que necesita de una sola vez antes de iniciar su ejecución.
>
> *Por qué:* **pedir todos los recursos de una vez** antes de empezar: así nunca se retiene uno mientras se espera otro. Que el SO quite recursos rompe la no apropiación; el orden global rompe la espera circular. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Deadlock (interbloqueo pasivo)|Guía · Deadlock]]

> [!question] P20 · Dos hilos al 100 % sin avanzar
> Al analizar una aplicación concurrente, se detecta que dos hilos están consumiendo el 100% del procesador cambiando constantemente el valor de sus variables, pero sin lograr avanzar en el procesamiento de sus datos. ¿Qué problema presenta la aplicación?
> - a. Violación del principio de exclusión mutua.
> - b. Interbloqueo pasivo (deadlock).
> - c. Inversión de prioridad no gestionada.
> - d. Interbloqueo activo (livelock).

> [!success]- Respuesta
>
> - d. ✅ Interbloqueo activo (livelock).
>
> *Por qué:* activos, cambiando de estado y sin progreso: **livelock**. En un deadlock los hilos estarían **suspendidos**, sin gastar CPU. [[1.8 - Corrección en los programas concurrentes|Ver 1.8]] · [[Guia examen temas 1 y 2#Livelock (interbloqueo activo)|Guía · Livelock]]

> [!abstract]- 📝 Hoja de respuestas · Simulacro 8
> P1 *inanición* · P2 *no apropiación* · P3 **a** · P4 *inversión* · P5 **d**  
> P6 **d** · P7 **d** · P8 **c** · P9 **a** · P10 *herencia*  
> P11 *exclusión mutua* · P12 **b** · P13 **d** · P14 **a** · P15 *interbloqueo*  
> P16 *bloqueo activo* · P17 **b** · P18 **d** · P19 **a** · P20 **d**  

---

## Registro de resultados

Apunta la nota de cada intento (aciertos / total) para ver qué apartados necesitan otra vuelta.

| Simulacro | Preguntas | Intento 1 | Intento 2 | Intento 3 |
| --- | --- | --- | --- | --- |
| 1 · Programa vs. proceso | 40 | | | |
| 2 · Computación concurrente | 20 | | | |
| 3 · Procesos en el sistema operativo | 16 | | | |
| 4 · Técnicas de programación concurrente | 20 | | | |
| 5 · Orden de ejecución | 19 | | | |
| 6 · Sincronización | 20 | | | |
| 7 · Comunicación entre procesos | 19 | | | |
| 8 · Corrección en los programas concurrentes | 20 | | | |

## Esquema de repaso

| Simulacro | Ideas que más se preguntan |
| --- | --- |
| 1 · Programa vs. proceso | Programa **estático** / proceso **dinámico**; ejecutable binario vs. interpretado (bytecode, intérprete); permiso `+x` en Unix; demonio = servicio, en segundo plano y cargado en el arranque |
| 2 · Computación concurrente | Concurrencia ≠ paralelismo (≥ 2 núcleos); multiprogramación + cambio de contexto = sobrecarga; SMP vs. AMP; memoria común (multiprocesamiento) vs. local (distribuido, cluster) |
| 3 · Procesos en el SO | Segmentos código/datos/pila/heap; PCB y contador de programa; estados y transiciones (asignación, apropiación); zombi; RR y colas multinivel; scheduler decide, dispatcher ejecuta |
| 4 · Técnicas | Concurrente vs. paralela vs. distribuida; procesos independientes, competidores (exclusión mutua) y cooperantes (productor-consumidor, pipes) |
| 5 · Orden de ejecución | Orden total vs. parcial; race condition (depende del *timing*) ⊃ data race (misma variable + ≥ 1 escritura + sin sincronizar); comportamiento errático |
| 6 · Sincronización | Acceso a datos vs. control; Bernstein (L∩E, E∩L, E∩E = ∅); LOAD/ADD/STORE; `volatile` = visibilidad, no atomicidad; `wait()` libera el cerrojo; `IllegalMonitorStateException` |
| 7 · Comunicación | Emisor, receptor, mensaje, canal; símplex / half / full duplex; síncrona vs. asíncrona; simétrica (P2P) vs. asimétrica (cliente-servidor); memoria compartida vs. paso de mensajes |
| 8 · Corrección | Seguridad (lo que no debe pasar) vs. viveza (lo que debe pasar); 4 condiciones de Coffman y cómo romperlas; deadlock vs. livelock; inanición y *fairness*; inversión y herencia de prioridad; semáforo contador |

## Relaciones

- [[Cuestionario 1-1]] · [[Cuestionario 1-2]] · [[Cuestionario 1-3]] · [[Cuestionario 1-4]] · [[Cuestionario 1-5]] · [[Cuestionario 1-6]] · [[Cuestionario 1-7]] · [[Cuestionario 1-8]] — cuestionarios originales del aula
- [[1.1 - Programa vs. Proceso]] · [[1.2 - Computacion concurrente]] · [[1.3 - Procesos en el sistema operativo]] · [[1.4 - Tecnicas de programacion concurrente]] · [[1.5 - Orden de ejecucion]] · [[1.6 - Sincronizacion]] · [[1.8 - Corrección en los programas concurrentes]] — apuntes del Tema 1
- [[1.R - Preguntas del Tema 1]] · [[1.R2 - Preguntas del Tema 1 (II)]] — repaso con preguntas cortas

## Para repasar

- [ ] Hacer los 8 simulacros sin abrir las respuestas.
- [ ] Repetir las preguntas ⚠️ que fallaste en Moodle.
- [ ] Repetir cualquier simulacro con menos de un 80 % de aciertos.
- [ ] Repasar en el apunte enlazado cada pregunta fallada.

## Guía relacionada

- [[Guia examen temas 1 y 2|🧠 Guía de teoría y chuleta]]
- [[Test de repaso temas 1 y 2|✅ Test de repaso temas 1 y 2]]
- [[Practicos temas 1 y 2|💻 Prácticos temas 1 y 2]]

┌───────────────────────────────────────────┬──────────────────────────┬──────────────────┐
│                  Patrón                   │           Dato           │ Lo esperable por │
│                                           │                          │       azar       │
├───────────────────────────────────────────┼──────────────────────────┼──────────────────┤
│                                           │ a 33 · b 29 · c 32 · d   │ equilibrado → no │
│ Letra de la respuesta                     │ 34, sin secuencias       │  hay patrón      │
│                                           │ repetidas                │                  │
├───────────────────────────────────────────┼──────────────────────────┼──────────────────┤
│ La correcta es la opción más larga        │ 86 / 128 (67 %)          │ 25 %             │
├───────────────────────────────────────────┼──────────────────────────┼──────────────────┤
│ Palabras absolutas (siempre,              │ 6 % de las correctas     │                  │
│ exclusivamente, obligatoriamente,         │ frente al 33 % de las    │ —                │
│ únicamente, automáticamente…)             │ incorrectas              │                  │
├───────────────────────────────────────────┼──────────────────────────┼──────────────────┤
│ La correcta repite más palabras del       │ 95 / 128 (74 %)          │ ~25 %            │
│ enunciado                                 │                          │                  │
├───────────────────────────────────────────┼──────────────────────────┼──────────────────┤
│ Opciones de relleno absurdas (la RAM      │ en casi todas las        │ —                │
│ borra variables, se reinicia la placa…)   │ preguntas                │                  │
└───────────────────────────────────────────┴──────────────────────────┴──────────────────┘