from django.urls import path

from teachers import views

urlpatterns = [
    path('upload-marks', views.upload_marks, name='upload_marks'),
]