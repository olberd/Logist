from django.contrib import admin

# Register your models here.
from TruckReestr.models import Trip, Driver, Truck, Files, Company, OurCompany


class FilesInline(admin.StackedInline):
    model = Files
    list_display = ('doc',)
    extra = 3


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = 'name', 'doc'


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_date', 'trip_time', 'trip_from', 'trip_to', 'driver', 'truck', 'trip_cost', 'company')
    search_fields = ('trip_date', 'driver', 'truck',)
    inlines = [FilesInline]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    fields = ('name', 'passport_ser', 'passport_no', 'passport_issued', 'passport_date',
              'driver_license_ser', 'driver_license_no', 'driver_license_date', 'phone', 'number_auto')
    list_display = ('name', 'passport_ser', 'passport_no', 'passport_issued', 'passport_date',
                    'driver_license_ser', 'driver_license_no', 'driver_license_date', 'phone', 'number_auto')


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('number_auto', 'brand_auto', 'type_auto',)


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ('name', 'name_full')


@admin.register(OurCompany)
class OurCompany(admin.ModelAdmin):
    list_display = ('name', 'name_full')




