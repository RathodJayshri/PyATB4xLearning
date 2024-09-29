# print('hello jayu')
#
# list1 = [1,2,3,4,5,6,7]
# def sum_even_odd(list1):
#     even = 0
#     odd = 0
#
#     for i in list1:
#         if i % 2 == 0:
#             even = list1[i+1]
#         else:
#             odd += i
#     return even, odd
#
# even_sum, odd_sum = sum_even_odd(list1)
# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)



# X = [1,2,3,4,5,6,7]
#
# X1 = []
# X2 = []
#
# for  i in range(len(X)):
#
#     if i%2==0:
#         print(i, "==========")
#         X1.append(X[i]+2)
#     else:
#         X2.append(X[i]+1)
# print(X1)
# print(X2)


X = [1, 2, 3, 4, 5, 6, 7]

# Add 2 to elements at even indices
for i in range(0, len(X), 2):  # Start from index 0 and step by 2
    X[i] += 2

print(X)





