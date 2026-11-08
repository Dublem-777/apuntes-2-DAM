---
asignatura: SGE
tema: 5
tipo: ejercicio
estado: completo
fecha: 2026-11-05
tags:
  - DAM/ejercicio
  - DAM/sge/kpi
  - DAM/sge/business-intelligence
---

# KPI y toma de decisiones basada en datos

**Grupo:** Sergio Casado Sánchez, Alejandro Vega García y Daniel Madrid Mérida
**Escenarios desarrollados:** 1, 2 y 3

---

## Escenario 1. Ayuntamiento de una ciudad mediana

> [!question] Escenario
> El ayuntamiento recibe muchas quejas por tráfico, contaminación y ruido, pero no tiene información suficiente para decidir en qué zonas invertir primero ni para comprobar si las medidas actuales funcionan.

### Parte 1. Análisis del problema

**Problema principal:** el ayuntamiento decide sin datos fiables. No sabe qué zonas están peor ni si sus medidas sirven, así que puede invertir donde no hace falta.

**Datos y fuentes:**

| Dato | Fuente |
| --- | --- |
| Intensidad de tráfico y atascos por calle y hora | Sensores y cámaras de tráfico, datos de navegadores (Google Maps) |
| Niveles de contaminación (NO₂, partículas PM10/PM2,5) | Estaciones de medición de calidad del aire |
| Niveles de ruido por zona y franja horaria | Sonómetros instalados en la vía pública |
| Quejas de los vecinos (tipo, zona, fecha) | Registro municipal, web y app de incidencias |
| Uso del transporte público y la bici | Validaciones de tarjetas de transporte y bici pública |

### Parte 2. Propuesta de KPI

| KPI propuesto | ¿Qué mide? | ¿Cómo se calcula o mide? | ¿Para qué sirve? |
| --- | --- | --- | --- |
| **KPI 1 · Índice de calidad del aire** | La contaminación de cada zona | Media diaria de NO₂ y PM10 (µg/m³) de cada estación, comparada con los límites legales | Saber qué zonas superan los límites y deben tener prioridad |
| **KPI 2 · Nivel medio de ruido** | El ruido de cada zona | Media de decibelios (dB) por zona en horario de día y de noche | Detectar puntos negros de ruido y comprobar si bajan tras actuar |
| **KPI 3 · Quejas por cada 1.000 habitantes** | El malestar vecinal por zona | (Nº de quejas en la zona ÷ habitantes de la zona) × 1.000 | Comparar barrios de distinto tamaño y medir si los vecinos notan la mejora |

### Parte 3. Toma de decisiones

**Medidas:** crear zonas de bajas emisiones en los barrios más contaminados, reforzar el transporte público y los carriles bici, regular semáforos según el tráfico real y poner asfalto silencioso o limitar la velocidad en las calles más ruidosas.

**Uso de los KPI:** medir cada KPI antes de actuar, fijar un objetivo (por ejemplo, bajar un 15 % el NO₂ en un año) y comparar mes a mes la zona donde se actúa con otras similares en las que no. Si no mejora, se cambia la medida.

**Por qué con datos:** las quejas solo reflejan a quien se queja; los sensores muestran la situación real de toda la ciudad. Con datos se invierte primero donde más falta hace y se justifica el gasto de dinero público.

<div style="page-break-after: always;"></div>

## Escenario 2. Universidad «Horizonte»

> [!question] Escenario
> Cada año aumenta el número de estudiantes que abandonan antes de empezar el segundo curso. El equipo directivo quiere usar los datos para encontrar las causas y prevenir el abandono.

### Parte 1. Análisis del problema

**Problema principal:** cada vez más alumnos de primero dejan la carrera y la universidad no sabe por qué. Pierde alumnos, ingresos y prestigio, y los estudiantes pierden tiempo y dinero.

**Datos y fuentes:**

| Dato | Fuente |
| --- | --- |
| Notas, asignaturas aprobadas y suspensas por alumno | Sistema de gestión académica |
| Asistencia a clase y uso del aula virtual | Control de asistencia, registros de Moodle |
| Perfil del alumno (nota de acceso, vía de acceso, si trabaja, si tiene beca) | Datos de matrícula y de becas |
| Satisfacción con la carrera, el profesorado y los servicios | Encuestas a los alumnos |
| Motivo del abandono | Encuesta o entrevista de baja |

### Parte 2. Propuesta de KPI

| KPI propuesto | ¿Qué mide? | ¿Cómo se calcula o mide? | ¿Para qué sirve? |
| --- | --- | --- | --- |
| **KPI 1 · Tasa de abandono en primer curso** | El % de alumnos que no se matriculan en segundo | (Alumnos de 1º que no se matriculan al curso siguiente ÷ alumnos matriculados en 1º) × 100 | Medir el problema por carrera y ver su evolución año a año |
| **KPI 2 · Tasa de rendimiento** | El éxito académico del alumno | (Créditos aprobados ÷ créditos matriculados) × 100 | Detectar alumnos en riesgo: un rendimiento bajo en el primer cuatrimestre suele anticipar el abandono |
| **KPI 3 · Tasa de actividad en el aula virtual** | La implicación del alumno | % de alumnos que no entran en Moodle o no entregan tareas en las últimas 2 semanas | Avisar a tiempo de alumnos que se están desconectando |

### Parte 3. Toma de decisiones

**Medidas:** un sistema de alerta temprana con los KPI 2 y 3, tutorías y mentorías con alumnos de cursos superiores para los alumnos en riesgo, cursos de refuerzo en las asignaturas con más suspensos y más becas u horarios flexibles para quienes trabajan.

**Uso de los KPI:** comparar la tasa de abandono y de rendimiento de los alumnos que reciben tutoría con los que no, y la de este curso con la de cursos anteriores. Si el abandono baja, se amplía la medida a más carreras.

**Por qué con datos:** cada profesor puede tener su propia explicación del abandono (falta de nivel, de interés, problemas económicos), pero solo los datos dicen cuál pesa más en cada carrera. Así se ayuda a los alumnos antes de que se vayan y no cuando ya es tarde.

<div style="page-break-after: always;"></div>

## Escenario 3. Hospital público regional

> [!question] Escenario
> El hospital tiene largas listas de espera y urgencias suele estar saturado. La dirección quiere reorganizar los recursos para reducir los tiempos de espera y mejorar la atención sin aumentar los costes.

### Parte 1. Análisis del problema

**Problema principal:** los recursos (personal, camas, quirófanos) no están organizados según la demanda real. Por eso hay saturación en urgencias y esperas largas, y empeora la atención a los pacientes.

**Datos y fuentes:**

| Dato | Fuente |
| --- | --- |
| Llegadas a urgencias por día y hora, y nivel de gravedad (triaje) | Sistema informático de urgencias |
| Tiempos de espera hasta ser atendido y hasta el alta | Historia clínica electrónica, registros de admisión |
| Ocupación de camas y quirófanos | Sistema de gestión hospitalaria |
| Pacientes en lista de espera y días de espera por especialidad | Registro de listas de espera |
| Turnos y número de profesionales | Sistema de recursos humanos |
| Satisfacción de los pacientes | Encuestas tras la atención |

### Parte 2. Propuesta de KPI

| KPI propuesto | ¿Qué mide? | ¿Cómo se calcula o mide? | ¿Para qué sirve? |
| --- | --- | --- | --- |
| **KPI 1 · Tiempo medio de espera en urgencias** | La rapidez de la atención urgente | Media de minutos entre la llegada del paciente y la primera atención médica, por nivel de gravedad | Ver en qué horas y días hay saturación para reforzar personal en esos momentos |
| **KPI 2 · Demora media en lista de espera** | La espera para consultas y operaciones | Media de días desde que se incluye al paciente en la lista hasta que se le atiende, por especialidad | Saber qué especialidades necesitan más recursos o reorganizar su agenda |
| **KPI 3 · Tasa de ocupación de camas** | El aprovechamiento de las camas | (Camas ocupadas ÷ camas disponibles) × 100 | Detectar falta de camas (más del 90 %) o camas infrautilizadas que se pueden redistribuir |

> [!tip] Calidad de la atención
> Para medir la calidad se puede añadir la **tasa de reingresos en 30 días** (% de pacientes que vuelven a ingresar tras el alta) y la **satisfacción del paciente** en las encuestas.

### Parte 3. Toma de decisiones

**Medidas:** adaptar los turnos del personal de urgencias a las horas punta, crear una vía rápida para los casos leves, usar los quirófanos también por la tarde para reducir listas de espera y agilizar las altas para liberar camas antes.

**Uso de los KPI:** seguirlos en un cuadro de mando diario y mensual, comparar los valores antes y después de cada cambio y fijar objetivos (por ejemplo, bajar de 3 a 2 horas la espera media en urgencias). Si un cambio sube los costes o empeora otro KPI, se revisa.

**Por qué con datos:** sin aumentar el presupuesto, la única forma de mejorar es usar mejor lo que ya hay, y para eso hay que saber exactamente dónde y cuándo faltan recursos. Además, en un servicio público las decisiones tienen que poder justificarse con hechos.

---

## Relacionado

- [[1.3 - Sistemas de información de gestión]]
- [[1.2 - La gestión empresarial]]
