from django.urls import path
from .views import RegistrationUser,  loginUser, profileView, LogoutView, UserCheck
urlpatterns = [
    path('register/', RegistrationUser.as_view() ),
    path('login/', loginUser.as_view()),
    path('profile/', profileView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user-check/', UserCheck.as_view())
]