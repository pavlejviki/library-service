from celery import shared_task
from utils.borrowing_helper import find_overdue_borrowings


@shared_task
def daily_overdue_borrowings_check() -> int:
    find_overdue_borrowings()
