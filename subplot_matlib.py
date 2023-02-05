import matplotlib.pyplot as plt
x = [1,2,3]
y = [4,5,6]
z = [10,20,30]
y = ['A','B','C']
plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.bar(y,z)