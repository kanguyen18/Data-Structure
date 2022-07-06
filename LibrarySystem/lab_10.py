# In my library, I do not allow a book checked out by Patron A to be returned by Patron B since that will cause more difficulties in deciding whether the book checking in belonged to our library. Therefore, when you test the first case, my code will raise error and decline the transaction.

import os.path
import argparse
import sys

class Library:
    
    class _Book:
        __slot__ = 'ISBN', '_title', '_count', '_checkoutCount'
        
        def __init__(self, ISBN, title):
            self._ISBN = ISBN
            self._title = title
            self._count = 1
            self._checkoutCount = 0
            
        def getISBN(self):
            return self._ISBN
        
        def getTitle(self):
            return self._title
        
        def getCount(self):
            return self._count
        
        def getCheckout(self):
            return self._checkoutCount
        
        def checkoutAdd(self):
            self._checkoutCount += 1
        
        def decrementCount(self):
            if self._count == 0:
                print("No more copy to decrement", file=sys.stderr)
                return
            else:
                self._count -= 1
        
        def incrementCount(self):
            self._count += 1
            
    class _Patron:
        # I add an attribute named borrow, which is a list to keep track of the book that this patron is borrowing. So, when he returns a book, if the ISBN of the book is in the borrow list, the library will accept the transaction and remove the ISBN from the borrow list. If the ISBN of the book is NOT in the borrow list, the library will raise error notifying that the book was not borrowed from this library.
        __slot__ = '_ID', '_borrow', '_checkoutCount'
        
        def __init__(self, ID):
            self._ID = ID
            self._borrow = []
            self._checkoutCount = 0
            
        def getID(self):
            return self._ID
            
        def getBorrow(self):
            return self._borrow
        
        def getCheckout(self):
            return self._checkoutCount
        
        def checkoutAdd(self):
            self._checkoutCount += 1
        
        def addBorrow(self, ISBN):
            self._borrow.append(ISBN)
            
    def __init__(self):
        # The main data structure I used is Python dictionary
        self._book = {}
        self._patron = {}
        self._totalBook = 0
        self._checkout = 0
        self._checkin = 0
        self._popularBook = None
        self._popularPatron = None
        
    def getTotalBook(self):
        return self._totalBook
    
    def getCheckout(self):
        return self._checkout
    
    def getCheckin(self):
        return self._checkin
    
    def getPopularBook(self):
        return self._popularBook
    
    def getPopularPatron(self):
        return self._popularPatron
    
    def addBook(self, ISBN, title):
        # Check invalid ISBN. A valid ISBN needs to have 10 digits and the first 9 digits are numbers.
        if len(ISBN) != 10 or ISBN[:9].isdigit() == False:
            print("Invalid ISBN", file=sys.stderr)
        else:
            if self._book.get(ISBN):
                # Raise error if same ISBN but different titles
                if title == self._book.get(ISBN).getTitle():
                    self._book.get(ISBN).incrementCount()
                    self._totalBook += 1
                else:
                    print("Same ISBN but different titles", file=sys.stderr)
                    return
            else:
                self._book[ISBN] = self._Book(ISBN, title)
                self._totalBook += 1
            
    def addPatron(self, ID):
        if self._patron.get(ID):
            print("Cannot duplicate patron", file=sys.stderr)
            return
        else:
            self._patron[ID] = self._Patron(ID)
            
    def checkout(self, ID, ISBN):
        # check if patron ID is valid. If yes, get the patron. If no, raise error.
        if self._patron.get(ID):
            patron = self._patron.get(ID)
        else:
            print("This ID does not exist", file=sys.stderr)
            return
        
         # check if there are available book copy, If yes, get the book. If no, raise error.
        if self._book.get(ISBN):
            book = self._book.get(ISBN)
            if book.getCount() == 0:
                print("Run out of copies", file=sys.stderr)
                return
            else:
                book.decrementCount()
                book.checkoutAdd()
                patron.addBorrow(book.getISBN())
                patron.checkoutAdd()
                self._checkout += 1
        else:
            print("This book does not exist", file=sys.stderr)
            return
        
        # find the most checkout book
        if self._popularBook == None:
            self._popularBook = book
        elif book.getCheckout() > self._popularBook.getCheckout():
            self._popularBook = book
        
        # find the most checkout patron
        if self._popularPatron == None:
            self._popularPatron = patron
        elif patron.getCheckout() > self._popularPatron.getCheckout():
            self._popularPatron = patron
        
    def checkin(self, ID, ISBN):
        # check if patron ID is valid. If yes, get the patron. If no, raise error.
        if self._patron.get(ID):
            patron = self._patron.get(ID)
        else:
            print("This ID does not exist", file=sys.stderr)
            return
        
         # check if the returning book was taken from our library by checking the borrow list of the patron. If yes, add the book copy back. If no, raise error.
        if ISBN in patron.getBorrow():
            patron.getBorrow().remove(ISBN)
            self._book.get(ISBN).incrementCount()
            self._checkin += 1      
        else:
            print("The book is not from our library", file=sys.stderr)
            return
        
    def removeBook(self, ISBN):
        # I only remove a copy of the book that is kept in the Library. That means the copy which is being borrowed by the patron will not be removed.
        # check if the ISBN exists. If yes, remove 1 copy. If no, raise error.
        if self._book.get(ISBN):
            self._totalBook -= 1
            self._book.get(ISBN).decrementCount()
        else:
            print("This book does not exist", file=sys.stderr)
            return
        
    def removePatron(self, ID):
        # check if the ID exists. If yes, remove the patron. If no, raise error.
        if self._patron.get(ID):
            self._patron.pop(ID)
        else:
            print("This ID does not exist", file=sys.stderr)
            return
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 7')
    parser.add_argument('-i','--inputFileName', type=str, help='File of strings, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r')
    
    myLibrary = Library()
    for i in input_file:
        i = i.strip("\n")
        a = i.split(", ")
        if a[0] == "addPatron":
            myLibrary.addPatron(a[1])
        if a[0] == "addBook":
            myLibrary.addBook(a[1],a[2])
        if a[0] == "checkout":
            myLibrary.checkout(a[1],a[2])
        if a[0] == "checkin":
            myLibrary.checkin(a[1],a[2])
        if a[0] == "removeBook":
            myLibrary.removeBook(a[1])
        if a[0] == "removePatron":
            myLibrary.removePatron(a[1])
            
    print(myLibrary.getTotalBook())
    print(myLibrary.getCheckout())
    print(myLibrary.getCheckin())
    popularBook = myLibrary.getPopularBook()
    popularPatron = myLibrary.getPopularPatron()
    # Display most check-out book and patron if they are different from None
    if popularBook:
        print(popularBook.getISBN()+", "+popularBook.getTitle()+", "+str(popularBook.getCheckout()))
    if popularPatron:
        print(popularPatron.getID()+", "+str(popularPatron.getCheckout()))
    
    
    
            
            
            