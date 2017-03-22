from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from people.models import User
from people.serializers import UserSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_staff=False, is_active=True)
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAuthenticated,)
