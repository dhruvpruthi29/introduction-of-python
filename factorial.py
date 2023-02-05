n = int(input('Enter a Number: '))
fact = 1
if n==0 or n==1:
    print('factorial is: 1')
else:
    for i in range(n,0,-1):
        fact  = fact*i
    print(f'the factorial is {fact}')