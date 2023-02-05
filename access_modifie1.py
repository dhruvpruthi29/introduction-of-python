class dog:
    __legs=4
    _breed='Labrador'
    print(__legs)
    
    def __init__(self,name):
        self.name = name
        
class age(dog):
    __year=2022
    def __init__(self,name,age):
        dog.__init__(self,name)
        self.age = age
        
x=dog('charly')
y=age('jacky',"7")
print(x.name,x._breed)
#uncommeting lines below gives error as __legs is private
#print(x.name,x__legs)
    