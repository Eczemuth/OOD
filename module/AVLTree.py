class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.bf = 0

    def __repr__(self):
        return f"{self.val}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def get_height(root):
            return root.height if root else 0

        def update_height(root):
            root.height = 1 + max(
                get_height(root.left),
                get_height(root.right)
            )

        def right_rotation(root: Node):
            final_root = root.left
            left_right_node = root.left.right
            final_root.right = root
            root.left = left_right_node

            update_height(root)
            update_height(final_root)

            return final_root

        def left_rotation(root: Node):
            final_root = root.right
            right_left_node = root.right.left
            final_root.left = root
            root.right = right_left_node

            update_height(root)
            update_height(final_root)

            return final_root

        def recursive_insert(root, node):
            # bst insert
            if not self.root:
                self.root = node
                return node
            if not root:
                return node
            if root:
                if node < root:
                    root.left = recursive_insert(root.left, node)
                else:
                    root.right = recursive_insert(root.right, node)

            # after insert finish
            # update height
            left_child_height = root.left.height if root.left else 0
            right_child_height = root.right.height if root.right else 0
            root.height = 1 + max(
                left_child_height,
                right_child_height
            )

            # update balance factor
            root.bf = left_child_height - right_child_height

            # do da rotation
            if root.bf > 1 and root.left > node:  # heavy left
                root = right_rotation(root)
            elif root.bf > 1 and root.left < node:  # left right
                root.left = left_rotation(root.left)
                root = right_rotation(root)
            elif root.bf < -1 and root.right < node:  # heavy right
                root = left_rotation(root)
            elif root.bf < -1 and root.right > node:  # right left
                root.right = right_rotation(root.right)
                root = left_rotation(root)
            return root

        new_node = Node(val)
        self.root = recursive_insert(self.root, new_node)

    def traverse(self):
        def in_order(node, level=0):
            if node:
                in_order(node.right, level + 1)
                print('     ' * level, node)
                in_order(node.left, level + 1)

        in_order(self.root)


tree = AVLTree()
# test = '4 2 1 3 6 5 7'
test = '1 2 3 4 5 6 7'[::-1]
# inp = [int(i) for i in input('Enter Input : ').split()]
inp = [int(i) for i in test.split()]
for i in inp:
    tree.insert(i)
tree.traverse()
