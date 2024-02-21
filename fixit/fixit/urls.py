
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('registration.urls')),
    path('api/worker/job/', include('jobposting.urls')),
    path('api/worker/gig/',include('gig.urls'))
]
