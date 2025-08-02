arr = [1, 4, 6, 8, 23, 29, 59]  
target = 1
n = len(arr)


def binary(arr, n, target):

    start = 0
    end = n - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1

    return mid


print(binary(arr, n, target))


def Linear(arr, n, target):
    i = 0
    while n != 0:
        if arr[i] == target:
            return i
        i = i + 1


print(Linear(arr, n, target))
