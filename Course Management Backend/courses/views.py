from django.shortcuts import render
from django.http import HttpResponse
from .models.category import Category
from .models.course import Course
from .serializers import CategorySerializer, CourseSerializer


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
                        "is_active": category.is_active
                        },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
