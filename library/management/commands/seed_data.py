from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from library.models import Book, Member, BorrowRecord
from datetime import timedelta
import random

fake = Faker()

# book categories
BOOK_CATEGORIES = [
    'Fiction', 'Science Fiction', 'Mystery', 'Romance', 'Thriller',
    'Biography', 'History', 'Science', 'Technology', 'Business',
    'Self-Help', 'Philosophy', 'Poetry', 'Drama', 'Children'
]

# book titles and authors
POPULAR_AUTHORS = [
    'J.K. Rowling', 'Stephen King', 'George R.R. Martin', 'Jane Austen',
    'Ernest Hemingway', 'Virginia Woolf', 'Gabriel García Márquez',
    'Haruki Murakami', 'Agatha Christie', 'Paulo Coelho'
]

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create 30 books
        books = []
        for _ in range(30):
            published_date = fake.date_between(start_date='-30y', end_date='today')
            book = Book.objects.create(
                title=fake.catch_phrase(),
                author=random.choice(POPULAR_AUTHORS),
                published_date=published_date,
                category=random.choice(BOOK_CATEGORIES),
                available_copies=random.randint(1, 10)
            )
            books.append(book)
            self.stdout.write(f'Created book: {book.title}')

        # Create 20 members
        members = []
        for _ in range(20):
            membership_date = fake.date_between(start_date='-5y', end_date='today')
            member = Member.objects.create(
                name=fake.name(),
                email=fake.email(),
                membership_date=membership_date,
                membership_status=random.choice(['Active', 'Active', 'Active', 'Inactive'])  # 75% active
            )
            members.append(member)
            self.stdout.write(f'Created member: {member.name}')

        # Create 25 borrow records
        for _ in range(25):
            member = random.choice(members)
            book = random.choice(books)
            borrow_date = fake.date_between(start_date='-1y', end_date='today')
            
            # 80% chance of book being returned
            return_date = None
            if random.random() < 0.8:
                return_date = fake.date_between(
                    start_date=borrow_date,
                    end_date=borrow_date + timedelta(days=30)
                )

            if return_date is None and book.available_copies > 0:
                book.available_copies -= 1
                book.save()

            borrow_record = BorrowRecord.objects.create(
                member=member,
                book=book,
                borrow_date=borrow_date,
                return_date=return_date
            )
            self.stdout.write(f'Created borrow record: {member.name} borrowed {book.title}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
