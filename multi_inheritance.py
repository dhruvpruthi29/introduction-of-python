class dog:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
class labrador(dog):
    def __init__(self,name,age,master):
        super().__init__(name,age)
        self.master = master
x = labrador("jacky","7","smith")
print(x.name)
print(x.age)
print(x.master)