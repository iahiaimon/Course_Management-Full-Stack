from django.urls import path

from .views import(
    EnrollmentView,
)

urlpatterns = [
    path('enrollment/', EnrollmentView.as_view(), name='enrollment'),
]