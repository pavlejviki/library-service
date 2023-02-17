import datetime

from borrowings_service.models import Borrowing
from telegram_notifier import send_message


def find_overdue_borrowings():
    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(days=1)

    overdue_borrowings = Borrowing.objects.filter(
        expected_return_date__lte=tomorrow, actual_return_date__isnull=True
    )
    if not overdue_borrowings:
        message = "No borrowings overdue today!"
        send_message(message)
    else:
        for borrowing in overdue_borrowings:
            user = borrowing.user_id
            message = (
                f"A book is overdue!\n"
                f"Title: {borrowing.book_id.title}\n"
                f"Author: {borrowing.book_id.author}\n"
                f"Borrowed by: {user.username}\n"
                f"Expected return date: {borrowing.expected_return_date}\n"
            )
            send_message(message)
