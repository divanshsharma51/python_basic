#OOPs
class Student:
    
    #Defualt Constructor
    def __init__(self):       #python wont use this constructor as parmeters dosnt match
        pass
    
    college_name = "ABC College"    #Common values should store as class attribute as it occupy less space
    
    #Parametrized Constructor      #It matches the parameters
    def __init__(self,name,marks):
       self.name = name   #obj attr > class attr
       self.marks = marks
       print("New student added and marks.....")
    
s1 = Student("karan",78)
print(s1.name,s1.marks,s1.college_name)
      
     
s2 = Student("arjun",85)
print(s2.name,s2.marks,Student.college_name)  #class.attri   also works  