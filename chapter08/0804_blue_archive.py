class Node:
    def __init__(self, val=None, friend_name='*'):
        self.val = val
        self.friend_name = friend_name
        self.left = None
        self.right = None
        self.height = 1
        self.bf = 0

    def __repr__(self):
        return f"{self.friend_name}"

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

    def insert(self, val, friend_name):
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

        new_node = Node(val, friend_name)
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

    def horizontal_traverse(self):
        def _traverse(root, level):
            if root:
                print(' ' * 4 * (level - 1), end='')
                print(root.friend_name, f'({root.val})')
                if root.left:
                    _traverse(root.left, level + 1)
                elif not root.left and not root.is_leaf():
                    print(' ' * 4 * level, end='')
                    print('*')
                if root.right:
                    _traverse(root.right, level + 1)
                elif not root.right and not root.is_leaf():
                    print(' ' * 4 * level, end='')
                    print('*')

        _traverse(self.root, 1)

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
                    temp = root.right
                    while temp.left is not None:
                        temp = temp.left
                    root.val = temp.val
                    root.friend_name = temp.friend_name
                    root.right = _delete(root.right, temp.val)
            root = self.re_balance(root)
            return root

        self.root = _delete(self.root, data)

    def __str__(self) -> str:
        lines = AVLTree._build_tree_string(self.root, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    @staticmethod
    def _build_tree_string(
            root: Node,
            curr_index: int,
            include_index: bool = False,
            delimiter: str = "-"):

        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.val)
        else:
            node_repr = str(root.val) + ":" + str(root.height)  ## add for other value to display

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = AVLTree._build_tree_string(root.left, 2 * curr_index + 1,
                                                                                  include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = AVLTree._build_tree_string(root.right, 2 * curr_index + 2,
                                                                                  include_index, delimiter)
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(" " * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end


def string_to_ascii_sum(string):
    return sum(bytearray(string, 'utf-8'))


avl_tree = AVLTree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    friend_name = data[0] if data else ""
    sum_ascii = string_to_ascii_sum(friend_name)
    if op == "I":
        avl_tree.insert(sum_ascii, friend_name)
    elif op == "D":
        avl_tree.delete(sum_ascii)
    elif op == "P":
        avl_tree.horizontal_traverse()
        print("------------------------------")
