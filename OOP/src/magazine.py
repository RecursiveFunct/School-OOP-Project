from src.library_item import LibraryItem
from datetime import date


class Magazine(LibraryItem):
    """
    Represents a magazine in the library system.

    Inherits shared fields and behavior from LibraryItem and adds
    magazine-specific attributes: issue number, issue date, and article count.

    Class attributes:
        late_rate (float): Late fee charged per overdue day ($0.10)
        loan_period_days (int): Number of days a magazine can be borrowed (7)
    """

    late_rate = 0.10
    loan_period_days = 7

    def __init__(self, isbn, title, author, publisher, issue_number, issue_date, article_count):
        super().__init__(isbn, title, author, publisher)
        self._issue_number = issue_number
        self._issue_date = issue_date
        self._article_count = article_count

    # ------------------------------------------------------------------
    # Magazine-specific properties
    # ------------------------------------------------------------------

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        if value < 1:
            raise ValueError("issue_number must be at least 1")
        self._issue_number = value

    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        if not isinstance(value, date):
            raise ValueError("issue_date must be a date object")
        self._issue_date = value

    @property
    def article_count(self):
        return self._article_count

    @article_count.setter
    def article_count(self, value):
        if value < 1:
            raise ValueError("article_count must be at least 1")
        self._article_count = value

    # ------------------------------------------------------------------
    # Abstract method implementations — TODO: complete these
    # ------------------------------------------------------------------

    def loan_duration_days(self) -> int:
        # TODO: Return the number of days a magazine can be borrowed.
        # Hint: Use the loan_period_days class attribute.
        pass

    def calculate_late_fee(self, days_overdue: int) -> float:
        # TODO: Calculate and return the total late fee.
        # Hint: Multiply days_overdue by the late_rate class attribute.
        pass

    def details(self) -> dict:
        # TODO: Return a dictionary with all details about this magazine.
        # Include: isbn, title, author, publisher, issue_number, issue_date, article_count, quantity, available
        # Hint: Format issue_date as a string using strftime('%Y-%m-%d')
        pass
