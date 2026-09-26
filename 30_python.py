#with syntax auto closes the file 
with open("demo3.txt","r") as f:
    data = f.read()
    print(data)
    
    
with open("demo3.txt","w") as f:
    f.write("write overwrites the data")
    
    

#to delete the file we need to import a library first
import os 

os.remove("filename")
