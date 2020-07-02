from django.urls import path
from rest_framework import routers

# from users.api.views import UserViewSet
from users.api.tokens import TokenCreate, TokenRefresh
from users.api.views import sign_up

app_name = 'users-api'

router = routers.DefaultRouter()
# router.register('users', UserViewSet, basename='user-api')

urlpatterns = [
    path('signup', sign_up, name='sign_up'),
    path('token/', TokenCreate.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
    # path('users/follow/<int:pk>', follow_user, name='user-follow'),
] + router.urls

