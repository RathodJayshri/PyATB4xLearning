'''
### Task #8

✅ Triangle Classifier:





![img.png](img.png)





Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
'''




def classify_triangle(a, b, c):
    """
    Classify a triangle based on its side lengths.

    Args:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    str: Classification of the triangle ("Equilateral", "Isosceles", or "Scalene").
    """



   # Check if the sides form a valid triangle
#     if a + b > c and a + c > b and b + c > a:
#         if a == b == c:
#             return "Equilateral"
#         elif a == b or b == c or a == c:
#             return "Isosceles"
#         else:
#             return "Scalene"
#     else:
#         return "Not a triangle"
#
# def main():
#     try:
#         a = float(input("Enter the length of the first side: "))
#         b = float(input("Enter the length of the second side: "))
#         c = float(input("Enter the length of the third side: "))
#
#         classification = classify_triangle(a, b, c)
#         print(f"The triangle is {classification}.")
#     except ValueError:
#         print("Please enter valid numerical values for the side lengths.")
#
# if __name__ == "__main__":
#     main()

# ==================================================================================================

# a = float(input("Enter the length of the first side: "))
# b = float(input("Enter the length of the second side: "))
# c = float(input("Enter the length of the third side: "))
#
#
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print( "Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print( "Scalene")
# else:
#     print("Not a triangle")

# ====================================================================================


a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))



# if a + b > c and a + c > b and b + c > a:
if a == b == c:
    print( "Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print( "Scalene")

