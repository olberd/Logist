from django import forms
from django.forms import ModelForm, inlineformset_factory

from .models import Trip, Files


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True
#
#
# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)
#
#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = [single_file_clean(data, initial)]
#         return result
#
#
# class FileFieldForm(forms.Form):
#     file_field = MultipleFileField()


class FilesForm(ModelForm):

    class Meta:
        model = Files
        fields = '__all__'
        # widgets = {
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
