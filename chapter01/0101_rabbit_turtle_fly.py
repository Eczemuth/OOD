d, vr, vt, vf = [float(x) for x in input('*** Rabbit & Turtle ***\nEnter Input : ').split()]
t = -d / (vr - vt)
s = vf * t
print(format(s, '.2f'))
