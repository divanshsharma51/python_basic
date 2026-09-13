#for loop to print values of the list 
fruits = ["apple","banana","cherry","orange"]

for x in fruits: 
    print(x)
    
    
    
    
#to find the idx in list using for loop
num = (2,4,5,5,1,7,8,2,4)

x = int(input("Search your no. :"))

idx = 0
for el in num:
    if el == x:
        print("your no. found at ",idx)
        break
    idx += 1
    
else:
    print("Your no. is not in the list ")
    