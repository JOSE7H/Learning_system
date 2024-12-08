from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from teachers.forms import MarkForm
from teachers.models import Teacher


# Create your views here.
@login_required
def upload_marks(request):
    teachers = Teacher.objects.get(user=request.user)
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            mark = form.save(commit=False)
            mark.teacher = teachers
            mark.save()
            return redirect('teacher-dashboard')
        else:
            form = MarkForm()
            return render(request,'upload_marks.html',{'form':form})

def teacher_dashboard(request):
    teacher=Teacher.objects.get(user=request.user)
    context = {'teacher':teacher,
               'classes':teacher.assigned_classes.all,
               'subjects':teacher.assigned_subjects.all,
               }
    return render(request,'teacher_dashboard.html',context)

