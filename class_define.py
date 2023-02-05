class dog:
    breed = 'Labrador'
    def details(self, name, age):
        self.name = name
        self.age = age
x = dog()
x.details("Jacky", "7")
print(x.name+' is a '+x.breed+' dog')