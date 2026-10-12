#class method
class Person:
    
    name = "anonymous"
    
    @classmethod                 # decorator
    def changename(cls,name):    # it is used to access/change the same attri inside a class
        cls.name = name
    
    #def __init__(self,name)              - can be done by this too
    #     self.__class__.name = name           __class__ refers to Person class
        
p1 = Person()
p1.changename("rahul")           
print(p1.name)
print(Person.name)       # if we dont use class method here it will print anonymous instead of rahul..





#Property method
class Marks:
    
    def __init__(self,phy,chem,bio):
        self.phy = phy 
        self.chem = chem
        self.bio = bio
        
        
    @property                        #decorator to use any method as property
    def persentage(self):
        return (str((self.phy + self.chem + self.bio)/ 3 )) + "%"
    
    
s1 = Marks(65,79,76)
print(s1.persentage)
 
s1.phy = 71               # it would show previous persentage even after updating marks if we didnt use property method
print(s1.persentage)