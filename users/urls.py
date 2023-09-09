from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [

    path('tokens/', TokenObtainPairView.as_view(), name='token_obtain_pairs'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("createuser/", UserCreateAPIView.as_view(), name="createuser"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
