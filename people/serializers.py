from rest_framework.serializers import ModelSerializer

from people.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        lookup_field = 'username'
        fields = '__all__'

        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
