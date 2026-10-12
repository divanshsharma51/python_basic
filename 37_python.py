#To find avg of 3 numbers using methods in class
class student:
     
     def __init__(self,name,marks):
         self.name = name
         self.marks = marks
         
     def get_avg(self):
         sum = 0
         for val in self.marks:
             sum += val
         print("hi", self.name,"Your avg marks is = ",sum/3)
         
         
         
         
s1 = student("Divansh",[85,70,78])
s1.get_avg()
