from django.contrib import admin
from django.contrib.admin import AdminSite

from teachers.models import Teacher, Subject, Mark

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)


class CustomAdminSite(AdminSite):
    site_header = 'Teachers Admin Site'
    site_title = 'Teachers Admin Site'