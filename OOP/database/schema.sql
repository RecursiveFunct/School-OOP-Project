-- Library Management System — Database Schema
--
-- This schema mirrors the OOP class hierarchy:
--   library_items is the base table (like LibraryItem)
--   books, dvds, magazines are type-specific tables (like child classes)
--
-- Run setup_database.py to initialize this schema.

CREATE TABLE IF NOT EXISTS customers (
    customer_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    email           TEXT UNIQUE,
    phone           TEXT,
    membership_date DATE NOT NULL,
    is_active       INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS library_items (
    item_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    item_type       TEXT NOT NULL,      -- 'Book', 'DVD', or 'Magazine'
    isbn            TEXT UNIQUE NOT NULL,
    title           TEXT NOT NULL,
    author          TEXT NOT NULL,
    publisher       TEXT NOT NULL,
    available       INTEGER DEFAULT 1,
    quantity        INTEGER DEFAULT 1,
    checkout_date   DATE,
    loan_period_days INTEGER,
    customer_id     INTEGER,
    date_added      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS books (
    book_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id  INTEGER UNIQUE NOT NULL,
    genre    TEXT,
    pages    INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES library_items(item_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS dvds (
    dvd_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id         INTEGER UNIQUE NOT NULL,
    director        TEXT,
    runtime_minutes INTEGER NOT NULL,
    rating          TEXT NOT NULL,
    FOREIGN KEY (item_id) REFERENCES library_items(item_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS magazines (
    magazine_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id       INTEGER UNIQUE NOT NULL,
    issue_number  INTEGER NOT NULL,
    issue_date    DATE NOT NULL,
    article_count INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES library_items(item_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS checkouts (
    checkout_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id           INTEGER NOT NULL,
    customer_id       INTEGER NOT NULL,
    checkout_date     DATE NOT NULL,
    due_date          DATE NOT NULL,
    return_date       DATE,
    late_fee_charged  REAL DEFAULT 0.0,
    FOREIGN KEY (item_id)     REFERENCES library_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Indexes to speed up common lookups
CREATE INDEX IF NOT EXISTS idx_isbn          ON library_items(isbn);
CREATE INDEX IF NOT EXISTS idx_item_type     ON library_items(item_type);
CREATE INDEX IF NOT EXISTS idx_checkout_item ON checkouts(item_id);
CREATE INDEX IF NOT EXISTS idx_checkout_cust ON checkouts(customer_id);
