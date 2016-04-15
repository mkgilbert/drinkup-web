from django import forms
from main.models import Menu

class AddMenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('name', 'description')
        