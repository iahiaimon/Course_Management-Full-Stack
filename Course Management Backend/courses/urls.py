from django.urls import path
from .views import(
    CategoryView,
    CourseView
)


urlpatterns = [
    path('category/' , CategoryView.as_view() , name="category"),
    path('course/' , CourseView.as_view() , name="course")
]