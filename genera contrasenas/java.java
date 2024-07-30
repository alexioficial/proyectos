public class java {
    public static void main(String args[]) {
        System.out.println("Su contrasena es: ");
        System.out.println(generaContrasena());
    }

    static String generaContrasena() {
        char[] mayusculas = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' };
        char[] minusculas = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' };
        char[] numeros = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' };
        char[] especial = { '!', '@', '#', '$', '%', '^', '&', '*', '/' };

        StringBuilder caracteres = new StringBuilder();
        caracteres.append(mayusculas);
        caracteres.append(minusculas);
        caracteres.append(numeros);
        caracteres.append(especial);

        StringBuilder contrasena = new StringBuilder();

        for (int i = 0; i <= 25; i++) {
            int cantidadCaracteres = caracteres.length();
            int numeroRandom = (int) (Math.random() * cantidadCaracteres);

            contrasena.append((caracteres.toString()).charAt(numeroRandom));
        }

        return contrasena.toString();
    }
}