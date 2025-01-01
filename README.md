# Library Management System

A Django-based Library Management System with RESTful APIs for managing books, members, and borrowing records.

## Features

- Book management with availability tracking
- Member registration and status management
- Book borrowing and return system
- Advanced filtering and search capabilities
- Pagination for all list endpoints
- Realistic data seeding for testing

## Database Setup

This project uses PostgreSQL database hosted on Neon.tech. To set up the database:

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Update the `DATABASE_URL` in `.env` with your database credentials:
```
DATABASE_URL='postgresql://<user>:<password>@<host>/<database>?sslmode=require'
```

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Seed the database with sample data:
```bash
python manage.py seed_data
```
This will create:
- 30 books with realistic titles and authors
- 20 members with proper details
- 25 borrow records with realistic dates

## API Endpoints

### Books
- `POST /api/books/`: Add a new book
- `GET /api/books/`: List all books
  - Query params: title, author, category
  - Pagination enabled

### Members
- `POST /api/members/`: Register a new member
- `GET /api/members/`: List all members
  - Pagination enabled

### Borrowing
- `POST /api/borrow-records/borrow_book/`: Borrow a book
- `POST /api/borrow-records/return_book/`: Return a book
- `GET /api/borrow-records/`: List all borrowing records
  - Pagination enabled

## Logging

The application uses Django's logging framework to track important events and errors. Logs are stored in two locations:

1. Console Output: Debug and higher level messages
2. File: `logs/library.log` contains all INFO and higher level messages

### Log Levels:
- DEBUG: Detailed information for debugging
- INFO: General system information and successful operations
- WARNING: Issues that don't prevent operation but should be noted
- ERROR: Serious problems that prevent operations from completing

### Log File Location
Logs are stored in the `logs/library.log` file. Make sure the `logs` directory exists and is writable.

## Development

The project uses:
- Django 5.1.4
- Django REST Framework 3.15.2
- PostgreSQL (via psycopg2-binary)
- python-dotenv for environment management
- Faker for generating test data
