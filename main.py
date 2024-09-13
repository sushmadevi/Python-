from library import book_list, add_book
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. List all books")
        print("2. Add a new book")
        print("3. Exit")
        option = input("Enter your option: ")
        if option == "1":
            books = book_list()
            if books:
                print("Books in the library:")
                for book in books:
                    print(book)
            else:
                print("No books in the library.")
        elif option == "2":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            year = input("Enter the year published: ")
            try:
                year = int(year)
                add_book(title, author, year)
                print("Book added successfully.")
    except ValueError:
            print("Year must be an integer.")
        elif option == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")
    main_menu()
print(main_menu())