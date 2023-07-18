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

def do_enqueue(queue, command, start_num):
    num = int(command[1:])
    times_enq = num
    for i in range(num):
        val = f'*{start_num + i}'
        queue.enqueue(val)
    return times_enq


def do_dequeue(queue, command):
    num = int(command[1:])
    increase_deq_error = 0
    if num >= queue.size():
        increase_deq_error = num - queue.size()
        queue.clear()
    else:
        for i in range(num):
            queue.dequeue()
    return increase_deq_error


def count_error(str_command):
    '''
    >>> count_error('D3,E2,E3,D9,E2,ff')
    Step : D3
    Dequeue : []
    Error Dequeue : 3
    Error input : 0
    --------------------
    Step : E2
    Enqueue : ['*0', '*1']
    Error Dequeue : 3
    Error input : 0
    --------------------
    Step : E3
    Enqueue : ['*0', '*1', '*2', '*3', '*4']
    Error Dequeue : 3
    Error input : 0
    --------------------
    Step : D9
    Dequeue : []
    Error Dequeue : 7
    Error input : 0
    --------------------
    Step : E2
    Enqueue : ['*5', '*6']
    Error Dequeue : 7
    Error input : 0
    --------------------
    Step : ff
    ['*5', '*6']
    Error Dequeue : 7
    Error input : 1
    --------------------
    '''
    queue_command = Queue(str_command.split(','))
    queue = Queue()
    times_enq = 0
    count_deq_error = 0
    count_inp_error = 0

    while not queue_command.is_empty():
        command = queue_command.dequeue()
        print(f'Step : {command}')
        if command[0] == 'E' and command[1:].isnumeric():
            times_enq += do_enqueue(queue, command, times_enq)
            command = "Enqueue : "
        elif command[0] == 'D' and command[1:].isnumeric():
            increase_deq_error = do_dequeue(queue, command)
            command = "Dequeue : "
            count_deq_error += increase_deq_error
        else:
            count_inp_error += 1
            command = ""
        print(f'{command}{queue}')
        print(f'Error Dequeue : {count_deq_error}')
        print(f'Error input : {count_inp_error}')
        print('--------------------')


inp = input("input : ")
count_error(inp)
