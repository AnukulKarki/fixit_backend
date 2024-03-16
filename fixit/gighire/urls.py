from django.urls import path
from .views import GigProposalApplyView, GigProposalListview, GigProposalAcceptView, GigProposalRejectView, CurrentGigWorkView, CurrentGigWorkClientView, GigWorkStartView, GigWorkCompleteView, GigWorkCancelView, GigWorkPayView, RatingView
#api/gig/
urlpatterns = [
    path('proposal/<int:id>/', GigProposalApplyView.as_view()), #id -> worker
    path('list/', GigProposalListview.as_view()),
    path('proposal/accept/<int:id>/', GigProposalAcceptView.as_view()),#id = proposal id
    path('proposal/reject/<int:id>/', GigProposalRejectView.as_view()),#id = proposal id
    path('current-work/', CurrentGigWorkView.as_view()),
    path('current-work/client/', CurrentGigWorkClientView.as_view()),
    path('work/start/<int:id>/', GigWorkStartView.as_view()),
    path('work/complete/<int:id>/', GigWorkCompleteView.as_view()),
    path('work/cancel/<int:id>/', GigWorkCancelView.as_view()),
    path('work/pay/<int:id>/', GigWorkPayView.as_view()),
    path('work/rating/<int:id>/', RatingView.as_view()),
]