
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Введите число: "))
index = binary_search(arr, target)
if index != -1:
    print(f"Искомый элемент найден на позиции {index}")
else:
    print("Искомый элемент не найден")