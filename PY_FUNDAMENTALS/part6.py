numbers = {10, 20, 30}
print(numbers)

numbers.add(40)
print(numbers)

numbers.update([50, 60, 70])
print(numbers)

numbers.remove(20) # Removes 20; error if missing
print(numbers)

numbers.discard(50) # Removes 50; no error if missing
print(numbers)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B) # Union
print(A & B) # Intersection
print(A - B) # Difference