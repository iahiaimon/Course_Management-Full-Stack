from django.db import models
from core.models.basemodel import BaseModel

class Category(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title

