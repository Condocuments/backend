from rest_framework.serializers import ModelSerializer

from people.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        lookup_field = 'username'

        exclude = (
            'groups',
            'is_staff',
            'is_superuser',
            'user_permissions',
            'password',
            'is_active',
            'date_joined',
            'birth_date'
        )
        extra_kwargs = {
            'url': {'lookup_field': 'username'},
            'ssn': {'write_only': True},
            'license': {'write_only': True},
        }
