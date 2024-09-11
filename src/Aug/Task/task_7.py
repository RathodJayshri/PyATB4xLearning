'''
### Task #7

✅ Leap Year Checker:



![img_1.png](img_1.png)



Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
'''

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# ==============================================================================================


# year = int(input("Enter a year: "))
#
# if (year % 4 ==0 and year % 100 != 0 ) or (year % 400 == 0):
#     print(print(f"{year} is a leap year."))
#
# else:
#     print(print(f"{year} is not a leap year."))


# ====================================================================================================

# year = int(input("Enter a year: "))
#
# if (year % 4 ==0 or year % 400 == 0 ) and ( year % 100 != 0):
#     print(print(f"{year} is a leap year."))
#
# else:
#     print(print(f"{year} is not a leap year."))