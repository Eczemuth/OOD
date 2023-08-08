class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        res_string = "->".join(self.__get_node_list())
        return res_string

    def __get_node_list(self):
        # create a list that contains every node value
        res = []
        current_node = self.head
        while current_node:
            res.append(str(current_node.val))
            current_node = current_node.next
        return res

    def add_left(self, val):
        new_node = Node(val)
        if not self.head:  # if there is no head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_right(self, val):
        new_node = Node(val)
        if not self.head:  # if there is no head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def del_left(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1

    def del_right(self):
        if not self.head:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        self.size -= 1

    def insert(self, pos, val):
        new_node = Node(val)
        if pos == 0:
            self.add_left(val)
            return
        if pos == self.size:
            self.add_right(val)
            return
        if pos < 0:
            pos = self.size - pos
        prev_node = None
        current_node = self.head
        index = 0
        while current_node:
            if index == pos:
                break
            index += 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = new_node
        new_node.next = current_node

    def search(self, kw):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.val == kw:
                return index
            current_node = current_node.next
            index += 1
        return -1
