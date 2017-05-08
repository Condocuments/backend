from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from condocument_settings.helpers.enum import ContentType
from condos.models import Condo


# Create your models here.


class Content(models.Model):
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    info = models.FileField(verbose_name=_('Info'), upload_to='info')
    description = models.TextField(verbose_name=_('Description'), max_length=200, blank=True, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='user_contents',
                             null=True,
                             blank=True)
    condo = models.ForeignKey(to=Condo, verbose_name=_('Condo'), related_name='condo_contents', blank=True, null=True)
    type = models.CharField(verbose_name=_('Type'), choices=ContentType.choices(), max_length=10,
                            default=ContentType.CONDO)

    def __str__(self):
        return ' - '.join((str(self.type), str(self.pk)))
