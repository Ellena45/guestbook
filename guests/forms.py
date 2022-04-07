from django.db import models
from django.forms import ModelForm
from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'companyname', 'email', 'consultant')


        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vorname'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nachname'}),
            'companyname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firmenname'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'consultant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bei wem zu Besuch'}),
        }


