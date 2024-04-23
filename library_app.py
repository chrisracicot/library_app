#comments

#import os and Book class
import os
from book import Book
        
#def find_book_by_isbn
def find_book_by_isbn(book_list,isbn):
    for i in range(len(book_list)):
        if book_list[i].get_isbn() == isbn:
            return i
    return -1       #•	Returns the index of the matching book or -1 if none found

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
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title",
    "Author", "Genre", "Availability"))
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
            if available == "True":
                available = True
            elif available == "False":
                available = False
            book = Book(isbn, title, author, genre_name, available)
            book_list.append(book)

#def print_menu           
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
            print(f"'{book.get_title()}' with ISBN {book.get_isbn()} is successfully borrowed.")
        else:
            print(f"'{book.get_title()}' with ISBN {book.get_isbn()} is not currently available.")
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
            print(f"'{book.get_title()}' with ISBN {book.get_isbn()} is successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {book.get_isbn()} is not currently borrowed.")
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
    print(f"'{title}' with ISBN {isbn} is successfully added.")

#def remove_book
def remove_book(book_list):
    print("-- Remove a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    title = book_list[index].get_title()
    if index != -1:
        del book_list[index]
        print(f"'{title}' with ISBN {isbn} is successfully removed.")
    else:
        print(f'No book found with that ISBN.')

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

    #loop for user to enter options until user choose to quit
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
            #loop in the librarian system 
            while True:
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
                    save_books(books, file_path) 
                    print("-- Exit the system --")
                    print("Book catalog has been saved.")
                    print("Good Bye!")
                    break

        else:
            print("Invalid choice. Please enter a valid option.")
    
if __name__ == "__main__":
    main()
