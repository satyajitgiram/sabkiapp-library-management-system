from django.db import models
from django.core.validators import MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    published_date = models.DateField(null=False)
    category = models.CharField(max_length=100, null=False)
    available_copies = models.IntegerField(
        null=False,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
            models.Index(fields=['category']),
        ]
        ordering = ['title', 'id']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member(models.Model):
    class MembershipStatus(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        INACTIVE = 'Inactive', 'Inactive'

    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True, null=False)
    membership_date = models.DateField(null=False)
    membership_status = models.CharField(
        max_length=10,
        choices=MembershipStatus.choices,
        default=MembershipStatus.ACTIVE
    )

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['membership_status']),
        ]
        ordering = ['name', 'id']

    def __str__(self):
        return f"{self.name} ({self.email})"


class BorrowRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=False)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['borrow_date']),
            models.Index(fields=['return_date']),
        ]
        ordering = ['-borrow_date', 'id']

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
