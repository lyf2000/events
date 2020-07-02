from django.urls import path
from rest_framework import routers

from event.api.views import EventViewSet

app_name = 'event-api'


router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='events-api')

urlpatterns = [
] + router.urls
