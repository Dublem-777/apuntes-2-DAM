---
asignatura: Optativa
tema: 4-8
tipo: ejercicio
estado: completo
fecha: 2026-11-04
tags:
  - DAM/ejercicio
  - DAM/optativa/android-practicas
  - DAM/optativa/ejercicios
---

# Práctica 2 · Login con Snackbar y diálogo

> [!info] Origen
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Práctica evaluable de Android (vistas)  
> Práctica anterior: [[Práctica 1 - BMI]]

> [!note] Sobre la solución
> Solución desarrollada con lo visto en los temas de Android hasta la fecha de la práctica, siguiendo el estilo del proyecto `HelloWorld` de los apuntes: paquete `es.iessaladillo.pedrojoya.<app>`, *layout* `main_activity.xml`, ViewBinding con `by lazy`, `setupViews()` y recursos con prefijo `main_`. Compilada (AGP 9.5, `compileSdk = 37`, `minSdk = 27`) y probada en el emulador *Medium Phone* con Android 13 (API 33).

---

## Práctica 2 · Login con Snackbar y diálogo

> [!question] Enunciado
> Realiza la aplicación que se muestra en las imágenes adjuntas. El único usuario válido es **Username:** `baldomero` **Password:** `llegateligero`.
> En Username debes activar el modo `clear_text`. En el Password debes activar el modo `password_toggle`.
>
> Imágenes adjuntas (estado inicial · errores · usuario no encontrado · usuario correcto · diálogo):
>
> ![[android-practica2-default.png|180]] ![[android-practica2-error.png|180]] ![[android-practica2-not-found.png|180]] ![[android-practica2-logged-in.png|180]] ![[android-practica2-dialogo.png|180]]

> [!info] Proyecto
> **Proyecto:** `PracticaLogin`  
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Android/Practicas/Practica02_Login`

> [!note] Lo que se deduce de las capturas
> - Debajo de cada campo hay un texto de ayuda, «* required», que el mensaje de error sustituye mientras dura.
> - Usuario vacío → «Can't be blank». Contraseña vacía → «Invalid password». Con algún error, el foco va al primer campo incorrecto y el teclado sigue abierto (`error.png`).
> - Campos rellenos pero que no son los de `baldomero` → Snackbar «User not found», sin acción (`not_found.png`).
> - Usuario correcto → Snackbar «User logged in» con la acción «SHOW» (`logged_in.png`), que abre el diálogo «User data» / «Logged in as baldomero» con el botón «Accept» (`dialogo.png`).
> - En los dos últimos casos el teclado está cerrado, así que se oculta al validar.
>
> Las capturas no dicen qué hace «Invalid password» con una contraseña rellena. Aquí solo se exige que no esté vacía, porque en `not_found.png` una de 4 caracteres pasa la validación.

### Clases y métodos introducidos
- `TextInputLayout` con `app:endIconMode="clear_text"` (aspa para vaciar el usuario) y `app:endIconMode="password_toggle"` (ojo para ver u ocultar la contraseña).
- `app:helperText`: el texto de ayuda «* required». Al poner `error` se sustituye por el error, y al quitarlo (`error = null`) vuelve.
- `Snackbar.make(vista, texto, duración)` y `setAction(texto) { … }`: mensaje en la parte inferior, con o sin acción.
- `MaterialAlertDialogBuilder`: diálogo con título, mensaje y botón positivo.
- `isNotBlank()`: comprueba que un texto no esté vacío ni sea solo espacios.
- `companion object` con `private const val`: el usuario y la contraseña válidos, como constantes de la clase.

> **Términos explicados:** [[04 - Vistas básicas I#7. TextInputLayout|`TextInputLayout`, `endIconMode` y `helperText`]] · [[07 - Mensajes emergentes#2. Snackbar|`Snackbar` y su acción]] · [[07 - Mensajes emergentes#3. Diálogos|`MaterialAlertDialogBuilder`]] · [[08 - Gestión de la entrada de texto#3. ImeOptions|tecla IME]] · [[08 - Gestión de la entrada de texto#4. Gestión de la escritura|`doAfterTextChanged`]] · [[06 - POO I#17. Objetos compañeros|`companion object`]] · [[08 - POO III#3. Constantes conocidas en tiempo de compilación|`const val`]]

#### Ejemplo simple de funcionamiento
```kotlin
Snackbar.make(binding.root, "User logged in", Snackbar.LENGTH_LONG)
    .setAction("Show") { /* se ejecuta al pulsar la acción */ }
    .show()
```

### Tutorial: cómo hacerla paso a paso

> [!tip] Cómo seguir este tutorial
> La app se construye **en trozos pequeños** y se ejecuta al final de cada paso (**✅ Comprueba**). Los callouts **🆕** explican lo nuevo respecto a la [[Práctica 1 - BMI|Práctica 1]]: los iconos y el texto de ayuda de los campos, el **Snackbar** y el **diálogo**. Lo que ya salió allí (`TextInputLayout`, `error`, tecla ✓, `hideSoftKeyboard()`) solo se enlaza.

#### Paso 1 · Plan en papel (a partir de las capturas)

Compara las capturas de dos en dos y pregúntate qué ha hecho el usuario para pasar de una a otra:

| De… | a… | Qué ha pasado | Se convierte en… |
| --- | --- | --- | --- |
| `default.png` | `error.png` | Login con campos vacíos | `validateFields()` pone los errores |
| `default.png` | `not_found.png` | Login con datos que no son los de `baldomero` | Snackbar sin acción |
| `default.png` | `logged_in.png` | Login correcto | Snackbar con acción «SHOW» |
| `logged_in.png` | `dialogo.png` | Pulsar «SHOW» | `showUserData()` abre el diálogo |

Estado que recordar: **ninguno**. Los campos guardan su propio texto y las credenciales válidas son constantes.

#### Paso 2 · Proyecto y recursos

1. *Empty Views Activity* `PracticaLogin` con el paquete `es.iessaladillo.pedrojoya.practicalogin`, preparada como siempre ([[Guía - Cómo hacer un ejercicio de Android#Paso 3 · Preparar el proyecto (siempre igual)|guía, paso 3]]) y con el tema `NoActionBar`, como en la [[Práctica 1 - BMI|Práctica 1]] (las capturas no tienen barra de título).
2. Copia `strings.xml` y `dimens.xml` del [[#Código fuente (proyecto `PracticaLogin`)|código fuente]].

> [!abstract] 🆕 Tres detalles de `strings.xml`
> - **El apóstrofo:** `Can\'t be blank`. En los recursos de cadena `'` es un carácter especial; sin la `\` el proyecto **no compila**.
> - **`%1$s`:** en `Logged in as %1$s` el hueco se rellena con el nombre de usuario (`getString(R.string.main_logged_in_as, username)`), igual que las cadenas con parámetros del BMI.
> - **«SHOW» en mayúsculas:** en Material 3 los botones ya no pasan el texto a mayúsculas solos, así que se escribe tal cual se quiere ver.

#### Paso 3 · El *layout*: campos con icono y texto de ayuda

Un `LinearLayout` vertical con los dos `TextInputLayout` y el botón ([[#Código fuente (proyecto `PracticaLogin`)|código fuente]]). Lo nuevo son tres atributos del marco (`til…`) y uno del cuadro (`txt…`):

```xml
<!-- Usuario -->
<com.google.android.material.textfield.TextInputLayout
    android:id="@+id/tilUsername"
    style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
    ...
    app:endIconMode="clear_text"
    app:helperText="@string/main_required">

<!-- Contraseña -->
<com.google.android.material.textfield.TextInputLayout
    android:id="@+id/tilPassword"
    ...
    app:endIconMode="password_toggle"
    app:helperText="@string/main_required">

    <com.google.android.material.textfield.TextInputEditText
        android:id="@+id/txtPassword"
        ...
        android:inputType="textPassword" />
```

> [!abstract] 🆕 `app:endIconMode`: iconos que funcionan solos
> Es un icono a la derecha del campo que el `TextInputLayout` gestiona **sin una línea de Kotlin**:
> | Valor | Icono | Qué hace |
> | --- | --- | --- |
> | `clear_text` | ✕ | Vacía el campo. Solo aparece cuando el campo tiene el foco **y** texto. |
> | `password_toggle` | 👁 | Cambia entre ver los puntos y ver el texto. Necesita que el campo sea `textPassword`. |
>
> [[04 - Vistas básicas I#7. TextInputLayout|Ver 4 · 7. TextInputLayout]]

> [!abstract] 🆕 `android:inputType="textPassword"`
> Se pone en el **cuadro** (`TextInputEditText`): oculta lo escrito con puntos y el teclado no sugiere ni recuerda palabras. Sin él, el ojo de `password_toggle` no tiene nada que ocultar.

> [!abstract] 🆕 `app:helperText` frente a `error`
> `helperText` es un texto de ayuda permanente debajo del campo («* required»). El `TextInputLayout` tiene **un solo hueco** debajo del campo:
> - Si hay `error`, se ve el error (en rojo).
> - Si `error = null`, vuelve a verse el `helperText`.
>
> Es como un cartel con dos caras: no hay que borrar ni volver a escribir «* required» a mano.

> [!success] ✅ Comprueba
> Ejecuta sin haber escrito nada de Kotlin: debajo de cada campo sale «* required». Escribe en la contraseña y pulsa el ojo: se ve el texto. Escribe en el usuario: aparece el ✕, y al pulsarlo se vacía.

#### Paso 4 · Las credenciales válidas como constantes

Al principio de `MainActivity`:

```kotlin
companion object {
    // El único usuario válido del enunciado
    private const val VALID_USERNAME = "baldomero"
    private const val VALID_PASSWORD = "llegateligero"
}
```

> [!abstract] 🆕 `companion object` con `private const val`
> El `companion object` es lo que pertenece a la **clase** y no a cada objeto (lo más parecido al `static` de Java). Dentro, `const val` declara constantes conocidas al compilar, como `private static final String VALID_USERNAME = "baldomero";` en Java. Son `private` porque solo las usa esta actividad, y así no hay textos «mágicos» sueltos en mitad de `login()`. [[06 - POO I#17. Objetos compañeros|Ver POO I · 17. Objetos compañeros]] · [[08 - POO III#3. Constantes conocidas en tiempo de compilación|POO III · 3. const val]]

#### Paso 5 · Validar los campos

```kotlin
private fun validateFields(username: String, password: String): Boolean {
    val isUsernameValid = username.isNotBlank()
    val isPasswordValid = password.isNotBlank()
    binding.tilUsername.error = if (isUsernameValid) null else getString(R.string.main_blank_username)
    binding.tilPassword.error = if (isPasswordValid) null else getString(R.string.main_invalid_password)
    if (!isUsernameValid) {
        binding.txtUsername.requestFocus()
    } else if (!isPasswordValid) {
        binding.txtPassword.requestFocus()
    }
    return isUsernameValid && isPasswordValid
}
```

Y un primer `login()` que solo lee los campos y valida, enganchado al botón con `binding.btnLogin.setOnClickListener { login() }`:

```kotlin
private fun login() {
    val username = binding.txtUsername.text.toString()
    val password = binding.txtPassword.text.toString()
    if (!validateFields(username, password)) {
        return
    }
}
```

> [!abstract] 🆕 `isNotBlank()`
> `isNotEmpty()` daría por bueno un usuario de tres espacios. `isNotBlank()` exige que haya **algún carácter que no sea espacio**: rechaza `""` y `"   "`.

> [!abstract] 🆕 `if` como expresión para el error
> `error = if (valido) null else getString(…)` pone o quita el error en una sola línea. Se calculan **los dos** errores antes de mover el foco, para que, si fallan ambos, se vean los dos a la vez (como en `error.png`).

> [!success] ✅ Comprueba
> Login con todo vacío: «Can't be blank» y «Invalid password» en rojo, en lugar de «* required», y el cursor en el usuario. Escribe un usuario y vuelve a pulsar: el error del usuario se va y el foco salta a la contraseña.

#### Paso 6 · El Snackbar «User not found»

Completa `login()`: si la validación pasa, cierra el teclado y compara con las constantes:

```kotlin
hideSoftKeyboard()
if (username == VALID_USERNAME && password == VALID_PASSWORD) {
    showLoggedIn(username)
} else {
    Snackbar.make(binding.root, R.string.main_user_not_found, Snackbar.LENGTH_SHORT).show()
}
```

`hideSoftKeyboard()` es la de `SoftInputUtils.kt`, igual que en la [[Práctica 1 - BMI#Paso 12 · Remates (errores, tecla ✓, teclado y Reset)|Práctica 1]].

> [!abstract] 🆕 `Snackbar.make(vista, texto, duración)`
> Un Snackbar es un mensaje que **sube desde abajo** y se va solo. Es el hermano mayor del `Toast`: se ve dentro de la app (no flotando encima) y puede llevar un botón.
> | Parámetro | Aquí | Por qué |
> | --- | --- | --- |
> | `vista` | `binding.root` | El Snackbar necesita una vista de la pantalla para saber **dónde** colgarse; busca desde ella hacia arriba el sitio adecuado. Sirve cualquier vista visible; la raíz es lo más cómodo. |
> | `texto` | `R.string.main_user_not_found` | Admite el id del recurso directamente. |
> | `duración` | `Snackbar.LENGTH_SHORT` | `LENGTH_SHORT` (~2 s), `LENGTH_LONG` (~3,5 s) o `LENGTH_INDEFINITE` (hasta que se cierre). |
>
> Como el `Toast`, **sin `.show()` no aparece**. [[07 - Mensajes emergentes#2. Snackbar|Ver 7 · 2. Snackbar]]

> [!tip] Mientras no tengas `showLoggedIn()`
> Para probar este paso, escribe provisionalmente `showLoggedIn()` con un `Snackbar` igual que el de error, con el texto `R.string.main_user_logged_in`.

> [!success] ✅ Comprueba
> `baldo` y `1234` → el teclado se cierra y abajo sale «User not found» unos segundos (`not_found.png`).

#### Paso 7 · Snackbar con acción y diálogo

```kotlin
private fun showLoggedIn(username: String) {
    Snackbar.make(binding.root, R.string.main_user_logged_in, Snackbar.LENGTH_LONG)
        .setAction(R.string.main_show) { showUserData(username) }
        .show()
}

private fun showUserData(username: String) {
    val dialog: Dialog = MaterialAlertDialogBuilder(this)
        .setTitle(R.string.main_user_data)
        .setMessage(getString(R.string.main_logged_in_as, username))
        .setPositiveButton(R.string.main_accept, null)
        .create()
    dialog.show()
}
```

> [!abstract] 🆕 `setAction(texto) { … }`
> Añade un **botón** al Snackbar (a la derecha, con el color principal del tema). La lambda se ejecuta al pulsarlo, y después el Snackbar se cierra solo. Se usa `LENGTH_LONG` para dar tiempo a pulsarlo.
> Las llamadas van **encadenadas** (`make(…).setAction(…).show()`) porque cada método devuelve el mismo Snackbar: es como ir rellenando un formulario y al final entregarlo con `show()`. [[07 - Mensajes emergentes#2. Snackbar|Ver 7 · 2. Snackbar]]

> [!abstract] 🆕 `MaterialAlertDialogBuilder`
> Un diálogo es una ventana pequeña **encima** de la pantalla que hay que cerrar para seguir. Se construye con el patrón *Builder*: se va configurando por partes y al final se fabrica.
> | Llamada | Qué pone |
> | --- | --- |
> | `MaterialAlertDialogBuilder(this)` | Crea el constructor. `this` es la actividad: el diálogo necesita saber a qué pantalla pertenece. |
> | `setTitle(…)` | «User data». |
> | `setMessage(…)` | «Logged in as baldomero» (cadena con parámetro). |
> | `setPositiveButton(texto, null)` | El botón «Accept». El segundo parámetro es su *listener*; `null` porque solo tiene que **cerrar**, y eso lo hace el diálogo solo. |
> | `create()` y `show()` | Fabrica el `Dialog` y lo muestra. |
>
> [[07 - Mensajes emergentes#3. Diálogos|Ver 7 · 3. Diálogos]]

> [!success] ✅ Comprueba
> `baldomero` / `llegateligero` → Snackbar «User logged in» con «SHOW» (`logged_in.png`). Pulsa «SHOW» → diálogo «User data» (`dialogo.png`). «Accept» lo cierra.

#### Paso 8 · Remates

Igual que en la [[Práctica 1 - BMI|Práctica 1]], en `setupViews()`:
1. `doAfterTextChanged { binding.tilX.error = null }` en cada campo, para que al escribir se vaya el error y vuelva «* required». [[08 - Gestión de la entrada de texto#4. Gestión de la escritura|Ver 8 · 4. Gestión de la escritura]]
2. `setOnEditorActionListener` en la contraseña, para que la tecla ✓ (o Enter) llame a `login()`. [[08 - Gestión de la entrada de texto#3. ImeOptions|Ver 8 · 3. ImeOptions]]

> [!success] ✅ Comprueba
> Repite la prueba completa que hay al final de la [[#Explicación paso a paso|explicación paso a paso]], más abajo.

Con esto la práctica está terminada. El código completo, con todos los archivos juntos, es el siguiente.

### Código fuente (proyecto `PracticaLogin`)

Proyecto *Empty Views Activity* con el paquete `es.iessaladillo.pedrojoya.practicalogin`, el *layout* renombrado a `main_activity.xml` y ViewBinding activado (`buildFeatures { viewBinding = true }` en `app/build.gradle.kts`). El tema hereda de `Theme.Material3.DayNight.NoActionBar`, como se ve en las capturas, que no tienen barra de título.

#### `app/src/main/res/values/strings.xml`

```xml
<resources>
    <string name="app_name">Login</string>
    <string name="main_tilUsername">Username</string>
    <string name="main_tilPassword">Password</string>
    <string name="main_required">* required</string>
    <!-- El apóstrofo se escapa con \ en los recursos de cadena -->
    <string name="main_blank_username">Can\'t be blank</string>
    <string name="main_invalid_password">Invalid password</string>
    <string name="main_btnLogin">Login</string>
    <string name="main_user_not_found">User not found</string>
    <string name="main_user_logged_in">User logged in</string>
    <!-- En mayúsculas, como en la captura: Material 3 ya no las pone solo -->
    <string name="main_show">SHOW</string>
    <string name="main_user_data">User data</string>
    <!-- %1$s = nombre de usuario -->
    <string name="main_logged_in_as">Logged in as %1$s</string>
    <string name="main_accept">Accept</string>
</resources>
```

#### `app/src/main/res/values/dimens.xml`

```xml
<resources>
    <dimen name="main_padding">16dp</dimen>
    <dimen name="main_field_marginTop">16dp</dimen>
    <dimen name="main_btnLogin_marginTop">16dp</dimen>
</resources>
```

#### `app/src/main/res/layout/main_activity.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/llRoot"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="@dimen/main_padding">

    <!-- clear_text: aspa a la derecha que vacía el campo -->
    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/tilUsername"
        style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="@string/main_tilUsername"
        app:endIconMode="clear_text"
        app:helperText="@string/main_required">

        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/txtUsername"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:imeOptions="actionNext"
            android:inputType="text" />
    </com.google.android.material.textfield.TextInputLayout>

    <!-- password_toggle: ojo a la derecha que muestra u oculta la contraseña -->
    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/tilPassword"
        style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_field_marginTop"
        android:hint="@string/main_tilPassword"
        app:endIconMode="password_toggle"
        app:helperText="@string/main_required">

        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/txtPassword"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:imeOptions="actionDone"
            android:inputType="textPassword" />
    </com.google.android.material.textfield.TextInputLayout>

    <Button
        android:id="@+id/btnLogin"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_btnLogin_marginTop"
        android:text="@string/main_btnLogin" />

</LinearLayout>
```

#### `app/src/main/java/es/iessaladillo/pedrojoya/practicalogin/SoftInputUtils.kt`

```kotlin
package es.iessaladillo.pedrojoya.practicalogin

import android.app.Activity
import android.content.Context
import android.view.inputmethod.InputMethodManager

// Copiada de los apuntes del Tema 8 (solo la función que se usa)
fun Activity.hideSoftKeyboard() {
    val view = currentFocus
    if (view != null) {
        val imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
        imm.hideSoftInputFromWindow(view.windowToken, 0)
    }
}
```

#### `app/src/main/java/es/iessaladillo/pedrojoya/practicalogin/MainActivity.kt`

```kotlin
package es.iessaladillo.pedrojoya.practicalogin

import android.app.Dialog
import android.os.Bundle
import android.view.KeyEvent
import android.view.inputmethod.EditorInfo
import androidx.appcompat.app.AppCompatActivity
import androidx.core.widget.doAfterTextChanged
import com.google.android.material.dialog.MaterialAlertDialogBuilder
import com.google.android.material.snackbar.Snackbar
import es.iessaladillo.pedrojoya.practicalogin.databinding.MainActivityBinding

class MainActivity : AppCompatActivity() {

    companion object {
        // El único usuario válido del enunciado
        private const val VALID_USERNAME = "baldomero"
        private const val VALID_PASSWORD = "llegateligero"
    }

    private val binding: MainActivityBinding by lazy {
        MainActivityBinding.inflate(layoutInflater)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        setupViews()
    }

    private fun setupViews() {
        // Al escribir en un campo desaparece su error y vuelve "* required"
        binding.txtUsername.doAfterTextChanged { binding.tilUsername.error = null }
        binding.txtPassword.doAfterTextChanged { binding.tilPassword.error = null }
        // Done del teclado en pantalla o Enter físico: igual que pulsar "Login"
        binding.txtPassword.setOnEditorActionListener { _, actionId, keyEvent ->
            when (actionId) {
                EditorInfo.IME_ACTION_DONE -> {
                    login()
                    true
                }
                EditorInfo.IME_NULL -> {
                    if (keyEvent?.action == KeyEvent.ACTION_DOWN) {
                        login()
                    }
                    true
                }
                else -> false
            }
        }
        binding.btnLogin.setOnClickListener { login() }
    }

    private fun login() {
        val username = binding.txtUsername.text.toString()
        val password = binding.txtPassword.text.toString()
        if (!validateFields(username, password)) {
            return
        }
        hideSoftKeyboard()
        if (username == VALID_USERNAME && password == VALID_PASSWORD) {
            showLoggedIn(username)
        } else {
            Snackbar.make(binding.root, R.string.main_user_not_found, Snackbar.LENGTH_SHORT).show()
        }
    }

    // Pone el error en cada campo vacío y devuelve true si los dos son válidos
    private fun validateFields(username: String, password: String): Boolean {
        val isUsernameValid = username.isNotBlank()
        val isPasswordValid = password.isNotBlank()
        binding.tilUsername.error = if (isUsernameValid) null else getString(R.string.main_blank_username)
        binding.tilPassword.error = if (isPasswordValid) null else getString(R.string.main_invalid_password)
        // El foco va al primer campo incorrecto
        if (!isUsernameValid) {
            binding.txtUsername.requestFocus()
        } else if (!isPasswordValid) {
            binding.txtPassword.requestFocus()
        }
        return isUsernameValid && isPasswordValid
    }

    private fun showLoggedIn(username: String) {
        Snackbar.make(binding.root, R.string.main_user_logged_in, Snackbar.LENGTH_LONG)
            .setAction(R.string.main_show) { showUserData(username) }
            .show()
    }

    private fun showUserData(username: String) {
        val dialog: Dialog = MaterialAlertDialogBuilder(this)
            .setTitle(R.string.main_user_data)
            .setMessage(getString(R.string.main_logged_in_as, username))
            .setPositiveButton(R.string.main_accept, null)
            .create()
        dialog.show()
    }
}
```

### Explicación paso a paso
1. **Los dos campos.** Son `TextInputLayout` con borde (`OutlinedBox`) y lo que pide el enunciado:
   - **Usuario** con `app:endIconMode="clear_text"`. El aspa solo aparece cuando el campo tiene foco y texto; por eso no se ve en las capturas, que tienen el foco en la contraseña.
   - **Contraseña** con `app:endIconMode="password_toggle"` y `android:inputType="textPassword"`. El ojo cambia entre puntos y texto visible (ojo tachado en `logged_in.png`).

   Ninguno de los dos iconos necesita código: los gestiona el `TextInputLayout`.
2. **«* required».** Es el `app:helperText` de cada campo. Cuando se asigna `error`, el `TextInputLayout` muestra el error en su lugar. Con `error = null` vuelve a salir el texto de ayuda, como en `not_found.png`.
3. **El apóstrofo de «Can't».** En los recursos de cadena, `'` tiene un significado especial, así que se escribe `\'`. Sin la barra, el proyecto no compila.
4. **Las credenciales.** `VALID_USERNAME` y `VALID_PASSWORD` son `const val` dentro del `companion object`: constantes de la clase, conocidas al compilar y `private` porque solo las usa `MainActivity`. Así no hay literales sueltos en mitad de `login()`.
5. **`login()` en tres pasos:**
   1. Valida. Si algún campo está vacío, `validateFields()` pone sus errores, lleva el foco al primero y `login()` termina con `return`. El teclado no se cierra, como en `error.png`.
   2. Si los dos campos tienen texto, cierra el teclado con `hideSoftKeyboard()`.
   3. Compara con el usuario válido. Si coinciden, Snackbar con acción; si no, «User not found».
6. **`validateFields()`.** `isNotBlank()` rechaza tanto el texto vacío como el que solo tiene espacios. Se calculan los dos errores **antes** de decidir el foco, para que, si fallan ambos, se vean los dos a la vez (como en `error.png`) y el foco quede en el primero.
7. **Los Snackbar.** `Snackbar.make()` recibe la vista donde se «aloja» (la raíz del *layout*), el texto como `resId` y la duración. El de error es corto y no tiene acción. El de éxito dura más (`LENGTH_LONG`) para dar tiempo a pulsar «SHOW», y con `setAction(texto) { … }` se le añade el botón. La lambda se ejecuta al pulsarlo. El texto del recurso es «SHOW», ya en mayúsculas: los botones de Material 3 respetan las mayúsculas y minúsculas de la cadena, y con «Show» saldría distinto de la captura.
8. **El diálogo.** Igual que en los apuntes: `MaterialAlertDialogBuilder(this)` configura el título, el mensaje (con el parámetro `%1$s` relleno con el usuario) y el botón positivo. `create()` construye el `Dialog` y `show()` lo muestra. El *listener* del botón es `null` porque «Accept» solo tiene que cerrar el diálogo, y eso lo hace solo.
9. **Done en la contraseña.** Llama a `login()` igual que el botón, con el mismo `when` del [[08.1 - Ejercicios 8 Gestión de la entrada de texto|proyecto Login]], para que también funcione el Enter físico.

> [!tip] Prueba
> 1. Pulsar «Login» con los campos vacíos: «Can't be blank» y «Invalid password», con el foco en el usuario (`error.png`).
> 2. Escribir en un campo con error: el error desaparece y vuelve «* required».
> 3. `baldo` y una contraseña cualquiera: Snackbar «User not found» (`not_found.png`).
> 4. `baldomero` / `llegateligero`: Snackbar «User logged in» con «SHOW» (`logged_in.png`); al pulsarlo, el diálogo «User data» (`dialogo.png`).
> 5. Pulsar el ojo de la contraseña: se ve el texto y el ojo aparece tachado. Con foco y texto en el usuario aparece el aspa, que lo vacía.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Uso en la práctica |
| --- | --- | --- |
| Iconos de campo | `app:endIconMode="clear_text"` · `"password_toggle"` | Vaciar el usuario y ver u ocultar la contraseña. |
| Texto de ayuda | `app:helperText="@string/main_required"` | «* required», que el error sustituye mientras dura. |
| Snackbar con acción | `Snackbar.make(vista, resId, duración).setAction(resId) { … }.show()` | Avisar del login y ofrecer «SHOW». |
| Diálogo | `MaterialAlertDialogBuilder(this).setTitle(…).setMessage(…).setPositiveButton(…, null).create()` | Mostrar los datos del usuario. |
| Constantes de clase | `companion object { private const val … }` | Credenciales válidas sin literales sueltos. |

## Relaciones

- [[07 - Mensajes emergentes]] · Snackbar con acción y diálogos.
- [[04 - Vistas básicas I#7. TextInputLayout|04 - Vistas básicas I → 7. TextInputLayout]] · `endIconMode`, `helperText` y `error`.
- [[08.1 - Ejercicios 8 Gestión de la entrada de texto]] · tecla Done y `hideSoftKeyboard()`, reutilizados aquí.
