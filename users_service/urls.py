from django.contrib import admin
from django.urls import path, include

from users_service.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
]

app_name = "users_service"
