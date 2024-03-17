
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('registration.urls')),
    path('api/job/', include('jobposting.urls')),
    path('api/worker/gig/',include('gig.urls')),
    path('api/worker/proposal/',include('proposal.urls')),
    path('api/category/',include('category.urls')),
    path('api/work/', include('currentwork.urls')),
    path('api/gig/', include('gighire.urls')),
    path('api/admin/', include('admin.urls')),
    path('api/admin/brand/', include('brand.urls')),

]
