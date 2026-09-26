#Function to replace a word in a file
def replace_word(old_word,new_word):

    with open("demo4.txt","r") as f:
     data = f.read()
    
    new_data = data.replace(old_word,new_word)
    
    with open("demo4.txt","w") as f:
     f.write(new_data)
    

replace_word("java","python")