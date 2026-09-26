# Total of even numbers
arr = [ 1 , 2, 3, 4, 5, 6, 7 , 2]
tot = 0
for num in arr:
    if(num % 2 == 0):
        tot += num

print(tot)