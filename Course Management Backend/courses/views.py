from django.shortcuts import render
from django.http import HttpResponse
from .models.category import Category
from .serializers import CategorySerializer

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
        return Response(
            {
                "message": "All Category List",
                "serializer": {
                    "title": categories.title,
                    "is_active": categories.is_active,
                },
            },
            status=status.HTTP_201_CREATED,
        )

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "A new category created Successfully",
                    "serializer": {"title": serializer.title},
                },
                status=status.HTTP_201_CREATED,
            )
