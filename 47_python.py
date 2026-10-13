#Random Password Generator 
import random 
import string 

val = string.ascii_letters + string.digits + string.punctuation

pass_len = 8

password = "".join([random.choice(val) for i in range(pass_len)])

# password = 0
# for i in len(pass_len):
#   password += random.choice(val)          

print("Your Random Password =",password)