from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.models import ModelForm
from people.models import User
from django.utils.translation import ugettext_lazy as _


class PersonAdminForm(ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput, strip=False,
                                help_text=_("Enter the same password as before, for verification."))

    password = ReadOnlyPasswordHashField(label=_("Password"),
                                         help_text=_("Raw passwords are not stored, so there is no way to see "
                                                     "this user's password, but you can change the password "
                                                     "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['password1'].widget = forms.HiddenInput()
            self.fields['password1'].required = False
            self.fields['password2'].widget = forms.HiddenInput()
            self.fields['password2'].required = False
        else:
            self.fields['password'].widget = forms.HiddenInput()

    def clean_password(self):
        return self.initial.get("password")

    def clean_password2(self):
        if not self.instance.pk:
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            self.instance.username = self.cleaned_data.get('username')
            password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
            return password2

    def save(self, *args, **kwargs):
        person = super(PersonAdminForm, self).save(*args, **kwargs)
        password = self.cleaned_data.get('password1', None)
        if password:
            person.set_password(password)
            person.save()
        return person
