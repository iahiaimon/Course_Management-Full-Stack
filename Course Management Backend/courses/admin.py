from django.contrib import admin
from .models.category import Category
from .models.course import Course
# Register your models here.

admin.site.register(Category , Course)
