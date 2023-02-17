from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from books_service.models import Book
from books_service.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):

        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super().get_permissions()
