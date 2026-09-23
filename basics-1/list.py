l1 = ["apple","mango","banana"]
print(l1[1:1])

l1[1:1] = ["kiwi" , "potato"] # inserts element 
print(l1)

l1[1:3] = [] # delete element from index 1 - 2  , 3 is not included

l1[1:3] = ["chaddi" , "baniyan"]  # replaces the element from 1-2 with chaddi and baniyan
print(l1)

l1[1:2] = "chaddi"  # chaddi is treated as an array and inserted so always use [] for inserting elements

print(l1)
