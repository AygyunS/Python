def binary_search(arr, left, right, x):
    if left >= right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == x:
        return mid

    elif arr[mid] > x:
        return binary_search(arr, left, mid-1, x)

    else:
        return binary_search(arr, mid+1, right, x)


arr = [1, 3, 5, 7, 9]
left = 0
right = len(arr) - 1
x = 5

index = binary_search(arr, left, right, x)
print(index)
