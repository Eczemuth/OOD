def swap(arr, index):
    if arr[index] < arr[index - 1] and index > 0:
        arr[index], arr[index - 1] = arr[index - 1], arr[index]
        return swap(arr, index - 1)
    return index


def insertion_sort(arr, index, max_index):
    if index > max_index:
        return
    print(f"insert {arr[index]} at index {swap(arr, index)} :", arr[:index+1], arr[index+1:] if arr[index+1:] else '')
    insertion_sort(arr, index + 1, max_index)


inp = [int(e) for e in input('Enter Input : ').split()]
# inp = [int(e) for e in '4 3 2 1'.split()]
# inp = [int(e) for e in '1 3 4 2'.split()]
insertion_sort(inp, 1, len(inp) - 1)
print('sorted')
print(inp)
