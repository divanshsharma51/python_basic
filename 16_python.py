#to prove wheather list is palindrome or not
list1 = [1,2,3,5,2,5,3,2,1]
copy1 = list1.copy()
(copy1.reverse())

if( copy1 == list1 ):
    print("palindrome")
    
else:
    print("not palindrome")