import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TodoApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> tasks = new ArrayList<>();
        boolean running = true;

        System.out.println("Simple Todo App");
        while (running) {
            System.out.println();
            System.out.println("1) Add task");
            System.out.println("2) List tasks");
            System.out.println("3) Complete task");
            System.out.println("4) Exit");
            System.out.print("Choose an option: ");

            String choice = scanner.nextLine().trim();
            switch (choice) {
                case "1":
                    System.out.print("Enter task description: ");
                    String task = scanner.nextLine().trim();
                    if (!task.isEmpty()) {
                        tasks.add(task);
                        System.out.println("Task added.");
                    } else {
                        System.out.println("Cannot add empty task.");
                    }
                    break;
                case "2":
                    if (tasks.isEmpty()) {
                        System.out.println("No tasks yet.");
                    } else {
                        System.out.println("Current tasks:");
                        for (int i = 0; i < tasks.size(); i++) {
                            System.out.printf("%d) %s%n", i + 1, tasks.get(i));
                        }
                    }
                    break;
                case "3":
                    if (tasks.isEmpty()) {
                        System.out.println("Nothing to complete.");
                        break;
                    }
                    System.out.print("Enter task number to complete: ");
                    try {
                        int index = Integer.parseInt(scanner.nextLine().trim());
                        if (index >= 1 && index <= tasks.size()) {
                            String removed = tasks.remove(index - 1);
                            System.out.println("Completed: " + removed);
                        } else {
                            System.out.println("Invalid task number.");
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Please enter a valid number.");
                    }
                    break;
                case "4":
                    running = false;
                    break;
                default:
                    System.out.println("Unknown option. Try again.");
            }
        }

        System.out.println("Goodbye!");
        scanner.close();
    }
}
