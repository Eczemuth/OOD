def bi_search(left, right, arr, target):
    mid = (left + right) // 2
    # print(left, right, arr, mid, arr[mid])
    if left > right:
        return False
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1
    return bi_search(left, right, arr, target)


inp = input('Enter Input : ').split('/')
collection, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(collection) - 1, sorted(collection), k))
