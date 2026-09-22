string1 = "hello world"
#now if i want only world then i can use slice here
print(string1[6:11]) # picks string from index 6(if 6 takes letter from 7 6 not included) till 11
#prints world

print(string1[0:5]) # 0 included but 5 not included
# prints hello

#^ We can see the real working here 

l = "0123456"
print(l[:4])   # prints till 3 , 4 excluded as 0 , 1 , 2 , 3  are 4 numbers 
print(l[:-4])   # prints till 2 . -4 is counted 4 from backward
print(l[-5:-4])   # prints 2 as we have started from -5(2)included till -4(3) not included 
print(l[-3:-4])   # prints nothing as we started from -3(4) till -4(3) we cannot print reverse
print(l[:])    # prints as it is 
print(l[:7:2])    # prints till 6 but with increment of 2 eg: 0 , 2 , 4 , 6
 

 