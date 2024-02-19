from django.urls import path
from .views import GigPostView, GigListView, GigDeleteView, GigEditView
urlpatterns = [
    path('post/', GigPostView.as_view()),
    path('list/', GigListView.as_view()),
    path('delete/<int:id>/', GigDeleteView.as_view()),
    path('edit/<int:id>/', GigEditView.as_view()),
]