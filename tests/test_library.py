"""
Library System — Test File

Use this file to test your class implementations.
You do not need a special testing framework — just run this file directly:

    python tests/test_library.py

A simple way to test is to create instances of your classes, call their
methods, and check that the output matches what you expect.
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import from src
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.book import Book
from src.dvd import DVD
from src.magazine import Magazine
from datetime import date


# ----------------------------------------------------------------------
# Example tests — run these to check your implementations
# ----------------------------------------------------------------------

def test_book():
    """Test the Book class."""
    book = Book(
        isbn='978-0-13-110362-7',
        title='The C Programming Language',
        author='Brian W. Kernighan',
        publisher='Prentice Hall',
        genre='Programming',
        pages=274
    )

    # Test loan_duration_days
    assert book.loan_duration_days() == 14, "Book loan period should be 14 days"

    # Test calculate_late_fee
    assert book.calculate_late_fee(4) == 1.00, "4 days overdue at $0.25/day should be $1.00"

    # Test details returns a dict
    info = book.details()
    assert isinstance(info, dict), "details() should return a dictionary"
    assert info['title'] == 'The C Programming Language'

    print("Book tests passed.")


def test_dvd():
    """Test the DVD class."""
    dvd = DVD(
        isbn='978-0-7952-7533-0',
        title='The Matrix',
        author='Lana Wachowski',
        publisher='Warner Bros',
        director='Lana Wachowski',
        runtime_minutes=136,
        rating='R'
    )

    # Test loan_duration_days
    assert dvd.loan_duration_days() == 3, "DVD loan period should be 3 days"

    # Test calculate_late_fee
    assert dvd.calculate_late_fee(2) == 1.00, "2 days overdue at $0.50/day should be $1.00"

    # Test details
    info = dvd.details()
    assert isinstance(info, dict), "details() should return a dictionary"
    assert info['director'] == 'Lana Wachowski'

    print("DVD tests passed.")


def test_magazine():
    """Test the Magazine class."""
    magazine = Magazine(
        isbn='978-0-7432-5000-0',
        title='National Geographic',
        author='Various',
        publisher='National Geographic',
        issue_number=42,
        issue_date=date(2024, 6, 1),
        article_count=15
    )

    # Test loan_duration_days
    assert magazine.loan_duration_days() == 7, "Magazine loan period should be 7 days"

    # Test calculate_late_fee
    assert magazine.calculate_late_fee(10) == 1.00, "10 days overdue at $0.10/day should be $1.00"

    # Test details
    info = magazine.details()
    assert isinstance(info, dict), "details() should return a dictionary"
    assert info['issue_number'] == 42

    print("Magazine tests passed.")


def test_inheritance():
    """Test that child classes properly inherit from LibraryItem."""
    from src.library_item import LibraryItem

    book = Book('111', 'Test Book', 'Author', 'Publisher', 'Fiction', 100)

    assert isinstance(book, LibraryItem), "Book should be an instance of LibraryItem"
    assert book.title == 'Test Book'
    assert book.available == True

    print("Inheritance tests passed.")


# TODO: Add your own tests below. Think about:
#   - What happens if you pass invalid data to a setter?
#   - Does encapsulation work correctly (can you access private attributes directly)?
#   - Do all three item types behave differently when calculate_late_fee is called?


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------

if __name__ == "__main__":
    test_book()
    test_dvd()
    test_magazine()
    test_inheritance()
    print("\nAll tests passed!")
