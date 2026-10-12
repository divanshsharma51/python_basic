#Inheritence

class car:
     
    @staticmethod
    def start():
        return "car started...."
    
    @staticmethod
    def stop():
        return "car stoped....."
    
class TATA(car):                 #Single-level Inheritence 
                                 # child class inherites the property of parent class
    def __init__(self,brand):
        self.brand = brand
    
    
class Nexon(TATA):                # Multi-level Inheritence
                                  # child class inherites the property of multiple parent class
    def __init__(self,type):
        self.type = type

   
c1 = Nexon("Petrol")
print(c1.start())   



class A:
    varA = "welcome to a class"
    
class B:
    varB = "welcome to b class"
    
class C(B,A):                          #Multiple Inheritence
    varC = "welcome to c class"


c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)