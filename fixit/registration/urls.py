from django.urls import path
from .views import RegistrationUser
urlpatterns = [
    path('registration/', RegistrationUser.as_view() ),
]