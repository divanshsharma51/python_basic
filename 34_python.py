#OOPs
class Student:    #Creting CLASS Student
    name = "Karan"  #Creating ATTRIBUTES name , age
    age = 18
    
s1 = Student()   #Creating OBJECTS
print(s1.name)       #     s1 n s2
print(s1.age)

s2 = Student()
print(s2.name)
    


#init function 
class car: 
    color = "blue"
    
    def __init__(self):           #definig init   /  self is to define c1 
        print("color of car is")
        
        
c1 = car()        #() is used to call init function
print(c1.color)   #to print other object
    