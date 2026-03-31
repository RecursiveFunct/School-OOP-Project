# Library Management System
### Object-Oriented Programming Assessment

---

## Overview

In this project you will finish building a **Library Lending Manager** — a small Python application that manages a collection of books, DVDs, and magazines. The starter code gives you a working foundation. Your job is to complete the missing pieces, connect them together, and make the system functional.

By the end of this project your application should allow a user to:

- Add new items to the library
- Search for items by title or author
- Check out and return items
- View overdue items and active customer loans

---

## Project Structure

```
OOP/
├── main.py                  # Entry point — contains the menu and user interface
├── setup_database.py        # Run this once to create your database
│
├── src/
│   ├── library_item.py      # PROVIDED — abstract base class for all items
│   ├── book.py              # COMPLETE ME — Book class
│   ├── dvd.py               # COMPLETE ME — DVD class
│   ├── magazine.py          # COMPLETE ME — Magazine class
│   └── database_manager.py  # PROVIDED — handles all database operations
│
├── database/
│   ├── schema.sql           # PROVIDED — database table definitions
│   └── seed_data.sql        # PROVIDED — sample data loaded on setup
│
└── tests/
    └── test_library.py      # COMPLETE ME — write your tests here
```

**PROVIDED** files are fully implemented. Read them to understand how they work, but you should not need to modify them.

**COMPLETE ME** files have `TODO` comments marking the code you need to write.

---

## Getting Started

**1. Set up your database** (run this once):
```
python setup_database.py
```

**2. Run the application:**
```
python main.py
```

**3. Run your tests:**
```
python tests/test_library.py
```

---

## What You Need to Implement

### 1. Complete the child classes (`src/book.py`, `src/dvd.py`, `src/magazine.py`)

Each class already has its constructor and properties written for you. Your task is to implement the three abstract methods that every item type must have:

| Method | What it should do |
|---|---|
| `loan_duration_days()` | Return the number of days this item type can be borrowed |
| `calculate_late_fee(days_overdue)` | Return the total late fee as a float |
| `details()` | Return a dictionary of all item attributes |

Refer to the class attributes (`late_rate`, `loan_period_days`) already defined at the top of each class.

**Loan periods and late rates:**
| Type | Loan Period | Late Fee |
|---|---|---|
| Book | 14 days | $0.25 / day |
| DVD | 3 days | $0.50 / day |
| Magazine | 7 days | $0.10 / day |

### 2. Complete the menu methods in `main.py`

The `view_all_items()` method is fully implemented as a working example — read it carefully to understand the pattern. Then implement the remaining methods, each marked with a `TODO` comment:

- `add_item_menu()` — collect input and add a new item
- `search_items()` — search and display results
- `checkout_item_menu()` — process a checkout
- `return_item_menu()` — process a return
- `view_overdue_items()` — display overdue items
- `view_customer_checkouts()` — display a customer's active loans

Each `TODO` includes hints about which `DatabaseManager` method to call.

### 3. Write tests in `tests/test_library.py`

Several example tests are already written. Add your own to verify your implementations work correctly, including edge cases and invalid input.

---

## OOP Concepts to Demonstrate

Your completed project should clearly show all four pillars of OOP:

| Concept | Where it appears |
|---|---|
| **Abstraction** | `LibraryItem` defines abstract methods that child classes must implement |
| **Inheritance** | `Book`, `DVD`, and `Magazine` all inherit shared fields and behavior from `LibraryItem` |
| **Encapsulation** | Attributes are protected (`_name`) and accessed through properties with validation |
| **Polymorphism** | Calling `calculate_late_fee()` on a `Book`, `DVD`, or `Magazine` produces different results |

---

## Deliverables

*Project Organization*
| Deliverable | Description |
|---|---|
| Repo Directory | Project uses the provided directory structure appropriately |
| README.md | Your README explains the project and how to run it |
| GitHub Repo | Project is pushed to your assigned GitHub repo — **failure to push means the project will not be graded** |

*Class Structures*
| Deliverable | Description |
|---|---|
| Abstract Base Class | `LibraryItem` serves as the abstract parent with abstract methods |
| Derived Classes | `Book`, `DVD`, and `Magazine` provide complete implementations of all abstract methods |
| Encapsulation | Protected attributes accessed and validated through property getters and setters |
| Abstraction | Menu code in `main.py` works with item objects without knowing their internal details |
| Inheritance | Child classes inherit shared fields and can access base class data |
| Polymorphism | The same method call behaves differently depending on the item type |
| Constructors and Instances | Functional instances of each class can be created and used |

*Database and Queries*
| Deliverable | Description |
|---|---|
| Database File | A `.db` file is included in your repo with the correct tables and data |
| SQL Files | Schema and seed data SQL files are present in the `database/` folder |

*Questions and Free Response*
| Deliverable | Description |
|---|---|
| Reflection | All reflection questions are answered in complete sentences |

---

## Scoring Guide

| Score | Description |
|---|---|
| 4 | All deliverables complete. Project is fully functional and the README clearly explains it. |
| 3 | All deliverables complete. Project works with minor issues. |
| 2 | Most deliverables complete. A few gaps in functionality or explanation. |
| 1 | Some deliverables complete. Significant gaps remain. |
| 0 | Little to no work submitted. |

---

## Evidence of Testing

Include evidence of testing in your submission:
- A short section in this README (below) describing what you tested and what happened
- Seed data already in the database to show sample records
- Your completed `tests/test_library.py` with all tests passing

---

## Reflection Questions

Answer each question in 2–3 sentences. Write your answers directly in this README.

1. What is the role of `LibraryItem` as an abstract base class? Why is it useful to have one?
   - *Answer:*

2. What do the abstract methods (`loan_duration_days`, `calculate_late_fee`, `details`) force each child class to do? Why does this lead to better design?
   - *Answer:*

3. How does encapsulation (protected attributes + property setters with validation) protect your data? Give a specific example from the code.
   - *Answer:*

4. How does polymorphism appear in this project? Give an example of the same method call producing a different result depending on the object type.
   - *Answer:*

5. How is the database structured? What does each table store, and how do the tables relate to each other?
   - *Answer:*

6. What was the most challenging part of this project for you, and how did you work through it?
   - *Answer:*

---

## Testing Evidence

*Replace this section with your own notes after you test the application.*

Tested scenarios:
- [ ] Adding a book, DVD, and magazine
- [ ] Searching by title
- [ ] Checking out an item
- [ ] Returning an item (on time and late)
- [ ] Viewing overdue items
