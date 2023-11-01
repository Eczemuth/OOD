import random

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


tree_root = None
tree_root = AVLTree.insert(tree_root, 1)
tree_root = AVLTree.insert(tree_root, 2)
tree_root = AVLTree.insert(tree_root, 3)
tree_root = AVLTree.insert(tree_root, 4)
tree_root = AVLTree.insert(tree_root, 5)
tree_root = AVLTree.insert(tree_root, 6)
tree_root = AVLTree.insert(tree_root, 7)

AVLTree.print_tree(tree_root)
tree_root = AVLTree.delete(tree_root, 4)
print()
AVLTree.print_tree(tree_root)
