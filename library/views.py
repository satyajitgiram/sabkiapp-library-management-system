from rest_framework import viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, Member, BorrowRecord
from .serializers import BookSerializer, MemberSerializer, BorrowRecordSerializer
from .filters import BookFilter, MemberFilter, BorrowRecordFilter
from datetime import date
import logging

logger = logging.getLogger('library')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating new book: {request.data.get('title')}")
        response = super().create(request, *args, **kwargs)
        logger.info(f"Book created successfully with id: {response.data.get('id')}")
        return response

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filterset_class = MemberFilter
    pagination_class = pagination.PageNumberPagination

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating new member: {request.data.get('name')}")
        response = super().create(request, *args, **kwargs)
        logger.info(f"Member created successfully with id: {response.data.get('id')}")
        return response

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    filterset_class = BorrowRecordFilter

    @action(detail=False, methods=['post'])
    def borrow_book(self, request):
        book_id = request.data.get('book_id')
        member_id = request.data.get('member_id')

        logger.info(f"Attempting to borrow book {book_id} for member {member_id}")
        
        try:
            book = Book.objects.get(id=book_id)
            member = Member.objects.get(id=member_id)

            if book.available_copies <= 0:
                logger.warning(f"Book {book.title} has no available copies")
                return Response(
                    {'error': 'No copies available'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if member.membership_status != 'Active':
                logger.warning(f"Member {member.name} is not active")
                return Response(
                    {'error': 'Member is not active'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            borrow_record = BorrowRecord.objects.create(
                book=book,
                member=member,
                borrow_date=date.today()
            )

            book.available_copies -= 1
            book.save()

            logger.info(f"Book {book.title} borrowed successfully by {member.name}")
            return Response(
                BorrowRecordSerializer(borrow_record).data,
                status=status.HTTP_201_CREATED
            )

        except (Book.DoesNotExist, Member.DoesNotExist) as e:
            logger.error(f"Book or Member not found: {str(e)}")
            return Response(
                {'error': 'Book or Member not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error in borrow_book: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'])
    def return_book(self, request):
        borrow_record_id = request.data.get('borrow_record_id')
        logger.info(f"Attempting to return book for borrow record {borrow_record_id}")
        
        try:
            borrow_record = BorrowRecord.objects.get(id=borrow_record_id, return_date=None)
            book = borrow_record.book

            borrow_record.return_date = date.today()
            borrow_record.save()

            book.available_copies += 1
            book.save()

            logger.info(f"Book {book.title} returned successfully")
            return Response(
                BorrowRecordSerializer(borrow_record).data,
                status=status.HTTP_200_OK
            )

        except BorrowRecord.DoesNotExist:
            logger.warning(f"Active borrow record not found for id {borrow_record_id}")
            return Response(
                {'error': 'Active borrow record not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error in return_book: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
