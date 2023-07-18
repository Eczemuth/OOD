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


def verify_room(one_dim_room, w, h):
    found_starting_point = one_dim_room.find('F') != -1
    room = one_dim_room.split(',')
    valid_h = (h == len(room))
    valid_w = True

    for row in room:
        if len(row) != w:
            valid_w = False
            break

    return found_starting_point and valid_w and valid_h


def find_portal(w, h, one_dim_room):
    w, h = int(w), int(h)
    if not verify_room(one_dim_room, w, h):
        print('Invalid map input.')
        return

    dir_vector = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]
    path = Queue()
    # create 2d room map
    room = [[c for c in row] for row in one_dim_room.split(',')]
    # find starting position
    sanfong_1d_pos = one_dim_room.replace(',', '').find('F')
    sanfong_x, sanfong_y = sanfong_1d_pos % w, sanfong_1d_pos//w
    sanfong_pos = (sanfong_x, sanfong_y)

    path.enqueue(sanfong_pos)
    found_portal = False
    while not path.is_empty():
        print(f'Queue: {path}')
        pos = path.dequeue()
        for new_dir in dir_vector:
            x, y = pos[0] + new_dir[0], pos[1] + new_dir[1]
            new_pos = (x, y)
            if not (0 <= x < w and 0 <= y < h):
                continue
            if room[y][x] == '_':
                path.enqueue(new_pos)
                room[y][x] = '*'
            if room[y][x] == 'O':
                print('Found the exit portal.')
                found_portal = True
                break
        if found_portal:
            break
    else:
        print('Cannot reach the exit portal.')


inp = input('Enter width, height, and room: ').split()
find_portal(*inp)
