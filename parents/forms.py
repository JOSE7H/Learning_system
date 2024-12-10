
from django import forms

from parents.models import Parent
from students.models import Student


class ParentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget=forms.PasswordInput)
    children = forms.ModelMultipleChoiceField(queryset=Student.objects.all(),
                                              widget=forms.CheckboxSelectMultiple,required= True,)
    class Meta:
        model = Parent
        fields = ['username', 'password', 'children']
