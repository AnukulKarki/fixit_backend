from django.urls import path
from .views import JobRequirementPostView, JobRequirementEditView, JobRequirementDeleteView, JobRequirementDetailView, JobRequirementListView, JobRequirementListViewUser
urlpatterns = [
    path('post/',  JobRequirementPostView.as_view() ),
    path('edit/<int:id>/', JobRequirementEditView.as_view() ),
    path('delete/<int:id>/', JobRequirementDeleteView.as_view() ),
    path('detail/<int:id>/', JobRequirementDetailView.as_view() ),
    path('list/', JobRequirementListView.as_view() ),
    path('user/list/', JobRequirementListViewUser.as_view() )
]