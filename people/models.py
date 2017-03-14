from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


def validate_ssn(text):
    assert len(text) == 10, 'Length of SSN must be 10'


class User(AbstractUser):
    ssn = models.TextField(_('SSN'), max_length=15, blank=True, unique=True, validators=[validate_ssn, ])
    license = models.TextField(_('ID or License'), max_length=20, blank=True, unique=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Content(models.Model):
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    info = models.FileField(verbose_name=_('Info'), upload_to='info')
    description = models.TextField(verbose_name=_('Description'), max_length=200, blank=True, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='contents')

    def __str__(self):
        return ' - '.join((self.user.username, self.pk))
