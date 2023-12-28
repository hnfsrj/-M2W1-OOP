logged = False

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
    def __init__(self, name,password, id):
        self.name = name
        self.password = password
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

    def new_user(self,name,password):
        self.users.append(User(name,password,self.userid))
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


        return user.add(number)
       


zlib = Library()


class Transaction:
    def __init__(self,user):
        self.total_transactions = 0
        self.total_borrowed = 0
        self.total_returned = 0
        self.user = user


    def add_book(self, title, author, isbn, number=1):
        if number>=1:
            self.total_transactions += 1
            return zlib.new_book(title, author, isbn, number, self.user)

        return "Invalid number of books"

    def borrow_book(self, title):
        ztitle = list(filter(lambda x:x.title == title,zlib.books))
        
        if ztitle != []:
            borrowing = self.user.borrow(ztitle[0])
            
            if borrowing == "Done!":
                self.total_transactions += 1
                self.total_borrowed += 1

            return borrowing

        return "Unfortunately we dont have that book!"




    def return_book(self, title):
        ztitle = list(filter(lambda x:x.title == title,zlib.books))

        if ztitle != []:
            returning = self.user.return_books(ztitle[0])
            
            if returning == "Done!":
                self.total_transactions += 1
                self.total_returned += 1

            return returning

        return "Unfortunately we dont recognize that book!"
        

    def report(self):
        return f"""
            Total transactions: {self.total_transactions}
            Total borrowed: {self.total_borrowed}
            Total returned: {self.total_returned}
            Total users: {zlib.numUsers}
            Total books: {zlib.numBooks}
        """

def printer(txt):
    print('\n',txt,'\n')

def initialize():
    global transact, zlib, logged

    printer("Welcome to Leb Leb Library")

    while True:
        [print(i,end='\n') for i in ["\n1-Create an account","2-Login/change to an account","3-Add a book","4-Borrow a book","5-Return a book","6-View book details","7-Data about user","8-List of available books","9-Get transactions report","10-Logout","other-Quit"]]
        
        try:
            choice1 = int(input(":"))
        except:
            break

        if choice1 == 1:
            name = input("Enter your name: ")
            password = input("Create a password: ")

            printer(zlib.new_user(name, password))


        elif choice1 == 2:
            id = int(input("Enter your Id: "))
            password = input("Enter your password: ")

            if id<zlib.numUsers and id>=0:
                theuser = list(filter(lambda x: x.id == id,zlib.users))[0]

                if theuser.password == password:
                    transact = Transaction(theuser)
                    logged = True
                    printer("Logged in successfully!")
                else:
                    printer("Wrong Id or password")
            else:
                printer("Invalid Id!")

        elif choice1 == 3:
            if logged:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                isbn = input("Enter the isbn of the book: ")
                number = int(input("How many of this book do you want to add: "))
                
                printer(transact.add_book(title,author,isbn,number))

            else:
                printer("Please login to an account first!")

        elif choice1 == 4:
            if logged:
                title = input("Enter the title of the book: ")
                
                printer(transact.borrow_book(title))

            else:
                printer("Please login to an account first!")

        elif choice1 == 5:
            if logged:
                title = input("Enter the title of the book: ")
                
                printer(transact.return_book(title))

            else:
                printer("Please login to an account first!")

        elif choice1 == 6:
            if logged:
                title = input("Enter the title of the book: ")

                ztitle = list(filter(lambda x:x.title == title,zlib.books))

                if ztitle != []:
                    printer(ztitle[0].details())
                else:
                    printer("Unfortunately we dont recognize that book!")


            else:
                printer("Please login to an account first!")

        elif choice1 == 7:
            if logged:
                printer(transact.user.details())


            else:
                printer("Please login to an account first!")

        elif choice1 == 8:
                if zlib.books == []:
                    printer("There are no books in the library!")
                else:
                    
                    max = zlib.numBooks-1
                    min = 0
                    page = 0
                    zend = False


                    if max>=1:
                        printer("n-Next  |  p-Previous  |  other-Exit")
                        go = True
                    else:
                        go = False

                    printer(zlib.books[page].details())
                    
                    while go:

                        choice2 = input(f"Page {page+1} of {max+1} (n/p): ")

                        if choice2 == "n":
                            if page < max:
                                if not zend:
                                    page += 1

                                zend=False

                                printer(zlib.books[page].details())
                            else:
                                printer("You've already reached the end!")
                                zend = True
                        elif choice2 == "p":
                            if page > min:
                                if not zend:
                                    page -= 1

                                zend=False
                                
                                printer(zlib.books[page].details())
                            else:
                                printer("You've already reached the end!")
                                zend = True
                        else:
                            break


        elif choice1 == 9:
            if logged:
                printer(transact.report())
            else:
                printer("Please login to an account first!")
        elif choice1 == 10:
            if logged:
                transact = ''
                logged = False
                printer("Logged out of account successfully!")
            else:
                printer("Please login to an account first!")
        else:
            break



initialize()
printer('Thank you for using Leb Leb')