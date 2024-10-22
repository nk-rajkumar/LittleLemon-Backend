from django import forms
from .models import Booking
from django.forms.widgets import DateInput, TimeInput
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'guest_number', 'comment', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': DateInput(attrs={'type': 'date', 'min': datetime.date.today()}, format='%Y-%m-%d'),
            'booking_time': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date'].widget.attrs['min'] = datetime.date.today().strftime('%Y-%m-%d')
