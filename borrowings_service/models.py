from django.contrib.auth import get_user_model
from django.db import models

from books_service.models import Book
from library_service.settings import AUTH_USER_MODEL


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Borrowing of book {self.book_id.title} by user {self.user_id}'
