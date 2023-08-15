def my_pow(x, n):
    if n == 0:
        return 1
    x *= my_pow(x, abs(n) - 1)
    return 1 / x if n < 0 else x


val, n = [int(x) for x in input("Enter Input a b : ").split()]
my_pow(val, n)
print(my_pow(val, n))
