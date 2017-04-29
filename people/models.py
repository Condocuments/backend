from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


def validate_ssn(text):
    assert len(text) == 10, 'Length of SSN must be 10'


class User(AbstractUser):
    ssn = models.CharField(_('SSN'), max_length=15, blank=True, unique=True, validators=[validate_ssn, ], null=True)
    license = models.CharField(_('ID or License'), max_length=20, blank=True, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(verbose_name=_('Profile Picture'), upload_to='Profile', blank=True, null=True)

    def __str__(self):
        return self.username
