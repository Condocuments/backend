"""condocument_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import response, schemas
from rest_framework import routers, renderers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.authtoken import views

from condocument_settings import settings
from condos.views import CondoViewSet, AddressViewSet, UnitViewSet
from people.views import UserViewSet


def merge_strings(string, merge):
    """Merges simple strings."""
    return string % merge


admin.site.site_header = settings.ADMIN_TITLE


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Condocuments API')
    return response.Response(generator.get_schema(request=request))


router = routers.DefaultRouter(trailing_slash=False)
router.register(merge_strings(r'%s', 'condos'), CondoViewSet)
router.register(merge_strings(r'%s', 'unit'), UnitViewSet)
router.register(merge_strings(r'%s', 'address'), AddressViewSet)
router.register(merge_strings(r'%s', 'users'), UserViewSet, base_name='users')

API_VERSION = 'v1'

urlpatterns = [
    url('^$', schema_view),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/%s/' % API_VERSION, include(router.urls)),
    url(r'^admin/', include('loginas.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:  # only for testing purposes
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
