class MyInt:
    def __init__(self, val):
        self.val = val

    def __isPrime(self, n):
        if (n <= 1):
            return False

            # Check from 2 to sqrt(n)
        for i in range(2, int(n ** (1/2)) + 1):
            if (n % i == 0):
                return False

        return True

    def isPrime(self):
        return self.__isPrime(self.val)

    def showPrime(self):
        if self.val < 2:
            return '!!!A prime number is a natural number greater than 1'
        s = ''
        for n in range(self.val + 1):
            if self.__isPrime(n):
                s += str(n) + ' '

        return s

    def __sub__(self, other):
        return self.val - other.val // 2


print(' *** class MyInt ***')
n1, n2 = [int(x) for x in input('Enter 2 number : ').split()]

a = MyInt(n1)
b = MyInt(n2)

print(n1, 'isPrime :', a.isPrime())
print(n2, 'isPrime :', b.isPrime())
print(f'Prime number between {2} and {n1} :', a.showPrime())
print(f'Prime number between {2} and {n2} :', b.showPrime())
print(f'{n1} - {n2} =', a-b)