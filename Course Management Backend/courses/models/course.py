from django.db import models
from core.models.basemodel import BaseModel
from .category import Category


class Course(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    banner = models.ImageField(upload_to="Course/" , blank=True , null=True , default="Course/Default_Course.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DecimalField(max_digits=5 , decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} -- {self.category}"
