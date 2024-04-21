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
                with open(catalogue, newline='') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                                if row:  # check if row is not empty
                                        isbn, title, author, genre, available = row
                                        book = Book(isbn, title, author, genre, available)
                                        book_list.append(book)
                return len(book_list)


def main():

        book_list = []




if __name__ == "__main__":
        main()
