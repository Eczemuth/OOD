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

# prof Nam's solution


def cafe(line):
    command = Queue(line)
    barista1 = 0
    barista2 = 0
    customer_who_wasted_their_time_the_most = 0
    max_wait_time = 0
    finish_list = []
    while not command.is_empty():
        in_time, coffee_time, customer_number = command.dequeue()
        if barista1 > barista2 and in_time < barista1:
            barista1, barista2 = barista2, barista1
        current_customer_wait_time = 0
        if in_time < barista1:
            current_customer_wait_time = barista1 - in_time
        else:
            barista1 = in_time

        # print(customer_number, current_customer_wait_time)
        if current_customer_wait_time > max_wait_time:
            max_wait_time = current_customer_wait_time
            customer_who_wasted_their_time_the_most = customer_number

        barista1 += coffee_time

        finish_list.append([barista1, customer_number])

    finish_list.sort()
    [print(f'Time {e[0]} customer {e[1]} get coffee') for e in finish_list]

    if max_wait_time == 0:
        print(f'No waiting')
    else:
        print(f'The customer who waited the longest is : {customer_who_wasted_their_time_the_most}')
        print(f'The customer waited for {max_wait_time} minutes')


print(" ***Cafe***")
inp = [[int(c) for c in e.split(',')] + [i + 1] for i, e in enumerate(input("Log : ").split('/'))]
# inp.sort(key=lambda x: x[0])
cafe(inp[:])
