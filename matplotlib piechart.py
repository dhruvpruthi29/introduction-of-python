import matplotlib.pyplot as plt 
x = ['A','B','C'] 
y = [1,2,3]
z = [0.2,0,0]
plt.pie(y, labels=x, explode =z, shadow=True)


import matplotlib.pyplot as plt 
x = ['A','B','C'] 
y = [1,2,3]
plt.pie(y, labels=x)
