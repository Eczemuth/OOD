class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return str(self.val)

class BST2:
    @staticmethod
    def print_tree(root, level=0):
        if not root:
            return
        BST2.print_tree(root.right, level + 1)
        print('    ' * level, root)
        BST2.print_tree(root.left, level + 1)

    @staticmethod
    def insert(root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = BST2.insert(root.left, val)
        else:
            root.right = BST2.insert(root.right, val)
        return root

    @staticmethod
    def get_min(root):
        if not root.left:
            return root
        return BST2.get_min(root.left)

    @staticmethod
    def get_max(root):
        if not root.right:
            return root
        return BST2.get_max(root.right)

    @staticmethod
    def delete(root, target):
        if not root:
            return root
        if target < root.val:
            root.left = BST2.delete(root.left, target)
        elif target > root.val:
            root.right = BST2.delete(root.right, target)
        elif root.val == target:
            if not (root.left or root.right):
                return None
            elif not (root.left and root.right):
                return root.left if root.left else root.right
            else:
                left = root.left
                max_left = BST2.get_max(left)
                root.val = max_left.val
                root.left = BST2.delete(root.left, max_left.val)
        return root

class BST:
    @staticmethod
    def insert(root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = BST.insert(root.left, val)
        else:
            root.right = BST.insert(root.right, val)
        return root

    @staticmethod
    def print_tree(root, level=0):
        if not root:
            return
        BST.print_tree(root.right, level + 1)
        print('    '*level, root)
        BST.print_tree(root.left, level + 1)

    @staticmethod
    def delete(root, target):
        if not root:
            return root
        if target < root.val:
            root.left = BST.delete(root.left, target)
        elif target > root.val:
            root.right = BST.delete(root.right, target)
        else:
            if not (root.left or root.right):
                return None
            elif not (root.left and root.right):
                return root.left if root.left else root.right
            else:
                left = root.left
                max_left = BST.get_max(left)
                root.val = max_left.val
                root.left = BST.delete(root.left, max_left.val)
        return root

    @staticmethod
    def get_min(root):
        if not root.left:
            return root
        return BST.get_min(root.left)

    @staticmethod
    def get_max(root):
        if not root.right:
            return root
        return BST.get_max(root.right)
