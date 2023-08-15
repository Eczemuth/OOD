def combination(array, res_list=None, start=0, size=1):
    if start == len(array):
        return
    if not res_list:
        res_list = []
    if start + size <= len(array):
        res_list.append(array[start:start + size])
        combination(array, res_list, start, size + 1)
    else:
        combination(array, res_list, start + 1, 1)
    return res_list


def find_flavor(breads, y_sour, y_bitter, index=0):
    if index == len(breads) - 1:
        return breads[index][0], breads[index][1]
    sour, bitter = find_flavor(breads, y_sour, y_bitter, index + 1)
    return y_sour * sour * breads[index][0], y_bitter + bitter + breads[index][1]


def perket(bread_list_combi, bread_list_index=0, min_diff=1000000001):
    if bread_list_index == len(bread_list_combi):
        return min_diff
    y_sour, y_bitter = find_flavor(bread_list_combi[bread_list_index], 1, 0)
    diff = abs(y_sour - y_bitter)
    using_diff = min_diff
    if diff <= min_diff:
        using_diff = diff
    min_diff = perket(bread_list_combi, bread_list_index + 1, using_diff)
    return min_diff


inp = [[int(flv) for flv in bread.split()] for bread in input("Enter Input : ").split(",")]
bread_combi = combination(inp)
print(perket(bread_combi))
