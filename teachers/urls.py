from django.urls import path

from teachers import views

urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
    path('upload/students', views.upload_marks, name='upload_marks'),

]