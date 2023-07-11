class Stack:
    def __init__(self):
        self.__stack = []

    def __repr__(self):
        temp = [str(e) for e in self.__stack[::]]
        return '[' + ','.join(temp) + ']'

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        if not self.__stack:
            return None
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

    def isEmpty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

    def peek(self):
        if not self.__stack:
            return None
        return self.__stack[-1]


def postFixEval(postfix):
    stack = Stack()
    OPERATOR = "+-*/"
    for val in postfix:
        if val not in OPERATOR:
            stack.push(val)
        else:
            b = stack.pop()
            a = stack.pop()
            operator = val
            infix = a + operator + b
            stack.push(str(eval(infix)))

    return float(stack.pop())


# missed type at calcuation na krub
print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixEval(token)))
