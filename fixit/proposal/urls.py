from django.urls import path
from .views import ProposalAppliedWorkerView, ProposalApplyView
from workerhire.views import WorkerHire, WorkerRejectView
urlpatterns = [
    path('apply/<int:id>/',  ProposalApplyView.as_view() ), #proposal Apply  -> id = jobreq id
    path('list/<int:id>/',  ProposalAppliedWorkerView.as_view() ), #proposal Listing -> -> id = jobreq id
    path('hire/<int:id>/<int:jobid>/',  WorkerHire.as_view() ), #id = proposal id, jobid = job oid
    path('reject/<int:id>/',  WorkerRejectView.as_view() ), #id = proposal id, jobid = job oid
]