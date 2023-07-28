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

    def is_empty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

    def peek(self):
        if not self.__stack:
            return None
        return self.__stack[-1]


def change_drunk(h, drunk):
    if h % 2 == 0:
        h -= 1
        h += 2*(drunk - 1)
    else:
        h += 2*drunk
    return h


def count_trees(trees):
    stack = Stack()
    for tree in trees:
        try:
            action, h = tree.split()
        except ValueError:
            h = None
            action = tree

        if action == 'A':
            h = int(h)
            stack.push(h)

        elif action == 'B':
            temp = Stack()
            tree_found = 0
            most_height = 0

            while not stack.is_empty():
                curr_h = stack.pop()
                temp.push(curr_h)
                if curr_h > most_height:
                    tree_found += 1
                    most_height = curr_h

            while not temp.is_empty():
                stack.push(temp.pop())

            print(tree_found)

        elif action == 'S':
            temp_stack = Stack()
            while not stack.is_empty():
                val = stack.pop()
                if val % 2 == 0:
                    val -= 1
                    if val < 1:
                        val = 1
                else:
                    val += 2
                temp_stack.push(val)

            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())


command = input('Enter Input : ').split(',')
count_trees(command)
