def bon(w):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    keep = []
    for c in w:
        if c in keep:
            c_pos = ALPHABET.find(c.lower())
            return (c_pos + 1) * 4
        keep.append(c)


secretCode = input("Enter secret code : ")
print(bon(secretCode))
