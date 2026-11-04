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
