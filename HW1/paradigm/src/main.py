def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = input("Введите список целых чисел через запятую: ").split(",")
numbers = [int(num) for num in numbers]
bubble_sort_descending(numbers)
print("Числа, отсортированные в порядке убывания:")
for number in numbers:
    print(number, end=" ")
