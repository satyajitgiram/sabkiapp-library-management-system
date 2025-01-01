from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from .models import Book, Member, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 
                   'available_copies', 'total_times_borrowed')
    list_filter = ('category', 'available_copies')
    search_fields = ('title', 'author', 'category')
    ordering = ('title', 'author')
    date_hierarchy = 'published_date'
    list_per_page = 20

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            times_borrowed=Count('borrowrecord')
        )
        return queryset

    def total_times_borrowed(self, obj):
        return obj.times_borrowed
    total_times_borrowed.admin_order_field = 'times_borrowed'
    total_times_borrowed.short_description = 'Times Borrowed'

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'membership_date', 'membership_status',
                   'active_borrows', 'total_borrows')
    list_filter = ('membership_status', 'membership_date')
    search_fields = ('name', 'email')
    ordering = ('name',)
    date_hierarchy = 'membership_date'
    list_per_page = 20

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            total_borrow_count=Count('borrowrecord'),
            active_borrow_count=Count('borrowrecord',
                                    filter=models.Q(borrowrecord__return_date=None))
        )
        return queryset

    def active_borrows(self, obj):
        return obj.active_borrow_count
    active_borrows.admin_order_field = 'active_borrow_count'
    active_borrows.short_description = 'Active Borrows'

    def total_borrows(self, obj):
        return obj.total_borrow_count
    total_borrows.admin_order_field = 'total_borrow_count'
    total_borrows.short_description = 'Total Borrows'

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title', 'member_name', 'borrow_date',
                   'return_date', 'status_badge', 'borrow_duration')
    list_filter = (
        ('return_date', admin.EmptyFieldListFilter),
        'borrow_date',
        'book__category'
    )
    search_fields = (
        'book__title',
        'member__name',
        'member__email'
    )
    ordering = ('-borrow_date',)
    date_hierarchy = 'borrow_date'
    list_per_page = 20
    raw_id_fields = ('book', 'member')

    def book_title(self, obj):
        return obj.book.title
    book_title.admin_order_field = 'book__title'
    book_title.short_description = 'Book'

    def member_name(self, obj):
        return obj.member.name
    member_name.admin_order_field = 'member__name'
    member_name.short_description = 'Member'

    def status_badge(self, obj):
        if obj.return_date:
            return format_html(
                '<span style="background-color: #28a745; color: white; padding: 3px 10px; '
                'border-radius: 10px;">Returned</span>'
            )
        return format_html(
            '<span style="background-color: #ffc107; color: black; padding: 3px 10px; '
                'border-radius: 10px;">Borrowed</span>'
        )
    status_badge.short_description = 'Status'

    def borrow_duration(self, obj):
        if obj.return_date:
            duration = obj.return_date - obj.borrow_date
            return f"{duration.days} days"
        return "Ongoing"
    borrow_duration.short_description = 'Duration'

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term)
        
        try:
            from datetime import datetime
            date_obj = datetime.strptime(search_term, '%Y-%m-%d')
            queryset |= self.model.objects.filter(
                models.Q(borrow_date=date_obj) |
                models.Q(return_date=date_obj)
            )
        except ValueError:
            pass
        
        return queryset, use_distinct
