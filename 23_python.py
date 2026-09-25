# creating a function to print avg of 3 no.
def cal_avg(a , b, c):#parameters
   
   return (a + b + c) / 3 #return use to store the value after it executes

a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))


avg = cal_avg(a,b,c)#arguments
print("Your average is : ",avg)
