from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from TruckReestr.models import Trip, Driver, Files
from .forms import TripForm, FilesForm, TripFormProbe, TripFormSet


# def manage_trips(request, pk):
#     trip_instance = get_object_or_404(Trip, pk=pk)
#     # TripFormSet = formset_factory(TripForm, can_delete=True)
#     FileFormSet = formset_factory(FilesForm, extra=2)
#     if request.method == 'POST':
#         # trip_formset = TripFormSet(request.POST, request.FILES, prefix='trips')
#         trip_form = TripFormProbe(request.POST, prefix='trip')
#         files_formset = FileFormSet(request.POST, request.FILES, prefix='files')
#         if trip_form.is_valid() and files_formset.is_valid():
#             # obj = Trip()
#             # obj.driver = trip_form.cleaned_data['driver']
#             trip_form.save(commit=False)
#             for form in files_formset:
#                 form.save()
#             trip_form.save()
#     else:
#         trip_form = TripFormProbe(prefix='trips')
#         files_formset = FileFormSet(prefix='files')
#     return render(request, 'TruckReestr/manage_trips.html', {
#         'trip_form': trip_form,
#         'files_formset': files_formset,
#     })


def manage_trips(request, pk):
    # trip_instance = get_object_or_404(Trip)
    trip_instance = Trip.objects.get(id=pk)
    form_trip = TripForm(instance=trip_instance)
    TripFormSet = inlineformset_factory(Trip, Files, fields=['doc'], extra=1)
    if request.method == 'POST':
        form_trip = TripForm(request.POST, instance=trip_instance) # , prefix="trip"
        formset = TripFormSet(request.POST or None, request.FILES or None, instance=trip_instance)
        if formset.is_valid() and form_trip.is_valid():
            form_trip.save()
            formset.save()

        return redirect(reverse('trips'))
    else:
        formset = TripFormSet(instance=trip_instance)
    return render(request, 'TruckReestr/manage_trips.html', {
        'form_trip': form_trip,
        'formset': formset,
    })


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
    formset_class = TripFormSet
    fields = ['trip_date', 'trip_time', 'trip_from', 'trip_to', 'type_auto', 'trip_cost', 'driver', 'truck']
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

