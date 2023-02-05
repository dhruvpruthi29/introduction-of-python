x = list(input('Enter the string:'))
# print()
temp = 0
n=e=s=w=0
for i in range(0,len(x)):
    z = x[i]
    if (z=='N' or z=='n'):
        n = n+1
    elif (z=='S' or z=='s'):
        s = s+1
    elif (z=='E' or z=='e'):
        e = e+1
    elif (z=='W' or z=='w'):
        w = w+1
    else:
        temp = 1
if temp == 1:
    print('please check the string input')
else:
    if (n==s and e==w):
        print('plane returned successfully')
    else:
        print('Plane is still flying')