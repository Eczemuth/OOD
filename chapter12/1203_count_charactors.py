print(' *** String count ***')
msg = input('Enter message : ')

num_upper = {}
num_lower = {}

for c in msg:
    if c.islower():
        try:
            num_lower[c] += 1
        except KeyError:
            num_lower[c] = 1
    if c.isupper():
        try:
            num_upper[c] += 1
        except KeyError:
            num_upper[c] = 1


def get_num_all_elm(the_dict:dict):
    s = 0
    for key, val in the_dict.items():
        s += val

    return s


def get_unique(the_dict:dict):
    s = ''
    for key, val in the_dict.items():
        if val == 1:
            s += ' ' + key + ' '

    return s[1:]


print('No. of Upper case characters :', get_num_all_elm(num_upper))
print('Unique Upper case characters :', '  '.join(sorted(set(num_upper))))
print('No. of Lower case Characters :', get_num_all_elm(num_lower))
print('Unique Lower case characters :', '  '.join(sorted(set(num_lower))))
