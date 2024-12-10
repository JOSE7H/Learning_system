from django.contrib.auth.models import User
from django.db import models

from students.models import Student


# Create your models here.
class Parent(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(Student,  'Parent')

    def __str__(self):
        return self.name
    def get_child_classes(self):
        return ",".join(set(child.assigned_class for child in self.children.all()))
