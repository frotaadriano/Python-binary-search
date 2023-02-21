def binary_search(arr, x):
    """
    Perform a binary search for the element x in the sorted array arr.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6

index = binary_search(arr, x)
if index == -1:
    print(f"{x} was not found in the array.")
else:
    print(f"{x} was found at index {index} in the array.")
