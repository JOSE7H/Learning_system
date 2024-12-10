from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from parents.forms import ParentRegistrationForm
from parents.models import Parent


# Create your views here.
@login_required

def view_marks(request):
    parent = Parent.objects.get(user=request.user)
    children = parent.children.all()
    context = {'children': children}
    return render(request,'view_marks.html',context)

def register_parent(request, user=None):

    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            user = user.objects.create_user(form.cleaned_data['username'],password=form.cleaned_data['password'])
            parent = Parent.objects.create(user=user)

            parent.children.set(form.cleaned_data['children'])
            parent.save()
            login(request, user)
            return redirect('view_marks')
    else:
        form = ParentRegistrationForm()
        return render(request,'register_parent.html',{'form':form})

