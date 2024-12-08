from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.roll_number}'