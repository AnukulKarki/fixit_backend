from django.urls import path
from .views import ProposalAppliedWorkerView, ProposalApplyView
urlpatterns = [
    path('apply/<int:id>/',  ProposalApplyView.as_view() ), 
    path('list/<int:id>/',  ProposalAppliedWorkerView.as_view() ), 
]