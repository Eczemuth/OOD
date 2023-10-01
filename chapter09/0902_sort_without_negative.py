def merge_sort(arr, reverse=False):
    if len(arr) < 2:
        return arr

    half1_len = len(arr) // 2
    local_res = []
    left_arr = merge_sort(arr[:half1_len], reverse)
    right_arr = merge_sort(arr[half1_len:], reverse)

    while left_arr and right_arr:
        n1, n2 = left_arr[0], right_arr[0]
        if reverse:
            if n1 > n2:
                local_res.append(left_arr.pop(0))
            else:
                local_res.append(right_arr.pop(0))
        else:
            if n1 < n2:
                local_res.append(left_arr.pop(0))
            else:
                local_res.append(right_arr.pop(0))
    if left_arr:
        local_res.extend(left_arr)
    if right_arr:
        local_res.extend(right_arr)
    return local_res


def negative_inplace(arr):
    without_negative = []
    for e in arr:
        if e >= 0:
            without_negative.append(e)

    # O(n log n)
    # print(without_negative)
    without_negative = merge_sort(without_negative)
    # print(without_negative)

    # O(n + n log n) still O(n log n)
    j = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[i] = without_negative[j]
            j += 1


inp = [int(e) for e in input('Enter Input : ').split()]
# inp = [int(e) for e in '6 3 -2 5 -8 2 -2'.split()]
negative_inplace(inp)
print(*inp)

