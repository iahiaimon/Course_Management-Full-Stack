from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models.basemodel import BaseModel


class CustomUser(BaseModel , AbstractUser):
    email = models.EmailField(unique=True, error_messages={"unique": "Email already exists"})
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        Teacher = "teacher", "Teacher"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.username}--{self.role}"
