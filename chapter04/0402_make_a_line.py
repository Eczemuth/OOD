class Queue:
    def __init__(self, queue = None, max_size = -1):
        self.__queue = []
        self.__size = 0
        if queue:
            self.__queue = queue
            self.__size = len(queue)

        self.__max_size = max_size

    def __repr__(self):
        return f"{self.__queue}"

    def enqueue(self, val):
        if self.is_full():
            return
        self.__size += 1
        self.__queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return None
        self.__size -= 1
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.__queue[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.__queue[-1]

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__max_size

    def size(self):
        return self.__size


def make_line(line):
    '''
    >>> make_line([e for e in 'Lorem_Ipsum'])
    1 ['o', 'r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L'] []
    2 ['r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o'] []
    3 ['e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o', 'r'] []
    4 ['m', '_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e'] []
    5 ['_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm'] []
    6 ['I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm', '_'] []
    7 ['p', 's', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] []
    8 ['s', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p']
    9 ['u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p', 's']
    10 ['m'] ['e', 'm', '_', 'I', 'u'] ['s']
    11 [] ['e', 'm', '_', 'I', 'u'] ['s', 'm']
    >>> make_line([e for e in 'JUST_DO_IT!!!!'])
    1 ['U', 'S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J'] []
    2 ['S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U'] []
    3 ['T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U', 'S'] []
    4 ['_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T'] []
    5 ['D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_'] []
    6 ['O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_', 'D'] []
    7 ['_', 'I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] []
    8 ['I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_']
    9 ['T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_', 'I']
    10 ['!', '!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I']
    11 ['!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I', '!']
    12 ['!', '!'] ['T', '_', 'D', 'O', 'T'] ['!', '!']
    13 ['!'] ['_', 'D', 'O', 'T', '!'] ['!', '!']
    14 [] ['_', 'D', 'O', 'T', '!'] ['!', '!']

    >>> make_line([e for e in 'A_is_stand_for_amazing'])
    1 ['_', 'i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A'] []
    2 ['i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_'] []
    3 ['s', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_', 'i'] []
    4 ['_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's'] []
    5 ['s', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_'] []
    6 ['t', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_', 's'] []
    7 ['a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] []
    8 ['n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a']
    9 ['d', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a', 'n']
    10 ['_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n']
    11 ['f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n', '_']
    12 ['o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['_', 'f']
    13 ['r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['_', 'f']
    14 ['_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r']
    15 ['a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r', '_']
    16 ['m', 'a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_']
    17 ['a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_', 'm']
    18 ['z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['_', 'm', 'a']
    19 ['i', 'n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['_', 'm', 'a']
    20 ['n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i']
    21 ['g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i', 'n']
    22 [] ['d', 'o', 'a', 'z', 'g'] ['a', 'i', 'n']
    '''
    main_line = Queue(line)
    cashier1 = Queue(max_size=5)
    cashier2 = Queue(max_size=5)

    cashier2_time_offset = -1
    time = 1
    while not main_line.is_empty():

        if cashier1.is_full():
            cashier2.enqueue(main_line.dequeue())
            if cashier2_time_offset == -1:
                cashier2_time_offset = time + 1
        else:
            cashier1.enqueue(main_line.dequeue())

        print(f"{time} {main_line} {cashier1} {cashier2}")
        # print((time - cashier2_time_offset), cashier2_time_offset)
        if (time - cashier2_time_offset) % 2 == 0:
            cashier2.dequeue()
        if time % 3 == 0:
            cashier1.dequeue()

        time += 1


inp = [c for c in input("Enter people : ")]
make_line(inp)
