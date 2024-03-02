from django.urls import path
from .views import RegistrationUser, RegistrationWorker, loginWorker, loginUser, profileView, LogoutView, UserCheck
urlpatterns = [
    path('user-register/', RegistrationUser.as_view() ),
    path('worker-register/', RegistrationWorker.as_view() ),
    path('user-login/', loginUser.as_view()),
    path('worker-login/',loginWorker.as_view()),
    path('profile/', profileView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user-check/', UserCheck.as_view())
]