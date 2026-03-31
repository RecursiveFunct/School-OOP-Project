import sqlite3
from datetime import date, timedelta
from typing import List, Dict, Optional, Tuple


class DatabaseManager:
    """Manages all database operations for the library system."""

    def __init__(self, db_path: str = 'library.db'):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    # ------------------------------------------------------------------
    # Connection management
    # ------------------------------------------------------------------

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            self.cursor.execute('PRAGMA foreign_keys = ON')
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

    def disconnect(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    # ------------------------------------------------------------------
    # Generic query helpers
    # ------------------------------------------------------------------

    def execute_query(self, query: str, params: tuple = ()) -> bool:
        """Execute a data-modifying query (INSERT, UPDATE, DELETE)."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()
            return False

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[tuple]:
        """Fetch a single row from the database."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def fetch_all(self, query: str, params: tuple = ()) -> List[tuple]:
        """Fetch all matching rows from the database."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    # ------------------------------------------------------------------
    # Customer operations
    # ------------------------------------------------------------------

    def add_customer(self, first_name: str, last_name: str, email: str, phone: str) -> Optional[int]:
        """Add a new customer and return their assigned ID."""
        query = '''INSERT INTO customers (first_name, last_name, email, phone, membership_date, is_active)
                   VALUES (?, ?, ?, ?, ?, 1)'''
        if self.execute_query(query, (first_name, last_name, email, phone, date.today())):
            return self.cursor.lastrowid
        return None

    # ------------------------------------------------------------------
    # Item operations
    # ------------------------------------------------------------------

    def add_book(self, isbn: str, title: str, author: str, publisher: str,
                 genre: str, pages: int) -> Optional[int]:
        """Add a new book to the database. Returns the new item's ID."""
        query_items = '''INSERT INTO library_items
                         (item_type, isbn, title, author, publisher, available, quantity, loan_period_days)
                         VALUES (?, ?, ?, ?, ?, 1, 1, 14)'''
        if self.execute_query(query_items, ('Book', isbn, title, author, publisher)):
            item_id = self.cursor.lastrowid
            query_book = 'INSERT INTO books (item_id, genre, pages) VALUES (?, ?, ?)'
            if self.execute_query(query_book, (item_id, genre, pages)):
                return item_id
        return None

    def add_dvd(self, isbn: str, title: str, author: str, publisher: str,
                director: str, runtime: int, rating: str) -> Optional[int]:
        """Add a new DVD to the database. Returns the new item's ID."""
        query_items = '''INSERT INTO library_items
                         (item_type, isbn, title, author, publisher, available, quantity, loan_period_days)
                         VALUES (?, ?, ?, ?, ?, 1, 1, 3)'''
        if self.execute_query(query_items, ('DVD', isbn, title, author, publisher)):
            item_id = self.cursor.lastrowid
            query_dvd = 'INSERT INTO dvds (item_id, director, runtime_minutes, rating) VALUES (?, ?, ?, ?)'
            if self.execute_query(query_dvd, (item_id, director, runtime, rating)):
                return item_id
        return None

    def add_magazine(self, isbn: str, title: str, author: str, publisher: str,
                     issue_num: int, issue_date: date, article_count: int) -> Optional[int]:
        """Add a new magazine to the database. Returns the new item's ID."""
        query_items = '''INSERT INTO library_items
                         (item_type, isbn, title, author, publisher, available, quantity, loan_period_days)
                         VALUES (?, ?, ?, ?, ?, 1, 1, 7)'''
        if self.execute_query(query_items, ('Magazine', isbn, title, author, publisher)):
            item_id = self.cursor.lastrowid
            query_mag = 'INSERT INTO magazines (item_id, issue_number, issue_date, article_count) VALUES (?, ?, ?, ?)'
            if self.execute_query(query_mag, (item_id, issue_num, issue_date, article_count)):
                return item_id
        return None

    def get_all_items(self) -> List[Dict]:
        """Return a list of all items in the library."""
        query = '''SELECT item_id, item_type, isbn, title, author, publisher, available, quantity
                   FROM library_items
                   ORDER BY title'''
        results = self.fetch_all(query)
        return [
            {
                'item_id': row[0], 'item_type': row[1], 'isbn': row[2],
                'title': row[3], 'author': row[4], 'publisher': row[5],
                'available': row[6], 'quantity': row[7]
            }
            for row in results
        ]

    def get_item_by_id(self, item_id: int) -> Optional[Dict]:
        """Return details for a single item by its ID."""
        query = '''SELECT item_id, item_type, isbn, title, author, publisher, available, quantity
                   FROM library_items
                   WHERE item_id = ?'''
        row = self.fetch_one(query, (item_id,))
        if row:
            return {
                'item_id': row[0], 'item_type': row[1], 'isbn': row[2],
                'title': row[3], 'author': row[4], 'publisher': row[5],
                'available': row[6], 'quantity': row[7]
            }
        return None

    def search_items(self, search_term: str) -> List[Dict]:
        """Search for items by title or author (case-insensitive partial match)."""
        query = '''SELECT item_id, item_type, isbn, title, author, publisher, available, quantity
                   FROM library_items
                   WHERE title LIKE ? OR author LIKE ?
                   ORDER BY title'''
        pattern = f'%{search_term}%'
        results = self.fetch_all(query, (pattern, pattern))
        return [
            {
                'item_id': row[0], 'item_type': row[1], 'isbn': row[2],
                'title': row[3], 'author': row[4], 'publisher': row[5],
                'available': row[6], 'quantity': row[7]
            }
            for row in results
        ]

    # ------------------------------------------------------------------
    # Checkout and return operations
    # ------------------------------------------------------------------

    def checkout_item(self, item_id: int, customer_id: int) -> bool:
        """Record a checkout transaction. Returns True on success."""
        # Verify item exists and is available
        item = self.fetch_one(
            'SELECT loan_period_days, available FROM library_items WHERE item_id = ?',
            (item_id,)
        )
        if not item:
            print("Item not found.")
            return False
        if not item[1]:
            print("Item is not available for checkout.")
            return False

        loan_days = item[0]
        due_date = date.today() + timedelta(days=loan_days)

        # Record the checkout
        checkout_query = '''INSERT INTO checkouts (item_id, customer_id, checkout_date, due_date, late_fee_charged)
                            VALUES (?, ?, ?, ?, 0)'''
        if self.execute_query(checkout_query, (item_id, customer_id, date.today(), due_date)):
            # Mark item as unavailable
            update_query = '''UPDATE library_items
                              SET available = 0, customer_id = ?, checkout_date = ?
                              WHERE item_id = ?'''
            return self.execute_query(update_query, (customer_id, date.today(), item_id))
        return False

    def return_item(self, item_id: int, customer_id: int) -> Tuple[bool, float]:
        """
        Record an item return and calculate any late fee.
        Returns a tuple of (success, late_fee_amount).
        """
        # Find the active checkout record
        checkout = self.fetch_one(
            '''SELECT checkout_id, due_date FROM checkouts
               WHERE item_id = ? AND customer_id = ? AND return_date IS NULL
               ORDER BY checkout_id DESC LIMIT 1''',
            (item_id, customer_id)
        )
        if not checkout:
            print("No active checkout found for this item and customer.")
            return False, 0.0

        checkout_id, due_date_str = checkout
        today = date.today()
        days_overdue = max(0, (today - date.fromisoformat(due_date_str)).days)

        # Determine late fee based on item type
        item_type_row = self.fetch_one('SELECT item_type FROM library_items WHERE item_id = ?', (item_id,))
        item_type = item_type_row[0] if item_type_row else 'Book'

        late_fee = 0.0
        if days_overdue > 0:
            rates = {'Book': 0.25, 'DVD': 0.50, 'Magazine': 0.10}
            late_fee = days_overdue * rates.get(item_type, 0.25)

        # Update the checkout record
        return_query = '''UPDATE checkouts SET return_date = ?, late_fee_charged = ?
                          WHERE checkout_id = ?'''
        if self.execute_query(return_query, (today, late_fee, checkout_id)):
            # Mark item as available again
            self.execute_query(
                'UPDATE library_items SET available = 1, customer_id = NULL WHERE item_id = ?',
                (item_id,)
            )
            return True, late_fee
        return False, 0.0

    # ------------------------------------------------------------------
    # Reporting operations
    # ------------------------------------------------------------------

    def get_overdue_items(self) -> List[Dict]:
        """Return all items that are currently overdue."""
        query = '''SELECT
                       li.item_id,
                       li.title,
                       li.item_type,
                       c.first_name,
                       c.last_name,
                       ch.checkout_date,
                       ch.due_date,
                       CAST((julianday('now') - julianday(ch.due_date)) AS INTEGER) AS days_overdue
                   FROM library_items li
                   INNER JOIN checkouts ch ON li.item_id = ch.item_id
                   INNER JOIN customers c ON ch.customer_id = c.customer_id
                   WHERE ch.return_date IS NULL AND julianday('now') > julianday(ch.due_date)
                   ORDER BY ch.due_date'''
        results = self.fetch_all(query)
        return [
            {
                'item_id': row[0], 'title': row[1], 'item_type': row[2],
                'customer_name': f"{row[3]} {row[4]}",
                'checkout_date': row[5], 'due_date': row[6], 'days_overdue': row[7]
            }
            for row in results
        ]

    def get_customer_checkouts(self, customer_id: int) -> List[Dict]:
        """Return all active (unreturned) checkouts for a customer."""
        query = '''SELECT
                       li.item_id,
                       li.title,
                       li.item_type,
                       ch.checkout_date,
                       ch.due_date
                   FROM checkouts ch
                   INNER JOIN library_items li ON ch.item_id = li.item_id
                   WHERE ch.customer_id = ? AND ch.return_date IS NULL
                   ORDER BY ch.due_date'''
        results = self.fetch_all(query, (customer_id,))
        return [
            {
                'item_id': row[0], 'title': row[1], 'item_type': row[2],
                'checkout_date': row[3], 'due_date': row[4]
            }
            for row in results
        ]
