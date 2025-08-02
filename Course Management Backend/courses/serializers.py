from rest_framework.serializers import ModelSerializer

from .models.category import Category
from .models.course import Course
from .models.lesson import Lesson , LessonMaterial

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "description" , "is_active","created_at" , "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id", "title", "description", "banner",
            "price", "duration", "category",
            "is_active", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

class LessonMaterialSerializer(ModelSerializer):
    class Meta:
        model = LessonMaterial
        fields = ["id" , "lesson_material" , "lesson", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        

class LessonSerializer(ModelSerializer):
    lesson_materials = LessonMaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ["id" , "title" , "description" , "course" ,"lesson_materials" , "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]