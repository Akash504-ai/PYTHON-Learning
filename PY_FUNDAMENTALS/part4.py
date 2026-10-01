# ------------ Python Tuples ------------ #
numbers = (10, 20, 30, 40, 50)
print(numbers)
print(type(numbers))

student = ("Akash", 21, 7.07, True) # A tuple can contain different data types
print(student)

print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[-1])  # 50

# Here also has slicing

# Tuples are immutable
# numbers[0] = 100
# print(numbers) # this'll give err

numbers = (10, 20, 30, 20, 40, 20, 30)

print(numbers.count(20))  # 3
print(numbers.index(30))  # 2

print("=====built-in functions=====")

num = (10,20,30,40,50,60,70,80,90,100)
print(max(num)) #100
print(min(num)) #10
print(len(num)) #10
print(30 in num) #True
print(sum(num)) #550

# Where are tuples used in development? ---> 
# Coordinates (location = (22.57, 88.36))
# Returning multiple values
# Dictionary keys