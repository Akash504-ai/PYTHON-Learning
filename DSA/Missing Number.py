arr = [3, 0, 1]

x = len(arr)
y = x*(x + 1) // 2

total = 0
for i in arr:
    total += i

print(y-total)