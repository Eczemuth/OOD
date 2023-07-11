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


def check_parenthesis(expr):
    open_p = ["(", "["]
    close_p = [")", "]"]
    count_open = len([c for c in expr if c in open_p])
    count_close = len([c for c in expr if c in close_p])

    if len(expr) == 0 or count_open != count_close:
        return "Parentheses : Unmatched ! ! !"

    else:
        inv_pair = {")": "(", "]": "[", "}": "{"}
        s = Stack()
        for p in expr:
            if s.isEmpty():
                s.push(p)
                continue

            match = False
            if p in inv_pair:
                match = s.peek() == inv_pair[p]

            if match:
                s.pop()
            else:
                s.push(p)

        if s.isEmpty():
            return "Parentheses : Matched ! ! !"
        else:
            return "Parentheses : Unmatched ! ! !"


expr = input("Enter Input : ")
print(check_parenthesis(expr))
