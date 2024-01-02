from django import forms
from .models import Response, Employer


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['user', 'employer', 'position']


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
