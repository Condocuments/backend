from django.contrib import admin

from condos.models import Condo, Address, Application, BedroomQuantity, Unit


# Register your models here.


class ApplicationAdmin(admin.StackedInline):
    model = Application
    extra = 1


class BedroomQuantityAdmin(admin.StackedInline):
    model = BedroomQuantity
    extra = 3


class CondoAdmin(admin.ModelAdmin):
    list_filter = ('name', 'address')
    list_display = ('name', 'address')
    inlines = [BedroomQuantityAdmin, ApplicationAdmin]


class UnitAdmin(admin.ModelAdmin):
    list_display = ['number', 'condo']


admin.site.register(Condo, CondoAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Address)
