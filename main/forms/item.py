from django import forms
from main.models import Item

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'category', 'price')
        