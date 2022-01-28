from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from TruckReestr.models import Trip


# Create your views here.


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
    fields = ['trip_date', 'trip_time', 'trip_from', 'trip_to', 'type_auto', 'trip_cost', 'driver', 'truck', ]
    success_url = "/trips"


class TripDetailView(DetailView):
    model = Trip
