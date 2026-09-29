arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sum = 0
max_sum = 0

for i in arr:
    sum += i

    if(sum < 0):
        sum = 0

    elif sum > max_sum:
        max_sum = sum

print(max_sum)