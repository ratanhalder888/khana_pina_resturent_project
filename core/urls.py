from django.urls import path
from core.views import home, menu, tracking, reservation, contact
urlpatterns = [
    path('', home, name='home'),
    path("menu/", menu, name="menu"),
    path("order-track/", tracking, name="track"),
    path("reservation/", reservation, name="reservation"),
    path("contact/", contact, name="contact"),
]