#1 - string

name = "hello"

print(name[1])
print(name[1:])
print(name +  "op")

  # dictionart datatype
myD  = { 'comic' : 'marvel' , 'dc' : 'superman'}

myD['comic'] = "Superhero"  # dictionaries are mutable
print(myD['comic'])

tup = (1,2,3)
#! tup[0] = 4   -- Will give an error as tuples are inmutablel 
print(tup[0])

print(len(tup))   #len() function gives the length of anything


# list datatype

l1 = [2 , 4]
l2 = l1
l1[0] = 43
print(l1)
print(l2)

x = 10 
y = x   

x = 43
print(y)

#range data type
for i in range( 2 , 9 , 3):  # range(start , stop , step) step is the increment the default is 1
    print(i)

