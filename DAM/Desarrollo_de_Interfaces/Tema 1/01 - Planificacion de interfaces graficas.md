---
asignatura: DI
tema: 1
tipo: tema
estado: completo
fecha: 2026-09-21
tags:
  - DAM/tema
  - DAM/di/planificacion-interfaces-graficas
---

# 1 · Planificación de interfaces gráficas

> [!info] Asignatura
> [[DAM/Desarrollo_de_Interfaces/Indice|Desarrollo de Interfaces]] · Tema 1
> Fuente original: `Documentos/Notas/Unidad 01 - Planificación de interfaces gráficas.pdf` (Sergi García, sept. 2025)

## Índice del tema

- [[#1. Introducción y contexto profesional]]
- [[#2. Tipos de interfaces gráficas]]
- [[#3. Usabilidad y experiencia de usuario]]
- [[#4. Diseño visual y percepción]]
- [[#5. Guías de estilo]]
- [[#6. Componentes y estructuras de una interfaz]]
- [[#7. Planificación del diseño de la interfaz]]
- [[#8. Herramientas de diseño y prototipado (sin código)]]

---

## 1. Introducción y contexto profesional

Una **interfaz gráfica de usuario (GUI** — Graphical User Interface**)** es el espacio visual y funcional donde el usuario interactúa con un sistema informático, una aplicación o un dispositivo. Está formada por elementos visuales (ventanas, botones, menús, iconos, formularios, textos…) que permiten controlar y recibir información del sistema de manera sencilla, intuitiva y eficiente.

**Características clave de las interfaces gráficas:**

- Visual y táctil (en pantallas táctiles).
- Basada en metáforas visuales reconocibles (carpetas, papeles, botones).
- Interactiva: responde a las acciones del usuario (clics, toques, gestos).
- Puede estar en dispositivos diversos: ordenadores, móviles, tablets, dispositivos inteligentes.

**El papel del diseñador de interfaces:** crea los espacios visuales de interacción para que la experiencia sea *fácil de entender, eficiente, atractiva y accesible*. Sus funciones principales:

- Investigar y comprender necesidades y comportamientos de los usuarios.
- Diseñar estructuras, componentes y flujos de navegación.
- Elegir colores, tipografías, iconos y estilos.
- Elaborar prototipos, wireframes y mockups antes de desarrollar.
- Colaborar con desarrolladores y realizar mejoras continuas según feedback.

**Colaboración en equipo** (el diseñador actúa como puente entre todos):

| Perfil | Qué hace |
| --- | --- |
| Diseñador UX | Investigación del usuario, necesidades, arquitectura de la información, usabilidad |
| Diseñador UI | Aspecto visual e interacción directa: diseño gráfico y componentes |
| Desarrollador front-end | Programa la interfaz (web, móvil o escritorio) |
| Cliente / usuarios finales | Proveen requisitos y validan el producto |

**Objetivos de una interfaz gráfica** (tres fundamentales):

1. **Facilitar la interacción** — navegación clara, componentes reconocibles, feedback inmediato.
2. **Transmitir información** — datos comprensibles y organizados, priorizar lo importante, códigos visuales (color, iconos, tipografía).
3. **Generar confianza** — aspecto profesional y fiable, coherencia visual, mensajes de error claros.

---

## 2. Tipos de interfaces gráficas

### 2.1 Escritorio (Windows, MacOS, Linux)
Las más clásicas, para ordenadores personales: teclado y ratón, ventanas múltiples, menús desplegables, barras de herramientas, mucha información en pantalla. Windows (empresarial/doméstico), MacOS (diseño cuidado), Linux (GNOME, KDE… entornos técnicos).

### 2.2 Móviles (Android, iOS)
Pantalla táctil: toques, deslizamientos, pellizcos. Espacio limitado → simplificar; uso en movimiento y a una mano; gestos y notificaciones. Android (abierto, personalizable) vs iOS (cerrado, experiencia uniforme).

### 2.3 Híbridas (app multiplataforma)
Una sola base de código para varios dispositivos. Se adaptan a pantallas grandes y pequeñas; desarrollo más rápido y económico. Tecnologías: **React Native, Flutter, Ionic, Quasar, Kotlin Multiplatform**. Desafío: rendimiento y experiencia nativa en cada plataforma.

### 2.4 Realidad Aumentada (AR) y Virtual (VR)
- **AR**: superpone información digital sobre el mundo real (Pokémon Go, navegación).
- **VR**: entorno completamente digital con gafas/cascos (videojuegos, formación, simulación).
- Comunes: interfaces 3D inmersivas, sensores de movimiento; desafíos: evitar mareos, interacciones intuitivas en 3D.

### 2.5 Gestuales (Kinect, sensores)
Control por movimientos del cuerpo o manos. Eliminan dispositivos físicos; interacción natural pero menos precisa; requieren diseño claro de gestos.

### 2.6 Por voz (Siri, Alexa, Google Assistant)
Comandos y respuestas habladas en smartphones, altavoces, coches. Sin manos, ideales para multitarea y accesibilidad. Desafíos: reconocimiento preciso, lenguaje natural, contexto.

### 2.7 Resumen

| Tipo | Dispositivo típico | Interacción principal | Retos principales |
| --- | --- | --- | --- |
| Escritorio | PC, portátil | Ratón y teclado | Complejidad, multitarea |
| Móvil | Smartphone, tablet | Táctil | Espacio reducido, gestos |
| Híbrida | Móviles y escritorio | Táctil y ratón | Adaptación multi-dispositivo |
| AR / VR | Gafas, smartphones | Movimiento, visual 3D | Inmersión, ergonomía, mareos |
| Gestual | Sensores, cámaras | Movimientos corporales | Precisión, aprendizaje de gestos |
| Voz | Altavoces, smartphones | Comandos de voz | Reconocimiento, contexto, ruido |

---

## 3. Usabilidad y experiencia de usuario

### 3.1 Definición y principios
**Usabilidad** = facilidad con la que un usuario aprende a usar un sistema, completa sus tareas y lo hace de forma satisfactoria y eficiente. Principios:

1. **Facilidad de aprendizaje** — entendible rápidamente por usuarios nuevos.
2. **Eficiencia de uso** — tareas rápidas para usuarios frecuentes.
3. **Memorabilidad** — retomar la interfaz tras un tiempo sin usarla.
4. **Tasa de errores baja** — minimizar errores y facilitar la recuperación.
5. **Satisfacción** — experiencia agradable que cumpla expectativas.

### 3.2 Usabilidad vs UX
No son lo mismo: la usabilidad se centra en lo *fácil y eficiente* que es usar el producto. La **UX** es más amplia: todas las percepciones, emociones y reacciones **antes, durante y después** del uso (incluye usabilidad + diseño emocional, accesibilidad, estética, rendimiento y contexto).

### 3.3 Métricas de evaluación

| Métrica | Qué mide | Ejemplo |
| --- | --- | --- |
| **Eficacia** | % de éxito al completar tareas | 8 de 10 lo logran → 80% |
| **Eficiencia** | Tiempo y recursos (clics, pasos) | menos pasos → mayor eficiencia |
| **Satisfacción** | Percepción del usuario | cuestionarios **SUS**, escalas **Likert** |

### 3.4 Heurísticas de Jakob Nielsen (10)

1. Visibilidad del estado del sistema.
2. Correspondencia entre el sistema y el mundo real.
3. Control y libertad del usuario (deshacer/rehacer).
4. Consistencia y estándares.
5. Prevención de errores.
6. Reconocer antes que recordar.
7. Flexibilidad y eficiencia (atajos).
8. Estética y diseño minimalista.
9. Ayudar a reconocer, diagnosticar y recuperarse de errores.
10. Ayuda y documentación.

### 3.5 Accesibilidad: principios básicos
- **Contraste adecuado** (textos y elementos distinguibles).
- **Navegación clara** por teclado o lectores de pantalla.
- **Diseño inclusivo**: no depender solo del color (error en rojo + icono/texto).
- **Tamaño de fuente legible**.
- **Compatibilidad con tecnologías asistivas** (lectores/ampliadores de pantalla).

---

## 4. Diseño visual y percepción

### 4.1 Teoría de la Gestalt
Explica cómo percibimos patrones y estructuras visuales — clave para interfaces entendibles de forma natural:

| Principio | Qué dice |
| --- | --- |
| Proximidad | Elementos cercanos se perciben como relacionados |
| Semejanza | Similares en forma/color/tamaño se agrupan visualmente |
| Continuidad | La mente sigue líneas y patrones continuos |
| Figura-fondo | Se distingue un objeto de su fondo para enfocar la atención |
| Cierre | La mente completa formas incompletas |
| Simetría | Lo simétrico se percibe como un mismo grupo |

### 4.2 Colorimetría
- **RGB**: modelo aditivo de pantallas (rojo, verde, azul).
- **HSL**: tono, saturación y luminosidad — útil para colores armónicos.
- **HEX**: código hexadecimal, estándar en diseño web.
- Psicología del color: rojo = energía/urgencia · azul = confianza/calma · verde = naturaleza/seguridad · amarillo = atención/advertencia.
- Contraste (legibilidad), armonía (combinaciones agradables) y accesibilidad (daltonismo).

### 4.3 Tipografía y legibilidad
La tipografía transmite emociones, mejora la legibilidad, establece jerarquía y construye identidad de marca (Helvetica de Panasonic, futura de Disney).

Tipos de fuentes: **Serif** (remates, formal: Times New Roman) · **Sans-serif** (sin remates, legible en pantalla: Arial, Helvetica) · **Monoespaciadas** (mismo ancho: Courier, programación) · **Caligráficas** (escritura a mano) · **Decorativas** (impacto visual sobre legibilidad).

Elementos de composición tipográfica: **tamaño**, **jerarquía** (pesos, negrita/cursiva), **interlineado** (espacio entre líneas) y **espaciado** (margen y padding).

### 4.4 Composición y coherencia visual
- **Rejillas**: estructuran el espacio de forma ordenada.
- **Alineación**: organiza los elementos y crea fluidez.
- **Márgenes**: evitan aglomeración.
- **Consistencia entre pantallas** (colores, tipografías, botones, iconos) → el usuario reconoce patrones y reduce la curva de aprendizaje.

### 4.5 Iconografía y semiótica visual
- **Metáforas visuales**: sobre = email, lupa = buscar.
- Lenguaje icónico **universal**, simples, claros y coherentes con el estilo del diseño.

---

## 5. Guías de estilo

### 5.1 ¿Qué son y para qué sirven?
Documento con las **reglas y recomendaciones de diseño visual e interacción** de un proyecto o marca, para garantizar coherencia independientemente de quién diseñe o desarrolle. Sirven para: imagen unificada, colaboración entre equipos, agilidad (pautas predefinidas), accesibilidad/usabilidad estandarizada y escalabilidad.

### 5.2 Elementos comunes
- **Paleta de colores** (principal, secundarios, de acento, con códigos HEX/RGB).
- **Tipografías** (fuentes autorizadas, tamaños, estilos, jerarquías).
- **Botones** (formas, tamaños, estados: normal/hover/clic/deshabilitado).
- **Iconos** (conjunto oficial, estilo lineal/relleno/flat).
- **Componentes** reutilizables (menús, formularios, tarjetas, modales).
- Y directrices de espaciado, estilos de texto, imágenes, animaciones y accesibilidad.

### 5.3 Ventajas
**Coherencia · Escalabilidad · Reutilización · Colaboración · Calidad**.

### 5.4 Ejemplos reales
- **Material Design** (Google) — diseño basado en materiales físicos, animaciones, profundidad.
- **Fluent UI** (Microsoft) — fluidez, accesibilidad, adaptabilidad.
- **Apple HIG** (Human Interface Guidelines) — simplicidad y claridad en macOS/iOS/watchOS/tvOS.

---

## 6. Componentes y estructuras de una interfaz

### 6.1 Componentes típicos
**Botones** (ejecutan acciones, con estados) · **Menús** (desplegables o fijos) · **Formularios** (entrada de datos con validaciones) · **Cuadros de diálogo** (emergentes que piden información o confirman) · **Sliders** (valores en un rango). También: pestañas, listas desplegables, barras de progreso, iconos interactivos.

### 6.2 Estructura de ventanas
- **Modales**: bloquean el resto de la interfaz hasta resolverlas (confirmaciones, formularios críticos).
- **No modales**: permiten interactuar con otras ventanas a la vez (ayuda, paneles flotantes).

### 6.3 SDI vs MDI
- **SDI** (Single Document Interface): un documento por ventana independiente (editores de texto).
- **MDI** (Multiple Document Interface): varios documentos dentro de una ventana principal (edición gráfica, IDEs).

### 6.4 Patrones de interacción
- **Consistencia**: diseño uniforme en estilos, comportamientos y nomenclaturas.
- **Feedback**: respuestas claras e inmediatas a las acciones.
- **Accesibilidad**: navegable por teclado, contraste, tamaños legibles, tecnologías de asistencia.

---

## 7. Planificación del diseño de la interfaz

Fases del proceso de planificación:

1. **Investigación del usuario** → **Personas**: perfiles/arquetipos que sintetizan características, motivaciones y objetivos de grupos de usuarios reales.
2. **Modelado conceptual** → tareas y necesidades + estructura lógica de contenidos y funciones.
3. **Flujos de navegación y diagramas** → rutas posibles entre pantallas según las acciones; diagramas de interacción (transiciones, estados, respuestas).
4. **Mapa de pantallas o módulos** → esquema de todas las pantallas y sus relaciones jerárquicas.
5. **Wireframes** → esquemas simplificados: disposición de elementos sin detalles gráficos (funcionalidad y jerarquía).
6. **Mockups** → maquetas visuales realistas con colores, tipografías e iconos finales.
7. **Documentación del diseño** → personas y casos de uso, diagramas, wireframes/mockups, normas, requisitos funcionales y de usabilidad.

> [!tip] Wireframe vs Mockup
> Wireframe = estructura en blanco y negro. Mockup = aspecto visual final. El orden del proceso es: investigación → modelado → flujos → mapa → wireframe → mockup → documentación.

---

## 8. Herramientas de diseño y prototipado (sin código)

Permiten crear representaciones visuales y funcionales sin programar, para comunicar, iterar y validar antes del desarrollo: **Figma, Adobe XD, Sketch, Pencil Project, Balsamiq, Canva**.

| Herramienta | Plataformas | Nivel de dificultad | Colaboración | Precio |
| --- | --- | --- | --- | --- |
| Figma | Web, Windows, Mac | Bajo - Medio | Sí | Gratis y suscripción |
| Adobe XD | Windows, Mac | Medio | Sí | Gratis y suscripción |
| Sketch | Mac | Medio | Limitada | Pago |
| Pencil Project | Windows, Mac, Linux | Bajo | No | Gratis |
| Balsamiq | Web, Windows, Mac | Bajo | Limitada | Pago |
| Canva | Web, Windows, Mac | Bajo - Medio | Sí | Gratis y suscripción |

Con ellas se puede: crear **wireframes**, desarrollar **mockups** y **prototipar interacciones** (flujos y transiciones).

---

## Esquema

- GUI = espacio visual de interacción → objetivos: interacción, información, confianza
- Tipos: escritorio · móvil · híbrida · AR/VR · gestual · voz
- Usabilidad (5 principios) ⊂ UX · métricas: eficacia, eficiencia, satisfacción · 10 heurísticas Nielsen · accesibilidad
- Percepción: Gestalt · color (RGB/HSL/HEX) · tipografía · composición · iconos
- Guías de estilo: Material, Fluent, HIG
- Componentes: modales/no modales · SDI/MDI · consistencia, feedback, accesibilidad
- Planificación: personas → modelado → flujos → mapa → wireframe → mockup → documentación
- Herramientas: Figma (la referente)

## Para repasar

- [ ] Diferencias entre usabilidad y UX
- [ ] Las 10 heurísticas de Nielsen
- [ ] Principios de la Gestalt aplicados al diseño
- [ ] SDI vs MDI y ventanas modales vs no modales
- [ ] Wireframe vs mockup
- [ ] Componentes de una guía de estilo y ejemplos reales
- [ ] Tipos de interfaces y sus retos (tabla 2.7)
