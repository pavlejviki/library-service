from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books_service.serializers import BookSerializer
from borrowings_service.models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id",
        )


class BorrowingReadSerializer(BorrowingSerializer):
    book_id = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id",
        )


class BorrowingCreateSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
        )

    def create(self, validated_data):
        with transaction.atomic():
            book = validated_data.pop("book_id")
            id_ = validated_data.pop("id")
            actual_return_date = validated_data.pop("actual_return_date")
            if not id_:
                if book.inventory == 0:
                    raise ValidationError("This book is not available for borrowing.")
                book.inventory -= 1
                book.save()
            elif actual_return_date:
                book.inventory += 1
                book.save()
            Borrowing.objects.create(**validated_data)

