#sum of n numbers using while loop 
n = 5 
sum = 0

i = 1
while i < n + 1 :
    sum += i 
    i += 1

print("sum of n no. : ",sum)





#using for loop to calculate sum of n number's factorial
n = 5 
fact = 1 # cant take fact as 0 

for i in range(1,n+1):
    
    fact *= i 
    
print("sum of factorial of n numbers :",fact)