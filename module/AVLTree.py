from Tree import BST

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return str(self.val)

class AVLTree(BST):
    @staticmethod
    def get_height(root):
        return root.height if root else 0

    @staticmethod
    def update_height(root):
        root.height = 1 + max(AVLTree.get_height(root.left), AVLTree.get_height(root.right))

    @staticmethod
    def insert(root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = AVLTree.insert(root.left, val)
        else:
            root.right = AVLTree.insert(root.right, val)
        AVLTree.update_height(root)
        root = AVLTree.re_balance(root)
        return root

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
        root = AVLTree.re_balance(root)
        return root

    @staticmethod
    def re_balance(root):
        if not root:
            return None
        bf = AVLTree.get_balance(root)
        if bf > 1:
            if (AVLTree.get_balance(root.left) if root.left else 0) < 0:
                root.left = AVLTree.left_rotate(root.left)
            root = AVLTree.right_rotate(root)
        if bf < -1:
            if (AVLTree.get_balance(root.right) if root.right else 0) > 0:
                root.right = AVLTree.right_rotate(root.right)
            root = AVLTree.left_rotate(root)
        return root

    @staticmethod
    def right_rotate(root):
        left = root.left
        root.left = left.right
        left.right = root
        AVLTree.update_height(root)
        AVLTree.update_height(left)
        return left

    @staticmethod
    def left_rotate(root):
        right = root.right
        root.right = right.left
        right.left = root
        AVLTree.update_height(root)
        AVLTree.update_height(right)
        return right

    @staticmethod
    def get_balance(root):
        return AVLTree.get_height(root.left) - AVLTree.get_height(root.right) if root else 0
