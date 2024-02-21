from django.urls import path
from .views import GigPostView, GigListView, GigDeleteView, GigEditView, GigDetailView
urlpatterns = [
    path('post/', GigPostView.as_view()),
    path('list/', GigListView.as_view()),
    path('delete/<int:id>/', GigDeleteView.as_view()),
    path('edit/<int:id>/', GigEditView.as_view()),
    path('detail/<int:id>/', GigDetailView.as_view()),
]