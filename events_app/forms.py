from django import forms
from django.forms import ModelForm
from .models import Venue, Event


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = "__all__"   # It will take the all fields of venue model
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address') # For specific fields
        labels = {
            'name': "" ,
            'address': "" ,
            'zip_code':"", 
            'phone':"", 
            'web':"", 
            'email_address':""
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Address'}),
            'zip_code':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), 
            'phone':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), 
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website Address'}), 
            'email_address':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Adderss'})
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        # fields = "__all__"   # It will take the all fields of venue model
        fields = ('name','event_date', 'venue', 'manager','attendees','description' ) # For specific fields
        labels = {
            'name': "" ,
            'event_date': "YYYY-MM-DD HH:MM:SS" ,
            'venue':"", 
            'manager':"", 
            'attendees':"",
            'description':""
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose Vanue'}), 
            'manager':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Manager'}),  
            'attendees':forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'})
        }