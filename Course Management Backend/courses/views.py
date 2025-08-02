from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models.category import Category
from .models.course import Course
from .models.lesson import Lesson, LessonMaterial
from .serializers import (
    CategorySerializer,
    CourseSerializer,
    LessonSerializer,
    LessonMaterialSerializer,
)


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


class CategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True).data
        return Response(serializer)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(
                {
                    "message": "A new category created Successfully",
                    "category": {
                        "title": category.title,
                        "is_active": category.is_active,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            return Response(
                {
                    "message": "Category updated successfully",
                    "category": CategorySerializer(category).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(
            {"message": "Category deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class CourseView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True).data
        return Response(serializer)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(
                {
                    "message": "A new course created Successfully",
                    "course": {
                        "title": course.title,
                        "description": course.description,
                        "price": course.price,
                        "duration": course.duration,
                        "category": course.category.id,
                        "is_active": course.is_active,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            course = serializer.save()
            return Response(
                {
                    "message": "Course updated successfully",
                    "course": {
                        "title": course.title,
                        "description": course.description,
                        "price": course.price,
                        "duration": course.duration,
                        "category": course.category.id,
                        "is_active": course.is_active,
                    },
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(
            {"message": "Course deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class LessonView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(
            {"message": "All Lessons with Materials", "lessons": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        materials = request.FILES.getlist("lesson_materials")

        lesson_serializer = LessonSerializer(data=request.data)
        if lesson_serializer.is_valid():
            lesson = lesson_serializer.save()

            for material in materials:
                LessonMaterial.objects.create(lesson=lesson, lesson_material=material)

            return Response(
                {
                    "message": "Lesson created successfully with materials",
                    "lesson": LessonSerializer(lesson).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(lesson_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        materials = request.FILES.getlist("lesson_materials")

        serializer = LessonSerializer(lesson, data=request.data, partial=True)
        if serializer.is_valid():
            lesson = serializer.save()

            # Optionally clear existing materials before adding new ones
            # LessonMaterial.objects.filter(lesson=lesson).delete()

            for material in materials:
                LessonMaterial.objects.create(lesson=lesson, lesson_material=material)

            return Response(
                {
                    "message": "Lesson updated successfully",
                    "lesson": LessonSerializer(lesson).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        lesson.delete()
        return Response(
            {"message": "Lesson deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
