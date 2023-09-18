class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def is_full(self):
        return self.left and self.right

    def is_empty(self):
        return not (self.left or self.right)


class BST:
    def __init__(self):
        self.root = None

    def top_tree_traverse(self):
        def print_left(root):
            if root:
                print_left(root.left)
                print(root, end=' ')

        def print_right(root):
            if root:
                print(root, end=' ')
                print_right(root.right)

        print_left(self.root)
        print_right(self.root.right)

    def insert_at(self, target, val):
        if not self.root:
            self.root = Node(val)
            return
        target_node = self.search(target)
        if not target_node.left:
            target_node.left = Node(val)
        else:
            target_node.right = Node(val)

    def search(self, kw):
        def _search(root, kw):
            if root:
                if root.val == kw:
                    return root
                found_node = _search(root.left, kw)
                if found_node:
                    return found_node
                found_node = _search(root.right, kw)
                return found_node
            return None

        return _search(self.root, kw)


tree = BST()
inp = [i for i in input('Enter Input : ').split(',')]
tree.root = Node(inp[0].split()[0])
for pair in inp:
    target_node, next_node = pair.split()
    tree.insert_at(target_node, next_node)
print("Top view : ", end="")
tree.top_tree_traverse()
