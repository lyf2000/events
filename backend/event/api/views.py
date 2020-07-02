from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from .filters import PERIOD_CHOICES, get_curr_time
from .paginators import MyPaginator
from .serializers import EventSerializer
from ..models import Event


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = MyPaginator
    filter_backends = (SearchFilter, OrderingFilter)
    permission_classes = [IsAuthenticated]
    search_fields = ('title', 'text',)
    ordering = ('date',)

    def get_queryset(self):
        queryset = super().get_queryset()

        period = self.request.query_params.get('period', None)
        if period not in ['', None, 'all']:
            querie = Q(date__lte=PERIOD_CHOICES[period]()) & Q(date__gte=get_curr_time())

            queryset = queryset.filter(querie)
        user = self.request.user
        queryset = queryset.filter(author=user)
        return queryset
