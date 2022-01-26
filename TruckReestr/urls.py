from django.urls import path, include
from django.views.generic import TemplateView

from TruckReestr.views import AboutView, MyView, TripsListView, TripCreate, TripDetailView

# app_name = 'TruckReestr'

urlpatterns = [
    path('about2/', AboutView.as_view()),
    path('trips/', TripsListView.as_view(), name='trips'),
    path('tripnew/', TripCreate.as_view(), name='tripnew'),
    path('trips/<int:pk>', TripDetailView.as_view(), name='TripDetailView'),

]
