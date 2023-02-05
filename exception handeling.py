x = 10
try:
    print(x)
except:
    print("x is not defined!")
else:
    print("z is already defined!")

finally:
    print("I am in finally block.")