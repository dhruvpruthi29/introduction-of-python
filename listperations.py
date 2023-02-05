a = []
n = int(input('Enter the number of elements: '))
for i in range(0,n):
    x = int(input('Enter the element: '))
    a.append(x)
y = max(a)
z = min(a)
avg_value = sum(a)/len(a)
print(f'Maximum value is: {y}')
print(f'Minimum value is: {z}')
print(f'average value is: {avg_value}')