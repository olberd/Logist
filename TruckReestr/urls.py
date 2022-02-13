from django.urls import path, include
from django.views.generic import TemplateView

from TruckReestr.views import AboutView, MyView, TripsListView, TripCreate, TripDetailView, TripDeleteView, \
    TripUpdateView

# app_name = 'TruckReestr'

urlpatterns = [
    path('about2/', AboutView.as_view()),
    path('', TripsListView.as_view(), name='trips'),
    path('tripnew/', TripCreate.as_view(), name='tripnew'),
    path('trips/<int:pk>', TripDetailView.as_view(), name='tripdetail'),
    path('update/<int:pk>', TripUpdateView.as_view(), name='tripupdate'),
    path('delete/<int:pk>', TripDeleteView.as_view(), name='tripdelete'),

]
