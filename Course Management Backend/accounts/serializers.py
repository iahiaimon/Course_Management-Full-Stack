from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from .models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    confirm_password = CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "role",
            "password",
            "confirm_password",
            "address",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "is_active", "created_at", "updated_at"]
        extra_kwargs = {"email": {"required": True}, "password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise ValidationError({"confirm_password": "Passwords must match."})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = CustomUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            phone=validated_data.get("phone", ""),
            role=validated_data.get("role", CustomUser.Role.STUDENT),
            address=validated_data.get("address", ""),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.role = validated_data.get("role", instance.role)
        instance.address = validated_data.get("address", instance.address)
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        token["role"] = user.role  # 👈 Ensure role is included

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add user info in the response too (optional)
        data["user"] = {
            "username": self.user.username,
            "email": self.user.email,
            "role": self.user.role,
        }

        return data
