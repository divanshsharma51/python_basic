#Methods in Class
class result:
    
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def hello(self):           # Functions inside a class called as METHODS
        print("Hello students,",self.name)
        
    def get_marks(self):
        return self.marks
    

r1 = result("karan",86)
r1.hello()
print(r1.get_marks())