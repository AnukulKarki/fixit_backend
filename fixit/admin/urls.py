from django.urls import path
from .views import AdminRegister, AdminLogin
#api/admin/
urlpatterns = [
    path('register/',  AdminRegister.as_view()),
    path('login/',  AdminLogin.as_view()),
]