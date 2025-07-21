from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from datetime import timedelta
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from .models import Customer
from rest_framework.permissions import AllowAny
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

@method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True), name='post')
class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access = response.data.get("access")
            refresh = response.data.get("refresh")

            response.set_cookie(
                key="access_token",
                value=access,
                httponly=True,
                secure=True,  # Only for HTTPS
                samesite="Lax",  # Or 'Strict' depending on your needs
                max_age=60 * 30,  # 30 minutes
                path="/"
            )

            response.set_cookie(
                key="refresh_token",
                value=refresh,
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=60 * 60 * 24,  # 1 day
                path="/api/auth/token/refresh/"
            )

            # Remove tokens from response body (optional, for security)
            response.data.pop("access")
            response.data.pop("refresh")

        return response
    

class CookieTokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"detail": "Refresh token missing."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            response = Response({"detail": "Access token refreshed."}, status=status.HTTP_200_OK)

            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=30 * 60,
                path="/"
            )
            return response

        except Exception as e:
            return Response({"detail": "Invalid or expired refresh token."}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            response = Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)
            response.delete_cookie("access_token")
            response.delete_cookie("refresh_token")
            return response

        except Exception as e:
            return Response({"detail": "Invalid token or already logged out."}, status=status.HTTP_400_BAD_REQUEST)


class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'detail': 'Account activated successfully.'}, status=200)
        else:
            return Response({'detail': 'Activation link is invalid!'}, status=400)



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)