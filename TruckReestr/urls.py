from django import views
from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from TruckReestr.views import AboutView, MyView, TripsListView, TripCreate, TripDetailView, TripDeleteView, \
    TripUpdateView, DriverListView, DriverUpdateView, DriverCreateView, DriverDetailView, DriverDeleteView

# app_name = 'TruckReestr'

urlpatterns = [
    path('about2/', AboutView.as_view()),
    path('', TripsListView.as_view(), name='trips'),
    # path('tripnew/', TripCreate.as_view(), name='tripnew'),
    path('tripnew/', views.new_trip, name='tripnew'),
    path('trips/<int:pk>', TripDetailView.as_view(), name='tripdetail'),
    # path('update/<int:pk>', TripUpdateView.as_view(), name='tripupdate'),
    path('delete/<int:pk>', TripDeleteView.as_view(), name='tripdelete'),
    path('drivers/', DriverListView.as_view(), name='drivers'),
    path('drivernew/', DriverCreateView.as_view(), name='drivernew'),
    path('drivers/detail/<int:pk>', DriverDetailView.as_view(), name='driver_detail'),
    path('driver/update/<int:pk>', DriverUpdateView.as_view(), name='driver_update'),
    path('driver/delete/<int:pk>', DriverDeleteView.as_view(), name='driver_delete'),
    path('update/<int:trip_id>', views.manage_trips, name='tripupdate'),



]
