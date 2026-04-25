class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_available=True
class User:
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]
    
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} added")
    def show_available_books(self):
        print("Available books: ")
        found=False
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")
                found=True
        if not found:
            print("No books available")
    def issue_book(self,user,title):
        for book in self.books:
            if book.title==title:
              if book.is_available:
                  book.is_available=False
                  user.borrowed_books.append(book)
                  print(f"{title} issued to {user.name}")
              else:
                  print(f"{title} is already issued")
              return
        print(f"{title} not found in library")
    def return_book(self,user,title):
        for book in user.borrowed_books:
            if book.title==title:
                book.is_available=True
                user.borrowed_books.remove(book)
                print(f"{title} returned by {user.name}")
                return
        print(f"{user.name} does not have this book")

    
b1 = Book("Python Basics", "Guido")
b2 = Book("Java Fundamentals", "James")
b3 = Book("Data Structures", "Mark")
u=User("Dhatri")
lib=Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.show_available_books()
lib.issue_book(u,"Python Basics")
lib.return_book(u, "Python Basics")
lib.show_available_books()
