from django.urls import path

from students import views

urlpatterns = [
    path('',views.student_dashboard,name='student_dashboard'),
    path('students/<int:roll_number>',views.students_details,name='student_details'),
    # path('students/<int:student_id>',views.delete_student,name='delete_student'),
    path('students/<int:student_id>',views.student_dashboard,name='student_dashboard'),
    # path('students/<int:roll_number>',views.edit_student,name='edit_student'),
]