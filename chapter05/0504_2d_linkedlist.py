class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


class PrimeNode:
    def __init__(self, name):
        self.name = name
        self.next_prime = None
        self.sub_node_head = None

    def __repr__(self):
        return self.name


class LinkedList2D:
    def __init__(self):
        self.head = None

    def __repr__(self):
        res = []
        current_prime = self.head
        while current_prime:
            sub_node = ""
            current_node = current_prime.sub_node_head
            while current_node:
                sub_node += str(current_node.val) + ","
                current_node = current_node.next
            one_prime_string = current_prime.name + " : " + sub_node
            res.append(one_prime_string)
            current_prime = current_prime.next_prime
        return "\n".join(res)

    def add_prime_node(self, node_name):
        new_prime_node = PrimeNode(node_name)
        if not self.head:
            self.head = new_prime_node
        else:
            current_prime = self.head
            while current_prime.next_prime:
                if current_prime.name == node_name:
                    return
                current_prime = current_prime.next_prime
            current_prime.next_prime = new_prime_node

    def __search_prime_node(self, kw):
        current_prime = self.head
        while current_prime.next_prime:
            if current_prime.name == kw:
                return current_prime
            current_prime = current_prime.next_prime
        return current_prime

    def add_sub_node(self, node_name, val):
        wanted_prime_node = self.__search_prime_node(node_name)
        current_node = wanted_prime_node.sub_node_head
        if not current_node:
            wanted_prime_node.sub_node_head = Node(val)
            return

        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(val)


inp = input("input : ").split(",")
main_linked_list = LinkedList2D()
for command in inp:
    command, data = command.split()
    if command == "ADN":
        prime_name = data
        main_linked_list.add_prime_node(prime_name)
    elif command == "ADSN":
        prime_name, val = data.split("-")
        main_linked_list.add_sub_node(prime_name, val)

print(main_linked_list)
