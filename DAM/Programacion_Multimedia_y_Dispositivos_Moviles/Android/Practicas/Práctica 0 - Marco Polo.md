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

    private val binding: MainActivityBinding by lazy {
        MainActivityBinding.inflate(layoutInflater)
    }

    // true mientras la etiqueta muestra "Marco" (y el botón "Polo")
    private var showingMarco: Boolean = true

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        setupViews()
    }

    private fun setupViews() {
        binding.btnToggle.setOnClickListener { toggle() }
        showWords()
    }

    private fun toggle() {
        showingMarco = !showingMarco
        showWords()
    }

    private fun showWords() {
        // La etiqueta y el botón siempre muestran palabras opuestas
        if (showingMarco) {
            binding.lblMessage.setText(R.string.main_marco)
            binding.btnToggle.setText(R.string.main_polo)
        } else {
            binding.lblMessage.setText(R.string.main_polo)
            binding.btnToggle.setText(R.string.main_marco)
        }
    }
}
```

### Explicación paso a paso
1. **Recursos.** «Marco» y «Polo» son recursos de cadena (`main_marco` y `main_polo`), y el relleno y el margen son recursos de dimensión. Así el *layout* y el código no llevan ningún literal, como se practicó en el [[03.1 - Ejercicios 3 Recursos|ejercicio 3.1]].
2. **El *layout*.** Es lo que pide el enunciado: un `LinearLayout` vertical con un `TextView` (`lblMessage`) y debajo un `Button` (`btnToggle`). Los textos iniciales ya están puestos en el XML («Marco» en la etiqueta y «Polo» en el botón), así que la pantalla sale bien incluso antes de ejecutar código.
3. **El estado: `showingMarco`.** En vez de mirar qué texto tiene la etiqueta para decidir el siguiente, la actividad guarda en un `Boolean` qué palabra está mostrando. Es más seguro: comparar textos fallaría si mañana la app se tradujera (por ejemplo, con «Marco» en otro idioma), mientras que el `Boolean` no depende de cómo se escriba la palabra.
4. **`setupViews()`.** Asigna el *listener* del botón como lambda, porque `View.OnClickListener` tiene un solo método (conversión SAM). Además llama a `showWords()` para que la pantalla quede pintada según el estado inicial.
5. **`toggle()`.** Invierte el estado con `!` (si era `true` pasa a `false` y al revés) y repinta. Es lo que hace que la alternancia siga «y así sucesivamente» sin contar los clicks.
6. **`showWords()`.** Es la única función que toca la interfaz: según `showingMarco`, pone en la etiqueta una palabra y en el botón la contraria. Usa `setText(R.string.…)`, el **método** que recibe el `resId`. La propiedad `text = R.string…` no compila en Kotlin, como se explica en el [[03 - Recursos#1. La clase Resources|Tema 3]].

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
