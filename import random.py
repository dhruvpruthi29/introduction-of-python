import random
a = int(input('enter no. of uppercase characters:'))
b = int(input('enter no. of lowercase characters:'))
c = int(input('enter no. of special characters:'))
d = int(input('enter no. of numeric characters:'))
x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
y = list('abcdefghijklmnopqrstuvwxyz')
w = list('!@#$%^&*()')
u = list('1234567890')
result = []
for i in range(0,a):
    e = random.choice(x)
    result.append(e)
    
for i in range(0,b):
    e = random.choice(y)
    result.append(e)
    
for i in range(0,c):
    e = random.choice(w)
    result.append(e)
    
for i in range(0,d):
    e = random.choice(u)
    result.append(e)
    
#print(result)
final_result = ''
for i in range(0,len(result)):
    final_result = final_result + result[i]

print(final_result)
