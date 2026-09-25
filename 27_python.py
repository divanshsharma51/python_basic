#recursion func for calculating sum of n numbers
def num(n):
  
   
    if ( n == 0):
        return 0
    else:
      return n + num(n-1) 
       
    
print(num(10))




#to print all elements of the list 
def print_list(list,idx=0):
    if (idx == len(list)):
        return
    else:
        print(list[idx])
        print_list(list,idx +1)
    
    
numbers = [1,2,3,4,5]
print_list(numbers)