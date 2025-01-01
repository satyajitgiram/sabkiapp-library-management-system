from django_filters import rest_framework as filters
from .models import Book, Member, BorrowRecord

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(lookup_expr='iexact')
    published_date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'published_date']

class MemberFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    membership_status = filters.ChoiceFilter(choices=Member.MembershipStatus.choices)
    membership_date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = Member
        fields = ['name', 'email', 'membership_status', 'membership_date']

class BorrowRecordFilter(filters.FilterSet):
    book = filters.ModelChoiceFilter(queryset=Book.objects.all())
    member = filters.ModelChoiceFilter(queryset=Member.objects.all())
    borrow_date = filters.DateFromToRangeFilter()
    return_date = filters.DateFromToRangeFilter()
    is_returned = filters.BooleanFilter(field_name='return_date', lookup_expr='isnull', exclude=True)
    
    class Meta:
        model = BorrowRecord
        fields = ['book', 'member', 'borrow_date', 'return_date', 'is_returned']
