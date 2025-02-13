class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object_ref = Calc(3, 4)
object_ref2 = Calc(3, 4)
object_ref3 = Calc(3, 4)
object_ref4 = Calc(3, 4)
output = object_ref.sum()
print(output)



#  Class Variable.
#  Method
#      # Public - Variable - Don't Mention anything
#      # Protected - _
#      # Private - __
# Inheritance
# Polymorphism
# Abstraction,
# Encapsulation
# Static Method
# Variables


# Variables
# 1. Local Variable (within the functionc / block
# 2. global
# 3. instance variable (within the class
# 4. static variable ( in future)