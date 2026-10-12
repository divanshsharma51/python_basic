#Guessing a no.
import random

randnum = random.randint(0,100)

attempt = 0 

while True:
    num = input("Guess a number between 1 to 100 or q to quit : ")
    
    
    if num == "Q" or "q":
      print("GAME QUIT!!")
      break
      
    num = int(num)
    if num == randnum:
      print("You Got it!!")
      break
    
    
    if num < randnum:
     print("Your number is small")
   
    
    else:
     print("Your number is big")
    
    attempt += 1
    
   
print("ATTEMPTS TAKEN :",attempt)
