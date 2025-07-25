from django.urls import path
from .views import(
    CategoryView,
    CourseView,
    LessonView
)


urlpatterns = [
    path('category/' , CategoryView.as_view() , name="category"),
    path('course/' , CourseView.as_view() , name="course"),
    path('lesson/' , LessonView.as_view() , name="lesson"),
]