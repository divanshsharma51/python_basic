#to find the number in a tuple 
tup = (1,4,5,7,8,9,3,3,5)

num = int(input("Search your no. :"))

i = 0 
while i < len(tup):
    if tup[i] == num:
        print("your number found at index :", i)
        
    i += 1
