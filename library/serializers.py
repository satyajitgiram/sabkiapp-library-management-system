from rest_framework import serializers
from .models import Book, Member, BorrowRecord

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'category', 'available_copies']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'membership_date', 'membership_status']

class BorrowRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    member_name = serializers.CharField(source='member.name', read_only=True)
    
    class Meta:
        model = BorrowRecord
        fields = ['id', 'member', 'book', 'book_title', 'member_name', 'borrow_date', 'return_date']
        read_only_fields = ['book_title', 'member_name']
