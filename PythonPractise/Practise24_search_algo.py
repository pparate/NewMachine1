arr = [1,2,3,4,5,6,7,8,9]


# linear search
def search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1


print(search(arr, 10))


# binary search

def bina(arr, ele, start, end):
    if start > end:
        return -1

    mid = start + (end - start) // 2
    if arr[mid] == ele:
        return mid
    elif ele < arr[mid]:
        return bina(arr, ele, start, mid - 1)
    else:
        return bina(arr, ele, mid + 1, end)


print(bina(arr, 1, 0, len(arr)-1))
