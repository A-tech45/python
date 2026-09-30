# revising logics 
str = "bcdfghj"
vowel = [ "a","e","i","o","u" ]
i = 0
count = 0
for val in str :
    if vowel.__contains__(val) :
        print("Not a consonent")
    else:
      count += 1
      

print("The number of consonent are :" ,count)