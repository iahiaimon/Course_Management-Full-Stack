from rest_framework.serializers import ModelSerializer

from .models.category import Category
from .models.course import Course
from .models.lesson import Lesson

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "description" , "is_active","created_at" , "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id" , "title" , "description" , "banner" , "price" , "is_active","created_at" , "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"] 