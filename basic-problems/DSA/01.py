# find the missing number in the array

arr = [1, 2, 3, 5, 6, 7]
n = len(arr) + 1
sum = 0
for val in arr:
    sum = val + sum

actsum = n * (n + 1) / 2
# print(actsum)
# print(sum)

print("The missimg no is :", int(actsum - sum))
