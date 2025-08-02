from django.urls import path
from .views import(
    CategoryView,
    CategoryDetailView,
    CourseView,
    CourseDetailView,
    LessonView,
    LessonDetailView
)


urlpatterns = [
    path('category/' , CategoryView.as_view() , name="category"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-update-delete'),
    path('course/' , CourseView.as_view() , name="course"),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-update-delete'),
    path('lesson/' , LessonView.as_view() , name="lesson"),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-update-delete'),
]