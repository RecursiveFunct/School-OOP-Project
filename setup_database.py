"""
Run this script once before starting the application to create the database
and load sample data.

    python setup_database.py
"""

import sqlite3
from pathlib import Path


def setup_database(db_path: str = 'library.db'):
    """Create the database schema and load seed data."""

    schema_file = Path(__file__).parent / 'database' / 'schema.sql'
    seed_file = Path(__file__).parent / 'database' / 'seed_data.sql'

    if not schema_file.exists():
        print(f"Error: Schema file not found at {schema_file}")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        with open(schema_file, 'r') as f:
            conn.executescript(f.read())
        conn.commit()
        print(f"Database schema created: {db_path}")

        if seed_file.exists():
            with open(seed_file, 'r') as f:
                conn.executescript(f.read())
            conn.commit()
            print("Sample data loaded.")

        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False


if __name__ == "__main__":
    setup_database()
