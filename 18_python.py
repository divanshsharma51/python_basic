#while loop 
count = 1
while count <= 10:
    print("hello",count)
    count += 1
    
    
#for any number's table
n = int(input("Enter your no."))
i = 1 
while i <= 10:
    print(f"{n}*{i}=" ,n*i)
    i += 1


#to print the value of index
fruits = ["apple","banana","cherry","orange"]

idx = 0 
while idx < len(fruits):
    print(fruits[idx])
    idx += 1
