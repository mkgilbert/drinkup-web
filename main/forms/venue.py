from django import forms
from main.models import Venue

class AddVenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ('phone', 'name', 'address', 'description', 'website', 'hours', 'service_type')
        