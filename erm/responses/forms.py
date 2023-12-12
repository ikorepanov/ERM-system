from django import forms
from .models import JobApplication, Response


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['date_applied', 'company_name', 'resume', 'cover_letter']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('user', 'employer', 'position', 'employercontact')
