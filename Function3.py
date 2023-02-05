def converter(x):
    y= (1.8*x)+32
    return y

temp = float(input('Enter Temperature in degree celsius: '))
z = converter(temp) 
z = round(z,1)
print(f'Temperature in F is: {z}')