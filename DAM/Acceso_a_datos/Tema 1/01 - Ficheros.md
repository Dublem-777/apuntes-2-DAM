---
asignatura: AD
tema: 1
tipo: tema
estado: en curso
fecha: 2026-09-17
tags:
  - DAM/tema
  - DAM/acceso-a-datos/ficheros
---

# 1 · Ficheros

> [!info] Asignatura
> [[DAM/Acceso_a_datos/Indice|Acceso a Datos]] · Tema 1 · por ahora dados 1–5

## Índice del tema

- [[#1. Introducción]] ✅
- [[#2. La interfaz Path]] ✅
- [[#3. La clase Files]] ✅
- [[#4. El método move]] ✅
	- [[#4.1 Mover un archivo a otro directorio]] ✅
	- [[#4.2 Renombrar un archivo]] ✅
	- [[#4.3 Mover y renombrar al mismo tiempo un fichero]] ✅
	- [[#4.4 Sobrescribir un archivo existente]] ✅
	- [[#4.5 Mover un directorio completo]] ✅
	- [[#4.6 Renombrar un directorio]] ✅
	- [[#4.7 Mover y renombrar al mismo tiempo un directorio]] ✅
- [[#5. Listar elementos de un directorio]] ✅
- [[#6. Flujos]]
- [[#7. Ficheros de texto]]
	- [[#7.1 Método Files.readAllLines]]
	- [[#7.2 Método Files.writeString]]
	- [[#7.3 Método Files.write]]
	- [[#7.4 Clases BufferedReader y BufferedWriter]]
	- [[#7.5 Operaciones con arrays y desplazamientos]]
		- [[#7.5.1 Lectura]]
		- [[#7.5.2 Escritura]]
- [[#8. Método flush]]
- [[#9. Ficheros binarios]]
	- [[#9.1 FileInputStream y FileOutputStream]]
	- [[#9.2 DataInputStream y DataOutputStream]]
	- [[#9.3 ObjectInputStream y ObjectOutputStream]]
- [[#10. Ficheros de acceso aleatorio]]
- [[#11. Ficheros XML y JSON]]
	- [[#11.1 Ficheros XML]]
	- [[#11.2 Ficheros JSON]]
	- [[#11.3 Biblioteca Jackson]]
- [[#Esquema]]
- [[#Relaciones]]
- [[#Para repasar]]

---

## 1. Introducción

### 1.1 ¿Qué es un fichero?

Un **fichero o archivo** es un conjunto de datos o información almacenada en un dispositivo de almacenamiento, como un disco duro, pen drive, etc. Los ficheros pueden contener diversos tipos de datos: texto, imágenes, audio o vídeo.

Cada fichero tiene un **nombre** y una **extensión** que indica su tipo (por ejemplo, `.txt` para archivos de texto o `.jpg` para imágenes). Los sistemas operativos permiten organizar, gestionar y acceder a estos ficheros mediante **sistemas de archivos**, que estructuran y facilitan el almacenamiento y la recuperación de la información.

### 1.2 La API java.nio.file

Se introdujo en **Java 7** para mejorar la gestión de archivos y sistemas de archivos. Incluye tres piezas fundamentales:

| Pieza | Tipo | Qué hace |
| --- | --- | --- |
| `Path` | interfaz | Representa una ruta en el sistema de archivos. Puede referirse tanto a archivos como a directorios. |
| `Paths` | clase | Proporciona métodos estáticos para **obtener** objetos `Path`. |
| `Files` | clase | Proporciona métodos estáticos para **trabajar con archivos** (crear, copiar, leer, borrar…). |

> [!tip] Idea clave
> `Paths` fabrica la ruta → `Path` es la ruta → `Files` opera sobre ella.

### 1.3 Excepciones

Muchas operaciones lanzan excepciones en caso de error, por lo que es importante gestionar adecuadamente estas situaciones:

| Excepción | Cuándo se lanza |
| --- | --- |
| `IOException` | Excepción general: problema con las operaciones de E/S. |
| `NoSuchFileException` | El archivo o directorio no existe. |
| `FileAlreadyExistsException` | Se intenta crear un archivo o directorio que ya existe. |

> [!note] Orden de captura
> `NoSuchFileException` y `FileAlreadyExistsException` heredan de `IOException`, así que se capturan **antes** en el bloque `try-catch` (de la más específica a la más genérica).

### 1.4 Sensibilidad a mayúsculas/minúsculas

Depende del sistema operativo y del sistema de archivos utilizado:

| Sistema Operativo | Sensibilidad por defecto |
| --- | --- |
| Windows | No sensible (Case-Insensitive) |
| Linux/Unix | Sensible (Case-Sensitive) |
| macOS | No sensible, pero configurable |

- **Windows**: no diferencia mayúsculas de minúsculas. `archivo.txt` y `ARCHIVO.txt` se tratan como el **mismo** archivo.
- **Linux/Unix**: sí diferencia. `archivo.txt` es **distinto** de `ARCHIVO.txt`.

---

## 2. La interfaz Path

La interfaz `Path` representa la **ubicación** de un archivo o directorio en el sistema de archivos. Admite dos tipos de ruta:

- **Ruta relativa**: proporciona la ubicación **desde el directorio actual** de la aplicación.
- **Ruta absoluta**: proporciona la ubicación **completa desde la raíz** del sistema de archivos.

### 2.1 El separador de directorios

El separador es diferente según el sistema operativo:

- **Windows**: barra invertida `\`
- **Unix/Linux/Mac**: barra normal `/`

Java proporciona una manera de obtener el separador del sistema con `FileSystems.getDefault().getSeparator()`, devolviendo la barra adecuada según el SO:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.FileSystems;

public class Separator {

    public void show() {

        String separator = FileSystems.getDefault().getSeparator();
        String path = String.format("%2$s%1$s%3$s%1$s%4$s%1$s", separator, "home", "ies-saladillo", "directorio");
        System.out.println(path);

    }

    public static void main(String[] args) {

        new Separator().show();

    }

}
```

Salida por consola:

```
home/ies-saladillo/directorio/
```

> [!note] Este método solo construye un `String`: texto con forma de ruta, no un objeto `Path` que se pueda usar con la clase `Files`.

### 2.2 Crear un objeto Path: Paths.get()

Para crear un objeto `Path` se utiliza la clase `Paths` con el siguiente método:

```java
public static Path get(String first, String... more)
```

Convierte una cadena o una secuencia de cadenas en una ruta. Los parámetros pueden ser rutas relativas, absolutas o combinadas.

> [!note] A diferencia del 2.1, aquí el resultado es un objeto `Path` real: Java une las partes con el separador del SO y se puede operar con él (`Files`, `resolve()`, `getFileName()`…).

#### Rutas relativas

Se interpretan **en relación con el directorio de trabajo actual** de la aplicación:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class RelativePath {

    public void show() {

        Path file = Paths.get("directorio", "archivo.txt");
        Path file2 = Paths.get("directorio2/archivo2.txt");
        System.out.println(file);
        System.out.println(file2);

    }

    public static void main(String[] args) {

        new RelativePath().show();

    }

}
```

Salida por consola:

```
directorio/archivo.txt
directorio2/archivo2.txt
```

#### Rutas absolutas

Se interpretan como absolutas **independientemente del directorio de trabajo actual**:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class AbsolutePath {

    public void show() {

        //Unix/Linux/Mac
        Path absolutePath = Paths.get("/home/usuario/documentos/archivo.txt");
        System.out.printf("Ruta absoluta en Unix/Linux/Mac: %s\n", absolutePath);
        //Windows
        absolutePath = Paths.get("C:\\Usuarios\\ies-saladillo\\directorio\\archivo.txt");
        System.out.printf("Ruta absoluta en Windows: %s", absolutePath);

    }

    public static void main(String[] args) {

        new AbsolutePath().show();

    }

}
```

Salida por consola:

```
Ruta absoluta en Unix/Linux/Mac: /home/usuario/documentos/archivo.txt
Ruta absoluta en Windows: C:\Usuarios\ies-saladillo\directorio\archivo.txt
```

#### Combinando rutas: resolve()

Con el método `resolve` de `Path` se combinan una base + una relativa. Útil para crear rutas basadas en un directorio de base:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class Combined {

    public void show() {

        Path base = Paths.get("/home/usuario");
        Path file = base.resolve("directorio/archivo.txt");
        System.out.printf("Ruta combinada: %s", file);

    }

    public static void main(String[] args) {

        new Combined().show();

    }

}
```

Salida por consola:

```
Ruta combinada: /home/usuario/directorio/archivo.txt
```

### 2.3 Rutas independientes del SO

Con `Paths` + `Path` del paquete `java.nio.file` se pueden crear rutas de manera **independiente del sistema operativo**:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class PathsPath {

    public void show() {

        Path directory = Paths.get("home", "ies-saladillo", "directorio");
        Path file = Paths.get("home", "ies-saladillo", "directorio", "archivo.txt");
        System.out.println(directory);
        System.out.println(file);

    }

    public static void main(String[] args) {

        new PathsPath().show();

    }

}
```

Salida por consola:

```
home/ies-saladillo/directorio
home/ies-saladillo/directorio/archivo.txt
```

El método `get` se encarga de unir las partes de la ruta de forma adecuada para cada SO.

### 2.4 Obtener la ruta absoluta: toAbsolutePath()

Si necesitas la ruta absoluta de un archivo, la obtienes de un objeto `Path` con `toAbsolutePath()`:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class ToAbsolutePath {

    public void show() {

        Path file = Paths.get("directorio", "archivo.txt");
        Path absolutePath = file.toAbsolutePath();
        System.out.println(absolutePath);

    }

    public static void main(String[] args) {

        new ToAbsolutePath().show();

    }

}
```

Salida por consola:

```
/home/ies-saladillo/eclipse-workspace/FilesCode/directorio/archivo.txt
```

### 2.5 Rutas absolutas manuales según el SO

Si se necesita definir rutas absolutas manualmente, se puede verificar el sistema operativo con `System.getProperty("os.name")` para ajustar la ruta según sus convenciones:

```java
package tema1_Ficheros_interfazPath;

public class AdjustPath {

    public void show() {

        String os = System.getProperty("os.name").toLowerCase();
        String rutaAbsoluta;

        if (os.contains("win")) {
            rutaAbsoluta = "C:\\Usuarios\\ies-saladillo\\directorio\\archivo.txt";
        } else {
            rutaAbsoluta = "/home/ies-saladillo/directorio/archivo.txt";
        }
        System.out.printf("Ruta absoluta: %s", rutaAbsoluta);

    }

    public static void main(String[] args) {

        new AdjustPath().show();

    }

}
```

Salida por consola:

```
Ruta absoluta: /home/ies-saladillo/directorio/archivo.txt
```

### 2.6 El directorio actual

Para obtener en un `Path` el directorio actual se utiliza un `.`:

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class CurrentDirectoryPath {

    public void show() {

        Path currentDirectory = Paths.get("."); //El punto representa el directorio actual
        System.out.println(currentDirectory.toAbsolutePath());

    }

    public static void main(String[] args) {

        new CurrentDirectoryPath().show();

    }

}
```

Otra manera de obtener el directorio actual **en una cadena**, con la propiedad del sistema `user.dir`:

```java
package tema1_Ficheros_interfazPath;

public class CurrentDirectory {

    public void show() {

        String currentDir = System.getProperty("user.dir");
        System.out.printf("Directorio actual: %s", currentDir);

    }

    public static void main(String[] args) {

        new CurrentDirectory().show();

    }

}
```

Salida por consola:

```
Directorio actual: /home/ies-saladillo/eclipse-workspace/FilesCode
```

### 2.7 Otros métodos comunes de Path

| Método | Qué devuelve |
| --- | --- |
| `Path getFileName()` | El nombre del archivo o directorio (último elemento de la ruta). |
| `Path getParent()` | El directorio padre de la ruta. |
| `boolean isAbsolute()` | Si la ruta es absoluta o no. |

```java
package tema1_Ficheros_interfazPath;

import java.nio.file.Path;
import java.nio.file.Paths;

public class OtherMethods {

    public void show() {

        Path file = Paths.get("directorio", "archivo.txt");
        System.out.println(file.getFileName());
        System.out.println(file.getParent());
        System.out.println(file.isAbsolute());

    }

    public static void main(String[] args) {

        new OtherMethods().show();

    }

}
```

Salida por consola:

```
archivo.txt
directorio
false
```

---

## 3. La clase Files

La clase `Files` proporciona **métodos estáticos** para realizar operaciones sobre archivos y directorios: lectura, escritura, creación, eliminación, etc. Los más comunes:

| Método | Qué hace |
| --- | --- |
| `exists` | Comprueba si existe. Antes de trabajar con un archivo o directorio, es recomendable verificarlo. |
| `createFile` | Crea un archivo. |
| `createDirectory` | Crea un directorio. |
| `copy` | Copia un archivo. ⚠️ Si es una carpeta, se crea una carpeta vacía en el destino, **sin copiar los archivos que contiene**. |
| `move` | Mueve o renombra un archivo o directorio. |
| `delete` | Elimina un archivo o un directorio. El directorio tiene que estar **vacío**; si no, lanza `DirectoryNotEmptyException`. |
| `size` | Tamaño del archivo. |
| `isDirectory` | Si es un directorio. |
| `isRegularFile` | Si es un fichero regular (ni directorio ni enlace simbólico). |
| `isReadable` | Si se puede leer. |
| `isWritable` | Si se puede escribir. |
| `isExecutable` | Si es ejecutable. |

> [!warning] copy vs. move con directorios
> `Files.copy()` sobre un directorio **no copia su contenido** (crea el directorio vacío). `Files.delete()` sobre un directorio **no borrado vacío** lanza excepción.

Ejemplo completo (creación, comprobaciones, copia y borrado):

```java
package tema1_Ficheros_claseFiles;

import java.io.IOException;
import java.nio.file.*;

public class FilesClass {

    public void show() {

        Path file, fileCopy, directory;
        try {
            file = Paths.get("files", "file.txt");
            System.out.println(file);
            System.out.printf("El fichero %s existe\n", Files.exists(file) ? "sí" : "no");
            Files.createFile(file);
            System.out.printf("El fichero %s existe\n", Files.exists(file) ? "sí" : "no");
            System.out.printf("Tamaño del archivo: %d\n", Files.size(file));
            System.out.printf("¿Se puede leer?: %s\n", Files.isReadable(file) ? "sí" : "no");
            System.out.printf("¿Se puede escribir?: %s\n", Files.isWritable(file) ? "sí" : "no");
            System.out.printf("¿Es ejecutable?: %s\n", Files.isExecutable(file) ? "sí" : "no");
            System.out.printf("¿Es un fichero?: %s\n", Files.isRegularFile(file) ? "sí" : "no");
            directory = Paths.get("directory");
            Files.createDirectory(directory);
            System.out.printf("¿Es un directorio?: %s\n", Files.isDirectory(directory) ? "sí" : "no");
            fileCopy = Paths.get("files", "fileCopy.txt");
            Files.copy(file, fileCopy);
            Files.delete(file);
            Files.delete(fileCopy);
            Files.delete(directory);
        } catch (FileAlreadyExistsException e) {
            System.err.printf("El fichero ya existe: %s", e.getMessage());
        } catch (NoSuchFileException e) {
            System.err.printf("El fichero no existe: %s", e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }

    }

    public static void main(String[] args) {

        new FilesClass().show();

    }

}
```

Salida por consola:

```
files/file.txt
El fichero no existe
El fichero sí existe
Tamaño del archivo: 0
¿Se puede leer?: sí
¿Se puede escribir?: sí
¿Es ejecutable?: no
¿Es un fichero?: sí
¿Es un directorio?: sí
```

---

## 4. El método move

`Files.move(source, target, opciones...)` sirve **tanto para mover como para renombrar**: si las dos rutas están en el mismo directorio, el efecto es renombrar. Por defecto lanza excepción si el destino ya existe (se soluciona con `StandardCopyOption.REPLACE_EXISTING`, ver 4.4).

Los 7 casos son variaciones del mismo patrón: crear origen → `Files.move` → borrar al final.

### 4.1 Mover un archivo a otro directorio

Origen y destino en directorios distintos, mismo nombre:

```java
package tema1_Ficheros_metodoMove;

import java.io.IOException;
import java.nio.file.*;

public class MoveFile {

    public void show() {

        Path source, destination;
        try {
            source = Paths.get("file.txt");
            System.out.printf("Fichero origen: %s\n", source.toAbsolutePath());
            Files.createFile(source);
            destination = Paths.get("files", "file.txt");
            Files.move(source, destination);
            System.out.printf("Fichero movido con éxito a: %s", destination.toAbsolutePath());
            Files.delete(destination);
        } catch (FileAlreadyExistsException e) {
            System.err.printf("El fichero ya existe: %s", e.getMessage());
        } catch (NoSuchFileException e) {
            System.err.printf("El fichero no existe: %s", e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error al mover el archivo: %s", e.getMessage());
        }

    }

    public static void main(String[] args) {

        new MoveFile().show();

    }

}
```

Salida por consola:

```
Fichero origen: /home/ies-saladillo/eclipse-workspace/FilesCode/file.txt
Archivo movido con éxito a: /home/ies-saladillo/eclipse-workspace/FilesCode/files/file.txt
```

### 4.2 Renombrar un archivo

Mismo directorio, distinto nombre → efecto de renombrado:

```java
source = Paths.get("files", "file.txt");
Files.createFile(source);
newName = Paths.get("files", "renamedFile.txt");
Files.move(source, newName);
```

Salida por consola:

```
Fichero origen: /home/ies-saladillo/eclipse-workspace/FilesCode/files/file.txt
Archivo renombrado con éxito como: /home/ies-saladillo/eclipse-workspace/FilesCode/files/renamedFile.txt
```

### 4.3 Mover y renombrar al mismo tiempo un fichero

Directorio distinto **y** nombre distinto en una sola operación:

```java
source = Paths.get("file.txt");
Files.createFile(source);
destination = Paths.get("files", "renamedFile.txt");
Files.move(source, destination);
```

Salida por consola:

```
Fichero origen: /home/ies-saladillo/eclipse-workspace/FilesCode/file.txt
Fichero movido y renombrado con éxito a: /home/ies-saladillo/eclipse-workspace/FilesCode/files/renamedFile.txt
```

### 4.4 Sobrescribir un archivo existente

Por defecto, `move` lanza una excepción si el archivo de destino ya existe. Para sobrescribirlo se usa la opción `StandardCopyOption.REPLACE_EXISTING`:

```java
source = Paths.get("file.txt");
Files.createFile(source);
destination = Paths.get("files", "file.txt");
Files.createFile(destination);   // ya existe → sin la opción, move fallaría
Files.move(source, destination, StandardCopyOption.REPLACE_EXISTING);
```

Salida por consola:

```
Fichero origen: /home/ies-saladillo/eclipse-workspace/FilesCode/file.txt
Fichero sobrescrito con éxito a: /home/ies-saladillo/eclipse-workspace/FilesCode/files/file.txt
```

### 4.5 Mover un directorio completo

También se puede mover un directorio completo incluyendo todos sus archivos y subdirectorios:

```java
source = Paths.get("directory");
Files.createDirectory(source);
destination = Paths.get("files", "directory");
Files.move(source, destination);
```

Salida por consola:

```
Directorio origen: /home/ies-saladillo/eclipse-workspace/FilesCode/directory
Directorio movido con éxito a: /home/ies-saladillo/eclipse-workspace/FilesCode/files/directory
```

### 4.6 Renombrar un directorio

```java
source = Paths.get("directory");
Files.createDirectory(source);
newName = Paths.get("renamedDirectory");
Files.move(source, newName);
```

Salida por consola:

```
Directorio: /home/ies-saladillo/eclipse-workspace/FilesCode/directory
Directorio renombrado con éxito como: /home/ies-saladillo/eclipse-workspace/FilesCode/renamedDirectory
```

### 4.7 Mover y renombrar al mismo tiempo un directorio

```java
source = Paths.get("directory");
Files.createDirectory(source);
destination = Paths.get("files", "renamedDirectory");
Files.move(source, destination);
```

Salida por consola:

```
Directorio: /home/ies-saladillo/eclipse-workspace/FilesCode/directory
Directorio movido y renombrado con éxito a: /home/ies-saladillo/eclipse-workspace/FilesCode/files/renamedDirectory
```

> [!tip] Resumen 4.1–4.7
> Una sola API (`Files.move`) cubre los 7 casos: lo único que cambia son las rutas de origen y destino. Mismo directorio = renombrar; distinto directorio = mover; ambas cosas a la vez = mover + renombrar. `REPLACE_EXISTING` para sobrescribir.

---

## 5. Listar elementos de un directorio

Java proporciona en la clase `Files` el método estático `Stream<Path> list(Path dir)`: devuelve un `Stream<Path>` donde cada `Path` es un archivo o subdirectorio del directorio dado.

### 5.1 try-with-resources

Cuando usamos `list`, el sistema "presta" recursos para acceder a esa información. Si no cerramos el `Stream`, estaríamos ocupando memoria o archivos innecesariamente y el sistema iría más lento.

Para ello está el **try-with-resources**: estructura que gestiona automáticamente recursos como archivos, conexiones de BD o streams. Cualquier recurso que implemente `AutoCloseable` (es decir, que sabe cerrarse a sí mismo) **se cierra automáticamente al finalizar el bloque `try`, incluso si ocurre una excepción**. Los recursos se declaran en los paréntesis del `try`:

```java
package tema1_Ficheros_listarElementosDirectorio;

import java.io.IOException;
import java.nio.file.*;
import java.util.stream.Stream;

public class FilesList {

    public void show() {

        Path directory = Paths.get(".");
        // Usamos try-with-resources para asegurar que el Stream se cierre automáticamente
        try (Stream<Path> directoryContents = Files.list(directory)) {
            directoryContents.forEach(content -> System.out.println(content.getFileName()));
        } catch (NotDirectoryException e) {
            System.err.printf("El directorio no existe: %s", e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error al mostrar el contenido del directorio: %s", e.getMessage());
        }

    }

    public static void main(String[] args) {

        new FilesList().show();

    }

}
```

Salida por consola:

```
.settings
bin
files
src
.project
.classpath
```

### 5.2 Files.walk — recorrido recursivo

`Files.walk(directory)` funciona como `list` pero **además es recursivo**: también recorre subdirectorios. Para recorrer todos los niveles de un directorio es el método adecuado:

```java
try (Stream<Path> directoryContents = Files.walk(directory)) {
    directoryContents.forEach(System.out::println);
}
```

> [!warning] NotDirectoryException
> Se captura cuando la ruta dada no es un directorio. Va **antes** que `IOException` en el `try-catch` (excepción específica antes que genérica).

---

## 6. Flujos

Un flujo (o stream) se refiere al proceso de transferencia secuencial de datos entre dos fuentes, como un programa y un fichero, una red, una consola, etc. Un flujo puede ser de entrada (lectura) o de salida (escritura), dependiendo de la dirección en la que se transfieren los datos.

Existen dos categorías principales de flujos en Java: de bytes y de caracteres.

| Tipo de flujo | Trabaja con | Se usa para | Lectura | Escritura |
| --- | --- | --- | --- | --- |
| **Flujos de bytes** | Datos binarios, en forma de bytes | Datos no textuales: imágenes, vídeos, ficheros binarios | `InputStream` | `OutputStream` |
| **Flujos de caracteres** | Datos textuales, caracteres de 16 bits (Unicode) | Leer y escribir texto | `Reader` | `Writer` |

> [!tip] Idea clave
> ¿Es texto? → `Reader`/`Writer` (apartados 7 y 8). ¿Es cualquier otra cosa? → `InputStream`/`OutputStream` (apartados 9 y 10).

---

## 7. Ficheros de texto

### 7.1 Método Files.readAllLines

La clase `Files` proporciona métodos para leer y escribir archivos de texto. Para leer, el método `readAllLines` lee todas las líneas de un fichero y las devuelve en una lista:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class ReadTextFiles {
    public void readTextFile() {
        List<String> lines;
        try {
            lines = Files.readAllLines(Paths.get("files","readFile.txt"));
            lines.forEach(System.out::println);
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new ReadTextFiles().readTextFile();
    }
}
```

Salida por consola:

```text
Estamos aprendiendo
a manejar ficheros
de texto en Java
```

Este método utiliza la codificación por defecto del sistema que dependerá de la configuración local del sistema operativo en el que se esté ejecutando el programa. Por ejemplo, en sistemas Windows la codificación por defecto suele ser `Windows-1252`, mientras que en sistemas basados en Unix/Linux, como macOS, normalmente será `UTF-8`. Esto puede causar problemas si no es la adecuada, por ejemplo, con caracteres especiales o con tilde.

Para asegurar que el archivo se lea con una codificación específica, como `UTF-8`, Java proporciona una sobrecarga del método que acepta un segundo parámetro, especificando explícitamente la codificación:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class ReadTextFilesUTF8 {
    public void readTextFileUTF8() {
        List<String> lines;
        try {
            lines = Files.readAllLines(Paths.get("files","readFile.txt"),StandardCharsets.UTF_8);
            lines.forEach(System.out::println);
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new ReadTextFilesUTF8().readTextFileUTF8();
    }
}
```

### 7.2 Método Files.writeString

Para escribir, Java proporciona el siguiente método estático en la clase `Files`:

```java
Path writeString(Path path, CharSequence csq, OpenOption... options)
```

Este método escribe una cadena de texto completa en el archivo especificado utilizando la codificación por defecto del sistema. Igual que con la lectura, está sobrecargado por si se quiere especificar explícitamente la codificación.

Parámetros:

- `path`: el archivo donde se escribirá.
- `csq`: la cadena de texto que se desea escribir expresada como un `CharSequence`. En el _Tema 3.1 Cadenas_ del temario de Programación se explica la [interfaz CharSequence](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/1/1.4%20Cadenas.html#charsequence).
- `options`: opciones adicionales para el manejo del archivo. Admite varias opciones ya que es un _varargs_. He aquí las más comunes:
    - `CREATE`: crea el archivo si no existe.
    - `CREATE_NEW`: crea un archivo nuevo, pero lanza una excepción si ya existe.
    - `APPEND`: añade el contenido al final del archivo.
    - `TRUNCATE_EXISTING`: sobrescribe el archivo si ya existe.

> [!warning] Opciones por defecto
> Por defecto, `writeString` utiliza las opciones `CREATE` y `TRUNCATE_EXISTING`, es decir, si el archivo no existe, lo crea, y si ya existe, sobrescribe su contenido. Pero si se utiliza alguna opción, éstas dos opciones dejan de estar por defecto, entonces hay que añadirlas expresamente. Por ejemplo, si queremos utilizar `APPEND` en un bucle y queremos que en la primera iteración, el archivo se cree si no existe, pues entonces tendremos que poner `CREATE` y `APPEND`:

```java
Files.writeString(path, string, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
```

Veamos un ejemplo de utilización del método `writeString`:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.List;

public class WriteString {
    public void show() {
        Path path=Paths.get("files","fileWriteString.txt");
        try {
            Files.writeString(path, "He escrito esta línea con writeString. ");
            Files.writeString(path, "Le he añadido esta frase con la opción APPEND.",StandardOpenOption.APPEND);
            readTextFile(path);
            Files.writeString(path, "He perdido lo anterior porque no he usado la opción APPEND.");
            readTextFile(path);
            Files.delete(path);
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }
    }

    public void readTextFile(Path path) {
        List<String> lines;
        try {
            lines = Files.readAllLines(path);
            lines.forEach(System.out::println);
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }
    }

    public static void main(String[] args) {
        new WriteString().show();
    }
}
```

Salida por consola:

```text
He escrito esta línea con writeString. Le he añadido esta frase con la opción APPEND.

He perdido lo anterior porque no he usado la opción APPEND.
```

### 7.3 Método Files.write

Java nos proporciona también otro método estático en la clase `Files` para poder escribir varias líneas de texto indicadas en una estructura de datos iterable, como listas o flujos de datos:

```java
Path write(Path path, Iterable<? extends CharSequence> lines,
        OpenOption... options)
```

La interfaz `Iterable` se explica en el _Tema 12 Colecciones_ en el apartado [iteradores](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/450134/mod_resource/content/1/12%20Colecciones.html#iteradores).

> [!warning] Opciones por defecto
> Tal y como ocurre con el método `writeString`, este método también utiliza las opciones `CREATE` y `TRUNCATE_EXISTING` por defecto, es decir, si el archivo no existe, lo crea, y si ya existe, sobrescribe su contenido. Igualmente, si se utiliza alguna opción, éstas dos opciones dejan de estar por defecto, entonces hay que añadirlas expresamente.

```java
package tema1_Ficheros_ficherosTexto;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class WriteStrings {
    public void show() {
        Path path=Paths.get("files","fileWriteStrings.txt");
        Iterable<String> lines = Arrays.asList("Primera línea", "Segunda línea", "Tercera línea");
        try {
            Files.write(path, lines);
            readTextFile(path);
            Files.delete(path);
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }
    }

    public void readTextFile(Path path) {
        List<String> lines;
        try {
            lines = Files.readAllLines(path);
            lines.forEach(System.out::println);
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }
    }

    public static void main(String[] args) {
        new WriteStrings().show();
    }
}
```

Salida por consola:

```text
Primera línea
Segunda línea
Tercera línea
```

### 7.4 Clases BufferedReader y BufferedWriter

> [!definition] Buffer
> Un buffer es un espacio temporal en memoria (generalmente en RAM) que se utiliza para almacenar datos antes de que sean leídos o escritos. Este espacio permite agrupar varias operaciones de lectura o escritura en una sola operación de I/O, lo que es más eficiente que realizar muchas operaciones pequeñas directamente en el disco o en un flujo de entrada/salida.

En otras palabras, en lugar de leer o escribir datos byte a byte o carácter a carácter, los datos se acumulan en un buffer hasta que el espacio está lleno (o hasta que se realiza una operación como cerrar el flujo), momento en el cual todos los datos se procesan de una sola vez.

El uso de un buffer mejora el rendimiento en las operaciones de entrada/salida por dos razones principales:

1. Minimiza el número de accesos al disco o al sistema de archivos:
    - Acceder directamente al disco es lento en comparación con acceder a la memoria RAM.
    - Sin un buffer, cada operación de lectura o escritura implicaría una llamada al sistema para acceder al disco, lo que es costoso en términos de tiempo.
    - Al usar un buffer, varias operaciones pequeñas se agrupan en una sola operación más grande, lo que reduce el número de veces que se interactúa con el disco.
2. Reduce el tiempo de espera:
    - Al realizar muchas operaciones pequeñas, el sistema tiene que esperar a que cada una se complete antes de continuar con la siguiente.
    - Con un buffer, se acumulan datos en memoria hasta que se llena el buffer o se requiere su vaciado, lo que permite que las operaciones I/O sean más eficientes y rápidas.

¿Cuándo no hace falta usar un buffer?:

- Lectura/escritura en tiempo real: al procesar datos en tiempo real, como leer o escribir desde una red o en aplicaciones donde la latencia es crítica, el uso de un buffer puede introducir un pequeño retraso, ya que los datos no se procesan hasta que el buffer se llena.
- Operaciones pequeñas: si solo se está realizando una o dos operaciones de lectura/escritura pequeñas, el uso de un buffer no aportará mucho y podría incluso ser innecesario.

En Java, las lecturas/escrituras con buffer se hacen con las clases `BufferedReader` y `BufferedWriter` de la API antigua (basada en `java.io`), las cuales siguen siendo ampliamente utilizadas en muchos proyectos y bibliotecas, ya que muchos sistemas y aplicaciones grandes aún utilizan la API basada en `java.io`. Existen ciertas situaciones en las que la API antigua sigue siendo útil, como al trabajar con flujos (`InputStream`, `OutputStream`) y manejar I/O no relacionado con archivos (como conexiones de red, sockets, o lectura de la consola).

La API moderna (`java.nio`) utiliza las clases `BufferedReader` y `BufferedWriter` de la API antigua, pero las inicializa con métodos estáticos de la clase `Files` de la API moderna: `newBufferedReader` y `newBufferedWriter`. Éste último tiene también como párametro `OpenOption... options` para las diferentes opciones de escritura (`CREATE`, `APPEND`, etc). Veamos un ejemplo donde se copia todo el contenido de un fichero origen en un fichero destino. Los métodos utilizados son:

- `readLine` de `BufferedReader`: devuelve una línea del fichero. La línea que se devuelve, no lleva el `\n`. Cuando ya no hay más líneas que leer, devuelve `null`.
- `write` de `BufferedWriter`: escribe la línea en el fichero.
- `newLine` de `BufferedWriter`: escribe un salto de línea en el fichero.

```java
package tema1_Ficheros_ficherosTexto;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class NewBufferedClasses {
    public void show() {
        Path source=Paths.get("files","readFile.txt");
        Path destination=Paths.get("files","fileCopy.txt");
        String line;
        try (BufferedReader reader = Files.newBufferedReader(source);
             BufferedWriter writer = Files.newBufferedWriter(destination)){
            while ((line = reader.readLine()) != null) {
                writer.write(line);
                writer.newLine();
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new NewBufferedClasses().show();
    }
}
```

Veamos cómo se utilizan estas clases con la API antigua:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class BufferedClasses {
    public void show() {
        Path source=Paths.get("files","readFile.txt");
        Path destination=Paths.get("files","fileCopy.txt");
        String line;
        try (BufferedReader reader = new BufferedReader(new FileReader(source.toFile()));
             BufferedWriter writer = new BufferedWriter(new FileWriter(destination.toFile()))){
            while ((line = reader.readLine()) != null) {
                writer.write(line);
                writer.newLine();
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new BufferedClasses().show();
    }
}
```

El tamaño del buffer predeterminado en estas clases es de 8.192 bytes (8 KB). En la mayoría de los casos, es suficiente para las operaciones habituales de lectura y escritura. Sin embargo, se podría considerar modificar el tamaño del buffer en los siguientes casos:

- Manejo de archivos muy grandes: un tamaño de buffer más grande puede mejorar el rendimiento al reducir la cantidad de veces que se interactúa con el sistema de archivos.
- Archivos pequeños o tiempo real: en operaciones con archivos muy pequeños o en tiempo real, un tamaño de buffer más pequeño puede ser más eficiente, ya que reduce el tiempo que los datos permanecen en el buffer antes de ser procesados.

En el siguiente ejemplo, se utiliza un tamaño de buffer de 16.384 bytes (16 KB):

```java
package tema1_Ficheros_ficherosTexto;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ChangeBufferSize {
    public void show() {
        final int BUFFER_SIZE = 16384;//16 KB
        Path file=Paths.get("files","fileBuffer.txt");
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file.toFile()),BUFFER_SIZE)){
            writer.write("Texto que se escribirá con un buffer personalizado de 16 KB.");
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new ChangeBufferSize().show();
    }
}
```

> [!note] ¿Quién crea el archivo?
> Hay que tener en cuenta que `BufferedWriter` por sí misma no se encarga de crear el archivo, ya que su función principal es proporcionar un buffer para la escritura, mejorando el rendimiento. Sin embargo, al utilizar `BufferedWriter` junto con `FileWriter`, y dado que `FileWriter` crea el archivo si no existe, el archivo se generará automáticamente al escribir.

### 7.5 Operaciones con arrays y desplazamientos

En Java, los métodos que utilizan arrays, como `read(char[] cbuf)` o `write(char[] cbuf)`, permiten leer o escribir datos directamente en el array, actuando como un buffer temporal. Los arrays son útiles para almacenar datos en memoria y procesarlos de manera eficiente sin necesidad de trabajar con cada carácter o byte individualmente.

Además, existen métodos que permiten procesar partes específicas del array o buffer, como `read(char[] cbuf, int off, int len)` o `write(char[] cbuf, int off, int len)`. El parámetro `off` (abreviatura de _offset_) es el **desplazamiento**, es decir, define el punto de inicio dentro del array desde donde se empezará a leer o escribir, mientras que `len` indica la cantidad de elementos a procesar. Esto ofrece varias ventajas: eficiencia al evitar la necesidad de crear nuevos arrays o cargar grandes cantidades de datos en memoria, control preciso sobre las operaciones de entrada y salida y mejora del rendimiento en aplicaciones que manejan grandes volúmenes de datos, archivos grandes o transmisión en red.

#### 7.5.1 Lectura

Veamos los métodos de la clase `FileReader` para leer caracteres de un fichero. También existen estos métodos en la clase `BufferedReader` por si al programador le interesara utilizar los beneficios de una clase con buffer:

| Método | Descripción |
| --- | --- |
| `int read()` | Lee un solo carácter y devuelve su valor Unicode como un entero. Devuelve `-1` al final del fichero. |
| `int read(char[] cbuf)` | Lee caracteres del fichero y los introduce en el array `cbuf` hasta llenarlo o hasta que se alcance el final del fichero. Devuelve el número de caracteres leídos o `-1` si no hay más datos. |
| `int read(char[] cbuf, int off, int len)` | Lee `len` caracteres del fichero y los almacena en `cbuf` a partir de la posición `off`. Devuelve el número de caracteres leídos o `-1` si se llega al final del fichero. |

Veamos un ejemplo que lee un fichero de texto carácter a carácter y los muestra en pantalla utilizando el método `int read()`. Con el `-1` se detecta el fin del fichero:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MethodRead {
    public void show() {
        Path file=Paths.get("files","readFile.txt");
        int decimalCharacterCode;
        try (FileReader reader = new FileReader(file.toFile())){
            while ((decimalCharacterCode = reader.read()) != -1) {
                System.out.print((char) decimalCharacterCode);
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodRead().show();
    }
}
```

El siguiente ejemplo, utiliza el método `int read(char[] cbuf)` para leer un fichero de texto de 10 en 10 caracteres. Si los últimos caracteres leídos son menos de 10, solamente se cogen del array los caracteres válidos:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

public class MethodReadArray {
    public void show() {
        Path file=Paths.get("files","readFile.txt");
        int numberCharactersRead;
        final int LEN = 10;
        char cbuf[]= new char[LEN];
        try (FileReader reader = new FileReader(file.toFile())){
            while ((numberCharactersRead = reader.read(cbuf)) != -1) {
                if(numberCharactersRead == LEN) {
                    //Se han leído 10 caracteres del fichero.
                    System.out.print(cbuf);
                } else {
                    /* Cuando el número de caracteres leídos sea
                     * menor que 10, son los últimos
                     * caracteres del fichero. Se devuelve una
                     * copia del array con dichos caracteres.*/
                    System.out.print(Arrays.copyOf(cbuf, numberCharactersRead));
                }
                //Se duerme durante 1 segundo:
                TimeUnit.SECONDS.sleep(1);
            }
        } catch (InterruptedException e) {
            System.err.printf("La espera fue interrumpida. El proceso no pudo completarse correctamente: %s",e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodReadArray().show();
    }
}
```

El siguiente ejemplo utiliza desplazamiento para almacenar caracteres leídos del fichero en el array a partir del cuarto carácter. El array se ha inicializado con el carácter '0', por lo que al mostrar su contenido, aparecen delante los 3 caracteres '0' y a continuación, lo que se ha leído del fichero:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

public class MethodReadArrayOffset {
    public void show() {
        Path file=Paths.get("files","readFile.txt");
        int numberCharactersRead;
        final int LEN = 10;
        final int OFF = 3;
        char cbuf[]= new char[LEN];
        //Se inicializan todos los elementos del array al carácter '0':
        Arrays.fill(cbuf, '0');
        try (FileReader reader = new FileReader(file.toFile())){
            /*Leemos 7 caracteres del fichero y se almacenan en el
             * array a partir del cuarto carácter: */
            while ((numberCharactersRead = reader.read(cbuf,OFF,LEN-OFF)) != -1) {
                if(numberCharactersRead == LEN-OFF) {
                    //Se han leído 7 caracteres del fichero.
                    System.out.print(cbuf);
                } else {
                    /* Cuando el número de caracteres leídos sea
                     * menor de 7, son los últimos caracteres del
                     * fichero. Se devuelve una copia del array
                     * con dichos caracteres.*/
                    System.out.print(Arrays.copyOf(cbuf, OFF + numberCharactersRead));
                }
                //Se duerme durante 1 segundo:
                TimeUnit.SECONDS.sleep(1);
            }
        } catch (InterruptedException e) {
            System.err.printf("La espera fue interrumpida. El proceso no pudo completarse correctamente: %s",e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodReadArrayOffset().show();
    }
}
```

#### 7.5.2 Escritura

Veamos los métodos de la clase `FileWriter` para escribir caracteres en un fichero. El fichero se crea automáticamente si no existe. Si el fichero existe, todo su contenido anterior se borra. Si lo que queremos es mantener el contenido anterior y añadir caracteres por el final, entonces se coloca un segundo parámetro en el constructor con el valor a `true`:

```java
FileWriter fic = new FileWriter(fichero, true);
```

También existen estos métodos en la clase `BufferedWriter` por si al programador le interesara utilizar los beneficios de una clase con buffer:

| Método | Descripción |
| --- | --- |
| `void write(int c)` | Escribe el carácter `c` en el fichero. |
| `void write(char[] cbuf)` | Escribe el array de caracteres `cbuf` en el fichero. |
| `void write(char[] cbuf, int off, int len)` | Escribe en el fichero `len` caracteres del array, desde el índice `off`. |
| `void write(String str)` | Escribe la cadena `str` en el fichero. |
| `void write(String str, int off, int len)` | Escribe en el fichero `len` caracteres de la cadena `str`, desde el índice `off`. |

Veamos un ejemplo que escribe en un fichero de texto utilizando los métodos `write(int c)` y `write(String str)`:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MethodWrite {
    public void show() {
        Path file=Paths.get("files","writeFile.txt");
        writeContent(file);//Escribe en el fichero
        readContent(file); //Lee el contenido del fichero
    }

    private void writeContent(Path file) {
        String str = "Estamos aprendiendo a\nescribir caracteres\ncon la clase FileWriter\n"
                + "utilizando el método write(int c)\n";
        try (FileWriter writer = new FileWriter(file.toFile())){
            for(int i=0;i<str.length();i++) {
                writer.write(str.charAt(i));
            }
            writer.write("Esta línea la he escrito con el método write(String str)");
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    private void readContent(Path file) {
        int decimalCharacterCode;
        try (FileReader reader = new FileReader(file.toFile())){
            while ((decimalCharacterCode = reader.read()) != -1) {
                System.out.print((char) decimalCharacterCode);
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodWrite().show();
    }
}
```

El siguiente ejemplo, utiliza el método `int write(char[] cbuf)` para escribir en un fichero de texto de 10 en 10 caracteres:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.*;
import java.nio.file.*;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

public class MethodWriteArray {
    public void show() {
        Path file=Paths.get("files","writeArrayFile.txt");
        writeContent(file);//Escribe en el fichero
        readContent(file); //Lee el contenido del fichero
    }

    private void writeContent(Path file) {
        String str = "Estamos aprendiendo a\nescribir buffers de caracteres\ncon la clase "
                + "FileWriter\n utilizando el método write(char[] cbuf)\n";
        char content[] = str.toCharArray();
        final int LEN = 10;
        char cbuf[]= new char[LEN];
        try (FileWriter writer = new FileWriter(file.toFile())){
            for(int i=0;i<str.length();i+=LEN) {
                if(i+LEN<str.length()) {
                    /* El método copyOfRange devuelve un array nuevo copiado
                     * del array content desde i hasta i+LEN, es decir, 10
                     * caracteres desde el índice i. Es decir, se van
                     * obteniendo los caracteres de la cadena str de 10 en 10
                     * para guardarlos en el buffer cbuf. Luego, el buffer
                     * cbuf se copia al fichero con el método
                     * write(char[] cbuf) */
                    cbuf = Arrays.copyOfRange(content, i, i + LEN);
                    writer.write(cbuf);
                }
                else {
                    /* Si i+LEN se sale de la cadena str, entonces solamente
                     * se escriben en el fichero los caracteres desde i hasta
                     * el final de la cadena */
                    writer.write(Arrays.copyOfRange(content, i, str.length()));
                }
            }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    private void readContent(Path file) {
        int numberCharactersRead;
        final int LEN = 10;
        char cbuf[]= new char[LEN];
        try (FileReader reader = new FileReader(file.toFile())){
            while ((numberCharactersRead = reader.read(cbuf)) != -1) {
                if(numberCharactersRead == LEN) {
                    //Se han leído 10 caracteres del fichero.
                    System.out.print(cbuf);
                } else {
                    /* Cuando el número de caracteres leídos sea
                     * menor que 10, son los últimos
                     * caracteres del fichero. Se devuelve una
                     * copia del array con dichos caracteres.*/
                    System.out.print(Arrays.copyOf(cbuf, numberCharactersRead));
                }
                //Se duerme durante 1 segundo:
                TimeUnit.SECONDS.sleep(1);
            }
        } catch (InterruptedException e) {
            System.err.printf("La espera fue interrumpida. El proceso no pudo completarse correctamente: %s",e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodWriteArray().show();
    }
}
```

El siguiente ejemplo utiliza desplazamiento para coger de un array de caracteres los nombres de las asignaturas y meterlo en un fichero. Para ello, utiliza el método `write(char[] cbuf, int off, int len)`:

```java
package tema1_Ficheros_ficherosTexto;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MethodWriteArrayOffset {
    public void show() {
        Path file=Paths.get("files","writeArrayOffsetFile.txt");
        writeContent(file);//Escribe en el fichero
        readContent(file); //Lee el contenido del fichero
    }

    private void writeContent(Path file) {
        String str = "Estoy matriculado de Programación y de Entornos de Desarrollo";
        char cbuf[] = str.toCharArray();
        final int LEN_PROG = 12;
        final int OFF_PROG = 21;
        final int LEN_ENT = 22;
        final int OFF_ENT = 39;
        try (FileWriter writer = new FileWriter(file.toFile())){
            writer.write(cbuf,OFF_PROG,LEN_PROG);//Escribe Programación en el fichero
            writer.write('\n');
            writer.write(cbuf,OFF_ENT,LEN_ENT);//Escribe Entornos de Desarrollo en el fichero
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    private void readContent(Path file) {
        int decimalCharacterCode;
        try (FileReader reader = new FileReader(file.toFile())){
            while ((decimalCharacterCode = reader.read()) != -1) {
                System.out.print((char) decimalCharacterCode);
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodWriteArrayOffset().show();
    }
}
```

---

## 8. Método flush

En Java, algunos flujos de escritura como `FileWriter` o `BufferedWriter`, utilizan un buffer interno para mejorar el rendimiento. En lugar de escribir directamente en el fichero cada vez que se invoca el método de escritura, los datos se acumulan en un buffer y se escriben en el archivo cuando:

1. El buffer está lleno.
2. Se invoca el método `flush`.
3. Se cierra el flujo, con el método `close` o cuando se cierra automáticamente al finalizar un `try-with-resources`.

> [!warning] Leer antes de tiempo
> Por lo tanto, si al leer un fichero antes de cerrar el flujo o hacer un `flush`, es posible que no se vea el contenido completo, ya que puede estar aún en el buffer y por lo tanto, no se ha escrito todavía físicamente en el fichero.

> [!tip] `Files` no necesita `flush`
> En el caso de los métodos de la clase `Files` como `write` y `writeString`, estos métodos realizan la escritura de forma inmediata en el fichero, ya que trabajan de manera más sencilla y no utilizan un buffer interno de la misma forma que `FileWriter` o `BufferedWriter`, por lo que no hay que preocuparse por llamar a `flush` o `close`.

Veamos el ejemplo de la clase `MethodWriteArray` utilizando el método `flush`, para no tener que esperar a leer el fichero hasta el final. En el siguiente ejemplo, cada vez que se escribe en el fichero se hace un `flush` y se hace una lectura del fichero:

```java
package tema1_Ficheros_metodoFlush;

import java.io.*;
import java.nio.file.*;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

public class MethodFlush {
    public void show() {
        Path file=Paths.get("files","methodFlush.txt");
        String str = "Estamos aprendiendo a\nescribir buffers de caracteres\ncon la clase FileWriter\n"
                + "utilizando el método write(char[] cbuf)\n";
        char content[] = str.toCharArray();
        final int LEN = 10;
        char cbuf[]= new char[LEN];
        try (FileWriter writer = new FileWriter(file.toFile())){
            for(int i=0;i<str.length();i+=10) {
                cbuf = Arrays.copyOfRange(content, i, i + LEN);
                writer.write(cbuf);
                writer.flush();// Fuerza a escribir los datos en el fichero
                readContent(file);
                System.out.println("\n");
                TimeUnit.SECONDS.sleep(1);
            }
        } catch (InterruptedException e) {
            System.err.printf("La espera fue interrumpida. El proceso no pudo completarse correctamente: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    private void readContent(Path file) {
        int decimalCharacterCode;
        try (FileReader reader = new FileReader(file.toFile())){
            while ((decimalCharacterCode = reader.read()) != -1) {
                System.out.print((char) decimalCharacterCode);
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new MethodFlush().show();
    }
}
```

---

## 9. Ficheros binarios

En Java, los ficheros binarios son archivos que almacenan datos en formato binario. Los ficheros binarios se utilizan para almacenar datos como imágenes, vídeos, archivos de audio, documentos binarios o estructuras de datos complejas (como objetos).

Los ficheros binarios no son legibles directamente por el usuario como ocurre con los ficheros de texto pero tienen la ventaja de que ocupan menos espacio en disco.

Al manipular ficheros binarios en Java, usamos flujos de bytes, ya que este tipo de flujos está diseñado específicamente para leer y escribir datos en formato binario.

Veamos las clases principales para manejar ficheros binarios:

1. `FileInputStream` y `FileOutputStream`: para leer/escribir bytes en un fichero binario.
2. `BufferedInputStream` y `BufferedOutputStream`: para leer/escribir datos binarios de forma más eficiente, usando un buffer intermedio. Al utilizar buffer la clase `BufferedOutputStream`, hay que usar `flush` si se quiere leer el fichero antes de cerrar el flujo.
3. `DataInputStream` y `DataOutputStream`: para leer y escribir tipos de datos primitivos de una forma más conveniente, preservando el formato binario.
4. `ObjectInputStream` y `ObjectOutputStream`: para leer y escribir objetos en un fichero binario.

### 9.1 FileInputStream y FileOutputStream

Veamos los métodos de la clase `FileInputStream` para leer de un fichero binario:

| Método | Descripción |
| --- | --- |
| `int read()` | Lee un byte del fichero y devuelve su valor como un entero (0-255). Devuelve -1 si se ha llegado al final del fichero. |
| `int read(byte[] b)` | Lee bytes del fichero y los introduce en el array `b` y devuelve el número de bytes leídos. Devuelve -1 si se ha llegado al final del fichero. |
| `int read(byte[] b, int off, int len)` | Lee `len` bytes del fichero y los almacena en el array `b` comenzando desde el índice `off`. Devuelve el número de bytes leídos o -1 si se ha llegado al final del fichero. |

Veamos los métodos de la clase `FileOutputStream` para escribir en un fichero binario:

| Método | Descripción |
| --- | --- |
| `void write(int b)` | Escribe un byte en el fichero. Solo se escribe el último byte del valor entero `b` (0-255). |
| `void write(byte[] b)` | Escribe los bytes del array `b` en el fichero. |
| `void write(byte[] b, int off, int len)` | Escribe en el fichero `len` bytes del array `b`, comenzando desde el índice `off`. |

Tal y como ocurre con `FileWriter`, en la clase `FileOutputStream`, si el fichero existe, todo su contenido anterior se borra. Si lo que queremos es mantener el contenido anterior y añadir bytes por el final, entonces se coloca un segundo parámetro en el constructor con el valor a `true`:

```java
FileOutputStream fic = new FileOutputStream(fichero,true);
```

> [!note] Sin buffer
> `FileOutputStream` escribe directamente al archivo y no requiere el uso de `flush`. Además, `FileOutputStream` crea el fichero automáticamente si no existe.

El siguiente ejemplo escribe los números del 1 al 100 en un fichero binario, a continuación lee el fichero y muestra el contenido por consola:

```java
package tema1_Ficheros_ficherosBinarios;

import java.io.*;
import java.nio.file.*;

public class BinaryFile {
    public void show() {
        Path file=Paths.get("files","binaryFile.dat");
        int i;
        try (FileOutputStream writer = new FileOutputStream(file.toFile());
             FileInputStream reader = new FileInputStream(file.toFile())){
            for(i=1;i<=100;i++) {
                writer.write(i);
            }
            //Se puede leer sin usar flush
            while ((i = reader.read()) != -1) {
                System.out.println(i);
            }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new BinaryFile().show();
    }
}
```

### 9.2 DataInputStream y DataOutputStream

Estas clases se utilizan para leer y escribir tipos de datos primitivos (como `int`, `float`, `double`, etc.) de una forma más conveniente, preservando el formato binario. Si observamos en la API la clase `DataInputStream`, existen métodos `read` para cada uno de los tipos primitivos: `readInt()`, `readDouble()`, etc. Igualmente, tenemos los métodos de escritura `write` en la clase `DataOutputStream`: `writeInt()`, `writeDouble()`, etc.

`DataOutputStream`, cuando se combina con `FileOutputStream`, crea el archivo si no existe. Esto se debe a que `FileOutputStream` es quien se encarga de abrir el archivo para escritura, y si el archivo no existe, lo crea automáticamente.

`DataOutputStream` no necesita `flush` por sí solo, pero sí es necesario si lo combinas con un flujo con buffer como `BufferedOutputStream`.

Los métodos `readUTF()` y `writeUTF()` en Java son utilizados para leer y escribir cadenas de texto en un formato especial llamado UTF-8 modificado en flujos de datos binarios. Estos métodos son parte de las interfaces `DataInput` y `DataOutput`, que son implementadas por las clases `DataInputStream` y `DataOutputStream`. El formato **UTF-8 modificado** es una variación del estándar UTF-8 que se utiliza para comprimir las cadenas de texto y que garantiza la compatibilidad entre las distintas versiones de Java. En este formato, las cadenas se codifican en formato binario con la longitud de la cadena almacenada en los primeros dos bytes, seguida de los bytes que representan los caracteres. Es ideal para escribir texto en archivos binarios o en la red, donde se necesita un formato compacto. Hay que tener en cuenta cuando se trabaja con estas clases, que los datos se tienen que leer en el mismo orden en que fueron escritos, para poder preservar su tipo original. Es decir, `readUTF()` lee una cadena de texto que fue previamente escrita con `writeUTF()` desde un flujo de datos binario. `readUTF()` primero lee los dos bytes que indican la longitud de la cadena y luego decodifica los bytes en caracteres UTF-8. Si el formato de los datos no coincide con lo esperado (es decir, si no se escribió con `writeUTF()`), se lanzará una excepción `UTFDataFormatException`. Debido a que el tamaño de la cadena se almacena en dos bytes, el máximo tamaño que puede almacenar una cadena con `writeUTF()` es de 65.535 bytes (no caracteres, ya que en UTF-8 algunos caracteres ocupan más de un byte). Si la cadena excede los 65.535 bytes (2^16) en su representación UTF-8, se lanzará un `UTFDataFormatException`.

Hay otra manera de escribir cadenas de texto, con el método `writeChars(String s)`. Dicho método no utiliza un formato de codificación específico (como UTF-8), sino que simplemente escribe el valor numérico de cada carácter (de 16 bits) directamente en el flujo, es decir, escribe cada carácter en su formato de valor Unicode, por lo que siempre ocupan 2 bytes por carácter incluso si se trata de un carácter que podría codificarse en menos espacio. Este método no incluye información de la longitud de la cadena ni utiliza codificación compacta, sino que cada carácter ocupa exactamente 2 bytes, lo que significa que puede generar archivos más grandes que con otros métodos como `writeUTF()`. Esto puede ser útil para mantener consistencia en archivos binarios que siempre deben tener el mismo tamaño por carácter. Al no añadir información de la longitud, es importante leer los caracteres exactamente en el mismo orden en que fueron escritos.

| Método | Formato | Tamaño | Lectura |
| --- | --- | --- | --- |
| `writeUTF(String)` | UTF-8 modificado, con la longitud en los 2 primeros bytes | Compacto; máximo 65.535 bytes | `readUTF()` |
| `writeChars(String)` | Valor Unicode de cada carácter, sin longitud | Siempre 2 bytes por carácter | `readChar()` carácter a carácter |

> [!warning] Mismo orden de lectura y escritura
> En un fichero binario no hay "marcas" de tipo: los datos se leen **en el mismo orden y con el mismo tipo** con el que se escribieron. Si se escribe `writeInt` y luego `writeDouble`, hay que leer `readInt` y luego `readDouble`.

> [!tip] `EOFException` como fin de fichero
> En un fichero binario cualquier valor es válido, así que no existe un `-1` que marque el final: se lee en un `while (true)` y se captura `EOFException`.

El siguiente ejemplo escribe en un fichero datos primitivos y cadenas. A continuación, se lee el fichero y se muestra su contenido por consola. Como en un fichero binario puede existir cualquier valor, no hay manera de detectar con una secuencia de bits el final del fichero. En este caso, el programador lo puede detectar porque Java lanza la excepción `EOFException` cuando detecta el final del fichero:

```java
package tema1_Ficheros_ficherosBinarios;

import java.io.*;
import java.nio.file.*;

public class DataBinaryFile {
    public void show() {
        Path file=Paths.get("files","dataBinaryFile.dat");
        write(file);
        read(file);
    }

    public void write (Path file) {
        try (DataOutputStream writer = new DataOutputStream((new FileOutputStream(file.toFile())))){
             writer.writeUTF("He utilizado writeUTF para esta cadena");
             writer.writeInt(12345);
             writer.writeDouble(123.456);
             writer.writeChar('A');
             writer.writeBoolean(true);
             writer.writeChars("He utilizado writeChars para esta cadena");
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public void read (Path file) {
        StringBuilder text = new StringBuilder();
        char character;
        try (DataInputStream reader = new DataInputStream((new FileInputStream(file.toFile())))){
            System.out.println(reader.readUTF());
            System.out.println(reader.readInt());
            System.out.println(reader.readDouble());
            System.out.println(reader.readChar());
            System.out.println(reader.readBoolean());
            while (true) {
                //Se lee un carácter hasta que se lanza la excepción EOFException
                character = reader.readChar();
                text.append(character);
            }
        } catch (EOFException e) {
            System.out.println(text);//Muestra el contenido acumulado
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new DataBinaryFile().show();
    }
}
```

> [!example] Ejercicios
> [[01.3 - Ejercicios 1 Ficheros binarios]] — agenda telefónica en un fichero binario con `DataOutputStream`/`DataInputStream`.

### 9.3 ObjectInputStream y ObjectOutputStream

Para guardar objetos en un fichero binario en Java, se utiliza serialización. La **serialización** convierte un objeto en una secuencia de bytes que se puede escribir en un fichero y, más tarde, deserializar para reconstruir el objeto original. Para ello, Java proporciona las clases `ObjectOutputStream` y `ObjectInputStream`. La clase de los objetos que se desean guardar, debe implementar la interfaz `Serializable`. Esto permite que los objetos de esa clase se puedan convertir a bytes. La interfaz `Serializable` es una interfaz de marcado (no contiene métodos). Si una clase tiene atributos que son objetos, éstos también deben ser `Serializable` para poder guardarlos en un fichero binario.

Para **escribir el objeto** en el fichero binario se usa `ObjectOutputStream` junto con `FileOutputStream`. El método para escribir el objeto es el siguiente:

```java
final void writeObject(Object obj)
```

Para **leer el objeto** y deserializarlo, se usa `ObjectInputStream` junto con `FileInputStream`. El método para leer el objeto es el siguiente:

```java
final Object readObject()
```

Veamos un ejemplo con la clase `Vehicle`. En este caso, la clase `Vehicle` implementa `Serializable` y define un `serialVersionUID`, que es recomendable para mantener la compatibilidad de versiones de la clase en futuras actualizaciones, es decir, si cambia la estructura de una clase porque por ejemplo se añada o elimine un atributo, es posible que la deserialización falle. Definir un `serialVersionUID` ayuda a gestionar estas situaciones.

```java
package tema1_Ficheros_ficherosBinarios;

import java.io.*;
import java.nio.file.*;
import java.util.*;

public class SaveObject {
    public void show() {
        Path file=Paths.get("files","vehicles.dat");
        List<Vehicle> vehicles = generateVehicles();
        writeObjects(file,vehicles);//Escribe objetos Vehicle en el fichero
        readObjects(file); //Lee objetos Vehicle del fichero
    }

    private List<Vehicle> generateVehicles(){
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle(4, "rojo"));
        vehicles.add(new Vehicle(2, "azul"));
        vehicles.add(new Vehicle(4, "blanco"));
        vehicles.add(new Vehicle(2, "verde"));
        vehicles.add(new Vehicle(2, "rojo"));
        return vehicles;
    }

    private void writeObjects(Path file,List<Vehicle> vehicles) {
        try (ObjectOutputStream writer = new ObjectOutputStream(new FileOutputStream(file.toFile()))){
            for(Vehicle vehicle:vehicles) {
                writer.writeObject(vehicle);//Escribe un objeto vehículo en el fichero
            }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    private void readObjects(Path file) {
        Vehicle vehicle;
        try (ObjectInputStream reader = new ObjectInputStream(new FileInputStream(file.toFile()))) {
            while (true) {
                vehicle = (Vehicle) reader.readObject();//Lee un objeto vehículo del fichero
                System.out.println(vehicle);
            }
        } catch (EOFException e) {
            System.out.println("Lectura del fichero finalizada");
        } catch (ClassNotFoundException e) {
            System.err.printf("Clase no encontrada: %s",e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new SaveObject().show();
    }
}
```

`ObjectOutputStream` convierte los objetos `vehicle` en una secuencia de bytes y los guarda en el fichero `"vehicles.dat"`. `ObjectInputStream` convierte la secuencia de bytes de `"vehicles.dat"` en objetos `Vehicle`.

> [!warning] Cabecera duplicada → `StreamCorruptedException`
> Pero existe un problema con los ficheros de objetos: al escribir objetos en un fichero por primera vez, `ObjectOutputStream` añade una cabecera al inicio del fichero. Esta cabecera indica el inicio de una secuencia de objetos serializados. Si se quiere escribir objetos en un fichero pero respetando los objetos que ya tiene, al abrir el fichero con `ObjectOutputStream`, ésta añadirá otra cabecera. Cuando se lea el fichero y se llegue a la segunda cabecera, se lanzará la excepción `StreamCorruptedException`. Para resolver este problema, se crea una subclase de `ObjectOutputStream` que evite escribir la cabecera si el fichero ya contiene objetos. De esta forma, solo se escribe la cabecera la primera vez y, en sucesivas escrituras, se omite.

En el ejemplo, se abre el fichero con el segundo parámetro del constructor de `FileOutputStream` a `true` (`new FileOutputStream(file.toFile(), true)`) para añadir contenido y se utiliza como `ObjectOutputStream`, la clase `AppendableObjectOutputStream`. De esta forma, no se escribe la cabecera:

```java
package tema1_Ficheros_ficherosBinarios;

import java.io.*;

public class AppendableObjectOutputStream extends ObjectOutputStream{
    public AppendableObjectOutputStream(OutputStream out) throws IOException {
        super(out);
    }

    @Override
    protected void writeStreamHeader() throws IOException {
    }
}
```

```java
package tema1_Ficheros_ficherosBinarios;

import java.io.*;
import java.nio.file.*;
import java.util.*;

public class SaveAppendableObject {
    public void show() {
        Path file=Paths.get("files","vehicles.dat");
        List<Vehicle> vehicles = generateVehicles();
        writeObjects(file,vehicles);//Escribe objetos Vehicle en el fichero
        readObjects(file); //Lee objetos Vehicle del fichero
    }

    private List<Vehicle> generateVehicles(){
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle(2, "amarillo"));
        vehicles.add(new Vehicle(4, "negro"));
        vehicles.add(new Vehicle(4, "naranja"));
        return vehicles;
    }

    private void writeObjects(Path file,List<Vehicle> vehicles) {
        try (FileOutputStream fos = new FileOutputStream(file.toFile(), true);
             ObjectOutputStream writer = new AppendableObjectOutputStream(fos)) {
            for(Vehicle vehicle:vehicles) {
                writer.writeObject(vehicle);
            }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    private void readObjects(Path file) {
        Vehicle vehicle;
        try (ObjectInputStream reader = new ObjectInputStream(new FileInputStream(file.toFile()))) {
            while (true) {
                vehicle = (Vehicle) reader.readObject();
                System.out.println(vehicle);
            }
        } catch (EOFException e) {
            System.out.println("Lectura del fichero finalizada");
        } catch (ClassNotFoundException e) {
            System.err.printf("Clase no encontrada: %s",e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new SaveAppendableObject().show();
    }
}
```

> [!example] Ejercicios
> [[01.4 - Ejercicios 1 Ficheros binarios de objetos]] — agenda telefónica guardando objetos, con menú consultar/sobrescribir/añadir.

---

## 10. Ficheros de acceso aleatorio

Hasta ahora, todas las operaciones que hemos realizado sobre los ficheros se realizaban de forma secuencial. Se empezaba la lectura en el primer byte o el primer carácter o el primer objeto, y seguidamente se leían los siguientes uno a continuación de otro hasta llegar al fin del fichero. Igualmente cuando escribíamos los datos en el fichero se iban escribiendo a continuación de la última información escrita. Java dispone de la clase `RandomAccessFile` que dispone de métodos para acceder al contenido de un fichero binario de forma aleatoria (no secuencial) y para posicionarnos en una posición concreta del mismo. Esta clase no es parte de la jerarquía `InputStream/OutputStream`, ya que su comportamiento es totalmente distinto puesto que se puede avanzar y retroceder dentro de un fichero. Esto es especialmente útil cuando se necesita modificar o acceder a ciertas partes de un fichero grande, sin cargarlo completamente en memoria.

A diferencia de otras clases de ficheros en Java, `RandomAccessFile` permite leer y escribir en el mismo fichero. En los constructores de la clase `RandomAccessFile`, se especifica con un parámetro el modo de acceso al fichero:

- `r`: abre el fichero en modo de solo lectura. El fichero debe existir. Una operación de escritura en este fichero lanzará la excepción `IOException`.
- `rw`: abre el fichero en modo lectura y escritura. Si el fichero no existe se crea.

Una vez abierto el fichero pueden usarse los mismos métodos `read` de la clase `DataInputStream` para cada uno de los tipos primitivos (`readInt()`, `readDouble()`, etc), y los mismos métodos `write` de la clase `DataOutputStream` (`writeInt()`, `writeDouble()`, etc).

La clase `RandomAccessFile` maneja un **puntero** que indica la posición actual en el fichero. Cuando el fichero se crea, el puntero apunta al principio del mismo. Las sucesivas llamadas a los métodos `read` y `write` ajustan el puntero según la cantidad de bytes leídos o escritos. Además, el programador puede mover el puntero a cualquier posición del fichero.

Veamos los métodos principales:

| Método | Función |
| --- | --- |
| `long length()` | Devuelve el tamaño del fichero en bytes. La posición `length()` marca el final del fichero. |
| `long getFilePointer()` | Devuelve la posición actual del puntero. |
| `void seek(long pos)` | Permite mover el puntero a una posición específica, donde `pos` es el número de bytes desde el comienzo del fichero. |
| `int skipBytes(int n)` | Avanza el puntero un número específico de bytes. Devuelve el número real de bytes saltados, que puede ser menor que `n` si se intenta saltar más allá del final. Si `n` es negativo, no avanza el puntero. |

> [!tip] Detectar el final del fichero
> El final del fichero se detecta cuando el puntero alcanza la longitud del fichero, es decir, el bucle se realiza mientras el puntero sea más pequeño: `while(reader.getFilePointer() < reader.length())`.

En los siguientes ejemplos, se está utilizando un fichero de acceso aleatorio con vehículos. Para que se pueda acceder en modo aleatorio, se guarda en el fichero un identificador para cada vehículo para que el usuario pueda especificar el índice del vehículo que desea leer, modificar o eliminar. Los vehículos se pueden almacenar con un tamaño fijo o, si el tamaño varía, hay que almacenar la información de desplazamiento (offset) de cada uno. En los ejemplos, todos los vehículos ocupan lo mismo. Para ello, hay que fijar el número de caracteres máximo que van a tener las cadenas. En nuestro caso, son los colores los que se almacenan en cadena y se utilizan 15 caracteres para guardar el color. Si algún color es más pequeño, se rellena con espacios. Al leer el color, se pueden eliminar los espacios con el método `trim()` de las cadenas. Para saber el tamaño de cada vehículo, hay que sumar los bytes en función de cada tipo de dato:

- `int` para el identificador: 4 bytes.
- `int` para el número de ruedas: 4 bytes.
- `double` para la velocidad: 8 bytes.
- 15 caracteres de tipo `char` para el color. Como cada `char` ocupa 2 bytes: 30 bytes.

> [!tip] Registro de tamaño fijo
> Por lo tanto, cada vehículo ocupa **4 + 4 + 8 + 30 = 46 bytes**. Así, el vehículo con identificador `n` empieza en la posición `(n - 1) * 46`, que es lo que se le pasa a `seek`.

El siguiente ejemplo guarda vehículos en un fichero y luego los lee para mostrarlos por consola. Ambos procesos son secuenciales, no hace falta hacer un uso del fichero de manera aleatoria ya que hay que recorrerlo de principio a fin:

```java
package tema1_Ficheros_ficherosAccesoAleatorio;

public final class Constants {
    //Longitud del color: 15 caracteres
    public static final int LEN_COLOR = 15;

    //Número de bytes que ocupa cada vehículo
    public static final int NUM_BYTES_VEHICLE = 46;

    //Número de bytes donde se encuentra el color en un vehículo
    public static final int POSITION_COLOR = 16;

    //Número de bytes que ocupa el identificador
    public static final int IDENTIFIER = 4;
}
```

```java
package tema1_Ficheros_ficherosAccesoAleatorio;

import static tema1_Ficheros_ficherosAccesoAleatorio.Constants.LEN_COLOR;
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class AccessSequential {
    public void show() {
        Path file=Paths.get("files","randomAccessFile.dat");
        List<Vehicle> vehicles = generateVehicles();
        writeSequential(file, vehicles);//Se crea el fichero con los vehículos de manera secuencial
        readSequential(file);//Se lee el fichero de manera secuencial para mostrar los vehículos por consola
    }

    private List<Vehicle> generateVehicles(){
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle(4, "rojo"));
        vehicles.add(new Vehicle(2, "azul"));
        vehicles.add(new Vehicle(4, "blanco"));
        vehicles.add(new Vehicle(2, "verde"));
        vehicles.add(new Vehicle(2, "amarillo"));
        for(int i=0;i<vehicles.size();i++) {
            vehicles.get(i).accelerate(i*50.25);
        }
        return vehicles;
    }

    //Este método escribe de manera secuencial
    private void writeSequential (Path file, List<Vehicle> vehicles) {
        StringBuilder sb;
        int identifier=0;
        try (RandomAccessFile writer = new RandomAccessFile(file.toFile(), "rw")) {
             for(Vehicle v:vehicles) {
                 writer.writeInt(++identifier);
                 writer.writeInt(v.getWheelCount());
                 writer.writeDouble(v.getSpeed());
                 sb = new StringBuilder(v.getColour());
                 sb.setLength(LEN_COLOR);
                 writer.writeChars(sb.toString());
             }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    //Este método lee de manera secuencial
    private void readSequential (Path file) {
        char[] buffer = new char[LEN_COLOR];
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
            System.out.println("Lectura del fichero de manera secuencial:");
            while(reader.getFilePointer() < reader.length()) {
                System.out.printf("Vehículo %d: \n",reader.readInt());
                System.out.printf("\tNúmero de ruedas: %d\n",reader.readInt());
                System.out.printf("\tVelocidad: %.2f\n",reader.readDouble());
                for (int i = 0; i < LEN_COLOR; i++) {
                    buffer[i] = reader.readChar();
                }
                System.out.printf("\tColor: %s\n",new String(buffer).trim());
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new AccessSequential().show();
    }
}
```

En el ejemplo siguiente, se accede al fichero de manera aleatoria para buscar el vehículo que indique el usuario. Al usuario se le muestra el rango de identificadores válidos. Para ello, el método `calculateLastIndex` se posiciona en el último vehículo para leer el identificador. A continuación, el método `readRandom` accede al vehículo elegido por el usuario, lee el vehículo y lo muestra por consola:

```java
package tema1_Ficheros_ficherosAccesoAleatorio;

import static tema1_Ficheros_ficherosAccesoAleatorio.Constants.*;
import java.io.*;
import java.nio.file.*;
import java.util.Scanner;

public class ReadRandom {
    public void show() {
        Path file=Paths.get("files","randomAccessFile.dat");
        int lastIdentifier = calculateLastIndex(file);
        readRandom(file, lastIdentifier);//Se lee un vehículo del fichero de manera aleatoria
    }

    //Este método calcula el último identificador
    private int calculateLastIndex (Path file) {
        int lastIdentifier = 0;
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
             reader.seek(reader.length()-NUM_BYTES_VEHICLE);//Se posiciona en el último vehículo
             lastIdentifier=reader.readInt();//Lee el identificador del último vehículo
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
        return lastIdentifier;
    }

    //Este método lee de manera aleatoria
    @SuppressWarnings("resource")
    private void readRandom (Path file, int lastIdentifier) {
        Scanner keyboard = new Scanner(System.in);
        char[] buffer = new char[LEN_COLOR];
        int identifier;
        long position;
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
            System.out.printf("\nIntroduce el identificador del vehículo que quieres consultar entre 1 y %d: ",lastIdentifier);
            identifier=keyboard.nextInt();
            position = (identifier-1) * NUM_BYTES_VEHICLE;
            if (position >= 0 && position < reader.length()) {
                reader.seek(position);//Se coloca el puntero al comienzo del vehículo elegido por el usuario
                System.out.printf("Vehículo %d: \n", reader.readInt());
                System.out.printf("\tNúmero de ruedas: %d\n", reader.readInt());
                System.out.printf("\tVelocidad: %.2f\n", reader.readDouble());
                for (int j = 0; j < LEN_COLOR; j++) {
                    buffer[j] = reader.readChar(); // Lee un carácter
                }
                System.out.printf("\tColor: %s\n", new String(buffer).trim());
            } else {
                System.out.println("El índice del vehículo no es correcto.");
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new ReadRandom().show();
    }
}
```

El siguiente ejemplo modifica el color de un vehículo a petición del usuario. El puntero se coloca en el color del vehículo y lo sobrescribe con el nuevo valor:

```java
package tema1_Ficheros_ficherosAccesoAleatorio;

import static tema1_Ficheros_ficherosAccesoAleatorio.Constants.*;
import java.io.*;
import java.nio.file.*;
import java.util.Scanner;

public class ModifyColor {
    public void show() {
        Path file=Paths.get("files","randomAccessFile.dat");
        int lastIdentifier = calculateLastIndex(file);
        readSequential(file);
        modifyColour(file, lastIdentifier);//Se modifica un color de un vehículo de manera aleatoria
        readSequential(file);
    }

    //Este método calcula el último identificador
    private int calculateLastIndex (Path file) {
        int lastIdentifier = 0;
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
             reader.seek(reader.length()-NUM_BYTES_VEHICLE);//Se posiciona en el último vehículo
             lastIdentifier=reader.readInt();//Lee el identificador del último vehículo
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
        return lastIdentifier;
    }

    //Este método lee de manera secuencial
    private void readSequential (Path file) {
        char[] buffer = new char[LEN_COLOR];
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
            System.out.println("Lectura del fichero de manera secuencial:");
            while(reader.getFilePointer() < reader.length()) {
                System.out.printf("Vehículo %d: \n",reader.readInt());
                System.out.printf("\tNúmero de ruedas: %d\n",reader.readInt());
                System.out.printf("\tVelocidad: %.2f\n",reader.readDouble());
                for (int i = 0; i < LEN_COLOR; i++) {
                    buffer[i] = reader.readChar();
                }
                System.out.printf("\tColor: %s\n",new String(buffer).trim());
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    //Este método modifica el color de un vehículo
    @SuppressWarnings("resource")
    private void modifyColour (Path file, int lastIdentifier) {
        Scanner keyboard = new Scanner(System.in);
        StringBuilder sb;
        int i;
        long position;
        try (RandomAccessFile writer = new RandomAccessFile(file.toFile(), "rw")) {
            System.out.printf("\nIntroduce el índice del vehículo (1-%d) al que quieres modificarle el color: ",lastIdentifier);
            i=keyboard.nextInt();
            keyboard.nextLine();//Limpieza del buffer
            position = (i-1) * NUM_BYTES_VEHICLE;
            if (position >= 0 && position < writer.length()) {
                writer.seek(position);//Se coloca el puntero al comienzo del vehículo elegido por el usuario
                writer.skipBytes(POSITION_COLOR);//Se coloca el puntero en el color
                System.out.println("Introduce el nuevo color del vehículo: ");
                sb = new StringBuilder(keyboard.nextLine());
                sb.setLength(LEN_COLOR);
                writer.writeChars(sb.toString());
            } else {
                System.out.println("El índice del vehículo no es correcto.");
            }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new ModifyColor().show();
    }
}
```

> [!warning] Añadir por el final
> La clase `RandomAccessFile` siempre sobrescribe el fichero por defecto. Si lo que deseamos es añadir por el final, hay que poner el puntero al final y luego escribir. Cómo colocar el puntero al final: `reader.seek(reader.length());`. En el ejemplo siguiente, se añade un vehículo nuevo al final del fichero:

```java
package tema1_Ficheros_ficherosAccesoAleatorio;

import static tema1_Ficheros_ficherosAccesoAleatorio.Constants.*;
import java.io.*;
import java.nio.file.*;
import java.util.Scanner;

public class AddAtTheEnd {
    public void show() {
        Path file=Paths.get("files","randomAccessFile.dat");
        readSequential(file);
        addAtTheEnd(file);//Se añade un vehículo nuevo al final del fichero
        readSequential(file);
    }

    //Este método lee de manera secuencial
    private void readSequential (Path file) {
        char[] buffer = new char[LEN_COLOR];
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
            System.out.println("Lectura del fichero de manera secuencial:");
            while(reader.getFilePointer() < reader.length()) {
                System.out.printf("Vehículo %d: \n",reader.readInt());
                System.out.printf("\tNúmero de ruedas: %d\n",reader.readInt());
                System.out.printf("\tVelocidad: %.2f\n",reader.readDouble());
                for (int i = 0; i < LEN_COLOR; i++) {
                    buffer[i] = reader.readChar();
                }
                System.out.printf("\tColor: %s\n",new String(buffer).trim());
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    //Este método añade un vehículo nuevo al final del fichero
    @SuppressWarnings("resource")
    private void addAtTheEnd (Path file) {
        Scanner keyboard = new Scanner(System.in);
        StringBuilder sb;
        int last;
        try (RandomAccessFile raf = new RandomAccessFile(file.toFile(), "rw")) {
             raf.seek(raf.length()-NUM_BYTES_VEHICLE);//Se posiciona en el último vehículo
             last=raf.readInt();//Lee el identificador del último vehículo
             raf.seek(raf.length());//Se posiciona al final del fichero
             raf.writeInt(++last);
             System.out.println("Vas a añadir un nuevo vehículo por el final");
             System.out.print("Introduce el número de ruedas: ");
             raf.writeInt(keyboard.nextInt());
             System.out.print("Introduce la velocidad: ");
             raf.writeDouble(keyboard.nextDouble());
             keyboard.nextLine();//Limpieza del buffer
             System.out.print("Introduce el color: ");
             sb = new StringBuilder(keyboard.nextLine());
             sb.setLength(LEN_COLOR);
             raf.writeChars(sb.toString());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new AddAtTheEnd().show();
    }
}
```

El siguiente ejemplo sustituye un vehículo por otro elegido por el usuario:

```java
package tema1_Ficheros_ficherosAccesoAleatorio;

import static tema1_Ficheros_ficherosAccesoAleatorio.Constants.*;
import java.io.*;
import java.nio.file.*;
import java.util.Scanner;

public class ReplaceVehicle {
    public void show() {
        Path file=Paths.get("files","randomAccessFile.dat");
        int lastIdentifier = calculateLastIndex(file);
        readSequential(file);
        replaceVehicle(file, lastIdentifier);//Se sustituye un vehículo por otro
        readSequential(file);
    }

    //Este método calcula el último identificador
    private int calculateLastIndex (Path file) {
        int lastIdentifier = 0;
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
             reader.seek(reader.length()-NUM_BYTES_VEHICLE);//Se posiciona en el último vehículo
             lastIdentifier=reader.readInt();//Lee el identificador del último vehículo
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
        return lastIdentifier;
    }

    //Este método lee de manera secuencial
    private void readSequential (Path file) {
        char[] buffer = new char[LEN_COLOR];
        try (RandomAccessFile reader = new RandomAccessFile(file.toFile(), "r")){
            System.out.println("Lectura del fichero de manera secuencial:");
            while(reader.getFilePointer() < reader.length()) {
                System.out.printf("Vehículo %d: \n",reader.readInt());
                System.out.printf("\tNúmero de ruedas: %d\n",reader.readInt());
                System.out.printf("\tVelocidad: %.2f\n",reader.readDouble());
                for (int i = 0; i < LEN_COLOR; i++) {
                    buffer[i] = reader.readChar();
                }
                System.out.printf("\tColor: %s\n",new String(buffer).trim());
            }
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    //Este método sustituye un vehículo por otro
    @SuppressWarnings("resource")
    private void replaceVehicle (Path file, int lastIdentifier) {
        Scanner keyboard = new Scanner(System.in);
        StringBuilder sb;
        int i;
        long position;
        try (RandomAccessFile writer = new RandomAccessFile(file.toFile(), "rw")) {
            System.out.printf("\nIntroduce el índice (1-%d) del vehículo que quieres sustituir: ",lastIdentifier);
            i=keyboard.nextInt();
            keyboard.nextLine();//Limpieza del buffer
            position = (i-1) * NUM_BYTES_VEHICLE;
            if (position >= 0 && position < writer.length()) {
                writer.seek(position);//Se coloca el puntero al comienzo del vehículo elegido por el usuario
                writer.skipBytes(IDENTIFIER);//Se salta el identificador porque es el mismo
                System.out.print("Introduce el número de ruedas: ");
                writer.writeInt(keyboard.nextInt());
                System.out.print("Introduce la velocidad: ");
                writer.writeDouble(keyboard.nextDouble());
                keyboard.nextLine();//Limpieza del buffer
                System.out.print("Introduce el color: ");
                sb = new StringBuilder(keyboard.nextLine());
                sb.setLength(LEN_COLOR);
                writer.writeChars(sb.toString());
            } else {
                System.out.println("El índice del vehículo no es correcto.");
            }
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new ReplaceVehicle().show();
    }
}
```

> [!example] Ejercicios
> [[01.5 - Ejercicios 1 Ficheros de acceso aleatorio]] — agenda telefónica con `RandomAccessFile`: consultar, añadir y modificar contactos.

---

## 11. Ficheros XML y JSON

### 11.1 Ficheros XML

**XML** (e**X**tensible **M**arkup **L**anguage) es un formato de texto que permite estructurar datos de forma jerárquica utilizando etiquetas personalizadas.

La **estructura** de un documento XML es jerárquica, organizada en elementos que se anidan unos dentro de otros. Veamos un ejemplo de estructura XML para un alumno:

```xml
<alumno>
    <nombre>Juan Pérez</nombre>
    <edad>20</edad>
    <asignaturas>
        <asignatura>Programación</asignatura>
        <asignatura>Entornos de Desarrollo</asignatura>
    </asignaturas>
</alumno>
```

**Componentes principales de XML:**

- Elementos: en el ejemplo, `<alumno>`, `<nombre>`, `<edad>`, y `<asignatura>` son elementos.
- Atributos: se pueden añadir atributos dentro de las etiquetas para almacenar información adicional. Estos atributos deben ir entre comillas. Ejemplo: `<alumno id="1">`.
- Etiquetas de apertura y cierre: cada elemento tiene una etiqueta de apertura (`<nombre>`) y una de cierre (`</nombre>`).

**Reglas de XML:**

- Todo documento XML debe tener un elemento raíz único.
- Las etiquetas son sensibles a mayúsculas/minúsculas.
- Las etiquetas deben estar correctamente anidadas.

### 11.2 Ficheros JSON

**JSON** (**J**ava**S**cript **O**bject **N**otation) es un formato de texto ligero para el intercambio de datos, más simple que XML y ampliamente usado en aplicaciones web.

La **estructura** de un documento JSON está organizada en pares clave-valor, objetos y listas (arrays). Veamos el ejemplo del alumno en JSON:

```json
{
    "nombre": "Juan Pérez",
    "edad": 20,
    "asignaturas": ["Programación", "Entornos de Desarrollo"]
}
```

**Componentes principales de JSON:**

- Pares clave-valor: `"nombre": "Juan Pérez"` es un par clave-valor.
- Arrays: los arrays en JSON se definen entre corchetes `[]`. En este caso, `"asignaturas"` contiene un array de cadenas.
- Objetos: en JSON, un objeto es un conjunto de pares clave-valor delimitados por llaves `{}`.

**Tipos de datos en JSON**: en JSON, los tipos de datos son pocos y sencillos, lo cual facilita su uso como formato de intercambio de datos. Los tipos de datos en JSON son:

- Cadena de texto: se representan entre comillas dobles (`""`). Las cadenas pueden contener cualquier combinación de caracteres Unicode. Ejemplo:

    ```json
    "nombre": "Juan Pérez"
    ```

- Números: pueden ser enteros o decimales, positivos o negativos. En JSON no se diferencian los tipos de números (int, float, etc.) como en otros lenguajes, se manejan de forma unificada. Ejemplo:

    ```json
    "edad": 30,
    "altura": 1.75
    ```

- Booleanos: puede ser `true` o `false`. Ejemplo:

    ```json
    "esEstudiante": true
    ```

- Nulo (`null`): representa una ausencia de valor. Ejemplo:

    ```json
    "direccion": null
    ```

- Objeto: es una estructura de pares clave-valor, similar a un diccionario o mapa en otros lenguajes. Los objetos se representan entre llaves `{ }`, y cada par de clave-valor está separado por comas. Las claves deben ser cadenas de texto, como en el ejemplo, `"alumno"`, `"nombre"` y `"edad"`:

    ```json
    "alumno": {
        "nombre": "Ana",
        "edad": 20
    }
    ```

- Array: es una lista ordenada de valores, que pueden ser de cualquiera de los tipos anteriores, incluyendo otros arrays u objetos. Se representan entre corchetes `[ ]`. Ejemplo:

    ```json
    "amigos": ["Carlos", "Lucía", "Miguel"],
    "puntuaciones": [10, 20, 15, 30]
    ```

Veamos un ejemplo completo de JSON con todos los tipos de datos:

```json
{
   "nombre": "Carlos",
   "edad": 28,
   "esEstudiante": false,
   "direccion": null,
   "hobbies": ["lectura", "ajedrez", "ciclismo"],
   "contacto": {
       "email": "carlos@example.com",
       "telefono": "123456789"
   }
}
```

### 11.3 Biblioteca Jackson

**Jackson** es una biblioteca extremadamente popular y eficiente, diseñada originalmente para trabajar con JSON, aunque también tiene módulos que permiten procesar XML. Jackson es conocido por ser rápido, tanto en serialización como en deserialización.

> [!definition] Serializar y deserializar
> **Deserializar** significa transformar un archivo o una cadena de texto que contiene datos en un formato estructurado, como JSON o XML, en objetos que el programa puede usar directamente en memoria. Es el proceso inverso a la **serialización**, que convierte objetos en texto para almacenarlos o transmitirlos.

Podemos descargar los archivos `.jar` de [MVNRepository](https://mvnrepository.com/) (Maven Repository), que es el repositorio central más popular para proyectos Java. Funciona como una biblioteca universal donde se almacenan todas las librerías (dependencias) que podemos usar en nuestros proyectos Java.

Los archivos principales para trabajar con JSON en Jackson son:

- `jackson-databind`: tiene como dependencias `jackson-core` y `jackson-annotations`.
- `jackson-datatype-jsr310`: necesario si se utilizan fechas.

Para trabajar con ficheros XML, hacen falta las anteriores y además las siguientes:

- `jackson-dataformat-xml`: tiene como dependencias `woodstox-core` y `stax2-api`.

Para descargar cada uno, selecciona la última versión estable (Release) y descarga los archivos `.jar`. Crea una carpeta `lib` dentro del proyecto y copia los archivos `.jar`. A continuación, añádelos en el proyecto: en el Eclipse sitúate en el proyecto y en el botón derecho →_Build Path → Configure Build Path → Libraries → Classpath → Add JARs_.

Antes de usar Jackson para serializar o deserializar fechas, hay que registrar el módulo `JavaTimeModule`:

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

public class Main {
    public static void main(String[] args) {
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        // Ahora se puede serializar y deserializar fechas correctamente
    }
}
```

El siguiente código crea un fichero `json` con vehículos. A continuación, lee los vehículos del fichero `json` y los muestra por consola. Para que Jackson pueda deserializar, hay que añadir un constructor sin parámetros en la clase `Vehicle`. Dicho constructor vacío permite a Jackson crear una instancia de `Vehicle` sin necesidad de valores iniciales para sus atributos. Luego, Jackson puede llenar los valores individuales usando los datos del JSON:

```java
package tema1_Ficheros_ficherosJson;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import com.fasterxml.jackson.annotation.JsonFormat;

public class Vehicle {
    private int wheelCount;

    private double speed;

    private String colour;

    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate registrationDate;

    public Vehicle(int wheelCount, String colour, LocalDate registrationDate) {
        this.wheelCount = wheelCount;
        this.colour = colour;
        this.registrationDate = registrationDate;
        speed = 0;
    }

    // Constructor vacío (obligatorio para Jackson)
    public Vehicle() {
    }

    public int getWheelCount() {
        return wheelCount;
    }

    public double getSpeed() {
        return speed;
    }

    public LocalDate getRegistrationDate() {
        return registrationDate;
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
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return String.format("Número de ruedas: %d, color: %s, velocidad: %.2f, fecha de matriculación: %s", wheelCount, colour, speed, formatter.format(registrationDate));
    }
}
```

```java
package tema1_Ficheros_ficherosJson;

import java.io.*;
import java.nio.file.*;
import java.time.LocalDate;
import java.util.*;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

public class JsonFile {
    public void show() {
        Path file=Paths.get("files","vehicles.json");
        List<Vehicle> vehicles = generateVehicles();
        writeJson(file, vehicles);//Se escribe el fichero Json
        readJson(file);//Se lee el fichero Json
    }

    private List<Vehicle> generateVehicles(){
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle(4, "rojo", LocalDate.of(2020, 8, 22)));
        vehicles.add(new Vehicle(2, "azul", LocalDate.of(2022, 9, 7)));
        vehicles.add(new Vehicle(4, "blanco", LocalDate.of(2024, 2, 10)));
        vehicles.add(new Vehicle(2, "verde", LocalDate.of(2021, 3, 11)));
        vehicles.add(new Vehicle(2, "amarillo", LocalDate.of(2019, 5, 19)));
        for(int i=0;i<vehicles.size();i++) {
            vehicles.get(i).accelerate(i*50.25);
        }
        return vehicles;
    }

    private void writeJson (Path file, List<Vehicle> vehicles) {
        String json;
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        try {
            json = mapper.writeValueAsString(vehicles);//Devuelve una cadena con los datos de los vehículos en formato json
            Files.writeString(file, json);//Se escribe en el fichero la cadena que contiene el json
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }
    }

    private void readJson (Path file) {
        List<String> lines;
        String json;
        List<Vehicle> vehicles;
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        try {
            lines = Files.readAllLines(file);//Se leen las líneas del fichero
            /* String.join une todas las líneas en una sola usando cadena
             * vacía como separador, lo que significa que no habrá ningún
             * separador entre las líneas:  */
            json = String.join("", lines);
            vehicles = mapper.readValue(json, new TypeReference<List<Vehicle>>() {});//Lee la cadena que contiene el json y devuelve una lista con los vehículos leídos
            vehicles.forEach(System.out::println);
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new JsonFile().show();
    }
}
```

El fichero `json` generado es el siguiente:

```json
[{"wheelCount":4,"speed":0.0,"colour":"rojo","registrationDate":"22/08/2020"},{"wheelCount":2,"speed":50.25,"colour":"azul","registrationDate":"07/09/2022"},{"wheelCount":4,"speed":100.5,"colour":"blanco","registrationDate":"10/02/2024"},{"wheelCount":2,"speed":150.75,"colour":"verde","registrationDate":"11/03/2021"},{"wheelCount":2,"speed":201.0,"colour":"amarillo","registrationDate":"19/05/2019"}]
```

Si quisiéramos hacer lo mismo pero con un `xml`, nos saldría el siguiente fichero. Podemos observar que las etiquetas por defecto son `<ArrayList>` y `<item>`:

```xml
<ArrayList>
    <item>
        <wheelCount>4</wheelCount>
        <speed>0.0</speed>
        <colour>rojo</colour>
        <registrationDate>22/08/2020</registrationDate>
    </item>
    <item>
        <wheelCount>2</wheelCount>
        <speed>50.25</speed>
        <colour>azul</colour>
        <registrationDate>07/09/2022</registrationDate>
    </item>
    <item>
        <wheelCount>4</wheelCount>
        <speed>100.5</speed>
        <colour>blanco</colour>
        <registrationDate>10/02/2024</registrationDate>
    </item>
    <item>
        <wheelCount>2</wheelCount>
        <speed>150.75</speed>
        <colour>verde</colour>
        <registrationDate>11/03/2021</registrationDate>
    </item>
    <item>
        <wheelCount>2</wheelCount>
        <speed>201.0</speed>
        <colour>amarillo</colour>
        <registrationDate>19/05/2019</registrationDate>
    </item>
</ArrayList>
```

Para personalizar las etiquetas generadas en el XML al serializar con Jackson, hay que utilizar la anotación `@JacksonXmlRootElement` para la raíz del XML y `@JacksonXmlProperty` para los atributos y elementos. Estas anotaciones están disponibles en el paquete `com.fasterxml.jackson.dataformat.xml.annotation`. Dichas anotaciones hay que insertarlas en la clase `Vehicle`:

```java
package tema1_Ficheros_ficherosXml;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.dataformat.xml.annotation.*;

@JacksonXmlRootElement(localName = "Vehicle") // Etiqueta raíz personalizada
public class Vehicle {
    @JacksonXmlProperty(localName = "WheelCount") // Etiqueta personalizada para wheelCount
    private int wheelCount;

    @JacksonXmlProperty(localName = "Speed") // Etiqueta personalizada para speed
    private double speed;

    @JacksonXmlProperty(localName = "Colour") // Etiqueta personalizada para colour
    private String colour;

    @JacksonXmlProperty(localName = "RegistrationDate") // Etiqueta personalizada para registrationDate
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate registrationDate;

    public Vehicle(int wheelCount, String colour, LocalDate registrationDate) {
        this.wheelCount = wheelCount;
        this.colour = colour;
        this.registrationDate = registrationDate;
        speed = 0;
    }

    // Constructor vacío (obligatorio para Jackson)
    public Vehicle() {
    }

    public int getWheelCount() {
        return wheelCount;
    }

    public double getSpeed() {
        return speed;
    }

    public LocalDate getRegistrationDate() {
        return registrationDate;
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
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return String.format("Número de ruedas: %d, color: %s, velocidad: %.2f, fecha de matriculación: %s", wheelCount, colour, speed, formatter.format(registrationDate));
    }
}
```

Para indicar en el `xml` la lista de vehículos, si no queremos las etiquetas `<ArrayList>` y `</ArrayList>` que se generan por defecto, la lista se puede envolver en una clase `VehicleList` con una etiqueta personalizada para el nodo raíz:

```java
package tema1_Ficheros_ficherosXml;

import java.util.List;
import com.fasterxml.jackson.dataformat.xml.annotation.*;

@JacksonXmlRootElement(localName = "Vehicles") // Etiqueta raíz para la lista
public class VehicleList {
    @JacksonXmlElementWrapper(useWrapping = false) // Elimina el nodo "ArrayList"
    @JacksonXmlProperty(localName = "Vehicle") // Etiqueta para cada elemento. Si no se pone, coge el nombre del atributo: vehicles
    private List<Vehicle> vehicles;

    public VehicleList() {}

    public VehicleList(List<Vehicle> vehicles) {
        this.vehicles = vehicles;
    }

    public List<Vehicle> getVehicles() {
        return vehicles;
    }

    public void setVehicles(List<Vehicle> vehicles) {
        this.vehicles = vehicles;
    }
}
```

El siguiente código crea un fichero `xml` con vehículos. A continuación, lee los vehículos del fichero `xml` y los muestra por consola.

```java
package tema1_Ficheros_ficherosXml;

import java.io.*;
import java.nio.file.*;
import java.time.LocalDate;
import java.util.*;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

public class XmlFile {
    public void show() {
        Path file=Paths.get("files","vehicles.xml");
        VehicleList vehicleList = generateVehicles();
        writeXml(file, vehicleList);//Se escribe el fichero Xml
        readXml(file);//Se lee el fichero Xml
    }

    private VehicleList generateVehicles(){
        VehicleList vehicleList;
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle(4, "rojo", LocalDate.of(2020, 8, 22)));
        vehicles.add(new Vehicle(2, "azul", LocalDate.of(2022, 9, 7)));
        vehicles.add(new Vehicle(4, "blanco", LocalDate.of(2024, 2, 10)));
        vehicles.add(new Vehicle(2, "verde", LocalDate.of(2021, 3, 11)));
        vehicles.add(new Vehicle(2, "amarillo", LocalDate.of(2019, 5, 19)));
        for(int i=0;i<vehicles.size();i++) {
            vehicles.get(i).accelerate(i*50.25);
        }
        vehicleList = new VehicleList(vehicles);
        return vehicleList;
    }

    private void writeXml (Path file, VehicleList vehicleList) {
        XmlMapper xmlMapper = new XmlMapper();
        xmlMapper.registerModule(new JavaTimeModule());
        String xml;
        try {
            xml = xmlMapper.writeValueAsString(vehicleList);//Devuelve una cadena con los datos de los vehículos en formato xml
            Files.writeString(file, xml);//Se escribe en el fichero la cadena que contiene el xml
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s", e.getMessage());
        }
    }

    private void readXml (Path file) {
        List<String> lines;
        String xml;
        XmlMapper xmlMapper = new XmlMapper();
        xmlMapper.registerModule(new JavaTimeModule());
        List<Vehicle> vehicles;
        try {
            lines = Files.readAllLines(file);//Se leen las líneas del fichero
            /* String.join une todas las líneas en una sola usando cadena
             * vacía como separador, lo que significa que no habrá ningún
             * separador entre las líneas:  */
            xml = String.join("", lines);
            vehicles = xmlMapper.readValue(xml, new TypeReference<List<Vehicle>>() {});//Lee la cadena que contiene el xml y devuelve una lista con los vehículos leídos
            vehicles.forEach(System.out::println);
        } catch (FileNotFoundException e) {
            System.err.printf("El fichero no existe: %s",e.getMessage());
        } catch (IOException e) {
            System.err.printf("Error de entrada/salida: %s",e.getMessage());
        }
    }

    public static void main(String[] args) {
        new XmlFile().show();
    }
}
```

El fichero `xml` generado es el siguiente:

```xml
<Vehicles>
    <Vehicle>
        <WheelCount>4</WheelCount>
        <Speed>0.0</Speed>
        <Colour>rojo</Colour>
        <RegistrationDate>22/08/2020</RegistrationDate>
    </Vehicle>
    <Vehicle>
        <WheelCount>2</WheelCount>
        <Speed>50.25</Speed>
        <Colour>azul</Colour>
        <RegistrationDate>07/09/2022</RegistrationDate>
    </Vehicle>
    <Vehicle>
        <WheelCount>4</WheelCount>
        <Speed>100.5</Speed>
        <Colour>blanco</Colour>
        <RegistrationDate>10/02/2024</RegistrationDate>
    </Vehicle>
    <Vehicle>
        <WheelCount>2</WheelCount>
        <Speed>150.75</Speed>
        <Colour>verde</Colour>
        <RegistrationDate>11/03/2021</RegistrationDate>
    </Vehicle>
    <Vehicle>
        <WheelCount>2</WheelCount>
        <Speed>201.0</Speed>
        <Colour>amarillo</Colour>
        <RegistrationDate>19/05/2019</RegistrationDate>
    </Vehicle>
</Vehicles>
```

> [!tip] Resumen Jackson
> `ObjectMapper` (JSON) y `XmlMapper` (XML) funcionan igual: `writeValueAsString(objeto)` serializa y `readValue(texto, new TypeReference<List<Vehicle>>() {})` deserializa. La clase necesita un **constructor sin parámetros**, y las fechas `LocalDate` necesitan registrar `JavaTimeModule` (y `@JsonFormat` para fijar el patrón).

---

## Esquema

### Apartados 1–5: rutas y operaciones con ficheros

- Fichero = datos + nombre + extensión, gestionado por el SO mediante sistemas de archivos.
- API `java.nio.file` (Java 7): `Path` (ruta), `Paths` (fábrica de rutas), `Files` (operaciones).
- `Path` admite rutas relativas/absolutas; separador según SO; `resolve`, `toAbsolutePath`, `getFileName`, `getParent`, `isAbsolute`.
- `Files`: crear, existir, copiar, mover, borrar, tamaño y permisos — todo estático y con excepciones que hay que capturar.
- Excepciones: `IOException` (genérica) ⊃ `NoSuchFileException`, `FileAlreadyExistsException`.
- `Files.move` = mover + renombrar (mismo directorio → renombra); `StandardCopyOption.REPLACE_EXISTING` para sobrescribir; funciona con ficheros y directorios (aunque move de directorio arrastra todo su contenido, a diferencia de copy).
- `Files.list` → `Stream<Path>` (un nivel); `Files.walk` → recursivo. Ambos con **try-with-resources**: los recursos `AutoCloseable` se cierran solos al acabar el `try`, aunque haya excepción.

### Apartados 6–11: lectura y escritura

| Necesidad | Clases / métodos | Detalle clave |
| --- | --- | --- |
| Leer un texto entero | `Files.readAllLines` | Devuelve `List<String>`; sobrecarga con `StandardCharsets.UTF_8`. |
| Escribir texto | `Files.writeString`, `Files.write` | Por defecto `CREATE` + `TRUNCATE_EXISTING`; si pasas opciones, añádelas tú. |
| Texto línea a línea | `Files.newBufferedReader` / `newBufferedWriter` | `readLine()` devuelve `null` al final; `newLine()` para el salto. Buffer de 8 KB. |
| Texto carácter a carácter | `FileReader` / `FileWriter` | `read()` devuelve `-1` al final; `new FileWriter(f, true)` para añadir. |
| Trozos de un array | `read(cbuf, off, len)` / `write(cbuf, off, len)` | `off` = desplazamiento dentro del array, `len` = cuántos elementos. |
| Forzar la escritura | `flush()` | Necesario con buffer (`FileWriter`, `BufferedWriter`, `BufferedOutputStream`) si se lee antes de cerrar. |
| Bytes | `FileInputStream` / `FileOutputStream` | `read()` devuelve 0–255 o `-1` al final. |
| Tipos primitivos | `DataInputStream` / `DataOutputStream` | Leer en el mismo orden; fin con `EOFException`; `writeUTF` vs `writeChars`. |
| Objetos | `ObjectInputStream` / `ObjectOutputStream` | La clase implementa `Serializable`; para añadir, `AppendableObjectOutputStream`. |
| Acceso directo | `RandomAccessFile` (`"r"` / `"rw"`) | Registros de tamaño fijo + `seek((id - 1) * TAMAÑO)`. |
| XML / JSON | Jackson: `ObjectMapper` / `XmlMapper` | `writeValueAsString` / `readValue`; constructor vacío; anotaciones `@JacksonXml…`. |

## Relaciones

- Boletín 1 · Directorios: [[01.1 - Ejercicios 1 Directorios]]
- Boletín 1 · Ficheros de texto: [[01.2 - Ejercicios 1 Ficheros de texto]]
- Boletín 1 · Ficheros binarios: [[01.3 - Ejercicios 1 Ficheros binarios]]
- Boletín 1 · Ficheros binarios de objetos: [[01.4 - Ejercicios 1 Ficheros binarios de objetos]]
- Boletín 1 · Ficheros de acceso aleatorio: [[01.5 - Ejercicios 1 Ficheros de acceso aleatorio]]
- Normas de paquetes y clases: [[04 - Reglas de nomenclatura en los ejercicios]]
- Excepciones en Java (curso anterior): [[Programación basica/Tema 6/Excepciones|Programación básica → Excepciones]]
- Índice de la asignatura: [[DAM/Acceso_a_datos/Indice|Índice de Acceso a Datos]]

## Para repasar

- [ ] Construir rutas con `Paths.get` y `resolve` sin depender del separador del SO.
- [ ] Mover, renombrar y sobrescribir con `Files.move` y `REPLACE_EXISTING`.
- [ ] Listar directorios con `Files.list` / `Files.walk` dentro de un try-with-resources.
- [ ] Distinguir flujos de bytes (`InputStream`/`OutputStream`) y de caracteres (`Reader`/`Writer`).
- [ ] Saber qué opciones usan por defecto `writeString` y `write` y cuándo hay que añadir `CREATE`.
- [ ] Leer y escribir con arrays y desplazamiento (`off`, `len`).
- [ ] Explicar cuándo hace falta `flush` y cuándo no.
- [ ] Leer datos primitivos en el mismo orden en que se escribieron y detectar el final con `EOFException`.
- [ ] Serializar objetos y añadir al fichero sin duplicar la cabecera.
- [ ] Calcular el tamaño de un registro y posicionarse con `seek` en un `RandomAccessFile`.
- [ ] Serializar y deserializar una lista a JSON y XML con Jackson.
