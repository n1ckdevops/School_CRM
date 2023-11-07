from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from students.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('students/', include('students.urls', namespace='students')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
