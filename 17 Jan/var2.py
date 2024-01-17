#Data strukturer

#Exempel 1

# values = [1, 2, 3]
# values.append(4)
# print(values)

values = [1, 2, 3]
values.remove(2)
print(values)

#Exempel 2

values2 = (1, 2, 3)
print(type(values2))

#Exempel 3

# values3 = {1, 2, 3}
# print(type(values3)) 

values3 = {1, 2, 3, 3, 2, 4, 1, 1}
print(values3)

#Exempel 4

values4 = {
    "name" : "Pelle",
    "age": 20,
    "email": "pelle@email.com"
}


print(values4["email"])

