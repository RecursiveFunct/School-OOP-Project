from src.database_manager import DatabaseManager
from src.book import Book
from src.dvd import DVD
from src.magazine import Magazine
from datetime import date


class LibrarySystem:
    """Main interface for the Library Management System."""

    def __init__(self, db_path: str = 'library.db'):
        self.db = DatabaseManager(db_path)
        self.db.connect()

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 50)
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Item to Library")
        print("2. Search Items")
        print("3. View All Items")
        print("4. Checkout Item")
        print("5. Return Item")
        print("6. View Overdue Items")
        print("7. View Customer Checkouts")
        print("8. Exit")
        print("=" * 50)

    def view_all_items(self):
        """Display all items currently in the library."""
        items = self.db.get_all_items()

        if not items:
            print("\nNo items in the library.")
            return

        print(f"\n{'ID':<5} {'Type':<12} {'Title':<30} {'Author':<20} {'Available'}")
        print("-" * 75)
        for item in items:
            status = "Yes" if item['available'] else "No"
            print(f"{item['item_id']:<5} {item['item_type']:<12} {item['title']:<30} {item['author']:<20} {status}")

    def add_item_menu(self):
        """Prompt the user to add a new item to the library."""
        # TODO: Ask the user what type of item to add (Book, DVD, or Magazine).
        # Collect the relevant input fields for that item type.
        # Create an instance of the appropriate class (Book, DVD, or Magazine).
        # Use self.db.add_book(), self.db.add_dvd(), or self.db.add_magazine() to save it.
        # Print a confirmation message if successful.
        #
        # Hint — common fields for all item types:
        #   isbn, title, author, publisher
        #
        # Book-specific:   genre, pages (int)
        # DVD-specific:    director, runtime_minutes (int), rating (e.g. 'PG-13')
        # Magazine-specific: issue_number (int), issue_date (date), article_count (int)
        #
        # Example of creating a Book object and printing its details:
        #   book = Book(isbn, title, author, publisher, genre, pages)
        #   print(book.details())
        pass

    def search_items(self):
        """Search for items by title or author."""
        # TODO: Ask the user for a search term.
        # Use self.db.search_items(search_term) to get matching results.
        # Display the results in a readable format.
        # Handle the case where no items are found.
        pass

    def checkout_item_menu(self):
        """Check out an item to a customer."""
        # TODO: Ask the user for an item ID and a customer ID.
        # Use self.db.checkout_item(item_id, customer_id) to process the checkout.
        # Print a success or failure message.
        # Hint: get_item_by_id(item_id) can retrieve the item's title for a friendly message.
        pass

    def return_item_menu(self):
        """Process the return of a checked-out item."""
        # TODO: Ask the user for the item ID and customer ID.
        # Use self.db.return_item(item_id, customer_id) — it returns (success, late_fee).
        # If late_fee > 0, inform the customer of the amount owed.
        pass

    def view_overdue_items(self):
        """Display all items that are currently overdue."""
        # TODO: Use self.db.get_overdue_items() to retrieve overdue items.
        # Display the results showing: item title, type, customer name, due date, days overdue.
        # Handle the case where nothing is overdue.
        pass

    def view_customer_checkouts(self):
        """Display all active checkouts for a specific customer."""
        # TODO: Ask the user for a customer ID.
        # Use self.db.get_customer_checkouts(customer_id) to retrieve their active loans.
        # Display each item's title, type, and due date.
        pass

    def run(self):
        """Main program loop."""
        print("Welcome to the Library Management System!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ").strip()

            if choice == '1':
                self.add_item_menu()
            elif choice == '2':
                self.search_items()
            elif choice == '3':
                self.view_all_items()
            elif choice == '4':
                self.checkout_item_menu()
            elif choice == '5':
                self.return_item_menu()
            elif choice == '6':
                self.view_overdue_items()
            elif choice == '7':
                self.view_customer_checkouts()
            elif choice == '8':
                print("\nGoodbye!")
                self.db.disconnect()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    system = LibrarySystem()
    system.run()
