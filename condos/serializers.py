from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from contents.serializers import ContentSerializer

from condos.models import Condo, Bedroom, BedroomQuantity, Address, Application, Unit


class BedroomSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bedroom


class AddressSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Address


class BedroomQuantitySerializer(ModelSerializer):
    bedroom = BedroomSerializer()

    class Meta:
        fields = '__all__'
        model = BedroomQuantity


class ApplicationSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Application


class CondoSerializer(ModelSerializer):
    slug = ReadOnlyField()
    condo_offer = BedroomQuantitySerializer(many=True)
    address = AddressSerializer()
    applications = ApplicationSerializer(many=True)
    condo_contents = ContentSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Condo
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class UnitSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Unit
        lookup_field = 'mls_number'
        extra_kwargs = {
            'url': {'lookup_field': 'mls_number'}
        }
