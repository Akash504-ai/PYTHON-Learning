arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

count = 0
maximum = arr[0]

for i in arr:
    count += i

    if count < 0:
        count = 0

    if count > maximum:
        maximum = count

print(maximum)