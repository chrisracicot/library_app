import csv

class Book:

        def __init__(self, isbn, title, author, genre, available):
                self.isbn = isbn
                self.title = title
                self.author = author
                self.genre = genre
                self.available = available

        
        GENRES = {
        0: "Romance",                   
        1: "Mystery",                 
        2: "Science Fiction",                  
        3: "Thriller",                  
        4: "Young Adult",                  
        5: "Children’s Fiction",                  
        6: "Self-help",                  
        7: "Fantasy",                  
        8: "Historical Fiction",                  
        9: "Poetry"                  
        }

        
        @staticmethod
        def load_books(book_list, catalogue):
                if catalogue != 'books.csv':
                        print(f"{catalogue} catalogue not found")
                        exit()

                print("Book catalogue has been loaded.")
                with open(catalogue, newline='') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                                if row:  # check if row is not empty
                                        isbn, title, author, genre, available = row
                                        book = Book(isbn, title, author, int(genre), available)  # Convert genre to int
                                        book_list.append(book)             
                return len(book_list)
        

        #Prints Main Menu for user
        def print_menu(menu_heading, menu_choices_dict):
                print("Reader's Guild Library - Main Menu")       
                print("==================================")
                for key, value in menu_choices_dict.items():
                        print(f"{key}: {value}")
                return input("Enter your selection: ")


        @staticmethod
        def books_headers(book_list):  
                
                # add book_list as an argument
                headings = ["ISBN", "Title", "Author", "Genre", "Available"]
                
                # Determine the maximum width for each column
                widths = []
                for i, attr in enumerate(headings):
                        attr_lower = attr.lower()  # Convert the heading back to lowercase for the getattr function
                        if attr_lower == "genre":
                                max_len = max(len(Book.GENRES[int(getattr(book, attr_lower))]) for book in book_list)
                        else:
                                max_len = max(len(str(getattr(book, attr_lower))) for book in book_list)
                        widths.append(max(max_len, len(headings[i])))
                
                # Create a format string that left-aligns each item
                format_string = " ".join("{:<" + str(width) + "}" for width in widths)
                
                # Use the format string to create the heading string
                heading_string = format_string.format(*headings)
                
                return heading_string



        
        def catalogue_dict():
                menu_dict = {
                        '1': 'Search for books',
                        '2': 'Borrow a book',
                        '3': 'Return a book',
                        '0': 'Exit the system'
                }
                return menu_dict




def main():
        book_list = []
        print("Starting the system...")

# ####################################IMPORTANT################################################################
#         Temporary work around for automatic csv entry: mark sure to 
#         replace "catalogue = books.csv" with "catalogue = str(input("Enter book file catalogue name: "))" 
#                               ### before submission ###
###############################################################################################################
        catalogue = 'books.csv'
###################################
        
        #Run load_books function and return length of list
        book_list_len = Book.load_books(book_list, catalogue)
        book_list_len = int(book_list_len)

        #creating main menu dictionary and search results display headings
        menu_heading = Book.books_headers(book_list)
        choices_dict = Book.catalogue_dict()


        menu_choice = ""
        while menu_choice != "0":
                menu_choice = Book.print_menu(menu_heading, choices_dict)
        if menu_choice == "1":
                Book.search_books()
        elif menu_choice == "2":
                Book.borrow_book()
        elif menu_choice == "3":
                Book.return_book()
        else:
                Book.validity_check()
        
        #Save books and exit the program
        Book.save_books(book_list, catalogue)
        print("-- Exit the system --")
        print("Book catalog has been saved.")
        print("Good Bye!")

if __name__ == "__main__":
        main()


# Functions that need to be created:

# Book.search_books()

# Book.borrow_book()

# Book.return_book()

# Book.validity_check()

# Book.find_book_by_isbn()

# Book.add_book()

# Book.remove_book()

# Book.print_books()

# Book.save_books()



#lily

#import os and Book class
import os
from book import Book
        
#def find_book_by_isbn
def find_book_by_isbn(book_list,isbn):
    for i in range(len(book_list)):
        if book_list[i].get_isbn() == isbn:
            return i
    return -1

#def search_books
def search_books(book_list,search_str):
    search_list = []
    search_str_lower = search_str.lower()
    for book in book_list:
        if ((search_str_lower in book.get_isbn().lower()) or
            (search_str_lower in book.get_title().lower()) or
            (search_str_lower in book.get_author().lower()) or
            (search_str_lower in book.get_genre_name().lower())):
            search_list.append(book)
    return search_list

#def print_books
def print_books(books):
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format('-' * 14, '-' * 25, '-' * 25, '-' * 20, '-' * 12))
    for book in books:
        print(book)

#def save_books
def save_books(book_list,path_name):
    with open (path_name, 'w') as file:
        count = 0
        for book in book_list:
            book_info = f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_available()}"
            file.write(book_info + '\n')
            count += 1
    return count          #•	Returns the number of books saved to the file

#def load_books
def load_books(book_list,path_name):
    with open(path_name, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            isbn, title, author, genre_name, available = data
            book = Book(isbn, title, author, genre_name, available)
            book_list.append(book)

#def print_menu
#staticmethod decorator define a static method without needing access to class instance attributes or methods  
@staticmethod
def print_menu(heading,options):
    print(heading)
    for key, value in options.items():
        print(f"{key}. {value}")

    user_choice = input("Enter your selection: ")
    while user_choice not in options and user_choice != "2130":
        user_choice = input("Invalid option\n" + "Enter your selection: ")
    return user_choice

#def borrow_book   
def borrow_book(book_list):
    print("-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list,isbn)
    if index != -1:
        book = book_list[index]
        if book.get_available():
            book.borrow_it()
            print(f'{book.get_title()} with ISBN {book.get_isbn()} is successfully borrowed.')
        else:
            print(f'{book.get_title()} with ISBN {book.get_isbn()} is not currently available.')
    else:
        print(f'No book found with that ISBN.')

#def return_book   
def return_book(book_list):
    print("-- Return a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index != -1:
        book = book_list[index]
        if not book.get_available():
            book.return_it()
            print(f'{book.get_title()} with ISBN {book.get_isbn()} is successfully returned.')
        else:
            print(f'{book.get_title()} with ISBN {book.get_isbn()} is not currently borrowed.')
    else:
        print(f'No book found with that ISBN.')

#def add_book
def add_book(book_list):
    print("-- Add a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    genre_input = input("Enter genre: ")
    while genre_input not in Book.GENRE_TABLE.values():
        print("Invalid genre. Choices are: "+", ".join(Book.GENRE_TABLE.values()))
        genre_input = input("Enter genre: ")
    for key, value in Book.GENRE_TABLE.items():
        if value == genre_input:
            genre = key
    new_book = Book(isbn, title, author, genre, available=True)
    new_book.set_available(True)
    book_list.append(new_book)
    print(f'{title} with ISBN {isbn} is successfully added.')

#def remove_book
def remove_book(book_list):
    print("-- Remove a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    title = book_list[index].get_title()
    if index != -1:
        del book_list[index]
        print(f'{title} with ISBN {isbn} is successfully removed.')

#def main
def main():
    books = []
    print("Starting the system ...")
    file_path = input("Enter book catalog filename: ")
    while not os.path.exists(file_path):
        file_path = input("File not found. Re-enter book catalog filename: ")
    load_books(books, file_path)   
    print("Book catalog has been loaded.")
    menu_heading = "Reader's Guild Library - Main Menu\n" + "=" * 34
    menu_options = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "0": "Exit the system"
    }
    #loop until user quit
    while True:
        choice = print_menu(menu_heading, menu_options)
        if choice == "1":
            print("-- Search for books --")
            search_value = input("Enter search value: ")
            search_result = search_books(books, search_value)
            if not search_result:
                print("No matching books found.")
            else:
                print_books(search_result)
            
        elif choice == "2":
            borrow_book(books)
            
        elif choice == "3":
            return_book(books)
            
        elif choice == "0":
            save_books(books, file_path) 
            print("-- Exit the system --")
            print("Book catalog has been saved.")
            print("Good Bye!")
            break

#if input passcode=2130, open a special menu
        elif choice == "2130":
            special_heading = "Reader's Guild Library - Librarian Menu\n" + "=" * 39
            special_menu = {
                "1": "Search for books",
                "2": "Borrow a book",
                "3": "Return a book",
                "4": "Add a book",
                "5": "Remove a book",
                "6": "Print catalog",
                "0": "Exit the system"
            }
            add_choice = print_menu(special_heading, special_menu)
            if add_choice == "1":
                print("-- Search for books --")
                search_value = input("Enter search value: ")
                search_result = search_books(search_value)
                if not search_result:
                    print("No matching books found.")
                else:
                    print_books(search_result)
                
            elif add_choice == "2":
                borrow_book(books)
            
            elif add_choice == "3":
                return_book(books)
            
            elif add_choice == "4":
                add_book(books)

            elif add_choice == "5":
                remove_book(books)

            elif add_choice == "6":
                print("-- Print book catalog --")
                print_books(books)
            
            elif add_choice == "0":
                save_books(books) 
                print("-- Exit the system --")
                print("Book catalog has been saved.")
                print("Good Bye!")
                break

        else:
            print("Invalid choice. Please enter a valid option.")
    
if __name__ == "__main__":
    main()
