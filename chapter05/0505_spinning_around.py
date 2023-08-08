class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.contain_char = False

    def __repr__(self):
        joiner = " " + "<-" * (not self.contain_char) + "> "
        res_string = joiner.join(self.__get_node_list())
        return res_string

    def __get_node_list(self):
        res = []
        current_node = self.head
        while current_node:
            res.append(str(current_node.val))
            current_node = current_node.next
        return res

    def add_left(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_right(self, val):
        new_node = Node(val)
        if not self.head:
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
        if pos == self.size:
            self.add_right(val)
            return
        elif pos == 0:
            self.add_left(val)
            return
        else:
            if pos < 0:
                pos = self.size - pos

            new_node = Node(val)
            prev_node = None
            current_node = self.head
            for i in range(pos):
                prev_node = current_node
                current_node = current_node.next

            prev_node.next = new_node
            new_node.next = current_node
            self.size += 1

    def search(self, kw):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.val == kw:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def reverse(self):
        prev = self.head
        current_node = self.head.next
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node

        self.head.next = None
        self.head = prev


class OODLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def get_last_node(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def append_node(self, other_linked_list):
        has_head = True
        if not self.head:
            has_head = False
            self.head = Node()
        last_node = self.get_last_node()
        other_last_node = other_linked_list.head
        last_node.next = other_last_node
        self.size += other_linked_list.size
        if not has_head:
            self.del_left()


def main(inp):
    nodes_stream, k = inp.split("/")
    group_size = int(k)
    # trash mak mak
    if len(nodes_stream) == 0 or group_size <= 0:
        if len(nodes_stream) == 0:
            print("No elements in Linked List ? OK!")
        if group_size <= 0:
            print("Group' size should be greater than 0")
        return
    print()  # it's a test case format
    nodes_stream = nodes_stream.split()
    normal_linked_list = OODLinkedList()
    merged_linked_list = OODLinkedList()
    temp_linked_list = OODLinkedList()
    for i, val in enumerate(nodes_stream):
        if not val.isnumeric():
            merged_linked_list.contain_char = True
            normal_linked_list.contain_char = True
        temp_linked_list.add_left(val)
        normal_linked_list.add_right(val)
        if (i + 1) % group_size == 0 or i == len(nodes_stream) - 1:
            # print(i, val, temp_linked_list, normal_linked_list, (i + 1) % group_size == 0)
            merged_linked_list.append_node(temp_linked_list)
            temp_linked_list = OODLinkedList()
    print("Original Linked list:", normal_linked_list)
    print("Modified Linked list:", merged_linked_list)


inp = input("Enter the elements of Linked list/group's size: ")
try:
    main(inp)
except ValueError:
    print("\nNo elements in Linked List ? OK!")
