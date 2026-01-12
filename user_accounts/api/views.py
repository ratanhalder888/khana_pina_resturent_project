from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from user_accounts.api.serializers import (
    JWTCheckBlacklistSerializer,
)


class JWTCheckBlacklistAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = JWTCheckBlacklistSerializer

    def post(self, request):
        serializer = JWTCheckBlacklistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                refresh_token = serializer.validated_data["refresh"]
                token = RefreshToken(refresh_token)
                token.check_blacklist()
                return Response({"token": "The Token is not Blacklisted!"})
            except TokenError:
                return Response(
                    {"token": "The Token is Blacklisted!"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(serializer.errors)


