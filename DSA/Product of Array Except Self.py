arr = [1, 2, 3, 4]

for i in arr:
    p = 1
    for j in arr:
        if i != j:
            p = p * j

    print(p)