class Book:
    """A class to represent a book with title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Check out the book (mark as unavailable)."""
        self._is_checked_out = True
    
    def return_book(self):
        """Return the book (mark as available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If book not found or not available, we could add error handling here
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        # If book not found, we could add error handling here
    
    def list_available_books(self):
        """List all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")