def find_three_sum(arr, target = 5):
    l = len(arr)
    if l < 3:
        return "Array Input Length Must More Than 2"

    result = []
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                new_arr = [arr[i], arr[j], arr[k]]
                if sum(new_arr) == target and new_arr not in result:
                    result.append(new_arr)

    return result


array = [int(n) for n in input('Enter Your List : ').split(' ')]
print(find_three_sum(array, 0))
