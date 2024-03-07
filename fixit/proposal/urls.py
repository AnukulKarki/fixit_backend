from django.urls import path
from .views import ProposalAppliedWorkerView, ProposalApplyView
from workerhire.views import WorkerHire
urlpatterns = [
    path('apply/<int:id>/',  ProposalApplyView.as_view() ), 
    path('list/<int:id>/',  ProposalAppliedWorkerView.as_view() ), 
    path('hire/<int:id>/<int:jobid>/',  WorkerHire.as_view() ), 
]