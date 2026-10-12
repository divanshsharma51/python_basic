#Super Method
class car:
    
    def __init__(self,type):
        self.type = type 
        
    @staticmethod
    def start():
             print( "car started....")
         
    @staticmethod
    def stop():
             print( "car stoped.....")   
    
    
    
class TATA(car):
    
    def __init__(self,name,type):
        super().__init__(type)        # super method to access the methods of parent class
        self.name = name
        super().start()
        

c1 = TATA("Nexon","Electric")
print(c1.name)
print(c1.type)