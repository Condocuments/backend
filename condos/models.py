from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from condocument_settings.helpers.enum import Types, PropertyType

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
    slug = models.SlugField(verbose_name=_('Slug'), max_length=150)
    address = models.OneToOneField(to='Address', verbose_name=_('Address'), related_name='condo', blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=20, blank=True, null=True)
    location = models.CharField(verbose_name=_('Location'), max_length=20, blank=True, null=True)
    year = models.IntegerField(verbose_name=_('Year'), blank=True, null=True)
    story_number = models.IntegerField(_('Number of Stories'), blank=True, null=True)
    unit_number = models.IntegerField(_('Number of Units'), blank=True, null=True)
    parking_spaces = models.IntegerField(_('Parking Spaces'), blank=True, null=True)
    fitness_center = models.BooleanField(_('Fitness Center'), default=False)
    pets = models.BooleanField(_('Pets'), default=False)
    valet_parking = models.BooleanField(_('Valet Parking'), default=False)
    pool = models.BooleanField(_('Pool'), default=False)
    market = models.CharField(_('Market'), max_length=100, blank=True, null=True)
    county = models.CharField(_('County'), max_length=60, blank=True, null=True)
    info = models.TextField(_('Info'), blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Condo, self).save(force_insert, force_update, using, update_fields)


class Unit(models.Model):
    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')

    number = models.CharField(_('Number'), max_length=100, db_index=True)
    mls_number = models.CharField(_('MLS Number'), max_length=50, db_index=True, unique=True)
    condo = models.ForeignKey(Condo, verbose_name=_('Condo'), related_name='units', blank=True, null=True)
    status = models.CharField('Status', max_length=10, blank=True, null=True)
    area = models.CharField('Area', max_length=30, blank=True, null=True)
    list_price = models.PositiveIntegerField(_('Price'), blank=True, null=True)
    beds = models.IntegerField(_('Beds'), blank=True, null=True)
    f_baths = models.IntegerField(_('FBaths'), blank=True, null=True)
    h_baths = models.IntegerField(_('HBaths'), blank=True, null=True)
    live_area = models.PositiveIntegerField(_('Live Area'), blank=True, null=True)
    association_fee = models.IntegerField(_('Association Fee'), blank=True, null=True)
    year = models.IntegerField(_('Year'), blank=True, null=True)
    garage_spot = models.IntegerField(_('Garage Spots'), blank=True, null=True)
    pool = models.BooleanField(_('Pool'), default=False)
    waterfront = models.BooleanField(_('Waterfront'), default=False)
    current_price = models.IntegerField(_('Current Price'), blank=True, null=True)
    entry_date = models.DateField(_('Entry Date'), blank=True, null=True)
    days_market = models.IntegerField(_('Days on market'), blank=True, null=True)
    property_type = models.CharField(_('Property type'), choices=PropertyType.choices(), default=PropertyType.RENT,
                                     max_length=10)
    rent_period = models.CharField(_('Rent Period'), max_length=50, blank=True, null=True)
    furnished = models.BooleanField(_('Furnished'), default=False)

    def __str__(self):
        return (self.number + ' - ' + str(self.condo)) if self.condo else self.number


class Bedroom(models.Model):
    class Meta:
        verbose_name = _('Bedroom')
        verbose_name_plural = _('Bedroom')

    name = models.CharField(_('Name'), max_length=50)
    quantity = models.IntegerField(_('Quantity'), default=0)

    def __str__(self):
        return ' - '.join((self.name, str(self.quantity)))


class BedroomQuantity(models.Model):
    class Meta:
        verbose_name = _('Bedroom Quantity')
        verbose_name_plural = _('Bedroom Quantity')

    bedroom = models.ForeignKey(to=Bedroom, verbose_name=_('Bedroom'), related_name='bedroom_offer')
    condo = models.ForeignKey(to=Condo, verbose_name=_('Condo'), related_name='condo_offer')
    type = models.CharField(verbose_name=_('Type'), choices=PropertyType.choices(), max_length=10)
    quantity = models.IntegerField(verbose_name=_('Quantity'), default=0)

    def __str__(self):
        return '(%s : %s ) - %s' % (str(self.condo), str(self.bedroom), str(self.quantity))


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
        return self.line_1 + ' ' + (self.apt if self.apt else '') + ', ' + str(self.city) + ', ' + str(
            self.state) + ' ' + str(self.zip_code)


class Application(models.Model):
    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

    pdf = models.FileField(verbose_name=_('PDF'), upload_to='PDF', null=True, blank=True)
    type = models.CharField(verbose_name=_('Type'), choices=Types.choices(), max_length=10, default=Types.BOTH.value)
    code = models.TextField(verbose_name=_('Code'), blank=True, null=True)
    condo = models.ForeignKey(to=Condo, verbose_name=_('Condo'), related_name='applications', blank=True, null=True)

    def __str__(self):
        return '-'.join((self.condo.name, self.type))
