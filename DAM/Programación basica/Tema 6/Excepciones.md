---
asignatura: Programacion_basica
tema: 6
tipo: tema
estado: en curso
fecha: 2026-10-06
tags:
  - DAM/tema
  - DAM/programacion-basica/excepciones
---

# 6 · Excepciones

> [!info] Asignatura
> [[DAM/Programación basica/Indice|Programación básica]] · Tema 6 · Excepciones

## Índice del apartado

- [[#1. Introducción]]
- [[#2. Try-catch]]
- [[#3. Manejo de excepciones]]
- [[#4. Métodos de las excepciones]]
- [[#5. Cuándo se debe capturar una excepción]]
- [[#6. Tipos de excepciones]]
- [[#7. Throws]]
- [[#8. Orden de los catch]]
- [[#9. Throw]]
- [[#10. Finally]]

---

## 1. Introducción

Uno de los problemas más importantes al escribir aplicaciones es el tratamiento de los errores. Los errores detienen la ejecución del programa e impiden su desarrollo normal y, lo peor, además provocan que el usuario esté desinformado. Los programadores tiene que reconocer las situaciones que pueden provocar el fin de la ejecución normal del programa por un error no controlado. Dicho de otra forma, todos los posibles errores en un programa deben de estar controlados. A veces es imposible evitarlos (por ejemplo no hay papel en la impresora, o falla el disco duro), pero sí reaccionar de forma lógica para que el usuario reconozca lo que está ocurriendo.

Java nos echa una mano para ello a través de las excepciones. Se denomina **excepción** a un hecho que podría provocar la detención del programa; es decir una condición de error en tiempo de ejecución pero que puede ser controlable (a través de los mecanismos adecuados). En java sin embargo se denomina error a una condición de error incontrolable (ejemplos son el error que ocurre cuando no se dispone de más memoria o errores de sintaxis).

Los errores de sintaxis son detectados durante la compilación, pero los errores de ejecución pueden provocar situaciones irreversibles, su control debe hacerse también en tiempo de ejecución y eso siempre ha sido problemático para la programación de aplicaciones.

En Java se puede preparar el código susceptible a provocar excepciones de modo que si ocurre una excepción, el código es lanzado (throw) a una determinada rutina previamente preparada por el programador, que permite manipular esa excepción. Si la excepción no fuera capturada, la ejecución del programa se detendría irremediablemente (en muchas ocasiones la propia sintaxis de Java impide que la excepción no sea controlada; es decir, obliga a controlarla).

---

## 2. Try-catch

El control de las excepciones se realiza mediante las sentencias **try** y **catch**.

```java
try {

    instrucciones susceptibles de provocar una excepción

}

catch (ClaseExcepción1 objetoQueCapturaLaExcepción) {

    instrucciones que se ejecutan si hay un error de tipo ClaseExcepción1

}

catch (ClaseExcepción2 objetoQueCapturaLaExcepción) {

    instrucciones que se ejecutan si hay un error de tipo ClaseExcepción2

}

...
```

Como se puede observar, puede haber más de una sentencia catch para un mismo bloque try debido a que un bloque de código puede ser susceptible a provocar varios tipos diferentes de excepciones.

Dentro del bloque try se colocan las instrucciones susceptibles de provocar una excepción, el bloque catch sirve para capturar esa excepción y evitar el fin de la ejecución del programa. Desde el bloque catch se maneja, en definitiva, la excepción.

Cada catch maneja un tipo de excepción. Cuando se produce una excepción, se busca el catch que posea el manejador de excepción adecuado, será el que utilice el mismo tipo de excepción que se ha producido. La búsqueda del catch se realiza en el orden en que se han escrito. Si se produce una excepción, primero se mira si cuadra en el primer catch. Si no cuadra, se pasa al siguiente, y así sucesivamente. Por este motivo, es importante el orden en que se coloquen los bloques catch.

Cuando acaba la ejecución del bloque catch, el programa continúa con la ejecución del código que le sigue al bloque del try-catch.

Ejemplo:

```java
package tema6_Excepciones;

import java.util.InputMismatchException;

import java.util.Scanner;

public class TryCatch {

    @SuppressWarnings("resource")

    public void show() {

        final String FIN = "fin";

        int base, exponent;

        String baseString;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.println("Bienvenido al programa para calcular una potencia.");

            System.out.print("Introduce la base o fin para terminar: ");

            baseString = keyboard.nextLine();

            if (!baseString.toLowerCase().equals(FIN)) {

                base = Integer.parseInt(baseString);

                System.out.print("Introduce el exponente: ");

                exponent = keyboard.nextInt();

                System.out.printf("%d elevado a %d es igual a %d", base, exponent, (int) Math.pow(base, exponent));

            }

        } catch (NumberFormatException e) {

            System.err.println("Error en la base");

        } catch (InputMismatchException e) {

            System.err.println("Error en el exponente");

        }

    }

    public static void main(String[] args) {

        new TryCatch().show();

    }

}

Para la base, si el usuario no introduce _fin_ y tampoco introduce un número entero, el `Integer.parseInt` al intentar convertir la cadena a número lanzará una excepción de tipo `NumberFormatException` y será manejada por el catch correspondiente. Para el exponente, si se introduce algo que no sea un número (una letra, un símbolo...), se producirá una excepción de tipo `InputMismatchException` y se manejará por su correspondiente catch. Si se produce un error de otro tipo, el programa se detendrá.

En este ejemplo se está utilizando _encadenamiento de llamadas a métodos_: `if(!baseString.toLowerCase().equals(FIN))` ya que el método `toLowerCase` devuelve la cadena convertida en minúsculas a la cual se le aplica después el método `equals`. En este caso nos sirve para que el usuario pueda finalizar utilizando _fin_ tanto en minúsculas como en mayúsculas.

Puede ser que el programador quiera mostrar el mismo mensaje de error para ambas excepciones. En este caso se utiliza el **multi-catch**, incorporado en Java desde la versión 7:
```

```java
package tema6_Excepciones;

import java.util.InputMismatchException;

import java.util.Scanner;

public class MultiCatch {

    @SuppressWarnings("resource")

    public void show() {

        final String FIN = "fin";

        int base, exponent;

        String baseString;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.println("Bienvenido al programa para calcular una potencia.");

            System.out.print("Introduce la base o fin para terminar: ");

            baseString = keyboard.nextLine();

            if (!baseString.toLowerCase().equals(FIN)) {

                base = Integer.parseInt(baseString);

                System.out.print("Introduce el exponente: ");

                exponent = keyboard.nextInt();

                System.out.printf("%d elevado a %d es igual a %d", base, exponent, (int) Math.pow(base, exponent));

            }

        } catch (NumberFormatException | InputMismatchException e) {

            System.err.println("Error en la base o en el exponente");

        }

    }

    public static void main(String[] args) {

        new MultiCatch().show();

    }

}

En el eclipse, si seleccionamos varias líneas de código, las podemos fácilmente insertar en un bloque try-catch: Menú _Source → Surround with_.
```

---

## 3. Manejo de excepciones

En la programación de aplicaciones en general siempre ha habido dos formas de manejar una excepción:

- Interrupción: en este caso se asume que el programa ha encontrado un error irrecuperable. La operación que dio lugar a la excepción se anula y se entiende que no hay manera de regresar al código que provocó la excepción.
    
- Reanudación: se puede manejar el error y regresar de nuevo al código que provocó el error.
    

La filosofía de Java es del tipo interrupción, pero se puede intentar emular la reanudación encerrando el bloque try-catch en un bucle que se repetirá hasta que el error deje de existir. Ejemplo:

```java
package tema6_Excepciones;

import java.util.InputMismatchException;

import java.util.Scanner;

public class Resumption {

    @SuppressWarnings("resource")

    public void show() {

        byte number = 0;

        Scanner keyboard = new Scanner(System.in);

        boolean error = false;

        do {

            try {

                System.out.print("Introduce un número de tipo byte, es decir, entre -128 y 127: ");

                number = keyboard.nextByte();

                System.out.printf("Valor del número: %d\n", number);

                error = false; //Si se ha entrado antes en el catch, error está a true

            } catch (InputMismatchException e) {

                System.err.println("Error");

                error = true;

                keyboard.nextLine(); //Limpieza del buffer

            }

        } while (error);

    }

    public static void main(String[] args) {

        new Resumption().show();

    }

}
```

Si el usuario introduce cualquier cosa que no sea un número, el método `nextByte()` lanza la excepción `InputMismatchException` y lo que ha metido el usuario se queda en el buffer. Para solucionarlo, se realiza una limpieza del buffer con `keyboard.nextLine()`.

---

## 4. Métodos de las excepciones

- getMessage: obtiene el mensaje descriptivo de la excepción.
    
- toString: devuelve una cadena sobre la situación de la excepción. Suele indicar la clase de excepción y el texto de getMessage.
    
- printStackTrace: escribe el método y mensaje de la excepción (la llamada información de pila). El resultado es el mismo mensaje que muestra el ejecutor (la máquina virtual de Java) cuando no se controla la excepción.
    

```java
package tema6_Excepciones;

import java.util.Scanner;

import java.util.InputMismatchException;

import static tema1_11_EscrituraEnPantalla.colores.Colors.*;

public class MethodsOfExceptions {

    @SuppressWarnings("resource")

    public void show() {

        final String FIN = "fin";

        int base, exponent;

        String baseString;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.println("Bienvenido al programa para calcular una potencia.");

            System.out.print("Introduce la base o fin para terminar: ");

            baseString = keyboard.nextLine();

            if (!baseString.toLowerCase().equals(FIN)) {

                base = Integer.parseInt(baseString);

                System.out.print("Introduce el exponente: ");

                exponent = keyboard.nextInt();

                System.out.printf("%d elevado a %d es igual a %d", base, exponent, (int) Math.pow(base, exponent));

            }

        } catch (NumberFormatException e) {

            System.err.println(GREEN + e.getMessage() + RESET);

            System.err.println(CYAN + e.toString() + RESET);

            e.printStackTrace();

        } catch (InputMismatchException e) {

            System.err.println(GREEN + e.getMessage() + RESET);

            System.err.println(CYAN + e.toString() + RESET);

            e.printStackTrace();

        }

    }

    public static void main(String[] args) {

        new MethodsOfExceptions().show();

    }

}
```

---

## 5. Cuándo se debe capturar una excepción

Una excepción se debe capturar cuando no sea un error de programación. Es decir, el programador debe distinguir si esa excepción es un error suyo de programación o no, porque si es un error de programación, no debe capturar el error sino solucionarlo. Veamos un ejemplo con la excepción _StringIndexOutOfBoundsException_.

Cuando se intenta acceder a una parte de la cadena que no existe, por ejemplo, si a la cadena "_hola_" le hacemos un _charAt(4)_, java nos lanza la excepción _StringIndexOutOfBoundsException_. El programador no debe capturar con un try-catch la excepción sino que debe corregir el error de programación que ha producido dicha excepción. Veamos un ejemplo:

```java
package tema6_Excepciones;

public class StringIndexOutOfBoundsException1 {

    public void show() {

        String str = "hola";

        for (int i = 0; i <= str.length(); i++) {

            System.out.println(str.charAt(i));

        }

    }

    public static void main(String[] args) {

        new StringIndexOutOfBoundsException1().show();

    }

}

La salida por consola es la siguiente:

```text
h

o

l

a

Exception in thread "main" java.lang.StringIndexOutOfBoundsException: String index out of range: 4

    at java.base/java.lang.StringLatin1.charAt(StringLatin1.java:47)

    at java.base/java.lang.String.charAt(String.java:702)

    at tema6_1_Excepciones.StringIndexOutOfBoundsException1.show(StringIndexOutOfBoundsException1.java:9)

    at tema6_1_Excepciones.StringIndexOutOfBoundsException1.main(StringIndexOutOfBoundsException1.java:16)
```
```

El programador no debe solucionarlo con un try-catch:

```java
package tema6_Excepciones;

public class StringIndexOutOfBoundsException2 {

    public void show() {

        String str = "hola";

        try {

            for (int i = 0; i <= str.length(); i++) {

                System.out.println(str.charAt(i));

            }

        } catch (StringIndexOutOfBoundsException e) {//Esto no se debe hacer

            System.err.println("Esto no se debe hacer");

        }

    }

    public static void main(String[] args) {

        new StringIndexOutOfBoundsException2().show();

    }

}
```

Sino que debe corregir el error, es decir, quitar el = de la condición del for, ya que en la última iteración, _i_ toma el valor de _string.length_, que es 4, cuando el _charAt(4)_ no es un carácter válido ya que los caracteres válidos van de 0 a 3. Por lo tanto, el programador debe corregir el error:

```java
package tema6_Excepciones;

public class StringIndexOutOfBoundsException3 {

    public void show() {

        String str = "hola";

        for (int i = 0; i < str.length(); i++) {

            System.out.println(str.charAt(i));

        }

    }

    public static void main(String[] args) {

        new StringIndexOutOfBoundsException3().show();

    }

}
```

---

## 6. Tipos de excepciones

En Java, la **herencia** define una relación entre clases en la cual una clase posee características (métodos y propiedades) que proceden de otra. A la clase que posee las características a heredar se la llama **superclase** o **clase padre** y la clase que las hereda se llama **subclase** o **clase hija**. Lo beneficioso de este tipo de relaciones es que los hijos pueden heredar las características de los padres y luego aportar características propias convirtiéndose en una manera de reutilizar código muy eficiente.

Java utiliza muchísimo la herencia en las clases que conforman su API. En cuanto a las excepciones se refiere, existen tres tipos de excepciones que Java maneja a través de la herencia: errores, comprobadas (_checked_) y no comprobadas (_unchecked_). El gráfico que se muestra a continuación muestra el árbol de herencia de las excepciones en Java. El paquete de todas es java.lang:

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/exceptions.png)

La clase principal de la cual heredan todas las excepciones Java es Throwable. De ella nacen dos ramas: Error y Exception. Error representa errores de una magnitud tal que una aplicación nunca debería intentar realizar nada con ellos (como errores de la JVM, desbordamientos de buffer, etc). La segunda rama, encabezada por Exception, representa aquellos errores que normalmente sí solemos gestionar, y a los que comúnmente solemos llamar _excepciones_.

De Exception nacen múltiples ramas: ClassNotFoundException, IOException, ParseException, SQLException y otras muchas, todas ellas de tipo _checked_. La única excepción que es de tipo _unchecked_ es RuntimeException y encabeza todas las de este tipo.

**Excepciones checked**

Una excepción de tipo checked representa un error del cual técnicamente podemos recuperarnos. En ciertos momentos, a pesar de la promesa de recuperabilidad, nuestro código no estará preparado para gestionar la situación de error, o simplemente no será su responsabilidad. En estos casos lo más razonable es relanzar la excepción y confiar en que un método superior en la cadena de llamadas sepa gestionarla.

Por tanto, todas las excepciones de tipo checked deben ser capturadas o relanzadas. En el primer caso, utilizamos el bloque try-catch. En caso de querer relanzar la excepción, debemos declarar dicha intención en la firma de la función que contiene las sentencias que lanzan la excepción, y lo hacemos mediante la claúsula throws.

Hay que tener presente que cuando se relanza una excepción estamos forzando al código cliente de nuestro método a capturarla o relanzarla. Una excepción que sea relanzada una y otra vez hacia arriba terminará llegando al método primigenio y, en caso de no ser capturada por éste, producirá la finalización de su hilo de ejecución (thread).

La dos preguntas que debemos hacernos en este momento es: ¿Cuándo capturar una excepción? ¿Cuándo relanzarla? La respuesta es muy simple. Capturamos una excepción cuando:

- Podemos recuperarnos del error y continuar con la ejecución.
    
- Queremos registrar el error.
    
- Queremos relanzar el error con un tipo de excepción distinto.
    

En definitiva, cuando tenemos que realizar algún tratamiento del propio error. Por contra, relanzamos una excepción cuando:

- No es competencia nuestra ningún tratamiento de ningún tipo sobre el error que se ha producido.
    
- Para centralizar el control de excepciones y facilitar el mantenimiento del código.
    

**Excepciones unchecked**

Son excepciones de tipo RuntimeException o de cualquiera de sus subclases. El aspecto más destacado de las excepciones de tipo unchecked es que no deben ser forzosamente declaradas ni capturadas (en otras palabras, no son comprobadas). Por ello no son necesarios bloques try-catch ni declarar formalmente en la firma de la función el lanzamiento de excepciones de este tipo. Ésto, por supuesto, también afecta a funciones y/o clases más hacia arriba en la cadena invocante.

---

## 7. Throws

En caso de querer relanzar la excepción, debemos declarar dicha intención en la firma de la función que contiene las sentencias que lanzan la excepción, y lo hacemos mediante la claúsula throws.

¿Tiene obligación de tener un try-catch el que llame a la función? Si la excepción es de tipo RuntimeException o cualquiera de sus hijas, no existe la obligación de poner un try-catch. En cualquier otro caso, sí existe dicha obligación, de hecho si no se hace, Java da un error de compilación.

Ejemplo:

```java
package tema6_ThrowsThrowFinally;

import java.util.Scanner;

public class Throws {

    @SuppressWarnings("resource")

    public void show() {

        final String FIN = "fin", SIGUIENTE = "siguiente";

        int number;

        String str;

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Introduce un número o siguiente para pasar al siguiente número: ");

        str = keyboard.nextLine();

        if (!str.toLowerCase().equals(SIGUIENTE)) {

            /*

             * Aquí no estamos obligados a poner un try-catch porque 

             * NumberFormatException es hija de RuntimeException:

             */

            number = convertirNumero(str);

            System.out.printf("Valor del número introducido: %d\n", number);

        }

        try {

            System.out.print("Introduce un número o fin para terminar: ");

            str = keyboard.nextLine();

            if (!str.toLowerCase().equals(FIN)) {

                /*

                 * Aquí sí estamos obligados a poner un try-catch porque 

                 * Exception no es hija de RuntimeException:

                 */

                number = convertirNumero2(str);

                System.out.printf("Valor del número introducido: %d\n", number);

            }

        } catch (Exception e) {

            System.err.println("Error en el número");

        }

    }

    public int convertirNumero(String str) throws NumberFormatException {

        return Integer.parseInt(str);

    }

    public int convertirNumero2(String str) throws Exception {

        return Integer.parseInt(str);

    }

    public static void main(String[] args) {

        new Throws().show();

    }

}
```

---

## 8. Orden de los catch

Cuando se tienen varios catch para el mismo try, hay que tener la precaución de poner los catch de las subclases antes que los de las superclases porque si no, los catch de las subclases nunca se capturarían. Ejemplo:

```java
package tema6_ThrowsThrowFinally;

import java.util.InputMismatchException;

import java.util.Scanner;

public class CatchOrder1 {

    @SuppressWarnings("resource")

    public void show() {

        final String FIN = "fin";

        String str;

        byte number = 0;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.print("Introduce un número de tipo byte, es decir, entre -128 y 127: ");

            number = keyboard.nextByte();

            keyboard.nextLine(); //Limpieza del buffer

            System.out.printf("Valor del número introducido: %d\n", number);

            System.out.print("Introduzca otro número de tipo byte o fin para terminar: ");

            str = keyboard.nextLine();

            if (!str.toLowerCase().equals(FIN)) {

                number = Byte.parseByte(str);

                System.out.printf("Valor del otro número introducido: %d\n", number);

            }

        } catch (Exception e) {

            System.err.println("Error: no ha introducido un número entre -128 y 127");

        } catch (InputMismatchException e) {//Error de compilación: inalcanzable bloque catch

            System.err.println("Error");

        }

    }

    public static void main(String[] args) {

        new CatchOrder1().show();

    }

}
```

En este caso, Java da un error de compilación ya que InputMismatchException es hija de Exception. Si el usuario no introduce un número de tipo byte, se lanza una excepción de tipo InputMismatchException. Dicho objeto también es un objeto de tipo Exception, ya que los objetos de tipo hijo, también son objetos de tipo padre. Por lo tanto, nunca entraría en el catch del InputMismatchException. La solución es cambiar el orden de los catch:

```java
package tema6_ThrowsThrowFinally;

import java.util.InputMismatchException;

import java.util.Scanner;

public class CatchOrder2 {

    @SuppressWarnings("resource")

    public void show() {

        final String FIN = "fin";

        String str;

        byte number = 0;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.print("Introduce un número de tipo byte, es decir, entre -128 y 127: ");

            number = keyboard.nextByte();

            keyboard.nextLine(); //Limpieza del buffer

            System.out.printf("Valor del número introducido: %d\n", number);

            System.out.print("Introduzca otro número de tipo byte o fin para terminar: ");

            str = keyboard.nextLine();

            if (!str.toLowerCase().equals(FIN)) {

                number = Byte.parseByte(str);

                System.out.printf("Valor del otro número introducido: %d\n", number);

            }

        } catch (InputMismatchException e) {

            System.err.println("Error: no ha introducido un número entre -128 y 127");

        } catch (Exception e) {

            System.err.println("Error");

        }

    }

    public static void main(String[] args) {

        new CatchOrder2().show();

    }

}
```

---

## 9. Throw

Esta instrucción le permite al programador lanzar una excepción. El flujo del programa se dirigirá a la instrucción try-catch más cercana. Ejemplos:

- `throw new Exception();`
    
- `throw new Exception(“Error grave”);` Construye una excepción con el mensaje indicado. Ese mensaje se puede obtener en el catch con el método _getMessage_ del objeto que contiene la excepción. Ejemplo:
    

```java
package tema6_ThrowsThrowFinally;

import java.util.Scanner;

public class Throw {

    @SuppressWarnings("resource")

    public void show() {

        double n;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.println("Introduce un número: ");

            n = keyboard.nextDouble();

            division(n);

        } catch (ArithmeticException e) {

            System.err.println(e.getMessage());

        }

    }

    public void division(double n) {

        /*

         * float y double admiten Infinity por lo que no se lanza 

         * una excepción cuando se divide entre cero.

         * Podemos lanzar la excepción usando throw

         * */

        if (n == 0) {

            throw new ArithmeticException("Error: no se puede dividir entre cero");

        }

        System.out.printf("500 entre %.2f: %.2f\n", n, 500 / n);

    }

    public static void main(String[] args) {

        new Throw().show();

    }

}
```

---

## 10. Finally

Las instrucciones que se encuentran en el **finally** se ejecutan independientemente de si hubo o no excepción. Es decir, esas sentencias se ejecutan siempre. Si el código del try ha ido bien y no se ha lanzado ninguna excepción, después se ejecutan las instrucciones del _finally_ y luego se continúa por el código que le sigue al bloque del try-catch. Pero si se ha lanzado alguna excepción, se ejecutan las instrucciones del catch correspondiente, luego se ejecutan las instrucciones del _finally_ y luego se continúa por el código que le sigue al bloque del try-catch. Por lo tanto, se coloca en el bloque _finally_ código común para todas las excepciones y también para cuando no hay excepciones. Normalmente se suelen poner instrucciones de limpieza. Ejemplo:

```java
package tema6_ThrowsThrowFinally;

import java.util.InputMismatchException;

import java.util.Scanner;

public class Finally {

    @SuppressWarnings("resource")

    public void show() {

        int number = 0;

        String str;

        boolean error = false;

        Scanner keyboard = new Scanner(System.in);

        try {

            System.out.print("Introduce un número: ");

            number = keyboard.nextInt();

        } catch (InputMismatchException e) {

            System.err.println("Error");

            error = true;

        } finally {

            keyboard.nextLine();//Limpieza del buffer

        }

        System.out.print("Introduce una cadena: ");

        str = keyboard.nextLine();

        System.out.printf("El número introducido ha sido: %s\n", error ? "error" : number);

        System.out.printf("La cadena introducida ha sido: %s", str);

    }

    public static void main(String[] args) {

        new Finally().show();

    }

}
```

En el ejemplo, hay que limpiar el buffer haya o no una excepción, por lo tanto, se limpia en el _finally_.

Pero ¿qué diferencia hay entre poner código en el _finally_ o ponerlo después del bloque try-catch? Pues que en el _finally_ siempre se va a ejecutar aunque se rompa el flujo de ejecución, es decir, aunque exista por ejemplo un `return` en el _try_ o un `throw` en el _catch_. El código que se encuentre después del bloque try-catch, no se ejecutaría en esos casos.

## Esquema resumen de conceptos clave

| Concepto | Idea principal |
| --- | --- |
| Excepción | Situación anómala en ejecución que puede gestionarse mediante mecanismos de control. |
| `try-catch` | Delimita código susceptible de fallar y define cómo tratar excepciones capturadas. |
| Multi-catch | Permite tratar varios tipos de excepción en un mismo bloque `catch`. |
| Excepciones comprobadas | Deben capturarse o declararse con `throws`. |
| `throw` y `throws` | `throw` lanza una excepción; `throws` declara excepciones que un método puede propagar. |
| Orden de `catch` | Capturar subclases antes que superclases. |
| `finally` | Ejecuta limpieza tanto si se produce una excepción como si no. |

## Relaciones

- [[Programación orientada a objetos]] — control de invariantes mediante excepciones.
- [[1.2 · Funciones]] — declaración de excepciones en métodos con `throws`.

## Para repasar

- [ ] Estructurar bloques `try-catch` y utilizar multi-catch.
- [ ] Decidir cuándo capturar una excepción y cuándo corregir un error de programación.
- [ ] Diferenciar excepciones comprobadas y no comprobadas.
- [ ] Declarar excepciones con `throws` y lanzarlas con `throw`.
- [ ] Ordenar bloques `catch` desde la subclase a la superclase.
- [ ] Explicar cuándo se ejecuta `finally` y qué tareas ubicar en él.
