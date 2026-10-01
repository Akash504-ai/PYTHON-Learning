# While

# i = 1
# while i <= 5:
#     print(i, end = " ")
#     i+=1

# ------------------------------ #

# Sum of numbers from 1 to 10 --> 
# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
    
# print(sum) # 55

# ------------------------------ #

# Multiplication table

# n = int(input("Enter no : "))
# i = 1
# while(i <= 10):
#     print(f"{n} * {i} = {n*i}")
#     i += 1

# -------------while loop end here----------------- #

# -------------for loop end here----------------- #

# for i in range(1, 6):
#     print(i)

# ------------------------------ #
# From 2 to 10, increment by 2
# for i in range(2, 11, 2):
#     print(i)

# -------------Brek statement----------------- #
# while True:
#     number = int(input("Enter a number (0 to exit): "))

#     if number == 0:
#         break

#     print("You entered:", number)

# print("Program ended")

#--------------------lambda--------------------#

# Normal function
def sq(n):
    return n * n
print(sq(5))

# lambda function
sq = lambda n: n*n
print(sq(6))

add = lambda a, b: a*b
print(add(9,9))