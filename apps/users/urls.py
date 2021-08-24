from . import views
from django.urls import path

urlpatterns = [
    path("login/", views.UserFormView.as_view(), name="user-login-form"),
]
