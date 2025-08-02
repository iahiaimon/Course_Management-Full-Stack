from django.shortcuts import render
from .models import Enrollment
from .serializers import EnrollmentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

# Create your views here.


class EnrollmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            enrollment = serializer.save()
            return Response (
                {
                    "message" : "You Enrolled the course successfully",
                    "enrollment" : {
                        "student" : enrollment.student.username,
                        "course" : enrollment.course.title,
                        "enrollment_date" : enrollment.enrollment_date,
                        "status" : enrollment.status
                    },
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
