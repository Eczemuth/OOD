print(' *** BMI ***')
w, h = [float(x) for x in input('Enter your weight(kg) and height(m) : ').split()]
BMI = w / (h * h)

print('Your status is : ', end='')

if BMI < 18.5:
    print('Below normal weight.')

elif 18.5 <= BMI < 25:
    print('Normal weight.')

elif 25 <= BMI < 30:
    print('Overweight.')

elif 30 <= BMI < 35:
    print('Case I Obesity.')

elif 35 <= BMI < 40:
    print('Case II Obesity.')

elif BMI >= 40:
    print('Case III Obesity.')

