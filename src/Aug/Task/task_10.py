# Task #10 -
#Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# # Example usage
# number = int(input("Enter a number: "))
# print(f"The factorial of {number} is {factorial(number)}")



n = int(input("Enter a number: "))
def factorial(n):
    if n < 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(f"The factorial of {n} is {factorial(n)}")
