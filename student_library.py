class Library:
    def __init__(self,ListOfBooks):
        self.books=ListOfBooks
            
    def displayAvailabeBooks(self):
        for (index,book) in enumerate (self.books):
            print(index,book)
    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"Your {bookName} book is issued.Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
        else:
            print("Sorry,This book is already been issued to someone else or not present in the Central Library.Please wait until the book is returned.")  
    def return_donate_Books(self,bookName):
        if bookName.isspace():
            print(f"Please mention the name of the book you want to return or donate.")
        else:
            self.books.append(bookName)
            print(f"Thanks you for returning/donating this book.")
            
    
class Student:
    def requestBook(self):
        self.book=input("Enter the book you want to borrow ")
        return self.book
        
    def return_donate_Book(self):
        self.book=input("Enter the book you want to return/donate ")
        return self.book

    
if __name__=="__main__":
    centralLibrary=Library(["Algorithm","Django","Clrs","Python Notes"])
    student=Student()
    while(True):
        print('''=====Welcome to Central Library=====
        Please choose an option:
        1.List all the books.
        2.Request a book.
        3.Return/Donate a book.
        4.Exit the library.
        ''')
        a=int(input("Enter your choice ")) 
        if a==1:
            centralLibrary.displayAvailabeBooks()
        elif a==2:
            centralLibrary.borrowBooks(student.requestBook())
        elif a==3:
            centralLibrary.return_donate_Books(student.return_donate_Book())
        elif a==4:
            print("Thanks for chooosing Central Library!Have a great day ahead!")
            exit()
        else:
            print("INVALID CHOICE")   
