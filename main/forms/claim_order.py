from django import forms
from main.models import Employee, Order


class ClaimOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('__all__')
