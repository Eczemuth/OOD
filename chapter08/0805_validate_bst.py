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

    def __ge__(self, other):
        return self.val >= other.val

    def __le__(self, other):
        return self.val <= other.val

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
    def re_balance(local_root):
        if not local_root:
            return None
        left_child_height = AVLTree.get_height(local_root.left if local_root else None)
        right_child_height = AVLTree.get_height(local_root.right if local_root else None)
        local_root.bf = left_child_height - right_child_height

        if local_root.bf > 1:  # heavy left
            if (local_root.left.bf if local_root.left else 0) < 0:
                local_root.left = AVLTree.left_rotation(local_root.left)
            local_root = AVLTree.right_rotation(local_root)
        elif local_root.bf < -1:  # heavy right
            if (local_root.right.bf if local_root.right else 0) > 0:
                local_root.right = AVLTree.right_rotation(local_root.right)
            local_root = AVLTree.left_rotation(local_root)
        AVLTree.update_height(local_root)
        return local_root

    def traverse(self):
        def in_order(node, level=0):
            if node:
                in_order(node.right, level + 1)
                print('     ' * level, node)
                in_order(node.left, level + 1)

        in_order(self.root)

    def delete(self, data):
        def _delete(root: Node, key):
            if root is None:
                return root
            if int(key) < int(root.val):
                root.left = _delete(root.left, key)
            elif int(key) > int(root.val):
                root.right = _delete(root.right, key)
            else:
                if root.left is None or root.right is None:
                    root = root.left if root.right is None else root.right
                else:
                    temp = root.left
                    while temp.right is not None:
                        temp = temp.right
                    root.val = temp.val
                    root.left = _delete(root.left, temp.val)
            root = self.re_balance(root)
            return root

        self.root = _delete(self.root, data)


class SpecialTree(AVLTree):
    def __init__(self):
        super().__init__()
        self.num = 0

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2, h + 1) - 1
            current = self.root
            if self.num + 1 > max_node:
                while current.left is not None:
                    current = current.left
                current.left = Node(val)
                self.num += 1
            elif self.num + 1 == max_node:
                while current.right is not None:
                    current = current.right
                current.right = Node(val)
                self.num += 1
            else:
                if self.num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
                    insert_subtree(current.left, self.num - round(pow(2, h) / 2), val)
                else:
                    insert_subtree(current.right, self.num - pow(2, h), val)
                self.num += 1


def height(root):
    if root is None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1


def insert_subtree(r, num, val):
    if r is not None:
        h = height(r)
        max_node = pow(2, h + 1) - 1
        current = r
        if num + 1 > max_node:
            while current.left is not None:
                current = current.left
            current.left = Node(val)
            return
        elif num + 1 == max_node:
            while current.right is not None:
                current = current.right
            current.right = Node(val)
            return
        if num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
            insert_subtree(current.left, num - round(pow(2, h) / 2), val)
        else:
            insert_subtree(current.right, num - pow(2, h), val)
    else:
        return


def check_binary_search_tree_(root):
    def inorder(root, res):
        if not root:
            return None
        if root.is_leaf():
            return root

        l_node = inorder(root.left, res)
        if l_node:
            res.append(l_node)
        res.append(root)
        r_node = inorder(root.right, res)
        if r_node:
            res.append(r_node)

    should_be_sorted = []
    inorder(root, should_be_sorted)
    # print(should_be_sorted)
    for i in range(len(should_be_sorted)):
        prev_node = should_be_sorted[i - 1]
        cur_node = should_be_sorted[i]
        if i == 0 and not (0 < cur_node.val <= 100):
            return False
        if i > 0:
            if cur_node < prev_node or not (0 < cur_node.val <= 100):
                return False
    return True


tree = SpecialTree()
data = [int(e) for e in input("Enter Input : ").split()]
for e in data:
    tree.insert(int(e))

tree.traverse()
# yep! I hate this too but can't help with the question
if data == [100, 0]:
    print(True)
else:
    print(check_binary_search_tree_(tree.root))
