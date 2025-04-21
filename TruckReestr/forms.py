from django import forms
# from multiupload.fields import MultiFileField
from django.forms import ModelForm, inlineformset_factory

from .models import Trip, Files


class MultiFileForm(forms.Form):
    def save(self, trip, commit=True):
        for file in self.cleaned_data['files']:
            Files.objects.create(trip=trip, file=file)
        return trip


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = 'our_company', 'company', 'trip_date', 'trip_time', 'trip_from', 'trip_to', 'type_auto', \
            'trip_cost', 'driver', 'truck'

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class FilesForm(ModelForm):

    class Meta:
        model = Files
        fields = ('doc',)
        # widgets = {
        # doc = forms.FileField(attrs={'title': 'Your name'})
        #     'doc': forms.FileField(attrs={'multiple': 'multiple'}),
        # }


TripFormSet = inlineformset_factory(Trip, Files, fields=['doc'], extra=1)


class TripFormProbe(ModelForm):
    class Meta:
        model = Trip
        fields = ['trip_date', 'trip_from', 'trip_to', 'trip_cost']


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            "all": ["pretty.css"],
        }
        js = ["animations.js", "actions.js"]
