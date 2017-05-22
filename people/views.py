from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from people.models import User
from people.serializers import UserSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_staff=False, is_active=True)
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdminUser,)

    @list_route(methods=['post'], permission_classes=(AllowAny,))
    def register(self, request):
        try:
            User.objects.get_by_natural_key(request.data['username'])
        except User.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except KeyError:
            return Response({'Error': 'Wrong parameters'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response({'Error': 'This username already exists'}, status=status.HTTP_400_BAD_REQUEST)
