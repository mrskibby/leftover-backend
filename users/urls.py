from django.urls import path
from .views import RegisterView, CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='cookie_token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
