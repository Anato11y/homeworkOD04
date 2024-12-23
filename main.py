# O(n^2) - квадратичная сложность в худшем и среднем случаях
# O(n) - линейная сложность в лучшем случае (если массив уже отсортирован)
# Реализация пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Пример использования пузырьковой сортировки
arr = [5, 7, 4, 3, 8, 2]
bubble_sort(arr)
print(arr)

# O(n log n) - средняя временная сложность
# O(n^2) - худший случай (при плохом выборе опорного элемента)
# Реализация быстрой сортировки
def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))
    return quick_sort(left) + center + quick_sort(right)

# Пример использования быстрой сортировки
arr = [5, 2, 9, 0, 1, 5, 3]
print(quick_sort(arr))

# O(n^2) - квадратичная сложность во всех случаях
# Реализация сортировки выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования сортировки выбором
arr = [-3, 5, 0, -8, 1, 10]
selection_sort(arr)
print(arr)

# O(n^2) - квадратичная сложность в худшем и среднем случаях
# O(n) - линейная сложность в лучшем случае (если массив почти отсортирован)
# Реализация сортировки вставками
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Пример использования сортировки вставками
arr = [-3, 5, 0, -8, 1, 10]
insert_sort(arr)
print(arr)
