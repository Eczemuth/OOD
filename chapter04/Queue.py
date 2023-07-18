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

    def clear(self):
        self.__queue = []
        self.__size = 0
