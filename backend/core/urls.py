from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

# from rest_framework_swagger.views import get_swagger_view
from . import settings

api_urlpatterns = [
    path('api/', include('event.api.urls')),
    path('api/', include('users.api.urls')),

]

urlpatterns = [
                  path('admin/', admin.site.urls),

              ] + api_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
