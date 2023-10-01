def binary_search(left, right, arr, target):
    mid = (left + right) // 2
    if left > right:
        return False
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1
    return binary_search(left, right, arr, target)
