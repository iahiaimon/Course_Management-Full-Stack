from django.db import models
from accounts.models import CustomUser
from courses.models.course import Course
from core.models.basemodel import BaseModel
from django.utils import timezone

# Create your models here.


class Enrollment(BaseModel):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.PENDING,
    )

    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (
            f"{self.student.username} enrolled in {self.course.title} ({self.status})"
        )
