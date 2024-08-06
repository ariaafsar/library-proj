class Librarian:
    def __init__(self) :
        self.members_list= [] # list of objects of members
        self.books_list = [] # list of objects of books
    def change_book_stock(self, book_name, number):
        book = self.find_book_by_name(book_name)
        book : Book
        book.change_book_stock(number)
    def add_book(self,book_name,author, genre, initial_stock):
        new_book = Book(book_name,author, genre, initial_stock)
        self.books_list.append(new_book)        
    def add_member(self, member_name) :
        new_member = Member(member_name)
        self.members_list.append(new_member)

    def give_book_to_member(self, member_name, book_name, days):
        member = self.find_member_by_name(member_name)
        member : Member
        member.give_book(book_name, days)
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
        this_author_books = []
        for book in self.books_list:
            book : Book
            if book.author == author_name:
                this_author_books.append(book.book_name)
        return this_author_books
    def find_books_by_genre(self, genre):
        this_genre_books = []
        for book in self.books_list:
            book : Book
            if book.genre == genre:
                this_genre_books.append(book.book_name)
        return this_genre_books
    def check_given_books(self):
        for member in self.members_list:
            member : Member
            if member.given_books_list:
                for book in member.given_books_list:
                    print(f"{member.name}-{book[0]}-{book[1]}")
        

class Book : 
    def __init__(self, book_name, author,genre ,initial_stock) : 
        self.book_name = book_name 
        self.author = author  
        self.genre = genre 
        self.stock_book = initial_stock 
         
    def change_book_stock(self, number): 
        self.stock_book += number
class Member:
    def __init__(self, name) :
        self.name = name
        self.given_books_list = [] # must be a 2d list having remaining days and str of name of a book
    def give_book(self, book_name , days) :
        self.given_books_list.append([book_name, days])
    def bill(self): # give bill for all members books
        bill = 0
        for book in self.given_books_list:
            if book[1] < 0 :
                bill -= (book[1] * 1000)
        return bill
