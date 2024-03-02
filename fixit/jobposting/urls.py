from django.urls import path
from .views import JobRequirementPostView, JobRequirementEditView, JobRequirementDeleteView, JobRequirementDetailView, JobRequirementListView, JobRequirementListViewUser, JobRequirementUserDetailView
urlpatterns = [
    path('post/',  JobRequirementPostView.as_view() ), #Post
    path('edit/<int:id>/', JobRequirementEditView.as_view() ), #edit the job requirement
    path('delete/<int:id>/', JobRequirementDeleteView.as_view() ), # delete the job requriement by the users
    path('detail/<int:id>/', JobRequirementDetailView.as_view() ), # can watch the details of every job requirements
    path('user/detail/<int:id>/', JobRequirementUserDetailView.as_view() ), #can only watch the detais of the job requirement of logged in user
    path('list-all/', JobRequirementListView.as_view() ), # list all the job req
    path('user/list/', JobRequirementListViewUser.as_view() ), #list the job req that is posted by the user only
]