from django.contrib import admin

# Register your models here.
from TruckReestr.models import Trip, Driver, Truck


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_date', 'trip_time', 'trip_from', 'trip_to', 'driver', 'truck', 'trip_cost')


# admin.site.register(Trip)
admin.site.register(Driver)
admin.site.register(Truck)

