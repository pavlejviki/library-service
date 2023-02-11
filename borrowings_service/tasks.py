from celery import shared_task
from utils import find_overdue_borrowings

from borrowings_service.models import Borrowing


@shared_task
def daily_overdue_borrowings_check() -> int:
    find_overdue_borrowings()
