from teachers.models import Mark
from django.forms import forms

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['student','subject','mark']