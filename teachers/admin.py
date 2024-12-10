from django.contrib import admin
from django.contrib.admin import AdminSite

from teachers.models import Teacher, Subject, Mark

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)


