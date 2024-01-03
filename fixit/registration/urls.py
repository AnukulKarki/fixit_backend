from django.urls import path
from .views import RegistrationUser, RegistrationWorker
urlpatterns = [
    path('userRegistration/', RegistrationUser.as_view() ),
    path('workerRegistration/', RegistrationWorker.as_view() ),
]