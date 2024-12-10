from django.contrib.auth.models import User
from django.db import models

from students.models import Student


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    is_core = models.BooleanField(default=False)

    def __str__(self):
        subject_type = "Core" if self.is_core else "Elective"
        return self.name

class Teacher(models.Model):
    CLASS_CHOICES = [
        ('Form 1', 'Form 1'),
        ('Form 2', 'Form 2'),
        ('Form 3', 'Form 3'),
        ('Form 4', 'Form 4'),
    ]
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50,default='')
    subject=models.ManyToManyField(Subject)
    assigned_classes = models.CharField(max_length=10, choices=CLASS_CHOICES)

    def __str__(self):
        return self.full_name

class Mark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.FloatField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student}-{self.subject} ({self.marks})"
