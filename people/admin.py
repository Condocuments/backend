from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from django.contrib.auth.admin import UserAdmin
from contents.models import Content
from people.forms import PersonAdminForm
from people.models import User


# Register your models here.


class ContentAdmin(admin.StackedInline):
    model = Content
    extra = 3


class IUserAdmin(UserAdmin):
    form = PersonAdminForm
    list_display = ('username', 'first_name', 'last_name', 'ssn', 'license')
    inlines = [ContentAdmin, ]

    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'username',
                'email',
                'ssn',
                'license',
                'birth_date',
                'profile_picture',
                'is_active',
            ),
        }),
        (None, {
            'fields': (
                'password1',
                'password2',
                'password',
            )
        }),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': (
                'is_staff',
                'is_superuser',
                'user_permissions',
                'groups',
            )
        }),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('last_login',),
        }),
    )

    list_filter = ('is_active', 'is_staff', 'is_superuser')

    def get_fieldsets(self, request, obj=None):
        return self.fieldsets

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        defaults.update(kwargs)
        return super(UserAdmin, self).get_form(request, obj, **defaults)


admin.site.register(User, IUserAdmin)
TokenAdmin.raw_id_fields = ('user',)
