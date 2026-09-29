arr = [2, 3, -2, 4]

maximum = arr[0]
for i in range(len(arr)):
    product = 1
    for j in range(i,len(arr)):
        product = product * arr[j]
        if product > maximum:
            maximum = product

print(maximum)