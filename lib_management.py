class Book:
    def __init__(self, title, author, isbn, number):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.number = number
        self.lent = 0

    def details(self):
        return f"""
            Title: {self.title}
            Author: {self.author}
            ISBN: {self.isbn}
            Available in library: {self.number}
            Number of times lent to readers: {self.lent}
        """

    def lend(self):
        if self.number>=1:
            self.number-=1
            self.lent+=1

            return "Done!"
        else:
            return "Book not available!"

    def return_book(self):
        self.number += 1
        self.lent -= 1

    def is_available(self):
        return True if self.number>=1 else False


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.added = 0
        self.borrowed = 0
        self.borrowed_books = []

    def details(self):
        return f"""
            Name: {self.name}
            ID: {self.id}
            Books added: {self.added}
            Books borrowed: {self.borrowed}
            Borrowed books: {[i.title for i in self.borrowed_books]}
        """

    def add(self,num):
        self.added += num

        return "Done"

    def borrow(self,book):
        if book.is_available():
            book.lend()
            
            self.borrowed += 1
            self.borrowed_books.append(book)

            return "Done!"
        
        return "The book is currently not available!"
        

    def return_books(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed -= 1
            self.borrowed_books.remove(book)

            return "Done!"

        return "You haven't borrowed this book!"


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.numUsers = 0
        self.numBooks = 0
        self.userid = 0

    def new_user(self,name):
        self.users.append(User(name,self.userid))
        self.userid += 1

        self.numUsers += 1

        return f"New user registered successfully!\nYour ID is: {self.userid-1}"


    def new_book(self,title, author, isbn, number, user):

        thebook = list(filter(lambda x:x.title==title,self.books))

        if thebook != []:
            thebook[0].number += 1
        else:
            self.books.append(Book(title,author,isbn,number))

        self.numBooks += 1

        print(user.name)

        return user.add(number)
        # return user.details()
       


zlib = Library()


class Transaction:
    def __init__(self,user):
        self.total_transactions = 0
        self.total_borrowed = 0
        self.total_returned = 0
        self.user = user


    def add_book(self, title, author, isbn, number=1):
        self.total_transactions += 1
        return zlib.new_book(title, author, isbn, number, self.user)


    def borrow_book(self, title):
        self.total_transactions += 1
        self.total_borrowed += 1
        return self.user.borrow(list(filter(lambda x:x.title == title,zlib.books))[0])


    def return_book(self, title):
        self.total_transactions += 1
        self.total_returned += 1
        return self.user.return_books(list(filter(lambda x:x.title == title,zlib.books))[0])


    def report(self):
        return f"""
            Total transactions: {self.total_transactions}
            Total borrowed: {self.total_borrowed}
            Total returned: {self.total_returned}
            Total users: {zlib.numUsers}
            Total books: {zlib.numBooks}
        """


def initialize():
    global transact, zlib

    print("Welcome to Leb Leb Library")

    while True:
        print("1-Create an account","2-Login to an account","3-Add a book","4-Borrow a book","5-Return a book","6-View book details","7-Get transactions report","other-Quit",end='\n')
        choice1 = int(input(":"))

        if choice1 == 1:
            name = input("Enter your name: ")
            print(zlib.new_user(name))


        elif choice1 == 2:
            id = int(input("Enter your Id to login: "))

            if id<zlib.numUsers:
                transact = Transaction(list(filter(lambda x: x.id == id,zlib.users))[0])
                print("Logged in successfully!")
                print(transact.user)
            else:
                print("Invalid Id!")

        elif choice1 == 3:
            if transact:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                isbn = input("Enter the isbn of the book: ")
                number = int(input("How many of this book do you want to add: "))
                
                print(transact.add_book(title,author,isbn,number))

            else:
                print("Please login to an account first!")

        elif choice1 == 4:
            if transact:
                title = input("Enter the title of the book: ")
                
                print(transact.borrow_book(title))

            else:
                print("Please login to an account first!")

        elif choice1 == 5:
            if transact:
                title = input("Enter the title of the book: ")
                
                print(transact.return_book(title))

            else:
                print("Please login to an account first!")

        elif choice1 == 6:
            if transact:
                title = input("Enter the title of the book: ")
                
                print(list(filter(lambda x:x.title == title,zlib.books))[0].details())

            else:
                print("Please login to an account first!")

        elif choice1 == 7:
            if transact:
                print(transact.report())
            else:
                print("Please login to an account first!")
        else:
            break



initialize()
print('Thank you for using Leb Leb')