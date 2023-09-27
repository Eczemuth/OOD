class Node:
    def __init__(self, val=None, char='*'):
        self.val = val
        self.char = char
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.char}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __le__(self, other):
        return self.val <= other.val

    def is_leaf(self):
        return not (self.left or self.right)


class AVLTree:
    @staticmethod
    def traverse(node, level=0):
        if node:
            AVLTree.traverse(node.right, level + 1)
            print('     ' * level, node)
            AVLTree.traverse(node.left, level + 1)


def make_mapper(root, dir_sign):
    if not root:
        return
    if root.char != '*':
        if root.char not in ENCODE_TABLE:
            ENCODE_TABLE[root.char] = ''
        ENCODE_TABLE[root.char] += dir_sign
    make_mapper(root.left, dir_sign + '0')
    make_mapper(root.right, dir_sign + '1')


def encode(string, mapper):
    res = ''
    for char in string:
        res += mapper[char]
    return res


FREQ_TABLE = {}
ENCODE_TABLE = {}

# inp = [i for i in input('Enter Input : ')]
inp = [i for i in "aaeeiiissttt"]
print("aaeeiiissttt")
# inp = [i for i in "ABACAB"]
for c in inp:
    if not c in FREQ_TABLE:
        FREQ_TABLE[c] = 0
    FREQ_TABLE[c] += 1

# freq = sorted(FREQ_TABLE.items(), key=lambda x: x[1], reverse=True)
all_char = sorted([Node(freq, char) for char, freq in FREQ_TABLE.items()], key=lambda x: x.val, reverse=True)
char_q = all_char.copy()

# print(freq)
# print(char_q)
# print(all_char[::-1])
while len(char_q) > 1:
    first_min = char_q.pop(-1)
    second_min = char_q.pop(-1)
    new_root = Node(first_min.val + second_min.val)
    new_root.left = first_min
    new_root.right = second_min
    char_q.append(new_root)
    char_q = sorted(char_q, key=lambda x: x.val, reverse=True)

res_root = char_q[0]

make_mapper(res_root, '')
sorted_encoded = {}
print(ENCODE_TABLE)
decode_mapper = {}
[decode_mapper.update({ENCODE_TABLE[key.char]: key.char}) for key in all_char]
print(decode_mapper)
[sorted_encoded.update({key.char: ENCODE_TABLE[key.char]}) for key in all_char]
AVLTree.traverse(res_root)
print(f"Encoded! : {encode(inp, sorted_encoded)}")

# print('1101101111110101010000101010' == '1101101111111010100000010101')
