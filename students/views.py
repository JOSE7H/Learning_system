from gc import get_objects

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from students.models import Student
from teachers.models import Mark


# Create your views here.
@login_required
def student_dashboard(request):
    students = Student.objects.all()

    return render(request, 'student_dashboard.html', {'students': students})

@login_required
def students_details(request,roll_number ):

    school_info={'school_name':"EduQuant School",'school_address':"1234 jydy , Metai, syndey",'school_contact':"xxxxxxxxxxxx"}


    student = get_object_or_404(Student, roll_number=roll_number)
    marks=Mark.objects.filter(student = student)

    return render(request,'student_details.html',{'student':student,'marks':marks,**school_info})


def delete_student(request,student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
       student.delete()
       messages.success(request,f"student {student.first_name} deleted successfully")
       return redirect('student_dashboard')

class EditStudentView(UpdateView):
    model = Student
    template_name = 'edit_student.html'
    fields = ['first_name', 'last_name', 'roll_number','class_name']
    success_url = reverse_lazy('student_dashboard')


def edit_student(request,student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.roll_number = request.POST['roll_number']
        student.class_name = request.POST['class_name']
        student.save()
        return render(request, 'edit_student.html', {'student':student})
