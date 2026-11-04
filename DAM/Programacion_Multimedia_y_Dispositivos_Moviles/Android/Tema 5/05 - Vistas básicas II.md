---
asignatura: Optativa
tema: 5
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-vistas
---

# 5 · Vistas básicas II

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 5 · Android (vistas)
> Tema anterior: [[04 - Vistas básicas I]] · Tema siguiente: [[06 - Vistas básicas III]]

> [!info] Material de referencia
> [Vistas básicas II](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a05%20-%20Vistas%20basicas%20II/)

## Índice del tema

- [[#1. CheckBox]]
- [[#2. Toggle icon button]]
- [[#3. Switch]]
- [[#4. RadioButton y RadioGroup]]
- [[#5. MaterialButtonToggleGroup]]

---

## 1. CheckBox

Un `Checkbox` o casilla de verificación es una vista que puede encontrarse en dos estados: _checked_ (marcado) o _unchecked_ (desmarcado), pasando de un estado al otro cuando se hace _click_ sobre él (_toggle_).

> [!note]- 🖼️ Imagen: Checkbox
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/checkbox.png)

La clase `CheckBox` es una subclase de `CompoundButton`, `Button`, `TextView` y `View`, por lo que hereda sus propiedades y métodos.

Si nuestra aplicación usa un tema que extienda de `Theme.MaterialComponents`, la etiqueta `<Checkbox>` se convierte internamente en una etiqueta `<com.google.android.material.checkbox.MaterialCheckBox>`, que corresponde a la implementación de las casillas de verficicación atendiendo a la guía _material design_.

Para saber más sobre _MaterialCheckBox_ visite: [https://github.com/material-components/material-components-android/blob/master/docs/components/Checkbox.md](https://github.com/material-components/material-components-android/blob/master/docs/components/Checkbox.md)

Sus atributos XML más importantes son:

- `android:text`: Texto mostrado.
- `android:checked`: Indica si el botón se encuentra inicialmente en estado _checked_. Por defecto es `false`.

En el siguiente código se define un `CheckBox`:

**Especificación de CheckBox en layout**

```xml
<CheckBox
    android:id="@+id/chkPolitely"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/main_chkPolitely"
    android:checked="true" />
```

Los métodos más usados de la clase `CheckBox` son:

- `isChecked()`: Retorna `true` si el botón se encuentra en el estado _checked_.
- `setChecked(boolean)`: Recibe `true` para hacer que el botón pase a estado _checked_ y `false` para el estado _unchecked_.
- `toggle()`: Cambia el estado del botón desde _checked_ a _unchecked_ o viceversa.
- `setOnCheckedChangeListener(onCheckedChangeListener)`: Establecemos para el _checkbox_ el objeto _listener_ de una clase que implemente la interfaz `OnCheckedChangeListener` cuyo método de _callback_ será llamado cuando el estado del _checkbox_ cambie, ya sea por interacción del usuario o desde código Java o Kotlin. Como se trata de una interfaz funcional podemos usar una expresión _lambda_.

Por ejemplo:

**Métodos principales de CheckBox**

```java
binding.chkPoliltely.setOnCheckedChangeListener((buttonView, isChecked) ->
    // ...
);
if (binding.chkPolitely.isChecked()) {
    binding.chkPolitely.setChecked(false);
}
```

> [!note] Este fragmento de los apuntes está en Java
> Se nota en la lambda `(…) ->` y en los `;`; además, `chkPoliltely` tiene una errata. En Kotlin, con la lambda fuera del paréntesis y las propiedades en vez de los *getters*/*setters*, sería:
> ```kotlin
> binding.chkPolitely.setOnCheckedChangeListener { buttonView, isChecked ->
>     // ...
> }
> if (binding.chkPolitely.isChecked) {
>     binding.chkPolitely.isChecked = false
> }
> ```

Si queremos definir un _checkbox_ que pueda tener el estado indeterminado, usaremos en nuestro _layout_ directamente la vista `com.google.android.material.checkbox.MaterialCheckBox`, pudiendo especificar el atributo `app:checkedState="indeterminate"` o desde código usar los métodos `setCheckedState(MaterialCheckbox.STATE_INDETERMINATE)` y `addOnCheckedStateChangedListener()`.

## 2. Toggle icon button

Podemos crear un checkbox que en vez de mostrar una casilla de verificación, muestre un icono u otro dependiendo de si se encuentra en estado _checked_ o no. Para ello asignaremos al atributo `android:button` un _drawable_ correspondiente a una especificación XML con el icono a mostrar en cada estado. También podemos usar el atributo `android:buttonTint` para tintar los iconos con un color determinado. Por ejemplo:

**Checkbox con icono**

```xml
<CheckBox
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:button="@drawable/sl_favourite_24dp"
    android:buttonTint="@color/colorPrimary" />
```

Por su parte, en la carpeta `res/drawable` debemos crear un nuevo archivo de recurso _drawable_ haciendo click derecho sobre la carpeta `res/drawable` y eligiendo la opción `New > Drawable Resource File`, al que asignaremos el nombre `sl_favourite_24dp` con el siguiente contenido:

**Especificación XML de drawable atendiendo al estado de la vista**

```xml
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@drawable/ic_baseline_favorite_border_24" android:state_checked="false" />
    <item android:drawable="@drawable/ic_baseline_favorite_24" android:state_checked="true" />
    <item android:drawable="@drawable/ic_baseline_favorite_border_24" />
</selector>
```

Dicho archivo de especificación de _drawable_ establece que si está en estado _checked_ se use el icono `ic_baseline_favorite_24` de la carpeta `res/drawable`, y si no está en estado _checked_ o en cualquier otro caso se use el icono `ic_baseline_favorite_border_24`.

Los iconos `ic_baseline_favorite_24` y `ic_baseline_favorite_border_24` corresponden a iconos vectoriales, cuya principal ventaja es que se visualizan correctamente en cualquier escala, por lo se verán bien en cualquier tamaño de pantalla.

Veamos el resultado del toggle icon button:

> [!note]- 🖼️ Imagen: Toggle icon button
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/toggle_icon_button.gif)

Para saber más sobre esta vista visite: [https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md#icon](https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md#icon)

## 3. Switch

Un _switch_ corresponde a la representación visual de un interruptor o conmutador, que puede encontrarse en dos estados posibles: pulsado/activado (_on_ o _checked_) o no pulsado/desactivado (_off_ o _unchecked_), similar a un _checkbox_. Sin embargo, a diferencia de este último, aparte de haciendo _click_, en un _switch_ para pasar de un estado a otro el usuario también podrá deslizar el interruptor a derecha o izquierda.

La vista `androidx.appcompat.widget.SwitchCompat`, perteneciente a la librería AppCompat, hereda de `CompoundButton`, `Button`, `TextView` y `View`, por lo que hereda las propiedades y métodos de éstos.

Por su parte, la vista `com.google.android.material.materialswitch.MaterialSwitch`, que hereda de `androidx.appcompat.widget.SwitchCompat`, implementa las características de la guía _material design_ respecto a los _switch_, y corresponde a la vista que se recomienda usar.

> [!note]- 🖼️ Imagen: MaterialSwitch
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/switch.png)

Sus atributos XML más importantes son:

- `android:text`: Texto que acompaña al interruptor.
- `android:checked`: Indica si el botón se encuentra inicialmente en estado _on_. Por defecto es `false`.

En el siguiente código se define una vista `MaterialSwitch` de ejemplo. Debemos fijarnos en que a la hora de especificar el nombre de la clase debemos indicar el nombre completo:

**Especificación de MaterialSwitch en layout**

```xml
<com.google.android.material.materialswitch.MaterialSwitch
    android:id="@+id/swtPolitely"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:checked="true"/>
```

Los métodos más usados de la clase `MaterialSwitch` son similares a los de la clase `CheckBox`.

Para saber más sobre esta vista visite [https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md](https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md)

> [!warning] Aviso
> Existe una vista más antigua, llamada `Switch`, del propio _framework_, que no es compatible con las nuevas versiones de Android. De ahí que nuestra vistas se llamen `SwitchCompat` y `MaterialSwitch`, y no simplemente `Switch`.

## 4. RadioButton y RadioGroup

Al igual que un _checkBox_, un botón de opción (_radio button_) puede encontrarse en dos estados posibles: _checked_ (marcado) o _unchecked_ (desmarcado). Sin embargo, una vez que un _radio button_ ha sido seleccionado, no puede ser desmarcado individualmente.

De hecho, los _radio buttons_ casi siempre van a ser agrupados de manera que, en un momento dado, sólo uno de los del grupo pueda estar en estado _checked_, permaneciendo el resto en estado _unchecked_. Al igual que `CheckBox` y `SwitchCompat`, la clase `RadioButton` extiende de `CompoundButton`, `Button,` `TextView` y `View`, por lo hereda sus propiedades y métodos.

> [!note]- 🖼️ Imagen: RadioButton
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/radio.png)

Si nuestra aplicación usa un tema que extienda de `Theme.MaterialComponents`, la etiqueta `<RadioButton>` se convierte internamente e una etiqueta `<com.google.android.material.button.MaterialRadioButton>`, que corresponde a la implementación de un _radio button_ atendiendo a la guía _material design_.

Para poder agrupar varios _radio buttons_ usaremos un tipo de contenedor denominado `RadioGroup`, que es una subclase de `LinearLayout` (que veremos con detenimiento dentro de muy poco), `ViewGroup` y `View`. `RadioGroup` crea un ámbito de multiexclusión para un conjunto de _radio buttons_, de manera que al marcar un _radio button_ del grupo, se desmarcan el resto de _radio buttons_ del mismo. Por defecto inicialmente todos los _radio buttons_ del grupo aparecen desmarcados.

Para conocer en un momento dado qué _radio button_ del grupo está marcado, se utilizará su atributo `id`, por lo que deberemos especificar siempre dicho atributo para cada _radio button_.

Sus atributos XML más importantes son:

- `android:orientation`: Establece cómo se sitúan los _radio buttons_ en el contenedor, `vertical` (verticalmente) o `horizontal` (horizontalmente). Este atributo es heredado de `LinearLayout`.
- `android:checkedButton`: Recibe el `id` del _radio button_ hijo del _radiogroup_ que debe estar seleccionado inicialmente.

Los métodos más interesantes de la clase `RadioGroup` son:

- `check(radioButtonIdResId)`: Selecciona (marca) el _radio button_ cuyo `id` corresponde con el valor recibido como parámetro.
- `clearCheck()`: Desmarca el _radio button_ seleccionado, de manera que todos los _radio buttons_ del grupo permanecen desmarcados.
- `getCheckedRadioButtonId()`: Retorna el identificador (`id`) del _radio button_ del grupo que está seleccionado en ese momento. Si no hay ninguno seleccionado, retorna `-1`.
- `setOnCheckedChangeListener(onCheckedChangeListener)`: Registramos el objeto _listener_ de una clase que implementa la interfaz `OnCheckedChangeListener` cuyo método de _callback_ será llamado por el sistema cuando se cambie el _radio button_ seleccionado dentro del grupo, ya sea el usuario o desde código.

En nuestro fichero de _layout_ XML incluiremos una etiqueta `<RadioGroup>` dentro de la que insertaremos las distintas etiquetas `<RadioButton>` correspondientes a los _radio button_ que conforman el grupo. Es muy importante que asignemos a cada _radio button_ un identificador para poder en ejecución nuestra ejecución qué _radio button_ del grupo está seleccionado:

**Especificación de RadioGroup y RadioButtons en layout**

```xml
<RadioGroup
    android:id="@+id/rdgColor"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">
    <RadioButton
        android:id="@+id/rdbRed"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/main_rdbRed" />
    <RadioButton
        android:id="@+id/rdbBlue"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/main_rdbBlue" />
</RadioGroup>
```

En el siguiente código se muestra el uso en tiempo de ejecución de algunos de los métodos más importantes de `RadioGroup`:

**Métodos principales de RadioGroup**

```java
binding.rdgColor.clearCheck();
binding.rdgColor.check(R.id.rdbColorAzul);
int selectedColorRadioButtonId = binding.rdg.getCheckedRadioButtonId();
```

> [!note] También está en Java
> Los ids no coinciden con el *layout* de arriba (`rdbColorAzul` en vez de `rdbBlue`, `rdg` en vez de `rdgColor`). En Kotlin y con los ids del *layout*:
> ```kotlin
> binding.rdgColor.clearCheck()
> binding.rdgColor.check(R.id.rdbBlue)
> val selectedColorRadioButtonId = binding.rdgColor.checkedRadioButtonId
> ```

Respecto a la clase `RadioButton`, sus métodos principales son los mismos que los de la clase `CheckBox`, aunque normalmente no se trabaja con ellos individualmente, sino con el `RadioGroup`, como acabamos de ver.

Para saber más sobre esta vista visite: [https://github.com/material-components/material-components-android/blob/master/docs/components/RadioButton.md](https://github.com/material-components/material-components-android/blob/master/docs/components/RadioButton.md)

## 5. MaterialButtonToggleGroup

La librería de _material design_ nos proporciona un _ViewGroup_ llamado `com.google.android.material.button.MaterialButtonToggleGroup`, que corresponde a un contenedor de un grupo de botones _checkables_. Dichos botones automáticamente se marcan como _checkables_, y por defecto se puede seleccionar más de un botón del grupo a la vez.

La clase `com.google.android.material.button.MaterialButtonToggleGroup` extiende de `LinearLayout` (lo estudiaremos dentro de poco) y por defecto ocupa toda la anchura disponible.

Sus atributos XML principales son:

- `app:singleSelection`: Recibe `true` si queremos que a la vez solo pueda estar seleccionado un botón del grupo de botones.
- `app:selectionRequired`: Recibe `true` si queremos que siempre deba haber algún botón seleccionado de entre el grupo de botones.
- `app:checkedButton`: Para indicar el _resId_ del botón seleccionado, en el que caso de que solo uno de ellos pueda estar seleccionado.

Normalmente a los botones del grupo se les aplica el atributo `style="?attr/materialButtonOutlinedStyle"` para que correspondan a _outlined buttons_.

Veamos un ejemplo de especificación de `MaterialButtonToggleGroup` en el que solo se puede seleccionar un botón y siempre debe haber uno seleccionado:

**Especificación de MaterialButtonToggleGroup en layout**

```xml
<com.google.android.material.button.MaterialButtonToggleGroup
    android:id="@+id/toggleButton"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:selectionRequired="true"
    app:singleSelection="true"
    app:checkedButton="@+id/button1">
    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button 1"
        style="?attr/materialButtonOutlinedStyle" />
    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button 2"
        style="?attr/materialButtonOutlinedStyle" />
    <Button
        android:id="@+id/button3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button 3"
        style="?attr/materialButtonOutlinedStyle" />
</com.google.android.material.button.MaterialButtonToggleGroup>
```

> [!note]- 🖼️ Imagen: MaterialButtonToggleGroup
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/material_button_toggle_group.png)

Para cambiar la selección desde código dispone de los métodos `check(buttonId)`, para seleccionar un botón, `uncheck(buttonId)`, para quitar la selección a un botón, y `clearChecked()` para que no haya ninguno seleccionado.

Para saber el botón seleccionado tenemos el método `getCheckedButtonId()`, que retorna el id del botón seleccionado, si es que solo puede seleccionarse uno. Si pueden seleccionarse varios botones, podemos obtener sus ids con el método `getCheckedButtonsIds()`, que retorna una lista con los ids de los botones seleccionados.

Si queremos ejecutar un determinado código cada vez que cambie la selección podemos usar el método `addOnButtonCheckedListener(onButtonCheckedListener)`, que recibe un objeto de la interfaz `OnButtonCheckedListener`, que dispone de un método `onButtonChecked(group, checkedId, isChecked)`, que será llamado por el sistema cada vez que cambie el estado de selección de alguno de los botones. Recibe el propio `MaterialButtonToggleGroup`, el id del botón cuyo estado de selección ha cambiado, y el estado de selección en el que éste ha quedado.

Por otra parte, si en vez de botones con texto, queremos que sean botones con solo iconos, podemos definir un estilo para ello y aplicárselo a los botones correspondientes. Veamos primero cómo definir el estilo dentro del archivo `res/values/styles.xml`:

**Estilo para que los botones solo muestren un icono**

```xml
<style name="Widget.App.Button.OutlinedButton.IconOnly" parent="Widget.Material3.Button.OutlinedButton">
    <item name="iconPadding">0dp</item>
    <item name="android:insetTop">0dp</item>
    <item name="android:insetBottom">0dp</item>
    <item name="android:paddingLeft">12dp</item>
    <item name="android:paddingRight">12dp</item>
    <item name="android:minWidth">48dp</item>
    <item name="android:minHeight">48dp</item>
</style>
```

Y después simplemente hay que aplicar dicho estilo a todos los botones del grupo:

**Especificación de MaterialButtonToggleGroup con botones icónicos**

```xml
<com.google.android.material.button.MaterialButtonToggleGroup
    android:id="@+id/toggleButton"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:selectionRequired="true"
    app:singleSelection="true"
    app:checkedButton="@+id/button1">
    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:icon="@drawable/ic_favorite_24dp"
        style="@style/Widget.App.Button.OutlinedButton.IconOnly" />
    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:icon="@drawable/ic_remove_red_eye_24dp"
        style="@style/Widget.App.Button.OutlinedButton.IconOnly" />
    <Button
        android:id="@+id/button3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:icon="@drawable/ic_notifications_24dp"
        style="@style/Widget.App.Button.OutlinedButton.IconOnly" />
</com.google.android.material.button.MaterialButtonToggleGroup>
```

El resultado es el siguiente:

> [!note]- 🖼️ Imagen: MaterialButtonToggleGroup con botones icónicos
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/material_button_toggle_group_icons.png)

Para saber más sobre esta vista visite: [https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md#toggle-button](https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md#toggle-button)

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| CheckBox | `android:checked` · `isChecked` · `toggle()` | Dos estados; `setOnCheckedChangeListener`. |
| Estado indeterminado | `MaterialCheckBox` + `app:checkedState="indeterminate"` | Tercer estado, solo con la vista de Material. |
| *Toggle icon button* | `android:button="@drawable/sl_…"` | Un `<selector>` elige el icono según `state_checked`. |
| MaterialSwitch | `com.google.android.material.materialswitch.MaterialSwitch` | Interruptor deslizable; mismos métodos que `CheckBox`. No usar el `Switch` antiguo. |
| RadioGroup | `<RadioGroup>` con `<RadioButton>` | Solo uno marcado; `check()`, `clearCheck()` y `checkedRadioButtonId` (`-1` si ninguno). |
| MaterialButtonToggleGroup | `app:singleSelection` · `app:selectionRequired` · `app:checkedButton` | Grupo de botones *checkables*; `addOnButtonCheckedListener`. |

## Relaciones

- Tema anterior: [[04 - Vistas básicas I]] · Tema siguiente: [[06 - Vistas básicas III]]
- [[03 - Recursos#11. Recursos de estilo|03 - Recursos → 11. Recursos de estilo]] — el estilo `IconOnly` de los botones del grupo.
- [[10 - Programación funcional#6. Conversión SAM|10 - Programación funcional → 6. Conversión SAM]] — los *listeners* como lambdas.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar las diferencias entre CheckBox, MaterialSwitch y RadioButton.
- [ ] Crear un *toggle icon button* con un `<selector>`.
- [ ] Agrupar *radio buttons* y averiguar cuál está marcado.
- [ ] Configurar un MaterialButtonToggleGroup de selección única y obligatoria.
- [ ] Pasar a Kotlin los fragmentos en Java de los apuntes.
