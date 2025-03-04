from book_data import save_books

def add_book(books):
    title = input("Enter book title: ").strip()
    if not title.isalpha():
        print("Error: The book title must be a string (letters only).")
        return

    author = input("Enter author: ").strip()
    if not author.replace(" ", "").isalpha():
        print("Error: Author name must contain only letters.")
        return

    book_id = input("Enter ISBN/Book ID: ").strip()
    if not book_id.isdigit():
        print("Error: ISBN/Book ID must be numeric.")
        return

    genre = input("Enter genre: ").strip()

    try:
        price = float(input("Enter price: "))
        if price <= 0:
            print("Error: Price must be a positive number.")
            return
    except ValueError:
        print("Error: Price must be a valid number.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("Error: Quantity must be a non-negative integer.")
            return
    except ValueError:
        print("Error: Quantity must be an integer.")
        return

    if any(book['book_id'] == book_id for book in books):
        print("Error: A book with this ID already exists!")
        return
    
    new_book = {
        "title": title,
        "author": author,
        "book_id": book_id,
        "genre": genre,
        "price": price,
        "quantity": quantity
    }

    books.append(new_book)
    save_books(books)
    print("✅ Book added successfully!")
