# Conditions and Loops

# Write a program to take a user age and let him know if he can go the club.
# 21

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.


# 2. Rough loigc
# age  > 21 -> print can go
# age < 21 -> print can't go


# 3. write the logic
age = input("Enter you age\n")
age = int(age)

if age >= 21:
    print(f"Can go Club -> {age}")
else:
    print(f"Can't go with this age -> {age}")





#a = 10 # this is assignment -
#== -> true or false
a = 19 # int - whole numbrs -1, 2, 3

print(type(a))
if a == 10:
    print("Hello World")
else:
    print("Not Hello")



# Problem to find the max between two

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 3. - input method
# 31.4 or 45.34

num1 = float(input("Enter the num1\n"))
num2 = float(input("Enter the num2\n"))

if num1 > num2:
    print(f"Max is {num1}")
else:
    print("Max is ", num2)
    print(f"Max is {num2}")




# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

# Logic ?  If else - 1 condition
# more 1 condition -> if elif else

# Syntax
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("do 2")
# elif condition 3:
#     print("do 4")
# else:
#     print(" do 4")=


num1 = int(input("Enter the num1\n"))  # 5 , # 10
num2 = int(input("Enter the num2\n"))  # 3 , # 12
num3 = int(input("Enter the num3\n"))  # 2 , # 11

#  5 > 3 and 5 > 2 -> true -> 5
# num 1 >  num2  and num 1 > num 3 ->  num 1

#  12 > 10 and 12 > 11 -> true -> 12
# num 2 >  num1  and num 2 > num 3 ->  num 2

# num 3

if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:
    print("Max is ", num3)

result = max(num1, num2, num3)
print(result)





# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 ->  O/p -> str -> A or B....

score = int(input("Enter your score\n"))
# score >=90 and scroe <=100 -> "A"
# score >=80 and scroe <=89 -> "B"

if score >= 90 and score <= 100:  # Simplified Chaining Format -> 90 <= score <= 100
    print("You grade is ", "A")
elif score >= 80 and score <= 89:
    print("You grade is ", "B")
elif score >= 70 and score <= 79:
    print("You grade is ", "C")
elif score >= 60 and score <= 69:
    print("You grade is ", "D")
elif score >= 100:
    print("You are  Superman!!")
else:
    print("You grade is ", "F")





# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 ->  O/p -> str -> A or B....

score = int(input("Enter your score\n"))
# score >=90 and score <=100 -> "A"
# score >=80 and score
# <=89 -> "B"

if 90 <= score <= 100:  # Simplified Chaining Format -> 90 <= score <= 100
    print("You grade is ", "A")
elif 80 <= score <= 89:
    print("You grade is ", "B")
elif 70 <= score <= 79:
    print("You grade is ", "C")
elif 60 <= score <= 69:
    print("You grade is ", "D")
elif score >= 100:
    print("You are  Superman!!")
else:
    print("You grade is ", "F")
