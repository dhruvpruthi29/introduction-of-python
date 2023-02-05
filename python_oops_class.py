class dog:
    def details(self, name, age):
        self.name = name
        self.age = age
x = dog()
x.details("Jacky","7")
print(x.name)
print(x.age)