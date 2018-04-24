#Leandro Lopez
#lslopez, rboppana
#Section H
#################################################
# Lab9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################
# Recursively finds log3 of a number 
def logBase3(n):
    if n < 3:
        return 0 #Base case 
    else:
        return 1 + logBase3(n//3) #integer division to keep it in integers

# Finds alternating sum of a list of digits 
def alternatingSum(L):
    if not L:
        return 0 #Base case 
    elif len(L) % 2 == 1: #Add when length is odd 
        return L[-1] + alternatingSum(L[:-1])
    # Substract when length is even 
    else: return -1*L[-1] + alternatingSum(L[:-1])

# Returns list of powers of 3 
def powersOf3ToN(n):
    L = [3**logBase3(n)] #find exponent of log3(n)
    if n < 1: 
        return None #Return None if n is less than 
    else:
        if n >= 3:
            L.extend(powersOf3ToN(n//3)) #Extend list every iteration
        return sorted(L) #Sort the list in ascending order 

# Wrapper function for binarySearchValues
def binarySearchValues(L, v):
    return binarySearchValuesHelper(L, v, 0, len(L)-1)

def binarySearchValuesHelper(L, v, lo, hi):
    mid = (lo + hi)//2 #Find medium 
    if hi == lo: 
        return [(mid, L[mid])] # If char not found return tuple 
    elif L[mid] == v:
        return [(mid, L[mid])] # If char found return tuple and found char
    elif hi < 0: 
        return [] # If medium drops below 0, return empty list 
    elif L[mid] < v: 
        # If value less than v, return tuple and change lo
        return [(mid, L[mid])] + binarySearchValuesHelper(L, v, mid+1, hi)
    elif L[mid] > v: 
        # If value greater than v, return tuple and change hi 
        return [(mid, L[mid])] + binarySearchValuesHelper(L, v, lo, mid-1) 
  
# OOP questions
##############################################

class Book(object):
    # Initialize variables 
    def __init__(self, name, author, numberOfPages):
        self.name = name 
        self.author = author 
        self.numberOfPages = numberOfPages
        self.currentPage = 1
        self.bookMark = 0 
    
    # Format the output 
    def __str__(self):
        if self.bookMark == 0 and self.numberOfPages == 1:
            return "Book<%s by %s: %d page, currently on page %d>" %(self.name,
                self.author, self.numberOfPages, self.currentPage)

        elif self.bookMark == 0 and self.numberOfPages > 1: 
            return "Book<%s by %s: %d pages, currently on page %d>" %(self.name,
                self.author, self.numberOfPages, self.currentPage)
        elif self.bookMark != 0 and self.numberOfPages == 1:
            text = "Book<%s by %s: %d page, currently on page %d, page %d "
            text2 = "bookmarked>"
            total = text+text2
            return total % (self.name, self.author, self.numberOfPages,
                                 self.currentPage, self.bookMark)
        else: 
            text = "Book<%s by %s: %d pages, currently on page %d, page %d "
            text2 = "bookmarked>"
            total = text+text2
            return total % (self.name, self.author, self.numberOfPages,
                                 self.currentPage, self.bookMark)
    # Turn page 
    def turnPage(self, delta):
        if (delta + self.currentPage > 0 and #Check delta is within bounds 
            delta + self.currentPage <= self.numberOfPages):
            self.currentPage += delta
        elif delta + self.currentPage > self.numberOfPages:
            self.currentPage = self.numberOfPages
   
    def getCurrentPage(self):
        return self.currentPage
    
    def getBookmarkedPage(self):
        if self.bookMark == 0: #If no bookmarks return None 
            return None 
        else: return self.bookMark

    # Place bookmark
    def placeBookmark(self):
        self.bookMark = self.currentPage
    
    # Remove bookmark    
    def removeBookmark(self):
        self.bookMark = 0
    
    # If bookmark exists, turn to that page 
    def turnToBookmark(self):
        if self.bookMark != 0:
            self.currentPage = self.bookMark 
    
#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Done!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(-42) == None)
    assert(powersOf3ToN(0.99) == None)
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(3) == [1, 3])
    assert(powersOf3ToN(8.9999) == [1, 3])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(9.1111) == [1, 3, 9])
    assert(powersOf3ToN(100) == [1, 3, 9, 27, 81])
    print('Done!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    L = ['a', 'c', 'f', 'g', 'm', 'q']
    assert(binarySearchValues(L, 'a') == [(2,'f'), (0,'a')])
    assert(binarySearchValues(L, 'c') == [(2,'f'), (0,'a'), (1,'c')])
    assert(binarySearchValues(L, 'f') == [(2,'f')])
    assert(binarySearchValues(L, 'g') == [(2,'f'), (4, 'm'), (3, 'g')])
    assert(binarySearchValues(L, 'm') == [(2,'f'), (4, 'm')])
    assert(binarySearchValues(L, 'q') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'z') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'b') == [(2,'f'), (0,'a'), (1,'c')])
    print('Done!')

def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone", 
                 "J. K. Rowling", 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert(str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
                         "1 page, currently on page 1>")
                         
    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4) # turning pages does not return
    assert(book1.getCurrentPage() == 5)
    book1.turnPage(-1)
    assert(book1.getCurrentPage() == 4)
    book1.turnPage(400)
    assert(book1.getCurrentPage() == 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert(book2.getCurrentPage() == 1)
    book2.turnPage(1)
    assert(book2.getCurrentPage() == 1)
    
    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 1>")
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(9)
    book3.placeBookmark() # does not return
    assert(book3.getBookmarkedPage() == 10)
    book3.turnPage(7)
    assert(book3.getBookmarkedPage() == 10)
    assert(book3.getCurrentPage() == 17)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert(book3.getCurrentPage() == 10)
    book3.removeBookmark()
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(25)
    assert(book3.getCurrentPage() == 35)
    book3.turnToBookmark() # if there's no bookmark, don't turn to a page
    assert(book3.getCurrentPage() == 35)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 35>")
    
    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert(book5 == book6)
    assert(book5 != book7)
    assert(book5 != book8)
    book5.turnPage(1)
    assert(book5 != book6)
    book5.turnPage(-1)
    assert(book5 == book6)
    book6.placeBookmark()
    assert(book5 != book6)
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testAlternatingSum()
    testPowersOf3ToN()
    testBinarySearchValues()
    testBookClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
