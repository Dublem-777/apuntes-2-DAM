import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class CharacterCounter {
    private static final String VOWELS = "aeiouáéíóúAEIOUÁÉÍÓÚ";

    private String mode;
    private boolean debug;

    //Comprueba que llega exactamente un argumento válido
    public boolean validateArgs(String[] args) {
        if (args.length != 1) {
            return false;
        }
        return args[0].equals("vowels") || args[0].equals("consonants");
    }

    //Lee la variable de entorno DEBUG_MODE
    public boolean isDebug() {
        String value = System.getenv("DEBUG_MODE");
        return value != null && value.equals("TRUE");
    }

    //Cuenta las vocales de una línea
    public int countVocals(String line) {
        int count = 0;
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if ((Character.isLetter(c) && VOWELS.indexOf(c) >= 0)) {
                count++;
            }
        }
        return count;
    }

    //Cuenta las consonantes: letras que NO son vocales
    public int countConsonants(String line) {
        int count = 0;
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if ((Character.isLetter(c) && VOWELS.indexOf(c) < 0)) {
                count ++;
            }
        }
        return count;
    }

    //Bucle principal: lee de stdin hasta que el padre cierre la tubería
    public int processInput() throws IOException {
        int total = 0;
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
        String line;
        while ((line = input.readLine()) != null) {
            int count = mode.equals("vowels") ? countVocals(line) : countConsonants(line);
            total += count;
            if (debug) {
                System.err.printf("[PID: %d] Line parsed. Found %d %s%n", ProcessHandle.current().pid(), count, mode);
            }
        }
        return total;
    }

    //Arrancar el programa
    public void run(String[] args) {
        if (!validateArgs(args)) {
            System.err.println("Error: Invalid mode");
            System.exit(1);
        }
        mode = args[0];
        debug = isDebug();
        try {
            int total = processInput();
            System.out.println("Total" + mode + ": " + total);
            System.exit(0);
        } catch (IOException e) {
            System.err.println("Error de lectura: " + e.getMessage());
            System.exit(1);
        }
    }

    public static void main (String[] args) {
        new CharacterCounter().run(args);
    }
}