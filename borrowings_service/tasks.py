from borrowings_service.models import Borrowing

from celery import shared_task


@shared_task
def count_borrowings() -> int:
    return Borrowing.objects.count()


