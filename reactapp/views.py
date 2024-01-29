# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from allauth.account.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets
from apps.models import Project





from .serializers import UserSerializer
from .serializers import ProjectSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
class UserLoginView(LoginView):
    def get_response(self):
        user_serializer = UserSerializer(self.user)
        data = {'user': user_serializer.data}
        return Response(data)
