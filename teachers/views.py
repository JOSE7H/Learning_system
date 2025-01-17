from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import teachers
from teachers.forms import MarkForm
from teachers.models import Teacher


# Create your views here.
@login_required
def upload_marks(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            mark = form.save
            mark.teacher = teachers
            mark.save()
            return redirect('teacher-dashboard')
        else:
            form = MarkForm()
            return render(request,'upload_marks.html',{'form':form})

@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher_dashboard.html', context)
