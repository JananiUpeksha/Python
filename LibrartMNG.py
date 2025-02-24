"""
Library mng system
use are tasked with creating a basic lib mng system using inheritance implemet following classes
01.Base class - lib items
Attributes - title,author,publication_year
Methods - display_info - print the details of the item

02.Dirived class- Book - inherit from lib item
Additional attributes - genre,isbn
Override methos - display_info - print the details including the genre,isbn

03.Dirived class - Magazine - inherit from lib item
Additional attributes - issue
Override methos - display_info - print the details including the issue

Task - create instances of each clas(Book,Magazine) with appropiate values for there attributes
     - call the display info method for each instance to test inheritance and method overriding
"""
class LibraryItems:
    def __init__(self, title, author, publish_year):
        self.title = title
        self.author = author
        self.publish_year = publish_year

    def display_info(self):
        pass

class Book(LibraryItems):
    def __init__(self, title, author, publish_year, genre, isbn):
        super().__init__(title, author, publish_year)  # Corrected constructor call
        self.genre = genre
        self.isbn = isbn

    def display_info(self):
        print(self.title, self.author, self.publish_year, self.genre, self.isbn)

class Magazine(Book):
    def __init__(self, title, author, publish_year, genre, isbn, issue):
        super().__init__(title, author, publish_year, genre, isbn)  # Corrected constructor call
        self.issue = issue

    def display_info(self):
        print(self.title, self.author, self.publish_year, self.genre, self.isbn, self.issue)

# Example usage:
book = Book("Madol DUwa", "M.Wikramasinghe", 2012, "Youth", 234000)
book.display_info()

magazine = Magazine("Madol DUwa", "M.Wikramasinghe", 2012, "Youth", 234000, 2013)
magazine.display_info()

