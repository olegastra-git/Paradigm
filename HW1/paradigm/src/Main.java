import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите список целых чисел через запятую: ");
        String input = scanner.nextLine();

        String[] numbersArray = input.split(",");
        int[] numbers = new int[numbersArray.length];

        for (int i = 0; i < numbersArray.length; i++) {
            numbers[i] = Integer.parseInt(numbersArray[i]);
        }

        bubbleSortDescending(numbers);

        System.out.println("Числа, отсортированные в порядке убывания:");

        for (int number : numbers) {
            System.out.print(number + " ");
        }
    }

    private static void bubbleSortDescending(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] < arr[j + 1]) {
                    // меняем элементы местами
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}