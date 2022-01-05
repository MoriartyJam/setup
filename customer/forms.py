from django.forms import ModelForm
from .models import Client
from django import forms
from django.utils.translation import gettext_lazy as _


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email']

    def clean_name(self):
        name = self.cleaned_data['name'].capitalize()

        if Client.objects.filter(name=name).exists():
            raise forms.ValidationError('')

        return name
