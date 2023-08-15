def print1ToN(n):
    if n <= 1:
        print(1, end = " ")
        return
    if n < 0:
        print(1, end=" ")
        return
    print1ToN(n - 1)
    print(n, end=" ")


def printNto1(n):
    if n <= 1:
        print(1, end=" ")
        return
    if n < 0:
        print(1, end=" ")
        return
    print(n, end=" ")
    printNto1(n - 1)


inp = int(input("Enter Input : "))

print1ToN(inp)
printNto1(inp)
