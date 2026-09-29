arr = [1, 2, 3, 1]

seen = set()

for i in arr:
    if i in seen:
        print(True)
        break
    seen.add(i)
else:
    print(False)