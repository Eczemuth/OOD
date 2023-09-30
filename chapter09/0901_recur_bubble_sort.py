def bubble_sort(arr, i=-1):
    if i + 1 < len(arr):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        bubble_sort(arr, i + 1)
        bubble_sort(arr, i + 1)
    return arr


inp = [int(e) for e in input('Enter Input : ').split()]
print(bubble_sort(inp))
