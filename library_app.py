import csv

class Book:

        def __init__(self, isbn, title, author, quantity, available):
                self.isbn = isbn
                self.title = title
                self.author = author
                self.quantity = quantity
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
                return book_list

        def print_menu(menu_heading, menu_choices_dict):
                print("Reader's Guild Library - Main Menu")       
                print("==================================")
                for key, value in menu_choices_dict.items():
                        print(f"{key}: {value}")
                return input("Enter your selection: ")

        @staticmethod
        def books_headers(book_list):  # add book_list as an argument
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

                #########print test###############
                print(heading_string)
                
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

# ####################################IMPORTANT###################################################
#         #Temporary work around for automatic csv entry: mark sure to replace "catalogue = books.csv" 
#         #with "catalogue = str(input("Enter book file catalogue name: "))" before submission ###
#         catalogue = 'books.csv'
#################################################################################################
        catalogue = 'books.csv'
        
        book_list = Book.load_books(book_list, catalogue)
        
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
                
        Book.save_books(book_list, catalogue)
        print("-- Exit the system --")
        print("Book catalog has been saved.")
        print("Good Bye!")


if __name__ == "__main__":
        main()
