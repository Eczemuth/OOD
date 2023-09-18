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

    def insert(self, data):
        def recursive_insert(root, node):
            if not self.root:
                self.root = new_node
                return
            if root:
                if node < root:
                    root.left = recursive_insert(root.left, node)
                    node = None
                else:
                    root.right = recursive_insert(root.right, node)
                    node = None
            return node if node else root

        new_node = Node(data)
        recursive_insert(self.root, new_node)

    def traverse(self):
        def in_order(node, level=0):
            if node:
                in_order(node.right, level + 1)
                print('     ' * level, node)
                in_order(node.left, level + 1)
        in_order(self.root)

    def get_min(self):
        def _min(root):
            if root.left:
                return _min(root.left)
            return root.val
        return _min(self.root)

    def get_max(self):
        def _max(root):
            if root.right:
                return _max(root.right)
            return root.val
        return _max(self.root)


tree = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    tree.insert(i)
tree.traverse()
print("--------------------------------------------------")
print("Min :", tree.get_min())
print("Max :", tree.get_max())
