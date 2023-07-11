class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        temp = [str(e) for e in self.stack[::]]
        return '[' + ','.join(temp) + ']'

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]


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

            while not stack.isEmpty():
                curr_h = stack.pop()
                temp.push(curr_h)
                if curr_h > most_height:
                    tree_found += 1
                    most_height = curr_h

            while not temp.isEmpty():
                stack.push(temp.pop())

            print(tree_found)

        elif action == 'S':
            for i in range(stack.size()):
                if stack.stack[i] % 2 == 0:
                    stack.stack[i] -= 1
                    if stack.stack[i] < 1:
                        stack.stack[i] = 1
                else:
                    stack.stack[i] += 2


command = input('Enter Input : ').split(',')
count_trees(command)
