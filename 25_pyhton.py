#function to print factorial of n
def print_fact(n):
   fact = 1
   for i in range(1,n+1):
      
      fact *= i
   print(fact)   
   
   return fact   

num = int(input("Enter your no. : "))      
print_fact(num)
   


#function to covert USD into INR
def cal_inr(usd):
    inr = usd * 95.9
    print(usd,"USD = ",inr,"INR")
    
 
usd = int(input("Enter usd : "))
cal_inr(usd)



#Function of odd nd even
def cal_num(num):
    if num % 2 == 0:
        print("EVEN")
    
    else:
        print("ODD")
    

value = int(input("Enter your no. : "))    
cal_num(value)