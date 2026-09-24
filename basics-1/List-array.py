l1 = ["apple","mango","banana"]
print(l1[1:1])

l1[1:1] = ["kiwi" , "potato"] # inserts element 
print(l1)

l1[1:3] = [] # delete element from index 1 - 2  , 3 is not included

l1[1:3] = ["chaddi" , "baniyan"]  # replaces the element from 1-2 with chaddi and baniyan
print(l1)

l1[1:2] = "chaddi"  # chaddi is treated as an array and inserted so always use [] for inserting elements

print(l1)

l1.append("kiwi") # append is used to insert elements in the end of the  list
l1.pop() # pop is used to remove elements in the end of the  list
l1.remove("apple") # remove is used to remove the element u want from the list
print(l1)

l1.insert(1 , "graps")  # inserts graps in index pos 1
print(l1)


l1_copy = l1.copy() # creates another copy reference of the l1
l1_cope = l1 # This referes to the same memory location 
l1.append("books") # This also changes (the original list ) the list element in l1_cope (As List is mutable)

l1_copy.append("books") #this doesnot changes the original list as it stores copy of it ( another copy reference )