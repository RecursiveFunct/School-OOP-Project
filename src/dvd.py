from src.library_item import LibraryItem


class DVD(LibraryItem):
    """
    Represents a DVD in the library system.

    Inherits shared fields and behavior from LibraryItem and adds
    DVD-specific attributes: director, runtime, and content rating.

    Class attributes:
        late_rate (float): Late fee charged per overdue day ($0.50)
        loan_period_days (int): Number of days a DVD can be borrowed (3)
    """

    late_rate = 0.50
    loan_period_days = 3

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R', 'NC-17']

    def __init__(self, isbn, title, author, publisher, director, runtime_minutes, rating):
        super().__init__(isbn, title, author, publisher)
        self._director = director
        self._runtime_minutes = runtime_minutes
        self._rating = rating

    # ------------------------------------------------------------------
    # DVD-specific properties
    # ------------------------------------------------------------------

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("director must be a non-empty string")
        self._director = value

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, value):
        if value < 1:
            raise ValueError("runtime must be at least 1 minute")
        self._runtime_minutes = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value not in self.VALID_RATINGS:
            raise ValueError(f"rating must be one of {self.VALID_RATINGS}")
        self._rating = value

    # ------------------------------------------------------------------
    # Abstract method implementations — TODO: complete these
    # ------------------------------------------------------------------

    def loan_duration_days(self) -> int:
        # TODO: Return the number of days a DVD can be borrowed.
        # Hint: Use the loan_period_days class attribute.
        pass

    def calculate_late_fee(self, days_overdue: int) -> float:
        # TODO: Calculate and return the total late fee.
        # Hint: Multiply days_overdue by the late_rate class attribute.
        pass

    def details(self) -> dict:
        # TODO: Return a dictionary with all details about this DVD.
        # Include: isbn, title, author, publisher, director, runtime_minutes, rating, quantity, available
        pass
