from django.urls import path
from .views import jobPostView
urlpatterns = [
    path('job-post/', jobPostView.as_view() )
]