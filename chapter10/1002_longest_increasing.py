data = [int(e) for e in input('Data : ').split()]
# data = [int(e) for e in '9 26 22 75 47'.split()]
# data = [int(e) for e in '1 52 28 25 40 64 84 28 77 46'.split()]
res = 0
index = seq = 1
stack = []

for n in data:
    if stack:
        while stack[-1] >= n:
            stack.pop(-1)
            if not stack:
                break
    stack.append(n)
    print(index, stack, sep=" : ")
    res = max(res, len(stack))
    index += 1

print('longest increasing subsequence :', res)
