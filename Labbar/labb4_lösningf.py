#övning 1

# def magical_stairs():

#     print("Välkomna till den Magiska Trappan")

#     for i in range(1,21):
#         #Kontroll, delbart med 3?
#         if i % 3 == 0:
#             print(f'Ett magiskt hinder här!')
#         else:
#             print(f'Kliver på trappsteget {i} och finner en gnistrande magi')


# magical_stairs()

#----------------------------------------------------------------------------------------------------

#Övning 2

# def mystical_show(mystical_items):
#     print("Välkomna till Rollkalles magiska föreställning")

#     for index, mystical_item in enumerate(mystical_items, start = 1):
#         print(f"Magi#{index}: {mystical_item}")
    
# #Skapa lista med magiska föremål
# mystical_items = ["Svävande hatt", "Oförstörbart trollspö", "Invisibility Cape", "Försvinnande kanin"]

# #Anropa funktionen
# mystical_show(mystical_items)

#----------------------------------------------------------------------------------------------------

#En tom dictionary->lagra studenternas namn och betyg.
students = {}

#Funktion lägga till student och betyg

def add_student():
    name = input("Ange studentens namn: ")
    grade = int(input("Ange studentens betyg: "))

#Uppdatera eller lägga in
    if name in students:
        students[name] = grade
        print(f'Betyget för {name} har uppdaterats till {grade}.')
    else:
        students[name] = grade
        print(f'{name} har lagts till med betyget {grade}')

#För att visa studentlistan
def show_students():
    #Inga elever..
    if not students:
        print('Inga studenter registrerade ännu.')
    else:
        print('Studentlista:')
        for name, grade in students.items():
            print(f'{name}: {grade}')

#För högst betyg
def get_top_student():
    if not students:
        print('Inga studenter registrerade ännu.') 
    else:      
        top_student = max(students, key=students.get)
        return f'Bästa student: {top_student} med betyg {students[top_student]}'

#Evig loop
while True:
    print('\n Välj en åtgärd:')
    print('1. Lägg till student och betyg')
    print('2. Visa studentlista')
    print('3. Hitta bästa studenten')
    print('4. Avsluta programmet')

    choice = input('Ange ditt val (1-4):')

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        print(get_top_student())
    elif choice == '4':
        print('Programmet avslutas. Hej då!')
        break
    else:
        print('Ogiltigt val. Försök igen.')





                         

    
