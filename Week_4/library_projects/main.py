from my_data import data
from my_utils import helpers
from services import library

def show_books():
    books = data.get_books()
    if not books:
        print("No books in the library yet.")
        return
    for i, b in enumerate(books, start=1):
        print(helpers.format_book(b, i))

def main():
    data.load_books()  # Load books when app starts
    
    while True:
        print("\n__Library Menu__")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            data.add_book(title, author)
            print(f"'{title}' by {author} added to library.")

        elif choice == "2":
            print("\nLibrary Collection:")
            show_books()

        elif choice == "3":
            title = input("Enter book title to borrow: ")
            print(library.borrow_book(title))

        elif choice == "4":
            title = input("Enter book title to return: ")
            print(library.return_book(title))

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()


#__Library Menu__
# 1. Add Book
# 2. List Books
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter your choice (1-5): 3
# Enter book title to borrow: physics
# Book not available.

# __Library Menu__
# 1. Add Book
# 2. List Books
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter your choice (1-5): 5
# Exiting... Goodbye!