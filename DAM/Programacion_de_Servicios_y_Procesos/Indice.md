---
asignatura: PSyP
tipo: indice
curso: 2026-27
tags:
  - DAM/indice
---

# Programación de Servicios y Procesos — Índice

> [!tip] Preparación de examen (Temas 1 y 2)
> - 🐣 [[1.1 Explicacion desde cero (T1-T2)|Explicación desde cero]] — empieza aquí: Tema 1 y Tema 2 con analogías y palabras de los huecos (test del jueves), Tema 2 paso a paso y recetario para completar funciones.
> - 📝 [[3.2 Simulacro examen practico (T2)]] — simulacro del práctico (1 h, 24 huecos + 12 líneas completas) · [[3.3 Simulacro examen practico (T2) - Soluciones|soluciones]]
> - 🧠 [[1.2 Guia y chuleta (T1-T2)|Teoría y chuleta]] — conceptos, tablas comparativas y resumen final.
> - ✅ [[2.1 Repaso general - 55 preguntas (T1-T2)]] — 55 preguntas tipo test con solución razonada.
> - ⏱️ [[2.2 Simulacros por apartado (T1)]] — 8 simulacros (174 preguntas de los cuestionarios Moodle, uno por apartado) con hoja de respuestas.
> - 📝 [[2.4 Examen completo - 50 preguntas (T1)]] — examen completo de 50 preguntas con opciones barajadas y patrones de respuesta detectados.
> - ⏱️ [[2.3 Simulacros por apartado (T2)]] — 5 simulacros (las 149 preguntas reales de los cuestionarios 2-1 … 2-5, uno por apartado) con hoja de respuestas.
> - 📝 [[2.5 Examen completo - 40 preguntas (T2)]] — examen tipo test del Tema 2 (30 de test + 10 de hueco de los cuestionarios 2-1 … 2-5), con nota con y sin penalización.
> - 💻 [[3.1 Ejercicios resueltos (T1-T2)]] — ejercicios resueltos y explicados (huecos de código).

# Procesos e Hilos

- 1 - Program. concurrente
	- [Intro 1]
    - [[1.1 - Programa vs. Proceso]] ✅
    - [[1.2 - Computacion concurrente]] ✅
    - [[1.3 - Procesos en el sistema operativo]] ✅
    - [[1.4 - Tecnicas de programacion concurrente]] ✅
    - [[1.C - Cuestionario Apartado 1.1]] ✅ 38/40 (auto-test)
    - [[1.5 - Orden de ejecucion]] ✅
    - [[1.6 - Sincronizacion]] ✅
    - [[1.R - Preguntas del Tema 1]] ✅ (repaso 14 preguntas)
    - [[1.R2 - Preguntas del Tema 1 (II)]] ✅ (repaso 13 preguntas)
    - [[1.7 - Comunicación]] ✅
    - [1.8 - Propiedades de corrección]
    
- 2 - Gestión de procesos
    - [Intro 2]
    - [[2.Repaso - Ejercicio filtro con subproceso]] ✅
    - [[2.Repaso - Listar archivos con Runtime]] ✅
    - [[2.1 - Instalación y configuracion de java]] ✅
    - [[2.2 - Gestión de subprocesos]] ✅
    - [[2.3 - Flujos de comunicación]] ✅
    - [[2.4 - Finalización de subprocesos]] ✅
    - [[2.5 - Información sobre procesos]] ✅
    - [[2.E - Ejercicio filtro con subproceso]] ✅
    - [[2.E2 - Listar archivos con Runtime]] ✅
    - [[2.E3 - Diccionario con subprocesos]] ✅
    - [[2.E4 - Invertir líneas con subproceso]] ✅
    
- 3 - Gestión de hilos
    - [Intro 3]
    - [3.1 - Introducción]
    - [3.2 - Thread]
    - [3.3 - Runnable]
    - [3.4 - Prioridad]
    - [3.5 - Interrumpir]
    - [3.6 - Dormir]
    - [3.7 - Esperar la finalización]
    - [3.8 - Daemons]
    - [3.9 - UncaughtExceptionHandler]
    - [3.10 - ThreadGroup]
    - [3.11 - ThreadFactory]
    - [3.12 - ThreadLocal]
    
- 4 - Cerrojos
    - [Intro 4]
    - [4.1 - Introducción a los sincronizadores]
    - [4.2 - Volatile]
    - [4.3 - Cerrojo intrínseco]
    - [4.4 - Lock striping]
    - [4.5 - Spin waiting]
    - [4.6 - Wait notify]
    - [4.7 - Lock]
    - [4.8 - Condition]
    - [4.9 - ReentrantReadWriteLock]
    - [4.10 - StampedLock]
    - [4.11 - Semaphore]
    - [4.12 - Caso de estudio - La cena de los filósofos]
    
- 5 - Barreras
    - [Intro 5]
    - [5.1 - Barreras de sincronización]
    - [5.2 - CountDownLatch]
    - [5.3 - CyclicBarrier]
    - [5.4 - Phaser]
    - [5.5 - Exchanger]
    
- 6 - Variables atómicas
    - [Intro 6]
    - [6.1 - Paquete atomic]
    - [6.2 - Variables atómicas]
    - [6.3 - Acumuladores atómicos]
    - [6.4 - VarHandle]
    
- 7 - Colecciones thread-safe
    - [Intro 7]
    - [7.1 - Tipos de colecciones thread-safe]
    - [7.2 - Unmodifiable collections]
    - [7.3 - Copy on write collections]
    - [7.4 - Inmutable collections]
    - [7.5 - Synchronized collections]
    - [7.6 - Concurrent-aware collections]
    - [7.7 - Concurrent-aware collections que usan cerrojos]
    - [7.8 - Lock-free concurrent-aware collections]
    
- 8 - Executor framework
    - [Intro 8]
    - [8.1 - Introducción al executor framework]
    - [8.2 - Executor]
    - [8.3 - ThreadPoolExecutor]
    - [8.4 - Terminación de un ejecutor]
    - [8.5 - CachedThreadPool]
    - [8.6 - FixedThreadPool]
    - [8.7 - Callable]
    - [8.8 - Future]
    - [8.9 - Métodos de envío de tareas en la interfaz ExecutorService]
    - [8.10 - invokeAll()]
    - [8.11 - invokeAny()]
    - [8.12 - ThreadFactory]
    - [8.13 - RejectedExecutionHandler]
    - [8.14 - ScheduledThreadPoolExecutor]
    - [8.15 - Planificación del inicio de ejecución de una tarea]
    - [8.16 - Ejecutar una tarea de manera periódica]
    - [8.17 - Cancelación de tareas y terminación del ScheduledThreadPoolExecutor]
    - [8.18 - FutureTask]
    - [8.19 - ExecutorCompletionService]
    
- 9 - Fork-Join framework
    - [Intro 9]
    - [9.1 - Introducción al Fork-Join framework]
    - [9.2 - ForkJoinPool]
    - [9.3 - ForkJoinTask]
    - [9.4 - Algoritmo de robo de trabajo]
    - [9.5 - RecursiveAction]
    - [9.6 - RecursiveTask]
    - [9.7 - Common Fork-Join pool]
    
- 10 - CompletableFuture
    - [Intro 10]
    - [10.1 - Introducción a CompletableFuture]
    - [10.2 - Nomenclatura de los métodos]
    - [10.3 - Métodos factoría]
    - [10.4 - Obtención del valor]
    - [10.5 - Ejecutar un runnable asíncronamente]
    - [10.6 - Consumir el resultado asíncronamente]
    - [10.7 - Transformar el resultado asíncronamente]
    - [10.8 - Gestión de excepciones]
    - [10.9 - Completado explícito]
    - [10.10 - Trabajo con más de dos CompletableFuture]
    
- 11 - Hilos virtuales y concurrencia estructurada
    - [Intro 11]
    - [11.1 - Hilos virtuales]
    - [11.2 - Concurrencia estructurada]

---

# Networking


- 12 - Sockets
    - [Intro] 
    - [12.1 - Arquitectura Cliente Servidor]
    - [12.2 - TCP/IP]
    - [12.3 - InetAddress y NetworkInterface]
    - [12.4 - Concepto de socket]
    - [12.5 - Sockets orientados a conexión]
    - [12.6 - Sockets no orientados a conexión]
    
- 13 - HTTP
    - [Intro]
    - [13.1 - URI]
    - [13.2 - URL]
    - [13.3 - URLEncoder y URLDecoder]
    - [13.4 - UrlConnection]
    - [13.5 - Protocolo HTTP]
    - [13.6 - Arquitectura REST]
    - [13.7 - HttpURLConnection]
    - [13.8 - OkHttp]
    - [13.9 - HttpClient]
    - [13.10 - Retrofit]
    
- 14 - Otros protocolos de la capa de aplicación
    - [14.1 - FTP]
    - [14.2 - Mail]
    
- 19 - APIs REST con Spring boot
    - [19.1 - Spring]
    - [19.2 - Spring IoC]
    - [19.3 - Definición de entidades JPA]
    - [19.4 - Definición de un rest controller y consulta de entidades]
    - [19.5 - Consulta de una entidad a partir de su id]
    - [19.6 - Respuesta de error por defecto]
    - [19.7 - Eliminar una entidad]
    - [19.8 - Actualizar una entidad]
    - [19.9 - Agregar una entidad]
    - [19.10 - Request params]
    - [19.11 - Necesidad de validación]
    - [19.12 - Paginación]
    - [19.13 - Relaciones entre entidades]
    - [19.14 - Documentación de APIs REST con OpenAPI 3 y Swagger]
    - [19.15 - CORS (Cross-Origin Resource Sharing)]
    - [19.16 - Niveles de madurez de Richardson]
    - [19.17 - Nesecidad de securizar nuestra API Rest]
    - [19.18 - JWT]

---

# Programación Segura


15 - Criptografía
- [Intro]
- [15.1 - Objetivos de seguridad]
- [15.2 - Definición de criptografía]
- [15.3 - Tipos de algoritmos y de cifradores]
- [15.4 - JCA y JCE]
- [15.5 - Proveedores y motores criptográficos]
- [15.6 - Claves criptográficas]
- [15.7 - Funciones hash]
- [15.8 - Algoritmos de criptografía simétrica]
- [15.9 - MAC y HMAC]
- [15.10 - Algoritmos de criptografía asimétrica]
- [15.11 - Claves de sesión]
- [15.12 - Firma digital]
- [15.13 - Certificado digital]
- [15.14 - Encriptar y desencriptar flujos de datos]
- [15.15 - Herramienta keytool y almacén de claves]
- [15.16 - Firma de archivos jar]
- [15.17 - TLS/SSL y SSH]
- [15.18 - Sockets seguros]
- [15.19 - Herramienta OpenSSL]