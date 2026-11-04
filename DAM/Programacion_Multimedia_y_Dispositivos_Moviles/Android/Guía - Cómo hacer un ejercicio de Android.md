---
asignatura: Optativa
tema: 1-8
tipo: guia
estado: completo
fecha: 2026-11-04
tags:
  - DAM/guia
  - DAM/optativa/android-guia
---

# Guía · Cómo hacer un ejercicio de Android (desde cero)

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Android (vistas), temas 1–8

> [!tip] Cómo usar esta guía
> Si acabas de empezar, léela en orden una vez entera:
> 1. Primero, **qué piezas tiene una app** (sección 1).
> 2. Después, **la receta** que sirve para cualquier ejercicio (sección 2).
> 3. Luego, **la receta aplicada** a la Práctica 0 paso a paso (sección 3).
>
> A partir de ahí, usa la **chuleta** (sección 5) y los **errores típicos** (sección 6) como consulta mientras haces ejercicios.

## Índice

- [[#1. Las piezas de una app Android]]
- [[#2. La receta: 7 pasos para cualquier ejercicio]]
- [[#3. La receta aplicada: Práctica 0 · Marco Polo]]
- [[#4. Cómo crece la receta en ejercicios más grandes]]
- [[#5. Chuleta: «quiero hacer X» → «uso Y»]]
- [[#6. Errores típicos y qué significan]]
- [[#7. Probar la app: emulador y Logcat]]
- [[#8. Checklist antes de entregar]]

---

## 1. Las piezas de una app Android

Una app de las que hacemos en clase tiene siempre las mismas cinco piezas. Piensa en **un restaurante**:

| Pieza | Archivo | Analogía | Qué hace |
| --- | --- | --- | --- |
| **Actividad** | `MainActivity.kt` | El **camarero** | Es la pantalla «viva»: lee lo que hace el usuario y decide qué mostrar. Aquí va el código Kotlin. |
| **Layout** | `res/layout/main_activity.xml` | La **decoración del salón** | Dice *qué hay* en la pantalla y *dónde*: un texto aquí, un botón debajo… No hace nada por sí solo. |
| **Recursos** | `res/values/strings.xml`, `colors.xml`, `dimens.xml` | La **despensa** | Los textos, colores y medidas, guardados con un nombre para usarlos donde haga falta. |
| **Manifiesto** | `AndroidManifest.xml` | La **licencia de apertura** | Le dice a Android qué pantallas tiene la app y cuál se abre primero. Casi nunca se toca. |
| **Gradle** | `app/build.gradle.kts` | La **lista de proveedores** | Configura cómo se construye la app y qué librerías usa. En nuestros ejercicios solo se toca una vez, para activar ViewBinding. |

> [!definition] La idea clave
> **El XML dibuja; el Kotlin reacciona.** El *layout* coloca las vistas (textos, botones, campos…), y la actividad las «engancha» con ViewBinding para cambiarlas cuando el usuario hace algo.

¿Cómo se conectan el XML y el Kotlin? Con el **id**. Si en el XML pones `android:id="@+id/btnLogin"`, en Kotlin tienes `binding.btnLogin`. Es como poner una etiqueta con nombre a cada mueble para que el camarero sepa cuál es cuál.

> [!example]- 🔗 Fuente
> [[02 - Creación de un proyecto#2. Estructura de un proyecto|02 · Estructura de un proyecto]] · [[02 - Creación de un proyecto#5. Activity|02 · Activity]] · [[02 - Creación de un proyecto#6. Especificación XML de layout|02 · Especificación XML de layout]] · [[02 - Creación de un proyecto#14. ViewBinding|02 · ViewBinding]]

---

## 2. La receta: 7 pasos para cualquier ejercicio

Todos los ejercicios y prácticas que hemos resuelto (HelloWorld, CountingClicks, Login, Marco Polo, BMI…) se han hecho con **los mismos 7 pasos**. Si los sigues en orden, nunca te quedarás sin saber por dónde seguir.

### Paso 1 · Entender el enunciado (con papel, sin ordenador)

Antes de abrir Android Studio, escribe dos listas:

1. **Qué se ve en la pantalla**: cada texto, botón, campo, imagen… → serán las **vistas** del *layout*.
2. **Qué pasa cuando…**: «cuando pulso el botón…», «cuando escribo…», «si el campo está vacío…» → serán los ***listeners*** y las **funciones** del Kotlin.

Y una tercera pregunta: **¿qué tiene que «recordar» la app?** (cuántos clicks llevo, qué palabra se muestra…) → serán las **variables de estado** de la actividad.

> [!tip] Si te dan capturas
> Cada captura es un estado de la pantalla. Compáralas de dos en dos y pregúntate: «¿qué ha hecho el usuario para pasar de esta a esta?». Cada respuesta es un *listener*.

### Paso 2 · Crear el proyecto

1. `File -> New -> New Project` → pestaña *Phone and Tablet* → **Empty Views Activity** (¡no «Empty Activity», que es Jetpack Compose!).
2. Rellena:
   - **Name**: el nombre de la app (`MarcoPolo`).
   - **Package name**: `es.iessaladillo.pedrojoya.marcopolo` (todo en minúsculas, sin espacios).
   - **Language**: Kotlin.
   - **Minimum SDK**: API 27.
   - **Build configuration language**: Kotlin DSL.
3. Pulsa `Finish` y espera a que Gradle termine. La primera vez tarda bastante, porque descarga cosas.

### Paso 3 · Preparar el proyecto (siempre igual)

Esto se hace en **todos** los proyectos. Son tres retoques a la plantilla:

**a) Activar ViewBinding.** En `app/build.gradle.kts`, dentro de `android { … }`, añade:

```kotlin
android {
    // ...
    buildFeatures {
        viewBinding = true
    }
}
```

Después pulsa **Sync Now** (aparece arriba, en una barra amarilla).

**b) Renombrar el layout.** Clic derecho en `res/layout/activity_main.xml` → `Refactor -> Rename` → `main_activity.xml`. Así la clase de ViewBinding se llamará `MainActivityBinding`, igual que la actividad.

**c) Sustituir el código de la plantilla** de `MainActivity.kt` por el esqueleto del curso:

```kotlin
class MainActivity : AppCompatActivity() {

    // El binding da acceso a todas las vistas con id del layout
    private val binding: MainActivityBinding by lazy {
        MainActivityBinding.inflate(layoutInflater)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        setupViews()
    }

    private fun setupViews() {
        // Aquí se configuran las vistas y se asignan los listeners
    }
}
```

> [!warning] El código «edge-to-edge» de la plantilla
> La plantilla trae `enableEdgeToEdge()` y un bloque `ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { … }`. Ese bloque busca una vista con id `main`. Si cambias el *layout* y esa vista ya no existe, **no compila** (`Unresolved reference 'main'`).
> - En nuestros proyectos se quita, como en los apuntes, y en el emulador de clase (Android 13) se ve bien.
> - En un **móvil con Android 15 o superior**, las apps se dibujan por debajo de la barra de estado. Si al probar en tu móvil el contenido queda tapado arriba, deja ese bloque y pon `android:id="@+id/main"` a la vista raíz de tu *layout*.

### Paso 4 · Los recursos

Antes de dibujar, mete en la «despensa» todo lo que tenga texto o medida:

- `res/values/strings.xml` → **cada texto** que se ve: `<string name="main_btnLogin">Login</string>`.
- `res/values/dimens.xml` → **cada medida**: `<dimen name="main_padding">16dp</dimen>`.
- `res/values/colors.xml` → **cada color** propio: `<color name="bmi_obesity1">#FFEF8C34</color>`.

Nombres: `main_` (la pantalla) + lo que es (`btnLogin`, `padding`…). Medidas en `dp` y textos en `sp`.

¿Por qué no escribir el texto directamente? Porque así, para traducir la app o cambiar un color, se toca **un solo sitio**.

### Paso 5 · El layout (el XML)

1. La raíz es un `LinearLayout` vertical: apila las vistas de arriba abajo. Si necesitas varias cosas **en fila**, mete dentro otro `LinearLayout` horizontal (como en la fila de unidades de la Práctica 1).
2. Cada vista lleva **siempre**:
   - `android:id="@+id/…"`: sin id, no aparece en el binding. Prefijos: `lbl` (TextView), `btn` (Button), `txt` (EditText), `til` (TextInputLayout), `img` (ImageView), `chk` (CheckBox), `rdb`/`rdg` (radio).
   - `android:layout_width` y `android:layout_height`: `match_parent` (todo el ancho del padre) o `wrap_content` (lo justo para su contenido).
3. Textos y medidas con `@string/…` y `@dimen/…`, nunca escritos a mano.
4. Mira la pestaña **Design** o **Split** del editor: verás la pantalla mientras escribes el XML.

### Paso 6 · El Kotlin (la lógica)

Dentro de la actividad, el orden es siempre el mismo:

1. **Estado**: variables `private var` con lo que la app tiene que recordar.
2. **`setupViews()`**: asigna los *listeners* («cuando pulsen este botón, llama a esta función»).
3. **Una función por acción**: `login()`, `toggle()`, `calculate()`… Cada una hace algo concreto.
4. **Una función que pinta la pantalla** a partir del estado (`showWords()`, `showResult()`…).

> [!tip] Separa «cambiar el dato» de «mostrar el dato»
> Es el truco que más simplifica:
> - El *listener* solo **cambia el estado** (`times++`).
> - Luego llama a **una** función que **pinta** según el estado (`showTimes()`).
>
> Así la pantalla nunca muestra algo que no corresponde al dato.

### Paso 7 · Ejecutar y probar

`Run -> Run 'app'` (o el ▶ verde). Prueba **cada frase del enunciado** una por una, y también lo que puede salir mal: campos vacíos, ceros, pulsar dos veces… Si la app se cierra sola, mira el **Logcat** (sección 7).

---

## 3. La receta aplicada: Práctica 0 · Marco Polo

> [!question] Enunciado (resumido)
> Un TextView y un Button en un LinearLayout vertical. Al principio: texto «Marco» y botón «Polo». Cada pulsación intercambia las dos palabras.

**Paso 1 · Papel:**
- **Se ve:** un texto y un botón → `lblMessage` (TextView) y `btnToggle` (Button).
- **Qué pasa cuando…:** se pulsa el botón → intercambiar las palabras → un *listener* que llama a `toggle()`.
- **Qué recuerda:** qué palabra se muestra ahora → `var showingMarco: Boolean = true`.

**Pasos 2 y 3 · Proyecto:** *Empty Views Activity* llamada `MarcoPolo`, ViewBinding activado y *layout* renombrado.

**Paso 4 · Recursos** (`strings.xml`):

```xml
<resources>
    <string name="app_name">MarcoPolo</string>
    <string name="main_marco">Marco</string>
    <string name="main_polo">Polo</string>
</resources>
```

**Paso 5 · Layout** (`main_activity.xml`, simplificado):

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/lblMessage"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/main_marco" />

    <Button
        android:id="@+id/btnToggle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/main_polo" />

</LinearLayout>
```

**Paso 6 · Kotlin** (dentro del esqueleto del paso 3):

```kotlin
// Estado: ¿se está mostrando "Marco"?
private var showingMarco: Boolean = true

private fun setupViews() {
    // Listener: al pulsar el botón, llama a toggle()
    binding.btnToggle.setOnClickListener { toggle() }
}

// Acción: cambia el estado y repinta
private fun toggle() {
    showingMarco = !showingMarco
    showWords()
}

// Pintar: la pantalla refleja el estado
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

**Paso 7 · Probar:** al abrir sale «Marco» / «Polo». Un click → «Polo» / «Marco». Otro → vuelve al principio.

> [!note] Fíjate en cómo encaja cada frase del enunciado
>
> | Frase del enunciado | Dónde está |
> | --- | --- |
> | «Un TextView y un Button en un LinearLayout vertical» | El XML |
> | «Inicialmente "Marco" y "Polo"» | `android:text` en el XML y `showingMarco = true` |
> | «Cuando se pulsa el botón…» | `setOnClickListener { toggle() }` |
> | «…y así sucesivamente» | `!` en `toggle()`, que alterna entre `true` y `false` |

Solución completa y explicada: [[Práctica 0 - Marco Polo]].

---

## 4. Cómo crece la receta en ejercicios más grandes

Los ejercicios más difíciles **no tienen otra receta**: tienen más filas en las listas del paso 1. Así quedan las de las otras prácticas:

| Ejercicio | Se ve (vistas) | Qué pasa cuando… (funciones) | Qué recuerda (estado) |
| --- | --- | --- | --- |
| [[04.1 - Ejercicios 4 Vistas básicas I\|CountingClicks]] | `lblTimes`, `btnClickMe` | click → `incrementTimes()` → `showTimes()` | `times: Int` |
| [[08.1 - Ejercicios 8 Gestión de la entrada de texto\|Login (Tema 8)]] | 2 etiquetas, 2 campos, botón, imagen | foco → `changeColor()`; Done o botón → `login()` | — (el texto lo guardan los campos) |
| [[Práctica 2 - Login con Snackbar y diálogo\|Práctica 2]] | 2 `TextInputLayout`, botón | botón o Done → `login()` → error / Snackbar → «SHOW» → `showUserData()` | — |
| [[Práctica 1 - BMI\|Práctica 1 · BMI]] | radios, switch, 2 campos, checkbox, 2 botones, resultado, barra, imagen | cambiar unidades → `changeUnitSystem()`; calcular → `calculate()` → `showResult()`; reset → `reset()` | `lastBmi: Double?` |

> [!tip] Cuando el ejercicio tiene «lógica de verdad», sácala a otro archivo
> En el BMI, las fórmulas (`calculateBmi()`) y la clasificación (`BmiClassification`) **no son pantalla**, así que van en sus propios archivos `.kt`, y la actividad solo los llama. Es lo mismo que hacías en Kotlin con clases y funciones: una cosa, un sitio.

---

## 5. Chuleta: «quiero hacer X» → «uso Y»

| Quiero… | Vista / herramienta | En Kotlin | Tema |
| --- | --- | --- | --- |
| Mostrar un texto | `TextView` | `binding.lbl.setText(R.string.x)` o `binding.lbl.text = "…"` | [[04 - Vistas básicas I#1. TextView\|4.1]] |
| Un botón que haga algo | `Button` | `binding.btn.setOnClickListener { hacerAlgo() }` | [[04 - Vistas básicas I#3. Listeners\|4.3]] |
| Que el usuario escriba | `TextInputLayout` + `TextInputEditText` | leer: `binding.txt.text.toString()` · escribir: `binding.txt.setText("…")` | [[04 - Vistas básicas I#7. TextInputLayout\|4.7]] |
| Leer un número escrito | (el campo anterior) | `binding.txt.text.toString().toDoubleOrNull()` → `null` si no es número | [[Práctica 1 - BMI\|Práctica 1]] |
| Marcar un error en un campo | `TextInputLayout` | `binding.til.error = getString(R.string.x)` · quitarlo: `= null` | [[04 - Vistas básicas I#7. TextInputLayout\|4.7]] |
| Un mensaje rápido | `Toast` | `Toast.makeText(this, "…", Toast.LENGTH_SHORT).show()` | [[07 - Mensajes emergentes#1. Toast\|7.1]] |
| Un mensaje con botón (deshacer, ver…) | `Snackbar` | `Snackbar.make(binding.root, R.string.x, Snackbar.LENGTH_LONG).setAction(R.string.y) { … }.show()` | [[07 - Mensajes emergentes#2. Snackbar\|7.2]] |
| Preguntar o informar con una ventana | Diálogo | `MaterialAlertDialogBuilder(this).setTitle(…).setMessage(…).setPositiveButton(…, null).create().show()` | [[07 - Mensajes emergentes#3. Diálogos\|7.3]] |
| Elegir una opción entre varias | `RadioGroup` + `RadioButton` | `binding.rdg.checkedRadioButtonId == R.id.rdbX` | [[05 - Vistas básicas II#4. RadioButton y RadioGroup\|5.4]] |
| Un sí / no | `CheckBox` o `MaterialSwitch` | `binding.chk.isChecked` | [[05 - Vistas básicas II#1. CheckBox\|5.1]] |
| Mostrar u ocultar algo | cualquier vista | `binding.vista.isVisible = true / false` | [[02 - Creación de un proyecto#8. Propiedades, métodos y atributos XML principales de View\|2.8]] |
| Una imagen | `ImageView` | `binding.img.setImageResource(R.drawable.x)` | [[04 - Vistas básicas I#4. ImageView\|4.4]] |
| Una barra de progreso | `LinearProgressIndicator` | `binding.prg.progress = 30` | [[06 - Vistas básicas III#1. Indicadores de progreso\|6.1]] |
| Que la tecla «hecho» del teclado haga algo | `android:imeOptions="actionDone"` | `setOnEditorActionListener { … }` | [[08 - Gestión de la entrada de texto#3. ImeOptions\|8.3]] |
| Reaccionar mientras escribe | (cualquier campo) | `binding.txt.doAfterTextChanged { … }` | [[08 - Gestión de la entrada de texto#4. Gestión de la escritura\|8.4]] |
| Cerrar el teclado | `SoftInputUtils.kt` de los apuntes | `hideSoftKeyboard()` | [[08 - Gestión de la entrada de texto#2. Gestión del teclado virtual\|8.2]] |

---

## 6. Errores típicos y qué significan

| Lo que ves | Por qué pasa | Solución |
| --- | --- | --- |
| `Unresolved reference 'MainActivityBinding'` | ViewBinding no está activado, o no has pulsado *Sync Now*. | Paso 3a y `File -> Sync Project with Gradle Files`. |
| `Unresolved reference 'lblMessage'` en `binding.lblMessage` | Esa vista no tiene `android:id`, o el id está escrito distinto. | Revisa el id en el XML (mayúsculas incluidas). |
| `Unresolved reference 'main'` | Queda el bloque edge-to-edge de la plantilla. | Quítalo o pon `android:id="@+id/main"` a la raíz (paso 3c). |
| `Assignment type mismatch: actual type is 'Int', but 'CharSequence!' was expected` | Has escrito `vista.text = R.string.x`. | Usa el método: `vista.setText(R.string.x)`. |
| `Assignment type mismatch` con `'Editable!'` al hacer `txt.text = "…"` | En un `EditText`, `text` es un `Editable`. | Usa `txt.setText("…")`. |
| No compila `strings.xml` con un apóstrofo | En recursos, `'` es especial. | Escríbelo como `\'` (`Can\'t`). |
| La app se cierra al pulsar un botón | Una excepción en tiempo de ejecución (por ejemplo, `toDouble()` de un texto vacío). | Mira el Logcat (sección 7); usa `toDoubleOrNull()`. |
| El Toast no aparece | Falta `.show()`. | `Toast.makeText(…).show()`. |
| Al girar el móvil se pierde lo que había | La actividad se destruye y se crea de nuevo (cambio de configuración). | Es normal por ahora; se arregla con ViewModel en temas posteriores. |
| Lo de arriba queda tapado por la barra de estado | Android 15 o superior dibuja *edge-to-edge*. | Paso 3c, aviso de edge-to-edge. |

---

## 7. Probar la app: emulador y Logcat

- **Emulador:** `Device Manager` (a la derecha) → ▶ junto a *Medium Phone*. Se crea como se explica en [[01 - Introducción a la programación para Android#6. Emulador|el Tema 1]]. Puedes escribir con el teclado del ordenador.
- **Logcat** (pestaña inferior): es el «diario» de la app. Si se cierra sola, filtra por **Error** y busca la línea `FATAL EXCEPTION`. Unas líneas más abajo aparece **tu archivo y número de línea** (`MainActivity.kt:42`): ese es el sitio del fallo.
- **Abrir los proyectos ya resueltos:** `File -> Open` → elige la carpeta del proyecto (la que contiene `settings.gradle.kts`), por ejemplo `Programas_clase/Programación Multimedia y para Dispositivos Móviles/Android/Practicas/Practica00_MarcoPolo`. Ejecútalo y compáralo con su nota: es la mejor forma de aprender.

> [!tip] Aprende «rompiendo»
> Con un proyecto que ya funciona, cambia **una sola cosa** y ejecuta: quita un id, pon un texto a mano, borra un `.show()`… Ver qué error sale y por qué enseña más que leer.

---

## 8. Checklist antes de entregar

- [ ] He hecho las tres listas del paso 1 y cada frase del enunciado tiene su sitio en el código.
- [ ] Todos los textos están en `strings.xml` y las medidas en `dimens.xml` (nada escrito a mano en el XML ni en el Kotlin).
- [ ] Todas las vistas tienen `android:id` con su prefijo (`lbl`, `btn`, `txt`, `til`…).
- [ ] La actividad sigue el esqueleto: `binding` con `by lazy`, `onCreate()` → `setupViews()`.
- [ ] Cada acción del usuario es una función con un nombre que dice lo que hace.
- [ ] He probado cada caso del enunciado y también los «malos» (vacío, cero, pulsar dos veces…).
- [ ] Si me han dado capturas, mi app se parece a ellas (textos, mayúsculas, orden de las vistas).
- [ ] No hay avisos amarillos importantes en el código (pasa el ratón por encima para leerlos).

---

## Relaciones

- Teoría: [[01 - Introducción a la programación para Android]] · [[02 - Creación de un proyecto]] · [[03 - Recursos]] · [[04 - Vistas básicas I]] · [[05 - Vistas básicas II]] · [[06 - Vistas básicas III]] · [[07 - Mensajes emergentes]] · [[08 - Gestión de la entrada de texto]]
- Ejercicios resueltos: [[03.1 - Ejercicios 3 Recursos]] · [[04.1 - Ejercicios 4 Vistas básicas I]] · [[08.1 - Ejercicios 8 Gestión de la entrada de texto]]
- Prácticas resueltas: [[Práctica 0 - Marco Polo]] · [[Práctica 1 - BMI]] · [[Práctica 2 - Login con Snackbar y diálogo]]
- Kotlin que se usa en Android: [[06 - POO I#11. Herencia|herencia]] (`: AppCompatActivity()`) · [[08 - POO III#11. Inicialización perezosa con lazy|`by lazy`]] · [[10 - Programación funcional#6. Conversión SAM|lambdas en los *listeners*]]
