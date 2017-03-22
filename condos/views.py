from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from condos.models import Condo, Unit, Address
from condos.serializers import CondoSerializer, UnitSerializer, AddressSerializer


# Create your views here.


class CondoViewSet(ModelViewSet):
    queryset = Condo.objects.all()
    serializer_class = CondoSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    lookup_field = 'mls_number'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
