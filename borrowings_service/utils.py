import datetime

from borrowings_service.models import Borrowing


def find_overdue_borrowings():
    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(days=1)

    overdue_borrowings = Borrowing.objects.filter(
        expected_return_date__lte=tomorrow,
        actual_return_date__isnull=True
    )

    for borrowing in overdue_borrowings:
        book = borrowing.book_id
        user = borrowing.user_id

        message = (
            f"A book is overdue!\n"
            f"Title: {book.title}\n"
            f"Author: {book.author}\n"
            f"Borrowed by: {user.username}\n"
            f"Expected return date: {borrowing.expected_return_date}\n"
        )