import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Sort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите список целых чисел через запятую: ");
        String input = scanner.nextLine();

        String[] numbersArray = input.split(",");
        Integer[] numbers = new Integer[numbersArray.length];

        for (int i = 0; i < numbersArray.length; i++) {
            numbers[i] = Integer.parseInt(numbersArray[i]);
        }

        List<Integer> numbersList = Arrays.asList(numbers);
        Collections.sort(numbersList, Collections.reverseOrder());

        System.out.println("Числа, отсортированные в порядке убывания:");

        for (int number : numbersList) {
            System.out.print(number + " ");
        }
    }
}