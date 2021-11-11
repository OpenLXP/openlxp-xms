from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Register a new user
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """
    Login a user
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Login a user
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # respond with the user data and add a token to the header response

            return Response({"email": serializer.data['email'],
                             "token": "SOME_TOKEN",
                             }, status=status.HTTP_200_OK,
                            headers={"Authorization": "Token " + serializer.data["email"]})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
