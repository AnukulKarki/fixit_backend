from django.urls import path
from .views import CurrentWorkerWorkView, startCurrentWorkerView, CancelCurrentWorkerView, CompleteCurrentWorkerView, PayWorkView, CurrentWorkerClientView, RatingView
urlpatterns = [
    path('current-work/', CurrentWorkerWorkView.as_view()),
    path('client/current-work/', CurrentWorkerClientView.as_view()),
    path('worker/cancel-work/<int:id>/', CancelCurrentWorkerView.as_view()),
    path('start-work/<int:id>/', startCurrentWorkerView.as_view()),
    path('complete-work/<int:id>/', CompleteCurrentWorkerView.as_view()),
    path('pay-work/<int:id>/', PayWorkView.as_view()),
    path('rate/<int:id>/', RatingView.as_view()),
]