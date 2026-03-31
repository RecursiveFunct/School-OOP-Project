-- Sample data for the Library Management System
-- This file is loaded automatically when you run setup_database.py

-- Sample customers
INSERT INTO customers (first_name, last_name, email, phone, membership_date, is_active) VALUES
('Alice',  'Johnson', 'alice.johnson@email.com', '555-0101', '2024-01-15', 1),
('Bob',    'Smith',   'bob.smith@email.com',     '555-0102', '2024-02-20', 1),
('Carol',  'Davis',   'carol.davis@email.com',   '555-0103', '2024-03-10', 1),
('David',  'Wilson',  'david.wilson@email.com',  '555-0104', '2024-04-05', 1);

-- Sample books
INSERT INTO library_items (item_type, isbn, title, author, publisher, available, quantity, loan_period_days) VALUES
('Book', '978-0-13-110362-7', 'The C Programming Language', 'Brian W. Kernighan', 'Prentice Hall',  1, 3, 14),
('Book', '978-0-201-63361-0', 'Design Patterns',            'Gang of Four',       'Addison-Wesley', 1, 2, 14),
('Book', '978-0-596-00712-6', 'Learning Python',            'Mark Lutz',          'O''Reilly Media', 1, 4, 14);

INSERT INTO books (item_id, genre, pages) VALUES
(1, 'Programming',      274),
(2, 'Software Design',  395),
(3, 'Python',          1216);

-- Sample DVDs
INSERT INTO library_items (item_type, isbn, title, author, publisher, available, quantity, loan_period_days) VALUES
('DVD', '978-0-7952-7533-0', 'The Matrix',   'Lana Wachowski',    'Warner Bros', 1, 2, 3),
('DVD', '978-0-7952-8715-9', 'Inception',    'Christopher Nolan', 'Warner Bros', 1, 1, 3),
('DVD', '978-0-8160-8370-5', 'Interstellar', 'Christopher Nolan', 'Paramount',   1, 2, 3);

INSERT INTO dvds (item_id, director, runtime_minutes, rating) VALUES
(4, 'Lana Wachowski',    136, 'R'),
(5, 'Christopher Nolan', 148, 'PG-13'),
(6, 'Christopher Nolan', 169, 'PG-13');

-- Sample magazines
INSERT INTO library_items (item_type, isbn, title, author, publisher, available, quantity, loan_period_days) VALUES
('Magazine', '978-0-7432-5000-0', 'National Geographic', 'Various', 'National Geographic', 1, 5, 7),
('Magazine', '978-0-375-50214-2', 'Popular Science',     'Various', 'Popular Science',     1, 3, 7),
('Magazine', '978-1-4926-0000-0', 'Time Magazine',       'Various', 'Time Inc',            1, 4, 7);

INSERT INTO magazines (item_id, issue_number, issue_date, article_count) VALUES
(7, 42, '2024-06-01', 15),
(8, 10, '2024-06-15', 12),
(9, 26, '2024-06-26', 18);
