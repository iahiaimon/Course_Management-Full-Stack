from django.contrib import admin
from .models import Enrollment
# Register your models here.

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date' , 'status')