# bubble sort


arr = [4, 7, 3, 8, 5, 9]


def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


bubble(arr)
print(arr)
arr = [4, 7, 3, 8, 5, 9]


def selection(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp


selection(arr)
print(arr)