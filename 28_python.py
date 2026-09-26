#FILE I/O
#reading a text file 
f = open("demo.txt","r")

data = f.read()

# line = f.readline()  
# line2 = f.readline()
# print(line)
# print(line2)        #to print line by line 

print(data)
print(type(data))

f.close()