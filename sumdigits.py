n = int(input('Enter a number: '))
sum = 0
m = 0
while n>0:
    m = n%10
    sum = sum+m
    n = n//10
print(f'The addition of the digits is: {sum}')