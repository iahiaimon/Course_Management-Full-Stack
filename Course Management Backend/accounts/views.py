from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework import generics

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .serializers import CustomTokenObtainPairSerializer

# Create your views here.


# class AllUserView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = CustomUserSerializer(users, many=True)
#         return Response(serializer.data)



class AllUserView(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Set this to IsAdminUser if only admins allowed

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=user.id)  # Show only their own profile

    def perform_create(self, serializer):
        if self.request.user.role == "admin":
            serializer.save()
        # else:
        #     raise PermissionDenied("Only admins can create new users.")


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User created successfully",
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "role": user.role,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response(
#                 {
#                     "message": "User logged in successfully",
#                     "token": token.key,
#                     "user": {
#                         "username": user.username,
#                         "email": user.email,
#                         "role": user.role,
#                     },
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         return Response(
#             {"message": "Invalid Username or Password"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )


class UserAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        return request.user

    def get(self, request):
        user = self.get_object(request)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = self.get_object(request)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Account updated successfully", "user": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = self.get_object(request)
        user.delete()
        return Response(
            {"message": "Account deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer