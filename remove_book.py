from book_data import save_books

def remove_book(books):
    book_id = input("Enter Book ID to remove: ")
    
    for book in books:
        if book['book_id'] == book_id:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return
    
    print("Book not found!")
