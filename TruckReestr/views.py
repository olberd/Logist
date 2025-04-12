from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from TruckReestr.models import Trip, Driver, Files
from .forms import TripForm, FilesForm, TripFormProbe


def new_trip(request):
    TripFormSet = inlineformset_factory(Trip, Files, fields=['name', 'doc'], extra=1)
    if request.method == 'POST':
        form_trip = TripForm(request.POST) # , prefix="trip"
        formset = TripFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid() and form_trip.is_valid():
            trip = form_trip.save()

            formset_instance = formset.save(commit=False)
            for formset in formset_instance:
                formset.trip = trip
                formset.save()
            return redirect(reverse('trips'))
    else:
        form_trip = TripForm()
        formset = TripFormSet()
    return render(request, 'TruckReestr/manage_trips.html', {
        'form_trip': form_trip,
        'formset': formset,
    })


def manage_trips(request, pk):
    # trip_instance = get_object_or_404(Trip)
    trip_instance = Trip.objects.get(id=pk)
    form_trip = TripForm(instance=trip_instance)
    TripFormSet = inlineformset_factory(Trip, Files, fields=['name', 'doc'], extra=1)
    if request.method == 'POST':
        form_trip = TripForm(request.POST, instance=trip_instance) # , prefix="trip"
        formset = TripFormSet(request.POST or None, request.FILES or None, instance=trip_instance)
        if formset.is_valid() and form_trip.is_valid():
            form_trip.save()
            formset.save()

        return redirect(reverse('trips'))
    else:
        form_trip = TripForm(instance=trip_instance)
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
    form_class = TripForm
    template_name = 'TruckReestr/trip_form.html'
    # fields = ['trip_date', 'trip_time', 'trip_from', 'trip_to', 'type_auto', 'trip_cost', 'driver', 'truck']
    success_url = "/"

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     inlines_form = TripFormSet()
    #     return self.render_to_response(self.get_context_data(
    #         form=form,
    #         inlines=inlines_form
    #     ))

    def form_valid(self, form):
        # self.object = form.save()
        # inlines_form.instance = self.object
        # inlines_form.save()
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, *args, **kwargs):
        ctx = super(TripCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = TripForm(self.request.POST)
            ctx['inlines'] = TripFormSet(self.request.POST)
        else:
            ctx['form'] = TripForm()
            ctx['inlines'] = TripFormSet()
        return ctx


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

