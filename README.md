# library-proj

class Librarian: parsa and fateme
    def __init__(self) :
        self.__members_list= [] # list of objects of members
        self.__books_list = [] # list of objects of books
    def change_book_stock(self, book_name, number):
    def add_book(self,book_name,author, genre, initial_stock):   
    def add_member(self, member_name) :

    def give_book_to_member(self, member_name, book_name, days):

    def find_book_by_name(self, book_name):
    
    def find_member_by_name(self, member_name):
    def find_books_by_author(self, author_name):
    def find_books_by_genre(self, genre):
    def check_given_books(self):
    def print_all(self):

class Book : sara
    def __init__(self, book_name, author,genre ,initial_stock) : 
        self.__book_name = book_name 
        self.__author = author  
        self.__genre = genre 
        self.__stock_book = initial_stock 
         
    def change_book_stock(self, number): 
    def get_name(self):
    def get_stock(self):
    def get_author(self):
    def get_genre(self):
class Member: aria
    def __init__(self, name) :
        self.__name = name
        self.__given_books_list = [] # must be a 2d list having remaining days and str of name of a book
    def give_book(self, book_name , days) :
    def bill(self): # give bill for all members books
        
    def get_name(self):    
    def get_books(self):
estimation 3 hours