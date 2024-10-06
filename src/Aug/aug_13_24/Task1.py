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

number1 = int(input("enter number1 here:"))
number2 = int(input("enter number2 here:"))

print(f"the max number from number1 and number2 is:{max(number1, number2)}")

No1 = 22
No2 = 11

if No1 > No2:
    print("No1 is greater")
else:
    print("No2 is greater")