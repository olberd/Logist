from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from TruckReestr.models import Trip, Driver
from .forms import UploadFileForm


class AboutView(TemplateView):
    template_name = "about.html"


class MyView(View):
    def get(self, request):
        return HttpResponse('result')


class TripsListView(ListView):
    paginate_by = 20
    model = Trip
    context_object_name = 'trips'


class TripCreate(CreateView):
    model = Trip
    form_class = UploadFileForm
    # fields = ['trip_date', 'trip_time', 'trip_from', 'trip_to', 'type_auto', 'trip_cost', 'driver', 'truck', 'docs']
    success_url = "/"


class TripDetailView(DetailView):
    model = Trip


class TripUpdateView(UpdateView):
    model = Trip
    fields = ['trip_date', 'trip_time', 'trip_from', 'trip_to', 'type_auto', 'trip_cost', 'driver', 'truck']
    # template_name = '../templates/TruckReestr/trip_form.html'
    template_name = 'TruckReestr/trip_form.html'
    success_url = '/'


class TripDeleteView(DeleteView):
    model = Trip
    success_url = '/'


class DriverListView(ListView):
    paginate_by = 20
    model = Driver
    context_object_name = 'drivers'
    template_name = 'TruckReestr/driver_list.html'


class DriverCreateView(CreateView):
    model = Driver
    fields = ['name', 'passport_ser', 'passport_no', 'passport_issued', 'passport_date',
              'driver_license_ser', 'driver_license_no', 'driver_license_date', 'phone', 'number_auto']

    success_url = "/drivers/"


class DriverDetailView(DetailView):
    model = Driver


class DriverUpdateView(UpdateView):
    model = Driver
    fields = ['name', 'passport_ser', 'passport_no', 'passport_issued', 'passport_date',
              'driver_license_ser', 'driver_license_no', 'driver_license_date', 'phone', 'number_auto'
              ]

    template_name = 'TruckReestr/driver_form.html'
    success_url = '/drivers/'


class DriverDeleteView(DeleteView):
    model = Driver
    success_url = '/drivers/'

