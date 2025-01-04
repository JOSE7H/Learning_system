from django.core.management import BaseCommand

from teachers.models import Teacher


class Command(BaseCommand):
    def handle(self, *args, **options):
        teachers=[{"full_name":"John MaNga","subject":"English","assigned_class":"Form 1"}]
        for t in teachers:
            teacher = Teacher(**t)
            teacher.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated.'))