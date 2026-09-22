

1 == 1 # true

1 == 3 # false

1 == 3 < 4 #false it is evaluated as 1 == 3 and 3 < 4 . here 1 == 3 gives false so false

3 == 3 < 6 # gives true 

# ** means power eg:

print(3**3)  # 3 to the power 3 = 27

# floor function 
import math
print(math.floor(3.5)) # this will give an error if u have not imported the maths library
# >> gives 3 

## Random function . u have to import it
import random
print(random.random())

# IF  u want to print between two numbers than
# then use :-
print(random.randint(2 , 5))  # prints any number between 2 , 5  includes 5
print(random.randrange(2 , 5))  # prints any number between 2 , 4 doesnot include 5

#another one is suffle 
#take a list l1 :
l1 = [ 'mango' , 'banana' , 'apple']

y = int(input())

if y == 2 :
    random.shuffle(l1)   # changes the original value
    print(l1)
else :
    print("404")

print(l1)