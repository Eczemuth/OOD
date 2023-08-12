def is_collide(l_ast, r_ast):
    return l_ast > 0 and r_ast < 0


def asteroid_collision(asts, index = -1):
    # print(index, len(asts), asts)
    if len(asts) + index <= 0:
        # print(asts)
        return asts
    if is_collide(asts[index - 1], asts[index]):
        factor = 0
        if abs(asts[index - 1]) > abs(asts[index]):
            asts.pop(index)
        elif abs(asts[index - 1]) < abs(asts[index]):
            asts.pop(index - 1)
        else:
            asts.pop(index)
            asts.pop(index)
            factor = 2
        if index != -1:
            return asteroid_collision(asts, -1)
        return asteroid_collision(asts, index - factor)
        # print(asts)
    else:
        return asteroid_collision(asts, index - 1)


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))
