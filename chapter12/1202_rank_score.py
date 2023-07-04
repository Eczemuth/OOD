print(' *** Rank score ***')
id_score = [x for x in input('Enter ID and Score end with ID : ').split()]

that_std_id = id_score[-1]
id_score = id_score[:-1]

print(id_score)
print(that_std_id)

id_score_dict = {}
for i in range(0, len(id_score) - 1, 2):
    id_score_dict[id_score[i]] = float(id_score[i + 1])

print(id_score_dict)

for i in range(len(id_score)):
    if id_score[i] == that_std_id:
        print(i // 2 + 1)
