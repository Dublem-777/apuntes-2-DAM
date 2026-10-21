---
asignatura: Programacion_basica
tema: 12
tipo: tema
estado: en curso
fecha: 2026-10-06
tags:
  - DAM/tema
  - DAM/programacion-basica/colecciones
---

# 12 · Colecciones

> [!info] Asignatura
> [[DAM/Programación basica/Indice|Programación básica]] · Tema 12 · Colecciones

## Índice del apartado

- [[#1. Introducción]]
- [[#2. Interfaz Collection]]
- [[#3. Interfaz List]]
- [[#4. Clase ArrayList]]
- [[#5. Método join]]
- [[#6. Invarianza, covarianza y contravarianza]]
- [[#7. Iteradores]]
- [[#8. Métodos equals y hashCode]]
- [[#9. Colecciones sin duplicados]]
  - [[#9.1 Clase HashSet]]
  - [[#9.2 Clase LinkedHashSet]]
  - [[#9.3 Clase EnumSet]]
- [[#10. Mapas]]
  - [[#10.1 Clase HashMap]]
  - [[#10.2 Clase LinkedHashMap]]
  - [[#10.3 Ejemplo de uso de un mapa en un enum]]
  - [[#10.4 Clase EnumMap]]
- [[#11. Árboles]]
  - [[#11.1 Clase TreeSet]]
  - [[#11.2 Clase TreeMap]]
- [[#12. Pilas y colas]]
  - [[#12.1 Clase ArrayDeque]]
- [[#13. Clase Collections]]

---

## 1. Introducción

Una colección representa un grupo de objetos. Esto objetos son conocidos como elementos. Cuando queremos trabajar con un conjunto de elementos, necesitamos un almacén donde poder guardarlos.

Las colecciones son estructuras de datos con la peculiaridad de que son estructuras dinámicas. Esto quiere decir que pueden aumentar o disminuir su tamaño dependiendo de los elementos que almacenan, lo que suponen una mejora respecto a las estructuras de datos estáticas cuyo tamaño se define en su creación y no se puede alterar en tiempo de ejecución, como por ejemplo, los arrays.

El API de Java nos proporciona en el paquete `java.util` el framework de las colecciones, que nos permite utilizar diferentes estructuras de datos para almacenar y recuperar objetos de cualquier clase. Java tiene desde la versión 2, todo un juego de clases e interfaces para guardar colecciones de objetos donde todas las entidades conceptuales están representadas por interfaces y las clases se usan para proveer implementaciones de esas interfaces. Estas clases e interfaces están estructuradas en una jerarquía.

Antes de que aparecieran los genéricos, en las colecciones se almacenaba cualquier objeto que heredara de `Object`. Pero esto presenta ciertos inconvenientes:

- Podríamos tener una colección con objetos completamente distintos, lo que puede dar lugar a problemas ya que en todo momento deberíamos saber qué tipo de objeto y en qué posición de la colección se encuentra el elemento con el que queremos trabajar, de otro modo podríamos tener incongruencias en el código o incluso hacer saltar una excepción.
    
- Otro inconveniente es que tendríamos que hacer continuos castings para poder trabajar con los elementos de la colección, lo cual resulta tedioso y poco productivo.
    

Veamos un ejemplo para obtener la suma de los valores almacenados en una lista. La clase `ArrayList` es una colección de Java para listas de elementos, con el método `add` se añaden elementos a la lista y con `get(int index)` se obtiene un elemento de la posición _index_:

int total = 0;

ArrayList numbers = new ArrayList();//Creación de la lista

numbers.add(1);//Se añade el elemento 1 a la lista utilizando el método add

numbers.add(2);

numbers.add(3);

for (int i = 0; i < numbers.size(); i++) {

  // Nos vemos a obligados a hacer casting, dado que numbers.get(i) retorna un Object:

  total += (int) numbers.get(i);

}

System.out.printf("Total: %d\n", total);

Como vemos en el ejemplo anterior, nos vemos obligados a hacer explícitamente un casting cuando obtenemos un elemento de la lista, dado que la lista internamente trabaja con elementos de la clase `Object`. No hay ningún contrato que permita a la clase `ArrayList` saber con qué tipo de datos queremos que trabaje.

Además, es posible añadir elementos de distinto tipo a la misma lista, con el agravante de que más adelante cuando se intente acceder al elemento y se haga un casting sobre él se producirá un error en tiempo de ejecución. Así, si modificamos el ejemplo anterior de la siguiente manera:

int total = 0;

ArrayList numbers = new ArrayList();

numbers.add(1);

numbers.add(2);

numbers.add("Antonio");

for (int i = 0; i < numbers.size(); i++) {

  /* Esta línea lanza una excepción en tiempo de ejecución cuando

     se trata de convertir a entero el elemento "Antonio" */

  total += (int) numbers.get(i);

}

System.out.printf("Total: %d\n", total);

Así pues, para resolver este problema, a partir de la versión 5 de Java se empezaron a utilizar los **genéricos**. Los genéricos nos permiten establecer un tipo con el que vamos a trabajar en esa colección, de esa manera podemos evitar los problemas mencionados anteriormente.

Por ejemplo, la clase `ArrayList` es una colección de Java para listas de elementos. Si observamos en la API esta clase, se define como `ArrayList<E>`. Esto significa que es una clase genérica donde E es el tipo genérico. Cuando se instancie un objeto de esta clase, hay que indicar el tipo concreto que se va a utilizar:

ArrayList<String> list = new ArrayList<>();

Cualquier método que se ejecute sobre la variable _list_ se hará traduciendo la letra genérica _E_ por _String_ en el código del método.

Para mantener la compatibilidad con las versiones anteriores a Java 5, podemos trabajar con colecciones sin tipo pero se recomienda **siempre utilizar las colecciones parametrizadas**, por ejemplo siempre utilizar `ArrayList<E>` y nunca `ArrayList`.

Así el ejemplo anterior podríamos modificarlo de la siguiente manera:

int total = 0;

ArrayList<Integer> numbers = new ArrayList<>();

numbers.add(1);

numbers.add(2);

/* La siguiente línea da un error de compilación, dado que el compilador

   detecta que estamos intentando añadir una cadena a una lista de 

   enteros: */

numbers.add("Antonio");

for (int i = 0; i < numbers.size(); i++) {

  /* Ya no es necesario hacer un cast explícito, dado que el compilador 

     lo hará internamente por nosotros, al haberle informado de que 

     queríamos trabajar con una lista de enteros: */

  total += numbers.get(i);

}

System.out.printf("Total: %d\n", total);

Como vemos en el ejemplo anterior, gracias a la información que le suministramos al compilador sobre el tipo de lista con el que queremos trabajar, en este caso `Integer`, el compilador es capaz de detectar en tiempo de compilación que no debería ser posible añadir una cadena a la lista, y además nos evita tener que hacer explícitamente el casting a entero cuando obtenemos los elementos de la lista, porque ya lo puede hacer él internamente por nosotros.

---

## 2. Interfaz Collection

Es la interfaz raíz de la jerarquía de las colecciones. Java no proporciona ninguna implementación directa de esta interfaz, sino que proporciona implementaciones de subinterfaces más específicas como _Set_ y _List_. Esta interfaz se utiliza normalmente para pasar colecciones y manipularlas cuando se desea la máxima generalidad.

Veamos algunos de los métodos que podemos observar en la API:

- `boolean add(E e)`: añade el elemento _e_ a la colección.
    
- `boolean addAll(Collection<? extends E> c)`: añade todos los elementos de la colección _c_.
    
- `void clear()`: elimina todos los elementos de la colección.
    
- `boolean contains(Object o)`: comprueba si el elemento _o_ está en la colección.
    
- `boolean containsAll(Collection<?> c)`: comprueba si todos los elementos de _c_ están en la colección.
    
- `boolean isEmpty()`: comprueba si la colección está vacía.
    
- `boolean remove(Object o)`: elimina de la colección el elemento _o_.
    
- `boolean removeAll(Collection<?> c)`: elimina de la colección todos los elementos de _c_.
    
- `boolean retainAll(Collection<?> c)`: elimina de la colección todos los elementos exceptos los que están en _c_, es decir, obtiene la intersección.
    
- `int size()`: devuelve el tamaño de la colección.

---

## 3. Interfaz List

Esta interfaz es una subinterfaz o interfaz hija de _Collection_, por lo tanto, tiene todos los métodos de _Collection_ y además añade los suyos propios.

Este tipo de colección se refiere a listas en las que los elementos de la colección tienen un orden, es decir, existe una secuencia de elementos. Cada elemento tiene un índice o posición. El primer elemento ocupa la posición 0.

La interfaz List sí admite elementos duplicados.

Veamos algunos de los métodos que podemos observar en la API:

- `void add(int index, E element)`: inserta el elemento _E_ en la posición _index_.
    
- `boolean add(E e)`: añade el elemento _e_ al final de la lista.
    
- `boolean addAll(int index, Collection<? extends E> c)`: inserta todos los elementos de _c_ en la posición _index_.
    
- `boolean addAll(Collection<? extends E> c)`: añade todos los elementos de _c_ al final de la lista.
    
- `E get(int index)`: devuelve el elemento de la posición _index_.
    
- `int indexOf(Object o)`: devuelve el índice de la primera ocurrencia del elemento _o_ en la lista, o -1 si la lista no contiene el elemento.
    
- `int lastIndexOf(Object o)`: devuelve el índice de la última ocurrencia del elemento _o_ en la lista, o -1 si la lista no contiene el elemento.
    
- `E remove(int index)`: elimina el elemento que se encuentra en la posición _index_.
    
- `E set(int index, E element)`: reemplaza el elemento que se encuentra en _index_ por el elemento _element_.
    
- `List<E> subList(int fromIndex, int toIndex)`: devuelve la sublista comprendida entre las posiciones _fromIndex_ incluida y _toIndex_ excluida.
    
- Métodos estáticos `of`: devuelven listas no modificables formadas por los elementos recibidos por parámetro. Está sobrecargado varias veces para admitir desde 0 a 10 elementos incluso hay una versión para recibir un _vararg_.
    

Existen varios tipos de implementaciones realizadas dentro de la plataforma Java para la interfaz _List_, como por ejemplo, _ArrayList_.

---

## 4. Clase ArrayList

Se basa en un array redimensionable que aumenta su tamaño según crece la colección de elementos. Lo bueno es que el tiempo de acceso a un elemento en particular es ínfimo. Lo malo es que si queremos eliminar un elemento del principio o del medio, la clase debe mover todos los que le siguen a la posición anterior, para tapar el agujero que deja el elemento removido. Esto hace que sacar elementos del medio o del principio sea costoso.

ArrayList mantiene el orden de inserción, es decir, si recorremos la colección se nos mostrará en el mismo órden en que insertamos los objetos.

Veamos un ejemplo de declaración e inicialización:

ArrayList<Integer> list = new ArrayList<Integer>();

A partir de java7, no es necesario indicar el genérico en la inicialización:

ArrayList<Integer> list = new ArrayList<>();

Para hacer el código más genérico, se puede definir la variable de tipo interfaz, ya que dicho código podría funcionar con cualquier clase que implemente la interfaz, simplemente habría que cambiar el `new`:

List<Integer> list = new ArrayList<>();

Veamos un ejemplo de _ArrayList_ donde utiliza métodos tanto de _Collection_ como de _List_:

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.List;

public class ShowArrayList {

    public void show() {

        List<Integer> list1 = new ArrayList<>();

        List<Integer> list2;

        List<Integer> list3;

        List<Integer> list4;

        list1.add(1);

        list1.add(2);//Se añaden los elementos al final de la lista

        list1.add(6);

        list1.add(2, 5);//Se añade el 5 en la posición 2

        for (Integer i : list1) {//Recorremos la lista con un bucle for-each: 1  2  5  6

            System.out.printf(" %d ", i);

        }

        System.out.println();

        list2 = List.of(3,4);

        list1.addAll(2, list2);//Se inserta list2 en la posición 2 de list1

        for (Integer i : list1) {// 1  2  3  4  5  6 

            System.out.printf(" %d ", i);

        }

        System.out.println();

        list3 = List.of(7,8);

        list1.addAll(list3);//Se inserta list3 al final de list1

        for (Integer i : list1) {// 1  2  3  4  5  6  7  8

            System.out.printf(" %d ", i);

        }

        System.out.printf("\nEl elemento de la posición 3 es: %d", list1.get(3));//4

        System.out.printf("\nEl elemento 4 se encuentra en la posición %d", list1.indexOf(4));//3

        list1.add(4);//Se añade un 4 al final de list1

        System.out.printf("\nLa posición del 4 en list1 por el final es: %d\n", list1.lastIndexOf(4));//8

        list1.remove(8);//Se elimina el elemento de la posición 8, que es el último 4 insertado

        for (Integer i : list1) {// 1  2  3  4  5  6  7  8

            System.out.printf(" %d ", i);

        }

        list1.set(6, 8);//Se reemplaza el elemento que se encuentra en la posición 6 por un 8

        System.out.println();

        for (Integer i : list1) {// 1  2  3  4  5  6  8  8

            System.out.printf(" %d ", i);

        }

        System.out.printf("\nLa sublista comprendida entre las posiciones 2 y 5 es: ");

        for (Integer i : list1.subList(2, 6)) {// 3  4  5  6

            System.out.printf(" %d ", i);

        }

        System.out.printf("\nEl 4 %s se encuentra en list1", list1.contains(4) ? "sí" : "no");//sí

        System.out.printf("\nEl 9 %s se encuentra en list1", list1.contains(9) ? "sí" : "no");//no

        //list1: 1  2  3  4  5  6  8  8

        //list2: 3  4

        //list3: 7  8

        System.out.printf("\nTodos los elementos de list2 %s se encuentran en list1",

                list1.containsAll(list2) ? "sí" : "no");//sí

        System.out.printf("\nTodos los elementos de list3 %s se encuentran en list1\n",

                list1.containsAll(list3) ? "sí" : "no");//no

        list1.removeAll(list3);//Se eliminan de list1 todos los elementos de list3, es decir, el 8

        for (Integer i : list1) {// 1  2  3  4  5  6 

            System.out.printf(" %d ", i);

        }

        System.out.println();

        list1.retainAll(list2);//Intersección entre list1 y list2

        for (Integer i : list1) {// 3  4

            System.out.printf(" %d ", i);

        }

        System.out.printf("\nEl tamaño de list1 es: %d", list1.size());//2

        System.out.printf("\nlist1 %s está vacía", list1.isEmpty() ? "sí" : "no");//no

        list1.clear();//Elimina todos los elementos de list1

        System.out.printf("\nlist1 %s está vacía", list1.isEmpty() ? "sí" : "no");//sí

        list4 = Arrays.asList(1, 2, 3, 4);//Devuelve una lista a partir de un varargs

        System.out.print("\nlist4 creada con Arrays.asList: ");

        for (Integer i : list4) {// 1  2  3  4

            System.out.printf(" %d ", i);

        }

    }

    public static void main(String[] args) {

        new ShowArrayList().show();

    }

}
```

Salida por consola:

```text
 1  2  5  6 

 1  2  3  4  5  6 

 1  2  3  4  5  6  7  8 
```

El elemento de la posición 3 es: 4

El elemento 4 se encuentra en la posición 3

La posición del 4 en list1 por el final es: 8

 1  2  3  4  5  6  7  8 

 1  2  3  4  5  6  8  8 

La sublista comprendida entre las posiciones 2 y 5 es:  3  4  5  6 

El 4 sí se encuentra en list1

El 9 no se encuentra en list1

Todos los elementos de list2 sí se encuentran en list1

Todos los elementos de list3 no se encuentran en list1

 1  2  3  4  5  6 

 3  4 

El tamaño de list1 es: 2

list1 no está vacía

list1 sí está vacía

list4 creada con Arrays.asList:  1  2  3  4 

Fijémonos en cómo se ha inicializado _list4_:

list4 = Arrays.asList(1, 2, 3, 4);

El método `Arrays.asList` proporciona una forma de crear una lista de tamaño fijo a partir del array especificado. Este método actúa como puente entre las APIs basadas en arrays y en colecciones. Además, en la interfaz Collection existe el método `toArray()` que devuelve un array con todos los elementos de la colección.

---

## 5. Método join

Es un método estático de la clase `String` que permite unir varios elementos con un delimitador. Devuelve una cadena compuesta por los elementos iterables unidos entre sí con una copia del delimitador especificado:

public static String join(CharSequence delimiter,Iterable<? extends CharSequence> elements)

Es especialmente útil cuando se tiene una colección y se quieren combinar sus elementos en una sola cadena separadas por un carácter o palabra concreta (como una coma, un espacio, etc.).

```java
package tema12_Colecciones;

import java.util.List;

public class Join {

    public void show() {

        List<String> elements = List.of("Manzana", "Pera", "Naranja");

        System.out.println(String.join(", ", elements)); //Manzana, Pera, Naranja

    }

    public static void main(String[] args) {

        new Join().show();

    }

}

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20ArrayList.html)
```

---

## 6. Invarianza, covarianza y contravarianza

Para poder entender bien los conceptos de **invarianza, covarianza y contravarianza** en los genéricos, empezaremos por estudiar dichos conceptos en los arrays.

En Java **los arrays son covariantes**, lo que básicamente significa que, dadas las reglas de subtipado de Java, un array de tipo `T[]` puede contener elementos de tipo `T` o cualquier subtipo de `T`. Así, el siguiente ejemplo es perfectamente válido:

Number[] numbers = new Number[3];

numbers[0] = new Integer(10);

numbers[1] = new Double(3.14);

numbers[2] = new Byte((byte) 0);

for (Number number: numbers) {

    System.out.println(number);

}

Pero no solo eso, las reglas de subtipado de Java también establecen que un array `S[]` es un subtipo del array `T[]` si `S` es un subtipo de `T`. Así el siguiente código es totalmente válido:

Integer[] ints = {1, 2, 3, 4};

Number[] numbers = ints;

for (Number number : numbers) {

        System.out.println(number);

}

porque según las reglas de subtipado de Java un array `Integer[]` es un subtipo de un array `Number[]`, dado que `Integer` es un subtipo de `Number.`

Pero esta regla de subtipado de arrays nos lleva a una pregunta interesante: si podemos hacer referencia a un `Integer[]` desde una variable `Number[]` ¿podremos almacenar en él algún número que no sea un entero? Hagamos la prueba en el ejemplo anterior:

Integer[] ints = {1, 2, 3, 4};

Number[] numbers = ints;

numbers[0] = 3.14;//Error de ejecución: ArrayStoreException

Esta última línea compilaría sin error, pero si ejecutamos este código, se produciría una excepción `ArrayStoreException` porque estamos tratando de almacenar un valor de tipo `Double` en un `Integer[]`. Si lo pensamos bien, el hecho de que estemos accediendo a `Integer[]` a través de una referencia `Number[]` es irrelevante aquí, lo que importa es que el array es un `Integer[]`.

Esto significa que, en cierta manera, podemos engañar al compilador, pero no podemos engañar al sistema de tipos en tiempo de ejecución. Y no podemos hacerlo porque los arrays son lo que se conoce como tipos _**reifiable**_ (literalmente, que se convierte en una cosa concreta, que no es abstracto). Esto significa que en tiempo de ejecución Java sabe que este array fue instanciado como un `Integer[]` al que, en este caso, simplemente se está accediendo a él a través de una referencia de tipo `Number[]`. Así que, como podemos ver, una cosa es el tipo real del objeto, y otra cosa distinta es el tipo de referencia que usamos para acceder a él.

Sin embargo, los genéricos de Java representan un gran reto en este sentido. Cuando se diseñaron para Java 5, se tuvo que hacer teniendo en cuenta que las colecciones de datos, como por ejemplo `List` (sin tipo) ya existían en Java, y que por tanto ya existía gran cantidad de código que hacía uso de listas de elementos de tipo `Object`. El problema es que no se podía permitir que al introducir los genéricos en las colecciones (como en `List<T>`) todo el código existente que usara colecciones dejara de compilar, es decir, no fuera compatible. Por este motivo, se tomó la decisión de que la información sobre el tipo que se le suministra a una clase genérica cuando se construye una instancia de ella solo se usara en tiempo de compilación para indicar cómo se debe crear el objeto correctamente, pero NO estuviera disponible en tiempo de ejecución. A este proceso de le denomina borrado de tipos, en inglés _**type erasure**_, e implica básicamente que en ejecución una `List<Integer>` ya simplemente se ve como una `List`.

Y el problema asociado al borrado de tipos en los genéricos es que como en tiempo de ejecución no hay información del tipo con el que se creó la lista, no habría forma de asegurar, en tiempo de ejecución, que el valor que estamos intentando almacenar en una lista es del tipo con el que se creó. Los tipos genéricos son no verificables, ya que en tiempo de ejecución no podemos determinar la verdadera naturaleza del tipo genérico. Así, teóricamente, no habría manera de lanzar una excepción en tiempo de ejecución en el siguiente ejemplo, a diferencia de como vimos antes usando arrays:

List<Integer> ints = new ArrayList<>();

ints.add(1);

ints.add(2);

List<Number> numbers = ints;

numbers.add(3.14);/* Esta línea NO puede producir un error en tiempo de ejecución porque la información sobre el tipo con el que se creó la lista numbers ha sido eliminada. */

En tiempo de ejecución el sistema no tiene manera de evitarnos ejecutar la última línea, dado que no puede determinar que la lista referenciada por `numbers` en realidad es una lista de enteros, por lo que podríamos insertar cualquier objeto.

La solución a este grave problema es usar la información que disponemos en tiempo de compilación, de manera que el compilador nos impida hacer referencia a una lista de enteros desde una variable de tipo lista de números. Es decir, que la solución de Java es producir un error de compilación al intentar hacer la asignación:

List<Integer> ints = new ArrayList<>();

ints.add(1);

ints.add(2);

List<Number> numbers = ints;//Error de compilación.

numbers.add(3.14);

De esta manera, si no podemos engañar al compilador, tampoco podremos engañar al sistema en tiempo de ejecución, ya que no podremos llegar a ejecutar nuestro código.

¿Y esta solución qué implicación tiene? Que a diferencia de lo que sucede con los arrays, **en Java las clases con tipos genéricos son, por defecto, invariantes**, por lo que, por ejemplo, si el tipo `U` es un subtipo del tipo `T`, `List<U>` NO es un subtipo de `List<T>`, como ha quedado demostrado en el código anterior al producir un error de compilación.

Evidentemente esta característica de los tipos genéricos en Java tendría un impacto muy negativo en el polimorfismo. Consideremos el método que calcula el sumatorio de los elementos contenidos en el array:

long sum(Number[] numbers) {

    long summation = 0;

    for(Number number : numbers) {

        summation += number.longValue();

    }

    return summation;

}

Podremos llamar a dicho método de las siguientes maneras sin que se produzca ningún error de compilación ni en tiempo de ejecución:

Integer[] myInts = {1,2,3,4,5};

Long[] myLongs = {1L, 2L, 3L, 4L, 5L};

Double[] myDoubles = {1.0, 2.0, 3.0, 4.0, 5.0};

System.out.println(sum(myInts));

System.out.println(sum(myLongs));

System.out.println(sum(myDoubles));

Sin embargo, si intentamos implementar el mismo método pero para que reciba una lista en vez de un array:

long sum(List<Number> numbers) {

        long summation = 0;

        for(Number number : numbers) {

                summation += number.longValue();

        }

        return summation;

}

Al tratar de usarlo podemos obtener errores en tiempo de compilación, como en los siguientes casos:

List<Integer> myInts = List.of(1,2,3,4,5);

List<Long> myLongs = List.of(1L, 2L, 3L, 4L, 5L);

List<Double> myDoubles = List.of(1.0, 2.0, 3.0, 4.0, 5.0);

System.out.println(sum(myInts));//Error de compilación

System.out.println(sum(myLongs));//Error de compilación

System.out.println(sum(myDoubles));//Error de compilación

¿Por qué se producen dichos errores de compilación? Porque, como acabamos de decir, los tipos genéricos NO son covariantes por defecto, sino invariantes, por lo que `List<Integer>` NO es un subtipo de `List<Number>` aunque `Integer` sea un subtipo de `Number`, y lo mismo con los casos de `Long` y `Double` del código anterior.

Evidentemente, desde el punto de vista del polimorfismo esto es inaceptable. Para solucionarlo, Java introdujo una nueva sintaxis para definir tipos parametrizados conocida como tipos comodín `?` (_bounded wildcard type_), que permite al desarrollador definir explícitamente la covarianza o la contravarianza de un genérico.

Empecemos con la **covarianza**. Así, en vez de usar un tipo `T` como argumento de tipo de una estructura genérica, podemos usar `<? extends T>` para indicar que podremos leer elementos de tipo `T` o de cualquier subclase de `T`, pero que no podremos insertar en la estructura ningún valor. Además, `T` puede ser tanto una clase como una interfaz, ya que `extends` en este contexto indica cualquier subtipo, independientemente de que provenga de herencia de clase o implementación de interfaz.

Por ejemplo, este código es perfectamente válido, dado que solo leemos desde la referencia `numbers`:

List<Integer> ints = new ArrayList<>();

ints.add(1);

ints.add(2);

List<? extends Number> numbers = ints;

for (Number number : numbers) {

        System.out.println(number);

}

La lectura está permitida porque en la definición de la lista hemos asegurado que el tipo de la lista real que referencie `numbers` debe ser forzosamente de alguna clase que extiende de `Number`, por lo que al acceder a un elemento de la lista internamente se puede hacer un casting al tipo `Number` con la seguridad de que la conversión no fallará.

Sin embargo, no nos está permitido escribir nada a través de dicha referencia:

List<Integer> ints = new ArrayList<>();

ints.add(1);

ints.add(2);

List<? extends Number> numbers = ints;

for (Number number : numbers) {

    System.out.println(number);

}

ints.add(25);

numbers.add(17);//Error de compilación, no se permite escribir a través de una referencia covariante

Y no se nos permite escribir porque entonces podríamos almacenar en la lista de enteros reverenciada por `numbers` cualquier valor que no fuera un entero.

Así, el método de un ejemplo anterior que sumaba todos los elementos de una lista quedaría de la siguiente manera:

long sum(List<? extends Number> numbers) {

        long summation = 0;

        for(Number number : numbers) {

                summation += number.longValue();

        }

        return summation;

}

y podríamos llamarla de las siguientes maneras sin que se produjera un error de compilación:

List<Integer> myInts = List.of(1,2,3,4,5);

List<Long> myLongs = List.of(1L, 2L, 3L, 4L, 5L);

List<Double> myDoubles = List.of(1.0, 2.0, 3.0, 4.0, 5.0);

System.out.println(sum(myInts));

System.out.println(sum(myLongs));

System.out.println(sum(myDoubles));

Veamos ahora la **contravarianza**. La contravarianza es el caso contrario a la covarianza, se utiliza para escribir elementos en una estructura genérica. Para definir la contravarianza usaremos `<? super T>` como indicador del tipo. Esto quiere decir que el tipo real es `T` o cualquier tipo que sea una superclase de `T` (en último caso `Object`).

Vamos a declarar una lista con un tipo comodín contravariante: `? super Integer`, es decir, una lista que acepta elementos de tipo `Integer` o de cualquier superclase de `Integer`, es decir, `Number` (superclase de `Integer`) y `Object` (superclase de `Number`):

List<Integer> ints = new ArrayList<>();

ints.add(1);

ints.add(2);

List<? super Integer> numbers = ints;

numbers.add(25);

numbers.add(25.4);//Error de compilación

La línea de código `numbers.add(25);` es válida porque 25 es un `Integer`, y el compilador sabe con certeza que cualquier lista que sea `? super Integer` puede recibir objetos de tipo Integer.

La línea de código `numbers.add(25.4);` genera un error de compilación ya que 25.4 es un `Double`, no un `Integer`, y aunque `Double` también es una subclase de `Number`, el compilador no puede garantizar que esa lista acepte cualquier subtipo de `Number`, porque la hemos declarado como `? super Integer`, no como `? super Number`.

La lectura hacia el tipo T no es segura, porque no tenemos forma de saber exactamente el tipo del objeto que se pretende leer a través de la referencia, ya que puede ser de cualquier clase `T` o superclase de `T`:

List<Integer> ints = new ArrayList<>();

ints.add(1);

ints.add(2);

List<? super Integer> numbers = ints;

Integer valor1 = ints.get(0);

Object valor2 = numbers.get(0);//Se puede asegurar que el primer valor de la lista es un Object ya que es superclase de todos los tipos

Integer valor3 = numbers.get(0);//Error de compilación: no se puede asegurar que el primer elemento de la lista sea un entero

Como podemos ver, si el compilador nos permitiera compilar esta última línea, podríamos obtener un `ClassCastException` en tiempo de ejecución al no poder asegurar en tiempo de ejecución el tipo del primer elemento de la lista. Así que, una vez más, el compilador no corre el riesgo de permitir esta operación insegura y la rechaza inmediatamente produciendo un error de compilación.

Así, a modo de resumen, podríamos decir que para los parámetros de un método se recomienda usar siempre la covarianza cuando solo pretendemos sacar valores genéricos de una estructura, la contravarianza cuando solo pretendemos poner valores genéricos en una estructura, y solo usar la invarianza (no usar el carácter comodín) cuando pretendemos hacer ambas cosas. Si seguimos esta regla aumentaremos la flexibilidad de nuestro código.

Sin embargo, no se recomienda usar el carácter comodín para los tipos de retorno de los métodos, ya que estaremos obligando al código cliente a usar tipo comodín.

Veamos un ejemplo en que se usa tanto covarianza como contravarianza. Consiste en un método que permite copiar los elementos de una lista de números, llamada _origen_, en otra lista llamada _destino_, y ambas listas son recibidas como parámetro. En este caso, para la lista _origen_ usaremos covarianza, ya que solo vamos a leer de ella, y para la lista _destino_ usaremos contravarianza, ya que solo vamos a escribir en ella:

public void copy(List<? extends Number> source, List<? super Number> target) {

        for(Number number : source) {

                target.add(number);

        }

}

De esta manera podremos realizar sin error las siguientes llamadas:

List<Integer> myInts = List.of(1, 2, 3, 4);

List<Double> myDoubles = List.of(3.14, 6.28);

List<Number> myObjs = new ArrayList<>();

copy(myInts, myObjs);

copy(myDoubles, myObjs);

---

## 7. Iteradores

En diseño de software, el patrón de diseño _Iterador_ (en inglés, _Iterator_) define una interfaz que declara los métodos necesarios para acceder secuencialmente a un grupo de objetos de una colección.

Este patrón debe ser utilizado cuando se requiera una forma estándar de recorrer una colección, es decir, cuando no sea necesario que un cliente sepa el tipo de colección que está recorriendo.

La interfaz `Iterable<T>` contine el método `iterator()` que devuelve una instancia de alguna clase que implemente la interfaz `Iterator<T>`:

- `Iterator<T> iterator()`: devuelve un iterador al comienzo de la colección.
    

La interfaz `Iterator<E>` permite el acceso secuencial a los elementos de una colección y realizar recorridos sobre la colección. Los métodos de `Iterator<E>` son:

- `boolean hasNext()`: comprueba si hay siguiente elemento.
    
- `E next()`: devuelve el siguiente elemento y mueve el iterador.
    
- `void remove()`: se invoca después de next() para eliminar el último elemento leído.
    

La interfaz `Collection<E>` es una subinterfaz o interfaz hija de `Iterable<E>`. La clase `ArrayList<E>` implementa `Collection<E>` y por lo tanto también `Iterable<E>`, así que dispone del método `iterator()`. Veamos un ejemplo de recorrido de un `ArrayList<E>` utilizando iteradores:

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.Iterator;

import java.util.List;

public class ShowIterator {

    public void show() {

        Iterator<String> it;

        List<String> list = new ArrayList<>();

        list.add("Juan");

        list.add("Antonio");

        list.add("Jaime");

        list.add("Vicente");

        it = list.iterator();

        while (it.hasNext()) {

            System.out.println(it.next());

        }

    }

    public static void main(String[] args) {

        new ShowIterator().show();

    }

}
```

Salida por consola:

```text
Juan

Antonio

Jaime

Vicente
```

Si no hay siguiente, `next()` lanza en ejecución una excepción `NoSuchElementException`:

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.Iterator;

import java.util.List;

public class NextException {

    public void show() {

        Iterator<String> it;

        List<String> list = new ArrayList<>();

        list.add("Juan");

        it = list.iterator();

        System.out.println(it.next());

        System.out.println(it.next());//Se lanza en ejecución una excepción NoSuchElementException

    }

    public static void main(String[] args) {

        new NextException().show();

    }

}

Tal y como vemos en el ejemplo anterior, hay que comprobar si hay siguiente con un `hasNext()` para que el `next()` no lanze la excepción.

No se puede modificar la colección dentro del bucle for-each porque se lanza en ejecución la excepción `ConcurrentModificationException`, ya que estamos recorriendo y modificando la lista a la vez:
```

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.List;

public class ModifyInsideForEach {

    public void show() {

        List<String> list = new ArrayList<>();

        list.add("Juan");

        list.add("Antonio");

        list.add("Jaime");

        list.add("Vicente");

        for (String s : list) {//Se lanza en ejecución la excepción ConcurrentModificationException

            System.out.printf(" %s ", s);

            if (s.equals("Antonio")) {

                list.remove("Antonio");

            }

        }

    }

    public static void main(String[] args) {

        new ModifyInsideForEach().show();

    }

}

Para solucionarlo, podemos utilizar el método `remove()` de `Iterator<E>`. Si se modifica una colección mientras se recorre, los iteradores quedan invalidados, a excepción del método `remove()` de la interfaz `Iterator<E>`. El método `remove()` permite eliminar elementos de la colección siendo la única forma adecuada para eliminar elementos durante la iteración:
```

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.Iterator;

import java.util.List;

public class RemoveIterator {

    public void show() {

        String s;

        Iterator<String> it;

        List<String> list = new ArrayList<>();

        list.add("Juan");

        list.add("Antonio");

        list.add("Jaime");

        list.add("Vicente");

        it = list.iterator();

        while (it.hasNext()) {

            s = it.next();

            if (s.equals("Antonio")) {

                it.remove();

            } else {

                System.out.println(s);

            }

        }

    }

    public static void main(String[] args) {

        new RemoveIterator().show();

    }

}
```

Salida por consola:

```text
Juan

Jaime

Vicente
```

Solo puede haber una invocación a `remove()` por cada invocación a `next()`. Si no se cumple, se lanza en ejecución una excepción `IllegalStateException`. Por ejemplo, imaginemos que tenemos una lista de personas y queremos eliminar a _Antonio_ y a la persona que venga detrás. Si cuando encontramos a _Antonio_, hacemos dos `remove()` seguidos, entonces salta la excepción:

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.Iterator;

import java.util.List;

public class RemoveNext1 {

    public void show() {

        String s;

        Iterator<String> it;

        List<String> list = new ArrayList<>();

        list.add("Juan");

        list.add("Antonio");

        list.add("Jaime");

        list.add("Vicente");

        it = list.iterator();

        while (it.hasNext()) {

            s = it.next();

            if (s.equals("Antonio")) {

                it.remove();

                it.remove();//Se lanza en ejecución la excepción IllegalStateException

            } else {

                System.out.println(s);

            }

        }

    }

    public static void main(String[] args) {

        new RemoveNext1().show();

    }

}

Tendríamos que hacer otro `next()` para el que venga detrás de _Antonio_:
```

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.Iterator;

import java.util.List;

public class RemoveNext2 {

    public void show() {

        String s;

        Iterator<String> it;

        List<String> list = new ArrayList<>();

        list.add("Juan");

        list.add("Antonio");

        list.add("Jaime");

        list.add("Vicente");

        it = list.iterator();

        while (it.hasNext()) {

            s = it.next();

            if (s.equals("Antonio")) {

                it.remove();

                if(it.hasNext()) {

                    it.next();

                    it.remove();

                }

            } else {

                System.out.println(s);

            }

        }

    }

    public static void main(String[] args) {

        new RemoveNext2().show();

    }

}
```

Salida por consola:

```text
Juan

Vicente
```

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20Iterator.html)

La interfaz `ListIterator<E>` es una subinterfaz o interfaz hija de `Iterator<E>`. Es un iterador para listas que permite al programador recorrer la lista hacia adelante y hacia atrás, modificar la lista durante la iteración y obtener la posición actual del iterador en la lista.

Hereda los métodos de `Iterator<E>` y además aporta otros métodos nuevos:

- `void add(E e)`: inserta el elemento en la lista antes del elemento que sería devuelto por _next()_, si lo hubiera, y después del elemento que sería devuelto por _previous()_, si lo hubiera. Una llamada posterior a next() no se vería afectada y una llamada posterior a _previous_() devolvería el nuevo elemento.
    
- `boolean hasPrevious()`: comprueba si hay un elemento anterior.
    
- `int nextIndex()`: devuelve el índice del elemento que sería devuelto por una llamada a _next()_. El índice del primer elemento es 0.
    
- `E previous()`: devuelve el elemento anterior de la lista y mueve la posición del cursor hacia atrás.
    
- `int previousIndex()`: devuelve el índice del elemento que sería devuelto por una llamada a _previous()_.
    
- `void set(E e)`: sustituye el último elemento devuelto por _next()_ o _previous()_ por el elemento _e_.
    

En la interfaz `List<E>`, hay dos métodos para crear este iterador:

- `ListIterator<E> listIterator()`: se coloca antes del primer elemento para que al hacer el primer _next()_ se devuelva el primer elemento.
    
- `ListIterator<E> listIterator(int index)`: se coloca antes del elemento que se encuentra en la posición _index_ para que al hacer un _next()_ se devuelva dicho elemento. Para recorrer la lista al revés, hay que crearlo con el tamaño de la lista para que el primer _previous()_ devuelva el último.
    

```java
package tema12_Colecciones;

import java.util.ArrayList;

import java.util.List;

import java.util.ListIterator;

public class ShowListIterator {

    public void show() {

        ListIterator<Integer> it;

        List<Integer> list = new ArrayList<>();

        list.add(1);

        list.add(2);

        list.add(4);

        list.add(6);

        //Recorrido de la lista hacia atrás:

        it = list.listIterator(list.size());

        while (it.hasPrevious()) {

            System.out.printf(" %d ", it.previous());// 6  4  2  1

        }

        it = list.listIterator(1);//Se coloca antes del elemento que se encuentra en la posición 1

        System.out.printf("\n %d ", it.next());//2

        System.out.printf("\n %d ", it.nextIndex());//2

        System.out.printf("\n %d ", it.previousIndex());//1

        it.add(3);//Una llamada posterior a next() no se ve afectada

        System.out.printf("\n %d ", it.next());//4 

        it.add(5);

        System.out.printf("\n %d ", it.previous());//5 Una llamada posterior a previous() devuelve el nuevo elemento

        System.out.printf("\n %d \n", it.next());//5

        it.set(7);//Sustituye el último elemento devuelto por next() por 7

        for (Integer i : list) {

            System.out.printf(" %d ", i);//1  2  3  4  7  6 

        }

    }

    public static void main(String[] args) {

        new ShowListIterator().show();

    }

}

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20ListIterator.html)
```

---

## 8. Métodos equals y hashCode

Vimos en el _[Tema 7 Herencia 6 El método toString](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/7%20Herencia.html#toString)_ que la clase _Object_ proporciona un cierto número de métodos de utilidad general que pueden utilizar todos los objetos ya que los heredan. Pero normalmente hay que sobrescribirlos para que funcionen adecuadamente adaptándolos a la clase correspondiente. Esto se hace con la idea de que todas las clases utilicen el mismo nombre y prototipo de método para hacer operaciones comunes. Como por ejemplo, `equals` que comprueba si dos elementos son iguales y `hashCode` que devuelve un número entero que identifica al objeto cuando se guarda en algunas estructuras de datos.

Sin embargo, debemos tener en cuenta que al sobrescribir todos estos métodos debemos seguir cumpliendo con el comportamiento que se espera de ellos, ya que son usados internamente por muchas clases del propio lenguaje. De lo contrario, las clases que dependen de ello, como `HashMap` y `HashSet` dejarían de funcionar correctamente.

En la implementación de `equals` de la clase `Object`, dos instancias de clase son iguales si están situadas en la misma posición de memoria.

Debemos tener en cuenta que cuando un programador usa el método `equals` sobre un objeto pasándole como argumento otro objeto, lo que pretende es descubrir si ambos objetos son equivalentes lógicamente (representan el mismo "valor"), no si están almacenados en la misma posición de memoria.

No sobrescribir el método `equals` en una determinada clase es la opción recomendada en los siguientes casos:

- Cuando cada instancia de la clase es intrínsecamente única, lo cual es cierto para clases como `Scanner` que representan entidades activas en lugar de valores.
    
- Cuando se considera que no hay necesidad de que la clase provea una prueba de "equivalencia lógica".
    
- Cuando una superclase de la clase ya lo ha sobrescrito y el comportamiento de la superclase es apropiado para las subclases.
    
- Cuando la clase es privada o friendly, y estamos completamente seguros de que su método `equals` nunca será invocado, ni explícita ni implícitamente.
    
- Cuando la clase controla las instancias que pueden ser creadas para asegurarse que no pueden existir dos objetos que representen el mismo "valor", como por ejemplo con las clases `enum` o las clases que siguen el patrón de diseño _singleton_. Para estas clases, la equivalencia lógica es igual que la igualdad de identidad, ya que no puede existir más de una instancia para un "valor". Dado que esta es la comprobación que realiza la implementación de `equals` en la clase `Object`, no tiene sentido sobrescribirlo.
    

Si nuestra clase no se encuentra en ninguno de los casos anteriores, es muy recomendable que sobrescribamos el _método_ `equals`. Un ejemplo muy característico es cuando la clase corresponda a una entidad que represente un valor (_value class_).

Como hemos comentado, cuando sobrescribamos el método `equals` debemos seguir cumpliendo el comportamiento que el sistema espera de él, que incluye las siguientes propiedades:

- Reflexiva: para todo objeto _x_ distinto de _null_ se debe cumplir que `x.equals(x)` sea _true_.
    
- Simétrica: para todo par de objetos _x_ e _y_ distintos de _null_ se debe cumplir que `x.equals(y)` solo debe retornar _true_ si `y.equals(x)` retorna _true_.
    
- Transitiva: para todo trío de objetos _x_, _y_ , _z_ distintos de _null_ se debe cumplir que si `x.equals(y)` retorna _true_ y `y.equals(z)` retorna _true_ entonces `x.equals(z)` debe retornar _true_.
    
- Consistente: para todo par de objetos _x_ e _y_ distintos de _null_ se debe cumplir que `x.equals(y)` siempre retorne el mismo valor si no hemos cambiado los atributos que se usan para comparar en alguno de los dos objetos.
    
- Para todo objeto _x_ distinto de _null_ se debe cumplir que `x.equals(null)` debe retornar _false_.
    

Así, para sobrescribir el método `equals` cumpliendo con las propiedades anteriores se recomienda seguir los siguientes pasos:

1. Usar el operador `==` para comprobar si el argumento corresponde a otra referencia al mismo objeto, en cuyo caso retornar _true_.
    
2. Usar el operador `instanceof` para comprobar si el objeto recibido como argumento no es de la misma clase, en cuyo caso retornar _false_. También nos sirve para comprobar si dicho argumento es _null_, ya que en este caso _instanceof_ retorna _false_.
    
3. Hacer casting del objeto recibido como argumento convirtiéndolo a la clase correspondiente. Dado que hemos hecho antes _instanceof_, el casting siempre tendrá éxito.
    
4. Para cada atributo significativo de la clase, comprobar que dicho atributo en el objeto argumento es equivalente al atributo en el objeto _this_. Si no tenemos éxito en alguno de ellos, retornar _false_. Si todas las comprobaciones se han hecho con éxito, retornar _true_. Para realizar la comprobación de cada atributo usar:
    
    - El operador `==` para valores primitivos que no sean _float_ ni _double_.
        
    - Para valores _float_ usar `Float.compare(value1, value2` y para valores _double_ usar `Double.compare(value1, value2)`.
        
    - Para valores correspondientes a objetos llamar a `equals` recursivamente. Si es válido que dichos objetos contengan _null_, entonces debemos usar `Objects.equals(object1, object2)` para que no se produzca la excepción `NullPointerException`.
        
    - Para los valores correspondientes a arrays, compara uno a uno los elementos significativos del array. Si todos los elementos son significativos, usa alguna de las versiones del método estático `Arrays.equals`.
        

Veamos un ejemplo:

public final class PhoneNumber {

    private final short areaCode, prefix, lineNum;

    @Override 

    public boolean equals(Object o) {

        PhoneNumber pn;

        if (o == this) return true;

        if (!(o instanceof PhoneNumber)) return false;

        pn = (PhoneNumber) o;

        return pn.lineNum == lineNum && pn.prefix == prefix

                && pn.areaCode == areaCode;

    }

    // ...

}

Una aspecto muy importante es que no debemos cambiar el tipo del objeto recibido como argumento, que siempre debe ser `Object`, o no estaremos sobrescribiendo el método `equals`, sino sobrecargándolo, lo que puede producir falsos positivos. El compilador no se quejará si no usamos la anotación `@Override` (por eso siempre se recomienda usarla). Por ejemplo, nunca hagas esto:

// NUNCA HAGAS ESTO. EL TIPO DE o DEBE SER Object

public boolean equals(MyClass o) {

    // ...

}

Escribir a mano los métodos `equals` y `hashCode` es bastante tedioso. Para facilitarnos esta tarea tenemos librerías como la librería AutoValue de Google que lo genera automáticamente para nosotros con tan solo usar una determinada anotación. Otra opción es dejar que el IDE nos genere dichos métodos, aunque esto tiene el inconveniente de que no se generan automáticamente de nuevo conforme añadimos atributos a nuestra clase, por lo que debemos tener cuidado, algo que sí hace AutoValue. En todo caso, es mejor usar el IDE que hacerlo nosotros a mano, ya que el humano es más propenso a los errores. En el Eclipse se encuentra en Menú _Source_ → _Generate hashCode() and equals()_.

Un detalle muy importante que no debemos olvidar es que **si en una clase sobrescribimos el método `equals` debemos obligatoriamente sobrescribir también el método `hashCode`** o de lo contrario no se estará cumpliendo con el comportamiento esperado de este último, lo que impedirá que los objetos de dichas clases funcionen correctamente en colecciones como `HashMap` y `HashSet`.

La implementación por defecto de `hashCode()` de la clase `Object` devuelve una representación numérica de la dirección de memoria en la que se encuentra ubicado el objeto. Tenemos que anularlo si lo que queremos es que `hashCode()` devuelva un número entero que identifique al objeto cuando se guarde en algunas estructuras de datos.

El comportamiento que se espera de `hashCode()` es el siguiente:

- Debe ser consistente, es decir, que repetidas llamadas al método `hashCode()` deben retornar el mismo valor, siempre y cuando no se haya modificado ninguno de los atributos usados para las comparaciones.
    
- Si dos objetos son equivalentes, es decir, si `x.equals(y)` retorna _true_, entonces `x.hashCode()` e`y.hashCode()` deben retornar el mismo valor entero.
    
- Si dos objetos no son equivalentes, es decir si `x.equals(y)` retorna _false_, no es estrictamente necesario, aunque sí recomendable, que `x.hashCode()` e `y.hashCode()` retornen valores diferentes, de manera que se mejore el rendimiento de las tablas _hash_. El algoritmo de la función _hash_ debe distribuir una colección de instancias de un tamaño considerable de forma uniforme entre todos los valores enteros.
    

La implementación característica al sobrescribir el método `hashCode()` en la clase `PhoneNumber`es la siguiente, usando los atributos _areaCode_, _prefix_ y _lineNum_:

public final class PhoneNumber {

    private final short areaCode, prefix, lineNum;

    @Override 

    public boolean equals(Object o) {

        PhoneNumber pn;

        if (o == this){

            return true;  

        } 

        if (!(o instanceof PhoneNumber)){

            return false;  

        } 

        pn = (PhoneNumber) o;

        return pn.lineNum == lineNum && pn.prefix == prefix

                && pn.areaCode == areaCode;

    }

    @Override 

    public int hashCode() {

        int result = Short.hashCode(areaCode);

        result = 31 * result + Short.hashCode(prefix);

        result = 31 * result + Short.hashCode(lineNum);

        return result;

    }

    // ...

}

Además de escribir nosotros a mano el código del método `hashCode()`, podemos usar la implementación proporcionada por algunas librerías, como Guava o AutoValue. Adicionalmente los IDEs nos proporcionan asistentes para la generación de este método, seleccionando los atributos que queremos usar. En el Eclipse se encuentra en Menú _Source_ → _Generate hashCode() and equals()_.

Si una clase es inmutable y el coste de calcular el valor _hash_ es significativo, podría considerar almacenar cacheado el código _hash_ en el propio objeto, en lugar de recalcularlo cada vez que se solicite. Si cree que la mayoría de los objetos de esta clase se usarán como claves _hash_, entonces debería calcular el código _hash_ cuando se cree la instancia. De lo contrario, podría elegir calcular perezosamente el código _hash_ la primera vez que se invoque al método `hash()`.

Dos consideraciones finales: **no excluir atributos significativos del cálculo del valor hash**, así se logrará un mejor rendimiento. En segundo lugar, **no proporcionar a los clientes de la clase demasiada información acerca de cómo se calcula el valor hash**, de esta manera el código cliente no podrá depender de cómo se calcula, permitiéndonos modificar la implementación del método en el futuro sin afectar a los clientes.

---

## 9. Colecciones sin duplicados

La interfaz `Set`, que hereda de _Collection_, permite implementar listas de elementos sin duplicados, es decir, modela la abstracción matemática de los conjuntos.

Existen varios tipos de implementaciones realizadas dentro de la plataforma Java:

- **HashSet**: esta implementación almacena los elementos en una tabla _hash_. Es la implementación con mejor rendimiento de todas pero no garantiza ningún orden a la hora de realizar iteraciones.
    
- **LinkedHashSet**: esta implementación almacena los elementos en función del orden de inserción. Es un poco más costosa que _HashSet_.
    
- **TreeSet**: esta implementación utiliza una estructura de árbol para ordenar los elementos. Es bastante más lenta que _HashSet_. La veremos más adelante en el apartado de los árboles.
    

### 9.1 Clase HashSet

Implementa la interfaz anterior. Es la clase más utilizada para implementar listas sin duplicados. Esta clase permite el elemento nulo. No garantiza ningún orden a la hora de realizar iteraciones.

Utiliza internamente una tabla de tipo _hash_:

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/hashtable.png)

Al querer guardar un objeto en esta estructura, se llama al método `hashCode()` el cual devuelve un número entero que la estructura usará para decidir en qué cajón guardará este dato. Para recuperar el objeto se llama al método `hashCode()` para determinar de qué cajón debo recuperar el objeto. El objetivo de guardar los datos de esta forma y de llamar al método es lograr almacenar y recuperar información en tiempo constante (lo cual no ocurre siempre, pero se acerca). El que no suceda esto depende, casi siempre, del valor que devuelva el método `hashCode()` para cada objeto.

Supongamos que guardamos 3 objetos en esta estructura y el método `hashCode()` de los 3 devuelve 0, esto quiere decir que los 3 objetos se guardarán en el cajón 0. Cuando se necesite recuperar un objeto, hay que recorrer los objetos del cajón 0 para determinar cuál es el que se quiere recuperar. Por lo tanto, este método `hashCode()` no es útil ya que lo que se pretende al guardar los elementos es que éstos queden dispersos de forma uniforme en toda la estructura quedando la menor cantidad de cajones vacíos y que no haya cajones donde se guarden muchos más elementos que en otros.

Si dos objetos tienen el mismo `hashCode`, ambos objetos se guardarán en el mismo cajón. La estructura usa entonces el método `equals` dentro de ese cajón para determinar cuál corresponde con el solicitado y para eso depende de que el programador haya sobreescrito el método, de lo contrario no garantiza un resultado correcto.

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/hashtable2.png)

Los objetos _HashSet_ se construyen con un tamaño inicial de tabla (el tamaño del array) y un factor de carga que indica cuándo se debe redimensionar el array. Es decir, si se creó un array de 100 elementos y la carga se estableció al 80%, cuando se hayan rellenado 80 valores, se redimensiona el array. Por defecto, el tamaño del array se toma con 16 y el factor de carga con 0,75 (75%). No obstante, se puede construir una lista _HashSet_ indicando ambos parámetros.

Esta implementación proporciona tiempos constantes en las operaciones básicas siempre y cuando la función _hash_ disperse de forma correcta los elementos dentro de la tabla _hash_. Es importante definir el tamaño inicial de la tabla ya que este tamaño marcará el rendimiento de esta implementación.

Veamos un ejemplo de `HashSet` con la clase `Vehicle`. Los atributos significativos a tener en cuenta para el `equals` y el `hashCode` son _wheelCount_ y _colour_. La velocidad (_speed_) no se incluye ya que si comparamos el mismo coche pero con velocidades distintas, en realidad, no deja de ser el mismo coche. El `equals` y el `hashCode` están generados con el Eclipse:

```java
package tema12_Colecciones.sinDuplicados;

public class Vehicle {

    private int wheelCount;

    private double speed;

    private String colour;

    public Vehicle(int wheelCount, String colour) {

        this.wheelCount = wheelCount;

        this.colour = colour;

        speed = 0;

    }

    public int getWheelCount() {

        return wheelCount;

    }

    public double getSpeed() {

        return speed;

    }

    public String getColour() {

        return colour;

    }

    public void setColour(String colour) {

        this.colour = colour;

    }

    public void accelerate(double amount) {

        speed += amount;

    }

    public void brake(double amount) {

        speed -= amount;

    }

    @Override

    public String toString() {

        return String.format("Número de ruedas: %d, color: %s, velocidad: %.2f", wheelCount, colour, speed);

    }

    @Override

    public int hashCode() {

        final int prime = 31;

        int result = 1;

        result = prime * result + ((colour == null) ? 0 : colour.hashCode());

        result = prime * result + wheelCount;

        return result;

    }

    @Override

    public boolean equals(Object obj) {

        if (this == obj)

            return true;

        if (obj == null)

            return false;

        if (!(obj instanceof Vehicle))

            return false;

        Vehicle other = (Vehicle) obj;

        if (colour == null) {

            if (other.colour != null)

                return false;

        } else if (!colour.equals(other.colour))

            return false;

        if (wheelCount != other.wheelCount)

            return false;

        return true;

    }

}
```

```java
package tema12_Colecciones.sinDuplicados;

import java.util.HashSet;

import java.util.Set;

public class ShowHashSet {

    public void show() {

        Set<Vehicle> set = new HashSet<>();

        set.add(new Vehicle(4, "azul"));

        set.add(new Vehicle(2, "rojo"));

        set.add(new Vehicle(4, "azul"));

        set.add(new Vehicle(2, "rojo"));

        set.add(new Vehicle(4, "verde"));

        for (Vehicle v : set) {

            System.out.println(v);//Se llama al toString del objeto

        }

    }

    public static void main(String[] args) {

        new ShowHashSet().show();

    }

}
```

Salida por consola:

```text
Número de ruedas: 4, color: verde, velocidad: 0,00

Número de ruedas: 4, color: azul, velocidad: 0,00

Número de ruedas: 2, color: rojo, velocidad: 0,00
```

### 9.2 Clase LinkedHashSet

Almacena los elementos en función del orden de inserción. Es un poco más costosa que _HashSet_.

```java
package tema12_Colecciones.sinDuplicados;

import java.util.LinkedHashSet;

import java.util.Set;

public class ShowLinkedHashSet {

    public void show() {

        Set<Vehicle> set = new LinkedHashSet<>();

        set.add(new Vehicle(4, "azul"));

        set.add(new Vehicle(2, "rojo"));

        set.add(new Vehicle(4, "azul"));

        set.add(new Vehicle(2, "rojo"));

        set.add(new Vehicle(4, "verde"));

        for (Vehicle v : set) {

            System.out.println(v);//Se llama al toString del objeto

        }

    }

    public static void main(String[] args) {

        new ShowLinkedHashSet().show();

    }

}
```

Salida por consola:

```text
Número de ruedas: 4, color: azul, velocidad: 0,00

Número de ruedas: 2, color: rojo, velocidad: 0,00

Número de ruedas: 4, color: verde, velocidad: 0,00
```

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20Colecciones%20sin%20duplicados.html)

### 9.3 Clase EnumSet

Es una implementación de conjuntos de alto rendimiento de tipos enumerados. Requiere que las constantes de enumeración colocadas en él pertenezcan al mismo tipo de enumeración. Veamos algunos de sus métodos:

- `static <E extends Enum<E>> EnumSet<E> allOf(Class<E> elementType)`: crea un conjunto de enumeraciones que contiene todos los valores del tipo de enumeración especificado.
    
- `static <E extends Enum<E>> EnumSet<E> complementOf(EnumSet<E> s)`: crea un conjunto de enumeraciones con el mismo tipo de elemento que el conjunto de enumeraciones especificado, conteniendo inicialmente todos los elementos de este tipo que no están contenidos en el conjunto especificado.
    
- `static <E extends Enum<E>> EnumSet<E> copyOf(Collection<E> c)`: crea un conjunto de enumeraciones a partir de una colección.
    
- `static <E extends Enum<E>> EnumSet<E> copyOf(EnumSet<E> s)`: crea un conjunto de enumeraciones a partir de otro.
    
- `static <E extends Enum<E>> EnumSet<E> noneOf(Class<E> elementType)`: crea un conjunto de enumeraciones vacío con el tipo de elemento especificado.
    
- `static <E extends Enum<E>> EnumSet<E> of(E e)`: crea un conjunto de enumeraciones que contiene el elemento especificado. Este método tiene varias sobrecargas para admitir más elementos.
    
- `static <E extends Enum<E>> EnumSet<E> range(E from, E to)`: crea un conjunto de enumeraciones que contiene inicialmente todos los elementos del rango definido por los dos elementos especificados.
    

```java
package tema12_Colecciones.enumSet;

public enum Operation {

    PLUS('+'), MINUS('-'), TIMES('*'), DIVIDE('/');

    private final char symbol;

    private Operation(char symbol) {

        this.symbol = symbol;

    }

    public char getSymbol() {

        return symbol;

    }

}
```

```java
package tema12_Colecciones.enumSet;

import java.util.EnumSet;

public class ShowEnumSet {

    public void show() {

        EnumSet<Operation> allOperations1, allOperations2, operations1, operations2, operations3, operations4;

        allOperations1 = EnumSet.allOf(Operation.class);

        System.out.printf("allOf: %s", allOperations1);//allOf: [PLUS, MINUS, TIMES, DIVIDE]

        allOperations2 = EnumSet.copyOf(allOperations1);

        System.out.printf("\ncopyOf: %s", allOperations2);//copyOf: [PLUS, MINUS, TIMES, DIVIDE]

        operations1 = EnumSet.noneOf(Operation.class);

        operations1.add(Operation.PLUS);

        operations1.add(Operation.MINUS);

        System.out.printf("\nnoneOf y add: %s", operations1);//noneOf y add: [PLUS, MINUS]

        operations2 = EnumSet.complementOf(operations1);

        System.out.printf("\ncomplementOf: %s", operations2);//complementOf: [TIMES, DIVIDE]

        operations3 = EnumSet.of(Operation.DIVIDE, Operation.MINUS);

        System.out.printf("\nof: %s", operations3);//of: [MINUS, DIVIDE]

        operations4 = EnumSet.range(Operation.MINUS, Operation.DIVIDE);

        System.out.printf("\nrange: %s\n", operations4);//range: [MINUS, TIMES, DIVIDE]     

        System.out.println(operations4.contains(Operation.PLUS));//false

        System.out.println(operations4.contains(Operation.MINUS));//true

    }

    public static void main(String[] args) {

        new ShowEnumSet().show();

    }

}
```

Salida por consola:

```text
allOf: [PLUS, MINUS, TIMES, DIVIDE]

copyOf: [PLUS, MINUS, TIMES, DIVIDE]

noneOf y add: [PLUS, MINUS]

complementOf: [TIMES, DIVIDE]

of: [MINUS, DIVIDE]

range: [MINUS, TIMES, DIVIDE]

false

true
```

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20EnumSet.html)

---

## 10. Mapas

Las colecciones de tipo Set tienen el inconveniente de tener que almacenar una copia exacta del elemento a buscar. Sin embargo, en la práctica es habitual que haya datos que se consideran clave, es decir, que identifican a cada objeto (el dni de las personas por ejemplo) de tal manera que se buscan los datos en base a esa clave y por otro lado se almacenan el resto de los datos. Los mapas permiten definir colecciones de elementos que poseen pares de datos clave-valor. Esto se utiliza para localizar valores en función de la clave que poseen. Son muy interesantes y rápidos. Los mapas también son conocidos como diccionarios.

La interfaz `Map<K,V>` es la raíz de todas las clases que implementan mapas. Hasta la versión 5, los mapas eran colecciones de pares clave-valor donde tanto la clave como el valor eran de tipo Object. Desde la versión 5, esta interfaz tiene dos genéricos: `K` para el tipo de datos de la clave y `V` para el tipo de los valores. Esta estructura de datos nos permite obtener el objeto `V` muy rápidamente a partir de su clave `K`.

Esta interfaz no hereda de Collection por lo que no tiene los métodos vistos anteriormente. La razón es que la obtención, búsqueda y borrado de elementos se hace de manera muy distinta.

Las claves no se pueden repetir por lo que se implementan con una tabla hash para que no haya duplicados. Por lo tanto, la clase que se utilice como clave tiene que sobrescribir los métodos `equals` y `hashCode`.

Veamos algunos métodos de esta interfaz:

- `boolean containsKey(Object key)`: devuelve _true_ si el mapa contiene dicha clave.
    
- `boolean containsValue(Object value)`: devuelve _true_ si el mapa contiene dicho valor.
    
- `V get(Object key)`: devuelve el valor asociado a la clave o _null_ si no existe esa clave en el mapa.
    
- `V getOrDefault(Object key, V defaultValue)`: devuelve el valor asociado a la clave o _defaultValue_ si no existe esa clave en el mapa.
    
- `V put(K key, V value)`: añade un par clave-valor al mapa. Si ya había un valor para esa clave, se reemplaza. Devuelve el valor que tenía antes dicha clave o _null_ si la clave no estaba en el mapa.
    
- `V putIfAbsent(K key, V value)`: si la clave especificada no está ya asociada a un valor o está asignada a _null_, se le asocia al valor dado y devuelve _null_, en caso contrario, devuelve el valor previamente asociado con la clave.
    
- `void putAll(Map<? extends K,? extends V> m)`: añade los pares clave-valor del mapa _m_.
    
- `V remove(Object key)`: elimina la clave y su valor asociado, el cual se devuelve. Si no existe dicha clave, devuelve _null_.
    
- `int size()`: devuelve el número de pares clave-valor del mapa.
    

Existen varios tipos de implementaciones realizadas dentro de la plataforma Java:

- **HashMap**: este implementación almacena las claves en una tabla _hash_. Es la implementación con mejor rendimiento de todas pero no garantiza ningún orden a la hora de realizar iteraciones.
    
- **LinkedHashMap**: esta implementación almacena las claves en función del orden de inserción. Es un poco más costosa que _HashMap_.
    
- **TreeMap**: esta implementación utiliza una estructura de árbol para ordenar las claves. Es bastante más lenta que _HashMap_. La veremos más adelante en el apartado de los árboles.
    

### 10.1 Clase HashMap

Esta implementación proporciona tiempos constantes en las operaciones básicas siempre y cuando la función _hash_ disperse de forma correcta las claves dentro de la tabla _hash_. Es importante definir el tamaño inicial de la tabla ya que este tamaño marcará el rendimiento de esta implementación. No garantiza ningún orden a la hora de recorrer el mapa.

Veamos un ejemplo de un mapa de vehículos donde la clave es la matrícula. Añadimos la matrícula como atributo por lo que hay que generar de nuevo los métodos `toString`, `equals` y `hashcode`:

```java
package tema12_Colecciones.mapas;

public class Vehicle {

    private String registration;//Atributo para almacenar la matrícula del coche

    private int wheelCount;

    private double speed;

    private String colour;

    public Vehicle(String registration, int wheelCount, String colour) {

        this.registration = registration;

        this.wheelCount = wheelCount;

        this.colour = colour;

        speed = 0;

    }

    public int getWheelCount() {

        return wheelCount;

    }

    public double getSpeed() {

        return speed;

    }

    public String getColour() {

        return colour;

    }

    public void setColour(String colour) {

        this.colour = colour;

    }

    public String getRegistration() {//get de la matrícula

        return registration;

    }

    public void accelerate(double amount) {

        speed += amount;

    }

    public void brake(double amount) {

        speed -= amount;

    }

    /* Como se ha añadido el nuevo atributo para la 

     * matrícula, hay que generar de nuevo los 

     * métodos toString, equals y hashcode:

     */

    @Override

    public String toString() {

        return String.format("Matrícula: %s Número de ruedas: %d, color: %s, velocidad: %.2f", registration, wheelCount, colour, speed);

    }

    @Override

    public int hashCode() {

        final int prime = 31;

        int result = 1;

        result = prime * result + ((colour == null) ? 0 : colour.hashCode());

        result = prime * result + ((registration == null) ? 0 : registration.hashCode());

        result = prime * result + wheelCount;

        return result;

    }

    @Override

    public boolean equals(Object obj) {

        if (this == obj)

            return true;

        if (obj == null)

            return false;

        if (!(obj instanceof Vehicle))

            return false;

        Vehicle other = (Vehicle) obj;

        if (colour == null) {

            if (other.colour != null)

                return false;

        } else if (!colour.equals(other.colour))

            return false;

        if (registration == null) {

            if (other.registration != null)

                return false;

        } else if (!registration.equals(other.registration))

            return false;

        if (wheelCount != other.wheelCount)

            return false;

        return true;

    }

}
```

```java
package tema12_Colecciones.mapas;

import java.util.HashMap;

import java.util.Map;

public class ShowHashMap {

    public void show() {

        Map<String, Vehicle> map = new HashMap<>();

        Map<String, Vehicle> map2 = new HashMap<>();

        Vehicle vehicles[] = new Vehicle[6];

        vehicles[0] = new Vehicle("9685KMX", 4, "azul");

        vehicles[1] = new Vehicle("1235GTR", 2, "rojo");

        vehicles[2] = new Vehicle("7314QWE", 4, "verde");

        vehicles[3] = new Vehicle("5930POI", 2, "negro");

        vehicles[4] = new Vehicle("1705UBG", 4, "blanco");

        vehicles[5] = new Vehicle("3495JZA", 2, "naranja");

        for (int i = 0; i < vehicles.length; i++) {

            map.put(vehicles[i].getRegistration(), vehicles[i]);

        }

        System.out.println(map.containsKey("1005SAW"));//false

        System.out.println(map.containsKey("1705UBG"));//true

        System.out.println(map.containsValue(new Vehicle("5930POI", 4, "negro")));//false

        System.out.println(map.containsValue(new Vehicle("5930POI", 2, "negro")));//true

        System.out.println(map.get("4554ASD"));//null

        System.out.println(map.get("1705UBG"));//Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

        System.out.println(map.getOrDefault("8080SAS", new Vehicle("4554ASD", 4, "negro")));//Matrícula: 4554ASD Número de ruedas: 4, color: negro, velocidad: 0,00

        System.out.println(map.getOrDefault("1705UBG", new Vehicle("4554ASD", 4, "negro")));//Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

        System.out.println(map.put("6320LPL", new Vehicle("6320LPL", 2, "verde")));//null

        System.out.println(map.put("6320LPL", new Vehicle("6320LPL", 4, "beis")));//Matrícula: 6320LPL Número de ruedas: 2, color: verde, velocidad: 0,00

        System.out.println(map.putIfAbsent("4687RTB", new Vehicle("4687RTB", 2, "blanco")));//null

        System.out.println(map.putIfAbsent("4687RTB", new Vehicle("4687RTB", 4, "naranja")));//Matrícula: 4687RTB Número de ruedas: 2, color: blanco, velocidad: 0,00

        System.out.println(map.remove("1234ABC"));//null

        System.out.println(map.remove("4687RTB"));//Matrícula: 4687RTB Número de ruedas: 2, color: blanco, velocidad: 0,00

        System.out.printf("El mapa tiene %d vehículos", map.size());

        map2.put("7410HJH", new Vehicle("7410HJH", 4, "rojo"));

        map2.put("8520FGF", new Vehicle("8520FGF", 2, "verde"));

        map.putAll(map2);//añade a map los pares clave-valor del mapa map2

        System.out.printf("\nDespués de añadirle map2, el mapa tiene %d vehículos", map.size());

    }

    public static void main(String[] args) {

        new ShowHashMap().show();

    }

}
```

Salida por consola:

```text
false

true

false

true

null

Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

Matrícula: 4554ASD Número de ruedas: 4, color: negro, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

null

Matrícula: 6320LPL Número de ruedas: 2, color: verde, velocidad: 0,00

null

Matrícula: 4687RTB Número de ruedas: 2, color: blanco, velocidad: 0,00

null

Matrícula: 4687RTB Número de ruedas: 2, color: blanco, velocidad: 0,00

El mapa tiene 7 vehículos

Después de añadirle map2, el mapa tiene 9 vehículos

Veamos las distintas maneras de recorrer un mapa:

- `Set<K> keySet()`: devuelve un conjunto con todas las claves. Como entre las claves no puede haber elementos duplicados , las claves forman un conjunto (_Set_).
    
- `Collection<V> values()`: devuelve una colección con todos los valores. Los valores sí pueden estar duplicados, por lo tanto, este método devuelve un _Collection_.
```
    
- `Set<Map.Entry<K,V>> entrySet()`: devuelve un conjunto de objetos _Map.Entry<K, V>_. Los pares de elementos (también llamados entradas) de los que está compuesto un _Map<K, V>_ son de un tipo que viene implementado por la interfaz _Map.Entry<K, V>_. La interfaz _Map.Entry<K, V>_ se define de forma interna a la interfaz _Map<K, V>_ y representa un objeto de par clave-valor, es decir, mediante esta interfaz podemos trabajar con una entrada del mapa. Veamos algunos métodos de la interfaz _Map.Entry<K, V>_:
    
    - `K getKey()`: retorna la clave.
        
    - `V getValue()`: retorna el valor.
        
    - `V setValue(V value)`: reemplaza el valor por _value_ y devuelve el valor anterior.
        

```java
package tema12_Colecciones.mapas;

import java.util.HashMap;

import java.util.Iterator;

import java.util.Map;

import java.util.Set;

public class TraverseHashMap {

    public void show() {

        Map<String, Vehicle> map = new HashMap<>();

        Vehicle vehicles[] = new Vehicle[6];

        vehicles[0] = new Vehicle("9685KMX", 4, "azul");

        vehicles[1] = new Vehicle("1235GTR", 2, "rojo");

        vehicles[2] = new Vehicle("7314QWE", 4, "verde");

        vehicles[3] = new Vehicle("5930POI", 2, "negro");

        vehicles[4] = new Vehicle("1705UBG", 4, "blanco");

        vehicles[5] = new Vehicle("3495JZA", 2, "naranja");

        for (int i = 0; i < vehicles.length; i++) {

            map.put(vehicles[i].getRegistration(), vehicles[i]);

        }

        System.out.println("Claves del mapa:\n");

        for (String s : map.keySet()) {//keySet() devuelve un conjunto con todas las claves

            System.out.println(s);

        }

        System.out.println("\nValores del mapa:\n");

        for (Vehicle v : map.values()) {//values() devuelve una colección con todos los vehículos

            System.out.println(v);

        }

        System.out.println("\nPares clave-valor del mapa usando un foreach:\n");

        for (Map.Entry<String, Vehicle> entry : map.entrySet()) {

            System.out.printf("Matrícula -> %s Vehículo -> %s\n", entry.getKey(), entry.getValue());

        }

        System.out.println("\nPares clave-valor del mapa usando iteradores:\n");

        Set<Map.Entry<String, Vehicle>> entrySet = map.entrySet();

        Iterator<Map.Entry<String, Vehicle>> it = entrySet.iterator();

        Map.Entry<String, Vehicle> entry;

        while (it.hasNext()) {

            entry = it.next();

            System.out.printf("Matrícula -> %s Vehículo -> %s\n", entry.getKey(), entry.getValue());

        }

    }

    public static void main(String[] args) {

        new TraverseHashMap().show();

    }

}
```

Salida por consola:

```text
Claves del mapa:

3495JZA

1705UBG

1235GTR

7314QWE

9685KMX

5930POI

Valores del mapa:

Matrícula: 3495JZA Número de ruedas: 2, color: naranja, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 5930POI Número de ruedas: 2, color: negro, velocidad: 0,00

Pares clave-valor del mapa usando un foreach:

Matrícula -> 3495JZA Vehículo -> Matrícula: 3495JZA Número de ruedas: 2, color: naranja, velocidad: 0,00

Matrícula -> 1705UBG Vehículo -> Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

Matrícula -> 1235GTR Vehículo -> Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula -> 7314QWE Vehículo -> Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula -> 9685KMX Vehículo -> Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula -> 5930POI Vehículo -> Matrícula: 5930POI Número de ruedas: 2, color: negro, velocidad: 0,00

Pares clave-valor del mapa usando iteradores:

Matrícula -> 3495JZA Vehículo -> Matrícula: 3495JZA Número de ruedas: 2, color: naranja, velocidad: 0,00

Matrícula -> 1705UBG Vehículo -> Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

Matrícula -> 1235GTR Vehículo -> Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula -> 7314QWE Vehículo -> Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula -> 9685KMX Vehículo -> Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula -> 5930POI Vehículo -> Matrícula: 5930POI Número de ruedas: 2, color: negro, velocidad: 0,00
```

### 10.2 Clase LinkedHashMap

Almacena las claves en función del orden de inserción. Es un poco más costosa que _HashMap_.

```java
package tema12_Colecciones.mapas;

import java.util.LinkedHashMap;

import java.util.Map;

public class ShowLinkedHashMap {

    public void show() {

        Map<String, Vehicle> map = new LinkedHashMap<>();

        Vehicle vehicles[] = new Vehicle[6];

        vehicles[0] = new Vehicle("9685KMX", 4, "azul");

        vehicles[1] = new Vehicle("1235GTR", 2, "rojo");

        vehicles[2] = new Vehicle("7314QWE", 4, "verde");

        vehicles[3] = new Vehicle("5930POI", 2, "negro");

        vehicles[4] = new Vehicle("1705UBG", 4, "blanco");

        vehicles[5] = new Vehicle("3495JZA", 2, "naranja");

        for (int i = 0; i < vehicles.length; i++) {

            map.put(vehicles[i].getRegistration(), vehicles[i]);

        }

        for (Map.Entry<String, Vehicle> entry : map.entrySet()) {

            System.out.printf("Matrícula -> %s Vehículo -> %s\n", entry.getKey(), entry.getValue());

        }

    }

    public static void main(String[] args) {

        new ShowLinkedHashMap().show();

    }

}
```

Salida por consola:

```text
Matrícula -> 9685KMX Vehículo -> Vehicle [registration=9685KMX, wheelCount=4, speed=0.0, colour=azul]

Matrícula -> 1235GTR Vehículo -> Vehicle [registration=1235GTR, wheelCount=2, speed=0.0, colour=rojo]

Matrícula -> 7314QWE Vehículo -> Vehicle [registration=7314QWE, wheelCount=4, speed=0.0, colour=verde]

Matrícula -> 5930POI Vehículo -> Vehicle [registration=5930POI, wheelCount=2, speed=0.0, colour=negro]

Matrícula -> 1705UBG Vehículo -> Vehicle [registration=1705UBG, wheelCount=4, speed=0.0, colour=blanco]

Matrícula -> 3495JZA Vehículo -> Vehicle [registration=3495JZA, wheelCount=2, speed=0.0, colour=naranja]

Podemos observar que los datos se muestran en el mismo orden en el que se insertaron.
```

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20Mapas.html)

### 10.3 Ejemplo de uso de un mapa en un enum

Si hemos sobrescrito el método `toString()` o las instancias del _enum_ tienen alguna forma adicional de referirnos a ellas, tiene bastante sentido que creemos un método estático parecido a `valueOf()`, pero que reciba dicha forma adicional de referirnos a las instancias.

```java
package tema12_Colecciones.mapas;

import java.util.Map;

public enum Operation {

    PLUS('+') {

        @Override

        public double apply(double x, double y) {

            return x + y;

        }

    },

    MINUS('-') {

        @Override

        public double apply(double x, double y) {

            return x - y;

        }

    },

    TIMES('*') {

        @Override

        public double apply(double x, double y) {

            return x * y;

        }

    },

    DIVIDE('/') {

        @Override

        public double apply(double x, double y) {

            return x / y;

        }

    };

    private final char symbol;

    private static final Map<Character, Operation> symbolToOperation = Map.of(Operation.PLUS.getSymbol(), Operation.PLUS,

            Operation.MINUS.getSymbol(), Operation.MINUS, Operation.TIMES.getSymbol(), Operation.TIMES,

            Operation.DIVIDE.getSymbol(), Operation.DIVIDE);

    Operation(char symbol) {

        this.symbol = symbol;

    }

    public char getSymbol() {

        return symbol;

    }

    public abstract double apply(double x, double y);

    public static Operation fromSymbol(char symbol) {

        return symbolToOperation.get(symbol);

    }

}
```

```java
package tema12_Colecciones.mapas;

public class ExampleUseMapEnum {

    public void show() {

        Operation operation;

        operation = Operation.fromSymbol('+');//operation se asigna con la instancia correspondiente al símbolo +

        System.out.printf("La variable operation es de tipo enum %s y su símbolo es %c", operation,

                operation.getSymbol());

    }

    public static void main(String[] args) {

        new ExampleUseMapEnum().show();

    }

}
```

Salida por consola:

```text
La variable operation es de tipo enum PLUS y su símbolo es +
```

Como vemos en el código anterior, creamos un mapa estático que relaciona cada símbolo con cada instancia, de manera que podamos obtener la instancia adecuada a partir del símbolo. Debemos tener en cuenta que no está permitido que los constructores de las instancias de un _enum_ accedan a los atributos estáticos del _enum_, con la excepción de las constantes de las instancias, dado que los atributos estáticos aún no han sido inicializados cuando se están ejecutando los constructores de las instancias. En los constructores de las instancias tampoco se puede acceder a otras instancias del _enum_.

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20Mapa%20en%20un%20enum.html)

### 10.4 Clase EnumMap

Es una implementación de mapa muy eficiente donde las claves son elementos de una enumeración.

```java
package tema12_Colecciones.enumMap;

public enum Operation {

    PLUS('+'), MINUS('-'), TIMES('*'), DIVIDE('/');

    private final char symbol;

    Operation(char symbol) {

        this.symbol = symbol;

    }

    public char getSymbol() {

        return symbol;

    }

}
```

```java
package tema12_Colecciones.enumMap;

import java.util.EnumMap;

import java.util.Map;

public class ShowEnumMap {

    public void show() {

        EnumMap<Operation, String> operationsMap = new EnumMap<>(Operation.class);

        operationsMap.put(Operation.PLUS, "Esta operación se utiliza para sumar");

        operationsMap.put(Operation.MINUS, "Esta operación se utiliza para restar");

        operationsMap.put(Operation.TIMES, "Esta operación se utiliza para multiplicar");

        operationsMap.put(Operation.DIVIDE, "Esta operación se utiliza para dividir");

        for (Map.Entry<Operation, String> entry : operationsMap.entrySet()) {

            System.out.printf("%-6s: %s\n", entry.getKey(), entry.getValue());

        }

    }

    public static void main(String[] args) {

        new ShowEnumMap().show();

    }

}
```

Salida por consola:

```text
PLUS  : Esta operación se utiliza para sumar

MINUS : Esta operación se utiliza para restar

TIMES : Esta operación se utiliza para multiplicar

DIVIDE: Esta operación se utiliza para dividir
```

---

## 11. Árboles

Los árboles se caracterizan por almacenar sus nodos en forma jerárquica y no en forma lineal como las listas.

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/arbol1.png)

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/arbol2.png)

Un árbol es una estructura en la que los datos se organizan en nodos. Los **árboles binarios** son aquellos en los que un nodo solamente puede tener dos hijos como máximo. Se utilizan para ordenar datos, de tal manera que a la izquierda se colocan los valores menores y a la derecha los valores mayores. Un árbol binario se puede recorrer de varias formas, siendo el recorrido **inorden** el que muestra los datos ordenados: subárbol izquierdo, raíz, subárbol derecho. Veamos un ejemplo:

![](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/arbolBinario.png)

Nos posicionamos en el 8. Mientras tenga subárbol iquierdo vamos avanzando hasta llegar al 1. Como es una hoja, la mostramos: el **1**. Luego, mostramos la raíz: el **3**. Después, continuamos con el subárbol derecho. Nos encontramos con el 6 pero tiene subárbol izquierdo, así que avanzamos hasta el 4. Como es una hoja, lo mostramos: el **4**. Luego, continuamos con la raíz: el **6**. Después, continuamos con el subárbol derecho, avanzando hasta el 7. Como es hoja, lo mostramos: el **7**. Ya hemos tratado todo el subárbol izquierdo del 8, que es la raíz. Ahora mostramos la raíz: el **8**, y a continuación comenzamos con el subárbol derecho del 8. Y así sucesivamente...El resultado final es: 1, 3, 4, 6, 7, 8, 10, 13 y 14, es decir, los elementos ordenados de menor a mayor.

Si queremos introducir un nuevo nodo en el árbol, hay que tener cuidado de no romper la estructura ni el orden del árbol. Hay que tener en cuenta que cada nodo no puede tener más de dos hijos, por esta razón si un nodo ya tiene 2 hijos, el nuevo nodo nunca se podrá insertar como su hijo. Con esta restricción nos aseguramos mantener la estructura del árbol, pero aún nos falta mantener el orden. Para localizar el lugar adecuado del árbol donde insertar el nuevo nodo se realizan comparaciones entre los nodos del árbol y el elemento a insertar. El primer nodo que se compara es el nodo raíz, si el nuevo nodo es menor que el raíz, la búsqueda prosigue por el nodo izquierdo de éste. Si el nuevo nodo fuese mayor, la búsqueda seguiría por el hijo derecho. Y así sucesivamente hasta llegar a un nodo que no tenga hijo en la rama por la que la búsqueda debería seguir. En este caso, el nuevo nodo se inserta en ese hueco, como su nuevo hijo.

Por ejemplo, queremos insertar el elemento 9. Lo primero es comparar el nuevo elemento con el nodo raíz. Como 9 > 8, entonces la búsqueda prosigue por el lado derecho. Ahora el nuevo nodo se compara con el elemento 10. En este caso 9 < 10, por lo que hay que continuar la búsqueda por la rama izquierda. Como la rama izquierda de 10 no tiene ningún nodo, se inserta en ese lugar el nuevo nodo.

La interfaz `SortedSet<E>` es la encargada de definir esta estructura. Esta interfaz es hija de `Set<E>`, que a su vez es hija de `Collection<E>`, que a su vez es hija de `Iterable<E>`. Por lo tanto, tiene los métodos de todas y además añade sus propios métodos:

- `E first()`: devuelve el elemento más pequeño.
    
- `E last()`: devuelve el elemento más grande.
    
- `SortedSet<E> headSet(E toElement)`: devuelve un _SortedSet_ que contendrá todos los elementos menores que _toElement_.
    
- `SortedSet<E> tailSet(E fromElement)`: devuelve un _SortedSet_ que contendrá todos los elementos mayores que _fromElement_.
    
- `SortedSet<E> subSet(E fromElement, E toElement)`: devuelve un _SortedSet_ que contendrá los elementos que van desde _fromElement_ incluido hasta _toElement_ excluido.
    

Pero ¿cómo ordenamos elementos como por ejemplo vehículos? Para ello, Java nos proporciona dos interfaces: `Comparable<T>` y `Comparator<T>`. La diferencia entre ambas es que _Comparable_ se implementa desde la propia clase que se quiere ordenar y _Comparator_ no.

### 11.1 Clase TreeSet

La clase `TreeSet<E>` es la que se utiliza prioritariamente para trabajar con árboles ordenados ya que implementa la interfaz `SortedSet<E>`.

Los objetos a incluir en un _TreeSet_ deben implementar _Comparable_ o bien crear el árbol con un constructor que reciba un _Comparator_.

La interfaz `Comparable` contiene un único método, el método `compareTo`, que recibe un objeto de la misma clase y que debe realizar una comparación entre ambos objetos, retornando un valor entero negativo, cero o positivo, dependiendo de si el objeto sobre el que se ejecuta es, respectivamente, menor, igual o mayor que el objeto recibido.

La definición de la interfaz es la siguiente:

public interface Comparable<T> {

    int compareTo(T o);

}

Por ejemplo, si quisiéramos crear un árbol para ordenar vehículos, lo primero que tendríamos que hacer es que la clase _Vehicle_ implemente la interfaz _Comparable_ y que el método _compareTo_ ordene por el atributo que deseemos. Por ejemplo, vamos a ordenar vehículos alfabéticamente por el color. Como el color es de tipo _String_, debemos utilizar el _compareTo_ de la clase _String_:

```java
package tema12_Colecciones.arboles1;

public class Vehicle implements Comparable<Vehicle> {//La clase Vehicle implementa Comparable

    private String registration;

    private int wheelCount;

    private double speed;

    private String colour;

    public Vehicle(String registration, int wheelCount, String colour) {

        this.registration = registration;

        this.wheelCount = wheelCount;

        this.colour = colour;

        speed = 0;

    }

    public int getWheelCount() {

        return wheelCount;

    }

    public double getSpeed() {

        return speed;

    }

    public String getColour() {

        return colour;

    }

    public void setColour(String colour) {

        this.colour = colour;

    }

    public String getRegistration() {

        return registration;

    }

    public void accelerate(double amount) {

        speed += amount;

    }

    public void brake(double amount) {

        speed -= amount;

    }

    @Override

    public String toString() {

        return String.format("Matrícula: %s Número de ruedas: %d, color: %s, velocidad: %.2f", registration, wheelCount, colour, speed);

    }

    @Override

    public int compareTo(Vehicle o) {//Tenemos que definir en este método el criterio de ordenación

        return colour.compareTo(o.colour);//Utilizamos el compareTo de la clase String

    }

}
```

```java
package tema12_Colecciones.arboles1;

import java.util.SortedSet;

import java.util.TreeSet;

public class TreeSet1 {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>();

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "negro"));

        tree.add(new Vehicle("1705UBG", 4, "blanco"));

        tree.add(new Vehicle("3495JZA", 2, "naranja"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new TreeSet1().show();

    }

}
```

Salida por consola:

```text
Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

Matrícula: 3495JZA Número de ruedas: 2, color: naranja, velocidad: 0,00

Matrícula: 5930POI Número de ruedas: 2, color: negro, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Pero ¿qué ocurriría si tuviéramos colores repetidos?:
```

```java
package tema12_Colecciones.arboles1;

import java.util.SortedSet;

import java.util.TreeSet;

public class TreeSet2 {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>();

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "azul"));

        tree.add(new Vehicle("1705UBG", 4, "rojo"));

        tree.add(new Vehicle("3495JZA", 2, "verde"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new TreeSet2().show();

    }

}
```

Salida por consola:

```text
Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00
```

Los tres primeros vehículos se introducen en el árbol. Cuando se va a introducir el cuarto que es de color azul, el árbol lo va comparando con _compareTo_ con los vehículos que ya existen en el árbol para encontrar la posición ordenada donde incluirlo. Pero cuando lo compara con el que es azul, el _compareTo_ le devuelve 0, por lo que el árbol interpreta que ese objeto ya existe en el árbol, que es igual a otro, por lo tanto no lo incluye en el árbol. Lo mismo ocurre con el quinto y el sexto. Por lo tanto, lo que ocurriría es que los 3 últimos no se introducen en el árbol porque el _compareTo_ devuelve 0 entre vehículos del mismo color, por lo que el árbol considera que son iguales. En estos casos, lo que se hace es que se incluye un segundo criterio de comparación: vamos a ordenar por el color, y en aquellos casos donde los vehículos tengan el mismo color, entonces vamos a ordenar por matrícula:

```java
package tema12_Colecciones.arboles2;

public class Vehicle implements Comparable<Vehicle> {

    private String registration;

    private int wheelCount;

    private double speed;

    private String colour;

    public Vehicle(String registration, int wheelCount, String colour) {

        this.registration = registration;

        this.wheelCount = wheelCount;

        this.colour = colour;

        speed = 0;

    }

    public int getWheelCount() {

        return wheelCount;

    }

    public double getSpeed() {

        return speed;

    }

    public String getColour() {

        return colour;

    }

    public void setColour(String colour) {

        this.colour = colour;

    }

    public String getRegistration() {

        return registration;

    }

    public void accelerate(double amount) {

        speed += amount;

    }

    public void brake(double amount) {

        speed -= amount;

    }

    @Override

    public String toString() {

        return String.format("Matrícula: %s Número de ruedas: %d, color: %s, velocidad: %.2f", registration, wheelCount, colour, speed);

    }

    @Override

    public int compareTo(Vehicle o) {

        int result = colour.compareTo(o.colour);

        if (result == 0) {//Introducimos un segundo criterio de ordenación

            result = registration.compareTo(o.registration);

        }

        return result;

    }

}
```

```java
package tema12_Colecciones.arboles2;

import java.util.SortedSet;

import java.util.TreeSet;

public class ShowTreeSet {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>();

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "azul"));

        tree.add(new Vehicle("1705UBG", 4, "rojo"));

        tree.add(new Vehicle("3495JZA", 2, "verde"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new ShowTreeSet().show();

    }

}
```

Salida por consola:

```text
Matrícula: 5930POI Número de ruedas: 2, color: azul, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: rojo, velocidad: 0,00

Matrícula: 3495JZA Número de ruedas: 2, color: verde, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00
```

Pero, ¿qué ocurriría si la clase _Vehicle_ no implementase la interfaz _Comparable_? Pues que no contendría el método _compareTo_, entonces el árbol no tendría la información de cómo ordenar los vehículos. En este caso, se lanzaría una excepción `ClassCastException`:

```java
package tema12_Colecciones.arboles3;

public class Vehicle {//No implementa Comparable por lo que no contiene el método compareTo

    private String registration;

    private int wheelCount;

    private double speed;

    private String colour;

    public Vehicle(String registration, int wheelCount, String colour) {

        this.registration = registration;

        this.wheelCount = wheelCount;

        this.colour = colour;

        speed = 0;

    }

    public int getWheelCount() {

        return wheelCount;

    }

    public double getSpeed() {

        return speed;

    }

    public String getColour() {

        return colour;

    }

    public void setColour(String colour) {

        this.colour = colour;

    }

    public String getRegistration() {

        return registration;

    }

    public void accelerate(double amount) {

        speed += amount;

    }

    public void brake(double amount) {

        speed -= amount;

    }

    @Override

    public String toString() {

        return String.format("Matrícula: %s Número de ruedas: %d, color: %s, velocidad: %.2f", registration, wheelCount, colour, speed);

    }

}
```

```java
package tema12_Colecciones.arboles3;

import java.util.SortedSet;

import java.util.TreeSet;

public class ShowException {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>();

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "negro"));

        tree.add(new Vehicle("1705UBG", 4, "blanco"));

        tree.add(new Vehicle("3495JZA", 2, "naranja"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new ShowException().show();

    }

}
```

Salida por consola:

Exception in thread "main" java.lang.ClassCastException: class tema12_Colecciones.arboles3.Vehicle cannot be cast to class java.lang.Comparable (tema12_Colecciones.arboles3.Vehicle is in unnamed module of loader 'app'; java.lang.Comparable is in module java.base of loader 'bootstrap')

    at java.base/java.util.TreeMap.compare(TreeMap.java:1291)

    at java.base/java.util.TreeMap.put(TreeMap.java:536)

    at java.base/java.util.TreeSet.add(TreeSet.java:255)

    at tema12_Colecciones.arboles3.ShowException.show(ShowException.java:11)

    at tema12_Colecciones.arboles3.ShowException.main(ShowException.java:25)

Otra posibilidad es utilizar un objeto `Comparator<E>`. Esta es otra interfaz que define el método `compare` al que se le pasan los dos objetos a comparar y cuyo resultado es como el de _compareTo_ (0 si son iguales, positivo si el primero es mayor y negativo si el segundo es mayor). Para definir un comparador de esta forma, hay que crear una clase que implemente esta interfaz y definir el método _compare_, después crear un objeto de ese tipo y usarlo en la construcción del árbol mediante un constructor que recibe un _Comparator_: `TreeSet(Comparator<? super E> comparator)`. En este caso, ésa será la forma prioritaria para ordenar la lista, por encima del método compareTo de la interfaz Comparable. Como ya dijimos anteriormente, la diferencia entre _Comparable_ y _Comparator_ es que _Comparable_ se implementa desde la propia clase que se quiere ordenar y _Comparator_ no, ya que _Comparator_ se implementa desde otra clase distinta a la que se quiere ordenar:

```java
package tema12_Colecciones.arboles3;

import java.util.Comparator;

public class VehicleComparator implements Comparator<Vehicle> {

    @Override

    public int compare(Vehicle o1, Vehicle o2) {

        int result = o1.getColour().compareTo(o2.getColour());

        if (result == 0) {

            result = o1.getRegistration().compareTo(o2.getRegistration());

        }

        return result;

    }

}
```

```java
package tema12_Colecciones.arboles3;

import java.util.SortedSet;

import java.util.TreeSet;

public class ShowComparator {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>(new VehicleComparator());

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "azul"));

        tree.add(new Vehicle("1705UBG", 4, "rojo"));

        tree.add(new Vehicle("3495JZA", 2, "verde"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new ShowComparator().show();

    }

}
```

Salida por consola:

```text
Matrícula: 5930POI Número de ruedas: 2, color: azul, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: rojo, velocidad: 0,00

Matrícula: 3495JZA Número de ruedas: 2, color: verde, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00
```

Pero si esta comparación solamente la vamos a utilizar una vez, tenemos que crear una clase solamente para un uso. Y si necesitamos ordenar los vehículos de varias maneras, tenemos que tener una clase por cada criterio de ordenación. En estos casos, podemos utilizar una clase inline anónima:

```java
package tema12_Colecciones.arboles3;

import java.util.Comparator;

import java.util.SortedSet;

import java.util.TreeSet;

public class AnonymousComparator {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>(new Comparator<Vehicle>() {

            @Override

            public int compare(Vehicle o1, Vehicle o2) {

                int result = o1.getColour().compareTo(o2.getColour());

                if (result == 0) {

                    result = o1.getRegistration().compareTo(o2.getRegistration());

                }

                return result;

            }

        });

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "azul"));

        tree.add(new Vehicle("1705UBG", 4, "rojo"));

        tree.add(new Vehicle("3495JZA", 2, "verde"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new AnonymousComparator().show();

    }

}
```

Salida por consola:

```text
Matrícula: 5930POI Número de ruedas: 2, color: azul, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: rojo, velocidad: 0,00

Matrícula: 3495JZA Número de ruedas: 2, color: verde, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00
```

Si quisiéramos ordenar de manera descendente, cambiamos el orden entre _o1_ y _o2_, es decir, hacemos que sea _o2_ el que ejecute el _compareTo_:

```java
package tema12_Colecciones.arboles3;

import java.util.Comparator;

import java.util.SortedSet;

import java.util.TreeSet;

public class DescendingOrder {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>(new Comparator<Vehicle>() {

            /*

             * Si quisiéramos ordenar de manera descendente, 

             * cambiamos el orden entre o1 y o2, es decir, 

             * hacemos que sea o2 el que ejecute el compareTo

             */

            @Override

            public int compare(Vehicle o1, Vehicle o2) {

                int result = o2.getColour().compareTo(o1.getColour());

                if (result == 0) {

                    result = o2.getRegistration().compareTo(o1.getRegistration());

                }

                return result;

            }

        });

        tree.add(new Vehicle("9685KMX", 4, "azul"));

        tree.add(new Vehicle("1235GTR", 2, "rojo"));

        tree.add(new Vehicle("7314QWE", 4, "verde"));

        tree.add(new Vehicle("5930POI", 2, "azul"));

        tree.add(new Vehicle("1705UBG", 4, "rojo"));

        tree.add(new Vehicle("3495JZA", 2, "verde"));

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new DescendingOrder().show();

    }

}
```

Salida por consola:

```text
Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula: 3495JZA Número de ruedas: 2, color: verde, velocidad: 0,00

Matrícula: 1705UBG Número de ruedas: 4, color: rojo, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 5930POI Número de ruedas: 2, color: azul, velocidad: 0,00
```

Los comparadores de tipo Comparator permiten ordenar de diferentes formas, por eso en la práctica se utilizan mucho. Por ejemplo, el método _sort_ de la clase _Arrays_ también admite indicar un comparador para saber de qué forma deseamos ordenar el array.

Cuando creemos clases que representen valores que posean un determinado orden natural, como por ejemplo un orden alfabético, numérico o cronológico, deberemos hacer que dicha clase implemente la interfaz `Comparable`, permitiendo así que los objetos de dicha clase puedan trabajar con mucho algoritmos genéricos e implementaciones de colecciones que dependen de dicha interfaz.

La mayoría de las clases estándar que representan valores y de las clases _enums_ incorporadas a Java, implementan la interfaz _Comparable_, como por ejemplo la clase _String_. Las clases que definamos nosotros que representen valores también deberían implementarla.

A la hora de realizar la implementación debemos respetar una serie de reglas:

- `x.compareTo(y) == -y. compareTo(x)` para todo valor de `x` e `y`.
    
- La relación es transitiva, es decir, que si `(x. compareTo(y) > 0 && y.compareTo(z) > 0)` entonces `x.compareTo(z) > 0`.
    
- Si `x.compareTo(y) == 0` entonces `x.compareTo(z) == y.compareTo(z)` para cualquier valor de `z`.
    
- Se recomienda que si `(x.compareTo(y) == 0)`, `x.equals(y)` sea true.
    

Si para comparar los objetos debemos comparar un atributo de un tipo primitivo, se recomienda usar los métodos estáticos de comparación `compare` de las clases boxed (wrappers) correspondientes, como `Long.compare()`, `Float.compare()`, etc., disponibles a partir de Java 7, en vez de usar los operadores `<` o `>`, ya que son menos verbosos y propensos al error:

```java
package tema12_Colecciones.arboles3;

import java.util.Comparator;

import java.util.SortedSet;

import java.util.TreeSet;

public class CompareBoxedClasses {

    public void show() {

        SortedSet<Vehicle> tree = new TreeSet<>(new Comparator<Vehicle>() {

            @Override

            public int compare(Vehicle o1, Vehicle o2) {

                int result = Integer.compare(o1.getWheelCount(), o2.getWheelCount());

                if (result == 0) {

                    result = Double.compare(o1.getSpeed(), o2.getSpeed());

                }

                return result;

            }

        });

        Vehicle vehicles[] = new Vehicle[6];

        vehicles[0] = new Vehicle("9685KMX", 4, "azul");

        vehicles[0].accelerate(100);

        vehicles[1] = new Vehicle("1235GTR", 2, "rojo");

        vehicles[1].accelerate(150);

        vehicles[2] = new Vehicle("7314QWE", 4, "verde");

        vehicles[2].accelerate(200);

        vehicles[3] = new Vehicle("5930POI", 2, "negro");

        vehicles[3].accelerate(80);

        vehicles[4] = new Vehicle("1705UBG", 4, "blanco");

        vehicles[4].accelerate(75);

        vehicles[5] = new Vehicle("3495JZA", 2, "naranja");

        vehicles[5].accelerate(170);

        for (int i = 0; i < vehicles.length; i++) {

            tree.add(vehicles[i]);

        }

        for (Vehicle v : tree) {

            System.out.println(v);

        }

    }

    public static void main(String[] args) {

        new CompareBoxedClasses().show();

    }

}
```

Salida por consola:

```text
Matrícula: 5930POI Número de ruedas: 2, color: negro, velocidad: 80,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 150,00

Matrícula: 3495JZA Número de ruedas: 2, color: naranja, velocidad: 170,00

Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 75,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 100,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 200,00
```

### 11.2 Clase TreeMap

Esta implementación utiliza una estructura de árbol que permite que los elementos del mapa se ordenen en sentido ascendente según la clave, por lo tanto, la clase de las claves tiene que implementar la interfaz _Comparable_ o bien indicar un objeto _Comparator_ durante la creación del _TreeMap_ .

TreeMap implementa la interfaz `SortedMap` que, a su vez, es heredera de `Map`, por lo que todo lo dicho sobre los mapas funciona con las colecciones de tipo _TreeMap_.

```java
package tema12_Colecciones.arboles3;

import java.util.Map;

import java.util.SortedMap;

import java.util.TreeMap;

public class ShowTreeMap {

    public void show() {

        SortedMap<String, Vehicle> sortedMap = new TreeMap<>();

        Vehicle vehicles[] = new Vehicle[6];

        vehicles[0] = new Vehicle("9685KMX", 4, "azul");

        vehicles[1] = new Vehicle("1235GTR", 2, "rojo");

        vehicles[2] = new Vehicle("7314QWE", 4, "verde");

        vehicles[3] = new Vehicle("5930POI", 2, "negro");

        vehicles[4] = new Vehicle("1705UBG", 4, "blanco");

        vehicles[5] = new Vehicle("3495JZA", 2, "naranja");

        for (int i = 0; i < vehicles.length; i++) {

            sortedMap.put(vehicles[i].getRegistration(), vehicles[i]);

        }

        for (Map.Entry<String, Vehicle> entry : sortedMap.entrySet()) {

            System.out.printf("Matrícula -> %s Vehículo -> %s\n", entry.getKey(), entry.getValue());

        }

    }

    public static void main(String[] args) {

        new ShowTreeMap().show();

    }

}
```

Salida por consola:

```text
Matrícula -> 1235GTR Vehículo -> Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula -> 1705UBG Vehículo -> Matrícula: 1705UBG Número de ruedas: 4, color: blanco, velocidad: 0,00

Matrícula -> 3495JZA Vehículo -> Matrícula: 3495JZA Número de ruedas: 2, color: naranja, velocidad: 0,00

Matrícula -> 5930POI Vehículo -> Matrícula: 5930POI Número de ruedas: 2, color: negro, velocidad: 0,00

Matrícula -> 7314QWE Vehículo -> Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula -> 9685KMX Vehículo -> Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00
```

Como podemos observar, está ordenado ascendentemente por la matrícula ya que la matrícula es de tipo `String` que implementa la interfaz `Comparable`. Si la clave fuera una clase hecha por nosotros, tendríamos que hacer que implementara _Comparable_ o bien indicar un _Comparator_ en la creación del _TreeMap_.

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20%C3%81rboles.html)

---

## 12. Pilas y colas

Una cola es un tipo de dato que sigue el principio **FIFO** **(_first in, first out_)** que implica que el primer elemento en ser insertado en la cola es también el primero en ser eliminado de la misma.

En el mundo real podemos encontrar este ejemplo en las colas de un banco, la cadena de impresión de documentos, etc. En el caso de la cola en el banco, la primera persona en llegar es también la primera en irse (suponiendo una única ventanilla) y en los documentos a imprimir, la impresora imprime según el orden de llegada.

`Queue<E>` es una interfaz que hereda de _Collection_ que proporciona operaciones para trabajar con una cola. Veamos alguna de ellas:

- `boolean add(E e)`: inserta el elemento al final de la cola.
    
- `E element()`: Devuelve, pero no elimina, el principio de la cola. Lanza la excepción `NoSuchElementException` si la cola está vacía.
    
- `E peek()`: Devuelve, pero no elimina, el principio de la cola. Devuelve _null_ si la cola está vacía.
    
- `E poll()`: Devuelve y elimina el principio de la cola. Devuelve _null_ si la cola está vacía.
    
- `E remove()`: Devuelve y elimina el principio de la cola. Lanza la excepción `NoSuchElementException` si la cola está vacía.
    

`Deque<E>` representa una cola de doble extremo, lo que significa que se puede insertar y eliminar elementos desde ambos extremos de la cola. El nombre _Deque_ es una abreviatura de _Double Ended Queue_. Admite, por lo tanto, la implementación de la cola _FIFO_ como la implementación de la pila _LIFO_, que implica que el último elemento que se ha insertado, es el primero en ser eliminado: **LIFO** **(_last in, first out_).**

_Deque_ hereda de _Queue_, por lo que tiene todos sus métodos y además añade los suyos propios. Veamos algunos de ellos:

- `void addFirst(E e)`: inserta el elemento al principio.
    
- `void addLast(E e)`: inserta el elemento al final.
    
- `E getFirst()`: Devuelve, pero no elimina, el primer elemento. Lanza la excepción `NoSuchElementException` si el deque está vacío.
    
- `E getLast()`: Devuelve, pero no elimina, el último elemento. Lanza la excepción `NoSuchElementException` si el deque está vacío.
    
- `E peekFirst()`: Devuelve, pero no elimina, el primer elemento. Devuelve _null_ si el deque está vacío.
    
- `E peekLast()`: Devuelve, pero no elimina, el último elemento. Devuelve _null_ si el deque está vacío.
    
- `E pollFirst()`: Devuelve y elimina el primer elemento. Devuelve _null_ si el deque está vacío.
    
- `E pollLast()`: Devuelve y elimina el último elemento. Devuelve _null_ si el deque está vacío.
    
- `E removeFirst()`: Devuelve y elimina el primer elemento. Lanza la excepción `NoSuchElementException` si el deque está vacío.
    
- `E removeLast()`: Devuelve y elimina el último elemento. Lanza la excepción `NoSuchElementException` si el deque está vacío.
    

### 12.1 Clase ArrayDeque

La clase `ArrayDeque<E>` implementa la interfaz _Deque_ y por lo tanto, también _Queue_, ya que _Deque_ hereda de _Queue_.

Veamos un ejemplo de uso de _ArrayDeque_ utilizado como una cola:

```java
package tema12_Colecciones.pilasYColas;

import java.util.ArrayDeque;

import java.util.Queue;

public class ShowQueue {

    public void show() {

        Queue<Vehicle> queue = new ArrayDeque<>();

        queue.add(new Vehicle("9685KMX", 4, "azul"));

        queue.add(new Vehicle("1235GTR", 2, "rojo"));

        queue.add(new Vehicle("7314QWE", 4, "verde"));

        System.out.println(queue.element());//Devuelve pero no elimina: 9685KMX

        System.out.println(queue.peek());//Devuelve pero no elimina: 9685KMX

        System.out.println(queue.poll());//Devuelve y elimina: 9685KMX

        System.out.println(queue.remove());//Devuelve y elimina: 1235GTR

        System.out.println(queue.remove());//Devuelve y elimina el último, se queda la cola vacía: 7314QWE

        System.out.println(queue.peek());//Devuelve null

        System.out.println(queue.poll());//Devuelve null

        System.out.println(queue.element());//Lanza NoSuchElementException porque la cola está vacía

        System.out.println(queue.remove());//Lanza NoSuchElementException porque la cola está vacía

    }

    public static void main(String[] args) {

        new ShowQueue().show();

    }

}
```

Salida por consola:

```text
Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

null

null

Exception in thread "main" java.util.NoSuchElementException

    at java.base/java.util.ArrayDeque.getFirst(ArrayDeque.java:401)

    at java.base/java.util.ArrayDeque.element(ArrayDeque.java:550)

    at tema12_Colecciones.pilasYColas.ShowQueue.show(ShowQueue.java:21)

    at tema12_Colecciones.pilasYColas.ShowQueue.main(ShowQueue.java:28)

Veamos otro ejemplo de uso de un _ArrayDeque_ utilizado como una pila:
```

```java
package tema12_Colecciones.pilasYColas;

import java.util.ArrayDeque;

import java.util.Deque;

public class ShowDeque {

    public void show() {

        Deque<Vehicle> deque = new ArrayDeque<>();

        deque.add(new Vehicle("9685KMX", 4, "azul"));

        deque.add(new Vehicle("1235GTR", 2, "rojo"));

        deque.add(new Vehicle("7314QWE", 4, "verde"));

        System.out.println(deque.getLast());//Devuelve pero no elimina: 7314QWE

        System.out.println(deque.peekLast());//Devuelve pero no elimina: 7314QWE

        System.out.println(deque.pollLast());//Devuelve y elimina: 7314QWE

        System.out.println(deque.removeLast());//Devuelve y elimina: 1235GTR

        System.out.println(deque.removeLast());//Devuelve y elimina el último, se queda la pila vacía: 9685KMX

        System.out.println(deque.peekLast());//Devuelve null

        System.out.println(deque.pollLast());//Devuelve null

        System.out.println(deque.getLast());//Lanza NoSuchElementException porque la pila está vacía

        System.out.println(deque.removeLast());//Lanza NoSuchElementException porque la pila está vacía

    }

    public static void main(String[] args) {

        new ShowDeque().show();

    }

}
```

Salida por consola:

```text
Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula: 7314QWE Número de ruedas: 4, color: verde, velocidad: 0,00

Matrícula: 1235GTR Número de ruedas: 2, color: rojo, velocidad: 0,00

Matrícula: 9685KMX Número de ruedas: 4, color: azul, velocidad: 0,00

null

null

Exception in thread "main" java.util.NoSuchElementException

    at java.base/java.util.ArrayDeque.getLast(ArrayDeque.java:412)

    at tema12_Colecciones.pilasYColas.ShowDeque.show(ShowDeque.java:21)

    at tema12_Colecciones.pilasYColas.ShowDeque.main(ShowDeque.java:28)
```

[![Ejercicios](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Exercises.png)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/Ejercicios/Tema%2012.%20Colecciones/Ejercicios%2012%20Pilas%20y%20colas.html)

---

## 13. Clase Collections

La clase `Collections` contiene numerosos métodos estáticos para utilizar con todo tipo de colecciones, como por ejemplo, para añadir, buscar, copiar, reemplazar, ordenar, obtener el máximo o el mínimo, etc.

## Esquema resumen de conceptos clave

| Concepto | Idea principal |
| --- | --- |
| Colección | Estructura dinámica que agrupa elementos y permite añadir o eliminar contenido. |
| `Collection` y `List` | Interfaces base para operaciones comunes y secuencias ordenadas. |
| `Set` | Colección sin elementos duplicados; implementaciones comunes: `HashSet`, `LinkedHashSet`, `EnumSet`. |
| `Map` | Asocia claves únicas con valores; `HashMap`, `LinkedHashMap` y `EnumMap` ofrecen implementaciones distintas. |
| Ordenación | `TreeSet` y `TreeMap` organizan elementos según orden natural o comparador. |
| Iterador | Recorre colecciones y permite eliminar elementos durante iteración de forma controlada. |
| `equals` y `hashCode` | Definen igualdad lógica y comportamiento correcto en colecciones basadas en hash. |
| `Collections` | Clase de utilidades estáticas para operar con colecciones. |

## Relaciones

- [[Genéricos]] — colecciones tipadas con parámetros genéricos.
- [[Herencia]] — elementos pueden ordenarse por `Comparable` o `Comparator`.
- [[4.1 Arrays unidimensionales]] — arrays como origen o destino de colecciones.

## Para repasar

- [ ] Elegir interfaz e implementación según orden, duplicados y acceso requerido.
- [ ] Recorrer y modificar colecciones con iteradores.
- [ ] Implementar `equals` y `hashCode` coherentes para usar elementos en sets/maps.
- [ ] Diferenciar `Set`, `List`, `Map`, colas y pilas.
- [ ] Ordenar con `Comparable` y `Comparator` en sets y maps ordenados.
- [ ] Usar utilidades de `Collections` y operaciones de `ArrayDeque`.
