library = []

def make_books(title, author, genre, book_id):
    my_books = {
        'book_id': book_id,
        'title': title,
        'author': author,
        'genre': genre,
    }
    library.append(my_books)
name = input('What is your name')
print("Welcome to the library %s." % (name))
   
book_id = 0

while True:
    interface_book = input("Do you want to [A]dd a new book, [R]emove a book or [C]heck the library or [E]xit")
    if interface_book == "A":
        title = input("What is the title of your book")
        author = input("Who is the author of your book")
        genre = input("What is the genre of your book")
        book_id = book_id + 1
        add_book = make_books(title, author, genre, book_id)

    if interface_book == "R":
        id_check = input("What is the book id")
        for dictionary in  library:
            if dictionary['book_id'] == id_check:
                library.remove(dictionary)
    if interface_book == "C":
        print(library)

    if interface_book == "E":
        break
        
        
   



    
