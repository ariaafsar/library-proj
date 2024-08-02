class Librarian:
    def __init__(self) :
        members_list= [] # list of objects of members
        books_list = [] # list of objects of books
    def change_book_stock(self, book_name, number):
        pass
    def add_book(self,book_name,author, genre, initial_stock):
        new_book = Book(book_name,author, genre, initial_stock)
        self.books_list.append(new_book)        
    def add_member(self, member_name) :
        new_member = Member(member_name)
        self.members_list.append(new_member)

    def give_book_to_member(self, member_name):
        pass
    def find_book_by_name(self, book_name):
        for book in self.books_list :
            book : Book
            if book_name == book.book_name:
                return book
        return None
    
    def find_member_by_name(self, member_name):
        for member in self.members_list:
            member : Member
            if member_name == member.name:
                return member
        return None
    def find_books_by_author(self, author_name):
        pass
    def find_books_by_genre(self, genre):
        pass

class Book :
    def __init__(self, book_name, initial_stock) :
        pass
    def change_book_stock(self, number):
        pass

class Member:
    def __init__(self, name) :
        given_books_list = [] # must be a 2d list having remaining days and str of name of a book
    def give_book(book_name, days):
        pass
    def bill(self): # give bill for all members books
        pass
