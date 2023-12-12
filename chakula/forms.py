from django import forms
from chakula.models import reservations


class reservationForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'phone_number', 'email', 'number_of_persons', 'booking_date']
