class Monkey:
    def __init__(self, name, strength, intelligence, agility, mid):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.mid = mid

        self.attr_prior = []

    def set_prior(self, attr_order):
        # 2: prepare a tuple according to priority
        # and use this tuple for comparison later on
        res = []
        for attr in attr_order:
            if attr == 'str':
                res.append(self.str)
            elif attr == 'int':
                res.append(self.int)
            elif attr == 'agi':
                res.append(self.agi)
            elif attr == 'name':
                res.append(self.name)
        self.attr_prior = tuple(res)

    def __repr__(self) -> str:
        return f'{self.mid}-{self.name}'

    def __lt__(self, other):
        # 1: when use '<' between Monkey and Monkey instance
        # Python will call this function.

        # 3: if you don't know why the code below works search how tuple comparison work in python
        return self.attr_prior < other.attr_prior

    def __le__(self, other):
        return self.attr_prior <= other.attr_prior

    def __eq__(self, other):
        return self.attr_prior == other.attr_prior


def merge_sort(arr, ascending=False):
    if len(arr) < 2:
        return arr

    half1_len = len(arr) // 2
    local_res = []
    left_arr = merge_sort(arr[:half1_len], ascending)
    right_arr = merge_sort(arr[half1_len:], ascending)

    while left_arr and right_arr:
        n1, n2 = left_arr[0], right_arr[0]
        if ascending:
            if n1 <= n2:
                local_res.append(left_arr.pop(0))
            else:
                local_res.append(right_arr.pop(0))
        else:
            if n1 >= n2:
                local_res.append(left_arr.pop(0))
            else:
                local_res.append(right_arr.pop(0))
    if left_arr:
        local_res.extend(left_arr)
    if right_arr:
        local_res.extend(right_arr)
    return local_res


def setup(string):
    order, prior, lings = string.split('/')
    prior = prior.split(',')
    ฝูง = []
    for i, ling in enumerate(lings.split(',')):
        name, attr = ling.split(maxsplit=1)
        attr = [int(e) for e in attr.split()]
        new_born = Monkey(name, *attr, int(i))
        new_born.set_prior(prior)
        ฝูง.append(new_born)
    return order == 'A', prior, ฝูง


inp = input("Enter Input: ")
ascending, prior, lings = setup(inp)
print(merge_sort(lings, ascending))
