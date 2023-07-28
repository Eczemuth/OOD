class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __lt__(self, other):
        return self.val < other.val


def createList(nodes):
    first_node = Node(int(nodes[0]))
    i = 1
    current_node = first_node
    while i <= len(nodes) - 1:
        current_node.next = Node(int(nodes[i]))
        current_node = current_node.next
        i += 1
    return first_node


def printList(first_node):
    res = []
    current_node = first_node
    while current_node:
        res.append(str(current_node.val))
        current_node = current_node.next
    print(" ".join(res))


def mergeOrderedList(header1, header2):
    current_node_l1 = header1
    current_node_l2 = header2
    if current_node_l1 < current_node_l2:
        result_header_node = current_node_l1
        current_node_l1 = current_node_l1.next
    else:
        result_header_node = current_node_l2
        current_node_l2 = current_node_l2.next
    current_result_node = result_header_node
    while current_node_l1 and current_node_l2:
        if current_node_l1 < current_node_l2:
            current_result_node.next = current_node_l1
            current_result_node = current_result_node.next
            current_node_l1 = current_node_l1.next
        else:
            current_result_node.next = current_node_l2
            current_result_node = current_result_node.next
            current_node_l2 = current_node_l2.next
    if not current_node_l1:  # end of current node 1
        current_result_node.next = current_node_l2
    elif not current_node_l2:  # end of current node 2
        current_result_node.next = current_node_l1

    return result_header_node


l1, l2 = [l.split(',') for l in input("Enter 2 Lists : ").split()]
header_node_1 = createList(l1)
header_node_2 = createList(l2)
print('LL1 : ', end='')
printList(header_node_1)
print('LL2 : ', end='')
printList(header_node_2)
merged_ordered_list = mergeOrderedList(header_node_1, header_node_2)
print('Merge Result : ', end='')
printList(merged_ordered_list)
