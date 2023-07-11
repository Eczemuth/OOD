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


class Dish:
    def __init__(self, weight, freq):
        self.weight = weight
        self.freq = freq

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"w : {self.weight} freq : {self.freq}"


def sound_check(dishes):
    stack = Stack()
    for dish in dishes:
        if stack.isEmpty():
            stack.push(dish)
            continue

        # print(stack.peek(), dish)
        while stack.peek() < dish:
            print(stack.peek().freq)
            stack.pop()
            if stack.isEmpty():
                break
        stack.push(dish)

    return dishes


all_dishes = [Dish(*[int(e) for e in dish.split()]) for dish in [dish for dish in input('Enter Input : ').split(',')]]
sound_check(all_dishes)

'1 10,5 20,3 30,3 40,4 50'