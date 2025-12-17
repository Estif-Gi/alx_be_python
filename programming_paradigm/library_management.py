class book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = _is_checked_out
class library:
    def __init__(self):
        self._books  = []

    def add_book(self, title):
        self._books.append(title)

    def check_out_book(self, title):
        book = self.find_book(title)
        if book:
            book.is_checked_out = True
        return book

    def find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None
    def list_available_books(self):
        return self._books