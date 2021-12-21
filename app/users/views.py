import json

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer


class LoginView(APIView):
    """Logs user in and returns token"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        POST endpoint that accepts a username and password, returns the
        session id cookie on success
        """
        # read login info
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        # check that credentials aren't empty
        if username is None or password is None:
            return Response({"info": "Username and Password is needed"},
                            status=status.HTTP_401_UNAUTHORIZED)

        # attempt login using credentials
        user = authenticate(username=username, password=password)

        # check if authentication was successful
        if user is None:
            return Response({"info": "User does not exist"},
                            status=status.HTTP_401_UNAUTHORIZED)

        # complete login, creates session id cookie if none supplied
        login(request, user)

        # responds with user info and session id cookie
        return Response({"user": UserSerializer(user,
                                                context=self.
                                                get_serializer_context()).
                        data})


class LogoutView(APIView):
    """Logs user out and ends session"""

    def post(self, request, *args, **kwargs):
        """
        POST endpoint that ends the current session
        """
        logout(request)
        response = Response(status=status.HTTP_200_OK)
        return response


class RegisterView(APIView):
    """User Registration API"""
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        POST request that takes in: email, password, first_name, and last_name
        """
        # grab the data before its serialized
        data = json.loads(request.body)
        username = data.get('email')
        password = data.get('password')

        # create the user in the db
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # authenticates the user after creation
        user = authenticate(username=username, password=password)

        # logs the user in and assigns a sessionID
        login(request, user)

        # responds with a HTTP 201 created and the user details.
        return \
            Response(
                {'user': UserSerializer(user,
                                        context=self.
                                        get_serializer_context()).data},
                status=status.HTTP_201_CREATED)


class IsLoggedInView(APIView):
    """API Endpoint to check if session is active"""

    def get(self, request):
        """
        Validates that a user has a valid sessionid
        """
        # if the user is not found/authenticated (invalid session id)
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response({'message': 'valid'}, status=status.HTTP_200_OK)
