from django import forms
from django.forms import ModelForm, inlineformset_factory, ClearableFileInput

from .models import Trip, Files


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


class FilesForm(ModelForm):
    # doc = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Files
        fields = '__all__'
        widgets = {
            'doc': ClearableFileInput(attrs={'multiple': True}),
        }


# TripFormSet = inlineformset_factory(Trip, Files, fields=['name', 'doc'], extra=2)


class TripFormProbe(ModelForm):
    class Meta:
        model = Trip
        fields = ['trip_date', 'trip_from', 'trip_to', 'trip_cost']
