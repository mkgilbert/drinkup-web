from django import forms
from main.models import Order

class ClaimOrder(forms.ModelForm):

    class Meta:
        model = Order
        fields = 'employee'
