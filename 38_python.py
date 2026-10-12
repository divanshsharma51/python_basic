#Static Method
class greet:
    
    @staticmethod    #decorator = changes the behaviour of normal func
       
    def hello():        #no need of self parameter as we used static method
        print("hello everyone ")

g1 = greet()
g1.hello()


# Abstraction = hiding unecessary details and showing only essential details to user
# Encapsulation = warpping all data and func into a single unit 