**Proyecto:  
Analizador de textos distribuido**  
  
  
Crear  
una aplicación Java multiproceso que consiste en dos partes:  
  
1.  
**MainAnalyzer.java**:  
Una aplicación que lanza y gestiona dos procesos "contadores".  
  
2.  
**CharacterCounter.java**:  
Una aplicación "trabajadora" que cuenta o vocales o  
consonantes, según se le indique.  
  
En  
nuestro proyecto, el MainAnalyzer debe lanzar dos instancias del  
CharacterCounter, pasarles un texto línea a línea para que lo  
procesen simultáneamente, y recoger los resultados finales de ambos.  
  
  
  
  
  
  
**Parte  
1: CharacterCounter.java**

- Debe esperar recibir exactamente un argumento de línea de comandos: una  
       cadena que será "vowels" o "consonants".
- Si no recibe un argumento, o el argumento no es "vowels" ni "consonants", debe escribir el mensaje de error "Error:  
       Invalid mode" en la salida de error y finalizar indicando que  
       se ha producido un error con el valor 1.
- Debe comprobar si existe una variable de entorno llamada `DEBUG_MODE`.
- Debe leer línea a línea el texto de su entrada estándar en un bucle. Por cada línea recibida contará el número de vocales o consonantes en esa línea (según el argumento recibido por la línea de comandos).
- Si la variable de entorno DEBUG_MODE tiene el valor TRUE, deberá imprimir un mensaje de depuración a su salida de error por cada línea procesada (ej. “[PID: 12345] Line parsed. Found n vocals”, donde 12345 es el pid del proceso, n es el número de vocales contadas). Si fuera un contador de consonantes mostraría el mismo mensaje pero indicando las consonantes encontradas.   
- Cuando ya no tenga más líneas que leer, deberá debe escribir una sola línea en su salida estándar con el resultado final (ej. "Total  
       vowels: 581") y finalizar indicando que se ha finalizado correctamente.

**Parte  
2: MainAnalyzer.java**

- Debe definir una lista de cadenas que simule el contenga el texto a analizar.
- Debe estar preparado para lanzar la clase CharacterCounter. La construcción del comando debe ser portable: debe obtener la ruta al ejecutable `java` usando la propiedad "java.home", y el classpath actual usando la propiedad "java.class.path".
- Debe configurar un `ProcessBuilder` para el contador de vocales, de manera que la salida de error del contador sea el mismo que el de MainAnalyzer, y el modo de depuración esté activo (DEBUG_MODE sea  
       TRUE)   
- Debe configurar un segundo `ProcessBuilder` para el contador de consonantes, establecido para él el directorio de trabajo "./logs". Los errores que se produzcan en el contador de consontantes se redireccionarán al archivo “./logs.consonant_err.log” del  
       directorio de trabajo.
- Iniciará la ejecución del contador de vocales y del contador de consonantes.
- Una vez iniciada la ejecución deberá mostrar por consola en su salida estándar los PIDs de ambos subprocesos.
- Después deberá enviar al contador de vocales y al contador de consonantes, cadena a cadena (cada una como una línea), la lista de frases creada inicialmente.
- Una vez enviadas todas las líneas, deberá cerrar la comunicación con ambos contadores, para que éstos dejen de procesar líneas.
- Después leerá la línea de resultado producida por el contador de vocales y la almacenará en una cadena.
- También hará lo mismo con la línea de resultado producida por el contador de consonantes.
- Cuando tanto el contador de vocales como el contador de consonantes hayan finalizado su ejecución, deberá obtener el valor de salida de ambos procesos.
- Finalmente deberá imprimir los resultados "Vowel Result: Total vowels:  
       581" y "Consonant Result: Total consonants: 1204"), e  
       informar si ambos procesos terminaron con éxito o si alguno falló.