from django import forms
from chakula.models import Reservation, message


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone_number', 'email', 'number_of_persons', 'booking_date']

class messageForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ['name', 'email', 'subject', 'description']
