from rest_framework.serializers import ModelSerializer ,CharField , ValidationError
from .models import Enrollment

class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrollment_date' , "status" , "is_active" ,"created_at" , "updated_at"]
        read_only_fields = ['id', 'created_at', 'updated_at']