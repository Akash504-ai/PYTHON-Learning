arr = [0, 1, 0, 3, 12]

ans = []

for i in range(len(arr)):
    if(arr[i] != 0):
        ans.append(arr[i])

while len(ans) < len(arr):
    ans.append(0)

print(ans)
