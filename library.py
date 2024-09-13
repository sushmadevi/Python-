from book import Book
library = []
def add_book(title, author, year):
    new_book = Book(title, author, year)
    library.append(new_book)
    print(f'Book "{title}" by {author} printed in the {year} added to the list.') 

def book_list():
    return []