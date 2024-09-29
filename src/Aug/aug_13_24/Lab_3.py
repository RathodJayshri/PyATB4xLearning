"""
number = 3.14159265359
formated_number = f"{number : .3f}"
formated_number = f"{number : .4f}"
print(formated_number)


table = 4
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")
"""

table = 5
for i in range(1,11):
    # print(f"{table} * i = {table*i}")
    print(f"{table * i}", end=',')





# num1 = int(input("Enter the num1 : "))
# num2 = int(input("Enter the num2 : "))
#
# print(num1+num2)



table = 7
for i in range(1,11):
    print(f"{table} * i = {table*i}")


table = int(input("enter table number which you want:"))

for i in range(1,11):
    print(f"{table} * i = {table * i}")


