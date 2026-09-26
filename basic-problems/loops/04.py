#reverse a string
name = "Akash"
rev = " "
for n in name:
    rev = n + rev  # if u write rev + n this will not work
# Explanation :- rev = n + rev 
#  first n = A and rev = " " 
#  so by condition rev(" ") = n ( A )  + rev(" ") / = now rev = A
#  in next rev = A . so n(k) + rev(A)  = rev(ka)
#  Continue ....
print(rev)