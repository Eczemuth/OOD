print('*** multiplication or sum ***')
a, b = [int(x) for x in input('Enter num1 num2 : ').split()]
res = a + b if a * b > 1000 else a * b
print('The result is', res)