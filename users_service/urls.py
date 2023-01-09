from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
]

app_name = "users_service"
