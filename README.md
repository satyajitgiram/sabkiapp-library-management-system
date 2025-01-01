# Library Management System

A Django-based Library Management System with RESTful APIs for managing books, members, and borrowing records.

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Database Setup:
- Install PostgreSQL if not already installed
- Create a database named 'library_db'
```sql
CREATE DATABASE library_db;
```

4. Configure Database:
- Update database credentials in `library_management/settings.py` if needed

5. Run Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the Development Server:
```bash
python manage.py runserver
```

## API Endpoints

### Books
- `POST /books/`: Add a new book
- `GET /books/`: List all books (with filtering options)

### Members
- `POST /members/`: Register a new member
- `GET /members/`: List all members (with pagination)

### Borrowing
- `POST /borrow/`: Borrow a book
- `POST /return/`: Return a book

## Features
- Book management with availability tracking
- Member registration and management
- Borrowing system with proper validation
- Advanced filtering and pagination
- Database optimization with proper indexing
