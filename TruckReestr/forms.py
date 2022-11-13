from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import Trip


class UploadFileForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
                    'media': ClearableFileInput(attrs={'multiple': True})
                  }
