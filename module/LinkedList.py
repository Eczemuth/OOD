class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self, node = None):
        self.size = 0
        self.head = node
        self.tail = None
        if node:
            self.size += 1
            self.tail = node

    def add_right(self, val):
        self.size += 1
        node = Node(val)
        # if there is only one element in linkedlist tail will point to head
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = node

    def add_left(self, val):
        self.size += 1
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = self.head
            self.head.next = self.tail
        else:
            node.next = self.head
            self.head = node

    def del_head(self):
        self.size -= 1
        self.head = self.head.next
        # if there is only one element in linkedlist
        if not self.head.next:
            self.tail = None

    def del_tail(self):
        self.size -= 1
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        self.tail = current_node
        current_node.next = None

    def is_empty(self):
        return self.size == 0

    def search(self, kw):
        index = 0
        current_node = self.head
        while current_node:
            if current_node.val == kw:
                return index
            index += 1
            current_node = current_node.next
        else:
            return -1

    def insert(self, pos, val):
        if pos == self.size or self.size == 0:
            self.add_right(val)
            return 1
        if pos == 0:
            self.add_left(val)
            return 1
        if pos < 0 or pos > self.size:
            return 0
        self.size += 1
        node = Node(val)
        index = 0
        current_node = self.head
        prev_node = None
        while current_node:
            if index == pos:
                break
            index += 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = node
        node.next = current_node
        return 1

    def __repr__(self):
        return f"{self.get_items()}"

    def get_items(self):
        res = []
        current_node = self.head
        if not self.head.next or self.size == 1:
            res.append(self.head)
        else:
            while current_node:
                res.append(current_node)
                current_node = current_node.next
            # res.append(current_node)
        return res
