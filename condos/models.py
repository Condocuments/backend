from django.db import models
from django.utils.translation import ugettext_lazy as _

from condocument_settings.helpers.enum import Types

_types = [
    ('LEASE', 'Lease'),
    ('BUY', 'Buy'),
    ('BOTH', 'Both')
]


class Condo(models.Model):
    class Meta:
        verbose_name = _('Condo')
        verbose_name_plural = _('Condos')

    name = models.CharField(verbose_name=_('Name'), max_length=100)
    address = models.OneToOneField(to='Address', verbose_name=_('Address'), related_name='condo', blank=True, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')

    line_1 = models.CharField(verbose_name=_('Line 1'), max_length=150)
    apt = models.CharField(verbose_name=_('Apt'), max_length=10, blank=True, null=True)
    city = models.CharField(verbose_name=_('City'), default='Miami', max_length=40)
    state = models.CharField(verbose_name=_('State'), default='FL', max_length=20)
    zip_code = models.IntegerField(verbose_name=_('Zip Code'))
    area = models.CharField(verbose_name=_('Area'), max_length=30, blank=True, null=True)

    def __str__(self):
        return self.line_1 + ' ' + self.apt if self.apt else '' + ', ' + str(self.city) + ', ' + str(
            self.state) + ' ' + str(self.zip_code)


class Application(models.Model):
    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

    pdf = models.FileField(verbose_name=_('PDF'), upload_to='PDF')
    type = models.CharField(verbose_name=_('Type'), choices=Types.choices(), max_length=10, default=Types.BOTH)
    code = models.TextField(verbose_name=_('Code'), blank=True, null=True)
    condo = models.ForeignKey(to=Condo, verbose_name=_('Condo'), related_name='applications', blank=True, null=True)

    def __str__(self):
        return '-'.join((self.condo.name, self.type))


