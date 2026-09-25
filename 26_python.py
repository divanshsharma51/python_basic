#Recursion 
def show(n):
    if n == 0 :#Base case
        return
    print(n)
    show(n-1)
    print("END")
    
show(5)
  
    


# recursion to count factorial of a number     
def fact(n):
    if ( n == 1 or n == 0):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(3))


