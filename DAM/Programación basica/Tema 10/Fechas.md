---
asignatura: Programacion_basica
tema: 10
tipo: tema
estado: en curso
fecha: 2026-10-06
tags:
  - DAM/tema
  - DAM/programacion-basica/fechas
---

# 10 · Fechas

> [!info] Asignatura
> [[DAM/Programación basica/Indice|Programación básica]] · Tema 10 · Fechas

## Índice del apartado

- [[#1. Introducción]]
- [[#2. Clase Locale]]
- [[#3. Métodos de la API de fechas]]
- [[#4. Enum DayOfWeek]]
- [[#5. Enum Month]]
- [[#6. Clase LocalDate]]
- [[#7. Clase YearMonth]]
- [[#8. Clase MonthDay]]
- [[#9. Clase Year]]
- [[#10. Clase LocalTime]]
- [[#11. Clase LocalDateTime]]
- [[#12. Clase DateTimeFormatter]]
- [[#13. Enum ChronoUnit]]
- [[#14. Clase Period]]
- [[#15. Clase Duration]]
- [[#16. Enum TimeUnit]]

---

## 1. Introducción

Java 8 introduce una nueva API para fechas y horas que es más fácil de leer, más amplia que la API anterior y thread-safe, es decir, los objetos se pueden utilizar con seguridad desde varios hilos de ejecución.

Esta API se introduce para cubrir los siguientes inconvenientes de la anterior:

1. La API anterior no es thread-safe por lo que los desarrolladores tienen que hacer frente a problemas de concurrencia durante el uso de la fecha. La nueva API de fecha y hora es inmutable y no tiene métodos setter. Al ser inmutables, no necesitan ser clonadas.
    
2. Dificultad para manejar zona-horaria en la API anterior.
    

En java 8 se crea un nuevo paquete para el manejo de fechas, se trata del paquete `java.time`. Las clases definidas en este paquete representan los principales conceptos de fecha - hora, incluyendo instantes, fechas, horas, períodos, zonas de tiempo, etc. Están basados en el sistema de calendario ISO, el cual es el calendario mundial _de-facto_ que sigue las reglas del calendario Gregoriano.

---

## 2. Clase Locale

Hay que destacar la importancia y el valor de respetar el idioma y la región geográfica del usuario al desarrollar aplicaciones de software. Permitir que el usuario se comunique con el software en su propio idioma es un gran impulso para las ventas del software. Cuando se trata de Java, es el concepto de configuración regional de Java lo que explica el proceso de internacionalización.

La configuración regional de Java consta de tres elementos principales: idioma, país y variantes. Las variantes son personalizaciones adicionales que pueden representar una jerga específica, un dialecto o cualquier ajuste que sea relevante para una aplicación específica en un entorno particular. Las variantes la utilizan los proveedores de software, ya sean sistemas operativos o navegadores, para funcionalidades adicionales.

En Java se utiliza la clase `Locale` del paquete `java.util` como una localización, es decir, representa una región geográfica, política o cultural específica. Una operación que requiere una localización para realizar su tarea se denomina sensible a la localización y utiliza la localización para adaptar la información al usuario. Por ejemplo, mostrar un número es una operación sensible a la configuración regional: el número debe formatearse de acuerdo con las costumbres y convenciones del país, región o cultura del usuario. Estas clases utilizan el objeto `Locale` para conocer qué configuración regional se está utilizando en la aplicación y se personalizan en cuanto a cómo formatear y presentar los datos al usuario. Por ejemplo, la clase `NumberFormat`, que puede devolver un número como 302 400 para Francia, 302 .400 para Alemania y 302, 400 para los Estados Unidos. También son clases sensibles a la configuración regional `DecimalFormat` y `DateTimeFormatter`.

Hay tres métodos estáticos disponibles para la creación de objetos `Locale`:

- `Locale.of(String language)`: utiliza solamente el idioma. En este caso, al no indicar un país, la aplicación no podrá adaptarse a las diferencias regionales del idioma. Ejemplo que indica que el idioma es inglés, pero no especifica un país o región en particular:
    
    Locale locale = Locale.of("en");
    
- `Locale.of(String language, String country)`: utiliza tanto el idioma como el país. Ejemplo que indica que el idioma es inglés y el país Estados Unidos. Esto permite a la aplicación adaptarse a las convenciones locales de Estados Unidos:
    
    Locale locale = Locale.of("en", "US");
    
- `Locale.of(String language, String country, String variant)`: utiliza el idioma, el país y la variante. Ejemplo:
    
    Locale locale = Locale.of("en", "US", "SiliconValley");
    

Los códigos se pueden encontrar en [https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry):

- _Type: language_: son los códigos de idioma.
    
- _Type: region_: son los códigos de país.
    
- _Type: variant_: son los códigos de la variante.
    

Los códigos de variante no conforman un estándar sino que son arbitrarios y específicos de la aplicación. Si existen variaciones en el idioma utilizado dentro del mismo país, se puede especificar una variante. Por ejemplo, en el Sur de Estados Unidos, la gente suele decir "y'all," cuando en el Norte dicen "you all." Se podría crear diferentes objetos Locale de esta forma:

Locale localeNorth = Locale.of("en", "US" ,"NORTH");

Locale localeSouth = Locale.of("en", "US", "SOUTH");

Si se crean objetos _Locale_ con los códigos de variante NORTH y SOUTH, como en el ejemplo anterior, solo nuestra aplicación sabrá como tratarlos.

Normalmente, se específican códigos de variante para identificar diferencias causadas por la plataforma de ordenador. Por ejemplo, las diferencias de fuentes podría forzar a utilizar caracteres diferentes en Windows y en UNIX. Se podría definir los objetos **Locale** con estos códigos de variante:

Locale localeUnix = Locale.of("de", "DE" ,"UNIX");

Locale localeWindows = Locale.of("de", "DE", "WINDOWS");

Tal y como podemos observar en la API, la clase _Locale_ tiene constantes predefinidas para algunos idiomas y países. Por ejemplo, **JAPAN** es la constante del país Japón mientras que **JAPANESE** es la constante del idioma japonés. Se puede crear un objeto _Locale_ utilizando una constante:

Locale l1 = Locale.JAPAN;//Se crea un objeto Locale con el idioma japonés y país Japón

Locale l2 = Locale.JAPANESE;// Se crea un objeto Locale con el idioma japonés 

Si no se asigna un objeto _Locale_ a un objeto sensible a la localidad, entonces se utiliza la localización por defecto, la cual se puede conocer con el método `getDefault()`, que obtiene el valor actual de la configuración regional por defecto para esa instancia de la Máquina Virtual de Java. La máquina virtual de Java establece la configuración regional por defecto durante el inicio basándose en el entorno del host. Se puede cambiar utilizando el método _setDefault_.

```java
package tema10_Fechas;

import java.util.Locale;

public class ClassLocale {

    public void show() {

        Locale l = Locale.getDefault();

        System.out.println(l.toString());

    }

    public static void main(String[] args) {

        new ClassLocale().show();

    }

}
```

Salida por consola:

```text
es_ES
```

---

## 3. Métodos de la API de fechas

Muchas de las clases de la API de fechas contienen los siguientes métodos:

- Métodos estáticos `of`: se utilizan para crear instancias de objetos de fecha y hora con literales y constantes enum sin la necesidad de utilizar constructores. Ejemplo:
    
    LocalDate localDate = LocalDate.of(2024, Month.AUGUST, 15);
    
- Métodos `plus` y `minus`: se utilizan para realizar operaciones de suma y resta respectivamente sobre objetos de fecha y hora. Ejemplos:
    
    Month month = Month.APRIL;
    
    Month month1 = month.plus(3);//JULY
    
    LocalDate localDate = LocalDate.of(2024, Month.AUGUST, 15);//2024-08-15
    
    LocalDate localDate1 = localDate.plusDays(5);//2024-08-20
    
- Métodos estáticos `now`: se utilizan para obtener la fecha y la hora actuales del sistema basándose en el reloj del sistema del entorno en el que se ejecuta la aplicación. Ejemplos:
    
    LocalDate localDate = LocalDate.now();
    
    Year year = Year.now();
    
- Métodos `parse`: se utilizan para crear objetos de fecha y hora a partir de cadenas. Ejemplos:
    
    LocalDate localDate = LocalDate.parse("2024-03-22");
    
    Year year = Year.parse("2024");
    
- Métodos `get`: se utilizan para obtener componentes específicos de un objeto de fecha y hora. Ejemplos:
    
    LocalDate date = LocalDate.of(2024, 2, 8);
    
    int year = date.getYear(); //Obtiene el año 2024
    
    int month = date.getMonthValue(); //Obtiene el mes 2
    
    int day = date.getDayOfMonth(); //Obtiene el día 8
    
    LocalTime time = LocalTime.of(15, 30, 25);
    
    int hour = time.getHour(); //Obtiene la hora 15
    
    int minute = time.getMinute(); //Obtiene el minuto 30
    
    int second = time.getSecond(); //Obtiene el segundo 25
    
- Métodos `between`: se utilizan para calcular la diferencia entre dos objetos de fecha y hora. Estos métodos permiten calcular la cantidad de tiempo transcurrido entre dos puntos en el tiempo, expresados en unidades específicas como días, meses, años, horas, minutos, etc. Ejemplos:
    
    long days = ChronoUnit.DAYS.between(localDate1, localDate2);
    
    Period period = Period.between(localDate1, localDate2);

---

## 4. Enum DayOfWeek

En el enum `DayOfWeek` del paquete `java.time` se definen los días de la semana con el siguiente conjunto de constantes:

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY

Podemos crear variables de tipo _DayOfWeek_ y asignarle una instancia del enum a través de dichas constantes:

DayOfWeek day1;//day1 es una variable del tipo de enumeración DayOfWeek

day1 = DayOfWeek.MONDAY;//Se le asigna la instancia del lunes a través de la constante MONDAY

También podemos crear una instancia del enum con el método estático `static DayOfWeek of(int dayOfWeek)`, que obtiene una instancia de _DayOfWeek_ a partir de un valor _int_ del 1 (lunes) al 7 (domingo).

DayOfWeek day2;//day2 es una variable del tipo de enumeración DayOfWeek

day2 = DayOfWeek.of(1);//Se le asigna la instancia del lunes a través del método of

Este enum contiene métodos que permiten manipular días hacia adelante y hacia atrás:

- `DayOfWeek plus(long days)`: devuelve el día de la semana que es el número especificado de días después de éste.
    
- `DayOfWeek minus(long days)`: devuelve el día de la semana que es el número especificado de días antes de éste.
    

DayOfWeek day3, day4;

day3 = day1.plus(4);//Viernes

day4 = day2.minus(2);//Sábado

Este enum contiene también el método `String getDisplayName(TextStyle style,Locale locale)` que devuelve la representación textual utilizada para identificar el día de la semana adecuada para su presentación al usuario. Los parámetros controlan el estilo del texto devuelto y la configuración regional. El estilo del texto se representa con el enum `TextStyle` donde se definen tres tamaños para el texto formateado: `full`, `short` y `narrow`.

```java
package tema10_Fechas;

import java.time.DayOfWeek;

import java.time.format.TextStyle;

import java.util.Locale;

public class EnumDayOfWeek {

    public void show() {

        DayOfWeek day1, day2, day3, day4;//Variables del tipo de enumeración DayOfWeek

        day1 = DayOfWeek.MONDAY;//Se le asigna la instancia del lunes a través de la constante MONDAY

        day2 = DayOfWeek.of(1);//Se le asigna la instancia del lunes a través del método of

        day3 = day1.plus(4);//Viernes

        day4 = day2.minus(2);//Sábado

        System.out.printf("day1: %s, day2: %s, day3: %s, day4: %s",day1,day2,day3,day4);

        Locale l = Locale.of("es", "ES");//idioma español castellano, país España

        System.out.printf("\nTextStyle.FULL:%s\n", day1.getDisplayName(TextStyle.FULL, l));

        System.out.printf("TextStyle.NARROW:%s\n", day1.getDisplayName(TextStyle.NARROW, l));

        System.out.printf("TextStyle.SHORT:%s\n", day1.getDisplayName(TextStyle.SHORT, l));

    }

    public static void main(String[] args) {

        new EnumDayOfWeek().show();

    }

}
```

Salida por consola:

```text
day1: MONDAY, day2: MONDAY, day3: FRIDAY, day4: SATURDAY

TextStyle.FULL: lunes

TextStyle.NARROW: L

TextStyle.SHORT: lun
```

---

## 5. Enum Month

En el enum `Month` del paquete `java.time` se definen los meses con el siguiente conjunto de constantes:

JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER

También tiene los métodos `of`, `plus`, `minus` y `getDisplayName` como el enumerado de días de la semana. Además, contiene métodos para conocer el número de días máximos y mínimos de cada mes:

- `int minLength()`: obtiene la duración mínima de este mes en días. Febrero tiene una duración mínima de 28 días. Abril, junio, septiembre y noviembre tienen 30 días. Todos los demás meses tienen 31 días.
    
- `int maxLength()`: obtiene la duración máxima de un mes en días. Febrero tiene una duración máxima de 29 días. Abril, junio, septiembre y noviembre tienen 30 días. Todos los demás meses tienen 31 días.
    

```java
package tema10_Fechas;

import java.time.Month;

import java.time.format.TextStyle;

import java.util.Locale;

public class EnumMonth {

    public void show() {

        Month month1, month2, month3, month4;//Variables del tipo de enumeración Month

        month1 = Month.APRIL;//Se le asigna la instancia del mes de abril a través de la constante APRIL

        month2 = Month.of(2);//Se le asigna la instancia del mes de febrero a través del método of

        month3 = month1.plus(4);//Agosto

        month4 = month2.minus(3);//Noviembre

        System.out.printf("month1: %s, month2: %s, month3: %s, month4: %s",month1,month2,month3,month4);

        System.out.printf("\n%s tiene como mínimo %d días y como máximo %d días",month2,month2.minLength(),month2.maxLength());

        System.out.printf("\n%s tiene como mínimo %d días y como máximo %d días",month1,month1.minLength(),month1.maxLength());

        System.out.printf("\n%s tiene como mínimo %d días y como máximo %d días",month3,month3.minLength(),month3.maxLength());

        Locale l = Locale.of("es", "ES");//idioma español castellano, país España

        System.out.printf("\nTextStyle.FULL: %s\n", month1.getDisplayName(TextStyle.FULL, l));

        System.out.printf("TextStyle.NARROW: %s\n", month1.getDisplayName(TextStyle.NARROW, l));

        System.out.printf("TextStyle.SHORT: %s\n", month1.getDisplayName(TextStyle.SHORT, l));

    }

    public static void main(String[] args) {

        new EnumMonth().show();

    }

}
```

Salida por consola:

```text
month1: APRIL, month2: FEBRUARY, month3: AUGUST, month4: NOVEMBER

FEBRUARY tiene como mínimo 28 días y como máximo 29 días

APRIL tiene como mínimo 30 días y como máximo 30 días

AUGUST tiene como mínimo 31 días y como máximo 31 días

TextStyle.FULL: abril

TextStyle.NARROW: A

TextStyle.SHORT: abr
```

---

## 6. Clase LocalDate

La clase `LocalDate` del paquete `java.time` nos permite registrar fechas específicas inmutables.

```java
package tema10_Fechas;

import java.time.LocalDate;

public class ClassLocalDate {

    public void show() {

        LocalDate currentDate, concertDate, parseDate;

        currentDate = LocalDate.now();//Se obtiene la fecha actual

        System.out.printf("Fecha actual: %s", currentDate);

        System.out.printf(", es decir, día %s del mes %s del año %s.", currentDate.getDayOfMonth(),

                currentDate.getMonthValue(), currentDate.getYear());

        concertDate = LocalDate.of(2022, 8, 13);//Obtiene una instancia de LocalDate a partir de un año, mes y día

        System.out.printf("\n\nEl concierto es el %s.", concertDate);

        System.out.println(" Las entradas se podrán comprar como máximo hasta");

        System.out.printf("5 días antes, es decir, hasta el %s.", concertDate.minusDays(5));

        parseDate = LocalDate.parse("2022-02-22");//Obtiene un LocalDate a partir de una cadena

        System.out.printf("\n\nFecha obtenida a partir de una cadena: %s", parseDate);

    }

    public static void main(String[] args) {

        new ClassLocalDate().show();

    }

}
```

Salida por consola:

```text
Fecha actual: 2022-02-03, es decir, día 3 del mes 2 del año 2022.

El concierto es el 2022-08-13. Las entradas se podrán comprar como máximo hasta

5 días antes, es decir, hasta el 2022-08-08.

Fecha obtenida a partir de una cadena: 2022-02-22
```

---

## 7. Clase YearMonth

Con la clase `YearMonth` del paquete `java.time` podemos generar objetos inmutables que representan la combinación de un año y un mes.

Tiene el método `int lengthOfMonth()` que devuelve la duración del mes en días.

```java
package tema10_Fechas;

import java.time.Month;

import java.time.YearMonth;

public class ClassYearMonth {

    public void show() {

        YearMonth currentYearMonth, ofYearMonth, parseYearMonth;

        currentYearMonth = YearMonth.now();//Se obtiene el YearMonth actual

        System.out.printf("Este año-mes es %s y tiene %d días", currentYearMonth, currentYearMonth.lengthOfMonth());

        ofYearMonth = YearMonth.of(2004, Month.FEBRUARY);//Obtiene una instancia YearMonth a partir de un año y un mes

        System.out.printf("\n\nEl año-mes %s tuvo %d días", ofYearMonth, ofYearMonth.lengthOfMonth());

        ofYearMonth = YearMonth.of(2010, Month.FEBRUARY);

        System.out.printf("\nEl año-mes %s tuvo %d días", ofYearMonth, ofYearMonth.lengthOfMonth());

        ofYearMonth = YearMonth.of(2000, Month.FEBRUARY);

        System.out.printf("\nEl año-mes %s tuvo %d días", ofYearMonth, ofYearMonth.lengthOfMonth());

        parseYearMonth = YearMonth.parse("2022-12");//Obtiene un YearMonth a partir de una cadena

        System.out.printf("\n\nAño-mes obtenido a partir de una cadena: %s", parseYearMonth);

    }

    public static void main(String[] args) {

        new ClassYearMonth().show();

    }

}
```

Salida por consola:

```text
Este año-mes es 2022-02 y tiene 28 días

El año-mes 2004-02 tuvo 29 días

El año-mes 2010-02 tuvo 28 días

El año-mes 2000-02 tuvo 29 días

Año-mes obtenido a partir de una cadena: 2022-12
```

---

## 8. Clase MonthDay

Con la clase `MonthDay` del paquete `java.time` podemos generar objetos inmutables que representan la combinación de un día y un mes.

```java
package tema10_Fechas;

import java.time.Month;

import java.time.MonthDay;

public class ClassMonthDay {

    public void show() {

        MonthDay currentMonthDay, ofMonthDay, parseMonthDay;

        currentMonthDay = MonthDay.now();//Se obtiene el MonthDay actual

        System.out.printf("Este día es %s, es decir, día %d del mes %d", currentMonthDay,

                currentMonthDay.getDayOfMonth(), currentMonthDay.getMonthValue());

        ofMonthDay = MonthDay.of(Month.FEBRUARY, 29);//Obtiene una instancia MonthDay a partir de un mes y un día

        System.out.printf("\n\nEl día %s del mes %s%s es válido para el año 2004", ofMonthDay.getDayOfMonth(),

                ofMonthDay.getMonthValue(), ofMonthDay.isValidYear(2004) ? "" : " no");

        System.out.printf("\nEl día %s del mes %s%s es válido para el año 2010", ofMonthDay.getDayOfMonth(),

                ofMonthDay.getMonthValue(), ofMonthDay.isValidYear(2010) ? "" : " no");

        parseMonthDay = MonthDay.parse("--12-03");//Obtiene un MonthDay a partir de una cadena

        System.out.printf("\n\nMes-día obtenido a partir de una cadena: %s", parseMonthDay);

    }

    public static void main(String[] args) {

        new ClassMonthDay().show();

    }

}
```

Salida por consola:

```text
Este día es --02-07, es decir, día 7 del mes 2

El día 29 del mes 2 es válido para el año 2004

El día 29 del mes 2 no es válido para el año 2010

Mes-día obtenido a partir de una cadena: --12-03
```

---

## 9. Clase Year

Con la clase `Year` del paquete `java.time` podemos generar objetos inmutables que representan un año concreto.

Tiene métodos como:

- `boolean isLeap()`: devuelve un booleano indicando si el año es bisiesto.
    
- `boolean isBefore(Year other)`: comprueba si el año es anterior al año del parámetro.
    
- `boolean isAfter(Year other)`: comprueba si el año es posterior al año del parámetro.
    

```java
package tema10_Fechas;

import java.time.Year;

public class ClassYear {

    public void show() {

        Year currentYear, ofYear, parseYear;

        currentYear = Year.now();//Obtiene el año actual

        System.out.printf("Este año es %s y %s es bisiesto\n", currentYear, currentYear.isLeap() ? "sí" : "no");

        ofYear = Year.of(2012);//Obtiene una instancia Year a partir de un año

        System.out.printf("\nEl año %s es %s al año actual", ofYear,

                ofYear.isBefore(currentYear) ? "anterior" : "posterior");

        parseYear = Year.parse("2021");//Obtiene un Year a partir de una cadena

        System.out.printf("\n\nAño obtenido a partir de una cadena: %s", parseYear);

    }

    public static void main(String[] args) {

        new ClassYear().show();

    }

}
```

Salida por consola:

```text
Este año es 2022 y no es bisiesto

El año 2012 es anterior al año actual

Año obtenido a partir de una cadena: 2021
```

---

## 10. Clase LocalTime

Con la clase `LocalTime` del paquete `java.time` podemos generar objetos inmutables que representan una hora concreta.

```java
package tema10_Fechas;

import java.time.LocalTime;

public class ClassLocalTime {

    public void show() {

        LocalTime currentTime, meetingTime, parseTime;

        currentTime = LocalTime.now();//Se obtiene la hora actual

        System.out.printf("Hora actual: %s", currentTime);

        System.out.printf("\nHora: %s Minutos: %s Segundos: %s Nanosegundos: %s", currentTime.getHour(),

                currentTime.getMinute(), currentTime.getSecond(), currentTime.getNano());

        meetingTime = LocalTime.of(10, 15);//Obtiene una instancia de LocalTime indicando hora y minutos

        System.out.printf("\n\nHora de la reunión: %s", meetingTime);

        parseTime = LocalTime.parse("11:45:30");//Obtiene un LocalTime a partir de una cadena

        System.out.printf("\n\nHora obtenida a partir de una cadena: %s", parseTime);

    }

    public static void main(String[] args) {

        new ClassLocalTime().show();

    }

}
```

Salida por consola:

```text
Hora actual: 08:56:53.868514995

Hora: 8 Minutos: 56 Segundos: 53 Nanosegundos: 868514995

Hora de la reunión: 10:15

Hora obtenida a partir de una cadena: 11:45:30
```

---

## 11. Clase LocalDateTime

Con la clase `LocalDateTime` del paquete `java.time` podemos generar objetos inmutables que representan una fecha y hora concretas.

```java
package tema10_Fechas;

import java.time.LocalDateTime;

public class ClassLocalDateTime {

    public void show() {

        LocalDateTime currentDateTime, meetingDateTime, parseDateTime;

        currentDateTime = LocalDateTime.now();//Se obtiene la fecha y hora actual

        System.out.printf("Fecha y hora actual: %s", currentDateTime);

        System.out.printf("\nDía del año: %s", currentDateTime.getDayOfYear());

        System.out.printf("\nDía de la semana: %s", currentDateTime.getDayOfWeek());

        System.out.printf("\nHora: %s", currentDateTime.getHour());

        System.out.printf("\nNanosegundos: %s", currentDateTime.getNano());

        meetingDateTime = LocalDateTime.of(2022, 11, 16, 9, 30, 45);//Obtiene una instancia de LocalDateTime a partir de un año,mes,día,hora,minutos y segundos

        System.out.printf("\n\nLa reunión es %s", meetingDateTime);

        System.out.printf("\nFecha de la reunión: %s", meetingDateTime.toLocalDate());

        System.out.printf("\nHora de la reunión: %s", meetingDateTime.toLocalTime());

        parseDateTime = LocalDateTime.parse("2022-12-03T10:15:30");//Obtiene un LocalDateTime a partir de una cadena

        System.out.printf("\n\nFecha y hora obtenida a partir de una cadena: %s", parseDateTime);

    }

    public static void main(String[] args) {

        new ClassLocalDateTime().show();

    }

}
```

Salida por consola:

```text
Fecha y hora actual: 2022-02-04T13:48:19.851351656

Día del año: 35

Día de la semana: FRIDAY

Hora: 13

Nanosegundos: 851351656

La reunión es 2022-11-16T09:30:45

Fecha de la reunión: 2022-11-16

Hora de la reunión: 09:30:45

Fecha y hora obtenida a partir de una cadena: 2022-12-03T10:15:30
```

---

## 12. Clase DateTimeFormatter

La clase `DateTimeFormatter` del paquete `java.time.format` se utiliza para dar formato a las fechas.

Se puede indicar el formato con:

- formatos predefinidos.
    
- creando patrones que se basan en una secuencia de letras y símbolos.
    

En la API podemos encontrar dichos formatos predefinidos y el significado de las letras y símbolos para crear un patrón. Veamos algunos:

- d: día del mes. Posibilidades:
    
    - `d`: si el día tiene un dígito, se muestra solamente ese dígito. Ejemplo: `7`. Si tiene dos dígitos, se muestran los dos. Ejemplo: `27`.
        
    - `dd`: si el día tiene un dígito, se muestra el dígito con un cero a la izquierda. Ejemplo: `07`. Si tiene dos dígitos, se muestran los dos. Ejemplo: `27`.
        
    - Más de dos: salta la excepción `IllegalArgumentException`.
        
- M: mes del año. Posibilidades:
    
    - `M`: si el mes tiene un dígito, se muestra solamente ese dígito. Ejemplo: `7`. Si tiene dos dígitos, se muestran los dos. Ejemplo: `11`.
        
    - `MM`: si el mes tiene un dígito, se muestra el dígito con un cero a la izquierda. Ejemplo: `07`. Si tiene dos dígitos, se muestran los dos. Ejemplo: `11`.
        
    - `MMM`: se muestra en formato `short`. Ejemplo: `jul`.
        
    - `MMMM`: se muestra en formato `full`. Ejemplo: `julio`.
        
    - `MMMMM`: se muestra en formato `narrow`. Ejemplo: `J`. Hay que tener en cuenta que los meses que empiecen con la misma letra, les va a salir la misma letra en el formato _narrow_. Por ejemplo, junio y julio van a tener la letra `J` así como marzo y mayo, que van a tener la letra `M`.
        
    - Más de 5: salta la excepción `IllegalArgumentException`.
        
- G: era. Hay dos eras:
    
    - Current Era (CE): era actual, es decir, después de Cristo.
        
    - Before Current Era (BCE): antes de la era actual, es decir, antes de Cristo.
        
    
    Posibilidades:
    
    - `G`, `GG`, `GGG`: _anno Dómini_(CE) y _antes de Cristo_(BCE).
        
    - `GGGG` : _después de Cristo_(CE) y _antes de Cristo_(BCE).
        
    - `GGGGG`: _d. C._(CE) y _a. C._(BCE).
        
    - Más de 5: salta la excepción `IllegalArgumentException`.
        
- u: año proléptico. Posibilidades:
    
    - `u`, `uuu`, `uuuu`: muestra el año con 4 dígitos.
        
    - `uu`: muestra el año con 2 dígitos.
        
    - Más de 4: se rellena con ceros a la izquierda.
        
- y: año de la era. Posibilidades:
    
    - `y`, `yyy`, `yyyy`: muestra el año con 4 dígitos.
        
    - `yy`: muestra el año con 2 dígitos.
        
    - Más de 4: se rellena con ceros a la izquierda.
        

¿qué diferencia existe entre `y` y `u`?:

En la era actual CE, `y` y `u` funcionan igual. La diferencia existe en los años de la era BCE, donde el año proléptico puede ser cero o negativo pero el año de la era no:

- Año proléptico: el año proléptico 0 es el 1 a.C., el año proléptico -1 es el 2 a.C., el año proléptico -2 es el 3 a.C., y así sucesivamente.
    
- Año de la era: el año aumenta en 1 a medida que el tiempo retrocede. El año de la era 1 es el 1 a.C., el año de la era 2 es el 2 a.C., el año de la era 3 es el 3 a.C., y así sucesivamente.
    

Los métodos `parse` que hemos visto en clases anteriores están sobrecargados para utilizarlos con un formato concreto.

Dispone del método `format` que devuelve una cadena con el formato especificado.

```java
package tema10_Fechas;

import java.time.LocalDate;

import java.time.LocalDateTime;

import java.time.format.DateTimeFormatter;

public class ClassDateTimeFormatter {

    public void show() {

        LocalDateTime localDateTime;

        LocalDate localDate = LocalDate.of(2023, 7, 9);

        LocalDate localDateEra = LocalDate.of(1, 1, 1);//1 de enero del año 1

        //Formato predefinido ISO_ORDINAL_DATE: año y día del año

        DateTimeFormatter formatter = DateTimeFormatter.ISO_ORDINAL_DATE;

        System.out.printf("Formato predefinido ISO_ORDINAL_DATE: %s", formatter.format(localDate));

        //Creación de patrones basados en secuencia de letras y símbolos

        formatter = DateTimeFormatter.ofPattern("G d M y");

        System.out.printf("\n\nPatrón \"%s\": %s", "G d M y", formatter.format(localDate));

        formatter = DateTimeFormatter.ofPattern("GG d/MM/yy");

        System.out.printf("\nPatrón \"%s\": %s", "GG d/MM/yy", formatter.format(localDate));

        formatter = DateTimeFormatter.ofPattern("GGG d MMM yyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGG d MMM yyy", formatter.format(localDate));

        formatter = DateTimeFormatter.ofPattern("GGGG dd-MMMM-yyyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd-MMMM-yyyy", formatter.format(localDate));

        formatter = DateTimeFormatter.ofPattern("GGGGG dd-MMMMM-yyyyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGGGG dd-MMMMM-yyyyy", formatter.format(localDate));

        //Era CE

        System.out.print("\n\nAño 1 d.C:");

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/uuuu");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/uuuu", formatter.format(localDateEra));

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/yyyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/yyyy", formatter.format(localDateEra));

        //Era BCE

        localDateEra = localDateEra.minusYears(1);

        System.out.print("\n\nAño 1 a.C:");

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/uuuu");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/uuuu", formatter.format(localDateEra));

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/yyyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/yyyy", formatter.format(localDateEra));

        localDateEra = localDateEra.minusYears(1);

        System.out.print("\n\nAño 2 a.C:");

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/uuuu");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/uuuu", formatter.format(localDateEra));

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/yyyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/yyyy", formatter.format(localDateEra));

        localDateEra = localDateEra.minusYears(1);

        System.out.print("\n\nAño 3 a.C:");

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/uuuu");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/uuuu", formatter.format(localDateEra));

        formatter = DateTimeFormatter.ofPattern("GGGG dd/MM/yyyy");

        System.out.printf("\nPatrón \"%s\": %s", "GGGG dd/MM/yyyy", formatter.format(localDateEra));

        //Uso de método parse con formato

        formatter = DateTimeFormatter.ofPattern("d MMMM yy HH:mm:ss");

        localDateTime = LocalDateTime.parse("7 febrero 22 10:01:30", formatter);

        System.out.printf("\n\nFecha y hora obtenida a partir de una cadena y un formato: %s", localDateTime);

    }

    public static void main(String[] args) {

        new ClassDateTimeFormatter().show();

    }

}
```

Salida por consola:

```text
Formato predefinido ISO_ORDINAL_DATE: 2023-190

Patrón "G d M y": anno Dómini 9 7 2023

Patrón "GG d/MM/yy": anno Dómini 9/07/23

Patrón "GGG d MMM yyy": anno Dómini 9 jul 2023

Patrón "GGGG dd-MMMM-yyyy": después de Cristo 09-julio-2023

Patrón "GGGGG dd-MMMMM-yyyyy": d. C. 09-J-02023

Año 1 d.C:

Patrón "GGGG dd/MM/uuuu": después de Cristo 01/01/0001

Patrón "GGGG dd/MM/yyyy": después de Cristo 01/01/0001

Año 1 a.C:

Patrón "GGGG dd/MM/uuuu": antes de Cristo 01/01/0000

Patrón "GGGG dd/MM/yyyy": antes de Cristo 01/01/0001

Año 2 a.C:

Patrón "GGGG dd/MM/uuuu": antes de Cristo 01/01/-0001

Patrón "GGGG dd/MM/yyyy": antes de Cristo 01/01/0002

Año 3 a.C:

Patrón "GGGG dd/MM/uuuu": antes de Cristo 01/01/-0002

Patrón "GGGG dd/MM/yyyy": antes de Cristo 01/01/0003

Fecha y hora obtenida a partir de una cadena y un formato: 2022-02-07T10:01:30
```

En el método `DateTimeFormatter.ofPattern` se puede combinar texto literal (es decir, frases que queremos que se muestren tal cual) con patrones de formato (como dd, MMMM, yyyy, HH:mm:ss, etc.). Para que el texto literal no se interprete como parte del patrón, se debe escribir entre comillas simples `'`. Ejemplo:

```java
package tema10_Fechas;

import java.time.LocalDateTime;

import java.time.format.DateTimeFormatter;

public class ClassDateTimeFormatter2 {

    public void show() {

        LocalDateTime now = LocalDateTime.now();

        DateTimeFormatter textAndPatternMix = DateTimeFormatter.ofPattern("'Hoy es' EEEE dd-MMMM-yyyy 'a las' HH:mm:ss");

        System.out.println(now.format(textAndPatternMix));

    }

    public static void main(String[] args) {

        new ClassDateTimeFormatter2().show();

    }

}
```

Salida por consola:

```text
Hoy es jueves 03-julio-2025 a las 23:20:28
```

---

## 13. Enum ChronoUnit

En este enum se definen un conjunto estándar de unidades de períodos de fecha, como por ejemplo, _DAYS, MONTHS, WEEKS, YEARS, HOURS, MINUTES, SECONDS_, etc.

```java
package tema10_Fechas;

import java.time.LocalDateTime;

import java.time.Month;

import java.time.temporal.ChronoUnit;

public class EnumChronoUnit {

    public void show() {

        LocalDateTime currentDateTime, concertDateTime;

        currentDateTime = LocalDateTime.of(2023, Month.JANUARY, 22, 17, 30);

        concertDateTime = LocalDateTime.of(2023, Month.AUGUST, 13, 21, 30);

        System.out.printf("Quedan para el concierto: %d meses o %d días o %d horas o %d minutos o %d segundos",

                ChronoUnit.MONTHS.between(currentDateTime, concertDateTime),

                ChronoUnit.DAYS.between(currentDateTime, concertDateTime),

                ChronoUnit.HOURS.between(currentDateTime, concertDateTime),

                ChronoUnit.MINUTES.between(currentDateTime, concertDateTime),

                ChronoUnit.SECONDS.between(currentDateTime, concertDateTime));

    }

    public static void main(String[] args) {

        new EnumChronoUnit().show();

    }

}
```

Salida por consola:

```text
Quedan para el concierto: 6 meses o 203 días o 4876 horas o 292560 minutos o 17553600 segundos
```

---

## 14. Clase Period

Esta clase modela un período de tiempo en términos de años, meses y días.

```java
package tema10_Fechas;

import java.time.LocalDate;

import java.time.Period;

public class ClassPeriod {

    public void show() {

        Period period;

        LocalDate oldDate, currentDate;

        oldDate = LocalDate.of(1988, 9, 28);

        currentDate = LocalDate.now();

        period = Period.between(oldDate, currentDate);//Obtiene una instancia de Period a partir de dos fechas

        System.out.printf("Período entre %s y %s: son %d años, %d meses y %d días. ", oldDate, currentDate,

                period.getYears(), period.getMonths(), period.getDays());

        System.out.printf("En total son %d meses.", period.toTotalMonths());

        period = Period.ofWeeks(50);//Obtiene una instancia de Period de 50 semanas

        System.out.printf("\n\n50 semanas son %d días.", period.getDays());

    }

    public static void main(String[] args) {

        new ClassPeriod().show();

    }

}
```

Salida por consola:

```text
Período entre 1988-09-28 y 2022-02-07: son 33 años, 4 meses y 10 días. En total son 400 meses.

50 semanas son 350 días.
```

---

## 15. Clase Duration

Esta clase modela un período de tiempo en términos de unidades de tiempo, como años, meses, días, horas, minutos, segundos y nanosegundos.

```java
package tema10_Fechas;

import java.time.Duration;

public class ClassDuration {

    public void show() {

        Duration duration;

        duration = Duration.ofMinutes(10);

        System.out.printf("Minutos: %d", duration.toMinutes());

        System.out.printf("\nSegundos: %d", duration.toSeconds());

        System.out.printf("\nNanosegundos: %d", duration.toNanos());

    }

    public static void main(String[] args) {

        new ClassDuration().show();

    }

}
```

Salida por consola:

```text
Minutos: 10

Segundos: 600

Nanosegundos: 600000000000
```

---

## 16. Enum TimeUnit

Con este enum se representan duraciones de tiempo en una determinada unidad. Proporciona métodos de utilidad para convertir entre unidades y para realizar operaciones de temporización y retraso.

```java
package tema10_Fechas;

import java.util.concurrent.TimeUnit;

public class EnumTimeUnit {

    public void show() {

        try {

            for (int i = 0; i < 5; i++) {

                System.out.printf("Iteración %d\n", i);

                TimeUnit.SECONDS.sleep(2);//Se duerme durante 2 segundos

            }

        } catch (InterruptedException e) {

            System.err.println("Interrupción mientras se duerme");

        }

    }

    public static void main(String[] args) {

        new EnumTimeUnit().show();

    }

}
```

## Esquema resumen de conceptos clave

| Concepto | Idea principal |
| --- | --- |
| `Locale` | Representa idioma y región para adaptar formato y presentación de datos. |
| Fecha y hora | Tipos como `LocalDate`, `LocalTime` y `LocalDateTime` representan componentes inmutables. |
| Formato | `DateTimeFormatter` convierte entre fechas/horas y cadenas siguiendo patrones o formatos ISO. |
| `ChronoUnit` | Calcula diferencias entre fechas y horas en unidades específicas. |
| `Period` y `Duration` | Representan cantidades de tiempo basadas en fechas y en tiempo, respectivamente. |
| `DayOfWeek`, `Month`, `TimeUnit` | Enums para días, meses y unidades temporales. |

## Relaciones

- [[Expresiones regulares]] — análisis y validación de cadenas que contienen fechas.
- [[1.4 Cadenas]] — conversión y formato textual de fechas y horas.
- [[Programación orientada a objetos]] — clases inmutables y objetos de la API `java.time`.

## Para repasar

- [ ] Elegir clase adecuada para fecha, hora o combinación de ambas.
- [ ] Crear objetos desde valores y analizar cadenas.
- [ ] Formatear y mostrar fechas con `DateTimeFormatter` y `Locale`.
- [ ] Calcular diferencias con `ChronoUnit`, `Period` y `Duration`.
- [ ] Usar enums de calendario y conversión entre unidades temporales.
