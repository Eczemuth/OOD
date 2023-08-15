def recursion_sort(arr, l_arr=-1, i=-1):
    if i == l_arr - 1:
        return
    if l_arr == -1:
        l_arr = len(arr)
    recursion_sort(arr, l_arr, i + 1)
    if arr[i] < arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursion_sort(arr, l_arr, i + 1)

    return arr


inp = input("Enter your List : ")
print("List after Sorted :", recursion_sort([int(e) for e in inp.split(',')]))
