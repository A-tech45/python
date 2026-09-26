#count positive numbers
arr = [ 1 , 2 , -2 , 4 , -7]
count = 0
for num in arr:
    print(num)
    if int(num) > 0:
        count += 1

print(count)