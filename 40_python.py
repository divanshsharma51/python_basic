# Private attributes and methods
class student:
     
     
    def __init__(self,name,acc_pass):
        self.name = name
        self.__acc_pass = acc_pass  # __ To convert into private attribute 
                                    #     cant access from outside the class
        
    def get_pass(self):             # To access private attri
       return  self.__acc_pass
    
    def __hello(self):
        print("Hello Everyone...")  # creating a private method only accessable within class
 
    def welcome(self):              # to access private method
       self.__hello()

s1 = student("rohan","ro123")
del s1                              # To delete a object

s2 = student("rahul","ra123")
           

print(s2.get_pass())                # to print private attri 
s2.welcome()