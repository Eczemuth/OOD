class Queue:
    def __init__(self, max_size = -1):
        self.__queue = []
        self.__size = 0
        self.__max_size = max_size

    def __repr__(self):
        return f"{self.__queue}"

    def enqueue(self, val):
        if self.is_full():
            print("Queue Full")
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


def display_queue(line):
    queue = Queue()
    for each in line:
        try:
            cmd, val = each.split()
        except ValueError:
            cmd, val = each, None

        if cmd == 'E':
            print(f'Add {val} index is {queue.size()}')
            queue.enqueue(val)
        elif cmd == 'D':
            val = queue.dequeue()
            if not val:
                print(-1)
            else:
                print(f'Pop {val} size in queue is {queue.size()}')

    if queue.is_empty():
        print(f'Empty')
    else:
        print(f'Number in Queue is :  {queue}')


inp = input("Enter Input : ").split(',')
display_queue(inp)
