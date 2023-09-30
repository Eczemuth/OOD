g_index = 0


def merge_sort(arr):
    global g_index
    g_index += 1
    if len(arr) < 2:
        return arr

    half1_len = len(arr)//2
    local_res = []
    left_arr = merge_sort(arr[:half1_len])
    right_arr = merge_sort(arr[half1_len:])
    while left_arr and right_arr:
        n1, n2 = left_arr[0], right_arr[0]
        if n1 < n2:
            local_res.append(left_arr.pop(0))
        else:
            local_res.append(right_arr.pop(0))

    if left_arr:
        local_res.extend(left_arr)
    if right_arr:
        local_res.extend(right_arr)
    return local_res


import random

testcases = [[random.randint(-50, 50) for _ in range(random.randint(5, 15))] for _ in range(20)]

for nums_arr in testcases:
    print(merge_sort(nums_arr) == sorted(nums_arr))

