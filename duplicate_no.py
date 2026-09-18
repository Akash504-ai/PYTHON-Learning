arr = [1, 2, 3, 1]
seen = set()
for num in arr:
    if num in seen:
        print(True)
        break

    seen.add(num)
else:
    print(False)