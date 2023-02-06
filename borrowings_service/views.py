from django.shortcuts import render
from rest_framework import mixins, viewsets

from borrowings_service.models import Borrowing
from borrowings_service.serializers import BorrowingSerializer, BorrowingReadSerializer, BorrowingCreateSerializer


class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Borrowing.objects.prefetch_related("user_id", "book_id")
    serializer_class = BorrowingSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return BorrowingReadSerializer

        if self.action == "put" or self.action == "patch":
            return BorrowingCreateSerializer

        return BorrowingSerializer
