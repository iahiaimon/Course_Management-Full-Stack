from django.urls import path
from .views import(
    AllUserView,
    UserRegistrationView,
    UserLoginView,
)

urlpatterns = [
    path("registration/" , UserRegistrationView.as_view() , name = "registration"),
    path("users/" , AllUserView.as_view() , name = "users"),
    path("login/" , UserLoginView.as_view() , name = "login"),
]