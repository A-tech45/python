# ok tuples are inmutablse 
tup = ("chai" , "masala" , "ginger" , "chai")
tup2 = ("chindi", "chinda" , "minda")
# Can add two tuples 
tup3 = tup + tup2

# ok if we want to find the count of an element we can use count() function\
# Eg:
print(tup.count("chai"))

# And all other functions that are applicable in list are  also applicable in tuple 
# like 
tup[0] # etc etc 

# we can tranfer values directly into variables 
# Eg:
(chai , masala , ginger , chai) = tup
print(chai) 

# See "chai"  value is saved in chai 

print(type(tup))

# there can be nested tuples 
# EG:
tup4 = ( "chai" , ( 1, 2, 3) , ("main"))