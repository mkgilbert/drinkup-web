from django import forms
from main.models import Venue

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','phone', 'description', 'website', 'hours', 'service_type')