from django.contrib import admin

from people.models import User
from contents.models import Content


# Register your models here.


class ContentAdmin(admin.StackedInline):
    model = Content
    extra = 3


class UserAdmin(admin.ModelAdmin):
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


admin.site.register(User, UserAdmin)
