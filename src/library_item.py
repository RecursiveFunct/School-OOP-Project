from abc import ABC, abstractmethod
from datetime import timedelta, date


class LibraryItem(ABC):
    """
    Abstract base class for all library items.

    This class defines the shared structure that every library item must have,
    including common fields like title, author, and availability tracking.

    Child classes (Book, DVD, Magazine) must implement the abstract methods
    defined here. This enforces a consistent interface across all item types.
    """

    def __init__(self, isbn, title, author, publisher):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher

        self._available = True
        self._quantity = 1
        self._checkout_date = date.min
        self._loan_period = timedelta()
        self._customer_id = 0

    # ------------------------------------------------------------------
    # Abstract methods — every child class MUST override these
    # ------------------------------------------------------------------

    @abstractmethod
    def loan_duration_days(self) -> int:
        """Return the number of days this item type can be borrowed."""
        pass

    @abstractmethod
    def calculate_late_fee(self, days_overdue: int) -> float:
        """Calculate and return the late fee for the given number of overdue days."""
        pass

    @abstractmethod
    def details(self) -> dict:
        """Return a dictionary containing all details about this item."""
        pass

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def publisher(self):
        return self._publisher

    @property
    def available(self):
        return self._available

    @property
    def quantity(self):
        return self._quantity

    @property
    def checkout_date(self):
        return self._checkout_date

    @property
    def loan_period(self):
        return self._loan_period

    @property
    def customer_id(self):
        return self._customer_id

    # ------------------------------------------------------------------
    # Setters (with validation)
    # ------------------------------------------------------------------

    @available.setter
    def available(self, status: bool):
        if not isinstance(status, bool):
            raise ValueError("available must be a boolean")
        self._available = status

    @quantity.setter
    def quantity(self, qty: int):
        if qty < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = qty

    @checkout_date.setter
    def checkout_date(self, new_date: date):
        if not isinstance(new_date, date):
            raise ValueError("checkout_date must be a date")
        self._checkout_date = new_date

    @loan_period.setter
    def loan_period(self, period: timedelta):
        if not isinstance(period, timedelta):
            raise ValueError("loan_period must be a timedelta")
        self._loan_period = period

    @customer_id.setter
    def customer_id(self, customer_id: int):
        if customer_id < 0:
            raise ValueError("customer_id cannot be negative")
        self._customer_id = customer_id
