arr = [2, 2, 1, 1, 1, 2, 2]

num = 0
ans = 0

for i in arr:
    if ans == 0:
        ans = i

    if i == ans:
        num += 1
    else: 
        num -= 1

print(ans)