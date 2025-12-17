# library_management.py
# A simple library management system demonstrating OOP concepts


class Book:
    """
    Represents a single book in the library.
    Has public attributes for title and author,
    and a private attribute to track checkout status.
    """

    def __init__(self, title, author):
        """Initialize a new book with title and author. Initially available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute: True if checked out

    def check_out(self):
        """Mark the book as checked out. Returns True if successful."""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned (available again). Returns True if successful."""
        if not self._is_checked_out:
            return False  # Was not checked out
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is currently available (not checked out)."""
        return not self._is_checked_out

    # Optional: nice string representation for debugging/printing
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    Provides methods to add books, check them out, return them,
    and list available ones.
    """

    def __init__(self):
        """Initialize an empty library with a private list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Add a Book instance to the library.
        :param book: An instance of the Book class
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.
        Marks the book as checked out if found and available.
        :param title: The title of the book to check out
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If not found or already checked out, do nothing (silent fail as per example)

    def return_book(self, title):
        """
        Return a book by its title.
        Marks the book as available again if found and currently checked out.
        :param title: The title of the book to return
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # Silent if not found or not checked out

    def list_available_books(self):
        """Print all books that are currently available (not checked out)."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")