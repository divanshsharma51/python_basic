#Polymorphism = allows method/operator to behave diff according to object or datatype
class Complex:
    
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,obj2):                 # Dundern func
        Newreal = self.real + obj2.real
        Newimg = self.img + obj2.img
        return Complex(Newreal,Newimg)
  
  
    def __sub__(self,obj2):
        Newreal = self.real - obj2.real
        Newimg = self.img - obj2.img
        return Complex(Newreal,Newimg)
    
    
num1 = Complex(6,9)
num1.showNumber()

num2 = Complex(4,7)
num2.showNumber()

num3 = num1 + num2 
num3.showNumber()
        
    