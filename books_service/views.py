from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from books_service.models import Book
from books_service.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (JWTAuthentication,)

    def get_permissions(self):
        self.permission_classes = [IsAdminUser, ]
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        return super().get_permissions()
