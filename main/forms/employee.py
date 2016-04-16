from django import forms
from main.models import Employee

class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'pin')
        