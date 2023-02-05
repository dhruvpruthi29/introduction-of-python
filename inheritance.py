class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
class labrador(dog):
    pass
x = labrador("jacky", "7")
print(x.name)
print(x.age)