from django.contrib import admin
from .models.category import Category
from .models.course import Course
from .models.lesson import Lesson , LessonMaterial
# Register your models here.

admin.site.register(Category)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description' , 'price', 'duration', 'category', 'is_active')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course', 'is_active')

@admin.register(LessonMaterial)
class LessonMaterialAdmin(admin.ModelAdmin):
    list_display = ("lesson_material" , "lesson" , "is_active")