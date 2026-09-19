arr = [2, 2, 1, 1, 1, 2, 2]

count = 0
number = 0

for i in arr:
    if count == 0:
        number = i

    if  i == number:
        count += 1
    else:
        count -= 1

print(number)