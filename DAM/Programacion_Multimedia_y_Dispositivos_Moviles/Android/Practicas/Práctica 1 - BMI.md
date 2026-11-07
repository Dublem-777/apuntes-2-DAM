---
asignatura: Optativa
tema: 2-8
tipo: ejercicio
estado: completo
fecha: 2026-11-04
tags:
  - DAM/ejercicio
  - DAM/optativa/android-practicas
  - DAM/optativa/ejercicios
---

# Práctica 1 · BMI

> [!info] Origen
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Práctica evaluable de Android (vistas)  
> Práctica anterior: [[Práctica 0 - Marco Polo]] · Práctica siguiente: [[Práctica 2 - Login con Snackbar y diálogo]]

> [!note] Sobre la solución
> Solución desarrollada con lo visto en los temas de Android hasta la fecha de la práctica, siguiendo el estilo del proyecto `HelloWorld` de los apuntes: paquete `es.iessaladillo.pedrojoya.<app>`, *layout* `main_activity.xml`, ViewBinding con `by lazy`, `setupViews()` y recursos con prefijo `main_`. Compilada (AGP 9.5, `compileSdk = 37`, `minSdk = 27`) y probada en el emulador *Medium Phone* con Android 13 (API 33).

---

## Práctica 1 · BMI

> [!question] Enunciado
> **Práctica 1: BMI** 
>
> Realiza la aplicación del vídeo (con el aspecto de la imagen adjunta). El vídeo es uno antiguo de hace unos años. Fíjate solo en como debe ser el funcionamiento de la interfaz respecto a la interacción del usuario.
>
> Adjunto zip imágenes de clasificación de BMI.
>
> - **Clasificación BMI:** UNDERWEIGHT (menos de 18.5), NORMAL_WEIGHT (menos de 25.0), OVERWWEIGHT (menos de 30.0), OBESITY_GRADE_1 (menos de 35.0), OBESITY_GRADE_2 (menos de 40.0), OBESITY_GRADE3 (a partir de 40.0).
> - **Fórmula en sistema métrico:** `widthInKgs / (heightInMeters * heightInMeters)`.
> - **Fórmula en sistema imperial:** `widthInPounds * 703 / (heightInInches * heightInInches)`.
> - Para pasar de kgs a pounds (lbs) multiplicar por `2.20462`. Para pasar de metros a inches multiplicar por `39.3701`.
> - **Colores para clasificación BMI:** underweight (`#FFEB5123`), normal_weight (`#FF71F34C`), overweight (`#FFF0AC3C`), obesity1 (`#FFEF8C34`), obesity2 (`#FFEA5528`), obesity3 (`#FFE83523`).
> - La anchura y la altura no pueden ser 0. Si se intenta se muestra un error como el de la imagen adjunta `bmi2.png`.
>
> Aspecto pedido y error:
>
> ![[android-practica1-bmi.png|300]] ![[android-practica1-bmi-error.png|300]]

> [!info] Proyecto
> **Proyecto:** `BMI`  
> **Ruta fuente:** `/home/dublem/Documentos/Programas_clase/Programación Multimedia y para Dispositivos Móviles/Android/Practicas/Practica01_BMI`  
> **Imágenes de clasificación:** las 6 del zip adjunto (`underweight.webp` … `obesity3.webp`), copiadas tal cual en `app/src/main/res/drawable/`.

> [!note] Erratas del enunciado e interpretación
> - `widthInKgs` y `widthInPounds` deberían ser *weight* (peso), no *width* (anchura). «La anchura y la altura no pueden ser 0» se refiere también al **peso** y la altura.
> - `OVERWWEIGHT` y `OBESITY_GRADE3` rompen el patrón de los demás nombres. En el código son `OVERWEIGHT` y `OBESITY_GRADE_3`.
> - **No se tenía el vídeo**, así que el funcionamiento sale de las dos capturas y de esta interpretación:
>   - **Convert activado:** al cambiar de sistema se convierten los valores escritos (100 kg → 220.46 lb). **Desactivado:** solo cambian las unidades del sufijo.
>   - **With classification desmarcado:** solo se muestra «BMI: 34.60», sin nombre de clase, color, barra ni imagen. Si se cambia con un resultado en pantalla, se repinta al momento.
>   - **Reset:** vacía los dos campos, quita los errores y oculta el resultado. No toca el sistema de unidades ni las opciones.
>   - El máximo de la barra de progreso (45) se ha estimado midiendo la captura.
>
> Si el vídeo muestra algo distinto, solo hay que cambiar la función correspondiente de `MainActivity`.

### Clases y métodos introducidos
- `TextInputLayout` con `style="@style/Widget.Material3.TextInputLayout.OutlinedBox"` y `app:suffixText`: el campo con borde y la unidad a la derecha. Su propiedad `error` muestra el error de `bmi2.png` (borde rojo, icono y texto debajo).
- `RadioGroup` horizontal con `setOnCheckedChangeListener`: el sistema de unidades.
- `MaterialSwitch` («Convert») y `CheckBox` («With classification»): opciones que se consultan con `isChecked`.
- `LinearProgressIndicator` determinado (`android:indeterminate="false"`, `android:max`), con `progress` y `setIndicatorColor()`.
- `ImageView` con `android:adjustViewBounds="true"`: la imagen ocupa todo el ancho y su altura se ajusta para no deformarla.
- `enum class` con propiedades y un `companion object` que elige la clasificación según el BMI.
- *Top-level* `const val` y una *top-level function* para las fórmulas, separadas de la interfaz.
- `isVisible` (*extension property* de `androidx.core`) para mostrar u ocultar vistas, y `doAfterTextChanged { }` para borrar el error al escribir.
- Recurso de entero (`@integer/main_bmi_max`), de color (uno por clasificación) y cadenas con parámetros (`%1$.2f`).

> **Términos explicados:** [[04 - Vistas básicas I#7. TextInputLayout|`TextInputLayout`]] · [[05 - Vistas básicas II#4. RadioButton y RadioGroup|`RadioGroup`]] · [[05 - Vistas básicas II#3. Switch|`MaterialSwitch`]] · [[05 - Vistas básicas II#1. CheckBox|`CheckBox`]] · [[06 - Vistas básicas III#1. Indicadores de progreso|indicadores de progreso]] · [[04 - Vistas básicas I#4. ImageView|`ImageView`]] · [[08 - Gestión de la entrada de texto#3. ImeOptions|tecla IME]] · [[08 - Gestión de la entrada de texto#4. Gestión de la escritura|`doAfterTextChanged`]] · [[03 - Recursos#8. Recursos de entero|recursos de entero]] · [[03 - Recursos#9. Recursos de color|de color]] · [[03 - Recursos#6. Recursos de cadena con parámetros|cadenas con parámetros]] · [[07 - POO II#Enumeraciones|enumeraciones]] · [[06 - POO I#17. Objetos compañeros|`companion object`]] · [[08 - POO III#1. Top-level functions|*top-level functions*]] · [[08 - POO III#3. Constantes conocidas en tiempo de compilación|`const val`]] · [[08 - POO III#6. Extension properties|*extension properties*]] · [[10 - Programación funcional#13.4 T.let()|`let`]]

#### Ejemplo simple de funcionamiento
```kotlin
// 100 kg y 1.70 m en sistema métrico
val bmi = 100 / (1.70 * 1.70)                 // 34.60...
val classification = BmiClassification.from(bmi) // OBESITY_GRADE_1 (entre 30 y 35)
```

### Tutorial: cómo hacerla paso a paso

> [!tip] Cómo seguir este tutorial
> La app se construye **en trozos pequeños**: primero la pantalla de arriba abajo, después la lógica que no es pantalla y, por último, la actividad, una acción cada vez. Al final de cada paso hay un **✅ Comprueba** para ejecutar y ver que funciona antes de seguir.
> Los callouts **🆕** explican cada elemento nuevo respecto a la [[Práctica 0 - Marco Polo|Práctica 0]]. Los pasos generales están en la [[Guía - Cómo hacer un ejercicio de Android|guía de cómo hacer un ejercicio de Android]].

#### Paso 1 · Plan en papel

| Pregunta | Respuesta | Se convierte en… |
| --- | --- | --- |
| ¿Qué se ve? | Título · fila «Unit system» con 2 radios y un *switch* · 2 campos con unidad · *checkbox* · 2 botones · resultado de color · barra · imagen | Un `LinearLayout` vertical con dos filas horizontales dentro |
| ¿Qué pasa cuando…? | Calculo → valido y muestro · cambio de sistema → cambio unidades (y convierto) · marco/desmarco clasificación → repinto · Reset → vacío | `calculate()` · `changeUnitSystem()` · `showResult()` · `reset()` |
| ¿Qué recuerda la app? | El último BMI calculado, para repintarlo sin recalcular | `var lastBmi: Double?` |
| ¿Qué lógica **no** es pantalla? | La fórmula y la clasificación | `Bmi.kt` y `BmiClassification.kt` |

#### Paso 2 · Crear el proyecto, quitar la barra de título y copiar las imágenes

1. *Empty Views Activity* `BMI` con el paquete `es.iessaladillo.pedrojoya.bmi`, ViewBinding, *layout* `main_activity.xml` y el esqueleto con `setupViews()` ([[Guía - Cómo hacer un ejercicio de Android#Paso 3 · Preparar el proyecto (siempre igual)|guía, paso 3]]).
2. En `res/values/themes.xml`, haz que el tema herede de `Theme.Material3.DayNight.NoActionBar`:
   ```xml
   <style name="Theme.App" parent="Theme.Material3.DayNight.NoActionBar" />
   ```
   (el nombre del estilo puede ser otro en tu plantilla, por ejemplo `Theme.BMI`; cambia solo el `parent`).
3. Descomprime el zip y copia las 6 imágenes en `res/drawable`: en el panel *Project*, pon la vista **Project** (no *Android*), entra en `app/src/main/res/drawable` y pega con `Ctrl + V`.

> [!abstract] 🆕 Tema sin barra de título (`NoActionBar`)
> El **tema** es el «uniforme» de toda la app: colores, tipografía y si hay barra de título arriba. En la captura no hay barra, y el título «BMI Calculator» forma parte del *layout*. Con `NoActionBar` la barra desaparece en todas las pantallas sin tocar el Kotlin. [[03 - Recursos#12. Recursos de tema|Ver 3 · 12. Recursos de tema]]

> [!abstract] 🆕 Imágenes propias en `res/drawable`
> Cada archivo de `drawable` genera una constante `R.drawable.<nombre>`: `obesity1.webp` → `R.drawable.obesity1`. Por eso el nombre del archivo **solo** puede tener minúsculas, números y `_` (nada de guiones, espacios ni mayúsculas), y la extensión no forma parte del nombre. Si un nombre no vale, el proyecto no compila. [[03 - Recursos#2. Recursos drawable|Ver 3 · 2. Recursos drawable]]

> [!success] ✅ Comprueba
> Ejecuta: pantalla vacía **sin** barra de título. En el *Project* ves las 6 imágenes en `drawable`, y en el Kotlin puedes escribir `R.drawable.` y el autocompletado te las ofrece.

#### Paso 3 · Los recursos

Copia `strings.xml`, `colors.xml`, `integers.xml` y `dimens.xml` del [[#Código fuente (proyecto `BMI`)|código fuente]]. Hay tres tipos de recurso que no habían salido en la Práctica 0:

> [!abstract] 🆕 Recursos de color (`colors.xml`)
> Los 6 colores del enunciado, con nombre: `<color name="bmi_obesity1">#FFEF8C34</color>`. El formato es `#AARRGGBB`: los dos primeros dígitos son la opacidad (`FF` = opaco). En el Kotlin se leen con `ContextCompat.getColor(this, R.color.bmi_obesity1)`, que devuelve el color como `Int`. [[03 - Recursos#9. Recursos de color|Ver 3 · 9. Recursos de color]]

> [!abstract] 🆕 Recurso de entero (`integers.xml`)
> `<integer name="main_bmi_max">45</integer>` es el máximo de la barra. Se usa en el XML con `@integer/main_bmi_max`. Es un número «de configuración» con nombre, igual que un `dimen` pero sin unidades. [[03 - Recursos#8. Recursos de entero|Ver 3 · 8. Recursos de entero]]

> [!abstract] 🆕 Cadenas con parámetros
> `BMI: %1$.2f %2$s` es una plantilla con dos huecos:
> - `%1$.2f` → el **1.er** argumento, decimal con **2** decimales (`34.6021…` → `34.60`).
> - `%2$s` → el **2.º** argumento, como texto.
>
> Se rellena en el Kotlin con `getString(R.string.main_bmi_classification, bmi, "Obesity class I")`. Es lo mismo que `String.format` de Java, pero desde un recurso. [[03 - Recursos#6. Recursos de cadena con parámetros|Ver 3 · 6. Recursos de cadena con parámetros]]

#### Paso 4 · *Layout* (1/3): título y fila del sistema de unidades

Dentro del `LinearLayout` vertical raíz, pon el `TextView` del título y, debajo, **otro `LinearLayout`, horizontal**, para que la etiqueta, los radios y el *switch* queden en la misma fila:

```xml
<LinearLayout
    android:id="@+id/llUnitSystem"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginTop="@dimen/main_section_marginTop"
    android:gravity="center_vertical"
    android:orientation="horizontal">

    <TextView
        android:id="@+id/lblUnitSystem"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/main_lblUnitSystem" />

    <RadioGroup
        android:id="@+id/rdgUnitSystem"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:checkedButton="@+id/rdbMetric"
        android:orientation="horizontal">

        <RadioButton
            android:id="@+id/rdbMetric"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/main_rdbMetric" />

        <RadioButton
            android:id="@+id/rdbImperial"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/main_rdbImperial" />
    </RadioGroup>

    <com.google.android.material.materialswitch.MaterialSwitch
        android:id="@+id/swtConvert"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="@dimen/main_swtConvert_marginStart"
        android:checked="true"
        android:text="@string/main_swtConvert" />
</LinearLayout>
```

> [!abstract] 🆕 `LinearLayout` anidados
> Un `LinearLayout` solo sabe ir en **una** dirección. Para una pantalla «vertical con alguna fila», se mete un `LinearLayout` horizontal **como hija** del vertical: es una balda dentro de la estantería. `gravity="center_vertical"` alinea por el centro a las hijas de la fila, para que el texto no quede más alto que los radios.

> [!abstract] 🆕 `RadioGroup` + `RadioButton`
> Los `RadioButton` sueltos se pueden marcar todos a la vez. Metidos en un `RadioGroup`, el grupo garantiza que **solo uno** esté marcado (como los botones de una radio antigua: al pulsar uno, salta el otro).
> - `android:orientation="horizontal"`: el `RadioGroup` es un `LinearLayout` especial, así que también tiene orientación.
> - `android:checkedButton="@+id/rdbMetric"`: cuál sale marcado al empezar.
>
> [[05 - Vistas básicas II#4. RadioButton y RadioGroup|Ver 5 · 4. RadioButton y RadioGroup]]

> [!abstract] 🆕 `MaterialSwitch`
> Un interruptor de sí/no. No es una vista de Android, sino de la librería **Material**, así que en el XML se escribe con el **nombre completo de la clase** (`com.google.android.material.materialswitch.MaterialSwitch`). Truco: escribe `<MaterialSw` y deja que el autocompletado ponga el resto. `android:checked="true"` lo deja activado al empezar. [[05 - Vistas básicas II#3. Switch|Ver 5 · 3. Switch]]

> [!success] ✅ Comprueba
> Ejecuta: el título y, debajo, la fila «Unit system: ◉ Metric ○ Imperial  Convert ⏽». Al pulsar *Imperial* se desmarca *Metric* sin escribir código: lo hace el `RadioGroup`.

#### Paso 5 · *Layout* (2/3): los campos con unidad

Debajo de la fila, los dos campos. Cada uno son **dos vistas**, una dentro de otra:

```xml
<com.google.android.material.textfield.TextInputLayout
    android:id="@+id/tilWeight"
    style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginTop="@dimen/main_section_marginTop"
    android:hint="@string/main_tilWeight"
    app:suffixText="@string/main_kg">

    <com.google.android.material.textfield.TextInputEditText
        android:id="@+id/txtWeight"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:imeOptions="actionNext"
        android:inputType="numberDecimal">

        <requestFocus />
    </com.google.android.material.textfield.TextInputEditText>
</com.google.android.material.textfield.TextInputLayout>
```

El de la altura es igual, con los ids `tilHeight`/`txtHeight`, el sufijo `@string/main_m`, `imeOptions="actionDone"` y sin `<requestFocus />`. Para usar `app:` añade a la raíz `xmlns:app="http://schemas.android.com/apk/res-auto"`.

> [!abstract] 🆕 `TextInputLayout` + `TextInputEditText`
> Piensa en un **marco y su cuadro**:
> - El `TextInputEditText` (dentro, id `txt…`) es el cuadro: donde se escribe. De él se lee el texto.
> - El `TextInputLayout` (fuera, id `til…`) es el marco: dibuja el borde, la etiqueta flotante (`hint`), el sufijo y el **error**.
>
> Por eso el texto se lee de `binding.txtWeight` y el error se pone en `binding.tilWeight`. [[04 - Vistas básicas I#7. TextInputLayout|Ver 4 · 7. TextInputLayout]]

> [!abstract] 🆕 Los atributos del campo
> | Atributo | Qué hace |
> | --- | --- |
> | `style="@style/…OutlinedBox"` | El campo con borde de la captura (sin él sale el de fondo relleno). `style` va **sin** `android:`. |
> | `app:suffixText` | Texto fijo a la derecha, dentro del campo: la unidad. Se cambia desde el Kotlin con `til.suffixText = …`. |
> | `android:inputType="numberDecimal"` | Abre el teclado numérico con separador decimal y no deja escribir letras. |
> | `android:imeOptions` | Qué tecla sale abajo a la derecha del teclado: `actionNext` (pasa al siguiente campo) o `actionDone` (✓, terminar). [[08 - Gestión de la entrada de texto#3. ImeOptions\|Ver 8 · 3. ImeOptions]] |
> | `<requestFocus />` | El cursor empieza en este campo. [[08 - Gestión de la entrada de texto#1. Gestión del foco\|Ver 8 · 1. Foco]] |

> [!success] ✅ Comprueba
> Ejecuta: dos campos con borde, «kg» y «m» a la derecha. Al tocar uno, el teclado es numérico; en el peso sale la tecla «→» (siguiente) y en la altura «✓».

#### Paso 6 · *Layout* (3/3): opciones, botones y resultado oculto

Añade el `CheckBox`, la fila horizontal de los dos botones y las tres vistas del resultado (`lblResult`, `prgBmi`, `imgClassification`), copiadas del [[#Código fuente (proyecto `BMI`)|código fuente]]. Lo nuevo está en el resultado:

```xml
<com.google.android.material.progressindicator.LinearProgressIndicator
    android:id="@+id/prgBmi"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:indeterminate="false"
    android:max="@integer/main_bmi_max"
    android:visibility="gone"
    app:trackThickness="@dimen/main_prgBmi_thickness" />

<ImageView
    android:id="@+id/imgClassification"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:adjustViewBounds="true"
    android:contentDescription="@string/main_imgClassification"
    android:visibility="gone" />
```

> [!abstract] 🆕 `CheckBox`
> Casilla de sí/no, como el *switch*, pero con aspecto de casilla. `android:checked="true"` la deja marcada al empezar y en el Kotlin se consulta con `isChecked`. [[05 - Vistas básicas II#1. CheckBox|Ver 5 · 1. CheckBox]]

> [!abstract] 🆕 `android:visibility="gone"`
> El resultado no debe verse hasta calcular. Hay tres valores:
> - `visible`: se ve (por defecto).
> - `invisible`: no se ve, pero **deja su hueco**.
> - `gone`: no se ve **ni ocupa sitio**, como si no estuviera.
>
> Se usa `gone` para que no quede un hueco en blanco. En el Kotlin se cambia con `vista.isVisible = true/false`. [[02 - Creación de un proyecto#8. Propiedades, métodos y atributos XML principales de View|Ver 2 · 8. Atributos de View]]

> [!abstract] 🆕 `LinearProgressIndicator` determinado
> Una barra de progreso. Con `indeterminate="false"` no da vueltas sin fin, sino que se llena **hasta un valor**: `max` es el tope (45) y `progress` lo lleno (si el BMI es 34.6 → 35 de 45). `app:trackThickness` es el grosor. [[06 - Vistas básicas III#1. Indicadores de progreso|Ver 6 · 1. Indicadores de progreso]]

> [!abstract] 🆕 `ImageView` con `adjustViewBounds`
> La imagen tiene `width="match_parent"` (todo el ancho) y `height="wrap_content"`. `adjustViewBounds="true"` le dice a la vista que **ajuste su alto a la proporción de la imagen**, para que no quede deformada ni con bandas vacías arriba y abajo. `contentDescription` es el texto que lee el lector de pantalla para personas ciegas. [[04 - Vistas básicas I#4. ImageView|Ver 4 · 4. ImageView]]

> [!success] ✅ Comprueba
> Ejecuta: la pantalla es igual que la captura **hasta los botones**, y debajo no hay nada. En la pestaña *Design*, si cambias un momento `gone` por `visible`, verás dónde aparecerá la barra.

#### Paso 7 · La lógica que no es pantalla: `Bmi.kt` y `BmiClassification.kt`

Clic derecho en el paquete → `New -> Kotlin Class/File`:
- `Bmi.kt` como **File**, con las constantes y `calculateBmi()`.
- `BmiClassification.kt` como **Enum class**.

Su código está en el [[#Código fuente (proyecto `BMI`)|código fuente]].

> [!abstract] 🆕 *Top-level* `const val` y *top-level function*
> En Kotlin no hace falta meter todo en una clase: `KG_TO_LB` y `calculateBmi()` están **sueltas en el archivo** y se usan desde cualquier sitio del paquete sin crear objetos. Es lo adecuado para una fórmula, que no guarda estado. `const val` indica una constante conocida al compilar (como `static final` en Java). [[08 - POO III#1. Top-level functions|Ver POO III · 1. Top-level functions]] · [[08 - POO III#3. Constantes conocidas en tiempo de compilación|3. const val]]

> [!abstract] 🆕 `enum class` que guarda ids de recursos
> Cada clasificación necesita **tres cosas**: su nombre, su color y su imagen. En lugar de tres `when` repartidos por la actividad, el `enum` las guarda juntas:
> ```kotlin
> OBESITY_GRADE_1(R.string.bmi_obesity1, R.color.bmi_obesity1, R.drawable.obesity1),
> ```
> Los tres son `Int` porque `R.string.x`, `R.color.x` y `R.drawable.x` son **números que identifican el recurso**, no el recurso en sí. Es como guardar la referencia del almacén en vez de la caja.
> `from(bmi)` está en el `companion object` para llamarla sobre el tipo: `BmiClassification.from(34.6)`. [[07 - POO II#Enumeraciones|Ver POO II · Enumeraciones]] · [[06 - POO I#17. Objetos compañeros|POO I · 17. Objetos compañeros]]

#### Paso 8 · Calcular con validación

En `MainActivity`, empieza solo con el botón «Calculate BMI». Primero una función que lee un campo y otra que lo valida:

```kotlin
// Admite coma o punto decimal; devuelve null si no es un número
private fun readValue(field: TextInputEditText): Double? =
    field.text.toString().replace(',', '.').toDoubleOrNull()

private fun validate(field: TextInputEditText, layout: TextInputLayout, errorResId: Int): Double? {
    val value = readValue(field)
    return if (value == null || value <= 0.0) {
        layout.error = getString(errorResId)
        null
    } else {
        layout.error = null
        value
    }
}
```

Y `calculate()`, que valida los dos campos y, si alguno falla, lleva el foco a él (la versión completa también cierra el teclado y oculta el resultado):

```kotlin
private fun calculate() {
    val weight = validate(binding.txtWeight, binding.tilWeight, R.string.main_invalid_weight)
    val height = validate(binding.txtHeight, binding.tilHeight, R.string.main_invalid_height)
    if (weight == null || height == null) {
        val wrongField = if (weight == null) binding.txtWeight else binding.txtHeight
        wrongField.requestFocus()
        wrongField.selectAll()
        return
    }
    val bmi = calculateBmi(weight, height, isMetric)
    lastBmi = bmi
    showResult(bmi)
}
```

Engánchalo en `setupViews()` con `binding.btnCalculate.setOnClickListener { calculate() }`.

> [!abstract] 🆕 `toDoubleOrNull()`
> `"abc".toDouble()` lanza una excepción y **cierra la app**. `toDoubleOrNull()` devuelve `null` si el texto no es un número (o está vacío), y así se comprueba con un simple `if`. El `replace(',', '.')` es porque un móvil en español escribe «1,70», y Kotlin solo entiende «1.70».

> [!abstract] 🆕 El error de un `TextInputLayout`
> `layout.error = "texto"` pinta el borde rojo, el icono ⓘ y el mensaje debajo, todo a la vez (lo de `bmi2.png`). `layout.error = null` lo quita. Se pone en el **marco** (`til…`), no en el cuadro (`txt…`). [[04 - Vistas básicas I#7. TextInputLayout|Ver 4 · 7. TextInputLayout]]

> [!abstract] 🆕 `requestFocus()` y `selectAll()`
> `requestFocus()` pone el cursor en el campo; `selectAll()` selecciona su texto, para que lo que escriba el usuario lo sustituya directamente. Es lo que se ve en la captura del error. [[08 - Gestión de la entrada de texto#1. Gestión del foco|Ver 8 · 1. Gestión del foco]]

> [!abstract] 🆕 Propiedad calculada `isMetric`
> ```kotlin
> private val isMetric: Boolean
>     get() = binding.rdgUnitSystem.checkedRadioButtonId == R.id.rdbMetric
> ```
> No guarda nada: cada vez que se lee, pregunta al `RadioGroup` qué radio está marcado (`checkedRadioButtonId`) y lo compara con el id de *Metric*. Así nunca se queda desfasada.

> [!tip] Mientras no tengas `showResult()`
> Para probar este paso, puedes escribir provisionalmente `showResult()` con una sola línea: `binding.lblResult.text = getString(R.string.main_bmi, bmi)` y `binding.lblResult.isVisible = true`. En el paso siguiente la completas.

> [!success] ✅ Comprueba
> - Altura `0` → «Invalid height» en rojo y el `0` seleccionado.
> - Los dos vacíos → los dos errores a la vez y el foco en el peso.
> - `100` y `1.70` → «BMI: 34.60».

#### Paso 9 · Mostrar el resultado con su clasificación

Completa `showResult()` como en el [[#Código fuente (proyecto `BMI`)|código fuente]]. El corazón es esto:

```kotlin
val classification = BmiClassification.from(bmi)
val color = ContextCompat.getColor(this, classification.colorResId)
binding.lblResult.text = getString(
    R.string.main_bmi_classification, bmi, getString(classification.labelResId)
)
binding.lblResult.setBackgroundColor(color)
binding.prgBmi.setIndicatorColor(color)
binding.prgBmi.progress = bmi.roundToInt()
binding.imgClassification.setImageResource(classification.imageResId)
```

> [!abstract] 🆕 Del id de recurso al valor
> El `enum` guarda **ids** (`Int`); cada vista pide el suyo a su manera:
> | Recurso | Cómo se convierte | Para qué |
> | --- | --- | --- |
> | Color | `ContextCompat.getColor(this, id)` | Color real para `setBackgroundColor()` y `setIndicatorColor()`. |
> | Cadena | `getString(id)` | El nombre de la clase para meterlo en la plantilla. |
> | Imagen | `setImageResource(id)` | La vista ya acepta el id directamente. |
>
> ¡Ojo! `setBackgroundColor(R.color.x)` compila (los dos son `Int`; Android Studio solo lo subraya) pero pinta un color sin sentido: hay que pasar por `ContextCompat.getColor`.

> [!abstract] 🆕 `progress` e `isVisible`
> - `progress` es un `Int`, así que el BMI (`Double`) se redondea con `roundToInt()`.
> - `isVisible = true/false` es una *extension property* de `androidx.core`: equivale a `visibility = View.VISIBLE` / `View.GONE`, pero más corto. [[08 - POO III#6. Extension properties|Ver POO III · 6. Extension properties]]

> [!success] ✅ Comprueba
> `100` y `1.70`: «BMI: 34.60 Obesity class I» con fondo naranja, barra naranja hasta ~35 y la imagen con la flecha en *Obese class I*, como la captura.

#### Paso 10 · El *checkbox* «With classification»

En `showResult()`, consulta `binding.chkClassification.isChecked` para mostrar u ocultar la barra y la imagen (y poner el fondo neutro si no hay clasificación). Para que cambie **al momento** al marcarlo con un resultado en pantalla, añade en `setupViews()`:

```kotlin
binding.chkClassification.setOnCheckedChangeListener { _, _ ->
    lastBmi?.let { showResult(it) }
}
```

> [!abstract] 🆕 `setOnCheckedChangeListener` y `?.let`
> Se ejecuta cada vez que la casilla cambia. Sus dos parámetros (la vista y si está marcada) no hacen falta, por eso se escriben `_, _`.
> `lastBmi?.let { showResult(it) }` significa «si hay un BMI guardado, repíntalo; si es `null`, no hagas nada». `it` es el valor ya sin `null`. [[05 - Vistas básicas II#1. CheckBox|Ver 5 · 1. CheckBox]] · [[10 - Programación funcional#13.4 T.let()|Kotlin · let]]

> [!success] ✅ Comprueba
> Con un resultado en pantalla, desmarca la casilla: queda solo «BMI: 34.60» con fondo morado, sin barra ni imagen. Márcala: vuelve todo.

#### Paso 11 · Cambiar el sistema de unidades

En `setupViews()`:

```kotlin
binding.rdgUnitSystem.setOnCheckedChangeListener { _, _ -> changeUnitSystem() }
```

`changeUnitSystem()` cambia los sufijos con `til.suffixText = getString(…)` y, si `binding.swtConvert.isChecked`, convierte los valores con `convert()`. Al final oculta el resultado, que ya no corresponde a las unidades.

> [!abstract] 🆕 El *listener* del `RadioGroup`
> Se pone en el **grupo**, no en cada radio: salta una sola vez por cambio, sea cual sea el radio pulsado. Dentro, `isMetric` dice cuál ha quedado marcado. [[05 - Vistas básicas II#4. RadioButton y RadioGroup|Ver 5 · 4. RadioButton y RadioGroup]]

> [!abstract] 🆕 `String.format(Locale.US, "%.2f", …)`
> Al escribir el valor convertido en el campo se usa `Locale.US` para que salga **con punto** (`220.46`), aunque el móvil esté en español (que pondría `220,46`). Así el número escrito se puede volver a leer sin problemas.

> [!success] ✅ Comprueba
> Con `100` y `1.70` y «Convert» activado, pulsa *Imperial*: «220.46 lb» y «66.93 in». Calcula: el BMI sigue siendo 34.60. Desactiva «Convert» y vuelve a *Metric*: solo cambian «lb»→«kg» e «in»→«m».

#### Paso 12 · Remates (errores, tecla ✓, teclado y Reset)

1. **Borrar el error al escribir:** en `setupViews()`, `binding.txtWeight.doAfterTextChanged { binding.tilWeight.error = null }` (y lo mismo con la altura). `doAfterTextChanged` es el atajo de `androidx.core` para no implementar un `TextWatcher` entero. [[08 - Gestión de la entrada de texto#4. Gestión de la escritura|Ver 8 · 4. Gestión de la escritura]]
2. **La tecla ✓ de la altura calcula:** `setOnEditorActionListener` con el mismo `when` del [[08.1 - Ejercicios 8 Gestión de la entrada de texto|proyecto Login]] (`IME_ACTION_DONE` para el teclado en pantalla e `IME_NULL` para el Enter físico). [[08 - Gestión de la entrada de texto#3. ImeOptions|Ver 8 · 3. ImeOptions]]
3. **Cerrar el teclado al calcular:** copia `SoftInputUtils.kt` de los apuntes (solo `hideSoftKeyboard()`) y llámala al principio de `calculate()`. Es una *extension function* de `Activity`, por eso se llama sin nada delante. [[08 - Gestión de la entrada de texto#2. Gestión del teclado virtual|Ver 8 · 2. Teclado virtual]]
4. **Reset:** `reset()` vacía los campos con `setText("")`, quita los errores, oculta el resultado y devuelve el foco al peso.

> [!success] ✅ Comprueba
> Repite la prueba completa que hay al final de la [[#Explicación paso a paso|explicación paso a paso]], más abajo.

Con esto la práctica está terminada. El código completo, con todos los archivos juntos, es el siguiente.

### Código fuente (proyecto `BMI`)

Proyecto *Empty Views Activity* con el paquete `es.iessaladillo.pedrojoya.bmi`, el *layout* renombrado a `main_activity.xml` y ViewBinding activado (`buildFeatures { viewBinding = true }` en `app/build.gradle.kts`). El tema hereda de `Theme.Material3.DayNight.NoActionBar`, así que el título «BMI Calculator» va dentro del *layout*, como en la captura. Las 6 imágenes del zip se copian a `app/src/main/res/drawable/`.

#### `app/src/main/res/values/strings.xml`

```xml
<resources>
    <string name="app_name">BMI</string>
    <string name="main_title">BMI Calculator</string>
    <string name="main_lblUnitSystem">Unit system:</string>
    <string name="main_rdbMetric">Metric</string>
    <string name="main_rdbImperial">Imperial</string>
    <string name="main_swtConvert">Convert</string>
    <string name="main_tilWeight">Weight</string>
    <string name="main_tilHeight">Height</string>
    <string name="main_kg">kg</string>
    <string name="main_lb">lb</string>
    <string name="main_m">m</string>
    <string name="main_in">in</string>
    <string name="main_chkClassification">With classification</string>
    <string name="main_btnCalculate">Calculate BMI</string>
    <string name="main_btnReset">Reset</string>
    <string name="main_invalid_weight">Invalid weight</string>
    <string name="main_invalid_height">Invalid height</string>
    <string name="main_imgClassification">BMI classification chart</string>
    <!-- %1$.2f = BMI con dos decimales; %2$s = nombre de la clasificación -->
    <string name="main_bmi">BMI: %1$.2f</string>
    <string name="main_bmi_classification">BMI: %1$.2f %2$s</string>

    <!-- Nombres de las clasificaciones (como en la captura y en las imágenes) -->
    <string name="bmi_underweight">Underweight</string>
    <string name="bmi_normal_weight">Normal weight</string>
    <string name="bmi_overweight">Overweight</string>
    <string name="bmi_obesity1">Obesity class I</string>
    <string name="bmi_obesity2">Obesity class II</string>
    <string name="bmi_obesity3">Obesity class III</string>
</resources>
```

#### `app/src/main/res/values/colors.xml`

```xml
<resources>
    <!-- Colores de las clasificaciones, del enunciado -->
    <color name="bmi_underweight">#FFEB5123</color>
    <color name="bmi_normal_weight">#FF71F34C</color>
    <color name="bmi_overweight">#FFF0AC3C</color>
    <color name="bmi_obesity1">#FFEF8C34</color>
    <color name="bmi_obesity2">#FFEA5528</color>
    <color name="bmi_obesity3">#FFE83523</color>
    <!-- Fondo del resultado cuando no se muestra la clasificación -->
    <color name="main_result_neutral">#FF6750A4</color>
</resources>
```

#### `app/src/main/res/values/integers.xml`

```xml
<resources>
    <!-- Valor máximo de la barra de progreso del BMI -->
    <integer name="main_bmi_max">45</integer>
</resources>
```

#### `app/src/main/res/values/dimens.xml`

```xml
<resources>
    <dimen name="main_padding">16dp</dimen>
    <dimen name="main_section_marginTop">24dp</dimen>
    <dimen name="main_field_marginTop">8dp</dimen>
    <dimen name="main_swtConvert_marginStart">16dp</dimen>
    <dimen name="main_btnReset_marginStart">8dp</dimen>
    <dimen name="main_lblResult_padding">8dp</dimen>
    <dimen name="main_prgBmi_marginTop">16dp</dimen>
    <dimen name="main_prgBmi_thickness">6dp</dimen>
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

    <TextView
        android:id="@+id/lblTitle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/main_title"
        android:textAppearance="@style/TextAppearance.Material3.HeadlineMedium" />

    <!-- Fila del sistema de unidades: etiqueta + radio buttons + switch -->
    <LinearLayout
        android:id="@+id/llUnitSystem"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_section_marginTop"
        android:gravity="center_vertical"
        android:orientation="horizontal">

        <TextView
            android:id="@+id/lblUnitSystem"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/main_lblUnitSystem" />

        <RadioGroup
            android:id="@+id/rdgUnitSystem"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:checkedButton="@+id/rdbMetric"
            android:orientation="horizontal">

            <RadioButton
                android:id="@+id/rdbMetric"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@string/main_rdbMetric" />

            <RadioButton
                android:id="@+id/rdbImperial"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@string/main_rdbImperial" />
        </RadioGroup>

        <com.google.android.material.materialswitch.MaterialSwitch
            android:id="@+id/swtConvert"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="@dimen/main_swtConvert_marginStart"
            android:checked="true"
            android:text="@string/main_swtConvert" />
    </LinearLayout>

    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/tilWeight"
        style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_section_marginTop"
        android:hint="@string/main_tilWeight"
        app:suffixText="@string/main_kg">

        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/txtWeight"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:imeOptions="actionNext"
            android:inputType="numberDecimal">

            <requestFocus />
        </com.google.android.material.textfield.TextInputEditText>
    </com.google.android.material.textfield.TextInputLayout>

    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/tilHeight"
        style="@style/Widget.Material3.TextInputLayout.OutlinedBox"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_field_marginTop"
        android:hint="@string/main_tilHeight"
        app:suffixText="@string/main_m">

        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/txtHeight"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:imeOptions="actionDone"
            android:inputType="numberDecimal" />
    </com.google.android.material.textfield.TextInputLayout>

    <CheckBox
        android:id="@+id/chkClassification"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_section_marginTop"
        android:checked="true"
        android:text="@string/main_chkClassification" />

    <LinearLayout
        android:id="@+id/llButtons"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_section_marginTop"
        android:orientation="horizontal">

        <Button
            android:id="@+id/btnCalculate"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/main_btnCalculate" />

        <Button
            android:id="@+id/btnReset"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="@dimen/main_btnReset_marginStart"
            android:text="@string/main_btnReset" />
    </LinearLayout>

    <!-- Resultado: oculto hasta que se calcula -->
    <TextView
        android:id="@+id/lblResult"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_section_marginTop"
        android:gravity="center"
        android:padding="@dimen/main_lblResult_padding"
        android:textAppearance="@style/TextAppearance.Material3.HeadlineSmall"
        android:textColor="@android:color/white"
        android:visibility="gone" />

    <com.google.android.material.progressindicator.LinearProgressIndicator
        android:id="@+id/prgBmi"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_prgBmi_marginTop"
        android:indeterminate="false"
        android:max="@integer/main_bmi_max"
        android:visibility="gone"
        app:trackThickness="@dimen/main_prgBmi_thickness" />

    <ImageView
        android:id="@+id/imgClassification"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="@dimen/main_prgBmi_marginTop"
        android:adjustViewBounds="true"
        android:contentDescription="@string/main_imgClassification"
        android:visibility="gone" />

</LinearLayout>
```

#### `app/src/main/java/es/iessaladillo/pedrojoya/bmi/Bmi.kt`

```kotlin
package es.iessaladillo.pedrojoya.bmi

// Factores de conversión del enunciado
const val KG_TO_LB = 2.20462
const val M_TO_IN = 39.3701

// Fórmulas del enunciado (allí pone "width", pero es el peso)
fun calculateBmi(weight: Double, height: Double, metric: Boolean): Double =
    if (metric) {
        weight / (height * height)
    } else {
        weight * 703 / (height * height)
    }
```

#### `app/src/main/java/es/iessaladillo/pedrojoya/bmi/BmiClassification.kt`

```kotlin
package es.iessaladillo.pedrojoya.bmi

// Cada clasificación sabe su nombre, su color y su imagen
enum class BmiClassification(
    val labelResId: Int,
    val colorResId: Int,
    val imageResId: Int,
) {
    UNDERWEIGHT(R.string.bmi_underweight, R.color.bmi_underweight, R.drawable.underweight),
    NORMAL_WEIGHT(R.string.bmi_normal_weight, R.color.bmi_normal_weight, R.drawable.normal_weight),
    OVERWEIGHT(R.string.bmi_overweight, R.color.bmi_overweight, R.drawable.overweight),
    OBESITY_GRADE_1(R.string.bmi_obesity1, R.color.bmi_obesity1, R.drawable.obesity1),
    OBESITY_GRADE_2(R.string.bmi_obesity2, R.color.bmi_obesity2, R.drawable.obesity2),
    OBESITY_GRADE_3(R.string.bmi_obesity3, R.color.bmi_obesity3, R.drawable.obesity3);

    companion object {
        // Límites del enunciado: cada clase llega hasta el valor indicado, sin incluirlo
        fun from(bmi: Double): BmiClassification = when {
            bmi < 18.5 -> UNDERWEIGHT
            bmi < 25.0 -> NORMAL_WEIGHT
            bmi < 30.0 -> OVERWEIGHT
            bmi < 35.0 -> OBESITY_GRADE_1
            bmi < 40.0 -> OBESITY_GRADE_2
            else -> OBESITY_GRADE_3
        }
    }
}
```

#### `app/src/main/java/es/iessaladillo/pedrojoya/bmi/SoftInputUtils.kt`

```kotlin
package es.iessaladillo.pedrojoya.bmi

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

#### `app/src/main/java/es/iessaladillo/pedrojoya/bmi/MainActivity.kt`

```kotlin
package es.iessaladillo.pedrojoya.bmi

import android.os.Bundle
import android.view.KeyEvent
import android.view.inputmethod.EditorInfo
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.core.view.isVisible
import androidx.core.widget.doAfterTextChanged
import com.google.android.material.textfield.TextInputEditText
import com.google.android.material.textfield.TextInputLayout
import es.iessaladillo.pedrojoya.bmi.databinding.MainActivityBinding
import java.util.Locale
import kotlin.math.roundToInt

class MainActivity : AppCompatActivity() {

    private val binding: MainActivityBinding by lazy {
        MainActivityBinding.inflate(layoutInflater)
    }

    // Último BMI calculado; null mientras no hay resultado en pantalla
    private var lastBmi: Double? = null

    // Propiedad calculada: se consulta el RadioGroup cada vez que se lee
    private val isMetric: Boolean
        get() = binding.rdgUnitSystem.checkedRadioButtonId == R.id.rdbMetric

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        setupViews()
    }

    private fun setupViews() {
        binding.rdgUnitSystem.setOnCheckedChangeListener { _, _ -> changeUnitSystem() }
        binding.chkClassification.setOnCheckedChangeListener { _, _ ->
            // Si ya hay un resultado, se repinta con o sin clasificación
            lastBmi?.let { showResult(it) }
        }
        // Al escribir en un campo desaparece su error
        binding.txtWeight.doAfterTextChanged { binding.tilWeight.error = null }
        binding.txtHeight.doAfterTextChanged { binding.tilHeight.error = null }
        // Done del teclado en pantalla o Enter físico: igual que pulsar "Calculate BMI"
        binding.txtHeight.setOnEditorActionListener { _, actionId, keyEvent ->
            when (actionId) {
                EditorInfo.IME_ACTION_DONE -> {
                    calculate()
                    true
                }
                EditorInfo.IME_NULL -> {
                    if (keyEvent?.action == KeyEvent.ACTION_DOWN) {
                        calculate()
                    }
                    true
                }
                else -> false
            }
        }
        binding.btnCalculate.setOnClickListener { calculate() }
        binding.btnReset.setOnClickListener { reset() }
    }

    private fun changeUnitSystem() {
        val metric = isMetric
        binding.tilWeight.suffixText = getString(if (metric) R.string.main_kg else R.string.main_lb)
        binding.tilHeight.suffixText = getString(if (metric) R.string.main_m else R.string.main_in)
        if (binding.swtConvert.isChecked) {
            convert(binding.txtWeight, if (metric) 1 / KG_TO_LB else KG_TO_LB)
            convert(binding.txtHeight, if (metric) 1 / M_TO_IN else M_TO_IN)
        }
        // El resultado que hubiera ya no corresponde a lo que hay en pantalla
        hideResult()
    }

    private fun convert(field: TextInputEditText, factor: Double) {
        // Campo vacío o no numérico: se deja como está
        val value = readValue(field) ?: return
        field.setText(String.format(Locale.US, "%.2f", value * factor))
    }

    // Admite coma o punto decimal; devuelve null si no es un número
    private fun readValue(field: TextInputEditText): Double? =
        field.text.toString().replace(',', '.').toDoubleOrNull()

    private fun calculate() {
        hideSoftKeyboard()
        val weight = validate(binding.txtWeight, binding.tilWeight, R.string.main_invalid_weight)
        val height = validate(binding.txtHeight, binding.tilHeight, R.string.main_invalid_height)
        if (weight == null || height == null) {
            // El foco va al primer campo erróneo, con su texto seleccionado (como en bmi2.png)
            val wrongField = if (weight == null) binding.txtWeight else binding.txtHeight
            wrongField.requestFocus()
            wrongField.selectAll()
            hideResult()
            return
        }
        val bmi = calculateBmi(weight, height, isMetric)
        lastBmi = bmi
        showResult(bmi)
    }

    // Devuelve el valor si es un número mayor que 0; si no, pone el error en su TextInputLayout
    private fun validate(field: TextInputEditText, layout: TextInputLayout, errorResId: Int): Double? {
        val value = readValue(field)
        return if (value == null || value <= 0.0) {
            layout.error = getString(errorResId)
            null
        } else {
            layout.error = null
            value
        }
    }

    private fun showResult(bmi: Double) {
        val withClassification = binding.chkClassification.isChecked
        if (withClassification) {
            val classification = BmiClassification.from(bmi)
            val color = ContextCompat.getColor(this, classification.colorResId)
            binding.lblResult.text = getString(
                R.string.main_bmi_classification, bmi, getString(classification.labelResId)
            )
            binding.lblResult.setBackgroundColor(color)
            binding.prgBmi.setIndicatorColor(color)
            binding.prgBmi.progress = bmi.roundToInt()
            binding.imgClassification.setImageResource(classification.imageResId)
        } else {
            binding.lblResult.text = getString(R.string.main_bmi, bmi)
            binding.lblResult.setBackgroundColor(ContextCompat.getColor(this, R.color.main_result_neutral))
        }
        binding.lblResult.isVisible = true
        binding.prgBmi.isVisible = withClassification
        binding.imgClassification.isVisible = withClassification
    }

    private fun hideResult() {
        lastBmi = null
        binding.lblResult.isVisible = false
        binding.prgBmi.isVisible = false
        binding.imgClassification.isVisible = false
    }

    private fun reset() {
        binding.txtWeight.setText("")
        binding.txtHeight.setText("")
        binding.tilWeight.error = null
        binding.tilHeight.error = null
        hideResult()
        binding.txtWeight.requestFocus()
    }
}
```

### Explicación paso a paso
1. **Organización del código.** La lógica está separada de la interfaz:
   - `Bmi.kt` solo calcula (fórmulas y constantes del enunciado, como *top-level*).
   - `BmiClassification.kt` solo clasifica (un `enum` que guarda el nombre, el color y la imagen de cada clase).
   - `MainActivity` solo lee la pantalla y la pinta.

   Si mañana cambia un límite o un color, se toca un único sitio.
2. **El *layout*.** Calca la captura con lo visto hasta ahora: un `LinearLayout` vertical, con dos `LinearLayout` horizontales para la fila de unidades y la de botones. Los campos son `TextInputLayout` con borde (`OutlinedBox`) y la unidad como sufijo (`app:suffixText`). El resultado, la barra y la imagen empiezan con `android:visibility="gone"`, porque no hay nada que mostrar hasta calcular. `gone` hace que tampoco ocupen espacio.
3. **`BmiClassification.from(bmi)`.** Es un `when` sin sujeto que compara de menor a mayor. Como cada rama solo se evalúa si las anteriores han fallado, `bmi < 25.0` ya significa «entre 18.5 y 25». El `else` recoge «a partir de 40». Al estar en el `companion object` se llama sobre la clase, sin crear nada: `BmiClassification.from(34.6)` devuelve `OBESITY_GRADE_1`.
4. **Leer los campos: `readValue()`.** `toDoubleOrNull()` devuelve `null` si el texto está vacío o no es un número, en lugar de lanzar una excepción como `toDouble()`. Antes se cambia la coma por punto, por si el teclado del móvil está en español y escribe «1,70».
5. **Validar: `validate()` y `calculate()`.** Un valor nulo o menor o igual que 0 pone el error en su `TextInputLayout`: `layout.error = getString(...)` dibuja el borde rojo, el icono y el texto, como en `bmi2.png`. Se validan **los dos** campos siempre, para que si ambos están mal se vean los dos errores a la vez. Después, el foco va al primero que falle y se selecciona su texto (`selectAll()`), para que el usuario lo sobrescriba directamente, como en la captura del error. El teclado se cierra al empezar con `hideSoftKeyboard()`.
6. **Borrar el error al escribir.** `doAfterTextChanged { … }` es el atajo de los apuntes del Tema 8 para `TextWatcher`: en cuanto el usuario cambia el texto, `error = null` quita el aviso rojo.
7. **Mostrar el resultado: `showResult()`.**
   - **Con clasificación:** el texto es «BMI: 34.60 Obesity class I», gracias a la cadena con parámetros `%1$.2f` (dos decimales) y `%2$s`. El fondo y la barra toman el color de la clase (`ContextCompat.getColor`), la barra avanza hasta el BMI redondeado y se pone la imagen de la clase.
   - **Sin clasificación:** solo el número, con un fondo neutro, y la barra y la imagen ocultas.

   `isVisible = true/false` es la *extension property* de `androidx.core` equivalente a `visibility = View.VISIBLE/View.GONE`.
8. **`lastBmi` y el `CheckBox`.** Se guarda el último BMI para que, si el usuario marca o desmarca «With classification» con un resultado en pantalla, se repinte sin recalcular. `lastBmi?.let { showResult(it) }` solo actúa si no es `null`.
9. **Cambiar de unidades: `changeUnitSystem()`.** `isMetric` es una propiedad calculada que pregunta al `RadioGroup` cada vez que se lee. Al cambiar de sistema se actualizan los sufijos. Si «Convert» está activado, `convert()` multiplica por el factor (o divide, al volver a métrico) y escribe el valor con dos decimales. Se usa `Locale.US` para que siempre lleve punto decimal. El resultado anterior se oculta, porque ya no corresponde a las unidades de la pantalla.
10. **Teclas y botones.** «Calculate BMI» y la tecla Done de la altura llaman a `calculate()`. La tecla Done se trata igual que en el [[08.1 - Ejercicios 8 Gestión de la entrada de texto|proyecto Login]], para que también funcione el Enter de un teclado físico. «Reset» vacía los campos, quita los errores, oculta el resultado y devuelve el foco al peso.

> [!tip] Prueba
> 1. Peso `100`, altura `1.70` y «Calculate BMI»: «BMI: 34.60 Obesity class I» en naranja, la barra en naranja y la imagen con la flecha en «Obese class I» (como la captura del enunciado).
> 2. Altura `0` y calcular: borde rojo, icono y «Invalid height», con el `0` seleccionado (como `bmi2.png`).
> 3. Con «Convert» activado, pasar a Imperial: 100 → 220.46 lb y 1.70 → 66.93 in. Al calcular sale el mismo BMI (34.60), ahora con la fórmula imperial.
> 4. Desmarcar «With classification» con un resultado en pantalla: queda solo «BMI: 34.60» con fondo neutro.
> 5. «Reset»: campos vacíos y sin resultado.

> [!warning] Igual que en las demás prácticas
> Si giras el móvil se pierde el resultado (cambio de configuración). Los campos sí se conservan, porque los `EditText` con id guardan su texto automáticamente. El enunciado no pide más; se resuelve con ViewModel más adelante.

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Uso en la práctica |
| --- | --- | --- |
| Campo con error | `til.error = getString(…)` / `til.error = null` | Validar peso y altura. |
| Unidad como sufijo | `app:suffixText` · `til.suffixText = …` | kg/lb y m/in según el sistema. |
| Lectura segura de un número | `text.toString().toDoubleOrNull()` | `null` en vez de excepción si no es un número. |
| `enum` con datos | `enum class BmiClassification(val colorResId: Int, …)` | Cada clase guarda su nombre, color e imagen. |
| Elegir por rangos | `when { bmi < 18.5 -> … else -> … }` | Clasificar el BMI. |
| Mostrar / ocultar | `vista.isVisible = true` · `android:visibility="gone"` | Resultado oculto hasta calcular. |
| Barra determinada | `android:max` · `progress` · `setIndicatorColor()` | Barra del color de la clase. |

## Relaciones

- [[05 - Vistas básicas II]] y [[06 - Vistas básicas III]] · `RadioGroup`, `MaterialSwitch`, `CheckBox` e indicadores de progreso.
- [[08.1 - Ejercicios 8 Gestión de la entrada de texto]] · tecla Done y `hideSoftKeyboard()`, reutilizados aquí.
- [[07 - POO II#Enumeraciones|07 - POO II → Enumeraciones]] · el `enum class` con propiedades.
