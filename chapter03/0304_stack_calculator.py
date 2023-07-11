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
            return 0
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

    def isEmpty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

    def peek(self):
        if not self.__stack:
            return 0
        return self.__stack[-1]


class StackCalc:
    def __init__(self):
        self.OPERATOR = ['+', '-', '*', '/', 'DUP', 'PSH', 'POP']
        self.val = 0
        self.stack = Stack()

    def run(self, expr):
        for val in expr:
            if val.isnumeric():
                self.stack.push(val)
            elif val not in self.OPERATOR:
                self.val = f"Invalid instruction: {val}"
                return
            else:
                if val in '+-*/':
                    a = self.stack.pop()
                    b = self.stack.pop()
                    operator = val
                    infix = a + operator + b
                    self.stack.push(str(int(eval(infix))))
                else:
                    if val == 'DUP':
                        self.stack.push(self.stack.peek())
                    elif val == 'PSH':
                        pass
                    elif val == 'POP':
                        self.stack.pop()
            self.val = self.stack.peek()

    def getValue(self):
        return self.val


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
