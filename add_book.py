from book_data import save_books

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    book_id = input("Enter Book ID: ")
    genre = input("Enter genre: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")
    
    if any(book['book_id'] == book_id for book in books):
        print("Book with this ID already exists!")
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
    print("Book added successfully!")