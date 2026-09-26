#Function to check whether the word exist in file or not 
def find_word(word):
   
    with open("demo4.txt","r") as f:
     data = f.read()
    if data.find(word) != -1:
        print(" The word found ")
    else:
        print("Not found")
        

find_word("python")  



#function to check the line word exists
def check_word(word):
    with open("demo4.txt","r") as f:
        line = 1
        data = True
        while True:
            data = f.readline()
            if  word in data :
                print("Your word is in line ",line)
                return
            line +=1
   
    print(-1)
            
    
check_word("python")