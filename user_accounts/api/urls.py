from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
)

from user_accounts.api.views import (
    JWTCheckBlacklistAPIView,
)

urlpatterns = [
    path("refresh/blacklist/", TokenBlacklistView.as_view(), name="blacklist-refresh"),
    path(
        "refresh/blacklist/check/",
        JWTCheckBlacklistAPIView.as_view(),
        name="blacklist-check",
    ),
    
]
