class Pair:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __repr__(self):
        return f'({self.num1},{self.num2})'

    def __lt__(self, other):
        # return self.num1 < other.num1 and self.num2 > other.num2
        return self.num1 < other.num1

    def __le__(self, other):
        return self.num1 >= other.num1 and self.num2 <= other.num2


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


pairs = []
inp = [int(e) for e in input('input : ').split()]
# inp = [int(e) for e in '16 1 4 7 14 11 19 15 3 8'.split()]
[pairs.append(Pair(inp[i - 1], inp[i])) for i in range(1, len(inp), 2)]
pairs = merge_sort(pairs, True)
# print(pairs)
res = 0

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[i].num2 < pairs[j].num2:
            # print(pairs[i], pairs[j])
            res += pairs[i].num1 + pairs[j].num1


print('ans =', res)
