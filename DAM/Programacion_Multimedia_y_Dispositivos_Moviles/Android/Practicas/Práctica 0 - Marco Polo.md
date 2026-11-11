---
asignatura: Optativa
tema: 2-4
tipo: ejercicio
estado: completo
fecha: 2026-11-04
tags:
  - DAM/ejercicio
  - DAM/optativa/android-practicas
  - DAM/optativa/ejercicios
---

# Práctica 0 · Marco Polo

> [!info] Origen
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Práctica evaluable de Android (vistas)  
> Práctica siguiente: [[Práctica 1 - BMI]]

> [!note] Sobre la solución
> Solución desarrollada con lo visto en los temas de Android hasta la fecha de la práctica, siguiendo el estilo del proyecto `HelloWorld` de los apuntes: paquete `es.iessaladillo.pedrojoya.<app>`, *layout* `main_activity.xml`, ViewBinding con `by lazy`, `setupViews()` y recursos con prefijo `main_`. Compilada (AGP 9.5, `compileSdk = 37`, `minSdk = 27`) y probada en el emulador *Medium Phone* con Android 13 (API 33).
>
> El Kotlin de esta nota lleva la explicación en comentarios y las funciones en orden de uso (primero se declaran las que se usan y después las que las llaman; `onCreate()` cierra la clase). Es el mismo código que el proyecto, con otro orden y más comentarios.

---

## Práctica 0 · Marco Polo

> [!question] Enunciado
> **Práctica 0: Marco Polo** 
>
> Realización una aplicación Android que muestre un TextView y un Button dentro de un LinearLayout vertical. Inicialmente el TextView debe mostrar el texto "Marco" y el botón debe mostrar el texto "Polo". Cuando se pulsa el botón, el TextView debe pasar a mostrar el texto "Polo" y el botón el texto "Marco". Si se vuelve a pulsar el botón, el TextView debe volver a mostrar "Marco" y el botón mostrar "Polo", y así sucesivamente.

> [!info] Proyecto
> **Proyecto:** `MarcoPolo`  
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Android/Practicas/Practica00_MarcoPolo`

### Clases y métodos introducidos
- `LinearLayout` con `android:orientation="vertical"`: coloca a sus hijas una debajo de otra.
- `TextView` y `Button`: la etiqueta con el texto y el botón que lo cambia.
- `setOnClickListener { … }`: el *listener* de click como lambda (conversión SAM).
- `setText(R.string.…)`: pone el texto a partir del `resId` de un recurso de cadena.
- Una propiedad `Boolean` de la actividad que recuerda qué palabra se está mostrando (el **estado** de la pantalla).

> **Términos explicados:** [[02 - Creación de un proyecto#10. Propiedades principales de ViewGroup|`LinearLayout` y `LayoutParams`]] · [[04 - Vistas básicas I#1. TextView|`TextView`]] · [[04 - Vistas básicas I#2. Button|`Button`]] · [[04 - Vistas básicas I#3. Listeners|*listeners* y lambdas]] · [[03 - Recursos#1. La clase Resources|`setText(resId)`]] · [[02 - Creación de un proyecto#14. ViewBinding|ViewBinding]]

#### Ejemplo simple de funcionamiento
```kotlin
var showingMarco = true
showingMarco = !showingMarco   // false: ahora toca "Polo"
showingMarco = !showingMarco   // true: vuelve a "Marco"
```

### Tutorial: cómo hacerla paso a paso

> [!tip] Cómo seguir este tutorial
> La app se construye **en trozos pequeños**, y al final de cada paso se ejecuta para comprobar que funciona. Si algo falla, sabes que está en lo último que has escrito.
> Los callouts **🆕** explican cada elemento nuevo de la práctica. Los pasos generales (crear el proyecto, activar ViewBinding…) están en la [[Guía - Cómo hacer un ejercicio de Android|guía de cómo hacer un ejercicio de Android]], que usa esta misma práctica de ejemplo.

#### Paso 1 · Plan en papel

Antes de abrir Android Studio, apunta las tres listas de la guía:

| Pregunta | Respuesta | Se convierte en… |
| --- | --- | --- |
| ¿Qué se ve? | Un texto y un botón, uno debajo del otro | `LinearLayout` vertical con `lblMessage` y `btnToggle` |
| ¿Qué pasa cuando…? | Pulso el botón → se intercambian las palabras | `setOnClickListener { toggle() }` |
| ¿Qué recuerda la app? | Qué palabra se está mostrando | `var showingMarco: Boolean` |

#### Paso 2 · Crear y preparar el proyecto

1. *Empty Views Activity* llamada `MarcoPolo`, con el paquete `es.iessaladillo.pedrojoya.marcopolo` y *Minimum SDK* API 27 ([[Guía - Cómo hacer un ejercicio de Android#Paso 2 · Crear el proyecto|guía, paso 2]]).
2. Activa ViewBinding, renombra el *layout* a `main_activity.xml` y pon el esqueleto de la actividad con `setupViews()` vacío ([[Guía - Cómo hacer un ejercicio de Android#Paso 3 · Preparar el proyecto (siempre igual)|guía, paso 3]]).

> [!success] ✅ Comprueba
> Ejecuta: sale una pantalla en blanco (o con el «Hello World!» de la plantilla) y la app **no se cierra**. Si no compila, el fallo está en la preparación y no en tu código.

#### Paso 3 · Los recursos

En `res/values/strings.xml` añade las dos palabras, y crea `res/values/dimens.xml` (clic derecho en `values` → `New -> Values Resource File`) con el relleno y el margen. El contenido está en el [[#Código fuente (proyecto `MarcoPolo`)|código fuente]].

> [!abstract] 🆕 Por qué «Marco» y «Polo» son recursos
> Las dos palabras se usan **en dos sitios**: en el XML (texto inicial) y en el Kotlin (al intercambiarlas). Si las escribieras a mano en cada sitio y luego cambiaras una, la otra quedaría desfasada. Con `@string/main_marco` y `R.string.main_marco` las dos partes leen del mismo cajón de la despensa.

#### Paso 4 · El *layout*: un `LinearLayout` vertical

Sustituye todo el contenido de `main_activity.xml` por la raíz vacía:

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/llRoot"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="@dimen/main_padding">

</LinearLayout>
```

> [!abstract] 🆕 `LinearLayout` y `android:orientation`
> Un `LinearLayout` es una **estantería**: coloca a sus hijas en fila, una tras otra.
> - `orientation="vertical"` → de arriba abajo (es lo que pide el enunciado).
> - `orientation="horizontal"` → de izquierda a derecha (la usarás en la Práctica 1 para poner cosas en la misma fila).
>
> `padding` deja un margen **interior** de 16 dp para que el contenido no quede pegado al borde de la pantalla. [[02 - Creación de un proyecto#10. Propiedades principales de ViewGroup|Ver 2 · 10. ViewGroup]]

#### Paso 5 · El texto y el botón

Dentro del `LinearLayout`, primero el `TextView` y después el `Button` (el orden en el XML es el orden en la pantalla):

```xml
<TextView
    android:id="@+id/lblMessage"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:gravity="center"
    android:text="@string/main_marco"
    android:textAppearance="@style/TextAppearance.Material3.HeadlineMedium" />

<Button
    android:id="@+id/btnToggle"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginTop="@dimen/main_btnToggle_marginTop"
    android:text="@string/main_polo" />
```

> [!abstract] 🆕 Los atributos que aparecen aquí
> | Atributo | Qué hace |
> | --- | --- |
> | `android:id="@+id/lblMessage"` | El `+` **crea** el id. Gracias a él existirá `binding.lblMessage` en el Kotlin. Sin id, la vista no está en el binding. |
> | `layout_width="match_parent"` | La vista ocupa todo el ancho de su padre. |
> | `layout_height="wrap_content"` | La vista mide lo justo para su contenido. |
> | `gravity="center"` | Centra el **texto dentro** del `TextView`. Como la vista ocupa todo el ancho, el texto queda en el centro de la pantalla. |
> | `textAppearance="@style/…HeadlineMedium"` | Aplica un estilo de texto ya hecho de Material 3 (tamaño de título). Así no hay que inventar tamaños con `textSize`. |
> | `layout_marginTop` | Separación **exterior** entre el botón y el texto de arriba. |
>
> [[04 - Vistas básicas I#1. TextView|Ver 4 · 1. TextView]] · [[04 - Vistas básicas I#2. Button|Ver 4 · 2. Button]]

> [!success] ✅ Comprueba
> Mira la pestaña **Split** del editor y ejecuta: arriba «Marco» centrado y debajo el botón «Polo». Pulsar el botón aún no hace nada, porque falta el Kotlin.

#### Paso 6 · El estado y el *listener*

En `MainActivity`, debajo de `binding`, declara el estado. Después escribe `toggle()` **encima** de `setupViews()` (primero se crea la función y luego se usa) y engancha el botón:

```kotlin
// true mientras la etiqueta muestra "Marco" (y el botón "Polo")
private var showingMarco: Boolean = true

// Se ejecuta en cada click: invierte el estado
private fun toggle() {
    showingMarco = !showingMarco
}

private fun setupViews() {
    // Lambda que se ejecuta en cada pulsación
    binding.btnToggle.setOnClickListener { toggle() }
}
```

> [!abstract] 🆕 El estado de la pantalla
> Es una propiedad de la actividad que **recuerda** algo entre click y click. Es como la libreta del camarero: no mira la mesa para adivinar qué ha pedido el cliente, lo tiene apuntado.
> No hace falta mirar qué texto tiene la etiqueta para decidir el siguiente: basta con consultar el `Boolean`, y `!` lo invierte (`true` → `false` → `true`…).

> [!abstract] 🆕 `setOnClickListener { … }`
> `OnClickListener` es una interfaz de **un solo método** (`onClick`). Por eso Kotlin deja pasar una lambda en su lugar (conversión SAM): lo que va entre llaves se ejecuta en cada pulsación.
> En Java sería `btnToggle.setOnClickListener(v -> toggle());`. [[04 - Vistas básicas I#3. Listeners|Ver 4 · 3. Listeners]]

#### Paso 7 · Pintar la pantalla según el estado

Añade `showWords()`, que es la **única** función que toca las vistas, **encima** de `toggle()` (porque `toggle()` la va a usar), y llámala desde `toggle()` y desde el final de `setupViews()`:

```kotlin
// Pinta la pantalla según el estado: etiqueta y botón con palabras opuestas
private fun showWords() {
    if (showingMarco) {
        binding.lblMessage.setText(R.string.main_marco)
        binding.btnToggle.setText(R.string.main_polo)
    } else {
        binding.lblMessage.setText(R.string.main_polo)
        binding.btnToggle.setText(R.string.main_marco)
    }
}
```

> [!abstract] 🆕 `setText(R.string.x)` y no `text = R.string.x`
> `R.string.main_marco` no es el texto, sino un **número** (`Int`) que identifica el recurso. El **método** `setText(Int)` sabe buscar el texto con ese número; la **propiedad** `text` espera un texto (`CharSequence`), así que `text = R.string.main_marco` **no compila**.
> Si tienes un texto ya hecho (`"Hola"`), puedes usar `text = "Hola"`; si tienes un recurso, usa siempre `setText(R.string…)`. [[03 - Recursos#1. La clase Resources|Ver 3 · 1. La clase Resources]]

> [!success] ✅ Comprueba
> Ejecuta y pulsa varias veces: las palabras se intercambian en cada click. Si quieres ver el estado, prueba a poner `showingMarco = false` al declararlo: la pantalla arranca al revés, porque `setupViews()` llama a `showWords()`.

Con esto la práctica está terminada. El código completo, con todos los archivos juntos, es el siguiente.

### Código fuente (proyecto `MarcoPolo`)

Proyecto *Empty Views Activity* con el paquete `es.iessaladillo.pedrojoya.marcopolo`, el *layout* renombrado a `main_activity.xml` y ViewBinding activado (`buildFeatures { viewBinding = true }` en `app/build.gradle.kts`, igual que en el [[03.1 - Ejercicios 3 Recursos|ejercicio 3.1]]).

#### `app/src/main/res/values/strings.xml`

```xml
<resources>
    <string name="app_name">MarcoPolo</string>
    <string name="main_marco">Marco</string>
    <string name="main_polo">Polo</string>
</resources>
```

#### `app/src/main/res/values/dimens.xml`

```xml
<resources>
    <dimen name="main_padding">16dp</dimen>
    <dimen name="main_btnToggle_marginTop">16dp</dimen>
</resources>
```

#### `app/src/main/res/layout/main_activity.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/llRoot"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="@dimen/main_padding">

    <TextView
        android:id="@+id/lblMessage"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center"
        android:text="@string/main_marco"
        android:textAppearance="@style/TextAppearance.Material3.HeadlineMedium" />

    <Button
        android:id="@+id/btnToggle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_btnToggle_marginTop"
        android:text="@string/main_polo" />

</LinearLayout>
```

#### `app/src/main/java/es/iessaladillo/pedrojoya/marcopolo/MainActivity.kt`

```kotlin
package es.iessaladillo.pedrojoya.marcopolo

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import es.iessaladillo.pedrojoya.marcopolo.databinding.MainActivityBinding

class MainActivity : AppCompatActivity() {

    // ViewBinding: una propiedad por cada vista con id del layout (binding.lblMessage,
    // binding.btnToggle). "by lazy" lo crea la primera vez que se usa, en onCreate()
    private val binding: MainActivityBinding by lazy {
        MainActivityBinding.inflate(layoutInflater)
    }

    // ESTADO de la pantalla: true mientras la etiqueta muestra "Marco" (y el botón "Polo").
    // Se consulta este Boolean en vez de comparar textos, que fallaría si la app se tradujera
    private var showingMarco: Boolean = true

    // Única función que toca la interfaz: pinta la pantalla según el estado.
    // La etiqueta y el botón siempre muestran palabras opuestas
    private fun showWords() {
        if (showingMarco) {
            // setText(resId) es el MÉTODO que recibe el id del recurso;
            // la propiedad "text = R.string.x" no compila, porque espera un texto y no un Int
            binding.lblMessage.setText(R.string.main_marco)
            binding.btnToggle.setText(R.string.main_polo)
        } else {
            binding.lblMessage.setText(R.string.main_polo)
            binding.btnToggle.setText(R.string.main_marco)
        }
    }

    // Se ejecuta en cada click: invierte el estado con ! (true → false → true…) y repinta.
    // Así la alternancia sigue "y así sucesivamente" sin contar los clicks
    private fun toggle() {
        showingMarco = !showingMarco
        showWords()
    }

    // Configura las vistas una sola vez, al crear la actividad
    private fun setupViews() {
        // OnClickListener tiene un solo método, así que se pasa una lambda (conversión SAM).
        // Lo que va entre llaves se ejecuta en cada pulsación
        binding.btnToggle.setOnClickListener { toggle() }
        // Pinta la pantalla según el estado inicial
        showWords()
    }

    // Punto de entrada: Android lo llama al crear la pantalla
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Muestra el layout (la raíz del binding) en la pantalla
        setContentView(binding.root)
        setupViews()
    }
}
```

### Explicación paso a paso
La explicación de cada parte del Kotlin está en los **comentarios del código**. Aquí solo queda el resumen:
1. **Recursos y *layout*.** «Marco» y «Polo» son recursos de cadena, como en el [[03.1 - Ejercicios 3 Recursos|ejercicio 3.1]]. El XML ya trae los textos iniciales, así que la pantalla sale bien antes de ejecutar código.
2. **Orden del código.** Las funciones van en el orden en que se necesitan: primero `showWords()`, después `toggle()` (que la usa), después `setupViews()` (que usa las dos) y al final `onCreate()`, que es por donde empieza Android.
3. **Idea clave.** Un estado (`showingMarco`) y una única función que pinta la pantalla a partir de él. Sobre `setText(resId)`, ver el [[03 - Recursos#1. La clase Resources|Tema 3]].

> [!tip] Prueba
> 1. Al abrir la app: la etiqueta dice «Marco» y el botón «Polo».
> 2. Primer click: la etiqueta dice «Polo» y el botón «Marco».
> 3. Segundo click: vuelve a «Marco» / «Polo», y así sucesivamente.

> [!warning] Si giras el móvil, vuelve a «Marco»
> Como en CountingClicks, girar la pantalla es un **cambio de configuración**: la actividad se crea de nuevo con `showingMarco = true`. El enunciado no pide conservar el estado. Se aprende a hacerlo en los temas «Cambio de configuración» y «ViewModel».

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Uso en la práctica |
| --- | --- | --- |
| Contenedor vertical | `<LinearLayout android:orientation="vertical">` | Etiqueta arriba y botón debajo. |
| Estado de la pantalla | `private var showingMarco: Boolean = true` | Recordar qué se muestra, sin comparar textos. |
| Invertir un `Boolean` | `showingMarco = !showingMarco` | Alternar entre los dos estados en cada click. |
| Texto desde recurso | `setText(R.string.x)` | Cambiar etiqueta y botón sin literales. |
| *Listener* de click | `btnToggle.setOnClickListener { toggle() }` | Reaccionar a cada pulsación. |

## Relaciones

- [[04 - Vistas básicas I]] · `TextView`, `Button` y *listeners*.
- [[02 - Creación de un proyecto]] · `LinearLayout`, actividad y ViewBinding.
- [[04.1 - Ejercicios 4 Vistas básicas I]] · CountingClicks, la misma estructura de estado + función que repinta.
