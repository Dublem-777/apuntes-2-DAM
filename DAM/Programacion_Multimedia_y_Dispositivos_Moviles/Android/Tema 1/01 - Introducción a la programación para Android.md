---
asignatura: Optativa
tema: 1
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-introduccion
---

# 1 · Introducción a la programación para Android

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 1 · Android (vistas)
> Tema siguiente: [[02 - Creación de un proyecto]]

> [!info] Material de referencia
> [Introducción a la programación para Android](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a01%20-%20Introduccion%20a%20la%20programacion%20para%20Android/)

## Índice del tema

- [[#1. ¿Qué es Android?]]
- [[#2. Historia]]
- [[#3. Versiones y distribución de uso]]
- [[#4. Entorno de desarrollo]]
- [[#5. Android Studio]]
- [[#6. Emulador]]
- [[#7. Intel x86 Emulator Accelerator (HAXM)]]
- [[#8. Ejecución en dispositivo físico]]

---

## 1. ¿Qué es Android?

Android es un **sistema operativo móvil** basado en **Linux**, diseñado para ser utilizado en dispositivos móviles como teléfonos inteligentes (_smart phones_), tabletas (_tablets_), televisiones (Google TV), relojes de pulsera (_smart watches_) y otros dispositivos.

Acompañando al núcleo Linux del sistema operativo, Android incorpora una serie de capas de software (_middleware_) que hacen de intermediarias entre el núcleo y otras aplicaciones, hardware, redes, etc, aportando distintas funcionalidades al dispositivo físico.

Al contrario que el sistema operativo para dispositivos móviles iOS de Apple, Android se desarrolla de forma abierta y se puede acceder a su código fuente.

El que se tenga acceso al código fuente no significa que se pueda tener siempre la última versión de Android en un determinado móvil, ya que el código para soportar el hardware (controladores) de cada fabricante normalmente no es público, por lo que no dispondríamos del _firmware_ para poder hacerlo funcionar en dicho terminal.

Por otro lado, las nuevas versiones de Android suelen requerir más recursos, por lo que los modelos de dispositivos más antiguos pueden quedar descartados por razones de memoria (RAM), velocidad de procesador, etc.

Las aplicaciones Android se desarrollan habitualmente en los lenguajes de programación Java o Kotlin, haciendo uso del Android Software Development Kit (Android SDK), el _kit_ de desarrollo de software proporcionado por Google, y cuya descarga es gratuita.

También tenemos disponible un _kit_ de desarrollo nativo para aplicaciones o extensiones en C o C++, aunque sólo se usa en casos muy específicos.

Google ha desarrollado su propia tienda online de aplicaciones para dispositivos Android, denominada **Google Play**. Esta web permite a los usuarios navegar y adquir aplicaciones publicadas por los desarrolladores, ya sean de pago o gratuitas, de manera que Google retribuye a los desarrolladores con un porcentaje del precio de las aplicaciones.

Por otra parte, los usuarios pueden instalar aplicaciones desde otras tiendas virtuales (tales como Amazon Appstore) o directamente en el dispositivo, si se dispone del archivo APK (paquete de instalación) de la aplicación.

Un archivo con extensión **.apk** es un paquete para el sistema operativo Android. Este formato es una variante del formato JAR de Java y se usa para distribuir e instalar componentes empaquetados para la plataforma Android para smartphones y tablets.

> [!example] 🎬 Vídeo
> [Explicación en video](https://www.youtube.com/watch?v=SkCbDKI18Rc)

## 2. Historia

El nombre Android (androide en castellano) hace referencia a la novela de Philip K. Dick llamada "¿Sueñan los androides con ovejas eléctricas?", que posteriormente fue adaptada al cine en la película "Blade Runner".

En julio de 2005, Google adquirió Android Inc., una pequeña compañía de Palo Alto, California fundada en 2003. Entre los cofundadores de Android que se fueron a trabajar a Google están Andy Rubin, Rich Miner, Nick Sears, y Chris White.

En Google, el equipo liderado por Rubin desarrolló una plataforma para dispositivos móviles basada en el kernel de Linux, que fue promocionado a fabricantes de dispositivos y operadores con la promesa de proveer un sistema flexible y actualizable. Google pretendía crear una alianza con fabricantes de hardware y software para que cooperaran entre sí en el desarrollo de dispositivos móviles.

El 5 de noviembre de 2007 la **Open Handset Alliance** (**OHA**, Alianza de Dispositivos móviles Abiertos), un consorcio de varias compañías, vio la luz con el fin de desarrollar estándares abiertos para dispositivos móviles.

El primer producto de la OHA fue Android, una plataforma para dispositivos móviles construida sobre la versión 2.6 del kernel de Linux.

El primer teléfono disponible en el mercado para ejecutar Android fue el HTC Dream, dado a conocer al público el 22 de octubre de 2008.

A principios de 2010 Google colaboró con HTC para lanzar su producto estrella en dispositivos Android, el Nexus One (cuyo nombre es un guiño a la película Blade Runner), como primer dispositivo Android "puro".

> [!info] Web oficial para desarrolladores Android
> La web oficial para desarrolladores Android es [https://developer.android.com/index.html](https://developer.android.com/index.html), en la que podemos encontrar toda la documentación oficial.

## 3. Versiones y distribución de uso

Android ha visto numerosas actualizaciones desde su liberación inicial. Estas actualizaciones al sistema operativo base típicamente arreglan bugs y agregan nuevas funciones. Generalmente cada actualización del sistema operativo Android es desarrollada bajo un nombre en código de un elemento relacionado con postres o dulces. En cada versión el postre elegido empieza por una letra distinta siguiendo el orden alfabético.

A continuación se muestran todas las versiones, con su nombre, su número de API y su fecha de liberación.

**Versiones de Android**

|Versión|Nombre|nº API|Fecha|
|---|---|---|---|
|1.0|Apple pie (pastel de manzana)|1|09/2008|
|1.1|Banana bread (pan de plátano)|2|02/2009|
|1.5|Cupcake (magdalena glaseada)|3|04/2009|
|1.6|Donut (rosquilla)|4|09/2009|
|2.0|Eclair (pepito o bilbaino)|5|10/2009|
|2.0.1|Eclair 0.1|6|12/2009|
|2.1|Eclair MR1|7|01/2010|
|2.2|Froyo (frozen yogurt, yogur helado)|8|05/2010|
|2.3|Gingerbread (pan de jengibre)|9|12/2010|
|2.3.3|Gingerbread MR1|10|02/2011|
|3.0|Honeycomb (panal de miel)|11|02/2011|
|3.1|Honeycomb MR1|12|05/2011|
|3.2|Honeycomb MR2|13|07/2011|
|4.0|Ice cream sandwich, ICS (sandwich de helado)|14|10/2011|
|4.0.3|ICS MR1|15|12/2011|
|4.1|Jelly Bean (gragea)|16|07/2012|
|4.2|Jelly Bean MR1|17|10/2012|
|4.3|Jelly Bean MR2|18|07/2013|
|4.4|KitKat (barrita de chocolate)|19|10/2013|
|L|Android L Preview|20|06/2014|
|5.0|Lollypop (piruleta)|21|11/2014|
|5.1|Lollipop MR1|22|03/2015|
|6.0|Marshmellow (nube, esponjita)|23|10/2015|
|7.0|Nougat (turrón)|24|08/2016|
|7.1|Nougat|25|12/2016|
|8|Oreo (galleta)|26|08/2017|
|8.1|Oreo|27|12/2017|
|9|Pie (pastel)|28|08/2018|
|10|Android 10 (Quince Tart)|29|09/2019|
|11|Android 11 (Red Velvet Cake)|30|09/2020|
|12|Android 12 (Snow Cone)|31|10/2021|
|12L|Android 12 Sv2 (Snow Cone v2)|32|03/2022|
|13|Android 13 (Tiramisu)|33|08/2022|
|14|Android 14 (Upside Down Cake)|34|10/2023|
|15|Android 15 (Vanilla Ice Cream)|35|09/2024|
|16|Android 16 (Baklava)|36|06/2025|

> [!info] Documentación oficial sobre versiones de Android
> [Documentación oficial sobre versiones de Android](https://developer.android.com/about/versions).

Cuando creemos un nuevo proyecto en Android Studio, éste nos permitirá acceder a pantalla "Help me choose" que muestra una estadística sobre la distribución de uso de las distintas versiones de Android entre los usuarios de Google Play.

> [!note]- 🖼️ Imagen: Pantalla Help me choose
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/help_me_choose.png)

Esta información de distribución es muy importante para nosotros como desarrolladores porque nos permite conocer, entre otras cosas, con qué versiones de la API de Android nos merece la pena que sean compatibles nuestras aplicaciones, esto es, la versión mínima de la API Android para la que deberíamos desarrollar nuestras aplicaciones. En nuestro caso usaremos como API mínima la versión de API 21.

Android ha sido criticado muchas veces por la **fragmentación** que sufren sus terminales. La fragmentación hace referencia a las distintas "versiones" de Android que hoy en día se pueden encontrar en el mercado. Las causas principales de esta fragmentación son las siguientes:

- Android es un sistema abierto, y como tal, los fabricantes pueden personalizar la versión oficial de Android a los dispositivos que desarrollan, lo que implica que la misma versión del sistema operativo no luzca exactamente igual en distintos dispositivos.
- El hecho de que muchos fabricantes instalan en sus dispositivos versiones personalizadas de Android, significa en la práctica, que las actualizaciones que realiza Google en la versión oficial de Android no son trasladadas inmediatamente a los dispositivos de los usuarios, ya que antes debe pasar por el proceso de personalización o adaptación que hacen los fabricantes. En algunos casos, dichas actualizaciones nunca llegan a producirse.
- En el mercado actual conviven dispositivos provenientes de diferentes versiones oficiales de Android, con distintas características.

Todo ello hace que la fragmentación sea un problema real para los desarrolladores de aplicaciones para Android, ya que tienen que desarrollar sus aplicaciones para multitud de dispositivos diferentes, con hardware diferente y con versiones del sistema operativo diferentes, lo que puede no ser rentable.

Sin embargo, la fragmentación, como toda diversidad, también tiene su lado positivo para los desarrolladores, como la aparición de tiendas online alternativas que crean competencia a Google Play de Google y provocan variedad y abarcamiento de mercado, por lo que más personas descargan aplicaciones.

Con objeto de mejorar los problemas de fragmentación, Google lleva a cabo distintas estrategias:

- Algunas de las novedades son incorporadas a la Google Play Services, una librería propietaria de Google, que se incluye en todos los dispositivos certificados por Google, y que es compatible con versiones de Android a partir de la API 8.

- Las nuevas versiones de Android son presentadas primero en distintas versiones beta, para que los fabricantes puedan ir trabajando en las actualizaciones o en el firmware necesario.

- Proporcionar a los desarrolladores un conjunto de librerías de soporte o compatiblidad, que le permitan desarrollar aplicaciones para dispositivos con versiones antiguas de Android pero que utilicen algunas de las novedades de las versiones recientes de Android.

> [!example] 🎬 Vídeo
> [Explicación en video](https://www.youtube.com/watch?v=Xgbxe6DI2LY)

## 4. Entorno de desarrollo

Para poder desarrollar aplicaciones Android es necesario que configuremos nuestro **equipo de desarrollo** con los siguientes elementos:

- **Sistema operativo**: Podemos usar un equipo de desarrollo con sistema operativo Windows, Linux o Mac OS.
- **Lenguaje**: Como se va a programar usando Java o Kotlin, es imprescindible tener instalado el JDK (_Java Development Kit_) de Oracle. Se recomienda usar la versión 1.8 de la JDK (Java 8).
- **Entorno integrado de desarrollo (IDE)**: Utilizaremos el IDE Android Studio.
- **Kit de desarrollo en Android**: Deberemos tener también una copia del Android SDK (_Software Development Kit_). Este paquete es un conjunto de herramientas que nos harán más fácil programar para Android y gestionar nuestros dispositivos virtuales. Se instala automáticamente al instalar Android Studio y podemos actualizarlo directamente desde el propio IDE.
- **Dispositivos de prueba**: Desde el IDE podremos crear distintos dispositivos virtuales (emuladores), sobre los que simular el comportamiento de las aplicaciones que estemos desarrollando en diferentes tipos de dispositivos, con distintos tamaño y resoluciones de pantalla. También podemos conectar dispositivos físicos reales a nuestro IDE en los que probar nuestras aplicaciones.

## 5. Android Studio

IntelliJ IDEA, también conocido como IntelliJ o IDEA, es un entorno de desarrollo de aplicaciones basadas en Java creado por la empresa JetBrains. Incluye plugins para Java y otros lenguajes y frameworks, entre ellos Android.

> [!info] Web oficial de IntelliJ IDEA
> [https://www.jetbrains.com/es-es/idea/](https://www.jetbrains.com/es-es/idea/)

Dispone de las algunas características muy interesantes para nosotros como desarrolladores:

- Editor de código con coloreado de sintaxis, autocompletado inteligente y refactorización de clases, diseños y estilos.
- Diseño de interfaces de usuario mediante drag-and-drop.
- Acceso al log del sistema (_logcat_), ejecución en modo debug

Aunque se trata de un producto comercial, existe una versión _community_, de código abierto, que puede usarse de forma gratuita, pero que no incluye todas las funcionalidades de la versión comercial.

En mayo de 2013, Google presentó Android Studio, un nuevo entorno de desarrollo gratuito basado en la versión _community_ de IntelliJ IDEA, en el que se integran todas las herramientas específicas necesarias para el desarrollo y depuración de aplicaciones Android. Además de las funcionalidades aportadas por el propio IntelliJ, Android Studio proporciona:

- Soporte para la generación de aplicaciones basadas en Gradle.
- Refactorización y corrección rápida específicos para Android.
- Herramienta Lint para mejorar el rendimiento, la usabilidad y la compatibilidad de nuestras aplicaciones.
- Funcionalidad de firma de aplicaciones.
- Asistentes basados en plantillas para crear diseños y componentes habituales.
- Editor de _layouts_ enriquecido, con funcionalidades avanzadas, como la posibilidad de añadir componentes a la interfaz de usuario simplemente arrastrando y soltando sobre ella, vista previa del _layout_ en distintas configuraciones de pantalla, etc.
- Herramientas de monitorización de uso de memoria, red, etc., por parte de nuestras aplicaciones.

Con la instalación de Android Studio se instalan también automáticamente varios componentes importantes del Android SDK, permitiéndonos añadir componentes o actualizarlos más adelante a través del propio IDE, mediante el conocido como _SDK Manager_ (gestor del SDK).

El _SDK Manager_ de Android Studio posee dos apartados bien diferenciados:

- _SDK Platforms_ (plataformas): Nos permite descargarnos las versiones de la API de Android con las que queremos trabajar. Si queremos desarrollar una aplicación para un versión específica deberemos tener instalada la Android SDK Platform correspondiente.
- _SDK Tools_ (herramientas): Nos permite instalar y actualizar distintas herramientas del SDK, como por ejemplo _Android SDK Build-Tools_ (herramientas de construcción), Android Emulator (emulador), Android SDK Platform-Tools, e Intel x86 Emulator Accelerator (HAXM installer)

Existen versiones de Android Studio para Windows, Mac y Linux.

> [!info] Web oficial de Android Studio
> [https://developer.android.com/studio](https://developer.android.com/studio)

Una vez instalado, cuando lo ejecutamos veremos la siguiente pantalla de bienvenida:

> [!note]- 🖼️ Imagen: Pantalla de bienvenida a Android Studio
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/android-studio.png)

## 6. Emulador

El SDK de Android incluye un emulador de dispositivos virtuales móviles que puede ser ejecutado en nuestro propio ordenador, lo que nos permite hacer prototipos, desarrollar y probar las aplicaciones Android que desarrollemos sin tener que usar un dispositivo móvil real.

El emulador proporciona una copia virtual de las características hardware y software de un dispositivo móvil real, excepto por el hecho de que no puede realizar llamadas telefónicas reales. Utiliza una ventana de nuestro sistema operativo para simular la pantalla del dispositivo móvil. Para manejar el emulador y su dispositivo móvil virtual dispondremos de una serie de teclas de navegación y de controles que podremos usar a través del ratón o del teclado de nuestro ordenador, que nos permitirán generar distintos eventos en nuestro dispositivo virtual para comprobar cómo se comporta ante ellos la aplicación que estamos desarrollando.

Con objeto de permitirnos modelar y probar nuestra aplicación de una manera sencilla, el emulador utiliza las configuraciones prediseñadas en uno o más **AVDs** (_Android Virtual Devices_, Dispositivos Virtuales Android), que nos permiten definir características hardware específicas del dispositivo móvil que queremos emular y sobre el que queremos realizar las pruebas.

Para gestionar los dispositivos de ejecución, tenemos la herramienta conocida como _Device Manager_ o gestor de dispositivos. Podemos acceder a ella a través de la opción `More actions -> Device Manager` de la pantalla de bienvenida, o si estamos dentro de Android Studio, a través del menú `Tools -> Device Manager`.

> [!note]- 🖼️ Imagen: Gestor de dispositivos
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/avd.png)

Con la instalación de Android Studio se nos instala también un dispositivo virtual por defecto, que podemos usar para probar nuestras aplicaciones, aunque a través del _Device Manager_ podemos crear tantos dispositivos virtuales como creemos oportuno.

Cada AVD que definamos puede tener las características de algún dispositivo Android real existente en el mercado, o características completamente personalizadas por nosotros.

Para crear un nuevo AVD tan solo debemos pulsar el icono con el símbolo `+`.

> [!note]- 🖼️ Imagen: Creación de un AVD
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/new-avd.png)

Se nos mostrará un asistente donde debemos seleccionar el primer lugar el hardware que deseamos para el dispositivo. Nosotros seleccionaremos la opción `Phone -> Medium Phone` y pulsaremos el botón `Next`.

> [!note]- 🖼️ Imagen: Creación de un AVD: Selección del hardware
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/avd-hardware.png)

El siguiente paso es seleccionar una versión de sistema operativo Android a cargar en el hardware seleccionado. En nuestro caso seleccionaremos la opción `Tiramisu - Android 13.0 (Google Play)`. Si no tenemos dicha imagen descargada, deberemos descargarla previamente pulsando el icono de descarga situado al lado del nombre de la imagen. Pulsaremos el botón `Next` para pasar al siguiente paso.

> [!note]- 🖼️ Imagen: Creación de un AVD: Selección de la versión de Android
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/avd-software.png)

El último paso es terminar la configuración de nuestro dispoistivo virtual. Dejaremos las opciones por defecto y pulsaremos el botón `Finish`.

> [!note]- 🖼️ Imagen: Creación de un AVD: Configuración final
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/avd-final.png)

Además, cuando creemos un AVD debemos indicar la imagen del sistema operativo Android que queremos cargar en el dispositivo virtual. De esta manera, podremos crear dispositivos virtuales con distintas características, como por ejemplo distintos tamaños de pantalla, y con distintas versiones de del sistema operativo Android, para poder comprobar cómo se comportan nuestras aplicaciones.

Cuando queramos ejecutar la aplicación que estemos desarrollando en ese momento, tan solo bastará con tener un dispositivo virtual o real seleccionado en el _combo box_ correspondiente, y pulsar sobre el icono correspondiente en la barra de herramientas de Android Studio.

> [!note]- 🖼️ Imagen: Ejecución de la aplicación en desarrollo
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/run.png)

Si queremos ejecutar la aplicación en varios dispositivos a la vez, debemos desplegar la _combo box_ de dispositivos y elegir la opción `Select multiple devices...`, tras lo que nos aparecerá una ventana de selección de dispositivos, donde podemos seleccionar uno o varios:

> [!note]- 🖼️ Imagen: Selector de dispositivos para ejecución
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/selectdeploymenttarget.png)

El emulador puede ejecutarse como una aplicación independiente o embebido dentro de Android Studio. Para que esta última opción esté disponible es necesario que esté activa la opción, en `Preferences (Settings) -> Tools -> Emulator -> Launch in the Running Devices tool window`.

En la siguiente imagen se muestra la ventana del emulador embebida dentro de Android Studio:

> [!note]- 🖼️ Imagen: Emulador embebido en Android Studio
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/emulator.png)

Una vez que nuestra aplicación está ejecutándose en el emulador, puede usar los servicios de la plataforma Android para invocar otras aplicaciones, acceder a la red, ejecutar audio o vídeo, almacenar y recuperar datos, notificar al usuario y mostrar transformaciones gráficas, estilos y temas. Es decir se trata de un dispositivo Android totalmente funcional. En algunos casos tendremos incluso acceso a la _Play store_.

El emulador también incluye distintas funcionalidades para la depuración, como la consola en la que podemos comprobar el log del kernel, simulación de interrupciones que se producen sobre nuestra aplicación, como el hecho de que ha llegado un mensaje SMS o una llamada telefónica, e incluso simular efectos de latencia y caídas en la red de datos, o movilidad de GPS.

Para acceder a dichos controles extendidos tendremos que pulsar sobre los tres puntitos verticales en la barra del emulador de la imagen anterior. Como resultado veremos una ventana de configuración de herramientas para el emulador como la siguiente, en la que tendremos distintas secciones de controles:

> [!note]- 🖼️ Imagen: Controles extendidos del emulador
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/emulatortools.png)

## 7. Intel x86 Emulator Accelerator (HAXM)

Los desarrolladores de Intel han creado una imagen del sistema Android que se ejecuta de manera nativa en CPUs x86, que es el tipo de procesador que poseen la mayoría de nuestros equipos de desarrollo. Esto es especialmente importante si tenemos en cuenta que hasta ahora tan solo disponíamos de imágenes para sistemas ARM, lo que implicaba un proceso de traducción durante la ejecución de nuestras aplicaciones en el emulador, ralentizándola.

Normalmente, durante la instalación de Android Studio, se insala también esta herramientas. Si no es así, podemos instalarla directamente desde el _SDK Manager_, accesible desde `More actions -> SDK Manager` de la pantalla de bienvenida de Android Studio, o desde el menú _Tools -> SDK Manager_. Dentro del SDK Manager, en la pestaña _SDK Tools_, seleccionaremos el elemento _Intel x86 Emulator Accelerator (HAXM Installer)_, tal y como se muestra en la siguiente imagen:

> [!note]- 🖼️ Imagen: Instalación de Intel x86 Emulator Accelerator (HAXM)
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/haxm.png)

Una vez descargado, comenzará su instalación desde la carpeta `<sdk folder>/sdk/extras/intel/Hardware_Accelerated_Execution_Manager/`.

> [!info] Instrucciones de instalación en Windows
> [https://software.intel.com/en-us/android/articles/installation-instructions-for-intel-hardware-accelerated-execution-manager-windows](https://software.intel.com/en-us/android/articles/installation-instructions-for-intel-hardware-accelerated-execution-manager-windows).

Intel ha publicado las imágenes correspondientes a distintas versiones de Android. Para poder utilizarlas deberemos descargarlas desde el _AVD manager_ integrado en Android Studio, algo que podremos hacer cuando estemos creando un nuevo dispositivo virtual.

## 8. Ejecución en dispositivo físico

Aunque podemos usar el emulador proporcionado por el Android SDK para probar y depurar nuestras aplicaciones, siempre será recomendable realizar nuestras pruebas en distintos dispositivos físicos para poder comprobar cómo se comporta nuestra aplicación en realidad. De esta manera podremos analizar su velocidad de ejecución, su comportamiento sobre distinto hardware, cómo reacciona ante diferentes eventos que acontezcan en el dispositivos, etc.

De hecho, algunas funcionalidad de nuestras aplicaciones sólo podremos probarlas en dispositivos físicos, ya que el emulador no dispone de ellas, como por ejemplo el acelerómetro.

Para poder probar nuestras aplicaciones en un dispositivo físico debemos cumplir con los siguientes requisitos:

- Tener instalado en el equipo de desarrollo el driver correspondiente a nuestro dispositivo físico para el sistema operativo del equipo de desarrollo. Este driver es suministrado por el fabricante del dispositivo, normalmente dentro de un pack de software del dispositivo para PC.
- Habilitar la opción de depuración en el dispositivo físico. Para ello abrir la aplicación de configuración en nuestro dispositivo Android llamada "Ajustes" y seleccionar el menú "Opciones de Desarrollo", activando la opción "Depuración USB". A partir de la versión Kit Kat de Android el menú "Opciones de Desarrollo" viene deshabilitado por defecto. Para habilitarlo bastará con entrar en el menú "Información del dispositivo" y **pulsar siete veces** sobre el campo "Número de Compilación".
- Tener conectado nuestro dispositivo al ordenador mediante un cable USB o mediante WiFi.

También tenemos disponible un asistente de conexión, accesible desde el desplegable de dispositivo de ejecución. Tan sólo deberemos seguir las instrucciones de conexión.

> [!note]- 🖼️ Imagen: Asistente de conexión
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/asistente-conexion.png)

> [!info] Drivers USB
> En la web oficial para desarrolladores Android puede encontrar más información sobre los drivers USB y una lista con las páginas de descarga de los drivers de los principales fabricantes [(https://developer.android.com/studio/run/oem-usb.html#Drivers)](https://developer.android.com/studio/run/oem-usb.html#Drivers).

Si nuestro dispositivo físico tiene la versión Android 11 o superior, podemos conectarlo a Android Studio directamente por Wi-Fi, para lo que iniciaremos el asistente correspondiente y seguiremos las indicaciones con lo que debemos hacer en nuestro dispositivo físico.

> [!note]- 🖼️ Imagen: Asistente de conexión por WiFi
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/pair-with-wifi.png)

La documentación oficial al respecto es:

> [!info] Conexión de dispositivo físico a Android Studio mediante Wi-Fi
> [https://developer.android.com/tools/adb#connect-to-a-device-over-wi-fi](https://developer.android.com/tools/adb#connect-to-a-device-over-wi-fi)

Por otra parte, otra d elas funcionalidad que nos interesarán si hemos conectado un dispositivo físico es que se muestre en el propio Android Studio la pantalla de nuestro dispositivo físico y que podamos interactuar con él, como si se tratara de un dispositivo virtual en el emulador. De esta manera no es necesario manipular directamente el dispositivo al realizar las pruebas, además de poder introducir los datos directamente desde el teclado del equipo de desarrollo.

Para ello, una vez que en el _Device Manager_ veamos listado nuestro dispositivo físico, deberemos pulsar el botón _start mirroring_:

> [!note]- 🖼️ Imagen: Iniciar la visualización de nuestro dispositivo físico en Android Studio
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/start-mirroring.png)

También existen aplicaciones externas que permiten mostrar en nuestro ordenador la pantalla del dispositivo físico en el que estamos probando la aplicación, permitiéndonos interactuar con él. Estas aplicaciones también suelen ser utilizadas para realizar demostraciones.

> [!info] Aplicaciones de visualización de dispositivos
> - scrcpy: [https://github.com/Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) (recomendada)
> - Mobizen: [https://www.mobizen.com/](https://www.mobizen.com/)
> - Airdroid: [http://web.airdroid.com/](http://web.airdroid.com/)
> - Vysor: [http://www.vysor.io/](http://www.vysor.io/)

> [!example] 🎬 Vídeo
> [Explicación en video de los apartados anteriores](https://www.youtube.com/watch?v=oNG_2Ev-bTA)

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis / dónde | Idea clave |
| --- | --- | --- |
| Android | SO móvil sobre el núcleo Linux + *middleware* | Abierto (su código es accesible); las apps se escriben en Kotlin o Java con el Android SDK. |
| APK | archivo `.apk` | Paquete de instalación; variante del formato JAR. |
| Nivel de API | API 21, API 33, API 36… | Cada versión de Android tiene su número de API; la API mínima decide qué dispositivos pueden instalar la app. |
| Fragmentación | — | Conviven muchas versiones y capas de fabricante; Google la suaviza con Play Services, betas y librerías de compatibilidad. |
| Android Studio | IDE basado en IntelliJ IDEA Community | Gradle, Lint, editor visual de *layouts*, firma de apps y monitorización. |
| SDK Manager | *SDK Platforms* · *SDK Tools* | Descarga versiones de la API y herramientas (emulador, *build-tools*…). |
| AVD | `Tools -> Device Manager` → `+` | Dispositivo virtual = hardware elegido + imagen de Android. |
| HAXM | *SDK Tools* | Acelera el emulador con imágenes x86 nativas. |
| Dispositivo físico | Opciones de desarrollo → Depuración USB | Se desbloquean pulsando 7 veces en «Número de compilación»; por Wi-Fi desde Android 11. |
| *Mirroring* | *start mirroring* · scrcpy | Ver y manejar el móvil real desde el ordenador. |

## Relaciones

- Tema siguiente: [[02 - Creación de un proyecto]] — el primer proyecto con Android Studio.
- [[01 - Introduccion a Kotlin]] — el lenguaje con el que se programan las apps.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar qué es Android y qué aporta el *middleware* sobre el núcleo Linux.
- [ ] Decir qué es un APK.
- [ ] Relacionar versión, nombre y nivel de API (p. ej. Android 13 = Tiramisu = API 33).
- [ ] Explicar las causas de la fragmentación y qué hace Google para reducirla.
- [ ] Enumerar lo que necesita el equipo de desarrollo (JDK, Android Studio, SDK, dispositivos).
- [ ] Crear un AVD desde el *Device Manager*.
- [ ] Activar las opciones de desarrollo y la depuración USB en un móvil real.
