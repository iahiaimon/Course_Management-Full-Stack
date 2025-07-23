from rest_framework.serializers import ModelSerializer ,CharField , ValidationError
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    confirm_password = CharField(write_only=True, required=True)  # Add confirm_password

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone', 'role', 'password', 'confirm_password', 'address', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {
            'email': {'required': True}  # Ensure email is required
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError({"confirm_password": "Passwords must match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],  # Remove default
            phone=validated_data.get('phone', ''),
            role=validated_data.get('role', CustomUser.Role.STUDENT),  # Use enum
            address=validated_data.get('address', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.role = validated_data.get('role', instance.role)
        instance.address = validated_data.get('address', instance.address)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance  # Fix typo (was 'user')