from django.db import models
from core.models.basemodel import BaseModel

from courses.models.course import Course
from accounts.models import CustomUser

class Lesson(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return f"{self.title} -- {self.course.title}"
    

class LessonMaterial(BaseModel):
    lesson_material = models.FileField(
        upload_to="Lesson_Material/",
        blank=True,
        null=True,        
        default=None
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_materials"
    )

    def __str__(self):
        return self.lesson_material.name if self.lesson_material else "No Material"
