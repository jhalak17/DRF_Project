from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer

# Create your views here.
class UserRegistration(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Success'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email = email, password =password)   # returns a User object if the credentials are valid
            if user:
                return Response({'msg':'Registration Success'}, status=status.HTTP_200_OK)     
        return Response({'errors':{'non_field_error':['Email or password not present']}}, status=status.HTTP_400_BAD_REQUEST)   


