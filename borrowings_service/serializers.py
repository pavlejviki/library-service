from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from books_service.serializers import BookSerializer
from borrowings_service.models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticated,)

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
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
        )

    def validate(self, data):
        if data["expected_return_date"] < data["borrow_date"]:
            raise serializers.ValidationError(
                "Expected return date must be later than the borrow date."
            )
        if (
            data["actual_return_date"]
            and data["actual_return_date"] < data["borrow_date"]
        ):
            raise serializers.ValidationError(
                "Actual return date must be later than the borrow date."
            )
        return data

    @staticmethod
    def decrease_book_inventory(book):
        if book.inventory == 0:
            raise ValidationError("This book is not available for borrowing.")
        book.inventory -= 1
        book.save()

    @staticmethod
    def increase_book_inventory(book, actual_return_date):
        if actual_return_date:
            book.inventory += 1
            book.save()

    def create(self, validated_data):
        with transaction.atomic():
            book = validated_data.get("book_id")
            self.decrease_book_inventory(book)
            borrowing = Borrowing.objects.create(**validated_data)
            return borrowing

    def update(self, instance, validated_data):
        with transaction.atomic():
            book = validated_data.get("book_id", instance.book_id)
            if instance.actual_return_date:
                raise ValidationError("Borrowing can be returned only once.")
            actual_return_date = validated_data.get("actual_return_date")
            self.increase_book_inventory(book, actual_return_date)
            instance.actual_return_date = validated_data.get(
                "actual_return_date", instance.actual_return_date
            )
            instance.save()
            return instance
