from src.library_item import LibraryItem


class Book(LibraryItem):
    """
    Represents a book in the library system.

    Inherits shared fields and behavior from LibraryItem and adds
    book-specific attributes: genre and page count.

    Class attributes:
        late_rate (float): Late fee charged per overdue day ($0.25)
        loan_period_days (int): Number of days a book can be borrowed (14)
    """

    late_rate = 0.25
    loan_period_days = 14

    def __init__(self, isbn, title, author, publisher, genre, pages):
        super().__init__(isbn, title, author, publisher)
        self._genre = genre
        self._pages = pages

    # ------------------------------------------------------------------
    # Book-specific properties
    # ------------------------------------------------------------------

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("genre must be a non-empty string")
        self._genre = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value < 1:
            raise ValueError("pages must be at least 1")
        self._pages = value

    # ------------------------------------------------------------------
    # Abstract method implementations — TODO: complete these
    # ------------------------------------------------------------------

    def loan_duration_days(self) -> int:
        # TODO: Return the number of days a book can be borrowed.
        # Hint: Use the loan_period_days class attribute.
        pass

    def calculate_late_fee(self, days_overdue: int) -> float:
        # TODO: Calculate and return the total late fee.
        # Hint: Multiply days_overdue by the late_rate class attribute.
        pass

    def details(self) -> dict:
        # TODO: Return a dictionary with all details about this book.
        # Include: isbn, title, author, publisher, genre, pages, quantity, available
        pass
