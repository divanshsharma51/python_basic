#function for counting length of the list
def len_list(list):
   print(len(list))
   return len(list)

#to print list in same line 
def print_list(list):
   for item in list:
      print(item,end = " ")



city = ["mumbai","delhi","pune","noida"]
num = [2,3,4,1,4,1,5,7]

len_list(city)
print_list(num)

