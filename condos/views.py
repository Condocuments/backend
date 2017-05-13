from django.db.models import Q
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from condos.models import Condo, Unit, Address
from condos.serializers import CondoSerializer, UnitSerializer, AddressSerializer


# Create your views here.


class CondoViewSet(ModelViewSet):
    queryset = Condo.objects.all()
    serializer_class = CondoSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @list_route(methods=['get'])
    def search(self, request, query=None):
        query = query or self.request.query_params['query']
        words = query.strip().split()
        condos = []
        for word in words:
            condos_temp = Condo.objects.filter(
                Q(name__icontains=word) | Q(location__icontains=word) | Q(county__icontains=word))

            address = Address.objects.filter(
                Q(line_1__icontains=word) | Q(city__icontains=word) | Q(state__icontains=word) | Q(
                    zip_code__icontains=word) | Q(area__icontains=word))
            for condo in condos_temp:
                condos.append(condo)
            for add in address:
                condos.append(add.condo)
            break

        serializer = CondoSerializer(condos, context={'request': request}, many=True)
        if serializer.data:
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response([{}], status=HTTP_200_OK)

    @detail_route(methods=['get'])
    def unit(self, request, slug=None):
        try:
            condo = Condo.objects.get(slug=slug)
        except Condo.DoesNotExist:
            return Response("Condo not Found", status=HTTP_400_BAD_REQUEST)
        units = Unit.objects.filter(condo=condo)
        serializer = UnitSerializer(units, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    lookup_field = 'mls_number'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
