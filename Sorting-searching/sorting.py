arr = [10, 2, 1, 4, 7, 8]
n = len(arr)


def bubbleSort(arr, n):

    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubbleSort(arr, n))


def selectionSort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# print(selectionSort(arr, n))


def insertionSort(arr, n):

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


# print(insertionSort(arr, n))
