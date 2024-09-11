"""
Create a program, take 2 inputs from the user num1, num2 give them max ,pow,mul, sum, div,sub.
format out with f{""}
"""
num1 = int(input("Enter number here:"))
num2 = int(input("Enter number here:"))

print(f"The max number from num1 and num2 is: {max(num1,num2)}")
print(f"The power of num1 is: {pow(num1,num2)}")
print(f"The mul of  num1 and num2 is: {(num1*num2)}")
print(f"The div is: {(num1/num2)}")
print(f"The sub is: {(num1-num2)}")
print(f"The sum is:{(num1+num2)}")
