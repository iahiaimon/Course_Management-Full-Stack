from rest_framework.serializers import ModelSerializer

from .models.category import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "description" , "is_active","created_at" , "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        