# print('Hello')
# print('Hello') # tap ctrl d to duplicate


list1 = [1,2,3,4,5,6,7]
def sum_even_odd(list1):
    sum_even = 0
    sum_odd = 0

    for i in list1:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_even, sum_odd

even_sum, odd_sum = sum_even_odd(list1)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)






