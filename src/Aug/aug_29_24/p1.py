my_list = [1, 3, 5, 4, 7, 9]

# Create a list of tuples (index, value)
index_value_pairs = [(index, value) for index , value in enumerate(my_list)]

# Print the result
print(index_value_pairs)


my_list = [1, 3, 5, 4, 7, 9]
#enumerate(my_list) generates pairs of indices and values,
# Use enumerate to get index and value
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
    # print(f"At Index  {index}, Value is : {value}")
