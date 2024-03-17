from django.urls import path
from .views import BrandItemPostView, BrandPostView
urlpatterns = [
    path('post/',  BrandPostView.as_view() ),
    path('item/post/',  BrandItemPostView.as_view() ),
]