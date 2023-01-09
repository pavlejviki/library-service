from django.contrib import admin
from django.urls import path, include

from users_service.views import CreateUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "users_service"
