from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User

class IsAnonymous(IsAuthenticated):

    def has_permission(self, request, view):
        return not super(IsAnonymous, self).has_permission(request, view)


@api_view(['POST'])
@permission_classes([IsAnonymous])
def sign_up(request):
    data = request.data
    username = data['username']
    email = data['email']
    password = data['password']
    try:
        User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
    except Exception as e:
        print(e)
        return JsonResponse(status=405, data={'error': str(e)})
    return Response(status=201)
