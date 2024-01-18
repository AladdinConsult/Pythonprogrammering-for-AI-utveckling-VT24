# 3 func....regga elever....visa elever....uppdaterar...
# regga....visa elever....uppdatera


#Del 1 Regga elever f
def registrera_student(namn, ålder, kurser):
    return {'namn':namn, 'ålder': ålder, 'kurser': kurser}

#Del 2 visa elever f
def visa_student(student):
    print(f"Namn: {student['namn']}, Ålder: {student['ålder']}, Kurser: {student['kurser']}")

#Del 3 Uppdatera f
def uppdatera_student_kurser(student, nya_kurser):
    student['kurser'] += nya_kurser

#Del 4 Regga elever
alice = registrera_student('Alice', 20, ['Pythonprogrammering', 'Databasdesign'])
bob = registrera_student('Bob', 22, ['Pythonprogrammering'])

#Del 5 Visa elever
print('Information om Alice:')
visa_student(alice)

print('\nInformation om Bob:')
visa_student(bob)

#Del 6 Uppdatera

uppdatera_student_kurser(bob, ['Datastrukturer'])

print("\nUppdaterad information om Bob:")
visa_student(bob)