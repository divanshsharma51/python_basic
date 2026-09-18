#range in loops 

for i in range(10):  #range(stop)
    print(i)
    
    
for j in range(2,10): # range(start,stop)
    print(j)
    
    
for h in range(2,10,2): #range(start,stop,step)
    print(h)






#to print multiplication table of no. using for loop ]
n = int(input("Enter your no. :"))

for i in range(1,11):
    print(f"{n}*{i} =",n*i)

