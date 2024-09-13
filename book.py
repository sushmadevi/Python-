class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
        
    def book_list():
        return []
    def add_book(book_list, title, author, year):
        new_book = Book(title, author, year)
        book_list.append(new_book)
        print(f'Book "{title}" by {author} printed in the {year} added to the list.') 
    def update_book(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year