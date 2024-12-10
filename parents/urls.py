from django.urls import path

from parents import views

urlpatterns = [
    path('view-marks', views.view_marks, name='view-marks'),
    path('register', views.register_parent, name='register-parent'),
]