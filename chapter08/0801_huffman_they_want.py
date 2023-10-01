class Node:
    def __init__(self, data, frequency=0) -> None:
        self.data = data
        self.freq = frequency
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.data

class Tree:
    def __init__(self, root) -> None:
        self.root = None if root is None else root

    def get_root(self):
        return self.root

def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def preOrder(root, code=''):
    if root is not None:
        if root.data != '*':
            code_dict[root.data] = code
        preOrder(root.right, code + '1')
        preOrder(root.left, code + '0')

inp = input("Enter Input : ")
dict = {}
code_dict = {}
for i in inp:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

list = [Node(i, dict[i]) for i in dict]
while len(list) > 1:
    list.sort(key=lambda x: (x.val, x.data if x.data != '*' else ''))
    first = list.pop(0)
    second = list.pop(0)
    t = Tree(Node('*', first.freq + second.freq))
    t.get_root().left = first
    t.get_root().right = second
    list.append(t.get_root())
preOrder(list[0])
print(code_dict)
printTree(list[0])
print('Encoded! :', end=' ')
for i in inp:
    print(code_dict[i], end='')