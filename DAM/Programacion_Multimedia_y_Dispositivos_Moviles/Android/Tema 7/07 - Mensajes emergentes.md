---
asignatura: Optativa
tema: 7
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-mensajes
---

# 7 · Mensajes emergentes

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 7 · Android (vistas)
> Tema anterior: [[06 - Vistas básicas III]] · Tema siguiente: [[08 - Gestión de la entrada de texto]]

> [!info] Material de referencia
> [Mensajes emergentes](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a07%20-%20Mensajes%20emergentes/)

## Índice del tema

- [[#1. Toast]]
- [[#2. Snackbar]]
- [[#3. Diálogos]]

---

## 1. Toast

Toda aplicación interactiva requiere de algún mecanismo para notificar al usuario cualquier tipo de información o evento que sea relevante. Android nos proporciona varias maneras de llevar a cabo esta notificación. En este apartado estudiaremos una de esas formas, los llamados _toasts_.

> [!definition] Toast
> Un _toast_ (brindis o tostada en español) es un mensaje emergente que se muestra en pantalla durante unos segundos y desaparece automáticamente transcurrido dicho tiempo, sin ser necesario ningún tipo de actuación por parte del usuario.

> [!note]- 🖼️ Imagen: Toast en pantalla
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/toast.jpg)

La principal ventaja de los _toast_ es que no interfieren en las acciones que esté realizando el usuario, ya que no requieren de su intervención, de manera que no debe dejar de hacer lo que estaba haciendo para atender al mensaje. De hecho, los _toasts_ ni siquiera reciben el foco mientras son mostrados.

> [!tip] Sugerencia
> Los _toasts_ son muy adecuados para mostrar mensajes rápidos y sencillos al usuario, ya que no son molestos, pero no deberían ser usados para hacer notificaciones importantes, ya que puede que el usuario no les preste demasiada atención antes de que dejen de mostrarse.

Para crear un _toast_ haremos uso de la clase `Toast` y, en concreto, de su método estático `makeText()`, que recibirá como parámetros el contexto en el que se debe mostrar, el texto del mensaje, y su duración, para la que emplearemos las constantes definidas en la clase `Toast` denominadas `LENGTH_SHORT` (duración corta) o `LENGTH_LONG` (duración larga). El método `makeText()` retorna el objeto `Toast` correspondiente, que podremos mostrar en pantalla mediante su método `show()`. Veámoslo en un ejemplo:

**Creación y mostrado de un Toast**

```kotlin
Toast.makeText(context, message, Toast.LENGTH_SHORT).show()
```

Por defecto los _toast_ aparecen en la parte inferior de la pantalla en un rectángulo gris semitransparente.

> [!warning] Aviso
> Debemos tener cuidado de no olvidar llamar al método `show()` del objeto `Toast` que hayamos creado, o de lo contrario el mensaje no se mostrará.

Como vemos, para poder crear un _toast_ debemos pasar como argumento el contexto. Pero ¿qué es eso del contexto? Lo estudiaremos a continuación.

> [!tip] El contexto ya está explicado
> Se vio en [[02 - Creación de un proyecto#4. Contexto|02 - Creación de un proyecto → 4. Contexto]]: dentro de una actividad, el contexto es la propia actividad (`this`).

## 2. Snackbar

Un _snackbar_ es un elemento para mostrar mensajes emergentes, parecido a un _toast_, pero puede incorporar aparte del mensaje, un único _text button_ que representa una acción que el usuario puede llevar a cabo.

Por ejemplo, supongamos que queremos informar de que se ha eliminado un elemento de una lista pero al mismo tiempo queremos dar la posibilidad de que el usuario deshaga la eliminación; lo más razonable es usar un _snackbar_ que muestre el mensaje de eliminación y la acción "deshacer". No debemos confundir el _snackbar_ con un diálogo de confirmación del tipo si / no, que se mostraría antes de llevar a cabo la eliminación.

> [!note]- 🖼️ Imagen: Snackbar
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/snackbar.png)

La creación de un _snackbar_ sigue un patrón parecido al de la creación de un _toast_. Usaremos el método estático `Snackbar.make()` para obtener un objeto `SnackBar`, que posteriormente podremos mostrar mediante su método `show()`.

Se puede cancelar la visualización de un Snackbar en cualquier momento mediante el método `dismiss()`.

El método `make(refViewResId, message, duration)` recibe los siguientes parámetros:

- La referencia a una vista en la que la _snackbar_ debe "alojarse". Normalmente corresponderá a la vista raíz del _layout_.
- El texto a mostrar en el `Snackbar`.
- La duración del mensaje en pantalla, definido con las constantes `Snackbar.LENGTH_SHORT` y `Snackbar.LENGTH_LONG`.

Para añadir la acción a la _snackbar_ utilizaremos su método `setAction(text, onClickListener)`, al que pasaremos como parámetros el texto del botón de acción, y un listener para su evento `onClick`, similar al de un botón normal, dentro del que podremos responder a la pulsación sobre la acción, llevando a cabo las tareas oportunas.

Podemos agregar un _callback_ para realizar alguna acción cuando el _snackbar_ se haya cerrado o cuando se muestre. Para ello usaremos el método `addCallback(callback)`, pasándole un objeto que extienda de la clase abstracta `BaseTransientBottomBar.BaseCallback<Snackbar>`, y que por tanto implemente sus método `onDismissed(snackbar, event)`, que es ejecutado cuando se cierra el _snackbar_, y el método `onShown()`, que es ejecutado cuando se muestra.

El parámetro `event` del método `onDismissed()` recibe uno de los siguientes valores, dependiendo de por qué se ha cerrado el _snackbar_:

- `DISMISS_EVENT_SWIPE`: El usuario ha hecho _swipe to dismiss_ con él.
- `DISMISS_EVENT_ACTION`: El usuario ha pulsado la acción.
- `DISMISS_EVENT_TIMEOUT`: Se ha cerrado automáticamente pasado el tiempo indicado.
- `DISMISS_EVENT_MANUAL`: Desde código se ha llamado al método `dismiss()`.

Veamos un ejemplo:

**Uso de Snackbar**

```kotlin
Snackbar.make(binding.root, getString(R.string.main_student_deleted), Snackbar.LENGTH_LONG)
        .setAction(getString(R.string.main_undo)) { addStudent(student) }
        .addCallback(object : BaseTransientBottomBar.BaseCallback<Snackbar>() {
            override fun onDismissed(transientBottomBar: Snackbar?, event: Int) {
                viewModel.onUiMessageShown()
            }

            override fun onShown(transientBottomBar: Snackbar?) {
                super.onShown(transientBottomBar)
            }
        })
        .show()
```

El botón de acción se mostrará por defecto con el _secondary color_ del tema de la aplicación. Si queremos mostrarlo en otro color, usaremos el método `setActionTextColor()` del objeto `Snackbar`, pasándole el color deseado.

Por defecto, los `Snackbar` se muestran anclados al borde inferior de la vista padre. Sin embargo, podemos anclar un `Snackbar` a cualquier vista haciendo uso de su método `setAnchorView()`, le manera que se muestre por encima de dicha vista. Esto es especialmente útil cuando usamos vistas que se muestran en la parte inferior, como `BottomAppBar` o `BottomNavigationView`, que estudiaremos más adelante.

## 3. Diálogos

Los diálogos son un mecanismo que podemos incluir en nuestras aplicaciones para mostrar o solicitar información puntual al usuario. A diferencia de los _Toast_ o los _Snackbar_, cuya función es la de informar, los diálogos están centrados en la acción contraria, la de obtener algún dato o alguna decisión que el usuario debe aportar a la aplicación. Normalmente se utilizan para solicitar la confirmación a alguna operación, pedir al usuario que seleccione entre una serie de opciones, o pedir algún dato adicional, como una fecha.

Visualmente un diálogo es una pequeña ventana que no ocupa la pantalla completa y que se usa normalmente cuando se requiere que el usuario tome una acción determinada o introduzca algún dato antes de continuar con el procesamiento normal.

La clase `Dialog` es la clase base para los diálogos, aunque debe evitarse su instanciación directa, prefiriéndose el uso de subclases específicas para determinados tipos de diálogos.

Android nos proporciona una serie de diálogos estándar ya creados, representados por sus respectivas clases (subclases de `Dialog`),

Android nos permite crear diálogos personalizados. Con objeto de que estos diálogos tengan una apariencia similar en todas las aplicaciones, Android nos proporciona la clase `AlertDialog` (subclase de `Dialog`), que contiene un objeto constructor de diálogos.

Un `AlertDialog` tiene tres zonas bien definidas:

- Área de título: Muestra el título del diálogo. Es opcional. Puede incluir un icono.
- Área de contenido: Puede mostrar un mensaje, una lista de valores o un _layout_ personalizado.
- Área de botones de acción: Cómo máximo contendrá tres botones, que suelen denominarse _positive button_ (botón positivo), _negative button_ (botón negativo) y _neutral button_ (botón neutral).

> [!note]- 🖼️ Imagen: AlertDialog
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/alertdialog.png)

Sin embargo, para crear un `AlertDialog` personalizado normalmente no instanciaremos directamente un objeto de dicha clase, sino que utilizaremos el patrón de diseño _builder_. Así, crearemos un objeto de la clase `MaterialAlertDialogBuilder`, que extiende de `AlertDialog.Builder`, que es una clase constructora que posee todos los métodos necesarios para construir el diálogo a nuestro gusto y que éste siga las caracteríticas de la guía _material design_. El constructor de la clase `MaterialAlertDialogBuilder(context)` recibe el contexto.

Usaremos métodos de este objeto _builder_ para configurar el diálogo y finalmente llamaremos a su método `create()` para que se construya el diálogo, obteniendo el objeto `Dialog` correspondiente.

La clase `MaterialAlertDialogBuilder` proporciona los siguientes métodos para configurar el área de título:

- `setIcon(drawableResId)`: Establece el icono que se mostrará en el área de título (no se recomienda su uso atendiendo a la guía de diseño _material design_).
- `setTitle(text)`: Esteblece el texto que se mostrará en el área de título.

Para el área de contenido disponemos de una serie de métodos, normalmente incompatibles entre sí, para crear distintos tipos de contenido:

- `setMessage(text)`: Muestra un mensaje simple en el área de contenido. Ideal para mostrar un texto de confirmación o un texto informativo.
- `setItems(stringArray, onClickListener)`: Muestra una lista de opciones. Recibe, por un lado, un array de de cadena correspondiente a las opciones a mostrar y, por otro lado, un _listener_ correspondiente al objeto que responderá al hecho de que el usuario haya seleccionado una de las opciones de la lista. Se trata de un diálogo de selección directa, en el sentido de que en cuanto el usuario selecciona una de las opciones el diálogo se cierra. Está sobrecargado para recibir como primer argumento el _resId_ de un recurso de array de cadenas.
- `setSingleChoiceItems(stringArray, checkedItemIndex, onClickListener)`: Muestra una lista de opciones. Recibe tres parámetros: un array de cadenas correspondiente a las opciones a mostrar, el número de opción seleccionada por defecto (`-1` si ninguna debe estar seleccionada) y un _listener_ correspondiente al objeto que responderá al hecho de que el usuario haya seleccionado una de las opciones de la lista. Se diferencia del método anterior en que cuando un usuario pulsa sobre una opción, ésta se selecciona pero el diálogo no se cierra, de manera que permite al usuario que cambie de opinión. Normalmente se combina con el método `setNeutralButton()` que veremos a continuación, para crear un botón en la zona de botones de acción para que el diálogo se cierre cuando se pulse dicho botón. Está sobrecargado para recibir como primer argumento el _resId_ de un recurso de array de cadenas.
- `setMultiChoiceItems(stringArray, checkedItemIndexArray, onClickListener)`: Similar al anterior, pero el usuario podrá seleccionar varias opciones a la vez. Recibe el array de opciones, un array booleano para indicar las opciones seleccionadas por defecto y el _listener_ que responderá cada vez que el usuario cambie el estado de selección de cada una de las opciones. Está sobrecargado para recibir como primer argumento el _resId_ de un recurso de array de cadenas.

Para el área de botones de acción también tenemos disponibles una serie de métodos de configurar. Podremos crear como máximo tres botones mediante los métodos :

- `setPositiveButton(text, onClickListener)`, para el botón positivo.
- `setNegativeButton(text, onClickListener)`, para el botón negativo y
- `setNeutralButton(text, onClickListener)` para el botón neutral.

Estos tres métodos reciben el texto que debe mostrar el botón y un _listener_ correspondiente al objeto que debe responder cuando el usuario pulse el botón correspondiente. Al tratarse de una interfaz funcional, podemos pasar como _listener_ una lambda.

Además tenemos dos métodos de `AlertDialog.Builder` con los que podemos configurar el comportamiento del diálogo respecto a su cierre:

- `setCancelable()`: para indicar si el diálogo se debe cerrar al pulsar fuera de él.
- `setOnDismissListener()`: para indicar el _listener_ que será llamado cuando se cierre el diálogo.

Una vez configurado el diálogo a través de los distintos métodos del objeto `MaterialAlertDialogBuilder` procederemos a construir el objeto `Dialog` llando al método `create()` del _builder_. Cuando queramos mostrar el díalogo, tan solo deberemos llamar al método `show()` del objeto `Dialog` correspondiente.

Veamos un ejemplo en el que se construye un diálogo que muestra un mensaje, el botón "positivo" y el "negativo", haciendo uso de `MaterialAlertDialogBuilder`:

**Creación de un diálogo usando MaterialAlertDialogBuilder**

```kotlin
val dialog: Dialog = MaterialAlertDialogBuilder(requireContext())
        .setTitle(title)
        .setMessage(message)
        .setPositiveButton("Accept") { dialog, which ->
            // ...
        }
        .setNegativeButton("Cancel") { dialog, which ->
            // ...
        }
        .create()

// Cuando queramos mostrar el diálogo
dialog.show()
```

Para saber más sobre cómo configurar el aspecto visual de los diálogos visite [https://github.com/material-components/material-components-android/blob/master/docs/components/Dialog.md](https://github.com/material-components/material-components-android/blob/master/docs/components/Dialog.md).

La librería material design nos proporciona de serie dos diálogos estándar, uno para la selección de una fecha o de un rango de fechas, conocido como `MaterialDatePicker`, y otro para la selección de una hora, denominado `MaterialTimePicker`.

> [!note]- 🖼️ Imagen: DatePickerDialog
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/datepicker.png)

El `MaterialDatePicker` dispone de un clase `Builder` con la que construir el diálogo. Con el método `setTitleText()` podemos establecer el título, con `setSelection()` la fecha que debe mostrar inicialmente el diálogo y con el método `build()` construiremos el diálogo. Si queremos añadir un listener para cuando se pulse el botón positivo, usaremos el me´todo `addOnPositiveButtonClickListener(lambda)`, al que pasaremos una lambda que recibe la selección realizada por el usuario, en forma de un `Long` correspondiente a utcMilliseconds. Cuando queramos mostrar el diálogo usaremos el método `show(supportFragmentManager, tag)`, donde `tag` corresponde a una cadena de caracteres con la que identificar el diálogo. Si quisiérmos obtener la fecha seleccionada usaremos la propiedad `selection`. Por ejemplo:

**MaterialDatePicker**

```kotlin
val datePicker = MaterialDatePicker.Builder.datePicker()
    .setTitleText("Select date")
    .setSelection(MaterialDatePicker.todayInUtcMilliseconds())
    .build()
    .apply {
        addOnPositiveButtonClickListener { selection ->
            // ...
        }
    }

// Cuando lo queramos mostrar
datePicker.show(supportFragmentManager, "TAG_DATEPICKER")
```

Para saber más sobre este diálogo visite [https://github.com/material-components/material-components-android/blob/master/docs/components/DatePicker.md](https://github.com/material-components/material-components-android/blob/master/docs/components/DatePicker.md)

El funcionamiento de `MaterialTimePickerDialog` es bastante similar. Con los métodos `setHour()` y `setMinute()` podemos establecer la hora y minutos mostrados inicialmente. Podremos usar las propiedades `hour` y `minute` posteriormente para obtener la hora y minutos seleccionados por el usuario.

> [!note]- 🖼️ Imagen: TimePickerDialog
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/timepicker.png)

**MaterialTimePicker**

```kotlin
val timePicker = MaterialTimePicker.Builder()
    .setTimeFormat(TimeFormat.CLOCK_24H)
    .setInputMode(INPUT_MODE_CLOCK)
    .setHour(12) // 0-23
    .setMinute(10) // 0-59
    .setTitleText("Select time")
    .build()
    .apply {
        addOnPositiveButtonClickListener {
            val timeString = "$hour:$minute"
        }
    }

// Cuando lo queramos mostrar
timePicker.show(supportFragmentManager, "TAG_TIMEPICKER")
```

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Toast | `Toast.makeText(context, msg, Toast.LENGTH_SHORT).show()` | Mensaje breve, sin foco ni acción; sin `show()` no aparece. |
| Snackbar | `Snackbar.make(vista, msg, Snackbar.LENGTH_LONG).setAction(texto) { … }.show()` | Mensaje con una única acción (p. ej. deshacer); `addCallback` y `setAnchorView`. |
| Motivo de cierre | `DISMISS_EVENT_SWIPE` · `_ACTION` · `_TIMEOUT` · `_MANUAL` | Llega en el parámetro `event` de `onDismissed()`. |
| AlertDialog | `MaterialAlertDialogBuilder(context)…create()` y después `show()` | Título, contenido y hasta tres botones (positivo, negativo y neutral). |
| Contenido del diálogo | `setMessage` · `setItems` · `setSingleChoiceItems` · `setMultiChoiceItems` | Mensaje, lista de selección directa, elección única o múltiple. |
| MaterialDatePicker | `MaterialDatePicker.Builder.datePicker()…build()` | `show(supportFragmentManager, tag)`; la selección es un `Long` en milisegundos UTC. |
| MaterialTimePicker | `MaterialTimePicker.Builder()…build()` | La hora elegida está en `hour` y `minute`. |

## Relaciones

- Tema anterior: [[06 - Vistas básicas III]] · Tema siguiente: [[08 - Gestión de la entrada de texto]]
- [[02 - Creación de un proyecto#4. Contexto|02 - Creación de un proyecto → 4. Contexto]] — el contexto que recibe `Toast.makeText()`.
- [[07 - POO II#Anonymous object expression|07 - POO II → Anonymous object expression]] — el *callback* del Snackbar.
- [[10 - Programación funcional#13.3 T.apply()|10 - Programación funcional → 13.3 T.apply()]] — los *pickers* se configuran con `apply`.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Mostrar un Toast y explicar cuándo no conviene usarlo.
- [ ] Mostrar un Snackbar con la acción de deshacer.
- [ ] Diferenciar Toast, Snackbar y diálogo.
- [ ] Construir un diálogo con `MaterialAlertDialogBuilder` y dos botones.
- [ ] Usar un MaterialDatePicker y un MaterialTimePicker.
