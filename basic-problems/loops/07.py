# Check  prime number
# Can be optimised further
number = 2;
chek = []
for i in range(1 , number + 1 ):
    if number % i == 0 :
        chek.append(i)

if len(chek) == 2:
    print("Its a prime number")

else:
    print("Its not a prime number")