import java.text.DecimalFormat;
import java.util.Arrays;

public class StudentGrades {
    public static void main(String[] args) {
        String[] students = {"Aarav", "Bina", "Chhaya", "Dipesh"};
        int[] marks = {82, 91, 76, 88};

        System.out.println("Student Grades Summary");
        System.out.println("-----------------------");
        for (int i = 0; i < students.length; i++) {
            System.out.printf("%s: %d%n", students[i], marks[i]);
        }

        double average = Arrays.stream(marks).average().orElse(0.0);
        int maxMark = Arrays.stream(marks).max().orElse(0);
        int minMark = Arrays.stream(marks).min().orElse(0);

        DecimalFormat formatter = new DecimalFormat("0.00");
        System.out.println();
        System.out.println("Class Average: " + formatter.format(average));
        System.out.println("Highest Mark: " + maxMark);
        System.out.println("Lowest Mark: " + minMark);
    }
}
