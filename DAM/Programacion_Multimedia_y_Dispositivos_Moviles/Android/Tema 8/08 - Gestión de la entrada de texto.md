---
asignatura: Optativa
tema: 8
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-entrada-texto
---

# 8 · Gestión de la entrada de texto

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 8 · Android (vistas)
> Ejercicios: [[08.1 - Ejercicios 8 Gestión de la entrada de texto]] · Tema anterior: [[07 - Mensajes emergentes]]

> [!info] Material de referencia
> [Gestión de la entrada de texto](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a08%20-%20Gestion%20de%20la%20entrada%20de%20texto/)

## Índice del tema

- [[#1. Gestión del foco]]
- [[#2. Gestión del teclado virtual]]
- [[#3. ImeOptions]]
- [[#4. Gestión de la escritura]]
- [[#5. Ejercicio]]

---

## 1. Gestión del foco

Android nos da la posibilidad de gestionar el foco en la interfaz de usuario de nuestra actividad.

> [!definition] Foco
> El foco hace referencia a cuál de las vistas de la interfaz de usuario presente en pantalla recibirá en ese momento los eventos de entrada de datos que produzca el usuario desde un dispositivo de entrada, normalmente el teclado. En un momento dado sólo una vista puede tener el foco.

Para que el usuario tenga una referencia visual de qué vista tiene el foco en cada momento, ésta suele mostrar algún tipo de clave visual, dependiendo del tipo de vista de la que se trate. Por ejemplo, en el caso de la vista `EditText`, la línea inferior se muestra de diferente color y aparece el cursor dentro de ella.

Por defecto cualquier vista puede recibir el foco. Sin embargo, podemos cambiar este comportamiento estableciendo en la vista correspondiente el atributo `android:focusable="false"`. Los distintos tipos de vistas establecen el valor adecuado para este atributo atendiendo a si tiene sentido o no que pueda obtener el foco, por lo que en la mayoría de las ocasiones no es necesario establecerlo explícitamente.

La clase `View` proporciona una serie de atributos XML y métodos para gestionar el foco y que vamos a continuación.

En un _layout_ con distintas vistas el foco irá pasando de una vista a otra conforme el usuario introduzca los datos o interactúe con las mismas. El sistema asignará por defecto un determinado orden de foco entre las vistas del _layout_, atendiendo a su posición en el mismo, siguiendo una estrategia de izquierda a derecha y, posteriormente, de arriba a abajo.

La mayoría de las veces dicho orden será el esperado, por lo que no tendremos que preocuparnos por ello. Sin embargo, en algunas ocasiones es necesario establecer un orden distinto al predefinido por el sistema. En ese caso Android nos permite establecer para las vistas los atributos `android:nextFocusDown`, `android:nextFocusLeft`, `android:nextFocusRight` y `android:nextFocusUp`, que recibirán el `id` de la vista a la que se debe dirigir el foco, dependiendo de la dirección que se pretenda seguir.

Otro aspecto interesante es qué vista debe obtener el foco inicialmente cuando se muestra un _layout_. Para indicarla, podemos hacerlo en la propia especificación XML de _layout_, incluyendo dentro de dicha vista la etiqueta `<requestFocus />`, como vemos en el siguiente ejemplo:

**Solicitud de foco en layout**

```xml
<EditText
    android:id="@+id/txtUsername"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="@string/main_txtUsername">

    <requestFocus/>
</EditText>
```

Por otra parte, si lo que queremos es forzar a que una determinada vista obtenga el foco en base a algún evento que se ha producido, entonces desde código Java o Kotlin deberemos llamar al método `requestFocus()` de dicha vista.

Por otro lado, en algunas ocasiones queremos realizar algún tipo de tarea cuando una determinada vista obtiene o pierde el foco. Para estos casos deberemos crear un objeto _listener_ que implemente la interfaz `View.OnFocusChangeListener` y asignárselo a la vista correspondiente mediante el método `setOnFocusChangeListener(onFocusChangeListener)`. Al tratarse de una interfaz funcional (SAM, _single abstract method_), podemos usar expresiones _lambda_.

Cuando la vista gane o pierda el foco el sistema llamará al método `onFocusChange(view, hasFocus)`, pasándole, además de la vista, si ésta ha quedado en posesión del foco o no. Veamos un ejemplo:

**Listener de obtención o pérdida del foco**

```kotlin
binding.txtUsername.setOnFocusChangeListener { _: View?, hasFocus: Boolean ->
    changeColor(binding.lblUsername, hasFocus)
}
```

Debemos tener en cuenta que este _listener_ se dispara no sólo cuando el usuario interactúa con la aplicación, sino también cuando desde código se hace que la vista tome el foco.

## 2. Gestión del teclado virtual

Cuando un `EditText` toma el foco por interacción del usuario, el sistema muestra el teclado virtual para que se introduzcan los datos.

El _framework_ no proporciona ningún método sencillo para forzar que se muestre o se oculte el teclado virtual, aunque podemos crearlo nosotros. Para ello se recomienda crear un fichero kotlin con las siguientes _extension function_ de utilidad:

**`Fichero de utilidad SoftInputUtils.kt`**

```kotlin
fun Activity.showKeyboard(view: View) {
    val imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
    view.requestFocus()
    imm.showSoftInput(view, InputMethodManager.SHOW_IMPLICIT)
}

fun Activity.hideSoftKeyboard() {
    val view = currentFocus
    if (view != null) {
        val imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
        imm.hideSoftInputFromWindow(view.windowToken, 0)
    }
}
```

Al iniciar una actividad, el sistema pasa automáticamente el foco al primer `EditText` del _layout_ o a aquel para el que se ha establecido la etiqueta `requestFocus`. Sin embargo, aunque le pase el foco, NO se mostrará el teclado virtual directamente.

Si queremos que ya inicialmente se muestre el teclado virtual, tendremos que indicarlo explícitamente en el archivo de manifiesto `AndroidManfiest.xml`, a través del atributo `android:windowSoftInputMode="stateVisible"` de la etiqueta `activity` correspondiente a la actividad en cuestión.

Por otra parte, debemos tener en cuenta que es posible que al mostrar el teclado virtual se oculte la vista sobre la que estamos escribiedo, atendiendo a su posición dentro de la interfaz de usuario.

Para solucionarlo, Android nos proporciona una manera de indicar cómo debe adaptarse la interfaz de la actividad cuando la vista que ha hecho que se muestre el teclado virtual va a quedar oculta tras éste.

Así, estableceremos en el mismo atributo anterior `android:windowSoftInputMode` a alguno de los siguientes valores:

- `adjustResize`: El layout de la actividad se redimensiona todo lo que se pueda para que la vista no quede oculta.
- `adjustPan`: El layout de la actividad es desplazado hacia arriba para que la vista no quede oculta.

Si además de alguno de los valores anteriores queremos indicar el valor `stateVisible` deberemos usar el operador `|` (`or` de bits) para indicar varios valores. Así, en el siguiente ejemplo, se indican los valores `stateVisible` y `adjustPan`:

**Especificación de windowSoftInputMode**

```xml
<activity
    <!-- ... -->
    android:windowSoftInputMode="stateVisible|adjustPan" />
```

## 3. ImeOptions

Como ya comentamos, el valor del atributo `android:inputType` de un `EditText` determina qué teclas aparecerán en el teclado virtual cuando éste se muestre como consecuencia de que dicha vista haya obtenido el foco.

> [!note]- 🖼️ Imagen: Teclado virtual
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/softkeyboard.png)

Pues bien, Android añade al teclado una tecla adicional con la acción que normalmente el usuario llevará a cabo cuando haya terminado de escribir su texto en el `EditText`. Dicha acción recibe el nombre de IME (_Input Method Editor_, editor de métodos de entrada) y por defecto es proporcionada por el sistema automáticamente, mostrando un icono distinto dependiendo de la acción de la que se trate.

Sin embargo, podemos personalizar la acción a mostrar, estableciendo el atributo `android:imeOptions` de la vista a alguno de los siguientes valores:

- `actionNext`: Ir a la siguiente vista en la que se pueden introducir datos. Si queremos configurar a qué vista podemos usar el atributo `android:nextFocusDown`. ([ver icono](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/imeactionnext.png))
- `actionPrevious`: Ir a la anterior vista en la que se pueden introducir datos. ([ver icono](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/imeactionprevious.png))
- `actionGo`: Ejecutar una tarea que mostrará al usuario resultados. ([ver icono](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/imeactiongo.png))
- `actionSearch`: Buscar con el texto introducido. ([ver icono](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/imeactionsearch.png))
- `actionSend`: Enviar contenido que incluye el texto introducido. ([ver icono](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/imeactionsend.png))
- `actionDone`: Completar la edición cerrando el teclado virtual. ([ver icono](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/imeactiondone.png))

> [!warning] Aviso
> Independientemente de que hayamos establecido una acción mediante el atributo `android:imeOptions`, si el `EditText` permite la introducción de varias líneas, la tecla IME siempre mostrará la acción de salto de línea, para permitir la introducción de varias líneas.

Podemos hacer que la tecla IME, en vez de mostrar un icono, muestre un texto personalizado, para lo que emplearemos el atributo `android:imeActionLabel="texto"`.

Otro aspecto importante es que tenemos la posibilidad de establecer un objeto _listener_ para cuando el usuario pulse la tecla IME, de manera que podamos ejecutar una tarea asociada.

Para tal fin asignaremos a la vista, mediante el método `setOnEditorActionListener()`, un objeto _listener_ que implemente la interfaz `TextView.OnEditorActionListener`, de manera que cuando el usuario pulse la tecla IME se llamará al método `onEditorAction()` del _listener_, pasándole entre otros parámetros el `id` de la acción, que, si lo necesitamos, podremos comparar con alguna de las constantes de la clase `EditorInfo`, como por ejemplo `EditorInfo.IME_ACTION_DONE`. El método `onEditorAction()` debe retornar un booleano indicando si el evento ha sido consumido o no.

**Listener para tecla IME**

```kotlin
binding.txtUsername.setOnEditorActionListener { textView, actionId, keyEvent ->
    // ...
    // Se retorna `true` para indicar que el evento ha sido consumido
    true
}
```

## 4. Gestión de la escritura

En algunas ocasiones es necesario realizar alguna tarea justo en el momento en el que el usuario cambia el texto de un `EditText`, como por ejemplo para validar los datos en tiempo real conforme se escriben, o habilitar / deshabilitar algún botón dependiendo de si se ha escrito o no algo de texto en el `EditText`.

Para tal fin deberemos crear un objeto _listener_ de una clase que implemente la interfaz `TextWatcher` y asignárselo al `EditText` mediante el método `addTextChangedListener(textWatcher)`.

De esta manera, cada vez que el usuario modifique el texto del `EditText`, se llamará a alguno los siguientes métodos del _listener_:

- `afterTextChanged()`: Se llama cuando el cambio ya ha sido realizado. Recibe el texto después del cambio.
- `beforeTextChanged()`: Se llama antes de que se escriba el texto. Esto te permite saber el estado del texto actual y de la sección que será reemplazada.
- `onTextChanged()`: Se llama cuando se ha reemplazado la sección del texto. Recibe qué porción del texto viejo se reemplazó y cuantos caracteres nuevos se agregaron.

**Listener para cambio de texto en EditExt**

```kotlin
binding.txtUsername.addTextChangedListener(object : TextWatcher {
    override fun beforeTextChanged(s: CharSequence, start: Int, count: Int, after: Int) {}

    override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {}

    override fun afterTextChanged(s: Editable) {
        validateUsername(s.toString())
    }
})
```

La interfaz `TextWatcher` no es una interfaz funcional, ya que posee más de un método abstracto. Por este motivo, no podemos usar directamente una expresión lambda para expresarlo.

Sin embargo, la librería de soporte de Android proporciona un módulo que incluye la función `doAfterTextChanged(lambda)`, que hace el trabajo sucio por nosotros cuando queremos establecer el código para el evento `afterTextChanged()`, permitiéndonos indicar directamente una expresión lambda. Este método retorna el `TextWatcher` creado internamente.

Otro aspecto curioso es que el método para establecer el listener se llama `addTextChangedListener(textWatcher)`, y no `setTextChangedListener(textWatcher)`, lo cual es indicativo de que podemos tener más de un _listener_ que sea notificado cuando cambie el texto del EditText.

Cuando se produce un cambio de configuración (como estudiaremos más adelante), el sistema preserva automáticamente el texto de los EditText, de manera que cuando la actividad vuelve a estar disponible, el sistema restaura automáticamente el texto de los EditText en el método `onRestoreInstanceState()`, que es ejecutado después del `onStart()` pero antes que el `onResume()`. Como consecuencia, si para ese momento ya hemos establecido un `TextWatcher` para la vista, su código será ejecutado.

Por este motivo, a la hora de asociar a la vista correspondiente los _listener_ que reaccionan a la entrada de datos, como `OnFocusChangeListener`, `TextWatcher` en los _EditText_, `OnCheckChangedListener` de _CheckBox_, o similares, debemos decidir si hacerlo en el método `onCreate()`, es decir, antes de que se restaure el estado automáticamente, o en el `onResume()`, es decir, después de que se restaure el estado automáticamente, dependiendo de si queramos que el evento correspondiente sea ejecutado tras la restauración o no. Si lo hacemos en el `onResume()`, entonces en el método `onPause()` deberemos quitar la asociación del _listener_ con la vista, para lo que emplearemos el método `removeTextChangedListener(listener)` de la vista.

Sin embargo, para los _listeners_ cuyos eventos no pueden ser disparados durante la restauración automática, como por ejemplo `OnClickListener`, es seguro asignárselos a la vista en el método `onCreate()` de la actividad.

## 5. Ejercicio

> [!question] Ejercicio · Proyecto Login
> En este proyecto deberás desarrollar la típica pantalla de login en la que el usuario introduce el nombre de usuario y la contraseña y pulsa un botón para hacer _login_. Ten en cuenta que inicialmente el campo username es el que coge el foco, que cada vez que un campo coge el foco el texto de arriba cambia de color y lo pierde cuando dicho campo pierde el foco. Además el teclado virtual está configurado para que muestre el botón de Done, de manera que al pulsarlo se realice la misma acción que se haría al pulsar el botón Login. La conexión se simulará mostrando un mensaje emergente con el usarname y password introducidos por el usuario. Para mostrar el mensaje emergente deberás usar lo que se conoce como un Toast, que podrás mostrar con la siguiente línea de código `Toast.makeText(context, message, Toast.LENGTH_SHORT).show()`. La imagen que se muestra en el login puede ser cualquier que tu quieras.
>
> [!note]- 🖼️ Imagen: Proyecto Login en ejecución
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/prLogin.gif)

> [!success] Resuelto y explicado
> [[08.1 - Ejercicios 8 Gestión de la entrada de texto]]

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Foco | `android:focusable` · `<requestFocus/>` · `requestFocus()` | Solo una vista lo tiene a la vez; el orden se cambia con `android:nextFocusDown/Up/Left/Right`. |
| Cambio de foco | `setOnFocusChangeListener { _, hasFocus -> … }` | También salta si el foco cambia desde código. |
| Teclado al empezar | `android:windowSoftInputMode="stateVisible"` | Por defecto el primer `EditText` coge el foco pero no abre el teclado. |
| Teclado que tapa la vista | `adjustResize` · `adjustPan` | Redimensiona el *layout* o lo desplaza hacia arriba; se combinan con `\|`. |
| Mostrar / ocultar teclado | *extension functions* con `InputMethodManager` | El *framework* no trae un método directo. |
| Tecla IME | `android:imeOptions="actionDone"` · `android:imeActionLabel` | `setOnEditorActionListener { … true }` (devuelve si consume el evento). |
| TextWatcher | `addTextChangedListener(object : TextWatcher { … })` | Tres métodos ⇒ no admite lambda; atajo: `doAfterTextChanged { … }`. |
| Restauración de estado | `onRestoreInstanceState()` entre `onStart()` y `onResume()` | Los *listeners* de entrada van en `onCreate()` o en `onResume()`/`onPause()` según se quiera que salten al restaurar. |

## Relaciones

- Ejercicios del tema: [[08.1 - Ejercicios 8 Gestión de la entrada de texto]]
- Tema anterior: [[07 - Mensajes emergentes]]
- [[04 - Vistas básicas I#6. EditText|04 - Vistas básicas I → 6. EditText]] — `inputType` y el texto de un `EditText`.
- [[07 - Mensajes emergentes#1. Toast|07 - Mensajes emergentes → 1. Toast]] — el mensaje del proyecto Login.
- [[08 - POO III#5. Extension functions|08 - POO III → 5. Extension functions]] — `showKeyboard()` y `hideSoftKeyboard()`.
- [[10 - Programación funcional#6. Conversión SAM|10 - Programación funcional → 6. Conversión SAM]] — por qué `TextWatcher` no admite lambda y `OnFocusChangeListener` sí.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Hacer que una vista tenga el foco al iniciar y cambiar el orden del foco.
- [ ] Reaccionar a que una vista gane o pierda el foco.
- [ ] Configurar `windowSoftInputMode` para mostrar el teclado y que no tape la vista.
- [ ] Cambiar la tecla IME y reaccionar a su pulsación.
- [ ] Validar en tiempo real con `TextWatcher` o `doAfterTextChanged`.
- [ ] Explicar si conviene asignar un *listener* en `onCreate()` o en `onResume()`.
- [ ] Hacer el proyecto Login.
