#To count no. of even no. in a file
count = 0 
with open("demo5.txt","r") as f:
    data = f.read()
    
    num = data.split(",")
    for val in num:
        if (int(val) % 2 == 0):
            count += 1
            
print(count)