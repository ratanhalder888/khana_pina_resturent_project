from django.contrib.auth.models import User
from djoser.serializers import UserSerializer
from rest_framework import serializers


class JWTCheckBlacklistSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class CustomUserSerializer(UserSerializer):
    # must_change_password = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ("password", "is_staff", "is_superuser", "user_permissions", "groups")
        read_only_fields = ("username",)

    def get_must_change_password(self, obj) -> bool:
        profile = getattr(obj, "accountprofile", None)
        if profile:
            return profile.must_change_password
        return False
