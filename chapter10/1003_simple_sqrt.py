def sqrt(low, high, num):
    if low > high or high == 0 or high == 1:
        return high
    # print(low, high)
    mid = (high + low) // 2
    if mid * mid > num:
        high = mid - 1
    else:
        low = mid + 1
    return sqrt(low, high, num)


n = int(input("simple sqrt: "))
# n = 9
print(sqrt(1, n, n))
