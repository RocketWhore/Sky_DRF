from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from users.models import User
from users.serializers import MyTokenObtainPairSerializer


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')


class LoginModifiedView(LoginView):
    model = User
    form_class = UserLoginForm


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
