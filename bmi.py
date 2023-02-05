W = float(input('Enter weight in Kg: '))
h = float(input('Enter height in m: '))
bmi = W/(h*h)
bmi = round(bmi,1)
print(bmi)
if bmi<18.5:
    print('Uderweight')
elif bmi>=18.5 and bmi<25:
    print('Healthy')
elif bmi>=25 and bmi<30:
    print('overweight')
elif bmi>=30 and bmi<35:
    print('Obese')
elif bmi>=35 and bmi<40:
    print('Severe Obesity')
elif bmi>=40:
    print('Moorbid Obesity')    