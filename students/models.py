from django.contrib.auth.models import User
from django.db import models




# Create your models here.
class Student(models.Model):
    CLASS_CHOICES =[
        ('Form 1', 'Form 1'),
        ('Form 2', 'Form 2'),
        ('Form 3', 'Form 3'),
        ('Form 4', 'Form 4'),

    ]
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES)



    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.roll_number}'