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
- 9. Ficheros binarios
	- 9.1 FileInputStream y FileOutputStream
	- 9.2 DataInputStream y DataOutputStream
	- 9.3 ObjectInputStream y ObjectOutputStream
- 10. Ficheros de acceso aleatorio
- 11. Ficheros XML y JSON
	- 11.1 Ficheros XML
	- 11.2 Ficheros JSON
	- 11.3 Biblioteca Jackson

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

## Esquema

- Fichero = datos + nombre + extensión, gestionado por el SO mediante sistemas de archivos.
- API `java.nio.file` (Java 7): `Path` (ruta), `Paths` (fábrica de rutas), `Files` (operaciones).
- `Path` admite rutas relativas/absolutas; separador según SO; `resolve`, `toAbsolutePath`, `getFileName`, `getParent`, `isAbsolute`.
- `Files`: crear, existir, copiar, mover, borrar, tamaño y permisos — todo estático y con excepciones que hay que capturar.
- Excepciones: `IOException` (genérica) ⊃ `NoSuchFileException`, `FileAlreadyExistsException`.
- `Files.move` = mover + renombrar (mismo directorio → renombra); `StandardCopyOption.REPLACE_EXISTING` para sobrescribir; funciona con ficheros y directorios (aunque move de directorio arrastra todo su contenido, a diferencia de copy).
- `Files.list` → `Stream<Path>` (un nivel); `Files.walk` → recursivo. Ambos con **try-with-resources**: los recursos `AutoCloseable` se cierran solos al acabar el `try`, aunque haya excepción.

---

## 6. Flujos

Un flujo (o stream) se refiere al proceso de transferencia secuencial de datos entre dos fuentes, como un programa y un fichero, una red, una consola, etc. Un flujo puede ser de entrada (lectura) o de salida (escritura), dependiendo de la dirección en la que se transfieren los datos.

Existen dos categorías principales de flujos en Java: de bytes y de caracteres.

- **Flujos de bytes**: trabajan con datos binarios, transfiriéndolos en forma de bytes. Se utilizan para leer y escribir datos no textuales, como imágenes, vídeos o ficheros binarios.
  - Clases principales:
    - `InputStream`: lectura de bytes.
    - `OutputStream`: escritura de bytes.
- **Flujos de caracteres**: trabajan con datos textuales, transfiriendo caracteres (16 bits en Java para soportar Unicode). Se utilizan para leer y escribir texto.
  - Clases principales:
    - `Reader`: lectura de caracteres.
    - `Writer`: escritura de caracteres.

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
        
    
    Por defecto, `writeString` utiliza las opciones `CREATE` y `TRUNCATE_EXISTING`, es decir, si el archivo no existe, lo crea, y si ya existe, sobrescribe su contenido. Pero si se utiliza alguna opción, éstas dos opciones dejan de estar por defecto, entonces hay que añadirlas expresamente. Por ejemplo, si queremos utilizar `APPEND` en un bucle y queremos que en la primera iteración, el archivo se cree si no existe, pues entonces tendremos que poner `CREATE` y `APPEND`:
    

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

Tal y como ocurre con el método `writeString`, este método también utiliza las opciones `CREATE` y `TRUNCATE_EXISTING` por defecto, es decir, si el archivo no existe, lo crea, y si ya existe, sobrescribe su contenido. Igualmente, si se utiliza alguna opción, éstas dos opciones dejan de estar por defecto, entonces hay que añadirlas expresamente.

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

Un buffer es un espacio temporal en memoria (generalmente en RAM) que se utiliza para almacenar datos antes de que sean leídos o escritos. Este espacio permite agrupar varias operaciones de lectura o escritura en una sola operación de I/O, lo que es más eficiente que realizar muchas operaciones pequeñas directamente en el disco o en un flujo de entrada/salida.

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

Hay que tener en cuenta que `BufferedWriter` por sí misma no se encarga de crear el archivo., ya que su función principal es proporcionar un buffer para la escritura, mejorando el rendimiento. Sin embargo, al utilizar `BufferedWriter` junto con `FileWriter`, y dado que `FileWriter` crea el archivo si no existe, el archivo se generará automáticamente al escribir.

### 7.5 Operaciones con arrays y desplazamientos

En Java, los métodos que utilizan arrays, como `read(char[] cbuf)` o `write(char[] cbuf)`, permiten leer o escribir datos directamente en el array, actuando como un buffer temporal. Los arrays son útiles para almacenar datos en memoria y procesarlos de manera eficiente sin necesidad de trabajar con cada carácter o byte individualmente.

Además, existen métodos que permiten procesar partes específicas del array o buffer, como `read(char[] cbuf, int off, int len)` o `write(char[] cbuf, int off, int len)`. El parámetro `off` (abreviatura de _offset_) es el **desplazamiento**, es decir, define el punto de inicio dentro del array desde donde se empezará a leer o escribir, mientras que `len` indica la cantidad de elementos a procesar. Esto ofrece varias ventajas: eficiencia al evitar la necesidad de crear nuevos arrays o cargar grandes cantidades de datos en memoria, control preciso sobre las operaciones de entrada y salida y mejora del rendimiento en aplicaciones que manejan grandes volúmenes de datos, archivos grandes o transmisión en red.

#### 7.5.1 Lectura

Veamos los métodos de la clase `FileReader` para leer caracteres de un fichero. También existen estos métodos en la clase `BufferedReader` por si al programador le interesara utilizar los beneficios de una clase con buffer:

|Método|Descripción|
|---|---|
|`int read()`|Lee un solo carácter y devuelve su valor Unicode como un entero. Devuelve `-1` al final del fichero.|
|`int read(char[] cbuf)`|Lee caracteres del fichero y los introduce en el array `cbuf` hasta llenarlo o hasta que se alcance el final del fichero. Devuelve el número de caracteres leídos o `-1` si no hay más datos.|
|`int read(char[] cbuf, int off, int len)`|Lee `len` caracteres del fichero y los almacena en `cbuf` a partir de la posición `off`. Devuelve el número de caracteres leídos o `-1` si se llega al final del fichero.|

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

|Método|Descripción|
|---|---|
|`void write(int c)`|Escribe el carácter `c` en el fichero.|
|`void write(char[] cbuf)`|Escribe el array de caracteres `cbuf` en el fichero.|
|`void write(char[] cbuf, int off, int len)`|Escribe en el fichero `len` caracteres del array, desde el índice `off`.|
|`void write(String str)`|Escribe la cadena `str` en el fichero.|
|`void write(String str, int off, int len)`|Escribe en el fichero `len` caracteres de la cadena `str`, desde el índice `off`.|

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
    

Por lo tanto, si al leer un fichero antes de cerrar el flujo o hacer un `flush`, es posible que no se vea el contenido completo, ya que puede estar aún en el buffer y por lo tanto, no se ha escrito todavía físicamente en el fichero.

En el caso de los métodos de la clase `Files` como `write` y `writeString`, estos métodos realizan la escritura de forma inmediata en el fichero, ya que trabajan de manera más sencilla y no utilizan un buffer interno de la misma forma que `FileWriter` o `BufferedWriter`, por lo que no hay que preocuparse por llamar a `flush` o `close`.

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
