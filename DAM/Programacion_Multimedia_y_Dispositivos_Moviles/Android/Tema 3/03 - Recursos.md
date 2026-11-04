---
asignatura: Optativa
tema: 3
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-recursos
---

# 3 · Recursos

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 3 · Android (vistas)
> Ejercicios: [[03.1 - Ejercicios 3 Recursos]] · Tema anterior: [[02 - Creación de un proyecto]] · Tema siguiente: [[04 - Vistas básicas I]]

> [!info] Material de referencia
> [Recursos](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a03%20-%20Recursos/)

## Índice del tema

- [[#1. La clase Resources]]
- [[#2. Recursos drawable]]
- [[#3. Recursos drawable de iconos vectoriales]]
- [[#4. Recursos de valor]]
- [[#5. Recursos de cadena]]
- [[#6. Recursos de cadena con parámetros]]
- [[#7. Recursos de plural]]
- [[#8. Recursos de entero]]
- [[#9. Recursos de color]]
- [[#10. Recursos de dimensión]]
- [[#11. Recursos de estilo]]
- [[#12. Recursos de tema]]
- [[#13. Ejercicio]]

---

## 1. La clase Resources

Vamos a modificar el código de la actividad de nuestro proyecto anterior para que en vez de usar el literal `"Hello. What a wonderful world!"`, emplee un recurso de cadena en su lugar.

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...
    private fun setupViews() {
        binding.lblMessage.text = "Hello. What a wonderful world!"
    }
}
```

El primer paso es definir el recurso de cadena en el archivo `app/src/main/res/strings.xml`, al que le vamos a dar el nombre `main_wonderful`.

**`app/src/main/res/strings.xml`**

```xml
<resources>
    <string name="app_name">HelloWorld</string>
    <string name="main_lblHello">Hello World!</string>
    <string name="main_wonderful">Hello. What a wonderful world!</string>
</resources>
```

Después, en la actividad, deberemos poder obtener el recurso correspondiente a partir su `resId`. Para ello es necesario que accedamos al objeto de la clase `Resources` asociado al contexto de ejecución del proyecto.

La clase `Resources` es una clase que nos va a permitir acceder desde código Java o Kotlin a todos los recursos de nuestro proyecto, a través de una serie de métodos que reciben el resId del recurso a obtener.

Para poder acceder al objeto `Resources` desde la actividad debemos usar su método `getResources()`. Una vez obtenido el objeto `Resources` podremos usar, por ejemplo, su método `getString(resId)` para obtener la cadena correspondiente al valor del recurso de cadena representado por dicho resId.

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...
    private fun setupViews() {
        val message = resources.getString(R.string.main_wonderful)
        binding.lblMessage.text = message
    }
}
```

La clase `Resources` nos proporciona métodos para acceder a todos los tipos de recursos: `getColor(resId)`, `getStringArray(resId)`, `getInteger(resId)`, etc.

La clase `Activity` dispone de un método `getString()` que internamente llama a `getResources().getString()`, por lo que tendremos que escribir menos código. Sin embargo, el resto de métodos de `Resources` no están disponibles en `Activity`

Así, el código anterior puede quedar más corto, de la siguiente manera:

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...
    private fun setupViews() {
        binding.lblMessage.text = getString(R.string.main_wonderful)
    }
}
```

Como este proceso de obtención del valor de un recurso desde el objeto `Resources` a partir de su _resId_ puede resultar tedioso, en muchos casos los métodos que reciben valores que pueden provenir de recursos están sobrecargados para recibir el resId del recurso, e internamente hacer por nosotros el trabajo sucio de obtener el objeto `Resources` y de usar el método adecuado para obtener el valor del recurso a partir del resId recibido.

Por ejemplo, el método `setText(resId)` de la clase `TextView` está sobrecargado para recibir como argumento, en vez de una cadena de caracteres, el _resId_ del recurso de cadena que se quiere establecer como texto del `TextView`. Así, el código anterior podría acortarse de la siguiente manera:

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...
    private fun setupViews() {
        binding.lblMessage.text = R.string.main_wonderful
    }
}
```

> [!warning] Ojo: en Kotlin esta línea no compila
> La propiedad `text` de Kotlin es de tipo `CharSequence`, así que no admite un `Int` (`Type mismatch`). La sobrecarga que recibe el `resId` es el **método** `setText(resId)`, y hay que llamarlo así: `binding.lblMessage.setText(R.string.main_wonderful)`.

> [!warning] Mucho cuidado
> Debido a que el método `setText(stringResId)` está sobrecargado para recibir un entero correspondiente al `resId` del recurso de cadena, si, por error le pasamos un valor entero cualquiera, por ejemplo la edad del usuario, no se producirá un error de compilación, sino un error en ejecución indicando que no se ha encontrado un recurso de cadena con dicho `resId`.

## 2. Recursos drawable

La carpeta `res/drawables` puede contener archivos de imágenes, cuyos nombres no pueden contener espacios en blanco, en los formatos más habituales: `png`, `bmp`, `jpeg`, `gif`, etc., además de definiciones de _drawables_ realizadas en XML.

Para acceder a este tipo de recursos desde código Java o Kotlin usaremos su resId, obtenido a través de `R.drawable`, que contendrá una propiedad con el nombre del archivo correspondiente a la imagen (sin extensión)

Para referenciarlos desde código XML usaremos la sintaxis `@drawable/<nombre_archivo_sin_extension>`.

## 3. Recursos drawable de iconos vectoriales

Android Studio incorpora el conocido como _Asset Studio_, que permite crear nuestros propios iconos vectoriales a partir de _clip arts_ predefinidos o de archivos de gráficos vectoriales estándar. Para abrir el _Asset Studio_ pulsaremos con el botón derecho del ratón sobre la carpeta `res/drawable` de nuestro proyecto y seleccionaremos la opción de menú `New -> Vector Asset`.

> [!note]- 🖼️ Imagen: Generador de recursos drawable de iconos vectoriales
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/vectorasset.png)

En la pantalla resultante podremos elegir entre crear el icono vectorial a partir de un _clip art_ o de un archivo local. Asset Studio incorpora _clip art_ estándar para las opciones más habituales. Para seleccionar un _clip art_ concreto pulsaremos sobre el botón correspondiente. Tendremos que introducir también el nombre con el que queremos que se cree el fichero con el icono vectorial. Podemos, opcionalmente cambiar el tamaño base del icono, su color y su opacidad. Normalmente dejaremos el icono de color negro, ya que posteriormente podremos tintar el icono del color que queramos. Al pulsar `Next` se nos mostrará otra pantalla para que elijamos donde guardar el archivo del icono, cuyo destino por defecto será la carpeta `res/drawable` de nuestro proyecto.

Los iconos vectoriales corresponden a recursos _drawable_ correspondientes a definiciones XML que describen el icono. Su acceso es similar al de los recursos _drawable_ tradicionales.

En la mayoría de casos no es necesario cambiar el color del icono, ya que Android proporciona atributos xml y métodos que permiten tintarlos del color deseado allí donde son usados.

## 4. Recursos de valor

Como hemos dicho antes, algunos de los recursos de nuestro programa son nombrados explícitamente y no se toma para ello el nombre del archivo en el que se encuentran. Este es el caso de los conocidos como recursos de valores, que son almacenados en distintos ficheros XML dentro de la carpeta `src/main/res/values/` de nuestro módulo.

> [!definition] Recurso de valor
> Un recurso de valor corresponde a un nombre que asociamos a un determinado literal, ya sea de cadena, entero, de dimensión, etc.

Estos ficheros XML incluirán en su interior la definición de recursos de valores. A diferencia del resto de carpetas, en las que cada fichero corresponde a un recurso, los ficheros contenidos en esta carpeta describen varios recursos, que son nombrados explícitamente.

El contenido de cada fichero deberá comenzar con la etiqueta `<resources>` (y terminar con `</resources>`), y cada hijo de dicha etiqueta será considerado un recurso de valor.

Podemos crear tantos ficheros de recursos de valores como queramos, nombrarlos a nuestro gusto e incluso mezclar recursos de valores de diferentes tipos en el mismo fichero.

Sin embargo, para una mayor claridad es recomendable colocar todos los recursos de valores del mismo tipo en un mismo fichero.

Normalmente se usan nombres estándar a la hora de nombrar los ficheros de recursos de valores, aunque no es obligatorio que sean exactamente esos nombres:

**Nombres estándar de ficheros de recursos de valor**

- `src/main/res/values/strings.xml`: Recursos de cadena y de arrays de de cadena.
- `src/main/res/values/integers.xml`: Recursos de entero.
- `src/main/res/values/colors.xml`: Recursos de color.
- `src/main/res/values/dimens.xml`: Recursos de dimensión.
- `src/main/res/values/styles.xml`: Recursos de estilo.
- `src/main/res/values/themes.xml`: Recusos de tema.

Como ejemplo, veamos un posible contenido del archivo `strings.xml`:

**`app/src/main/res/values/strings.xml`**

```xml
<resources>
    <string name="app_name">HelloWorld</string>
</resources>
```

En este caso estamos definiendo un recurso de cadena cuyo nombre será `app_name` y cuyo valor será `HelloWorld`.

Todas estas etiquetas XML usan el atributo `name` para que indiquemos el nombre que queremos darle al recurso.

A continuación estudiaremos distintos tipos de recursos de valores que podemos definir.

> [!tip] Sugerencia
> Se recomienda siempre definir recursos de valor en vez de usar literales, ya que esto nos va a permitir usar diferentes valores para distintas configuraciones del dispositivo, como por ejemplo para distintos idiomas, como veremos más adelante.

## 5. Recursos de cadena

Un recurso de cadena representa un literal de cadena usado por nuestro proyecto. Se define, normalmente dentro del archivo `res/values/strings.xml` de la siguiente manera:

**Recurso de cadena**

```xml
<string name="titulo">Mi Aplicación</string>
```

El valor puede contener las etiquetas HTML `<b>` (negrita), `<i>` (cursiva), o `<u>` (subrayado). Si el valor debe contener los caracteres `<`, `>`, o `&`, el valor debe incluirse dentro de `<![CDATA[valor]]>`

Para referenciar dicho recurso desde código Java usaremos su resId a través de la clase `R`, como en `R.string.titulo`.

Para referenciarlo desde código XML usaremos la sintaxis `@string/titulo`.

## 6. Recursos de cadena con parámetros

Suele ser muy habitual que tengamos que introducir valores calculados por nuestro programa dentro de un mensaje que se le quiera mostrar al usuario. Por ejemplo, supongamos que queremos mostrar el mensaje `3 times`, donde `3` corresponde al valor de una determinada variable.

La primera posibilidad es simplemente construir el mensaje final concatenando sus distintas partes, como en el siguiente código:

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    private var times: Int = 0
    // ...
    private fun setupViews() {
        binding.lblMessage.text = times + " " + getString(R.string.main_times)
    }
}
```

> [!note] Es el ejemplo de lo que **no** hay que hacer
> Además, en Kotlin no compila: `Int` no tiene un `+` que reciba un `String`. Con una plantilla sería `"$times ${getString(R.string.main_times)}"`, pero lo correcto es la cadena con parámetros que se explica a continuación.

habiendo definido en el archivo `res/values/strings.xml` el recurso de cadena

**`app/src/main/res/values/strings.xml`**

```xml
<string name="main_times">times</string>
```

Afortunadamente, Android nos proporciona un método más adecuado para tratar este tipo de situaciones. Así, podemos especificar que un determinado recurso de cadena contenga una serie de parámetros, de manera que al obtener el recurso podamos indicar los argumentos correspondientes a los valores de los parámetros.

> [!tip] Sugerencia
> Siempre es preferible que definas recursos de cadena con parámetros frente a concatenar valores y cadenas, incluso en el caso de Kotlin, y sus _template string_, ya que la definición de recursos de cadena nos ayuda a la internacionalización de nuestra aplicación, de manera que la cadena se pueda mostrar en el idioma del usuario.

Estos recursos siguen siendo recursos de cadena normales, por lo que normalmente se definen en el archivo `/res/values/strings.xml`. Así en el ejemplo anterior crearíamos el recurso de cadena:

**`app/src/main/res/values/strings.xml`**

```xml
<string name="main_times">%1$d times</string>
```

donde el `1$`indica que el valor asignado a dicho parámetro corresponderá al valor proporcionado como primer argumento adicional y el `%d` indica que el valor del argumento deberá ser un valor entero.

Si en vez de un valor entero, fuera una cadena usaríamos `%s`, y si fuera un valor real usaríamos `%f`.

Si tuviéramos más de un parámetro es segundo sería `2$`, el tercero `3$` y así sucesivamente.

> [!tip] Sugerencia
> El uso de `1$`, `2$` no es obligatorio, es decir, podemos indicar simplemente `%d`, `%s`, etc., pero se recomienda especificar el número de argumento por si en un idioma diferente tenemos que cambiar el orden en el que usan los argumentos en la cadena de formato.

Para poder especificar los argumentos correspondientes a los valores que deben tomar los parámetros, a la hora de obtener el recurso usaremos el método `getString(resId, arg…)` de la clase `Resources`, que está sobrecargado para recibir, además del `resId` de la cadena, los valores que queremos que tomen los parámetros, que deberemos pasar en el orden adecuado.

Esta versión de `getString()` también existe directamente en nuestra actividad, sin tener ni siquiera que obtener el objeto `Resources`. Por ejemplo:

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...
    private fun setupViews() {
        binding.lblMessage.text = getString(R.string.main_times, times)
    }
}
```

> [!note] Ten en cuenta
> Internamente el método `getString()` usa el método `format()` de la clase `String` de Java, y por este motivo la especificación de los valores es exactamente la misma que en dicho método.

## 7. Recursos de plural

En algunas ocasiones el texto de un recurso de cadena depende de una cierta cantidad numérica. Supongamos que queremos mostrar un texto con el número de veces que se ha hecho click; en este caso el texto podría ser `1 time`, `2 times`. Como vemos, dependiendo de si es más de una vez debemos usar el plural en vez del singular.

Aunque podríamos definir dos recursos de cadena distintos y decidir cuál usar dependiendo del valor de la variable, Android nos proporciona una funcionalidad muy interesante consistente en definir un único recurso que contenga en su interior la especificación de las distintas cadenas que deben usarse dependiendo de una determinada cantidad. Estos recursos reciben el nombre de **recursos de plural** (_plurals_). Veamos un ejemplo:

**`app/src/main/res/values/plurals.xml`**

```xml
<plurals name="main_times">
    <item quantity="one">%1$d time</item>
    <item quantity="other">%1$d times</item>
</plurals>
```

> [!tip] Sugerencia
> Los recursos de plural suelen definirse dentro de su propio fichero `/res/values/plurals.xml`, aunque al ser recursos de valor no es estrictamente necesario, por lo que podríamos definirlos, por ejemplo, dentro del archivo `string.xml`.

El atributo `quantity` puede tomar uno de los siguientes valores: `zero` (cero), `one` (uno), `two` (dos), `few` (pocos, tres o cuatro), `many` (muchos, más de 10), `other` (resto de casos).

> [!warning] Aviso
> Algunos de estos valores pueden no tener efecto dependiendo del idioma del que se trate. Por ejemplo, en el idioma español, sintácticamente hablando, el uso del singular/plural para la cantidad `0` no difiere del uso del singular/plural de cualquier valor distinto de `1`, como por ejemplo `0 veces` y `4 veces`. Por este motivo si usamos los valores `zero` y `other` a la vez en la definición de un plural y el idioma del dispositivo corresponde al español, la cadena asignada a `zero` nunca es usada, aunque el valor de la variable sea `0`, sino que en su lugar se usa la cadena asignada a `other`. En español sucede exactamente igual con los valores `two`, `few` o `many`.

Para poder obtener un recurso de plurales desde nuestro código Java o Kotlin debemos usar el método `getQuantityString(resId, quantity)` de la clase `Resources`, al que le pasaremos el `resId` del plural y la cantidad a usar para determinar cuál de las cadenas debe mostrarse.

> [!note] Ten en cuenta
> A diferencia de `getString()`, el método `getQuantityString()` no se encuentra definido en la clase `Activity`, sino tan sólo en la clase `Resources`, por lo que tendremos forzosamente que obtener primero el objeto `Resources` desde la actividad.

Si además las cadenas incluidas dentro del recurso plural contienen parámetros, entonces podemos usar una versión sobrecargada del método `getQuantityString(resId, quantity, arg…)`, que recibe el `resId` del plural, la cantidad a usar para determinar cuál de las cadenas debe usarse, y además otra serie de argumentos correspondientes a los valores para los parámetros de la cadena elegida.

Así, en nuestro proyecto haríamos:

**`app/src/main/kotlin+java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...
    private fun setupViews() {
        binding.lblMessage.text = getResources().getQuantityString(R.plurals.main_times, times, times);
    }
}
```

en cuyo caso, el primer `times` es usado para determinar qué cadena escoger de entre las pertenecientes al recurso de plural, y el segundo `times` se usa como argumento del parámetro de la cadena seleccionada.

## 8. Recursos de entero

Un recurso de entero corresponde a un literal entero. Se definen normalmente dentro del archivo `res/values/integers.xml` con el siguiente formato:

**Recurso de entero**

```xml
<integer name="columns">2</integer>
```

Para hacer referencia a ellos desde código Java o Kotlin usaramos su resId obtenido a partir de la clase `R`, como por ejemplo en `R.integer.titulo`. Podemos acceder al valor mediante el método `getInteger(resId)` de la clase `Resources`

Para hacer referencia a ellos desde código código XML usaremos la sintaxis `@integer/titulo`.

## 9. Recursos de color

Un recurso de color corresponde a un valor que representa un color en hexadecimal. Se define, normalmente dentro del archivo `res/values/colors.xml` con la siguiente sintaxis:

**Recurso de color**

```xml
<color name="fondo">#AA8862</color>
```

Para hacer referencia a un color desde código Java o Kotlin usaremos su resId obtenido a través de clase `R`, como en `R.color.fondo`. Para obtener el valor usaremos el método estático `ContextCompat.getColor(context, colorResId)`, que recibe como primer parámetro el contexto, que normalmente será la propia actividad. Esto le permite al método tener en cuenta el tema de la misma a la hora de retornar el color.

> [!tip] Sugerencia
> También existe el método `getColor(colorResId)` de la clase `Resources`, pero este método ha sido marcado como obsoleto (_deprecated_).

Para referenciar un color desde código XML usaremos la sintaxis `@color/fondo`.

## 10. Recursos de dimensión

Un recurso de dimensión representa una cantidad expresada en la unidad de dimensión, como `dp` o `sp`. Se crea, normalmente en el archivo `res/values/dimens.xml` usando la siguiente sintaxis:

**Recurso de dimensión**

```xml
<dimen name="margen_arriba">10dp</dimen>
```

Siempre debe especificarse el valor junto con la unidad.

Para hacer referencia a un valor de dimensión desde código Java o Kotlin usaremos su resId, obtenido a partir de la clase `R.dimen`, como en `R.dimen.margen_arriba`. Para obtener el valor usaremos el método `getDimension(resId)` de la clase `Resources`.

Para hacer referencia a un valor de dimensión desde código XML usaremos la sintaxis `@dimen/margen_arriba`.

Debemos evitar usar la unidad `px` (píxeles) para establecer distancias o tamaños en nuestros layouts. El motivo es que existen pantallas con el mismo tamaño pero que tienen distintas densidades de píxeles, por lo que en este caso, un determinado tamaño en píxeles corresponde a diferentes tamaños físicos reales dependiendo de la densidad de la pantalla en cuestión.

Por lo tanto, a la hora de especificar dimensiones debemos emplear siempre la unidad `dp` (o `dip`).

> [!definition] dp
> Un `dp` es un pixel independiente de la densidad (_density independent pixel_), y corresponde al tamaño físico de un pixel en una resolución de 160 puntos por pulgada.

Para el tamaño del texto, a la hora de especificar una dimensión, usaremos la unidad `sp`, en vez de `dp`.

> [!definition] sp
> Un `sp` es un pixel escalado (_scaled pixel_), y corresponde al valor de un `dp` pero escalado atendiendo al tamaño de texto especificado en las preferencias del dispositivo.

## 11. Recursos de estilo

En Android un estilo no es mas que un conjunto de propiedades y sus correspondientes valores al que le asignamos un nombre. Los estilos serán usados como un patrón para indicar de una sola vez todas las características relativas a la apariencia y al formato con las que debe mostrarse una determinada vista o ventana. De esta manera nos ahorramos el hecho de tener que especificar varias veces las mismas propiedades y sus valores para distintas vistas de nuestra aplicación que vayan a tener una apariencia similar.

Los estilos en Android siguen la misma filosofía que las hojas de estilo CSS en el diseño web: separar el diseño de los contenidos. Por un lado definiremos los estilos de nuestra aplicación en uno o más archivos XML de especificación de recursos. Por otro lado, cuando definamos una vista en una especificación de _layout_ podremos indicar que se muestre con uno de los estilos que hayamos definido.

Los estilos deben estar incluidos en un archivo XML dentro del directorio `res/values/` de nuestro proyecto, cuyo elemento raíz debe ser `<resources>`. El nombre del archivo XML puede ser el que queramos, aunque suele recibir el nombre `styles.xml`. En el mismo archivo podemos definir varios estilos, y podemos tener varios archivos en los que se definan estilos.

Por cada estilo que queramos crear debemos añadir al archivo XML un elemento `<style name="nombre_del_estilo">`, asignándole un nombre diferente a cada estilo. Dentro de este elemento incluiremos una serie de elementos `<item name="nombre_de_la propiedad">valor_de_la_propiedad</item>`, correspondientes a las propiedades que queramos establecer para el estilo. El valor de la propiedad dependerá obviamente de la propiedad concreta que la que se trate.

Android Studio nos permite crear un estilo a partir de las propiedades de una determinada vista en nuestro _layout_. Para ello, bastará con estando situados en dicha vista en el _layout_, pulsar el botón derecha del ratón y en el menú contextual seleccionar `Refactor -> Style`. Se nos abrirá un asistente que nos permite seleccionar qué propiedades de la vista queremos incluir en el estilo:

> [!note]- 🖼️ Imagen: Creación de un estilo a partir de las propiedades de una vista
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/extract-style.png)

Con objeto de no tener que incluir en la especificación de un estilo todas las propiedades necesarias, Android nos permite que cuando definimos un estilo indiquemos un estilo padre del que herede todas sus propiedades, dándonos la posibilidad de redefinir sólo aquellas propiedades que queramos añadir o cambiar en el nuevo estilo. Este estilo padre puede ser uno de los estilos predefinidos en Android o algún otro estilo definido por nosotros mismos.

Para crear un estilo que herede de uno de los estilos predefinidos en Android, deberemos incluir el atributo `parent` dentro su etiqueta `<style>`, asignándole el nombre del estilo que debe actuar como padre.

**Definición de estilo que hereda de un estilo del sistema**

```xml
<resources>
    <style name="CustomButton" parent="Widget.Material3.Button">
        <item name="android:textSize">18sp</item>
        <item name="fontFamily">@font/rubik</item>
        <item name="android:fontFamily">@font/rubik</item>
    </style>
</resources>
```

Si, por el contrario, queremos que nuestro estilo herede de otro estilo de la aplicación definido previamente por nosotros, NO utilizaremos el atributo `parent` de la etiqueta `style`, sino que simplemente a la hora de establecer el nombre del estilo le antepondremos el nombre del estilo padre, separándolo con un punto:

**Definición de un estilo que hereda de un estilo propio**

```xml
<style name="CustomButton.Red">
    <item name="android:textColor">#FF0000</item>
</style>
```

Para acceder a un estilo desde código Java usaremos la notación `R.style.nombre_estilo` y para hacerlo desde un archivo XML de especificación de _layout_ usaremos `@style/nombre_del_estilo`. Debemos fijarnos en que a la hora de definir la propiedad `style` del `TextView`, no usamos la notación `android:`.

## 12. Recursos de tema

Un tema no es más que un estilo que se aplica a una actividad o aplicación completa, en vez de a una determinada vista. Cuando establecemos un estilo como tema de una actividad o aplicación, éste se aplica a todas sus vistas, teniendo en cuenta que a cada vista sólo se le aplicarán las propiedades que acepte, como ya vimos en un apartado anterior.

Para aplicar un estilo como tema a una actividad o aplicación, deberemos incluir el atributo `android:theme` en el elemento `<activity>` o `<application>` correspondiente en el `AndroidManifest.xml`.

Si se trata de un estilo definido por nosotros usaremos la notación `android:theme="@style/nombre_del_estilo"`, como en el siguiente ejemplo:

**Uso de un estilo de tema**

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="es.iessaladillo.pedrojoya.sharedviewmodel">

    <application
        ...
        android:theme="@style/Theme.HelloWorld">
        <!-- ...-->
    </application>
</manifest>
```

El asistente de creación de proyectos de Android nos sugiere que creamos nuestros temas en el archivo `res/values/themes.xml`.

Como los temas no son más que estilos, a la hora de definir nuestro propios temas podemos hacer que éste herede de alguno de los temas predefinidos por Android o la librería de soporte, redefiniendo solamente las propiedades que deseemos modificar.

Algunas de las propiedades de los estilos no son aceptadas por ningún tipo de vista y sólo tienen sentido si el estilo se aplica como tema de una actividad o aplicación, ya que afectan a la ventana completa y no a vistas individuales. Ejemplo de ellos son las propiedades que permiten ocultar el título de la aplicación o la barra de estado, cambiar el fondo de la ventana, etc.

Normalmente en los proyectos creamos nuestro propio tema que hereda de uno de los temas definidos en la librería _material design_, que incorpora automáticamente la gestión de si en las preferencias del dispositivo se ha establecido el modo claro o el modo oscuro, personalizándolo atendiendo a las características de nuestra aplicación o actividad.

**Definición de un estilo de tema**

```xml
<resources xmlns:tools="http://schemas.android.com/tools">
    <!-- Base application theme. -->
    <style name="Base.Theme.HelloWorld" parent="Theme.Material3.DayNight.NoActionBar">
        <!-- Customize your light theme here. -->
        <!-- <item name="colorPrimary">@color/my_light_primary</item> -->
    </style>

    <style name="Theme.HelloWorld" parent="Base.Theme.HelloWorld" />
</resources>
```

Como vemos, algunos de los atributos que modificamos en el tema no llevan el _namespace_ `android:`, ya que se tratan de estilos incorporados al propio proyecto a través de la dependencia correspondiente a _appcompat_.

> [!warning] Aviso
> Para que podamos usar como tema base el tema `Theme.Material3.DayNight.NoActionBar`, es necesario que en archivo `build.gradle.kts` de nuestro módulo se haya incluido la dependencia a la librería de _material design_:
>
> ```kotlin
> dependencies {
>     // ...
>     implementation(libs.material)
> }
> ```

## 13. Ejercicio

> [!question] Ejercicio · Proyecto HelloWord con recursos
> Modifica el proyecto HelloWorld que desarrollaste en un apartado anterior, para que haga uso de recursos de cadena y de dimensión.

> [!success] Resuelto y explicado
> [[03.1 - Ejercicios 3 Recursos]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| `Resources` | `resources.getString(R.string.x)` · `getString(R.string.x)` | Acceso a los recursos desde código; `Activity` solo trae el atajo de `getString()`. |
| *Drawable* | `res/drawable` · `@drawable/x` · `R.drawable.x` | Imágenes y XML; el nombre es el del archivo sin extensión. |
| Icono vectorial | `New -> Vector Asset` | Se ve bien a cualquier escala y se tinta donde se usa. |
| Recursos de valor | `res/values/*.xml` dentro de `<resources>` | Se nombran con `name`; varios por fichero. |
| Cadena | `<string name="x">…</string>` | `@string/x` · `R.string.x`. |
| Cadena con parámetros | `%1$d` · `%2$s` · `getString(id, args)` | Mejor que concatenar: permite traducir y cambiar el orden. |
| Plural | `<plurals>` con `<item quantity="one">` y `<item quantity="other">` | `resources.getQuantityString(id, cantidad, args)`. |
| Entero | `<integer name="x">2</integer>` | `resources.getInteger(R.integer.x)`. |
| Color | `<color name="x">#AA8862</color>` | `ContextCompat.getColor(context, R.color.x)`. |
| Dimensión | `<dimen name="x">10dp</dimen>` | `dp` para tamaños, `sp` para texto, nunca `px`. |
| Estilo | `<style name="…" parent="…">` + `<item>` | Hereda con `parent` (del sistema) o con prefijo `Padre.Hijo` (propio); se aplica con `style="@style/x"`, sin `android:`. |
| Tema | `android:theme` en `<application>` o `<activity>` | Un estilo aplicado a toda la app o actividad; suele heredar de `Theme.Material3…`. |

## Relaciones

- Ejercicios del tema: [[03.1 - Ejercicios 3 Recursos]]
- Tema anterior: [[02 - Creación de un proyecto]] · Tema siguiente: [[04 - Vistas básicas I]]
- [[02 - Creación de un proyecto#11. Recursos y la clase R|02 - Creación de un proyecto → 11. Recursos y la clase R]] — qué es un recurso, la clase `R` y los `resId`.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Obtener una cadena con `getString()` y explicar por qué `setText(resId)` acepta un `Int`.
- [ ] Definir y usar una cadena con parámetros (`%1$d`).
- [ ] Definir un plural y obtenerlo con `getQuantityString()`.
- [ ] Explicar la diferencia entre `dp`, `sp` y `px`.
- [ ] Crear un estilo que herede de uno del sistema y otro que herede de uno propio.
- [ ] Aplicar un tema a la aplicación desde el manifiesto.
- [ ] Hacer el proyecto HelloWorld con recursos.
