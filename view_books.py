def view_books(books):
    if not books:
        print("No books available!")
        return
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, ID: {book['book_id']}, Genre: {book['genre']}, Price: {book['price']}, Stock: {book['quantity']}")