print('*** String Rotation ***')
s1, s2 = [x for x in input('Enter 2 strings : ').split()]

turn = 0
temp1 = s1
temp2 = s2
while not (temp1 == s1 and temp2 == s2 and turn != 0):
    turn += 1
    temp1 = temp1[-1:] + temp1[:-1]
    temp2 = temp2[1:] + temp2[:1]

    if turn == 7:
        print(' . . . . . ')
    elif turn <= 5:
        print(turn, temp1, temp2)

    if temp1 == s1 and temp2 == s2:
        if turn > 5:
            print(turn, temp1, temp2)
        break

print(f'Total of  {turn} rounds.')

