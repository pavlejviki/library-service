from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from borrowings_service.models import Borrowing
from borrowings_service.serializers import (
    BorrowingSerializer,
    BorrowingReadSerializer,
    BorrowingCreateSerializer,
)

from utils.telegram_notifier import send_message


class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Borrowing.objects.prefetch_related("user_id", "book_id")
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset

        if not self.request.user.is_staff:
            queryset = Borrowing.objects.filter(user_id=self.request.user)

        is_active = self.request.query_params.get("is_active")
        user_id = self.request.query_params.get("user_id")

        if is_active:
            queryset = queryset.filter(actual_return_date__isnull=True)

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return BorrowingReadSerializer

        if self.action == "create" or self.action == "update":
            return BorrowingCreateSerializer

        return BorrowingSerializer

    def perform_create(self, serializer):
        user = self.request.user
        borrowing = serializer.save(user_id=user)
        message = (
            f"Borrowing created successfully on {borrowing.borrow_date} "
            f'for book "{borrowing.book_id.title}"'
            f' with expected return date "{borrowing.expected_return_date}" for user {user.first_name} {user.last_name}'
        )
        send_message(message)
