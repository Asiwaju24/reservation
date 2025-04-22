from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'reservation_datetime', 'service']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'})
    )
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    reservation_datetime = forms.DateTimeField(
        widget= forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'})
    )