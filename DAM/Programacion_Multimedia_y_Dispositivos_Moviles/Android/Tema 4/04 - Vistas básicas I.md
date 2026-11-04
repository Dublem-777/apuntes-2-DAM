---
asignatura: Optativa
tema: 4
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-vistas
---

# 4 · Vistas básicas I

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 4 · Android (vistas)
> Ejercicios: [[04.1 - Ejercicios 4 Vistas básicas I]] · Tema anterior: [[03 - Recursos]] · Tema siguiente: [[05 - Vistas básicas II]]

> [!info] Material de referencia
> [Vistas básicas I](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a04%20-%20Vistas%20basicas%20I/)

## Índice del tema

- [[#1. TextView]]
- [[#2. Button]]
- [[#3. Listeners]]
- [[#4. ImageView]]
- [[#5. Carga de imágenes desde Internet]]
- [[#6. EditText]]
- [[#7. TextInputLayout]]
- [[#8. Ejercicio]]

---

## 1. TextView

La vista más simple que existe en Android es la etiqueta (_label_ en inglés), que recibe el nombre de `TextView`. Una etiqueta es un fragmento de texto que, por defecto, NO puede ser editado directamente por el usuario.

Se utilizan generalmente para dar información al usuario sobre una vista adyacente situada a su lado. Por ejemplo, es muy habitual encontrar una etiqueta seguida de un cuadro de texto, de manera que mediante la etiqueta se informa al usuario sobre el dato que debe introducir en esta última, como por por ejemplo un nombre, una edad, etc.

La clase `TextView` hereda directamente de la clase `View`.

Si queremos incluir un `TextView` en nuestro archivo de _layout_ e indicar en tiempo de compilación algunas de sus propiedades, tendremos que incluir en él una especificación como la que sigue:

**Especificación de TextView en layout**

```xml
<TextView
    android:id="@+id/lblName"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="@string/main_lblName"
    android:textColor="@color/primaryText"
    android:textStyle="bold" />
```

Los atributos XML más utilizados de los TextView son:

- `android:gravity`: Alineación del texto dentro del rectángulo correspondiente a la vista. Los valores más habituales son `start`, `center` y `end`. No tiene sentido definirlo si la anchura de la vista es `wrap_content`.
- `android:text`: Texto que muestra.
- `android:textColor`: Color del texto.
- `android:textAllCaps`: Texto todo en mayúsculas.
- `android:capitalize`: Pone en mayúsculas de manera automática el texto, ya sea la primera letra de la frase, la primera letra de cada palabra o todos los caracteres.
- `android:hint`: Consejo (_tooltip_ o _hint_) cuando no se tiene ningún texto. Tiene más sentido en la vista `EditText` que veremos más adelante.
- `android:textSize`: Tamaño de la letra.
- `android:textStyle`: Formato del texto, ya sea negrita (_bold_), cursiva (_italic_) o ambas (_bold_italic_).
- `android:ellipsize`: Posición por la que se trunca el texto cuando no cabe en la vista, añadiendo `...` (`start`, `end`, `middle`)
- `android:selectAllOnFocus`: Recibe un booleano para indicar si queremos que se seleccione automáticamente el texto de la vista cuando éste gane el foco. Esta propiedad se usará sobre todo en la vista `EditText` que veremos más adelante.
- `android:textAppearance`: Estilo tipográfico que define distintos aspectos, como el tamaño, el grosor, si debe aparecer todo en mayúsculas, etc.

También disponemos de un atributo específico para el editor visual de layouts llamado `tools:text`, que se aplica a cualquier vista que pueda mostrar texto, para indicar el texto que debe mostrar el editor visual de _layouts_, aunque no se haya especificado la propiedad `android:text` para la vista.

> [!tip] Sugerencia
> A la hora de mostrar un texto de ejemplo para ver cómo queda el diseño, podemos usar las colecciones de datos de ejemplo proporcionados por Android Studio. Por ejemplo para mostrar como texto un párrafo de _lorem ipsum_ podemos usar `tools:text="@tools:sample/lorem"` o para mostrar un nombre `tools:text="@tools:sample/full_name"`.

Por otra parte, tenemos la posibilidad de asociar un determinado _drawable_ (por ejemplo un pequeño icono a un `TextView`, de manera que se muestre a su lado (a su izquierda, derecha, arriba o abajo) a una determinada distancia. Para ello usaremos los siguientes atributos XML:

- `android:drawableLeft`, `android:drawableRight`, `android:drawableTop` y `android:drawableBottom`: _Drawable_ que debe mostrarse a su izquierda, derecha, arriba y abajo, respectivamente.
- `android:drawablePadding`: Espacio (distancia) entre el texto y el _drawable_.
- `app:drawableTint`: Color con el que tintar el _drawable_.

> [!tip] Sugerencia
> No existe ninguna propiedad para establecer el tamaño del _drawable_, por lo que se recomienda que el tamaño de éste sea acorde al del texto contenido en el `TextView`.

Desde código Java o Kotlin, los métodos más usados de `TextView` serán `setText(charSequence)` para establecer el texto que debe mostrar y `getText()`, que retorna un objeto `CharSequence` con el texto mostrado. `CharSequence` es una interfaz implementada por `String`. Si queremos convertirlo a cadena podemos usar el método `toString()` del objeto `CharSequence`.

**Obtener y establecer el texto de un TextView**

```kotlin
val name = binding.lblName.text.toString();
binding.lblName.text = name.toUpperCase();
```

> [!tip] En Kotlin actual
> Los `;` sobran y `toUpperCase()` está obsoleto: hoy se escribe `binding.lblName.text = name.uppercase()`.

Si nuestra aplicación usa un tema que extienda de `Theme.MaterialComponents`, la etiqueta `<TextView>` se convierte internamente e una etiqueta `<com.google.android.material.textview.MaterialTextView>`, que corresponde a la implementación de un _textview_ atendiendo a la guía _material design_.

La guía de diseño _material design_ establece una serie de estilos tipográficos estándar para el texto. Para saber más sobre ellos visite: [https://github.com/material-components/material-components-android/blob/master/docs/theming/Typography.md](https://github.com/material-components/material-components-android/blob/master/docs/theming/Typography.md)

Estos estilos están definidos como `TextAppearance.Material3.HeadlineLarge`, `TextAppearance.Material3.HeadlineMedium`, `TextAppearance.Material3.HeadlineSmall`, `TextAppearance.Material3.TitleLarge`etc. Para establecer un estilo tipográfico al `TextView` usaremos el atributo `android:textAppearance`.

**Uso de atributo android:textAppearance**

```xml
<TextView
    android:id="@+id/lblName"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="@string/main_lblName"
    android:textAppearance="@style/TextAppearance.Material3.HeadlineSmall" />
```

## 2. Button

Un botón (_button_) es un zona de pantalla que puede ser pulsada por el usuario para indicar que se empiece a llevar a cabo una acción. Android proporciona distintos tipos de vistas con funcionalidad de botón. El tipo más simple y genérico es la clase `Button`, que es una subclase de `TextView`, por lo que hereda sus propiedades y métodos.

Si nuestra aplicación usa un tema que extienda de `Theme.MaterialComponents`, la etiqueta `<Button>` se convierte internamente e una etiqueta `<com.google.android.material.button.MaterialButton>`, que corresponde a la implementación de los botones atendiendo a la guía _material design_.

La guía de diseño _material design_ establece estilos visuales para distintos tipos de botones. Para saber más visite: [https://m3.material.io/components/buttons/overview](https://m3.material.io/components/buttons/overview)

> [!note]- 🖼️ Imagen: Estilos estándar de Botones
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/buttons.png)

En el siguiente ejemplo se incluye un objeto `Button` en un fichero de _layout_ XML para el que se usa el tipo de botón por defecto:

**Especificación de Button en layout**

```xml
<Button
    android:id="@+id/btnAccept"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/main_btnAccept"/>
```

También podemos hacer que el botón de _material design_ incluya un icono. Para ello haremos uso de los atributos `app:icon` (icono), `app:iconSize` (tamaño), `app:iconGravity` (posición, _start_ o _end_) y `app:iconPadding` (separación respecto al texto). Por ejemplo:

**Button con texto e icono**

```xml
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/add_student"
    app:icon="@drawable/ic_baseline_add_24" />
```

Si queremos que el botón tenga un estilo diferente de los existentes en _material design_, simplemente debemos establecer el valor adecuado por el atributo `style`. Por ejemplo, para que sea de tipo _outlined button_ le aplicaremos el atributo `style="@style/Widget.Material3.Button.ElevatedButton"`. Por ejemplo:

**ElevatedButton con texto e icono**

```xml
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/add_student"
    app:icon="@drawable/ic_baseline_add_24"
    style="@style/Widget.Material3.Button.ElevatedButton" />
```

> [!info] Atributos material design para botones
> Para saber más sobre todos los atributos de los distintos tipos de botones en material design visite
>
> [https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md](https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md)

## 3. Listeners

En la programación de aplicaciones con interfaces de usuario gráficas es muy usual que las acciones realizadas por el usuario, conocidos como eventos, sean notificados al código de programación a través de lo que se conoce como _callbacks_ o _listeners_.

Un _listener_ no es más que una interfaz que contiene uno o más métodos de _callback_ que serán ejecutados por el sistema cuando se produzca el evento correspondiente en una determinada vista.

Nuestra misión como programadores será crear un objeto de una clase que implemente dicha interfaz _listener_ para que el o los métodos correspondientes contengan el código de respuesta al evento producido por el usuario. Por ejemplo, la interfaz `View.OnClickListener` define un método de _callback_ llamado `onClick(view)` que será llamado por el sistema cuando el usuario haga click sobre una vista, que será pasada como argumento al método.

Una vez creado dicho objeto _listener_, deberemos asociarlo a la vista correspondiente, para que el sistema sepa sobre qué objeto debe ejecutar el método de _callback_ cuando el usuario produzca el evento en la vista. Por ejemplo, llamaremos al método `setOnClickListener(onClickListener)` de una determinada vista para establecer el _listener_ `OnClickListener` a cuyo método `onClick(view)` queremos que el sistema llame cuando el usuario haga click sobre ella.

Como podemos intuir, los _listener_ son los candidatos perfectos para usar la sintaxis Java de clases inline anónimas, o de expresiones _object_ en Kotlin, ya que debemos crear un objeto específico para la ocasión y en realidad nos da igual cómo se llame la clase porque sólo vamos a crear un único objeto de ella.

Por ejemplo, podemos crear un objeto de una clase anónima que implementa la interfaz `OnClickListener` de manera inline, justo cuando se está estableciendo como _listener_ para una determinada vista a través de su método `setOnClickListener(onClickListener)`. Por ejemplo::

**`app/src/main/java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setupViews()
    }

    private fun setupViews() {
        binding.btnClickMe.setOnClickListener(object : View.OnClickListener {
            override fun onClick(view: View?) {
                // ...
            }
        })
        // ...
    }
}
```

Sin embargo, y como ya sabemos, gracias a la conversión SAM, podemos usar directamente un lambda como argumento de un parámetro cuyo tipo sea una interfaz funcional, aumentando la legibilidad de nuestro código. Por ejemplo, si queremos establecer el _listener_ para el código anterior haciendo uso de una expresión _lambda_ haríamos:

**`app/src/main/java/[paquete]/MainActivity.kt`**

```kotlin
class MainActivity : AppCompatActivity() {
    // ...

    private fun setupViews() {
        binding.btnClickMe.setOnClickListener {
            // ...
        }
        // ...
    }
}
```

Debemos tener en cuenta que solo podremos uar una lambda si el tipo corresponde a una interfaz funcional, por lo que en el caso de un _listener_ contenga más de un método abstracto, deberemos seguir usando _object expresions_.

> [!note] Long click
> En los sistemas operativos móviles no existe el concepto de click con botón derecho del ratón, ya que normalmente no se usa ningún dispositivo apuntador, sino que la pantalla del dispositivo es táctil. Sin embargo existe una acción similar conocida como hacer click largo, consistente en dejar pulsada la vista durante más tiempo del habitual.
>
> Para saber más sobre esta acción investiga en la documentación oficial [https://developer.android.com/index.html](https://developer.android.com/index.html) acerca de la interfaz `OnLongClickListener`.

## 4. ImageView

La clase `ImageView` permite mostrar una imagen en pantalla. Es una subclase directa de `View`, por lo que hereda sus métodos y propiedades. A diferencia de la clase `Button`, `ImageView` no es subclase de `TextView`, por lo que no hereda de ella, y por tanto, tampoco hereda sus atributos.

Sus atributos XML más importantes son:

- `android:src`: Imagen a mostrar en el `ImageView`. Normalmente esta propiedad recibirá el resId de un recurso de imagen (_drawable_) contenido en la carpeta `res/drawable` del proyecto, como por ejemplo `android:src="@drawable/photo"`. Para establecerlo desde código utilizaremos el método `setImageResource(drawableResId)`.
- `android:maxWidth`: Anchura máxima de la imagen.
- `android:maxHeight`: Altura máxima de la imagen.
- `android:scaleType`: Controla como se posicionará y redimensionará la imagen para adaptarse al tamaño del ImageView. El valor más usado es `centerCrop`, que redimensiona la imagen manteniendo la relación de aspecto para que su alto y ancho sea igual o mayor, respectivamente, que el alto y ancho del `ImageView`, de manera que coloca la imagen en el centro del `ImageView` y recorta la parte de la imagen que queda fuera de los límites del `ImageView`, por lo que puede que la imagen no se vea completa, aunque sí ocupará todo el espacio proporcionado por el `ImageView`.
- `android:contentDescription`: Descripción textual de la imagen, para mejorar la accesibilidad. Es heredada de `View`, pero con `ImageView` tiene mucho más sentido su uso.

> [!info] Propiedad scaleType
> Podemos ver un ejemplo de los distintos valores posibles para la propiedad `android:scaleType` en el enlace [http://etcodehome.blogspot.com.es/2011/05/android-imageview-scaletype-samples.html](http://etcodehome.blogspot.com.es/2011/05/android-imageview-scaletype-samples.html).

**Especificación de ImageView en layout**

```xml
<ImageView
    android:id="@+id/imgPhoto"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:src="@drawable/photo"
    android:scaleType="centerCrop"
    android:contentDescription="@string/main_imgPhoto"/>
```

Tenemos disponible también un atributo específico para el editor visual de _layouts_ llamado `tools:src`, que se aplica a una vista _ImageView_ para indicar la imagen que debe mostrar el editor visual, aunque no hayamos especificado el atributo `android:src`. Podemos usar alguna imagen proporcionada por Android Studio, mediante `@tools:sample/avatars`.

Cabe destacar de esta clase la familia de métodos `setImage...()` que permiten establecer en tiempo de ejecución la imagen que mostrará el `ImageView` pasándole como argumento el objeto correspondiente a la imagen. Así tenemos `setImageBitmap(bitmap)`, `setImageDrawable(drawable)`, `setImageResource(drawableResId)`, `setImageURI(uri)`.

En el siguiente código se muestra el uso del método `setImageResource()` para mostrar en el `ImageView` un recurso de tipo _drawable_ disponible dentro de nuestra carpeta `res`:

**Métodos principales de ImageView**

```kotlin
binding.imgPhoto.setImageResource(R.drawable.photo);
```

La librería _material design_ proporciona la vista `com.google.android.material.imageview.ShapeableImageView`, que hereda de `ImageView`, y que permite establecer un estilo de recorte para la vista, así como un borde para la misma, que seguirá el recorte realizado.

> [!info] Información sobre ShapeableImageView
> [Información sobre ShapeableImageView](https://www.howtodoandroid.com/shapeableimageview-material-components-android/)

De esta manera podremos crear, por ejemplo, una vista redonda, con las esquinas redondeadas o con las esquinas recortadas, para mostrar en su interior una imagen.

Sus principales atributos XML son:

- `app:shapeAppearanceOverlay`: Recibe el resId de un recurso de estilo en el que se define el estilo de recorte que se debe realizar sobre las esquinas de la vista. Por defecto no tiene ningún recorte.
- `app:strokeWidth`: Grosor del borde de la vista, que se mostrará siguiendo el estilo de recorte establecido. Debemos tener en cuenta que para que el borde no se visualice recortado, será necesario que se aplique un _padding_ al menos del mismo tamaño al grosor del borde.
- `app:strokeColor`: Color del borde de la vista.

Para definir el estilo de recorte usaremos los siguientes atributos:

- `cornerSize`, `cornerSizeTopLeft`, `cornerSizeTopRight`, `cornerSizeBottomRight`, `cornerSizeBottomLeft`: Tamaño del recorte de, respectivamente, las cuatro esquinas, la superior izquierda, la superior derecha, la inferior derecha y la inferior izquierda. Se puede especificar en `dp` o en porcentaje. Por defecto `0dp`.
- `cornerFamily`: Tipo de recorte de, respectivamente, las cuatro esquinas, la superior izquierda, la superior derecha, la inferior derecha y la inferior izquierda. Puede tomar el valor `rounded` o el valor `cut`. Por defecto vale `rounded`.

El estilo de recorte debe heredar de `ShapeAppearanceOverlay.App`. Por ejemplo, si queremos definir un estilo de recorte con las esquinas redondeadas al 50% de manera que si la vista es cuadrada se dibujo en forma de círculo, en el archivo `res/values/styles.xml` definiremos el siguiente estilo:

**Definición de estilo para vista circular**

```xml
<style name="ShapeAppearanceOverlay.App.CornerSize50Percent" parent="">
    <item name="cornerSize">50%</item>
</style>
```

Ahora veamos un ejemplo de definición de un `ShapeableImageView` que hace uso de dicho estilo de recorte, además de mostrar un borde:

**Definición de un ShapeableImageView con el estilo de recorte anterior**

```xml
<com.google.android.material.imageview.ShapeableImageView
    android:layout_width="80dp"
    android:layout_height="80dp"
    android:src="@drawable/ic_launcher_background"
    android:layout_margin="8dp"
    android:padding="4dp"
    app:strokeWidth="4dp"
    app:strokeColor="@color/purple_200"
    app:shapeAppearanceOverlay="@style/ShapeAppearanceOverlay.App.CornerSize50Percent" />
```

El resultado será el siguiente:

> [!note]- 🖼️ Imagen: Ejemplo de uso de ShapeableImageView
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/shapeable_image_view.png)

## 5. Carga de imágenes desde Internet

La vista `ImageView` no proporciona ningún método para mostrar una imagen disponible en la red a través de una determinada URL. Sin embargo, existe una librería de terceros, llamada Coil, que nos facilita mucho esta tarea.

Para poder trabajar con Coil es necesario que agreguemos la siguiente dependencia en el archivo `build.gradle.kts` de nuestro módulo:

**build.gradle.kts del módulo**

```kotlin
dependencies {
    implementation("io.coil-kt.coil3:coil:3.0.0-rc01")
    implementation("io.coil-kt.coil3:coil-network-okhttp:3.0.0-rc01")
}
```

Además, para que nuestra aplicación tenga acceso a Internet es necesario que en el archivo `AndroidManifest.xml` se solicite el permiso de Internet de la siguiente manera:

**`Manifiesto AndroidManifest.xml`**

```xml
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.example.compose_components">

    <uses-permission android:name="android.permission.INTERNET"/>

    <application
        ...>
        <!-- ... -->
    </application>
</manifest>
```

Para cargar una imagen a partir de su URL usaremos la _extension function_ de `ImageView` proporcionada por Coil:

**Carga de imagen a partir de su URL**

```kotlin
imageView.load("https://www.example.com/image.jpg") {
    crossfade(true)
}
```

Para saber más sobre esta librería visite [https://coil-kt.github.io/coil/](https://coil-kt.github.io/coil/).

## 6. EditText

Una caja de texto es una zona rectangular de pantalla que puede recibir el foco y en el que el usuario puede introducir y editar un texto. En Android, las cajas de texto se implementan gracias a la clase `EditText`, que es una subclase de `TextView`, por lo que hereda sus propiedades y métodos.

> [!note]- 🖼️ Imagen: EditText
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/textfields.png)

A continuación destacamos algunos atributos XML de los `EditText`:

- `android:capitalize`: Pone en mayúsculas de manera automática el texto, ya sea la primera letra de la frase, la primera letra de cada palabra o todos los caracteres. Es un atributo de `TextView`.
- `android:hint`: Consejo (_tooltip_ o _hint_) que se muestra al usuario cuando no se ha introducido ningún texto aún. Es un atributo de `TextView`.
- `android:inputType`: Indica el tipo de dato que va a ser introducido en el cuadro de texto, limitando los caracteres que pueden ser introducidos e incluso las teclas que aparecen en el teclado virtual del dispositivo. Podemos incluir un único valor o varias posibilidades combinadas con el carácter `|`. Algunos de los valores que podemos especificar son: `text` (texto genérico), `textEmailAddress` (dirección de email), `textPersonName` (nombre de una persona), `textPassword` (contraseña), `textVisiblePassword` (contraseña visible), `number` (número), `numberDecimal` (número real), `phone` (número de teléfono), `datetime` (fecha y hora), `date` (fecha), `time` (hora), `textMultiLine` (varias líneas de alto).
- `android:digits`: Cadena de caracteres que contiene los únicos caracteres válidos que pueden ser introducidos en el `EditText`. Por ejemplo, `android:digits="0123456789"` sólo permite introducir dígitos, ni siquiera `.` ni `,` La mayoría de las veces no se usa esta propiedad porque con `android:inputType` tenemos suficiente.
- `android:maxLength`: Número máximo de caracteres que podrán introducirse en el `EditText`. Muy útil cuando, por ejemplo, dicho dato va a ser almacenado en una base de datos estructurada donde la columna de la tabla correspondiente tiene un tamaño fijo.
- `android:ems`: Anchura del `EditText` en número de caracteres. Sólo tiene sentido cuando la propiedad `android:width` tiene el valor `wrap_content`.
- `android:lines`: Número de líneas de alto que ocupa visualmente la vista. Sólo tiene sentido si `android:inputType` incluye entre sus valores `textMultiLine`.
- `android:maxLines`: Número de líneas de alto que como máximo ocupará visualmente la vista. Sólo tiene sentido si `android:inputType` incluye entre sus valores `textMultiLine`. Si el valor de `android:lines` es menor al de `android:maxLines` el `EditText` podrá crecer conforme agreguemos líneas.

En el siguiente código definimos un `EditText` en el fichero de _layout_ XML:

**Especificación de EditText en layout**

```xml
<EditText
    android:id="@+id/txtName"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:inputType="textPersonName" />
```

Sin duda la propiedad más importante de `EditText` es su texto, que podemos obtener o establecer mediante el par de métodos `getText()` y `setText()`, heredados de `TextView`.

> [!warning] Aviso
> Debemos tener en cuenta que el método `getText()` de un `EditText` retorna un objeto de la clase `Editable`, y no una cadena, por lo que si queremos pasarlo a cadena deberemos usar el método `toString()` del objeto `Editable`.

Sin embargo `setText()` recibe un `CharSequence`, por lo que podemos pasarle directamente una cadena de caracteres.

En el siguiente código se muestra el uso de algunos de los métodos más importantes de `EditText`:

**Métodos principales de EditText**

```kotlin
val name = binding.txtName.text.toString();
binding.txtName.text = name.toUpperCase();
```

> [!warning] Ojo: con un `EditText` la segunda línea no compila en Kotlin
> En `EditText`, `getText()` devuelve `Editable` pero `setText()` recibe `CharSequence`. Como los tipos no coinciden, Kotlin trata `text` como una propiedad de **solo lectura** de tipo `Editable`, y asignarle un `String` da `Type mismatch`. Hay que llamar al método: `binding.txtName.setText(name.uppercase())`.

Otra propiedad muy interesante es la posibilidad de mostrar un mensaje de error en el `EditText` cuando su contenido no sea válido. Para ello usaremos el método `setError(message)`, que recibe el mensaje a mostrar. Si posteriormente queremos que desaparezca el error, debemos llamar a `setError(null)`.

## 7. TextInputLayout

La librería _material design_ define el concepto de _text field_ (campo de texto), como `EditText` mejorado con funcionalidad adicional como la siguiente:

- Convertir el _hint_ es una etiqueta flotante.
- Mostrar un mensaje de error.
- Mostrar un contador de caracteres.
- Mostrar un texto de ayuda.
- Mostrar un prefijo o un sufijo.
- Mostrar un icono a la izquierda o a la derecha del texto.
- Mostrar un icono para mostrar u ocultar el password contenido en el `EditText`.
- Ser usado con un menú desplegable, a modo de _spinner_ (ya lo veremos más adelante).

> [!note]- 🖼️ Imagen: TextInputLayout
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/textinputlayout.png)

Para especificar un _text field_ usaremos un nuevo _ViewGroup_, llamado `TextInputLayout`, dentro del que incluiremos una vista `TextInputEditText`, que es una versión específica de `EditText`.

Para indicar el comportamiento del _text field_ especificaremos una serie de atributos en la vista `TextInputLayout`. Por ejemplo, le asignaremos el atributo `android:hint` para indicar el _hint_ que debe mostrarse a modo de etiqueta flotante.

Veamos un ejemplo:

**Especificación de un text field**

```xml
<com.google.android.material.textfield.TextInputLayout
    android:id="@+id/textField"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="@string/label">

    <com.google.android.material.textfield.TextInputEditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>
</com.google.android.material.textfield.TextInputLayout>
```

Podemos agregar al `TextInputLayout` una serie de atributos para añadirle distintas funcionalidades.

La primera de ellas es la posibilidad de mostrar un icono a la izquierda del `TextInputEditText`:

- `app:startIconDrawable`: Icono que se muestra a la izquierda del `TextInputLayout`.
- `app:startIconContentDescription`: Descripción textual del icono que se muestra a la izquierda del `TextInputLayout`.

También podemos agregar un icono a la derecha del `TextInputEditText` de manera que al pulsarse se realice una acción concreta. Para ello usaremos los siguientes atributos:

- `app:endIconMode="custom"`: Modo de funcionamiento del icono que se muestra a la derecha del `TextInputLayout`. Cuando toma el valor `custom`, podemos configurar el icono, su descripción y la acción que se debe llevar a cabo al pulsarlo.
- `app:endIconDrawable`: Icono que se muestra a la derecha del `TextInputLayout`. Se usa cuando `app:endIconMode="custom"`.
- `app:endIconContentDescription`: Descripción textual del icono que se muestra a la derecha del `TextInputLayout`.

Para indicar el código que se debe ejecutar cuando se pulse el icono usaremos el método `setEndIconOnClickListener` del `TextInputLayout`.

También podemos establecer un prefijo o su sufijo textual, que se mostrará, respectivamente, antes o después del texto introducido por el usuario. Podemos usar este prefijo o sufijo por ejemplo para mostrar la unidad en la que el usuario debe introducir una determianda cantidad. Para ello usaremos los siguientes atributos:

- `app:prefixText`: Prefijo que se muestra antes del texto introducido por el usuario.
- `app:suffixText`: Sufijo que se muestra después del texto introducido por el usuario.

Por otra parte, podemos hacer que se muestre un texto informativo debajo del `TextInputEditText`, para lo que usaremos los siguientes atributos:

- `app:helperTextEnabled="true"`: Para que se muestre un texto de ayuda debajo del `TextInputEditText`.
- `app:helperText`: Texto de ayuda que se muestra debajo del `TextInputEditText`.

Pero además la vista `TextInputLayout` proporciona funcionalidad añadida respecto a la gestión de errores asociada a la validación del dato introducido en el `TextInputEditText`, ya que mediante su método `setError(mensaje)` podremos hacer que se muestre un determinado mensaje de error justo debajo del `TextInputEditText`. Cuando deje de producirse el error podremos dejar de mostrar el mensaje de error mediante el método `setErrorEnabled(false)` y `setError("")`.

Otra funcionalidad interesante de esta vista es la posibilidad de contabilizar automáticamente el número de caracteres que el usuario va introduciendo en el `TextInputEditText` mostrando a la derecha del texto de ayuda el número de caracteres introducidos y el máximo permitido. Para ello usaremos los atributos:

- `app:counterEnabled="true"`: Para activar dicha funcionalidad.
- `app:counterMaxLength`: Número máximo de caracteres permitido. Si se sobrepasa el contador se mostrará en rojo para indicar el error.

Por otro lado, en el caso de que el `TextInputEditText` tenga el atributo `android:inputType="textPassword"`, podemos hacer que se incluya un icono con el que conmutar entre mostrar u ocultar automáticamente el texto del _password_. Para ello debemos establecer en el `TextInputLayout` el atributo `app:endIconMode="password_toggle"`. El icono mostrado es configurado automáticamente.

En otras ocasiones querremos que al pulsar el icono que se muestra a la derecha de `TextInputEditText` directamente se elimine automáticamente el texto de este último. Para ello debemos establecer en el `TextInputLayout` el atributo `app:endIconMode="clear_text"`. El icono mostrado es configurado automáticamente.

Cuando hablemos de las listas desplegables veremos que usaremos un `TextInputLayout` que contenga en su interior un `AutoCompleteTextView`, proporcionándonos la funcionalidad de _hint_ que actúa como _label_ flotante siguiente la guía de diseño _material design_.

Para saber más sobre esta vista visite [https://github.com/material-components/material-components-android/blob/master/docs/components/TextField.md](https://github.com/material-components/material-components-android/blob/master/docs/components/TextField.md)

## 8. Ejercicio

> [!question] Ejercicio · Proyecto CountingClicks
> Realiza una aplicación que muestre cuántas veces se ha hecho click en un botón.
>
> [!note]- 🖼️ Imagen: Proyecto CountingClicks
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/prCountingClicks.gif)

> [!success] Resuelto y explicado
> [[04.1 - Ejercicios 4 Vistas básicas I]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| TextView | `android:text` · `android:textAppearance` · `tools:text` | Etiqueta que el usuario no edita. |
| Button | `<Button>` (internamente `MaterialButton`) | Hereda de `TextView`; `app:icon` y estilos `Widget.Material3.Button.*`. |
| *Listener* | `setOnClickListener { … }` | Conversión SAM: lambda si la interfaz tiene un solo método; si no, `object :`. |
| ImageView | `android:src` · `android:scaleType="centerCrop"` · `android:contentDescription` | `setImageResource(R.drawable.x)`. |
| ShapeableImageView | `app:shapeAppearanceOverlay` · `app:strokeWidth` | Esquinas redondeadas o cortadas, con borde. |
| Coil | `imageView.load(url) { crossfade(true) }` | Necesita su dependencia y el permiso `INTERNET`. |
| EditText | `android:inputType` · `android:hint` · `android:maxLength` | `text` es `Editable`: `toString()` para leer, `setText()` para escribir; `setError()`. |
| TextInputLayout | `TextInputLayout` + `TextInputEditText` | *Hint* flotante, error, contador, iconos, prefijo/sufijo, `password_toggle` y `clear_text`. |

## Relaciones

- Ejercicios del tema: [[04.1 - Ejercicios 4 Vistas básicas I]]
- Tema anterior: [[03 - Recursos]] · Tema siguiente: [[05 - Vistas básicas II]]
- [[10 - Programación funcional#6. Conversión SAM|10 - Programación funcional → 6. Conversión SAM]] — por qué el *listener* se puede escribir como lambda.
- [[07 - POO II#Anonymous object expression|07 - POO II → Anonymous object expression]] — el `object : View.OnClickListener`.
- [[08 - POO III#5. Extension functions|08 - POO III → 5. Extension functions]] — `load()` de Coil es una *extension function* de `ImageView`.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Definir en XML un `TextView`, un `Button`, un `ImageView` y un `EditText`.
- [ ] Asignar un `OnClickListener` con `object :` y con lambda, y explicar cuándo vale la lambda.
- [ ] Explicar qué hace `scaleType="centerCrop"`.
- [ ] Cargar una imagen de Internet con Coil (dependencia, permiso y `load()`).
- [ ] Leer y escribir el texto de un `EditText` y mostrar un error.
- [ ] Configurar un `TextInputLayout` con contador, texto de ayuda y `endIconMode`.
- [ ] Hacer el proyecto CountingClicks.
