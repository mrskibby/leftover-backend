from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from users.models import Customer


User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "is_active", "dob", "address"]
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         user = User(**validated_data)
#         user.is_active = False  # Mark inactive until email confirmation
#         if password:
#             user.set_password(password)
#         user.save()

#         # Avoid duplicate Customer creation
        
#         if not hasattr(user, 'customer_profile'):
#             Customer.objects.create(user=user)

#         # Activation email
#         # uid = urlsafe_base64_encode(force_bytes(user.pk))
#         # token = default_token_generator.make_token(user)
#         # activation_link = f"http://127.0.0.1:8000/api/auth/activate/{uid}/{token}/"

#         # send_mail(
#         #     subject="Activate your Leftovers account",
#         #     message=f"Hi {user.username},\n\nClick the link to activate your account:\n{activation_link}",
#         #     from_email="noreply@leftovers.com",
#         #     recipient_list=[user.email],
#         #     fail_silently=False,
#         # )

#         return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active", "dob", "address", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        # ✅ Ensure Customer profile is created
        from users.models import Customer
        Customer.objects.get_or_create(user=user)

        return user
