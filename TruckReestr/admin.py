from django.contrib import admin

# Register your models here.
from TruckReestr.models import Trip, Driver, Truck


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_date', 'trip_time', 'trip_from', 'trip_to', 'driver', 'truck', 'trip_cost')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    fields = ('surname', 'name', 'second_name', 'passport_ser', 'passport_no', 'passport_issued', 'passport_date',
              'driver_license_ser', 'driver_license_no', 'driver_license_date', 'phone', 'number_auto')
    list_display = ('surname', 'name', 'second_name', 'passport_ser', 'passport_no', 'passport_issued', 'passport_date',
              'driver_license_ser', 'driver_license_no', 'driver_license_date', 'phone', 'number_auto')


# admin.site.register(Trip)
# admin.site.register(Driver)
# admin.site.register(Truck)

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('number_auto', 'brand_auto', 'type_auto',)