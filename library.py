class Librarian:
    def __init__(self) :
        self.__members_list= [] # list of objects of members
        self.__books_list = [] # list of objects of books
    def change_book_stock(self, book_name, number):
        book = self.find_book_by_name(book_name)
        book : Book
        book.change_book_stock(number)
    def add_book(self,book_name,author, genre, initial_stock):
        new_book = Book(book_name,author, genre, initial_stock)
        self.__books_list.append(new_book)        
    def add_member(self, member_name) :
        new_member = Member(member_name)
        self.__members_list.append(new_member)

    def give_book_to_member(self, member_name, book_name, days):
        member = self.find_member_by_name(member_name)
        member : Member
        member.give_book(book_name, days)
        self.change_book_stock(book_name, -1)

    def find_book_by_name(self, book_name):
        for book in self.__books_list :
            book : Book
            if book_name == book.get_name():
                return book
        return None
    
    def find_member_by_name(self, member_name):
        for member in self.__members_list:
            member : Member
            if member_name == member.get_name():
                return member
        return None
    def find_books_by_author(self, author_name):
        this_author_books = []
        for book in self.__books_list:
            book : Book
            if book.get_author() == author_name:
                this_author_books.append(book.get_name())
        return this_author_books
    def find_books_by_genre(self, genre):
        this_genre_books = []
        for book in self.__books_list:
            book : Book
            if book.get_genre() == genre:
                this_genre_books.append(book.get_name())
        return this_genre_books
    def check_given_books(self):
        for member in self.__members_list:
            member : Member
            if member.get_books():
                for book in member.get_books():
                    print(f"{member.get_name()}-{book[0]}-{book[1]}")
    def print_all(self):
        for book in self.__books_list:
            book : Book
            print(book.get_name(), book.get_author(), book.get_author())
        

class Book : 
    def __init__(self, book_name, author,genre ,initial_stock) : 
        self.__book_name = book_name 
        self.__author = author  
        self.__genre = genre 
        self.__stock_book = initial_stock 
         
    def change_book_stock(self, number): 
        self.__stock_book += number
    def get_name(self):
        return self.__book_name
    def get_stock(self):
        return self.__stock_book
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
class Member:
    def __init__(self, name) :
        self.__name = name
        self.__given_books_list = [] # must be a 2d list having remaining days and str of name of a book
    def give_book(self, book_name , days) :
        self.__given_books_list.append([book_name, days])
    def bill(self): # give bill for all members books
        bill = 0
        for book in self.__given_books_list:
            if book[1] < 0 :
                bill -= (book[1] * 1000)
        return bill
    def get_name(self):
        return self.__name
    
    def get_books(self):
        return self.__given_books_list
