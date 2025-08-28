nums = [10, 2, 1, 4, 7, 8]
n = len(nums)


def bubbleSort(arr, n):

    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# print(bubbleSort(arr, n))


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


def merge(nums, l, mid, r):
    # a = nums[l : mid + 1]
    # b = nums[mid + 1 : r]

    a = []
    b = []

    for i in range(l, mid + 1):
        a.append(nums[i])
    for i in range(mid + 1, r + 1):
        b.append(nums[i])

    n, m = len(a), len(b)

    i, j, k = 0, 0, l

    while i < n and j < m:
        if a[i] <= b[j]:
            nums[k] = a[i]
            i += 1
        else:
            nums[k] = b[j]
            j += 1
        k += 1

    if i < n:
        while i < n:
            nums[k] = a[i]
            i += 1
            k += 1
    if j < m:
        while j < m:
            nums[k] = b[j]
            j += 1
            k += 1


def mergeSort(nums, l, r):
    if l >= r:
        return

    mid = (l + r) // 2

    mergeSort(nums, l, mid)
    mergeSort(nums, mid + 1, r)

    merge(nums, l, mid, r)

    return nums


# print(mergeSort(nums, 0, len(nums) - 1))


def partition(nums, l, r):
    pivot = nums[r]
    start = l

    for i in range(l, r):
        if pivot >= nums[i]:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
    nums[start], nums[r] = nums[r], nums[start]

    return start


def quickSort(nums, l, r):
    if l >= r:
        return

    p = partition(nums, l, r)
    quickSort(nums, l, p - 1)
    quickSort(nums, p + 1, r)

    return nums


print(quickSort(nums, 0, len(nums) - 1))


