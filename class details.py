class dog:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def dogdetails(self):
        print(self.name)
        print(self.age)
x = dog("Jacky","7")
y = dog("Tuffy", "4")
x.dogdetails()
y.dogdetails()
