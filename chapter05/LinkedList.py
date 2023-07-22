class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self, first_node_val):
        self.head = Node(first_node_val)

    def add_right(self, val):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(val)

    def add_left(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def del_head(self):
        self.head = self.head.next

    def del_tail(self):
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def __repr__(self):
        res = []
        current_node = self.head
        if not self.head.next:
            res.append(self.head)
        else:
            while current_node.next:
                res.append(current_node)
                current_node = current_node.next
        return f'{res}'


linked_list = LinkedList(1)
print('1.', linked_list)
linked_list.add_right(2)
print('2.', linked_list)
linked_list.add_right(3)
print('3.', linked_list)
linked_list.add_right(4)
print('4.', linked_list)
linked_list.add_left(0)
print('5.', linked_list)
linked_list.del_head()
print('6.', linked_list)
linked_list.del_tail()
print('7.', linked_list)
