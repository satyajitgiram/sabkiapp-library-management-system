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

## API Documentation

### Postman Collection

You can access the API documentation and test the endpoints using our Postman collection in two ways:

1. **Direct Import Link**:
   - Click [here](https://elements.getpostman.com/redirect?entityId=29249303-78999036-dc14-4b43-ab64-374d016da833&entityType=collection) to access the collection
   - Click "Fork" to add it to your workspace
   - Start testing the APIs!

2. **Manual Import**:
   - Download the `postman_collection.json` from this repository
   - Open Postman
   - Click "Import" -> "File" -> Select the downloaded JSON
   - The collection will be added to your workspace

The collection includes examples and documentation for all endpoints:
- Book Management (CRUD operations)
- Member Management
- Borrow/Return Operations
- Filtering and Search examples

## Deployment on Vercel

### Prerequisites
1. A Vercel account
2. A PostgreSQL database (You can use Vercel Postgres or any other provider)
3. Your project pushed to a GitHub repository

### Steps to Deploy

1. **Prepare Your Repository**
   - Push your code to GitHub
   - Make sure all requirements are in `requirements.txt`
   - Ensure `vercel.json` is present in the root directory

2. **Deploy on Vercel**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New" -> "Project"
   - Import your GitHub repository
   - Configure the following environment variables:
     ```
     DATABASE_URL=your_db_url
     DEBUG=False
     SECRET_KEY=your_secret_key
     ```
   - Click "Deploy"

3. **Post-Deployment**
   - Once deployed, go to your project settings
   - Note down your production URL
   - Update your frontend API endpoints if necessary

Your API will be available at: `https://your-project-name.vercel.app/api/`

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
