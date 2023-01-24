from django.core.exceptions import ValidationError
from django.db import models, transaction

from books_service.models import Book
from library_service.settings import AUTH_USER_MODEL


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def clean(self):
        if self.expected_return_date <= self.borrow_date:
            raise ValidationError(
                "Expected return date must be later than the borrow date."
            )
        if self.actual_return_date and self.actual_return_date <= self.borrow_date:
            raise ValidationError(
                "Actual return date must be later than the borrow date."
            )

    def validate_return_date(self):
        if self.actual_return_date and self.pk:
            raise ValidationError("Borrowing can be returned only once.")

    def manage_book_inventory(self, *args, **kwargs):
        with transaction.atomic():
            book = self.book_id
            if not self.pk:
                if book.inventory < 1:
                    raise ValidationError("This book is not available for borrowing.")
                book.inventory -= 1
                book.save()
            elif self.actual_return_date:
                book.inventory += 1
                book.save()
            super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        self.validate_return_date()
        self.manage_book_inventory(*args, *kwargs)

    def __str__(self):
        return f"Borrowing of book {self.book_id.title} by user {self.user_id}"
