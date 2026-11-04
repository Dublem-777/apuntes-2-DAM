---
asignatura: Optativa
tema: 6
tipo: tema
estado: completo
fecha: 2026-11-04
tags:
  - DAM/tema
  - DAM/optativa/android-vistas
---

# 6 · Vistas básicas III

> [!info] Asignatura
> **Optativa** · [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|temario en Programación Multimedia y Dispositivos Móviles]] · Tema 6 · Android (vistas)
> Tema anterior: [[05 - Vistas básicas II]] · Tema siguiente: [[07 - Mensajes emergentes]]

> [!info] Material de referencia
> [Vistas básicas III](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/a06%20-%20Vistas%20basicas%20III/)

## Índice del tema

- [[#1. Indicadores de progreso]]
- [[#2. Slider]]
- [[#3. RangeSlider]]

---

## 1. Indicadores de progreso

Se tratan de vistas que sirven de indicador visual del progreso que se está llevando a cabo en una determinada operación.

El progreso puede ser:

- determinado: Conocemos de antemano el valor final del progreso. La animación va desde el valor inicial hasta el valor final. La barra puede mostrar un segundo progreso secundario, como por ejemplo el nivel de _buffer_ durante un _streaming_.
- indeterminado: No conocemos o no existe un valor final del progreso, sino que simplemente la operación se inicia y finaliza en algún momento. Por tanto se muestra una animación cíclica para indicar el progreso.
- indeterminado y luego determinado: Inicialmente no conocemos el valor final del progreso, pero posteriormente se obtiene y se comienza el progreso. Inicialmente se muestra una animación cíclica representativa de progreso indeterminado y una vez obtenido el valor final se muestra como progreso determinado.

> [!note]- 🖼️ Imagen: ProgressBar
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/progressbar.gif)

La librería _material design_ incorpora dos vistas diferentes para representar el progreso, que siguen las indicaciones de la guía respecto al aspecto visual de estos elementos. Ambas permiten especificar un progreso determinado o indeterminado:

- `com.google.android.material.progressindicator.LinearProgressIndicator`: Representa una barra de progreso.
- `com.google.android.material.progressindicator.CircularProgressIndicator`: Representa un círculo de progreso.

Los atributos más importantes de estas vistas son:

- `android:indeterminate="false"`: para indicar que se trata de progreso determinado. Por defecto es `true` (indeterminado).
- `android:max`: Valor final (máximo) de progreso. Para progreso determinado.
- `android:progress`: Valor de progreso actual. Para progreso determinado.
- `android:secondaryProgress`: Valor de progreso secundario actual. Para progreso determinado con progreso secundario.

Los métodos más importantes de esta vista son:

- `setProgress()`: Permite establecer el valor actual de progreso. Para progreso determinado.
- `setSecondaryProgress()`: Permite establecer el valor actual de progreso secundario. Para progreso determinado con progreso secundario.
- `setIndeterminate(false)`: Permite establecer el progreso como indeterminado. Especialmente útil en el caso del progreso indeterminado y luego determinado, ya que al obtener el valor final de progreso se llama a este método para convertir el progreso indeterminado en determinado.

Por ejemplo para incluir un círculo de progreso indeterminado en nuestro _layout_ haríamos:

**Círculo de progreso circular indeterminado**

```xml
<com.google.android.material.progressindicator.CircularProgressIndicator
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:indeterminate="true" />
```

Para saber más sobre estas vistas visite: [https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md](https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md)

> [!warning] Aviso
> También existe la vista original `ProgressBar`, pero ésta NO usa los estilos definidos por Material Design 3, por lo que NO se recomienda su uso. Si le aplicamos al atributo `style` el valor `@style/Widget.AppCompat.ProgressBar.Horizontal` corrresponderá a una barra de progreso, y si le asignamos `@style/Widget.AppCompat.ProgressBar`, se mostrará como un círculo de progreso.

## 2. Slider

Un _slider_ es una vista que permite seleccionar un valor de tipo _float_ de entre un rango de valores, representados en una barra horizontal y elemento deslizable (_thumb_).

Existen dos tipos de _sliders_:

- Los _sliders_ continuos: Permiten seleccionar cualquier valor del rango.

> [!note]- 🖼️ Imagen: Slider continuo
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/slider_continuo.png)

- Los _sliders_ discretos: Solo permiten seleccionar determinados valores del rango, que además se marcan en la barra horizontal.

> [!note]- 🖼️ Imagen: Slider discreto
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/slider_discreto.png)

La librería de _material design_ incluye la vista `com.google.android.material.slider.Slider`, que permite crear ambos tipos de _sliders_. Sus principales atributos XML son:

- `android:valueFrom`: Límite inferior del rango de valores. Por defecto vale `0.0`.
- `android:valueTo`: Límite superior del rango de valores. Por defecto vale `1.0`.
- `android:value`: Valor actual seleccionado. Por defecto vale `0`.
- `android:stepSize`: Valor de salto entre los valores posibles, que convierte al _slider_ en discreto. Los únicos valores que se podrán seleccionar serán los límites del rango o los valores correspondientes a los saltos. Por defecto vale `0.0`, por lo que por defecto es _slider_ será continuo.
- `app:app:labelBehavior`: Indica el comportamiento de la etiqueta de valor que se muestra al arrastrar el _thumb_ del _slider_. Los posibles valores son `floating` (la etiqueta flota fuera del _slider_, valor por defecto), `withinBounds` (la etiqueta influye en la altura del _slider_), o `gone` (no se muestra etiqueta).

Por ejemplo, veamos la definición de un `Slider` continuo que puede tomar cualquier valor entre `0.0` y `100.0`:

**Definición de un slider continuo**

```xml
<com.google.android.material.slider.Slider
    android:id="@+id/continuousSlider"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:valueFrom="0.0"
    android:valueTo="100.0" />
```

Para definir un _slider_ discreto simplemente hay que establecer el atributo `android:stepSize`. Por ejemplo:

**Definición de un slider discreto**

```xml
<com.google.android.material.slider.Slider
    android:id="@+id/discreteSlider"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:valueFrom="0.0"
    android:valueTo="100.0"
    android:stepSize="10.0" />
```

Los métodos más importantes de la vista `Slider` son:

- `setValue(float)`: Permite establecer el valor actual desde código.
- `getValue(): Float`: retorna el valor seleccionado.
- `addOnChangeListener(onChangeListener)`: Recibe un objeto que implementa la interfaz `Slider.OnChangeLister`, cuyo método `onValueChange(slider, value, fromUser)` es llamado cada vez que cambia el valor, recibiendo el _slider_, el nuevo valor y un valor booleano indicativo si el valor fue cambiado por interacción del usuario.
- `setLabelFormatter(labelFormatter)`: Registra un objeto de la interfaz `LabelFormatter`, cuyo método `getFormattedValue(value)` será llamado cuando se deba mostrar un valor en la etiqueta, para que el método retorne la cadena que se debe mostrar.

Para saber más sobre esta vista visite: [https://github.com/material-components/material-components-android/blob/master/docs/components/Slider.md](https://github.com/material-components/material-components-android/blob/master/docs/components/Slider.md)

## 3. RangeSlider

Corresponde a un _slider_ en el que en vez de seleccionar un valor en un rango, se selecciona un subrango de valores del rango. Por este motivo muestra dos _thumbs_, que delimitan el subrango seleccionado.

Al igual que en el caso de _slider_, existen _range sliders_ continuos y _range sliders_ discretos.

> [!note]- 🖼️ Imagen: RangeSlider continuo
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/rangeslider_continuo.png)

La librería de _material design_ incluye una vista `com.google.android.material.slider.RangeSlider` que permite crear ambos tipos de _sliders_. Sus principales atributos XML son:

- `android:valueFrom`: Límite inferior del rango de valores. Por defecto vale `0.0`.
- `android:valueTo`: Límite superior del rango de valores. Por defecto vale `1.0`.
- `app:values`: Array con los límites del subrango seleccionado. Por defecto un array con los valores `0.0` y `0.0`.
- `android:stepSize`: Valor de salto entre los valores posibles, que convierte al _slider_ en discreto. Los únicos valores que se podrán seleccionar serán los límites del rango o los valores correspondientes a los saltos. Por defecto vale `0.0`, por lo que por defecto es _slider_ será continuo.
- `app:app:labelBehavior`: Indica el comportamiento de la etiqueta de valor que se muestra al arrastrar el _thumb_ del _slider_. Los posibles valores son `floating` (la etiqueta flota fuera del _slider_, valor por defecto), `withinBounds` (la etiqueta influye en la altura del _slider_), o `gone` (no se muestra etiqueta).

Por ejemplo, veamos la definición de un `RangeSlider` continuo que puede tomar cualquier subrango de valores entre `0.0` y `100.0`:

**Definición de un range slider continuo**

```xml
<com.google.android.material.slider.RangeSlider
    android:id="@+id/rangeSlider"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:valueFrom="0.0"
    android:valueTo="100.0"
    app:values="@array/rangeSlider_default" />
```

donde el archivo `values/arrays.xml` contiene:

**`Array de límites del subrango por defecto, en arrays.xml`**

```xml
<resources>
    <string-array name="rangeSlider_default">
        <item>50.0</item>
        <item>80.0</item>
    </string-array>
</resources>
```

Para definir un _range slider_ discreto simplemente hay que establecer el atributo `android:stepSize`.

Los métodos más importantes de la vista `RangeSlider` son:

- `setValues(List<Float>)`: Recibe una lista con los límites del subrango a seleccionar.
- `setValues(float...)`: Recibe un _vararg_ con los límites del subrango a seleccionar.
- `getValues(): List<Float>`: Retorna una lista con los límites del subrango seleccionado.
- `addOnChangeListener(onChangeListener)`: Recibe un objeto que implementa la interfaz `Slider.OnChangeLister`, cuyo método `onValueChange(slider, value, fromUser)` es llamado cada vez que cambia alguno de los límites del subrango seleccionado, recibiendo el _slider_, el nuevo valor y un valor booleano indicativo si el valor fue cambiado por interacción del usuario.
- `setLabelFormatter(labelFormatter)`: Registra un objeto de la interfaz `LabelFormatter`, cuyo método `getFormattedValue(value)` será llamado cuando se deba mostrar un valor en la etiqueta, para que el método retorne la cadena que se debe mostrar.

> [!note]- 🖼️ Imagen: RangeSlider con LabelFormatter
> En los apuntes del aula hay aquí una imagen; solo se ve con la sesión iniciada: [abrir imagen](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/244507/mod_resource/content/1/files/slider_range_formatter.png)

---

## Esquema resumen de conceptos clave

| Concepto | Sintaxis | Idea clave |
| --- | --- | --- |
| Tipos de progreso | `android:indeterminate="true"` / `"false"` | Determinado (se conoce el final), indeterminado o indeterminado y luego determinado. |
| Indicadores de Material | `LinearProgressIndicator` · `CircularProgressIndicator` | Barra o círculo; `android:max`, `android:progress`, `setProgress()`. No usar `ProgressBar`. |
| Slider | `android:valueFrom` · `android:valueTo` · `android:value` | Selecciona un `Float` de un rango; `addOnChangeListener`. |
| Slider discreto | `android:stepSize="10.0"` | Solo deja elegir los saltos marcados. |
| RangeSlider | `app:values="@array/…"` | Selecciona un subrango con dos *thumbs*; `values` es una `List<Float>`. |
| LabelFormatter | `setLabelFormatter(…)` | Decide el texto de la etiqueta del valor. |

## Relaciones

- Tema anterior: [[05 - Vistas básicas II]] · Tema siguiente: [[07 - Mensajes emergentes]]
- [[03 - Recursos#4. Recursos de valor|03 - Recursos → 4. Recursos de valor]] — el array de valores por defecto del RangeSlider.
- Índice: [[DAM/Programacion_Multimedia_y_Dispositivos_Moviles/Indice|Índice de PMDM]]

## Para repasar

- [ ] Explicar los tres tipos de progreso.
- [ ] Mostrar un círculo de progreso indeterminado.
- [ ] Crear un slider continuo y otro discreto.
- [ ] Definir un RangeSlider con su array de valores por defecto.
- [ ] Reaccionar a los cambios de valor con `addOnChangeListener`.
