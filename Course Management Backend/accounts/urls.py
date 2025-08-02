from django.urls import path
from .views import(
    AllUserView,
    UserRegistrationView,
    UserLoginView,
    UserAccountView
)

urlpatterns = [
    path("users/" , AllUserView.as_view() , name = "users"),
    path("register/" , UserRegistrationView.as_view() , name = "register"),
    path("login/" , UserLoginView.as_view() , name = "login"),
    path('account/', UserAccountView.as_view(), name='account'),
]