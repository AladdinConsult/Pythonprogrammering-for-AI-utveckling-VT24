#Skapa en klass Libary
class Libary:

    #Konstruktormetod
    def __init__(self, library_name):
        self.library_name = library_name
    
    #Strängrepresentation
    def __str__(self):
        return f"The city's libary, {self.library_name}"
    

#Skapa en klass Book som ärver från Libary
class Book(Libary):

    #Konstruktormetod
    #Använd super()
    def __init__(self, library_name, title, author, published_year):
        super().__init__(library_name)
        self.title = title
        self.author = author
        self.published_year = published_year
    
     #Strängrepresentation
    def __str__(self):
        return f'{super().__str__()}, has the book {self.title} by {self.author} published year {self.published_year}'
    
# skapa en instans av Libary
my_library = Libary("National Library")

# skapa 2 instanser av book
book1 = Book("National Library", "The Catcher in the Rye", "J.D Salinger", 1951)
book2 = Book("National Library", "To Kill a Mockingbird", "Harper Lee", 1960)

print(book1)
print(book2)

