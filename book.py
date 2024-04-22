class Book:
    GENRE_TABLE = {
        "0": "Romance",
        "1": "Mystery",
        "2": "Science Fiction",
        "3": "Thriller",
        "4": "Young Adult",
        "5": "Children's Fiction",
        "6": "elf-help",
        "7": "Fantasy",
        "8": "Historical Fiction",
        "9": "Poetry"
    }

    def __init__(self,isbn,title,author,genre,available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = bool(available)

    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    def get_available(self):
        return self.__available
    
    def get_genre_name(self):
        return self.GENRE_TABLE.get(str(self.__genre))
    
    def get_availability(self):
        if self.__available:
            return "Available"
        else:
            return "Borrowed"

    def set_isbn(self,isbn):
        self.__isbn = isbn
    def set_title(self,title):
        self.__title = title
    def set_author(self,author):
        self.__author = author
    def set_genre(self,genre):
        self.__genre = genre
    def set_available(self,available):
        self.__available = available

    def borrow_it(self):
        self.__available = False
    def return_it(self):
        self.__available = True

    def __str__(self):
        return f'{self.__isbn:<14} {self.__title:<25} {self.__author:<25} {self.get_genre_name():<20} {self.get_availability()}'