#Exempel 1

i = 10
j= 10
print(id(i))
print(id(j))

i+=1
print(id(i))


#Exempel 2

name1 = "John"
name2 = "John"

print (id(name1))
print (id(name2))

name1 = "Alice"
print (id(name1))
print (id(name2))

name2 = name2.replace('o', 'a')
print(name2)


