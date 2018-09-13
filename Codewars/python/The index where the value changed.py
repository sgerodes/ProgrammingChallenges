def changed(arr):
    if not arr or arr[0] == arr[-1]:
        return None
    return binary_search(arr, 0, len(arr)-1)


def binary_search(arr, left, right):
    mid = right - (right - left) // 2
    if not arr[mid] == arr[mid - 1]:
        return mid
    if arr[mid] == arr[0]:
        return binary_search(arr, mid, right)
    else:
        return binary_search(arr, left, mid)
