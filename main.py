from library import Member, Librarian, Book

print('welcome')

librarian = Librarian()

while(True):
    inp = input('1 - add a book \n2 - add a member\n3 - add stock to a book\n4 - search for a book\n5 - check for given books\n6 - check bill for a single member\n7 - give book to a member\n')

    if inp == '1':
        book_name = input('enter the book name :')
        genre = input('enter the genre: ')
        author = input('enter the author: ')
        initial_stock = int(input('enter the initial stock as a number : '))
        librarian.add_book(book_name, author, genre, initial_stock)
    elif inp == '2':
        member_name = input('enter the member name : ')
        librarian.add_member(member_name)

    elif inp == '3':
        added_stock = int(input('enter the added stock as a number : '))
        book_name = input(' enter the books name')
        librarian.change_book_stock(book_name, added_stock)

    elif inp == '4':
        search_inp = input('by what do you want to search?\n1 - search by name\n2- search by author\n3 - search by genre\n')
        if search_inp == '1':
            name_input = input('enter the name : ')
            book = librarian.find_book_by_name(name_input)
            if book == None:
                print('no match found')
            else :
                book : Book
                print(f"{book.get_name()} stock : {book.get_stock()}")

        elif search_inp == '2':
            author_name = input("enter the authors name : ")
            this_author_books = librarian.find_books_by_author(author_name)
            if this_author_books == []:
                print('no match found') 
            else:
                for book_name in this_author_books:
                    print(book_name)
        elif search_inp == '3':
            genre_name = input('enter the genre: ')
            this_genre_books = librarian.find_books_by_genre(genre_name)
            if this_genre_books == []:
                print('no match found')
            else:
                 for book_name in this_genre_books:
                    print(book_name)
        elif search_inp == '4':
            librarian.print_all()
        else :
            print('wrong input')
    elif inp == '5':
        librarian.check_given_books()
    elif inp == '6':
        member_name = input('give the member name: ')
        member = librarian.find_member_by_name(member_name)
        member : Member
        bill = member.bill()
        print(f"{member_name}  {bill}")
    elif inp == '7':
        member_name = input('enter the members name : ')
        book_name = input('enter the books name : ')
        days = int(input('enter the days : '))
        librarian.give_book_to_member(member_name, book_name, days)

    else :
        print('wrong input')