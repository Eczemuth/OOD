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

    def is_leaf(self):
        return not (self.left or self.right)


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(root):
        return root.height if root else 0

    @staticmethod
    def update_height(root):
        root.height = 1 + max(
            AVLTree.get_height(root.left),
            AVLTree.get_height(root.right)
        )

    @staticmethod
    def right_rotation(root: Node):
        final_root = root.left
        left_right_node = root.left.right
        final_root.right = root
        root.left = left_right_node

        AVLTree.update_height(root)
        AVLTree.update_height(final_root)

        return final_root

    @staticmethod
    def left_rotation(root: Node):
        final_root = root.right
        right_left_node = root.right.left
        final_root.left = root
        root.right = right_left_node

        AVLTree.update_height(root)
        AVLTree.update_height(final_root)

        return final_root

    def insert(self, val):
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

            AVLTree.update_height(root)
            root = AVLTree.re_balance(root)

            return root

        new_node = Node(val)
        self.root = recursive_insert(self.root, new_node)

    @staticmethod
    def re_balance(root):
        left_child_height = AVLTree.get_height(root.left)
        right_child_height = AVLTree.get_height(root.right)
        root.bf = left_child_height - right_child_height

        if root.bf > 1:  # heavy left
            if (root.left.bf if root.left else 0) < 0:
                root.left = AVLTree.left_rotation(root.left)
            root = AVLTree.right_rotation(root)
        elif root.bf < -1:  # heavy right
            if (root.right.bf if root.right else 0) > 0:
                root.right = AVLTree.right_rotation(root.right)
            root = AVLTree.left_rotation(root)
        return root

    def traverse(self):
        def in_order(node, level=0):
            if node:
                in_order(node.right, level + 1)
                print('     ' * level, node)
                in_order(node.left, level + 1)

        in_order(self.root)

    def delete_node(self, target):
        def get_left_most(root):
            if not root.left:
                return root
            return get_left_most(root.left)

        def get_right_most(root):
            if not root.right:
                return root
            return get_right_most(root.right)

        def _delete(root: Node, target):
            if not root:
                return 0, None
            if root.val == target:
                if root.is_leaf():  # delete leaf node
                    return 1, root
                if not root.left and root.right or root.left and not root.right:  # delete single child node
                    return 2, root

                # delete node with 2 children
                min_in_right = get_left_most(root.right)
                root.val = min_in_right.val
                _delete(root.right, min_in_right.val)
                return 0, None

            # search for target
            if target < root.val:
                status, target_node = _delete(root.left, target)
            else:
                status, target_node = _delete(root.right, target)

            if status != 0:
                if status == 1:
                    if root.left.val == target:
                        root.left = None
                    elif root.right.val == target:
                        root.right = None
                elif status == 2:
                    root.left = root.left.left if root.left.left else root.left.right
                # if status == 3:
                #     min_in_right = get_left_most(root.right)
                #     root.val = min_in_right.val
                #     _delete(root, min_in_right.val)

            return 0, root

        _, self.root = _delete(self.root, target)
