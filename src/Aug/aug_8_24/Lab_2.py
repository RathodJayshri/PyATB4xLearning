# print('hello jayu')
#
X = [1,2,3,4,5,6,7]

X1 = []
X2 = []

for  i in range(len(X)):

    if i%2==0:

        X1.append(X[i]+2)
    else:
        X2.append(X[i]+1)
print(X1)
print(X2)


# X = [1, 2, 3, 4, 5, 6, 7]
#
# # Add 2 to elements at even indices
# for i in range(0, len(X), 2):  # Start from index 0 and step by 2
#     X[i] += 2
#
# print(X)


#  add 2 is even index ele and 1 is odd index ele
X = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(X)):
    if i % 2 == 0:  # Even index
        X[i] += 2
    else:           # Odd index
        X[i] += 1

print(X)     # [3, 3, 5, 5, 7, 7, 9]



# print ele with index
# X = [1, 2, 3, 4, 5, 6, 7]
#
# for index, value in enumerate(X):
#     print(f'Index: {index}, Value: {value}')

X2 = [3,4,5,6,7,8,24,56,13]
for index, value in enumerate(X2):
    # print(f"Index: {index}, Value: {value}")
    print(f"{index} = {value}")

#  In Python, enumerate is a built-in function that adds a counter to an iterable (like a list or a tuple)
# and returns it as an enumerate object. This is particularly useful when you want to loop through an
# iterable and need both the index and the value of each element.


# add 3 in even numbers

X = [1, 2, 3, 4, 5, 6, 7]
result = []

for i in X:
    if i % 2 == 0:
        result.append(i + 3)

print(result)





