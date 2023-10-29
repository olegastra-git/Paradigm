def main():
    input_list = input("Введите список целых чисел через запятую: ")
    numbers = [int(num) for num in input_list.split(",")]

    numbers_list = sorted(numbers, reverse=True)

    print("Числа, отсортированные в порядке убывания:")
    for number in numbers_list:
        print(number, end=" ")

if __name__ == "__main__":
    main()
