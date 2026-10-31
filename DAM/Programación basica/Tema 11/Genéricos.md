---
asignatura: Programacion_basica
tema: 11
tipo: tema
estado: en curso
fecha: 2026-10-06
tags:
  - DAM/tema
  - DAM/programacion-basica/genericos
---

# 11 · Genéricos

> [!info] Asignatura
> [[DAM/Programación basica/Indice|Programación básica]] · Tema 11 · Genéricos

## Índice del apartado

- [[#1. Introducción]]
- [[#2. Clases genéricas]]
- [[#3. Métodos genéricos]]
- [[#4. Interfaces genéricas]]
- [[#5. Uso de varios genéricos]]
- [[#6. Tipos vinculados (o limitados)]]
- [[#7. Tipos comodín]]

---

## 1. Introducción

Desde su versión original 1.0, muchas nuevas características han sido añadidas a Java. Todas han mejorado y ampliado el alcance del lenguaje, pero una que ha tenido un impacto especialmente profundo y de gran alcance es el uso de genéricos porque sus efectos se sintieron en todo el lenguaje Java ya que añadieron un elemento de sintaxis completamente nuevo y causaron cambios en muchas de las clases y métodos de la API principal. Los genéricos de Java están basados en los famosos _templates_ de C++ y se introdujeron en la versión 5 de Java.

En su esencia, el término **genérico** significa **tipo parametrizado**, es decir, el tipo de datos sobre el que se opera se especifica como parámetro. Muchos algoritmos son lógicamente los mismos, independientemente del tipo de datos a los que se apliquen. Por ejemplo, un algoritmo de ordenación es el mismo si está ordenando elementos de tipo entero, decimales o cadena. Con los genéricos, se puede definir un algoritmo una vez, independientemente del tipo de datos y luego aplicar ese algoritmo a una amplia variedad de tipos de datos sin ningún esfuerzo adicional.

Lo que se use en un genérico debe ser un objeto, por lo tanto, los genéricos no funcionan con datos primitivos. Para resolver esta situación, la API de Java incorpora las clases envoltorio (wrapper class), que no son más que dotar a los datos primitivos con un envoltorio que permita tratarlos como objetos.

Los genéricos permiten crear clases, métodos e interfaces en los que los tipos de datos sobre los que actúan son un parámetro más, de manera que pueden adaptarse de forma automática para emplear dichos tipos.

---

## 2. Clases genéricas

Cuando una clase tiene algún parámetro de tipo se denomina **clase genérica**. Al crear objetos de esa clase, se debe indicar el tipo real por el que se va a sustituir el genérico. A partir de ese momento, donde se utilice el genérico, se sustituirá por el tipo real con el que se ha creado el objeto.

Veamos un ejemplo de clase genérica:

```java
package tema11_Genericos;

public class GenericClass<T> {//Clase genérica de tipo T

    private T attribute;//Declaramos un atributo de tipo T

    public GenericClass(T attribute) {

        this.attribute = attribute;

    }

    public T getAttribute() {

        return attribute;

    }

    public void show() {

        System.out.printf("El tipo de T es %s", attribute.getClass().getSimpleName());

        System.out.printf("  --->  Valor del atributo: %s\n", getAttribute());

    }

}
```

```java
package tema11_Genericos;

public class MainGenericClass {

    public void show() {

        //T es un parámetro de tipo que se sustituye por un tipo real al crear un objeto de la clase

        GenericClass<Integer> genInteger;//Se sustituye T por Integer

        GenericClass<Double> genDouble;//Se sustituye T por Double

        GenericClass<String> genString;//Se sustituye T por String

        GenericClass<Vehicle> genVehicle;//Se sustituye T por Vehicle

        genInteger = new GenericClass<Integer>(80);

        genDouble = new GenericClass<Double>(78.6);

        genString = new GenericClass<String>("Clases genéricas");

        genVehicle = new GenericClass<Vehicle>(new Vehicle(4, "azul"));

        genInteger.show();

        genDouble.show();

        genString.show();

        genVehicle.show();

    }

    public static void main(String[] args) {

        new MainGenericClass().show();

    }

}
```

Salida por consola:

```text
El tipo de T es Integer  --->  Valor del atributo: 80

El tipo de T es Double  --->  Valor del atributo: 78.6

El tipo de T es String  --->  Valor del atributo: Clases genéricas

El tipo de T es Vehicle  --->  Valor del atributo: Vehicle [wheelCount=4, speed=0.0, colour=azul]
```

Podemos observar que la clase tiene un atributo de tipo `T`, pero no se permiten variables estáticas de tipo `T`.

Una de las ventajas del uso de genéricos es que el compilador realiza comprobaciones de tipos y no permite asignar a un objeto la referencia de otro con distinta traducción del tipo de genérico:

genInteger = genDouble;//Error de compilación

El compilador informa con el siguiente mensaje de error: No puede convertir de `GenericClass<Double>` a `GenericClass<Integer>`. Si ambos hubieran sido del mismo tipo, sí se podría haber realizado la asignación.

A partir de Java 7, cuando instanciamos un objeto de una clase genérica, no es necesario especificar el tipo con el que queremos trabajar siempre y cuando el compilador pueda inferirlo (adivinarlo) a partir del contexto. Por lo tanto, el siguiente código:

genInteger = new GenericClass<Integer>(80);

genDouble = new GenericClass<Double>(78.6);

genString = new GenericClass<String>("Clases genéricas");

genVehicle = new GenericClass<Vehicle>(new Vehicle(4, "azul"));

también se puede realizar de la siguiente manera:

genInteger = new GenericClass<>(80);/*Como la variable a la que se asigna es GenericClass<Integer> es capaz de inferir que queremos crear un GenericClass<Integer> al hacer el new */

genDouble = new GenericClass<>(78.6);

genString = new GenericClass<>("Clases genéricas");

genVehicle = new GenericClass<>(new Vehicle(4, "azul"));

A esto se le conoce como **operador diamante**, dado que al quitar el tipo de la instanciación nos queda `<>` (que presenta una forma de diamante).

---

## 3. Métodos genéricos

Los métodos de una clase genérica pueden usar el parámetro del tipo de una clase y por tanto son genéricos de forma automática. Sin embargo, también podemos declarar métodos genéricos dentro de clases no genéricas, tanto estáticos como dinámicos, que reciban uno o más parámetros genéricos.

Los genéricos en un método se declaran en la firma del método delante del tipo de devolución.

Veamos un ejemplo de un método genérico:

```java
package tema11_Genericos;

public class GenericMethod {

    public <T> String showType(T parameter) {//El genérico <T> se declara delante del tipo de devolución String

        return parameter.getClass().getSimpleName();

    }

    public void show() {

        System.out.printf("El tipo del parámetro es %s\n", showType(80));

        System.out.printf("El tipo del parámetro es %s\n", showType(78.6));

        System.out.printf("El tipo del parámetro es %s\n", showType("Métodos genéricos"));

        System.out.printf("El tipo del parámetro es %s\n", showType(new Vehicle(4, "azul")));

    }

    public static void main(String[] args) {

        new GenericMethod().show();

    }

}
```

Salida por consola:

El tipo del parámetro es Integer

El tipo del parámetro es Double

El tipo del parámetro es String

El tipo del parámetro es Vehicle

---

## 4. Interfaces genéricas

Las interfaces también pueden contener parámetros de tipo, denominándose interfaces genéricas. Las clases que implementan la interfaz, tienen dos posibilidades:

- Implementar la interface traduciendo el genérico por un tipo concreto.
    
- Implementar la interface de manera genérica convirtiéndose en una clase genérica.
    

Veamos ejemplos de ambos casos:

Ejemplo de implementación de la interface traduciendo el genérico por un tipo concreto:

```java
package tema11_Genericos;

public interface GenericInterface<T> {

    T first(T[] array);

    T last(T[] array);

}
```

```java
package tema11_Genericos;

public class MyClass implements GenericInterface<Vehicle> {

    @Override

    public Vehicle first(Vehicle[] array) {

        return array[0];

    }

    @Override

    public Vehicle last(Vehicle[] array) {

        return array[array.length - 1];

    }

    public void show() {

        MyClass myClass = new MyClass();

        Vehicle[] array = new Vehicle[3];

        array[0] = new Vehicle(4, "azul");

        array[1] = new Vehicle(4, "blanco");

        array[2] = new Vehicle(2, "rojo");

        System.out.printf("Primer vehículo del array: %s\n", myClass.first(array));

        System.out.printf("Último vehículo del array: %s", myClass.last(array));

    }

    public static void main(String[] args) {

        new MyClass().show();

    }

}
```

Salida por consola:

```text
Primer vehículo del array: Vehicle [wheelCount=4, speed=0.0, colour=azul]

Último vehículo del array: Vehicle [wheelCount=2, speed=0.0, colour=rojo]
```

Ejemplo de implementación de la interface de manera genérica convirtiéndose en una clase genérica:

```java
package tema11_Genericos;

public class GenericClass2<T> implements GenericInterface<T> {

    @Override

    public T first(T[] array) {

        return array[0];

    }

    @Override

    public T last(T[] array) {

        return array[array.length - 1];

    }

}
```

```java
package tema11_Genericos;

public class MainGenericClass2 {

    public void show() {

        Vehicle[] array = new Vehicle[3];

        array[0] = new Vehicle(4, "azul");

        array[1] = new Vehicle(4, "blanco");

        array[2] = new Vehicle(2, "rojo");

        GenericClass2<Vehicle> genVehicle = new GenericClass2<>();

        System.out.printf("Primer vehículo del array: %s\n", genVehicle.first(array));

        System.out.printf("Último vehículo del array: %s", genVehicle.last(array));

    }

    public static void main(String[] args) {

        new MainGenericClass2().show();

    }

}
```

Salida por consola:

```text
Primer vehículo del array: Vehicle [wheelCount=4, speed=0.0, colour=azul]

Último vehículo del array: Vehicle [wheelCount=2, speed=0.0, colour=rojo]
```

---

## 5. Uso de varios genéricos

Se pueden utilizar varios genéricos indicándolos separados por comas dentro del operador diamante.

```java
package tema11_Genericos;

public class GenericClass3<T, V> {

    private T attribute1;

    private V attribute2;

    public GenericClass3(T attribute1, V attribute2) {

        this.attribute1 = attribute1;

        this.attribute2 = attribute2;

    }

    public T getAttribute1() {

        return attribute1;

    }

    public V getAttribute2() {

        return attribute2;

    }

    public void showAttributes() {

        System.out.printf("El tipo de T es %s", attribute1.getClass().getSimpleName());

        System.out.printf("  --->  Valor del atributo: %s\n", getAttribute1());

        System.out.printf("El tipo de V es %s", attribute2.getClass().getSimpleName());

        System.out.printf("  --->  Valor del atributo: %s\n\n", getAttribute2());

    }

}
```

```java
package tema11_Genericos;

public class MainGenericClass3 {

    public void show() {

        GenericClass3<Integer, Integer> variousGenerics1 = new GenericClass3<>(80, 56);

        GenericClass3<Integer, Double> variousGenerics2 = new GenericClass3<>(5, 78.6);

        GenericClass3<String, Vehicle> variousGenerics3 = new GenericClass3<>("Clases genéricas",

                new Vehicle(4, "azul"));

        variousGenerics1.showAttributes();

        variousGenerics2.showAttributes();

        variousGenerics3.showAttributes();

    }

    public static void main(String[] args) {

        new MainGenericClass3().show();

    }

}
```

Salida por consola:

```text
El tipo de T es Integer  --->  Valor del atributo: 80

El tipo de V es Integer  --->  Valor del atributo: 56

El tipo de T es Integer  --->  Valor del atributo: 5

El tipo de V es Double  --->  Valor del atributo: 78.6

El tipo de T es String  --->  Valor del atributo: Clases genéricas

El tipo de V es Vehicle  --->  Valor del atributo: Vehicle [wheelCount=4, speed=0.0, colour=azul]
```

El uso de genéricos puede crear situaciones de ambigüedad, sobretodo en casos de sobrecarga de métodos:

class Gen<T, V> {

    /* Estos dos métodos se sobrecargan pero dado que T y V pueden 

       ser del mismo tipo, se generarían dos métodos iguales por 

       lo que el compilador genera un error y este código no compila */

    void method(T ob) {}

    void method(V ob) {}

}

---

## 6. Tipos vinculados (o limitados)

Java ofrece los tipos vinculados que permiten, al especificar un parámetro de tipo, crear un vínculo superior que declare la superclase de la que deben derivarse todos los argumentos de tipo. Para ello usamos la cláusula _extends_ al especificar los parámetros de tipo: `<T extends superclass>`. Esto especifica que `T` solo se puede reemplazar por _superclass_ o por subclases de _superclass_.

La cláusula _extends_ también puede referirse a interfaces: `<T extends interface>`. En este caso, `T` solo se puede reemplazar por una clase que implemente dicha interfaz.

Los tipos numéricos heredan de la clase abstracta _Number_, por lo tanto, podemos limitar los parámetros de tipo a únicamente tipos numéricos: `<T extends Number>`. Esto nos permitiría utilizar métodos de la clase _Number_:

```java
package tema11_Genericos;

public class GenNumeric<T extends Number> { //Limitamos T a tipos numéricos

    private T attribute;

    public GenNumeric(T attribute) {

        this.attribute = attribute;

    }

    public T getAttribute() {

        return attribute;

    }

    double fraction() {

        return attribute.doubleValue() - attribute.intValue(); //Se pueden emplear métodos de la clase Number

    }

}
```

```java
package tema11_Genericos;

public class MainGenNumeric {

    public void show() {

        GenNumeric<Integer> genInteger;

        GenNumeric<Double> genDouble;

        genInteger = new GenNumeric<Integer>(80);

        genDouble = new GenNumeric<Double>(78.63);

        System.out.printf("La parte decimal de %s es %.2f\n", genInteger.getAttribute(), genInteger.fraction());

        System.out.printf("La parte decimal de %s es %.2f\n", genDouble.getAttribute(), genDouble.fraction());

    }

    public static void main(String[] args) {

        new MainGenNumeric().show();

    }

}
```

Salida por consola:

```text
La parte decimal de 80 es 0,00

La parte decimal de 78.63 es 0,63
```

Si intentamos utilizar una clase que no sea descendiente de _Number_, nos da un error de compilación:

GenNumeric<String> genString; //Error de compilación

Los tipos vinculados resultan especialmente útiles para garantizar que un parámetro sea compatible con otro:

class Pair<T, V extends T> { //V debe tener el mismo tipo que T o ser una subclase de T

    ....

}

V debe tener el mismo tipo que T o ser una subclase de T. Veamos ejemplos a la hora de crear objetos de la clase _Pair_:

Pair<Integer, Integer> pair1 = new Pair<Integer, Integer>();//Correcto

Pair<Number, Integer> pair2 = new Pair<Number, Integer>();//Correcto, Integer es una subclase de Number

Pair<Integer, String> pair3 = new Pair<Integer, String>(); //Incorrecto, String no es una subclase de Integer

---

## 7. Tipos comodín

El signo de interrogación `?` se conoce como comodín (wildcard) y representa un tipo desconocido. Tiene varios usos, uno de ellos es que es necesario utilizarlo cuando mezclamos objetos de la misma clase pero con distinta traducción del genérico. Veremos más usos de los tipos comodín en el _[Tema 12. Colecciones](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/3/12%20Colecciones.html)_.

Veamos un ejemplo sin tipo comodín para ver dónde nos podría hacer falta:

```java
package tema11_Genericos;

import java.util.Arrays;

public class GenericClass4<T> {

    private T[] array;

    GenericClass4(T[] array) {

        this.array = array;

    }

    public void showArray() {

        System.out.println(Arrays.toString(array));

    }

    public boolean equalSize(GenericClass4<T> gen) {

        return array.length == gen.array.length;

    }

}
```

```java
package tema11_Genericos;

public class MainGenericClass4 {

    public void show() {

        Integer[] array1 = { 8, 7, 9 };

        Integer[] array2 = { 3, 5, 12 };

        GenericClass4<Integer> gen1 = new GenericClass4<>(array1);

        GenericClass4<Integer> gen2 = new GenericClass4<>(array2);

        gen1.showArray();

        gen2.showArray();

        System.out.printf("%s tienen el mismo tamaño", gen1.equalSize(gen2) ? "Sí" : "No");

    }

    public static void main(String[] args) {

        new MainGenericClass4().show();

    }

}
```

Salida por consola:

```text
[8, 7, 9]

[3, 5, 12]

Sí tienen el mismo tamaño
```

El método `equalSize` recibe un objeto por parámetro y devuelve si ambos objetos tienen el mismo tamaño del array. En este caso funciona porque tienen la misma traducción del genérico (Integer). Pero ¿y si le pasamos por ejemplo uno de Double?:

```java
package tema11_Genericos;

public class Main {

    public void show() {

        Integer[] array1 = { 8, 7, 9 };

        Double[] array2 = { 3.6, 5.4, 12.42 };

        GenericClass4<Integer> gen1 = new GenericClass4<>(array1);

        GenericClass4<Double> gen2 = new GenericClass4<>(array2);

        gen1.showArray();

        gen2.showArray();

        System.out.printf("%s tienen el mismo tamaño", gen1.equalSize(gen2) ? "Sí" : "No");

    }

    public static void main(String[] args) {

        new Main().show();

    }

}

Nos da un error de compilación porque en el objeto `gen1` se ha traducido el genérico por Integer y le estamos pasando como argumento `gen2` que se ha traducido por Double. Entonces, en este caso, como lo que queremos en el método `equalSize` es simplemente comparar el tamaño de dos arrays y no nos importa que los arrays sean de distinto tipo, lo que podemos hacer es utilizar el tipo comodín `?` en el parámetro de `equalSize` para indicar que nos tienen que pasar un objeto de un tipo pero que no tiene por qué necesariamente coincidir con `T`:
```

```java
package tema11_Genericos;

import java.util.Arrays;

public class GenericClass5<T> {

    private T[] array;

    GenericClass5(T[] array) {

        this.array = array;

    }

    public void showArray() {

        System.out.println(Arrays.toString(array));

    }

    public boolean equalSize(GenericClass5<?> gen) {//Tipo comodín

        return array.length == gen.array.length;

    }

}
```

```java
package tema11_Genericos;

public class MainGenericClass5 {

    public void show() {

        Integer[] array1 = { 8, 7, 9 };

        Double[] array2 = { 3.6, 5.4, 12.42 };

        GenericClass5<Integer> gen1 = new GenericClass5<>(array1);

        GenericClass5<Double> gen2 = new GenericClass5<>(array2);

        gen1.showArray();

        gen2.showArray();

        System.out.printf("%s tienen el mismo tamaño", gen1.equalSize(gen2) ? "Sí" : "No");

    }

    public static void main(String[] args) {

        new MainGenericClass5().show();

    }

}
```

Salida por consola:

```text
[8, 7, 9]

[3.6, 5.4, 12.42]

Sí tienen el mismo tamaño
```

## Esquema resumen de conceptos clave

| Concepto | Idea principal |
| --- | --- |
| Parámetro de tipo | Permite definir clases, métodos e interfaces reutilizables con tipos distintos. |
| Comprobación de tipos | El compilador verifica compatibilidad y evita casts innecesarios. |
| Método genérico | Declara parámetros de tipo propios en la firma del método. |
| Tipo vinculado | Restringe el parámetro con `extends` a una clase o interfaz compatible. |
| Comodín `?` | Representa un tipo desconocido; `extends` y `super` restringen su uso. |

## Relaciones

- [[Programación orientada a objetos]] — clases, métodos, interfaces y tipos.
- [[Herencia]] — límites genéricos como `<T extends Number>` usan jerarquías de tipos.
- [[DAM/Programación basica/Tema 12/Colecciones]] — colecciones de Java se apoyan ampliamente en tipos genéricos.

## Para repasar

- [ ] Declarar y crear clases genéricas con uno o varios parámetros de tipo.
- [ ] Reconocer operador diamante y comprobar seguridad de tipos.
- [ ] Declarar métodos genéricos e interfaces genéricas.
- [ ] Usar tipos vinculados y entender sus restricciones.
- [ ] Diferenciar `? extends T` y `? super T` en parámetros y colecciones.
