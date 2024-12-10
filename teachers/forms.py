from students.models import Student
from teachers.models import Mark
from django.forms import forms

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['student','subject','mark']

        # def __init__(self, *args, **kwargs):
        #     teacher = kwargs.pop('teacher', None)
        #     super(MarkForm,self).__init__(*args, **kwargs)
        #     if teacher: self.fields['student'].queryset = Student.objects.filter(classroom__teacher=teacher)
        #     self.fields['subject'].queryset = teacher.assigned_subjects.all()