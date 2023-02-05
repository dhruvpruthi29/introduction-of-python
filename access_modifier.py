class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class dogbreed:
    def __init__(self,breed):
        self.breed = breed
class mydog(dog,dogbreed):
    def __init__(self,name,age,breed,master):
        dog.__init__(self,name,age)
        dogbreed.__init__(self,breed)
        self.master = master
x = mydog("jacky","7","labrador","smith")
print(x.name)
print(x.age)
print(x.breed)
print(x.master)