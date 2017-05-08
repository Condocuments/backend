from rest_framework.serializers import ModelSerializer
from contents.models import Content


class ContentSerializer(ModelSerializer):
    class Meta:
        fields = ('info', 'description')
        model = Content
