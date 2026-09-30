# revising logics 
str = "akasheoo"
vowel = [ "a","e","i","o","u" ]
i = 0
count = 0
for val in str :
    if vowel.__contains__(val) :
        count += 1
        print("found")
    else:
        print("notfound")

print("The number of vowels are :" ,count)