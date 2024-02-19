from django.urls import path
from .views import GigPostView, GigListView
urlpatterns = [
    path('post/', GigPostView.as_view()),
    path('list/', GigListView.as_view()),
]