# values = [1, 2, 3, 4]

# new_values = []

# for value in values: 
#     new_values.append(value**2)


# print(new_values)

#Comprehension

# values = [1, 2, 3, 4]


# new_values = [value**2 for value in values]
# print(new_values)

# values = [1, 2, 3, 4]

# new_values = []

# for value in values: 
#     if value % 2 == 0:
#         new_values.append(value**2)


# print(new_values)

values = [1, 2, 3, 4]

new_values = [value**2 for value in values if value % 2 == 0]
print(new_values)
