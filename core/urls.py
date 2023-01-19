
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/',include('AuthHandler.urls')),
    path('',include('jobseeker.urls')),
    path('',include('company.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
