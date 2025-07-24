from django.contrib import admin
from .models.category import Category
from .models.course import Course
# Register your models here.

admin.site.register(Category)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description' , 'price', 'duration', 'category', 'is_active')