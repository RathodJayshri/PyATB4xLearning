

#User defined functions
def make_pizza(*toppings):
    for topin in toppings:
        print(topin)

jayshri = make_pizza("tomato", "capsicum")

# Built in functions
r = max(1,2,3,4,5,7)
print(r)


def make_pizza(*toppings, base):
        print(toppings,base)

make_pizza("mushroom", "tomato", base = " thin crust") # here we can take only one base

