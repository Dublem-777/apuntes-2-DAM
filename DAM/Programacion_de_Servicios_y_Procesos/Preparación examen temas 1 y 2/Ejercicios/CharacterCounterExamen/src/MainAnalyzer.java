import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class MainAnalyzer {

    private final List<String> text;

    public MainAnalyzer() {
        //Lista de cadenas que simula el texto a analizar
        text = List.of(
                "En un lugar de la Mancha",
                "de cuyo nombre no quiero acordarme",
                "no ha mucho tiempo que vivía un hidalgo"
        );
    }

    //Construye el comando portable: java -cp <classpath> CharacterCounter <modo>
    public List<String> buildCommand(String mode) {
        String javaPath = System.getProperty("java.home") + File.separator + "bin" + File.separator + "java";

        //Ruta absoluta: si el hijo cambia de directorio, un classpath relativo dejaría de valer
        String classPath = new File(System.getProperty("java.class.path")).getAbsolutePath();

        List<String> command = new ArrayList<>();
        command.add(javaPath);
        command.add("-cp");
        command.add(classPath);
        command.add("CharacterCounter");
        command.add(mode);
        return command;
    }

    //Contador de vocales: stderr compartido con el padre y DEBUG_MODE=TRUE
    public ProcessBuilder configureVowelCounter() {
        ProcessBuilder pb = new ProcessBuilder(buildCommand("vowels"));
        pb.redirectError(ProcessBuilder.Redirect.INHERIT);
        pb.environment().put("DEBUG_MODE", "TRUE");
        return pb;
    }

    //Contador de consonantes: directorio ./logs y stderr a un fichero
    public ProcessBuilder configureConsonantsCounter() {
        ProcessBuilder pb = new ProcessBuilder(buildCommand("consonants"));
        File logs = new File("./logs");
        logs.mkdir();
        pb.directory(logs);
        pb.redirectError(new File(logs, "consonant_err.log"));
        return pb;
    }

    //Envía cada cadena como una línea y CIERRA la entrada del hijo
    public void sendLines(Process process, List<String> lines) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream(), StandardCharsets.UTF_8))){
            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }
        }
    }

    //Lee la línea del resultado que escribe el hijo en su stdout
    public String readResult(Process process) throws IOException {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8))) {
            return reader.readLine();
        }
    }

    public int waitAndGetExitCode(Process process) throws InterruptedException {
        return process.waitFor();
    }

    //Arrancar el programa
    public void run() {
        try {
            Process vowels = configureVowelCounter().start();
            Process consonants = configureConsonantsCounter().start();

            System.out.println("PID vowel counter: " + vowels.pid());
            System.out.println("PID consonant counter: " + consonants.pid());

            sendLines(vowels, text);
            sendLines(consonants, text);

            String vowelResult = readResult(vowels);
            String consonantResult = readResult(consonants);

            int vowelExit = waitAndGetExitCode(vowels);
            int consonantExit = waitAndGetExitCode(consonants);

            System.out.println("Vowel Result: " + vowelResult);
            System.out.println("Consonant Result: " + consonantResult);
            if (vowelExit == 0 && consonantExit == 0) {
                System.out.println("Ambos procesos terminaron con éxito");
            } else {
                System.out.println("Algún proceso falló (vowels=" + vowelExit + ", consonants=" + consonantExit + ").");
            }
        } catch (IOException e) {
            System.err.println("Error de E/S: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("Se interrumpió la espera");
        }
    }

    public static void main(String[] args) {
        new MainAnalyzer().run();
    }
}
