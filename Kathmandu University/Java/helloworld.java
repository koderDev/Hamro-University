import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine().trim();
        if (name.isEmpty()) {
            System.out.println("Hello, World from Java!");
        } else {
            System.out.printf("Hello, %s! Welcome to Java.%n", name);
        }
        scanner.close();
    }
}
