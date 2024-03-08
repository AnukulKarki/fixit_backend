from django.urls import path
from .views import CategoryListView
urlpatterns = [
    path('list/',  CategoryListView.as_view() ),
]